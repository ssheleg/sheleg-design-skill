#!/usr/bin/env node
/*
 * Render eval runner tests (evals/render/run.js).
 *
 * The runner counts what a generated surface contains. A counter that reports
 * zero on a tree known to hold a violet gradient is broken, so the committed
 * sample (evals/render/sample/, hand-written, contents listed in its README) is
 * run through the real script and every count is asserted. --write is watched
 * appending exactly one row to a COPY of RESULTS.md, never the real one.
 */
"use strict";

const { spawnSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const RUN = path.join(ROOT, "evals", "render", "run.js");
const SAMPLE = path.join(ROOT, "evals", "render", "sample");

let failures = 0;
function caseRun(label, fn) {
  try { fn(); console.log(`  ok  ${label}`); } catch (e) { failures++; console.log(`FAIL  ${label}: ${e.message}`); }
}
function assert(c, m) { if (!c) throw new Error(m); }
function run(...args) {
  const r = spawnSync(process.execPath, [RUN, ...args], { encoding: "utf8", timeout: 60000 });
  return { status: r.status, out: r.stdout || "", err: r.stderr || "" };
}

let j = null;
caseRun("the runner reads the sample and prints JSON", () => {
  const r = run(SAMPLE, "--json");
  assert(r.status === 0, `exit ${r.status}: ${r.err}`);
  j = JSON.parse(r.out);
  assert(j.rows.length === 4, `${j.rows.length} briefs`);
});
const by = (id) => j.rows.find((r) => r.id === id);

caseRun("the clean landing scores 0 S1 with a valid record and R8, R20, R24 PASS", () => {
  const r = by("landing-hero-motion");
  assert(r.severity.S1 === 0 && r.record.valid, JSON.stringify(r.severity) + JSON.stringify(r.record));
  for (const id of ["R8", "R20", "R24"]) assert(r.g[id].verdict === "PASS", `${id} ${r.g[id].verdict}`);
});
caseRun("the planted onboarding is caught: violet gradient, emoji icon, no reduced motion, no record", () => {
  const r = by("mobile-onboarding");
  for (const id of ["V001", "V027", "V043"]) assert(r.markers.includes(id), `${id} not counted: ${r.markers}`);
  assert(r.severity.S1 >= 3, `S1 ${r.severity.S1}`);
  assert(r.record.missing, "a missing record was not reported missing");
  assert(r.g.R20.verdict === "FAIL", `R20 ${r.g.R20.verdict}`);
});
caseRun("raw colour outside the tokens fails R8 on the dashboard", () => {
  const r = by("product-dashboard");
  assert(r.g.R8.verdict === "FAIL", `R8 ${r.g.R8.verdict}`);
  assert(r.record.valid, r.record.violations.join("; "));
  assert(r.g.R24.verdict === "N/A", "R24 is a flagship item");
});
caseRun("a generic taste profile makes the paywall record invalid", () => {
  const r = by("paywall");
  assert(!r.record.valid && r.record.violations.some((v) => v.startsWith("Taste:")), r.record.violations.join("; "));
});
caseRun("everything the source cannot decide is NOT_RUN, never PASS", () => {
  for (const r of j.rows) for (const id of ["R1", "R4", "R14", "R15", "R17"]) assert(r.g[id].verdict === "NOT_RUN", `${r.id} ${id} ${r.g[id].verdict}`);
});
caseRun("--write appends exactly one dated row to the results file it is given", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sheleg-render-eval-"));
  try {
    const copy = path.join(dir, "RESULTS.md");
    fs.copyFileSync(path.join(ROOT, "test", "evals", "RESULTS.md"), copy);
    const before = fs.readFileSync(copy, "utf8").split("\n").length;
    const r = run(SAMPLE, "--model", "test-model", "--write", "--results", copy);
    assert(r.status === 0, `exit ${r.status}: ${r.err}`);
    const text = fs.readFileSync(copy, "utf8");
    assert(text.split("\n").length === before + 1, "not exactly one line added");
    assert(new RegExp(`\\| \\d{4}-\\d{2}-\\d{2} \\| [\\d.]+ \\| \`[^\`]+\` \\| test-model \\| 4/4 \\|`).test(text), "the row is not shaped as the table's");
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
caseRun("a results file with no render-eval section is refused (exit 2), not written", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sheleg-render-eval-"));
  try {
    const copy = path.join(dir, "RESULTS.md");
    fs.writeFileSync(copy, "# Evaluation results\n");
    const r = run(SAMPLE, "--write", "--results", copy);
    assert(r.status === 2, `exit ${r.status}`);
    assert(fs.readFileSync(copy, "utf8") === "# Evaluation results\n", "the file changed");
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
caseRun("no outputs directory is a usage error", () => {
  assert(run().status === 2, "no args");
  assert(run(path.join(os.tmpdir(), "no-such-render-outputs")).status === 2, "missing dir");
});

console.log(failures ? `render eval tests: ${failures} FAILED` : "render eval tests: all passed");
process.exit(failures ? 1 : 0);
