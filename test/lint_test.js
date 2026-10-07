#!/usr/bin/env node
/*
 * Project linter tests — `npx sheleg-design-skill --lint <dir>`, end to end.
 *
 * The linter is the machine half of SLOP_MARKERS.md. A linter that finds nothing
 * on a known-dirty tree is a broken linter, so every rule is watched firing on a
 * planted defect here as well as in its own `--self-test`, and every case that
 * must stay quiet (prose emoji, a pack-declared face, a test fixture, a comment)
 * is watched staying quiet. Each case builds a throwaway project, runs the real
 * CLI as a process and reads its exit code and output; nothing is imported, so
 * the argument parser and the exit-code contract are what is under test.
 *
 * House residue rule: a passing case loses its temp tree at exit, a failing case
 * KEEPS it, and the run ends with one line saying what it left.
 */
"use strict";

const { spawnSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const BIN = path.join(ROOT, "bin", "cli.js");

let failures = 0;
const trees = []; // { dir, label, failed }
let current = null;

function project(files) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "sheleg-lint-test-"));
  trees.push({ dir, label: current, failed: false });
  for (const [rel, text] of Object.entries(files || {})) {
    const p = path.join(dir, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, text);
  }
  return dir;
}

function cli(...args) {
  const r = spawnSync(process.execPath, [BIN, ...args], {
    cwd: os.tmpdir(),
    env: Object.assign({}, process.env, { NO_COLOR: "1" }),
    encoding: "utf8",
    timeout: 120000,
  });
  return { status: r.status, out: r.stdout || "", err: r.stderr || "", all: (r.stdout || "") + (r.stderr || "") };
}

function json(dir, ...extra) {
  const r = cli("--lint", dir, "--json", ...extra);
  let parsed = null;
  try { parsed = JSON.parse(r.out); } catch (e) { parsed = null; }
  // A quiet case that never got an array proves nothing: "no finding" has to be
  // read off a run that produced findings at all.
  assert(Array.isArray(parsed), `--json did not print an array (exit ${r.status}):\n${r.all.slice(0, 400)}`);
  return Object.assign(r, { findings: parsed });
}

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function rulesOf(findings) {
  return new Set((findings || []).map((f) => f.rule));
}

function caseRun(label, fn) {
  current = label;
  try {
    fn();
    console.log(`  ok  ${label}`);
  } catch (e) {
    failures++;
    for (const t of trees) if (t.label === label) t.failed = true;
    console.log(`FAIL  ${label}: ${e.message}`);
  }
}

// A tree that clears the floor: tokens, a named-property transition on transform,
// and the reduced-motion branch that makes the motion legal.
const CLEAN_CSS = `:root {
  --accent: #0a7d55;
  --ink: #1a1f2b;
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
}
.card {
  color: var(--ink);
  transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out);
}
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; }
}
`;

// ------------------------------------------------------------------ usage (exit 2)

caseRun("--lint with no directory is a usage error (exit 2)", () => {
  const r = cli("--lint");
  assert(r.status === 2, `exit ${r.status}, want 2\n${r.all}`);
});

caseRun("--lint on a path that does not exist is a usage error (exit 2)", () => {
  const r = cli("--lint", path.join(os.tmpdir(), "sheleg-lint-no-such-dir-" + process.pid));
  assert(r.status === 2, `exit ${r.status}, want 2\n${r.all}`);
});

caseRun("--json, --ratchet and --include-tests without --lint are usage errors", () => {
  for (const args of [["--json"], ["--include-tests"], ["--ratchet", "b.json"]]) {
    const r = cli(...args);
    assert(r.status === 2, `${args.join(" ")}: exit ${r.status}, want 2`);
  }
});

caseRun("--lint mixed with an install or kit flag is a usage error", () => {
  const dir = project({ "a.css": CLEAN_CSS });
  for (const extra of [["--claude"], ["--kit", "workbench", "--out", "x"], ["--force"]]) {
    const r = cli("--lint", dir, ...extra);
    assert(r.status === 2, `${extra.join(" ")}: exit ${r.status}, want 2`);
  }
});

caseRun("a directory with nothing to lint is refused (exit 2), not passed", () => {
  const dir = project({ "README.md": "# nothing here\n", "node_modules/x/a.css": "a{transition: all 1s}\n" });
  const r = cli("--lint", dir);
  assert(r.status === 2, `exit ${r.status}, want 2\n${r.all}`);
  assert(/nothing to lint/i.test(r.all), `no reason given:\n${r.all}`);
});

// ------------------------------------------------------------------ the exit contract

caseRun("a clean tree exits 0 and says how many files it read", () => {
  const dir = project({ "src/app.css": CLEAN_CSS });
  const r = cli("--lint", dir);
  assert(r.status === 0, `exit ${r.status}, want 0\n${r.all}`);
  assert(/1 file/.test(r.all), `the file count is missing:\n${r.all}`);
});

caseRun("one S1 finding exits 1 and prints file:line rule severity", () => {
  const dir = project({ "src/app.css": CLEAN_CSS + ".x {\n  transition: all 0.3s;\n}\n" });
  const r = cli("--lint", dir);
  assert(r.status === 1, `exit ${r.status}, want 1\n${r.all}`);
  assert(/src\/app\.css:14\s+lint:transition-all\s+S1\s+V039/.test(r.out), `line format:\n${r.out}`);
});

caseRun("S2 and S3 findings print but leave the exit at 0", () => {
  const dir = project({
    "src/app.css": CLEAN_CSS + ".bg {\n  background-image: repeating-linear-gradient(45deg, #000 0 2px, transparent 2px 8px);\n}\n",
  });
  const r = cli("--lint", dir);
  assert(r.status === 0, `exit ${r.status}, want 0\n${r.all}`);
  assert(/lint:stripes\s+S3/.test(r.out), `the S3 finding was not printed:\n${r.out}`);
});

caseRun("--json prints exactly {id, rule, severity, file, line, snippet} per finding", () => {
  const dir = project({ "src/Hero.tsx": 'export const H = () => <h1 className="bg-clip-text text-transparent">Hi</h1>;\n' });
  const r = json(dir);
  assert(r.status === 1, `exit ${r.status}, want 1\n${r.all}`);
  assert(Array.isArray(r.findings), `stdout is not a JSON array:\n${r.out}`);
  const f = r.findings.find((x) => x.rule === "gradient-text");
  assert(f, `no gradient-text finding: ${r.out}`);
  assert(JSON.stringify(Object.keys(f).sort()) === JSON.stringify(["file", "id", "line", "rule", "severity", "snippet"]),
    `keys: ${Object.keys(f)}`);
  assert(f.id === "V002" && f.severity === "S1" && f.file === "src/Hero.tsx" && f.line === 1,
    `values: ${JSON.stringify(f)}`);
});

// ------------------------------------------------------------------ every S1 rule blocks

const S1_PLANTS = {
  "purple-gradient": ["a.tsx", '<div className="bg-gradient-to-r from-indigo-500 via-violet-500 to-pink-500" />\n'],
  "gradient-text": ["a.css", ".t { -webkit-background-clip: text; color: transparent; }\n"],
  "side-stripe": ["a.tsx", '<div className="rounded-lg border-l-4 border-red-500 p-4">Alert</div>\n'],
  "emoji-icon": ["a.tsx", 'const items = [{ icon: "📊", label: "Reports" }];\n'],
  "bounce-easing": ["a.css", ":root { --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1); }\n"],
  "transition-all": ["a.tsx", '<button className="transition-all duration-200">Go</button>\n'],
  "layout-transition": ["a.css", ".sidebar { transition: width 0.2s ease, padding-left 0.2s ease; }\n"],
  "scale-zero": ["a.tsx", "<motion.div initial={{ scale: 0 }} animate={{ scale: 1 }} />\n"],
  "ease-in": ["a.css", ".menu { transition: opacity 200ms ease-in; }\n"],
};

for (const [rule, [file, text]] of Object.entries(S1_PLANTS)) {
  caseRun(`S1 lint:${rule} fires on its planted defect and exits 1`, () => {
    // Every plant rides on a tree that is otherwise clean, reduced-motion included,
    // so the exit code can only come from the planted line.
    const dir = project({ "src/base.css": CLEAN_CSS, [`src/${file}`]: text });
    const r = json(dir);
    assert(r.status === 1, `exit ${r.status}, want 1\n${r.all}`);
    assert(rulesOf(r.findings).has(rule), `lint:${rule} did not fire: ${r.out}`);
  });
}

caseRun("S1 lint:no-reduced-motion fires on a tree with motion and no reduced path", () => {
  const dir = project({ "src/a.css": "@keyframes rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; } }\n.a { animation: rise 300ms cubic-bezier(0.23, 1, 0.32, 1); }\n" });
  const r = json(dir);
  assert(r.status === 1, `exit ${r.status}, want 1\n${r.all}`);
  assert(rulesOf(r.findings).has("no-reduced-motion"), `did not fire: ${r.out}`);
});

caseRun("lint:no-reduced-motion is satisfied by a reduced path anywhere in the tree", () => {
  const dir = project({
    "src/a.css": "@keyframes rise { from { opacity: 0; } to { opacity: 1; } }\n.a { animation: rise 300ms cubic-bezier(0.23, 1, 0.32, 1); }\n",
    "src/b.tsx": "import { useReducedMotion } from 'framer-motion';\nexport const B = () => { const r = useReducedMotion(); return null; };\n",
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("no-reduced-motion"), `fired anyway: ${r.out}`);
});

caseRun("a loading spinner alone does not demand a reduced path", () => {
  const dir = project({ "src/a.tsx": '<span className="animate-spin h-4 w-4" />\n' });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("no-reduced-motion"), `fired on a spinner: ${r.out}`);
});

// ------------------------------------------------------------------ emoji: data and markup, not prose

caseRun("emoji in icon data and as an element's only child are flagged, on their own lines", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/Use.tsx": [
      "const rows = [",
      '  { icon: "✏️", text: t("draft") },',
      '  { icon: "🧑‍💼", text: t("standup") },',
      "];",
      'const cat = { cost: { icon: "💸", color: "text-error" } };',
      'export const A = () => <span className="text-2xl">📈</span>;',
      "export const B = () => <i>{\"⚡\"}</i>;",
      "",
    ].join("\n"),
  });
  const r = json(dir);
  const lines = (r.findings || []).filter((f) => f.rule === "emoji-icon").map((f) => f.line).sort((a, b) => a - b);
  assert(JSON.stringify(lines) === JSON.stringify([2, 3, 5, 6, 7]), `emoji-icon lines ${JSON.stringify(lines)}\n${r.out}`);
});

caseRun("emoji inside prose copy is content, not an icon, and is left alone", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/Copy.tsx": [
      "export const P = () => <p>Shipped on time 🎉 thanks to everyone</p>;",
      'const msg = "Nice work 👍, see you tomorrow";',
      'const reactions = ["👍", "🎉", "❤️"];',
      "export const Q = () => <p>Copyright © 2026, Example™</p>;",
      "",
    ].join("\n"),
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("emoji-icon"), `prose flagged: ${r.out}`);
});

caseRun("✨ marking an AI feature is its own S2 marker and never blocks", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/Ai.tsx": "export const L = () => <p>✨ Expected: 12% more</p>;\n" });
  const r = json(dir);
  assert(r.status === 0, `exit ${r.status}, want 0\n${r.all}`);
  const f = (r.findings || []).find((x) => x.rule === "sparkles");
  assert(f && f.severity === "S2" && f.id === "V028", `sparkles: ${r.out}`);
});

// ------------------------------------------------------------------ default face

const NEXT_INTER = 'import { Inter } from "next/font/google";\n\nconst inter = Inter({ subsets: ["latin"] });\n';

caseRun("Inter as the face shown, with no declared reason, is flagged at the call (S2)", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/app/layout.tsx": NEXT_INTER });
  const r = json(dir);
  const f = (r.findings || []).find((x) => x.rule === "default-font");
  assert(f && f.file === "src/app/layout.tsx" && f.line === 3 && f.severity === "S2", `default-font: ${r.out}`);
  assert(r.status === 0, `an S2 changed the exit: ${r.status}`);
});

caseRun("a face a copied pack token layer names is a declared choice, not a default", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/app/layout.tsx": NEXT_INTER,
    "src/app/globals.css": "/* SHELEG Design — Ledger token layer (light default).\n   Copy verbatim. */\n:root {\n  --font-ui: Inter, ui-sans-serif, system-ui, sans-serif;\n}\n",
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("default-font"), `pack-declared face flagged: ${r.out}`);
});

caseRun("a pack token layer's measured tokens are its exception; the project's own rules are not", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/pack.css": "/* SHELEG Design — Ora token layer (dark).\n   Copy verbatim. */\n:root {\n  --motion-ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* overshoot — badges only */\n}\n.mine { transition: all 1s; }\n",
  });
  const r = json(dir);
  const got = (r.findings || []).filter((f) => f.file === "src/pack.css").map((f) => f.rule);
  assert(JSON.stringify(got) === JSON.stringify(["transition-all"]), `pack-layer findings ${JSON.stringify(got)}`);
});

caseRun("font-family: system-ui alone in a stylesheet is flagged; a named face first is not", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/a.css": "body { font-family: system-ui, -apple-system, sans-serif; }\n",
    "src/b.css": 'h1 { font-family: "Söhne", system-ui, sans-serif; }\n',
  });
  const r = json(dir);
  const files = (r.findings || []).filter((f) => f.rule === "default-font").map((f) => f.file);
  assert(JSON.stringify(files) === JSON.stringify(["src/a.css"]), `default-font files ${JSON.stringify(files)}`);
});

// ------------------------------------------------------------------ recorded exceptions

caseRun("a waiver with an id and a reason removes the finding and is counted", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/app/layout.tsx": 'import { Inter } from "next/font/google";\n// sheleg-lint-allow: V015 brand face, director record Brief line\nconst inter = Inter({ subsets: ["latin"] });\n',
  });
  const r = cli("--lint", dir);
  assert(!/lint:default-font/.test(r.out), `waived finding printed:\n${r.out}`);
  assert(/1 waived/.test(r.all), `the waiver is not counted:\n${r.all}`);
});

caseRun("a bare id with no reason waives nothing", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/a.css": ".x {\n  /* sheleg-lint-allow: V039 */\n  transition: all 1s;\n}\n",
  });
  const r = cli("--lint", dir);
  assert(r.status === 1 && /lint:transition-all/.test(r.out), `exit ${r.status}\n${r.all}`);
});

// ------------------------------------------------------------------ what is not read

caseRun("node_modules, build output, hidden dirs, minified files and tests are skipped", () => {
  const bad = "a { transition: all 1s; }\n";
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "node_modules/pkg/a.css": bad,
    "dist/a.css": bad,
    "build/a.css": bad,
    ".next/a.css": bad,
    "src/vendor.min.css": bad,
    "src/__tests__/a.css": bad,
    "src/lib/__tests__/ratchet.test.ts": 'const bad = "cubic-bezier(0.34, 1.56, 0.64, 1)";\n',
    "src/a.test.tsx": bad,
    "src/a.spec.ts": bad,
    "fixtures/a.css": bad,
    "tests/a.css": bad,
  });
  const r = json(dir);
  assert(r.status === 0, `exit ${r.status}, want 0\n${r.out}`);
  assert((r.findings || []).length === 0, `skipped trees were read: ${r.out}`);
});

caseRun("--include-tests reads test files but never node_modules", () => {
  const bad = "a { transition: all 1s; }\n";
  const dir = project({ "src/base.css": CLEAN_CSS, "src/__tests__/a.css": bad, "node_modules/p/a.css": bad });
  const r = json(dir, "--include-tests");
  const files = (r.findings || []).map((f) => f.file);
  assert(JSON.stringify(files) === JSON.stringify(["src/__tests__/a.css"]), `files ${JSON.stringify(files)}`);
});

caseRun("a pattern inside a comment is history, not code", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/a.css": "/* THE GRADIENTS ARE GONE: from-violet-400 to-fuchsia-400, bg-clip-text,\n   transition: all 0.3s */\n.a { color: var(--ink); }\n",
    "src/b.tsx": "// was: className=\"bg-gradient-to-r from-indigo-500 to-purple-600\"\nexport const B = () => null;\n",
  });
  const r = json(dir);
  assert((r.findings || []).length === 0, `comments were linted: ${r.out}`);
});

// ------------------------------------------------------------------ ratchet

caseRun("--ratchet with a missing budget exits 2 and prints today's counts to start from", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/a.tsx": '<p className="text-gray-500 bg-white">x</p>\n' });
  const r = cli("--lint", dir, "--ratchet", path.join(dir, "budget.json"));
  assert(r.status === 2, `exit ${r.status}, want 2\n${r.all}`);
  let seed = null;
  try { seed = JSON.parse(r.out); } catch (e) { seed = null; }
  assert(seed && seed["src/a.tsx"] === 1, `no usable seed on stdout:\n${r.out}`);
});

caseRun("lint:raw-color counts only under --ratchet", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/a.tsx": '<p className="text-gray-500">x</p>\n' });
  const plain = json(dir);
  assert(!rulesOf(plain.findings).has("raw-color"), `raw-color without a ratchet: ${plain.out}`);
  fs.writeFileSync(path.join(dir, "budget.json"), JSON.stringify({ "src/a.tsx": 1 }));
  const r = json(dir, "--ratchet", path.join(dir, "budget.json"));
  assert(rulesOf(r.findings).has("raw-color"), `raw-color under a ratchet: ${r.out}`);
  assert(r.status === 0, `a file at its budget exited ${r.status}`);
});

caseRun("a file over its budget exits 1; a file absent from the budget has none", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/a.tsx": '<p className="text-gray-500 border-zinc-200">x</p>\n',
    "src/new.tsx": '<p className="text-red-600">x</p>\n',
  });
  fs.writeFileSync(path.join(dir, "budget.json"), JSON.stringify({ "src/a.tsx": 2 }));
  const r = cli("--lint", dir, "--ratchet", path.join(dir, "budget.json"));
  assert(r.status === 1, `exit ${r.status}, want 1\n${r.all}`);
  assert(/src\/new\.tsx.*1.*budget 0/.test(r.all), `the overrun is not named:\n${r.all}`);
});

caseRun("a file under its budget passes and asks for the budget to be lowered", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/a.tsx": '<p className="text-gray-500">x</p>\n' });
  fs.writeFileSync(path.join(dir, "budget.json"), JSON.stringify({ "src/a.tsx": 5 }));
  const r = cli("--lint", dir, "--ratchet", path.join(dir, "budget.json"));
  assert(r.status === 0, `exit ${r.status}, want 0\n${r.all}`);
  assert(/lower/i.test(r.all), `no request to lower the budget:\n${r.all}`);
});

caseRun("a malformed budget is a usage error (exit 2)", () => {
  const dir = project({ "src/base.css": CLEAN_CSS });
  fs.writeFileSync(path.join(dir, "budget.json"), '{"src/a.tsx": "many"}');
  const r = cli("--lint", dir, "--ratchet", path.join(dir, "budget.json"));
  assert(r.status === 2, `exit ${r.status}, want 2\n${r.all}`);
});

// ------------------------------------------------------------------ the rest of the rule set

caseRun("each S2/S3 lint rule fires on its planted defect", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/blur.tsx": '<div className="rounded-2xl backdrop-blur-md bg-white/10 p-6">card</div>\n',
    "src/glow.css": ".btn { box-shadow: 0 0 24px rgba(168, 85, 247, 0.6); }\n",
    "src/grid.css": ".bg {\n  background-image:\n    linear-gradient(to right, var(--line) 1px, transparent 1px),\n    linear-gradient(to bottom, var(--line) 1px, transparent 1px);\n  background-size: 56px 56px;\n}\n",
    "src/gray.tsx": '<div className="bg-blue-600 text-gray-400 p-4">x</div>\n',
    "src/chrome.tsx": [1, 2, 3, 4].map((i) => `<div className="rounded-2xl shadow-lg p-6">${i}</div>`).join("\n") + "\n",
    "src/reveal.tsx": [1, 2, 3].map((i) => `<motion.section whileInView={{ opacity: 1, y: 0 }} initial={{ opacity: 0, y: 24 }}>${i}</motion.section>`).join("\n") + "\n",
  });
  const r = json(dir);
  const got = rulesOf(r.findings);
  for (const rule of ["decorative-blur", "glow", "grid-background", "gray-on-color", "uniform-card-chrome", "reveal-everywhere"]) {
    assert(got.has(rule), `lint:${rule} did not fire: ${r.out}`);
  }
});

caseRun("glass on a sticky bar or a dialog is function, not decoration", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/nav.tsx": '<header className="sticky top-0 backdrop-blur-md bg-white/70">nav</header>\n',
    "src/sheet.css": ".dialog-overlay {\n  backdrop-filter: blur(8px);\n}\n",
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("decorative-blur"), `function flagged: ${r.out}`);
});

caseRun("a 2px rail, a transparent arrow border and a blockquote rule are not side stripes", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/tree.tsx": '<ul className="border-l-2 border-zinc-200 pl-3">x</ul>\n',
    "src/tip.css": ".tip::after { border-left: 6px solid transparent; }\nblockquote { border-left: 4px solid var(--line); }\n",
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("side-stripe"), `flagged: ${r.out}`);
});

caseRun("ease-in-out, an --ease-in token name and scale(0.95) are not flagged", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/a.css": ":root { --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); }\n.m { transition: transform 300ms ease-in-out; transform: scale(0.95); }\n.p { transition-timing-function: var(--ease-in); }\n",
  });
  const r = json(dir);
  const got = rulesOf(r.findings);
  assert(!got.has("ease-in") && !got.has("scale-zero"), `flagged: ${r.out}`);
});

caseRun("a string that merely says \"back\" or \"bounce\" is not an ease", () => {
  // Found calibrating on a production tree: a wizard's `setDirection("back")` was
  // read as a GSAP ease. An ease is named in an ease position, or with its dot.
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/w.tsx": 'const [d, setD] = useState<"forward" | "back">("forward");\nsetD("back");\nconst kind = "bounce";\n',
  });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("bounce-easing"), `flagged: ${r.out}`);
});

caseRun("GSAP and motion eases that overshoot are the bounce marker", () => {
  const dir = project({
    "src/base.css": CLEAN_CSS,
    "src/g.tsx": 'gsap.to(el, { y: 0, ease: "back.out(1.7)" });\ngsap.to(el, { x: 0, ease: "elastic" });\n<motion.div transition={{ type: "spring", bounce: 0.5 }} />\n',
  });
  const r = json(dir);
  const lines = (r.findings || []).filter((f) => f.rule === "bounce-easing").map((f) => f.line);
  assert(JSON.stringify(lines) === "[1,2,3]", `bounce lines ${JSON.stringify(lines)}: ${r.out}`);
});

caseRun("a single-hue blue gradient is not the purple marker", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/a.css": ".h { background: linear-gradient(90deg, #2563eb, #0ea5e9); }\n" });
  const r = json(dir);
  assert(!rulesOf(r.findings).has("purple-gradient"), `flagged: ${r.out}`);
});

caseRun("a purple CSS gradient is the purple marker", () => {
  const dir = project({ "src/base.css": CLEAN_CSS, "src/a.css": ".h { background: linear-gradient(135deg, #7c3aed 0%, #a855f7 60%, #d946ef 100%); }\n" });
  const r = json(dir);
  assert(rulesOf(r.findings).has("purple-gradient"), `missed: ${r.out}`);
});

// ------------------------------------------------------------------ self-test

caseRun("--self-test plants a defect for every rule and exits 0", () => {
  const r = cli("--self-test");
  assert(r.status === 0, `exit ${r.status}\n${r.all}`);
  assert(/caught\s+lint:emoji-icon/.test(r.all), `no per-rule line:\n${r.all}`);
  assert(/catalogue/i.test(r.all), `the catalogue sync was not checked:\n${r.all}`);
});

// ------------------------------------------------------------------ residue

const kept = [];
for (const t of trees) {
  if (t.failed) kept.push(`${t.dir} (${t.label})`);
  else fs.rmSync(t.dir, { recursive: true, force: true });
}
console.log(`lint tests: ${failures ? failures + " failed" : "all passed"}; left behind: ${kept.length ? kept.join(", ") : "nothing"}`);
process.exit(failures ? 1 : 0);
