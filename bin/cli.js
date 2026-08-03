#!/usr/bin/env node
"use strict";

/**
 * sheleg-design-skill installer.
 *
 * Copies the SHELEG Design skill bundle (SKILL.md, SHELEG_DESIGN.md, the style
 * packs and their token CSS) into the current project so a Cursor / Claude
 * agent can discover and apply it.
 *
 * Zero dependencies on purpose: it must run instantly via `npx` with no install
 * step and no supply-chain surface.
 */

const fs = require("fs");
const path = require("path");

const SKILL_DIR = path.join(
  __dirname,
  "..",
  "plugins",
  "sheleg-design",
  "skills",
  "sheleg-design",
);
const SKILL_SLUG = "sheleg-design";
const CORE_FILES = ["SKILL.md", "SHELEG_DESIGN.md"];

// The bundle is everything under skill/ — walked at runtime so adding a
// style pack or token file never requires touching the installer.
function listBundleFiles() {
  const out = [];
  const walk = (dir, prefix) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) walk(path.join(dir, entry.name), rel);
      else out.push(rel);
    }
  };
  walk(SKILL_DIR, "");
  return out.sort();
}

const pkg = require(path.join(__dirname, "..", "package.json"));

const COLORS = {
  reset: "\x1b[0m",
  bold: "\x1b[1m",
  dim: "\x1b[2m",
  blue: "\x1b[38;5;75m",
  green: "\x1b[38;5;42m",
  yellow: "\x1b[38;5;214m",
};
const useColor = process.stdout.isTTY && !process.env.NO_COLOR;
const c = (color, s) => (useColor ? COLORS[color] + s + COLORS.reset : s);

function parseArgs(argv) {
  const opts = {
    target: null, // explicit --dir
    flavor: null, // "cursor" | "claude"
    force: false,
    help: false,
    version: false,
    error: null, // set → print help and exit non-zero
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") opts.help = true;
    else if (a === "--version" || a === "-v") opts.version = true;
    else if (a === "--force" || a === "-f") opts.force = true;
    else if (a === "--cursor") opts.flavor = "cursor";
    else if (a === "--claude") opts.flavor = "claude";
    else if (a === "--dir") {
      // A bare trailing --dir must fail loudly: silently falling back to
      // auto-detect would install somewhere the caller did not ask for.
      const value = argv[++i];
      if (!value || value.startsWith("-")) opts.error = "--dir needs a path";
      else opts.target = value;
    } else if (a.startsWith("--dir=")) {
      const value = a.slice("--dir=".length);
      if (!value) opts.error = "--dir needs a path";
      else opts.target = value;
    } else {
      opts.error = `unknown argument: ${a}`;
    }
  }
  if (opts.flavor && opts.target) {
    opts.error = "--dir cannot be combined with --cursor / --claude";
  }
  return opts;
}

function printHelp() {
  console.log(`
${c("bold", "SHELEG Design")} ${c("dim", "v" + pkg.version)}
Install the SHELEG Design skill into your project.

${c("bold", "Usage")}
  npx sheleg-design-skill [options]

${c("bold", "Options")}
  --cursor        Install to .cursor/skills/${SKILL_SLUG}/
  --claude        Install to .claude/skills/${SKILL_SLUG}/
  --dir <path>    Install to a custom directory
  --force, -f     Overwrite existing files
  --help, -h      Show this help
  --version, -v   Show version

${c("bold", "Default")}
  Auto-detects: uses .cursor/ if present, else .claude/ if present,
  otherwise creates .cursor/skills/${SKILL_SLUG}/.

${c("bold", "What it installs")}
  SKILL.md             the agent-facing skill (discovery + principles)
  SHELEG_DESIGN.md     the full reference (architecture, recipes, why it works)
  FIGMA_BRIDGE.md      the design↔code contract (tokens ⇄ Figma variables)
  AI_PRODUCT_PATTERNS.md  chat / agent / streaming surfaces (honest state)
  styles/              six style packs — instrument-console (dark console),
                       editorial-luxury (warm editorial), workbench (light/dark
                       product UI), briefing-room (dark 16:9 presentation deck),
                       atrium (warm cream consumer health), orchard (friendly
                       consumer biotech) — plus a ready-made token CSS per pack
                       and STYLE_PACK_TEMPLATE.md for authoring more
`);
}

function resolveTargetDir(opts, cwd) {
  if (opts.target) return path.resolve(cwd, opts.target);
  if (opts.flavor === "cursor")
    return path.join(cwd, ".cursor", "skills", SKILL_SLUG);
  if (opts.flavor === "claude")
    return path.join(cwd, ".claude", "skills", SKILL_SLUG);

  const hasCursor = fs.existsSync(path.join(cwd, ".cursor"));
  const hasClaude = fs.existsSync(path.join(cwd, ".claude"));
  if (hasCursor) return path.join(cwd, ".cursor", "skills", SKILL_SLUG);
  if (hasClaude) return path.join(cwd, ".claude", "skills", SKILL_SLUG);
  return path.join(cwd, ".cursor", "skills", SKILL_SLUG);
}

function main() {
  const opts = parseArgs(process.argv.slice(2));

  if (opts.error) {
    console.error(c("yellow", `sheleg-design-skill: ${opts.error}`));
    printHelp();
    process.exit(2);
  }
  if (opts.version) {
    console.log(pkg.version);
    return;
  }
  if (opts.help) {
    printHelp();
    return;
  }

  const cwd = process.cwd();
  const targetDir = resolveTargetDir(opts, cwd);

  // Verify the bundle is intact before touching the filesystem.
  for (const f of CORE_FILES) {
    if (!fs.existsSync(path.join(SKILL_DIR, f))) {
      console.error(
        c("yellow", `Bundle is missing ${f}. This is a packaging bug.`),
      );
      process.exit(1);
    }
  }

  const files = listBundleFiles();
  const existing = files.filter((f) =>
    fs.existsSync(path.join(targetDir, f)),
  );
  if (existing.length && !opts.force) {
    console.error(
      `\n${c("yellow", "Refusing to overwrite existing files:")}\n` +
        existing.map((f) => "  " + path.join(targetDir, f)).join("\n") +
        `\n\nRe-run with ${c("bold", "--force")} to overwrite.\n`,
    );
    process.exit(1);
  }

  fs.mkdirSync(targetDir, { recursive: true });
  for (const f of files) {
    const dest = path.join(targetDir, f);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(path.join(SKILL_DIR, f), dest);
  }

  const rel = path.relative(cwd, targetDir) || ".";
  console.log(
    `\n${c("green", "✓")} ${c("bold", "SHELEG Design")} installed to ${c("blue", rel + "/")}\n` +
      `  ${c("dim", "SKILL.md")}          the agent skill\n` +
      `  ${c("dim", "SHELEG_DESIGN.md")}  the full reference\n` +
      `  ${c("dim", "styles/")}           style packs + token CSS (instrument-console / editorial-luxury / workbench / briefing-room / atrium / orchard)\n\n` +
      `Your Cursor / Claude agent can now discover the skill and build\n` +
      `cinematic, scroll-driven pages — or style product UI (dashboards,\n` +
      `admin, internal tools) from the workbench pack — on its principles.\n\n` +
      `${c("dim", "Docs: " + pkg.homepage)}\n`,
  );
}

main();
