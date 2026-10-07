"use strict";

/**
 * The director-record validator: the machine half of templates/director-record.md.
 *
 *   npx sheleg-design-skill --check-record <file> [--json]
 *
 * A director record is where a design's decisions live before the first pixel
 * (CREATIVE_DIRECTOR.md, "The record the director owes"). Each field is a
 * `## <Field>` heading; the header carries `surface_class`, and the class decides
 * which fields are owed. This file checks that every owed field is present and
 * non-empty BY ITS RULE — a Taste of "modern, clean" is empty, five references
 * on example.com are none, a Fork that never names its rubric compared nothing.
 *
 * What this is NOT: a judge. It cannot tell a good falsifier from a weak one or
 * a real reference from a lazy one. It refuses the shapes that are certainly
 * not decisions, and leaves the rest to the review it exists to feed.
 *
 * Exit contract: 0 valid; 1 violations, each listed as `<Field>: <problem>`;
 * 2 a usage error (no file, unreadable file). Node, no dependencies.
 */

const fs = require("fs");
const path = require("path");

const FIELDS = [
  "Brief", "Mode", "Taste", "References", "Cast", "Fork", "Rubric", "Critique",
  "Markers", "Alignment", "Quality", "Signature", "Surfaces", "Haptics", "ADA", "Open",
];

const CLASSES = {
  flagship: FIELDS,
  product: ["Brief", "Mode", "References", "Markers", "Open"],
  internal: ["Brief", "Mode", "Markers", "Open"],
  ad: ["Brief", "Mode", "Taste", "References", "Markers", "Signature", "ADA", "Open"],
};

const MODES = ["new", "redesign", "update", "audit", "declined"];

// Words every product claims about itself. A Take or Ban line made only of these
// (and connectives) decides nothing a second reader could check against a render.
const GENERIC = new Set((
  "modern clean minimal minimalist minimalistic minimalism sleek simple elegant beautiful premium nice " +
  "professional contemporary fresh stylish polished slick cool good great high quality high-quality " +
  "trendy aesthetic aesthetically pleasing look looking looks feel feeling vibe vibes design designs ui ux " +
  "style styled stylized and or with a an the of to in very some bit more less like ugly outdated old " +
  "boring bad cheap cluttered messy busy dated generic tacky " +
  "современный современно чистый чисто минималистичный минималистичность минимализм минимальный стильный " +
  "стильно лаконичный простой элегантный красивый красиво премиальный премиум приятный профессиональный " +
  "свежий модный дизайн и с в на без очень устаревший некрасивый старый скучный дешёвый дешевый " +
  "перегруженный безвкусный"
).split(/\s+/));

const PLACEHOLDER_HOST = /^(?:localhost|127\.\d+\.\d+\.\d+|0\.0\.0\.0|(?:[\w-]+\.)*example(?:\.(?:com|org|net))?|(?:[\w-]+\.)*(?:test|invalid|local|localhost))$/i;

// ------------------------------------------------------------------ parsing

function stripComments(text) {
  return text.replace(/<!--[\s\S]*?-->/g, "");
}

/** {header, sections: Map(field -> body), duplicates: [field], order: [field]} */
function parse(text) {
  const clean = stripComments(text.replace(/\r\n/g, "\n"));
  const lines = clean.split("\n");
  const sections = new Map();
  const duplicates = [];
  const headerLines = [];
  let field = null;
  let body = [];
  const flush = () => {
    if (field === null) return;
    if (sections.has(field)) duplicates.push(field);
    else sections.set(field, body.join("\n").trim());
  };
  for (const line of lines) {
    const m = line.match(/^##\s+(.+?)\s*$/);
    if (m && !line.startsWith("###")) {
      flush();
      const name = m[1].trim();
      const known = FIELDS.find((f) => f.toLowerCase() === name.toLowerCase());
      field = known || `?${name}`;
      body = [];
      continue;
    }
    if (field === null) headerLines.push(line);
    else body.push(line);
  }
  flush();
  const header = headerLines.join("\n");
  const cls = header.match(/^\s*surface_class\s*:\s*(.*?)\s*$/m);
  return { header, surfaceClass: cls ? cls[1] : null, sections, duplicates };
}

const isEmpty = (body) => body === undefined || body.replace(/[\s|:-]/g, "") === "";

function labelled(body, label) {
  const m = body.match(new RegExp(`^\\s*(?:[-*]\\s*)?${label}\\s*:\\s*(.*)$`, "im"));
  return m ? m[1].trim() : null;
}

function listItems(body) {
  return body.split("\n").filter((l) => /^\s*(?:[-*+]|\d+[.)])\s+\S/.test(l));
}

function contentWords(text) {
  return (text.toLowerCase().match(/[\p{L}][\p{L}\p{N}'’-]*/gu) || [])
    .filter((w) => w.length >= 3 && !GENERIC.has(w));
}

function reasonAfter(body, word) {
  const rest = body.replace(new RegExp(`^\\s*${word}\\b`, "i"), "").replace(/^[\s—–:,.-]+/, "");
  return contentWords(rest).length >= 2;
}

// ------------------------------------------------------------------ field rules
// Each rule returns a list of problems (strings) for a non-empty body.

const RULES = {
  Brief(body) {
    const out = [];
    for (const label of ["Surface", "Job", "Constraint", "Falsifier"]) {
      const v = labelled(body, label);
      if (!v) out.push(`no ${label} line — the brief owes Surface, Job, Constraint and Falsifier, and the falsifier is the one that costs something`);
    }
    return out;
  },

  Mode(body) {
    const word = (body.match(/^\s*([A-Za-z]+)/) || [])[1];
    const mode = word ? word.toLowerCase() : "";
    if (!MODES.includes(mode)) {
      return [`"${(body.split("\n")[0] || "").slice(0, 40)}" is not a mode — start with new, redesign, update, audit or declined`];
    }
    if (mode === "declined" && !reasonAfter(body, "declined")) {
      return ["declined with no reason — a refusal is valid only with the reason written down"];
    }
    return [];
  },

  Taste(body) {
    const out = [];
    for (const label of ["Take", "Ban"]) {
      const v = labelled(body, label);
      if (v === null || v === "") out.push(`no ${label} line — a taste profile says what this surface takes and what it bans`);
      else if (!contentWords(v).length) {
        out.push(`${label} is only generic words ("${v.slice(0, 50)}") — modern, clean, minimal and sleek are claimed by every product and decide nothing; name the materials, references, type and rhythm`);
      }
    }
    return out;
  },

  References(body) {
    if (/\bnone found\b/i.test(body)) {
      const where = labelled(body, "Searched");
      if (!where || contentWords(where).length < 2) {
        return ["`none found` without a `Searched:` line — an empty sweep counts only when it says where it looked"];
      }
      return [];
    }
    const urls = new Set();
    for (const line of listItems(body)) {
      if (!/\b(?:take|берём|берем)\s*:\s*\S.{2,}/i.test(line)) continue;
      const m = line.match(/https?:\/\/([^\s/)>\]]+)[^\s)>\]]*/i);
      if (!m) continue;
      const host = m[1].replace(/:\d+$/, "");
      if (PLACEHOLDER_HOST.test(host)) continue;
      urls.add(m[0].replace(/[.,;]+$/, ""));
    }
    if (urls.size < 5) {
      return [`${urls.size} of 5 real-product references (a URL on a real host and a \`take:\` each), and no \`none found\` + \`Searched:\``];
    }
    return [];
  },

  Fork(body, sections) {
    const word = ((body.match(/^\s*([A-Za-z]+)/) || [])[1] || "").toLowerCase();
    if (word === "no") {
      return reasonAfter(body, "no") ? [] : ["`no` without a reason — say why the fork is not real"];
    }
    if (word !== "yes") return ["must start with yes or no"];
    const out = [];
    const rubric = sections.get("Rubric");
    if (isEmpty(rubric)) out.push("yes, but the record has no Rubric — the rubric is written before either direction, or the fork compared nothing");
    else if (!/\brubric\b/i.test(body)) out.push("yes, but the fork never references the rubric it was judged against");
    if (labelled(body, "A") === null || labelled(body, "B") === null) out.push("yes, but no `A:` and `B:` directions");
    const winner = labelled(body, "Winner");
    if (!winner) out.push("yes, but no `Winner:` line (and what was grafted from the other)");
    return out;
  },

  Rubric(body) {
    const n = listItems(body).length;
    return n >= 3 ? [] : [`${n} criteria — three to five, each checkable by someone who built neither variation`];
  },

  Critique(body) {
    if (/\bclean render\b/i.test(body)) return [];
    const items = listItems(body);
    if (!items.length) return ["no triple and no `clean render` — each observation is region → defect → change"];
    const bad = items.filter((l) => (l.match(/→|->/g) || []).length < 2);
    return bad.length ? [`${bad.length} line(s) not a triple (region → defect → change): "${bad[0].trim().slice(0, 60)}"`] : [];
  },

  Markers(body) {
    const out = [];
    if (!/--lint\b/.test(body)) out.push("cites no `--lint` run — the command, the revision and the counts by severity");
    if (!/(?:@|\brevision\b|\bcommit\b)\s*:?\s*[0-9a-f]{7,40}\b/i.test(body)) out.push("no revision the run was made at (`@ <commit>`)");
    const counts = body.match(/(\d+)\s*S1\b[\s\S]*?(\d+)\s*S2\b[\s\S]*?(\d+)\s*S3\b/);
    if (!counts) out.push("no counts by severity (`N S1, N S2, N S3`)");
    else if (Number(counts[1]) > 0) out.push(`the cited run has ${counts[1]} S1 finding(s) — an S1 blocks; fix it, or waive it in source with \`sheleg-lint-allow: V0NN <reason>\``);
    return out;
  },

  Quality(body) {
    return /\d/.test(body) ? [] : ["no number — the quality table is measured, not described"];
  },

  Signature(body) {
    const out = [];
    const whats = body.match(/^\s*(?:[-*]\s*)?What\s*:/gim) || [];
    if (whats.length > 1) out.push(`${whats.length} signature moments — exactly one per flow`);
    for (const label of ["What", "Where", "Why"]) {
      if (!labelled(body, label)) out.push(`no ${label} line — one moment: what, where, and why it comes from the subject`);
    }
    return out;
  },

  Haptics(body) {
    if (/^\s*n\/?a\b/i.test(body) && !reasonAfter(body.replace(/^\s*n\/?a/i, ""), "")) {
      return ["n/a without a reason"];
    }
    return [];
  },

  ADA(body, sections, cls) {
    const na = /^\s*n\/?a\b/i.test(body);
    if (cls === "flagship" || cls === "ad") {
      if (na) return [`n/a on a ${cls} surface — the ${cls} profile of ADA_RUBRIC.md is owed`];
      const out = [];
      const profile = labelled(body, "Profile");
      if (!profile || profile.toLowerCase().split(/\s+/)[0] !== cls) out.push(`no \`Profile: ${cls}\` line`);
      if (!labelled(body, "Targets")) out.push("no `Targets:` line naming the categories aimed at");
      const g = body.match(/^\s*G\s*:\s*(.*)$/im);
      if (!g) out.push("no `G:` verdict line");
      else {
        const gFail = (g[1].match(/(\d+)\s*FAIL/i) || [])[1];
        if (gFail && Number(gFail) > 0) out.push(`${gFail} G item(s) FAIL — every G item passes on the ${cls} profile, and no judge outvotes a gate`);
        if (!/\d+\s*PASS/i.test(g[1])) out.push("the `G:` line carries no PASS count");
      }
      const j = body.match(/^\s*J\s*:\s*(.*)$/im);
      if (!j) out.push("no `J:` line (NOT_ASSESSED until a labelled set exists)");
      else if (!/NOT_ASSESSED/.test(j[1])) {
        const jFail = Number((j[1].match(/(\d+)\s*FAIL/i) || [])[1] || 0);
        const jPass = Number((j[1].match(/(\d+)\s*PASS/i) || [])[1] || 0);
        if (jPass > 0 && !labelled(body, "Labelled set")) {
          out.push("J items scored PASS with no `Labelled set:` line — until judge agreement is measured on a labelled set, J is NOT_ASSESSED, not PASS");
        }
        if (cls === "flagship" && jFail > 2) out.push(`${jFail} J item(s) FAIL — the flagship threshold is at most two, each with its reason recorded`);
      }
      if (cls === "ad" && !/safe[\s-]*zones?\s*:\s*\S/i.test(body)) out.push("no `Safe zones:` line — an ad is checked against its placement's safe zones");
      return out;
    }
    if (na && !reasonAfter(body.replace(/^\s*n\/?a/i, ""), "")) return ["n/a without a reason"];
    return [];
  },
};

// ------------------------------------------------------------------ the check

/**
 * text -> {valid, surface_class, mode, declined, owed, violations: [{field, problem}]}
 */
function checkRecord(text) {
  const { surfaceClass, sections, duplicates } = parse(text);
  const violations = [];
  const add = (field, problem) => violations.push({ field, problem });

  const modeBody = sections.get("Mode");
  const modeWord = modeBody ? ((modeBody.match(/^\s*([A-Za-z]+)/) || [])[1] || "").toLowerCase() : null;

  // A refusal is a record too, and it owes only its reason.
  if (modeWord === "declined") {
    for (const p of RULES.Mode(modeBody)) add("Mode", p);
    return { valid: !violations.length, surface_class: surfaceClass, mode: "declined", declined: true, owed: ["Mode"], violations };
  }

  let owed = [];
  if (surfaceClass === null) add("surface_class", "missing from the header — flagship, product, internal or ad decides which fields are owed");
  else if (!CLASSES[surfaceClass]) add("surface_class", `"${surfaceClass}" is not one of flagship, product, internal, ad`);
  else owed = CLASSES[surfaceClass];
  // Without a class, hold the record to the full set rather than the smallest one.
  const required = owed.length ? owed : FIELDS;

  for (const f of duplicates) {
    if (!f.startsWith("?")) add(f, "written twice — one field, one answer");
  }
  for (const field of FIELDS) {
    const body = sections.get(field);
    const owes = required.includes(field);
    if (body === undefined) {
      if (owes) add(field, "missing");
      continue;
    }
    if (isEmpty(body)) {
      if (owes) add(field, "empty");
      continue;
    }
    const rule = RULES[field];
    if (rule) for (const p of rule(body, sections, surfaceClass)) add(field, p);
  }
  // Fork: yes is checked against a Rubric whether or not the class owes one; the
  // Rubric's own rule above already ran if it was filled.
  return { valid: !violations.length, surface_class: surfaceClass, mode: modeWord, declined: false, owed: required, violations };
}

// ------------------------------------------------------------------ self-test

// A valid flagship record and one planted defect per rule. The full suite with
// every class, the CLI and the exit codes is test/record_test.js; this half runs
// from the installed package, where the test tree is not shipped.
const VALID = [
  "---", "surface_class: flagship", "---",
  "## Brief", "Surface: landing", "Job: start a trial from the first screen", "Constraint: the brand teal", "Falsifier: the trial button is below the fold at 1280×800",
  "## Mode", "new — entered at references",
  "## Taste", "Take: ledger rhythm, tabular figures, one warm accent", "Ban: violet gradients, three equal cards",
  "## References",
  ...["stripe.com", "linear.app", "mercury.com", "ramp.com", "notion.so"].map((h) => `- ${h} — https://${h}/ — take: the pricing table's first row`),
  "## Cast", "- sheleg-design — direction (style)",
  "## Fork", "yes — rubric written first", "A: pack", "B: concept", "Winner: B — grafted the table from A",
  "## Rubric", "- trial reachable without scrolling", "- at most five type sizes", "- amounts in tabular figures",
  "## Critique", "clean render",
  "## Markers", "npx sheleg-design-skill --lint src @ 3f2a9c1 — 0 S1, 1 S2, 0 S3",
  "## Alignment", "falsifier checked at 1280×800: false",
  "## Quality", "contrast 7.1:1",
  "## Signature", "What: the price counts up once", "Where: hero", "Why: the product is a meter",
  "## Surfaces", "none needed — a marketing page",
  "## Haptics", "n/a — web surface, no haptic engine",
  "## ADA", "Profile: flagship", "Targets: Interaction", "G: 15 PASS / 0 FAIL / 2 N/A", "J: NOT_ASSESSED — no labelled set",
  "## Open", "Whether the counter replays on revisit.",
].join("\n");

const SELF_PLANTS = [
  ["surface_class", (t) => t.replace("surface_class: flagship\n", "")],
  ["Open", (t) => t.replace(/## Open\n[^\n]*$/, "")],
  ["Brief", (t) => t.replace(/Falsifier:[^\n]*\n/, "")],
  ["Mode", (t) => t.replace("new — entered at references", "refresh")],
  ["Taste", (t) => t.replace("Take: ledger rhythm, tabular figures, one warm accent", "Take: modern, clean")],
  ["References", (t) => t.replace("https://ramp.com/", "https://example.com/")],
  ["Fork", (t) => t.replace("yes — rubric written first", "yes — two directions")],
  ["Rubric", (t) => t.replace("- amounts in tabular figures\n", "")],
  ["Critique", (t) => t.replace("clean render", "- the hero feels generic")],
  ["Markers", (t) => t.replace("--lint src", "eyeball")],
  ["Quality", (t) => t.replace("contrast 7.1:1", "fine")],
  ["Signature", (t) => t.replace(/Why:[^\n]*\n/, "")],
  ["Haptics", (t) => t.replace("n/a — web surface, no haptic engine", "n/a")],
  ["ADA", (t) => t.replace("G: 15 PASS / 0 FAIL", "G: 14 PASS / 1 FAIL")],
];

function selfTest(write) {
  let ok = true;
  const base = checkRecord(VALID);
  if (!base.valid) {
    ok = false;
    write(`  BROKEN  record: the self-test's valid record fails: ${base.violations.map((v) => `${v.field}: ${v.problem}`).join("; ")}`);
  }
  for (const [field, plant] of SELF_PLANTS) {
    const planted = plant(VALID);
    if (planted === VALID) { ok = false; write(`  BROKEN  record: the plant for ${field} changed nothing`); continue; }
    const r = checkRecord(planted);
    if (r.violations.some((v) => v.field === field)) write(`  caught  record: ${field}`);
    else { ok = false; write(`  MISSED  record: ${field} — the planted defect passed`); }
  }
  const declined = checkRecord("## Mode\n\ndeclined — no interface in this change; the operator said no design.\n");
  if (!declined.valid) { ok = false; write("  MISSED  record: a declined record with its reason is refused"); }
  else write("  caught  record: declined + reason passes on its own");
  write(ok ? `record: ${SELF_PLANTS.length} rules caught, the valid record passes` : "record: self-test FAILED");
  return ok ? 0 : 1;
}

// ------------------------------------------------------------------ the command

/** opts: {file, json}; io: {out, err}. Returns the exit code. */
function runCheckRecord(opts, io) {
  const file = path.resolve(opts.file);
  let text = null;
  try {
    const st = fs.statSync(file);
    if (!st.isFile()) throw new Error("not a file");
    text = fs.readFileSync(file, "utf8");
  } catch (e) {
    io.err(`sheleg-design-skill --check-record: ${opts.file} is not a readable file`);
    return 2;
  }
  const r = checkRecord(text);
  if (opts.json) {
    io.out(JSON.stringify(Object.assign({ file: opts.file }, r), null, 2));
    return r.valid ? 0 : 1;
  }
  const cls = r.declined ? "declined" : r.surface_class || "no surface_class";
  io.out(`sheleg-design check-record — ${opts.file} (${cls}${r.mode && !r.declined ? `, mode ${r.mode}` : ""})`);
  for (const v of r.violations) io.out(`  ${v.field}: ${v.problem}`);
  if (r.valid) {
    io.out(r.declined
      ? "exit 0: a declined record with its reason — nothing else is owed"
      : `exit 0: valid ${r.surface_class} record, ${r.owed.length} owed field(s) present and filled`);
    return 0;
  }
  io.out(`exit 1: ${r.violations.length} violation(s). Template: templates/director-record.md in the installed skill.`);
  return 1;
}

module.exports = { FIELDS, CLASSES, MODES, parse, checkRecord, selfTest, runCheckRecord };
