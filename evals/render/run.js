#!/usr/bin/env node
"use strict";

/**
 * Render eval runner (D8): what a generated surface actually contains, counted.
 *
 *   node evals/render/run.js <outputs-dir> [--model <name>] [--note <text>]
 *                            [--write] [--results <RESULTS.md>] [--json]
 *
 * <outputs-dir> holds one directory per brief in briefs.json, named by its id,
 * each with the rendered source and the director record the run produced
 * (director-record.md). For every brief this runs the project linter
 * (bin/lint.js, the machine half of SLOP_MARKERS.md) and the record validator
 * (bin/record.js), and scores the G items of ADA_RUBRIC.md that can be read
 * from source alone. Everything else is NOT_RUN, by name, never PASS.
 *
 * What it does NOT do: generate. Producing the outputs is a model run, made by
 * hand in fresh sessions (evals/render/README.md); CI only proves this runner
 * on the committed sample. --write appends one dated row, with its method, to
 * test/evals/RESULTS.md.
 *
 * Exit: 0 the run completed (findings are results, not failures); 2 usage.
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..", "..");
const lint = require(path.join(ROOT, "bin", "lint.js"));
const record = require(path.join(ROOT, "bin", "record.js"));
const BRIEFS = JSON.parse(fs.readFileSync(path.join(__dirname, "briefs.json"), "utf8")).briefs;
const PKG = JSON.parse(fs.readFileSync(path.join(ROOT, "package.json"), "utf8"));

// The G items of ADA_RUBRIC.md, and the ones this runner can decide from source.
const G_ITEMS = ["R1", "R3", "R4", "R5", "R8", "R9", "R12", "R13", "R14", "R15", "R16", "R17", "R19", "R20", "R22", "R24"];
const FROM_SOURCE = ["R8", "R20", "R24"];
const MOTION = /\b(?:transition|animation)\s*:|@keyframes|\bmotion\.|whileInView|animate=/;

function parseArgs(argv) {
  const o = { dir: null, model: "NOT_RUN", note: "", write: false, results: path.join(ROOT, "test", "evals", "RESULTS.md"), json: false, error: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const val = () => {
      const v = argv[++i];
      if (!v || v.startsWith("--")) o.error = `${a} needs a value`;
      return v;
    };
    if (a === "--model") o.model = val();
    else if (a === "--note") o.note = val();
    else if (a === "--results") o.results = path.resolve(val() || "");
    else if (a === "--write") o.write = true;
    else if (a === "--json") o.json = true;
    else if (a.startsWith("--")) o.error = `unknown argument: ${a}`;
    else if (!o.dir) o.dir = a;
    else o.error = `one outputs directory, not two (${a})`;
  }
  if (!o.error && !o.dir) o.error = "give the directory holding one output directory per brief";
  return o;
}

function scoreBrief(brief, dir) {
  const out = { id: brief.id, surface_class: brief.surface_class, present: false };
  let st = null;
  try { st = fs.statSync(dir); } catch (e) { st = null; }
  if (!st || !st.isDirectory()) return out;
  out.present = true;

  const { files } = lint.walk(dir, false);
  out.files = files.length;
  const floor = files.length ? lint.lintFiles(files, { ratchet: false }) : { findings: [], waived: 0 };
  const sev = { S1: 0, S2: 0, S3: 0 };
  for (const f of floor.findings) sev[f.severity]++;
  out.severity = sev;
  out.waived = floor.waived;
  out.markers = [...new Set(floor.findings.map((f) => f.id))].sort();

  const recPath = path.join(dir, "director-record.md");
  let rec = null;
  if (fs.existsSync(recPath)) {
    rec = record.checkRecord(fs.readFileSync(recPath, "utf8"));
    out.record = { valid: rec.valid, surface_class: rec.surface_class, violations: rec.violations.map((v) => `${v.field}: ${v.problem}`) };
  } else {
    out.record = { valid: false, missing: true, violations: ["director-record.md: missing"] };
  }

  // G items from source. Each verdict says what it read, so a source-level PASS
  // is never mistaken for the rendered check the rubric names.
  const g = {};
  const raw = files.length ? lint.lintFiles(files, { ratchet: true }).findings.filter((f) => f.rule === "raw-color") : [];
  g.R8 = files.length ? { verdict: raw.length ? "FAIL" : "PASS", basis: `lint raw-color: ${raw.length}` } : { verdict: "NOT_RUN", basis: "no source" };
  const moves = files.some((f) => MOTION.test(f.text));
  const noRm = floor.findings.filter((f) => f.rule === "no-reduced-motion").length;
  g.R20 = !moves ? { verdict: "N/A", basis: "no motion in source" }
    : { verdict: noRm ? "FAIL" : "PASS", basis: `source only: reduced-motion branch ${noRm ? "missing" : "present"}; not toggled in a browser` };
  const surfaces = rec && !rec.declined ? record.parse(fs.readFileSync(recPath, "utf8")).sections.get("Surfaces") : undefined;
  g.R24 = brief.surface_class !== "flagship" ? { verdict: "N/A", basis: "not a flagship" }
    : { verdict: surfaces && surfaces.replace(/\s/g, "") ? "PASS" : "FAIL", basis: "the record's Surfaces field" };
  for (const id of G_ITEMS) if (!g[id]) g[id] = { verdict: "NOT_RUN", basis: "needs a browser, a simulator or a scenario run" };
  out.g = g;
  return out;
}

function summarise(rows) {
  const present = rows.filter((r) => r.present);
  const sev = { S1: 0, S2: 0, S3: 0 };
  let valid = 0;
  const g = { PASS: 0, FAIL: 0, "N/A": 0, NOT_RUN: 0 };
  for (const r of present) {
    for (const k of Object.keys(sev)) sev[k] += r.severity[k];
    if (r.record.valid) valid++;
    for (const id of FROM_SOURCE) g[r.g[id].verdict]++;
    g.NOT_RUN += G_ITEMS.length - FROM_SOURCE.length;
  }
  return { briefs: `${present.length}/${rows.length}`, sev, valid: `${valid}/${present.length}`, g };
}

function row(o, s, today) {
  const g = s.g;
  return `| ${today} | ${PKG.version} | \`${o.label}\` | ${o.model} | ${s.briefs} | ${s.sev.S1} / ${s.sev.S2} / ${s.sev.S3} | ${s.valid} | ${g.PASS} PASS / ${g.FAIL} FAIL / ${g["N/A"]} N/A / ${g.NOT_RUN} NOT_RUN | ${o.note || "—"} |`;
}

const HEADING = "## Render eval (D8)";
const TABLE_HEAD = [
  "| Date | Version | Outputs | Model | Briefs | S1 / S2 / S3 | Records valid | G items | Notes |",
  "|---|---|---|---|---|---|---|---|---|",
];

function appendRow(file, line) {
  let text = fs.readFileSync(file, "utf8");
  const at = text.indexOf(HEADING);
  if (at === -1) throw new Error(`${file} has no "${HEADING}" section — add it with its method before writing rows`);
  const head = text.indexOf(TABLE_HEAD[1], at);
  if (head === -1) throw new Error(`${file}: the ${HEADING} section has no table`);
  // The row goes after the last row of that table.
  let end = text.indexOf("\n", head) + 1;
  while (text.slice(end).startsWith("|")) end = text.indexOf("\n", end) + 1;
  text = text.slice(0, end) + line + "\n" + text.slice(end);
  fs.writeFileSync(file, text);
}

function main() {
  const o = parseArgs(process.argv.slice(2));
  if (o.error) {
    console.error(`render eval: ${o.error}\nusage: node evals/render/run.js <outputs-dir> [--model <name>] [--note <text>] [--write] [--results <file>] [--json]`);
    return 2;
  }
  const root = path.resolve(o.dir);
  if (!fs.existsSync(root) || !fs.statSync(root).isDirectory()) {
    console.error(`render eval: ${o.dir} is not a directory`);
    return 2;
  }
  o.label = path.relative(ROOT, root) || ".";
  const rows = BRIEFS.map((b) => scoreBrief(b, path.join(root, b.id)));
  const s = summarise(rows);
  const today = new Date().toISOString().slice(0, 10);

  if (o.json) console.log(JSON.stringify({ outputs: o.label, model: o.model, version: PKG.version, rows, summary: s }, null, 2));
  else {
    console.log(`render eval — ${o.label}, model ${o.model}, ${PKG.version}`);
    for (const r of rows) {
      if (!r.present) { console.log(`  ${r.id}: no output directory`); continue; }
      const gs = FROM_SOURCE.map((id) => `${id} ${r.g[id].verdict}`).join(", ");
      console.log(`  ${r.id} (${r.surface_class}): ${r.files} file(s), ${r.severity.S1} S1 / ${r.severity.S2} S2 / ${r.severity.S3} S3` +
        `${r.markers.length ? ` [${r.markers.join(" ")}]` : ""}; record ${r.record.valid ? "valid" : r.record.missing ? "missing" : `invalid (${r.record.violations.length})`}; ${gs}`);
    }
    console.log(`summary: briefs ${s.briefs}, ${s.sev.S1} S1 / ${s.sev.S2} S2 / ${s.sev.S3} S3, records valid ${s.valid}, G items ${s.g.PASS} PASS / ${s.g.FAIL} FAIL / ${s.g["N/A"]} N/A / ${s.g.NOT_RUN} NOT_RUN`);
  }
  if (o.write) {
    try {
      appendRow(o.results, row(o, s, today));
    } catch (e) {
      console.error(`render eval: ${e.message}`);
      return 2;
    }
    if (!o.json) console.log(`row written to ${path.relative(ROOT, o.results) || o.results}`);
  }
  return 0;
}

if (require.main === module) process.exitCode = main();

module.exports = { scoreBrief, summarise, row, appendRow, BRIEFS, G_ITEMS, FROM_SOURCE, HEADING };
