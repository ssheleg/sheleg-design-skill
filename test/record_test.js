#!/usr/bin/env node
/*
 * Director-record validator tests — `npx sheleg-design-skill --check-record <file>`.
 *
 * The record is where a design's decisions live before the first pixel
 * (templates/director-record.md). A validator that passes a record with no
 * falsifier, a taste profile of "modern, clean" or five references that are all
 * example.com is decoration, so every rule is watched failing here on ONE planted
 * defect in an otherwise valid record — and the valid records for each surface
 * class, plus a declined one, are watched passing. Each case writes a file and
 * runs the real CLI as a process: the argument parser and the exit-code contract
 * (0 valid, 1 violations, 2 usage) are what is under test.
 *
 * House residue rule: a passing case loses its temp file at exit, a failing case
 * KEEPS it, and the run ends with one line saying what it left.
 */
"use strict";

const { spawnSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const BIN = path.join(ROOT, "bin", "cli.js");
const FIX = path.join(__dirname, "fixtures", "records");
const TEMPLATE = path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design", "templates", "director-record.md");

let failures = 0;
const temps = []; // { file, label, failed }
let current = null;

function fixture(name) {
  return fs.readFileSync(path.join(FIX, name), "utf8");
}

function write(text) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sheleg-record-test-"));
  const file = path.join(dir, "director-record.md");
  fs.writeFileSync(file, text);
  temps.push({ file, dir, label: current, failed: false });
  return file;
}

function cli(...args) {
  const r = spawnSync(process.execPath, [BIN, ...args], {
    cwd: os.tmpdir(),
    env: Object.assign({}, process.env, { NO_COLOR: "1" }),
    encoding: "utf8",
    timeout: 60000,
  });
  return { status: r.status, out: r.stdout || "", err: r.stderr || "", all: (r.stdout || "") + (r.stderr || "") };
}

function check(text, ...extra) {
  return cli("--check-record", write(text), ...extra);
}

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function caseRun(label, fn) {
  current = label;
  try {
    fn();
    console.log(`  ok  ${label}`);
  } catch (e) {
    failures++;
    for (const t of temps) if (t.label === label) t.failed = true;
    console.log(`FAIL  ${label}: ${e.message}`);
  }
}

/** Replace exactly one occurrence; a mutation that matches nothing is a broken test, not a pass. */
function mutate(text, from, to) {
  const at = typeof from === "string" ? text.indexOf(from) : text.search(from);
  assert(at !== -1, `the mutation's anchor is not in the fixture: ${from}`);
  return text.replace(from, to);
}

/** Drop a whole `## Field` section, heading included. */
function dropSection(text, field) {
  const re = new RegExp(`^## ${field}\\n[\\s\\S]*?(?=^## |(?![\\s\\S]))`, "m");
  assert(re.test(text), `no ## ${field} section in the fixture`);
  return text.replace(re, "");
}

/** Replace a section's body. */
function setSection(text, field, body) {
  const re = new RegExp(`(^## ${field}\\n)[\\s\\S]*?(?=^## |(?![\\s\\S]))`, "m");
  assert(re.test(text), `no ## ${field} section in the fixture`);
  return text.replace(re, `$1\n${body}\n\n`);
}

function valid(r, what) {
  assert(r.status === 0, `${what} should be valid (exit 0), got exit ${r.status}:\n${r.all.slice(0, 800)}`);
}

/** Exactly the field named fails, with a message that says why. */
function rejects(r, field, needle) {
  assert(r.status === 1, `expected exit 1, got ${r.status}:\n${r.all.slice(0, 800)}`);
  const line = r.out.split("\n").find((l) => l.trimStart().startsWith(`${field}:`));
  assert(line, `no violation line for ${field}:\n${r.out.slice(0, 800)}`);
  if (needle) assert(line.toLowerCase().includes(needle.toLowerCase()), `the ${field} line does not say "${needle}": ${line}`);
}

const FLAG = fixture("flagship-valid.md");

// ------------------------------------------------------------ valid records

caseRun("a full flagship record is valid", () => valid(check(FLAG), "flagship-valid.md"));
caseRun("a product record owes only Brief, Mode, References, Markers, Open", () => valid(check(fixture("product-valid.md")), "product-valid.md"));
caseRun("an internal record owes only Brief, Mode, Markers, Open", () => valid(check(fixture("internal-valid.md")), "internal-valid.md"));
caseRun("an ad record is valid on the ad profile with safe zones", () => valid(check(fixture("ad-valid.md")), "ad-valid.md"));
caseRun("Mode: declined with a reason is a valid record on its own", () => {
  const r = check(fixture("declined.md"));
  valid(r, "declined.md");
  assert(/declined/i.test(r.out), `the verdict does not say the record is a refusal:\n${r.out}`);
});

// ------------------------------------------------------------ header and shape

caseRun("no surface_class header is refused", () => {
  rejects(check(mutate(FLAG, "surface_class: flagship\n", "")), "surface_class", "missing");
});
caseRun("an unknown surface_class is refused", () => {
  rejects(check(mutate(FLAG, "surface_class: flagship", "surface_class: hero")), "surface_class", "flagship");
});
caseRun("a missing field the class owes is refused", () => {
  rejects(check(dropSection(FLAG, "Open")), "Open", "missing");
});
caseRun("a field holding only template guidance counts as empty", () => {
  rejects(check(setSection(FLAG, "Cast", "<!-- each skill and what it is for -->")), "Cast", "empty");
});
caseRun("a field written twice is refused", () => {
  rejects(check(FLAG + "\n## Open\n\nA second answer.\n"), "Open", "twice");
});
caseRun("the unfilled template is refused field by field", () => {
  const t = mutate(fs.readFileSync(TEMPLATE, "utf8"), "<flagship | product | internal | ad>", "flagship");
  const r = check(t);
  assert(r.status === 1, `the copied template passed (exit ${r.status})`);
  const empty = r.out.split("\n").filter((l) => /^\s+[A-Za-z]+: empty/.test(l));
  assert(empty.length === 16, `expected all 16 fields reported empty, got ${empty.length}:\n${r.out}`);
});
caseRun("a product record without References is refused", () => {
  rejects(check(dropSection(fixture("product-valid.md"), "References")), "References", "missing");
});

// ------------------------------------------------------------ Brief and Mode

caseRun("a Brief without a Falsifier is refused", () => {
  rejects(check(mutate(FLAG, /^Falsifier:.*\n/m, "")), "Brief", "falsifier");
});
caseRun("a Mode outside new/redesign/update/audit/declined is refused", () => {
  rejects(check(setSection(FLAG, "Mode", "refresh — make it pop")), "Mode", "redesign");
});
caseRun("Mode: declined with no reason is refused", () => {
  rejects(check("## Mode\n\ndeclined\n"), "Mode", "reason");
});

// ------------------------------------------------------------ Taste

caseRun("a Taste of only generic words is read as empty", () => {
  const t = setSection(FLAG, "Taste", "Take: modern, clean, minimal\nBan: ugly, outdated");
  rejects(check(t), "Taste", "generic");
});
caseRun("a Taste in Russian generic words is read as empty too", () => {
  const t = setSection(FLAG, "Taste", "Take: современный, чистый, минималистичный\nBan: устаревший, некрасивый");
  rejects(check(t), "Taste", "generic");
});
caseRun("a Taste with no Ban line is refused", () => {
  rejects(check(mutate(FLAG, /^Ban:.*\n/m, "")), "Taste", "ban");
});

// ------------------------------------------------------------ References

caseRun("three references are not five", () => {
  const t = setSection(FLAG, "References", [
    "- Stripe Invoicing — https://stripe.com/invoicing — take: the line-item table",
    "- Wave — https://www.waveapps.com/invoicing — take: the client picker",
    "- FreshBooks — https://www.freshbooks.com/invoice — take: one action per step",
  ].join("\n"));
  rejects(check(t), "References", "3 of 5");
});
caseRun("placeholder hosts do not count as real products", () => {
  const t = mutate(mutate(FLAG, "https://stripe.com/invoicing", "https://example.com/a"), "https://www.waveapps.com/invoicing", "http://localhost:3000/b");
  rejects(check(t), "References", "3 of 5");
});
caseRun("a reference with no `take:` does not count", () => {
  const t = mutate(FLAG, " — take: the line-item table that totals as you type", "");
  rejects(check(t), "References", "4 of 5");
});
caseRun("`none found` without where it was searched is refused", () => {
  const t = setSection(fixture("product-valid.md"), "References", "none found");
  rejects(check(t), "References", "searched");
});

// ------------------------------------------------------------ Fork and Rubric

caseRun("Fork: yes that never references the rubric is refused", () => {
  rejects(check(mutate(FLAG, "yes — the rubric below was written before either direction existed.", "yes — two directions.")), "Fork", "rubric");
});
caseRun("Fork: yes with no rubric section is refused", () => {
  rejects(check(dropSection(FLAG, "Rubric")), "Fork", "rubric");
});
caseRun("Fork: yes without a winner is refused", () => {
  rejects(check(mutate(FLAG, /^Winner:.*\n/m, "")), "Fork", "winner");
});
caseRun("a Fork that is neither yes nor no is refused", () => {
  rejects(check(setSection(FLAG, "Fork", "maybe later")), "Fork", "yes or no");
});
caseRun("Fork: no without a reason is refused", () => {
  rejects(check(setSection(FLAG, "Fork", "no")), "Fork", "reason");
});
caseRun("Fork: no with a reason is valid", () => {
  valid(check(setSection(FLAG, "Fork", "no — the brand and the pack fix the answer; one direction, rendered once")), "Fork: no + reason");
});
caseRun("a Rubric of two criteria is refused", () => {
  const t = setSection(FLAG, "Rubric", "- send is reachable without scrolling\n- five type sizes at most");
  rejects(check(t), "Rubric", "three");
});

// ------------------------------------------------------------ Critique

caseRun("a critique line that is not region → defect → change is refused", () => {
  const t = setSection(FLAG, "Critique", "- the hero feels a bit generic");
  rejects(check(t), "Critique", "triple");
});
caseRun("`clean render` is a valid critique — there is no defect quota", () => {
  valid(check(setSection(FLAG, "Critique", "clean render — no observable defect at 375 or 768")), "clean render");
});

// ------------------------------------------------------------ Markers

caseRun("Markers that cite no --lint run are refused", () => {
  rejects(check(setSection(FLAG, "Markers", "checked by eye @ 3f2a9c1 — 0 S1, 0 S2, 0 S3")), "Markers", "--lint");
});
caseRun("Markers with no revision are refused", () => {
  rejects(check(setSection(FLAG, "Markers", "npx sheleg-design-skill --lint src — 0 S1, 2 S2, 1 S3")), "Markers", "revision");
});
caseRun("Markers with no counts by severity are refused", () => {
  rejects(check(setSection(FLAG, "Markers", "npx sheleg-design-skill --lint src @ 3f2a9c1 — clean")), "Markers", "counts");
});
caseRun("Markers citing an S1 finding are refused — S1 blocks", () => {
  rejects(check(setSection(FLAG, "Markers", "npx sheleg-design-skill --lint src @ 3f2a9c1 — 2 S1, 0 S2, 0 S3")), "Markers", "S1");
});

// ------------------------------------------------------------ the rest of the flagship set

caseRun("a Quality table with no number is refused", () => {
  rejects(check(setSection(FLAG, "Quality", "Looks right on every screen.")), "Quality", "number");
});
caseRun("two signature moments are refused — exactly one", () => {
  const t = setSection(FLAG, "Signature", "What: the envelope fold\nWhere: send\nWhy: paper\nWhat: a confetti burst\nWhere: first payment\nWhy: celebration");
  rejects(check(t), "Signature", "one");
});
caseRun("a Signature without its Why is refused", () => {
  rejects(check(mutate(FLAG, /^Why:.*\n/m, "")), "Signature", "why");
});
caseRun("Haptics: n/a with no reason is refused", () => {
  rejects(check(setSection(FLAG, "Haptics", "n/a")), "Haptics", "reason");
});

// ------------------------------------------------------------ ADA

caseRun("ADA: n/a on a flagship is refused", () => {
  rejects(check(setSection(FLAG, "ADA", "n/a — no time")), "ADA", "flagship");
});
caseRun("a flagship with a G item failing is refused — the judge cannot outvote a gate", () => {
  rejects(check(mutate(FLAG, "G: 15 PASS / 0 FAIL / 2 N/A", "G: 14 PASS / 1 FAIL / 2 N/A")), "ADA", "G");
});
caseRun("a flagship with three J items failing is refused", () => {
  const t = mutate(FLAG, "J: NOT_ASSESSED — no labelled set yet", "J: 4 PASS / 3 FAIL\nLabelled set: 24 screens, agreement 0.81");
  rejects(check(t), "ADA", "J");
});
caseRun("J items scored PASS without a labelled set are refused — NOT_ASSESSED, not PASS", () => {
  rejects(check(mutate(FLAG, "J: NOT_ASSESSED — no labelled set yet", "J: 9 PASS / 0 FAIL")), "ADA", "labelled set");
});
caseRun("an ad record without safe zones is refused", () => {
  rejects(check(mutate(fixture("ad-valid.md"), /^Safe zones:.*\n/m, "")), "ADA", "safe zone");
});

// ------------------------------------------------------------ usage and output

caseRun("--json prints the verdict as an object", () => {
  const r = check(setSection(FLAG, "Fork", "maybe"), "--json");
  assert(r.status === 1, `exit ${r.status}`);
  let v = null;
  try { v = JSON.parse(r.out); } catch (e) { v = null; }
  assert(v && v.valid === false && Array.isArray(v.violations), `not a verdict object:\n${r.out.slice(0, 400)}`);
  assert(v.violations.some((x) => x.field === "Fork"), "the Fork violation is not in the JSON");
  assert(v.surface_class === "flagship", `surface_class ${v.surface_class}`);
});
caseRun("no file is a usage error (exit 2)", () => {
  const r = cli("--check-record");
  assert(r.status === 2, `exit ${r.status}`);
});
caseRun("a file that does not exist is a usage error (exit 2)", () => {
  const r = cli("--check-record", path.join(os.tmpdir(), "no-such-record-sheleg.md"));
  assert(r.status === 2, `exit ${r.status}:\n${r.all}`);
});
caseRun("--check-record does not combine with --lint", () => {
  const r = cli("--check-record", path.join(FIX, "declined.md"), "--lint", ".");
  assert(r.status === 2, `exit ${r.status}`);
});
caseRun("--self-test covers the record rules too", () => {
  const r = cli("--self-test");
  assert(r.status === 0, `self-test exit ${r.status}:\n${r.all.slice(-800)}`);
  assert(/record:/.test(r.out), `the self-test says nothing about the record validator:\n${r.out.slice(-800)}`);
});

// ------------------------------------------------------------ residue

const left = [];
for (const t of temps) {
  if (t.failed) left.push(t.file);
  else fs.rmSync(t.dir, { recursive: true, force: true });
}
console.log(failures ? `record tests: ${failures} FAILED` : "record tests: all passed");
console.log(`left behind: ${left.length ? left.join(", ") : "nothing"}`);
process.exit(failures ? 1 : 0);
