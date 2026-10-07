"use strict";

/**
 * The project linter: the machine half of SLOP_MARKERS.md.
 *
 *   npx sheleg-design-skill --lint <dir> [--json] [--ratchet <budget.json>] [--include-tests]
 *   npx sheleg-design-skill --self-test
 *
 * Every rule below names the marker it checks (`id`) and the severity the
 * catalogue gives it. The validator reads those three fields off this file and
 * refuses a rule the catalogue does not list, or a catalogue `lint:` row this
 * file does not implement, so the two cannot drift apart silently.
 *
 * Written for Node with no dependencies, like the installer beside it: the
 * command runs wherever `npx` runs, and a Python requirement would have made it
 * fail on exactly the machines (a fresh macOS, Windows) that never asked for one.
 *
 * Exit contract: 0 no S1 finding and no ratchet overrun; 1 an S1 finding or an
 * overrun; 2 a usage error. S2 and S3 print and never move the exit code.
 *
 * What this is NOT: a renderer. It reads class strings, CSS declarations and
 * JSX data line by line, after comments are blanked out (line numbers kept). It
 * cannot see what the cascade resolves to, which is why half the catalogue is
 * marked `review`.
 */

const fs = require("fs");
const path = require("path");

const SKILL_DIR = path.join(__dirname, "..", "plugins", "sheleg-design", "skills", "sheleg-design");
const CATALOGUE = path.join(SKILL_DIR, "SLOP_MARKERS.md");

const EXTS = new Set([".html", ".htm", ".css", ".scss", ".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".vue", ".svelte", ".astro"]);
const CSS_EXTS = new Set([".css", ".scss"]);
const STYLE_HOSTS = new Set([".html", ".htm", ".vue", ".svelte", ".astro"]);
// Build output and dependency trees. Hidden directories (`.next`, `.git`,
// `.cursor` and the rest) are skipped by their leading dot.
const SKIP_DIRS = new Set(["node_modules", "dist", "build", "out", "coverage", "storybook-static", "bower_components", "jspm_packages", "vendor", "target"]);
// Tests are skipped by default: a ratchet test that guards against a pattern has
// to contain it, and reporting the guard as the defect is a false positive.
const TEST_DIRS = new Set(["__tests__", "__mocks__", "__fixtures__", "fixtures", "test", "tests", "e2e", "cypress", "playwright"]);
const TEST_FILE = /\.(test|spec)\.[a-z0-9]+$/i;
const MAX_BYTES = 2 * 1024 * 1024;

// ------------------------------------------------------------------ colour

const NAMED = {
  purple: "#800080", violet: "#ee82ee", indigo: "#4b0082", fuchsia: "#ff00ff", magenta: "#ff00ff",
  blueviolet: "#8a2be2", mediumpurple: "#9370db", rebeccapurple: "#663399", darkviolet: "#9400d3",
  darkorchid: "#9932cc", mediumorchid: "#ba55d3", orchid: "#da70d6", plum: "#dda0dd", darkmagenta: "#8b008b",
  slateblue: "#6a5acd", mediumslateblue: "#7b68ee", black: "#000000", white: "#ffffff", gray: "#808080",
  grey: "#808080", silver: "#c0c0c0", red: "#ff0000", blue: "#0000ff", green: "#008000", orange: "#ffa500",
};

function hsl(r, g, b) {
  r /= 255; g /= 255; b /= 255;
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  const l = (max + min) / 2;
  let h = 0;
  let s = 0;
  if (max !== min) {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    if (max === r) h = (g - b) / d + (g < b ? 6 : 0);
    else if (max === g) h = (b - r) / d + 2;
    else h = (r - g) / d + 4;
    h *= 60;
  }
  return { h, s, l };
}

/** Every colour literal on a string, as {h, s, l} (oklch hue kept as `oh`). */
function colours(text) {
  const out = [];
  const re = /#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b|rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)|hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%|oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)|\b([a-z]+)\b/gi;
  let m;
  while ((m = re.exec(text))) {
    if (m[1]) {
      let hex = m[1];
      if (hex.length <= 4) hex = hex.slice(0, 3).split("").map((c) => c + c).join("");
      out.push(hsl(parseInt(hex.slice(0, 2), 16), parseInt(hex.slice(2, 4), 16), parseInt(hex.slice(4, 6), 16)));
    } else if (m[2]) {
      out.push(hsl(+m[2], +m[3], +m[4]));
    } else if (m[5]) {
      out.push({ h: +m[5] % 360, s: +m[6] / 100, l: +m[7] / 100 });
    } else if (m[8]) {
      const c = +m[9];
      // oklch: chroma stands in for saturation; lightness may be 0–1 or a percent.
      const L = m[8].endsWith("%") ? parseFloat(m[8]) / 100 : +m[8];
      out.push({ h: NaN, oh: +m[10], s: Math.min(1, c / 0.2), l: L });
    } else if (m[11] && Object.prototype.hasOwnProperty.call(NAMED, m[11].toLowerCase())) {
      const hex = NAMED[m[11].toLowerCase()].slice(1);
      out.push(hsl(parseInt(hex.slice(0, 2), 16), parseInt(hex.slice(2, 4), 16), parseInt(hex.slice(4, 6), 16)));
    }
  }
  return out;
}

const isViolet = (c) => (c.oh >= 285 && c.oh <= 335 && c.s >= 0.4) || (c.h >= 250 && c.h <= 320 && c.s >= 0.3 && c.l >= 0.12 && c.l <= 0.9);
const isIndigo = (c) => (c.oh >= 270 && c.oh < 285 && c.s >= 0.4) || (c.h >= 232 && c.h < 250 && c.s >= 0.4 && c.l >= 0.12 && c.l <= 0.9);
const isChromatic = (c) => c.s >= 0.4 && c.l >= 0.15 && c.l <= 0.85;
const isGray = (c) => c.s < 0.15 && c.l >= 0.3 && c.l <= 0.8;

/** A gradient reads as the purple marker when a stop is violet-to-fuchsia, or
 * when indigo sits beside another hue (the indigo→violet→pink and indigo→blue
 * runs). A single-hue indigo or blue gradient is not the marker. */
function purpleStops(args) {
  const cs = colours(args).filter((c) => c.s >= 0.3);
  if (cs.some(isViolet)) return true;
  const indigo = cs.filter(isIndigo);
  return indigo.length > 0 && cs.length > indigo.length;
}

// ------------------------------------------------------------------ text helpers

/** Blank comments out, keeping every newline so line numbers survive. */
function stripComments(text, ext) {
  const blank = (s) => s.replace(/[^\n]/g, " ");
  let out = text.replace(/\/\*[\s\S]*?\*\//g, blank);
  if (ext !== ".css") {
    // `//` comments, only where `//` opens the line (after whitespace) or follows
    // whitespace after code — never inside `https://`.
    out = out.replace(/(^|[\s;{},])\/\/[^\n]*/gm, (m, lead) => lead + blank(m.slice(lead.length)));
  }
  out = out.replace(/<!--[\s\S]*?-->/g, blank);
  return out;
}

/** The arguments of every `fn(` call on a line, parentheses balanced. */
function calls(line, fn) {
  const out = [];
  let i = 0;
  const needle = fn + "(";
  while ((i = line.indexOf(needle, i)) !== -1) {
    const prev = line[i - 1];
    if (prev && /[\w-]/.test(prev)) { i += needle.length; continue; }
    let depth = 0;
    let j = i + fn.length;
    for (; j < line.length; j++) {
      if (line[j] === "(") depth++;
      else if (line[j] === ")" && --depth === 0) break;
    }
    out.push(line.slice(i + needle.length, j));
    i = j;
  }
  return out;
}

function splitTop(s) {
  const parts = [];
  let depth = 0;
  let cur = "";
  for (const ch of s) {
    if (ch === "(") depth++;
    if (ch === ")") depth--;
    if (ch === "," && depth === 0) { parts.push(cur); cur = ""; } else cur += ch;
  }
  parts.push(cur);
  return parts.map((p) => p.trim()).filter(Boolean);
}

const firstFamily = (value) => {
  const first = splitTop(value)[0] || "";
  return first.replace(/^['"`\s]+|['"`\s!]+$/g, "").replace(/\s*!important$/, "").toLowerCase();
};

const DEFAULT_FACES = new Set(["inter", "inter variable", "inter-variable", "roboto", "arial", "system-ui", "-apple-system", "blinkmacsystemfont", "segoe ui", "ui-sans-serif", "sans-serif"]);
const LAYOUT_PROP = /^(?:-webkit-)?(?:width|height|min-width|max-width|min-height|max-height|top|left|right|bottom|inset(?:-[a-z-]+)?|margin(?:-[a-z-]+)?|padding(?:-[a-z-]+)?|gap|row-gap|column-gap|font-size)$/;
const HUES = "red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose";
const NEUTRALS = "slate|gray|zinc|neutral|stone";
const EMOJI = "(?:\\p{Regional_Indicator}{2}|(?:\\p{Emoji_Presentation}|\\p{Extended_Pictographic}\\uFE0F)\\p{Emoji_Modifier}?(?:\\u200D(?:\\p{Emoji_Presentation}|\\p{Extended_Pictographic})\\uFE0F?\\p{Emoji_Modifier}?)*)";
const EMOJI_ONLY = `${EMOJI}(?:\\s*${EMOJI})*`;
const RE_EMOJI_DATA = new RegExp(`\\b\\w*(?:icon|Icon|emoji|Emoji|glyph|Glyph|symbol|Symbol)\\s*[:=]\\s*\\{?\\s*(['"\`])\\s*${EMOJI_ONLY}\\s*\\1`, "u");
const RE_EMOJI_CHILD = new RegExp(`<([A-Za-z][\\w.:-]*)(?:\\s[^<>]*)?>\\s*(?:${EMOJI_ONLY}|\\{\\s*(['"\`])\\s*${EMOJI_ONLY}\\s*\\2\\s*\\})\\s*</\\1\\s*>`, "u");

function cubic(args) {
  const n = args.split(/[\s,_]+/).filter(Boolean).map(Number);
  return n.length === 4 && n.every((x) => !Number.isNaN(x)) ? n : null;
}

const functionalGlass = /\b(?:sticky|fixed)\b|<(?:nav|header|dialog|aside|menu)\b|role=["'](?:dialog|menu|navigation|toolbar|tooltip)|\b(?:nav|navbar|navigation|header|topbar|toolbar|tab-?bar|bottom-?bar|app-?bar|sheet|drawer|modal|dialog|overlay|popover|dropdown|menu|tooltip|backdrop(?!-)|scrim|sidebar|command|toast|hud|lightbox)\b/i;

// ------------------------------------------------------------------ the rules
//
// `line` rules see one comment-blanked line plus a context: the CSS selector
// chain the line sits in (CSS and <style> blocks), and the two lines above it.
// `file` rules see the whole file. `project` rules see every file at once.

const RULES = [
  {
    rule: "purple-gradient", id: "V001", severity: "S1", scope: "line",
    test(line) {
      if (new RegExp(`\\b(?:from|via|to)-(?:indigo|violet|purple|fuchsia)-\\d{2,3}\\b`).test(line)) return true;
      for (const fn of ["linear-gradient", "radial-gradient", "conic-gradient", "repeating-linear-gradient", "repeating-radial-gradient"]) {
        if (calls(line, fn).some(purpleStops)) return true;
      }
      return false;
    },
  },
  {
    rule: "gradient-text", id: "V002", severity: "S1", scope: "line",
    test: (line) => /\bbg-clip-text\b|(?:-webkit-)?background-clip\s*:\s*text\b|(?:Webkit|webkit)?[Bb]ackgroundClip\s*:\s*['"`]text['"`]/.test(line),
  },
  {
    rule: "decorative-blur", id: "V003", severity: "S2", scope: "line",
    test(line, ctx) {
      if (!/\bbackdrop-blur(?:-[\w[\]]+)?\b|backdrop-filter\s*:[^;]*blur|backdropFilter\s*:\s*['"`][^'"`]*blur/.test(line)) return false;
      return !functionalGlass.test(line) && !functionalGlass.test(ctx.selector) && !functionalGlass.test(ctx.above);
    },
  },
  {
    rule: "glow", id: "V004", severity: "S2", scope: "line",
    test(line) {
      if (new RegExp(`\\b(?:shadow|drop-shadow)-(?:${HUES})-\\d{2,3}(?:\\/\\d+)?\\b`).test(line)) return true;
      const values = [];
      const decl = /(?:box|text)-shadow\s*:\s*([^;]+)|(?:boxShadow|textShadow)\s*:\s*['"`]([^'"`]+)/g;
      let m;
      while ((m = decl.exec(line))) values.push(m[1] || m[2]);
      const arb = /\b(?:shadow|drop-shadow)-\[([^\]]+)\]/g;
      while ((m = arb.exec(line))) values.push(m[1].replace(/_/g, " "));
      for (const args of calls(line, "drop-shadow")) values.push(args);
      return values.some((v) => splitTop(v).some((one) => {
        const offsets = one.replace(/(?:rgba?|hsla?|oklch|color-mix)\([^)]*\)/g, " ").match(/-?\d*\.?\d+(?:px|rem|em)?/g) || [];
        const nums = offsets.map((x) => parseFloat(x));
        return nums.length >= 3 && nums[0] === 0 && nums[1] === 0 && nums[2] > 0 && colours(one).some(isChromatic);
      }));
    },
  },
  {
    rule: "side-stripe", id: "V005", severity: "S1", scope: "line",
    test(line, ctx) {
      if (/<blockquote\b/.test(line) || /\bblockquote\b/.test(ctx.selector)) return false;
      if (/\bborder-[lrse]-(?:[3-9]|[1-9]\d)\b/.test(line)) return true;
      const arb = line.match(/\bborder-[lrse]-\[(\d+(?:\.\d+)?)px\]/);
      if (arb && +arb[1] >= 3) return true;
      const css = /border-(?:left|right|inline-start|inline-end)(?:-width)?\s*:\s*([^;]+)/g;
      let m;
      while ((m = css.exec(line))) {
        const w = m[1].match(/(\d+(?:\.\d+)?)px/);
        if (w && +w[1] >= 3 && !/transparent/.test(m[1])) return true;
      }
      return false;
    },
  },
  {
    rule: "grid-background", id: "V006", severity: "S2", scope: "line",
    test: (line) => calls(line, "linear-gradient").some((a) => /\btransparent\b/.test(a) && /(?:^|[\s,])[12]px\b/.test(a.replace(/_/g, " "))),
  },
  {
    rule: "stripes", id: "V007", severity: "S3", scope: "line",
    test: (line) => /\brepeating-(?:linear|radial|conic)-gradient\(/.test(line),
  },
  {
    rule: "gray-on-color", id: "V008", severity: "S2", scope: "line",
    test(line, ctx) {
      if (new RegExp(`\\bbg-(?:${HUES})-(?:500|600|700|800|900|950)\\b`).test(line) &&
          new RegExp(`\\btext-(?:${NEUTRALS})-(?:300|400|500|600)\\b`).test(line)) return true;
      // CSS: a grey `color:` inside a block whose background is saturated.
      const m = line.match(/(?:^|[;{\s])color\s*:\s*([^;]+)/);
      if (!m || !ctx.block) return false;
      const fg = colours(m[1]);
      const bg = colours(ctx.block.background || "");
      return fg.length > 0 && fg.every(isGray) && bg.some(isChromatic);
    },
  },
  {
    rule: "uniform-card-chrome", id: "V010", severity: "S3", scope: "file",
    run(lines) {
      const hits = [];
      lines.forEach((l, i) => {
        if (/\brounded-(?:2xl|3xl)\b/.test(l) && /\bshadow-(?:lg|xl|2xl)\b/.test(l)) hits.push(i);
      });
      return hits.length >= 4 ? [{ index: hits[0], note: `${hits.length} containers carry the same radius and shadow` }] : [];
    },
  },
  {
    rule: "raw-color", id: "V011", severity: "S3", scope: "line", ratchetOnly: true,
    count(line) {
      // A token definition is where a literal belongs: drop `--name: value` first.
      line = line.replace(/--[\w-]+\s*:[^;}]*/g, " ");
      let n = (line.match(new RegExp(`\\b(?:bg|text|border|from|via|to|ring|fill|stroke|outline|decoration|divide|placeholder|accent|caret|shadow|ring-offset)-(?:${NEUTRALS}|${HUES})-\\d{2,3}\\b`, "g")) || []).length;
      n += (line.match(/(?<![&\w])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b(?![\w-])/g) || []).length;
      n += (line.match(/\b(?:rgba?|hsla?|oklch)\(/g) || []).length;
      return n;
    },
  },
  {
    rule: "default-font", id: "V015", severity: "S2", scope: "project",
    run: defaultFont,
  },
  {
    rule: "emoji-icon", id: "V027", severity: "S1", scope: "line",
    test: (line) => RE_EMOJI_DATA.test(line) || RE_EMOJI_CHILD.test(line),
  },
  {
    rule: "sparkles", id: "V028", severity: "S2", scope: "line",
    test: (line, ctx) => !ctx.fired.has("emoji-icon") && (/✨/.test(line) || /<Sparkles(?:Icon)?\b|\bicon\s*[:=]\s*\{?\s*Sparkles(?:Icon)?\b/.test(line)),
  },
  {
    rule: "reveal-everywhere", id: "V037", severity: "S2", scope: "file",
    run(lines) {
      const hits = [];
      lines.forEach((l, i) => {
        const n = (l.match(/\bwhileInView\b|\bdata-aos=|<(?:Reveal|FadeIn|FadeUp|FadeInUp|ScrollReveal|AnimateOnScroll)\b/g) || []).length;
        for (let k = 0; k < n; k++) hits.push(i);
      });
      return hits.length >= 3 ? [{ index: hits[2], note: `${hits.length} scroll-in entrances in one file` }] : [];
    },
  },
  {
    rule: "bounce-easing", id: "V038", severity: "S1", scope: "line",
    test(line) {
      const curves = calls(line, "cubic-bezier").map(cubic);
      const arr = /\bease\s*:\s*\[([^\]]+)\]/.exec(line);
      if (arr) curves.push(cubic(arr[1]));
      if (curves.some((c) => c && (c[1] < 0 || c[1] > 1 || c[3] < 0 || c[3] > 1))) return true;
      if (/\b(?:ease(?:In|Out|InOut)(?:Back|Elastic|Bounce)|back(?:In|Out|InOut)|anticipate)\b/.test(line)) return true;
      // GSAP names an ease as a string: with its dot anywhere ("back.out(1.7)"), or
      // bare only in an ease position — a bare "back" elsewhere is just a word.
      if (/['"`](?:back|elastic|bounce)\.(?:in|out|inOut)(?:\([^)]*\))?['"`]/.test(line)) return true;
      if (/\bease\s*[:=]\s*['"`](?:back|elastic|bounce)(?:\([^)]*\))?['"`]/.test(line)) return true;
      if (/\banimate-bounce\b/.test(line)) return true;
      const spring = line.match(/\bbounce\s*:\s*(\d*\.?\d+)/);
      return Boolean(spring && +spring[1] > 0.3);
    },
  },
  {
    rule: "transition-all", id: "V039", severity: "S1", scope: "line",
    test: (line) => /\btransition(?:-property)?\s*:\s*['"`]?\s*all\b|\btransitionProperty\s*:\s*['"`]all\b|(?<![\w-])transition-all\b/.test(line),
  },
  {
    rule: "layout-transition", id: "V040", severity: "S1", scope: "line",
    test(line, ctx) {
      const lists = [];
      const css = /\btransition(?:-property)?\s*:\s*['"`]?([^;'"`}]+)/g;
      let m;
      while ((m = css.exec(line))) lists.push(...splitTop(m[1]).map((p) => p.split(/\s+/)[0]));
      const tw = /\btransition-\[([^\]]+)\]/g;
      while ((m = tw.exec(line))) lists.push(...m[1].split(/[,_]/).map((p) => p.trim().split(/\s+/)[0]));
      if (lists.some((p) => LAYOUT_PROP.test(p))) return true;
      // Inside @keyframes, a layout property declared at all is a layout animation.
      if (/@keyframes/.test(ctx.selector)) {
        const d = /(?:^|[{;\s])([a-z-]+)\s*:/g;
        while ((m = d.exec(line))) if (LAYOUT_PROP.test(m[1])) return true;
      }
      return /\b(?:animate|initial|exit|whileHover|whileTap|whileInView)\s*=\s*\{\{[^}]*\b(?:width|height|top|left|right|bottom|margin\w*|padding\w*)\s*:/.test(line);
    },
  },
  {
    rule: "scale-zero", id: "V041", severity: "S1", scope: "line",
    test: (line) => /\bscale(?:3d)?\(\s*0(?:\.0+)?\s*[,)]|(?<![\w-])scale-0\b|\bscale\s*:\s*0(?![.\d])/.test(line),
  },
  {
    rule: "ease-in", id: "V042", severity: "S1", scope: "line",
    test(line) {
      if (/(?<![-\w])ease-in(?![-\w])/.test(line)) return true;
      if (/\bease\s*:\s*['"`](?:easeIn|ease-in|in|(?:power\d|expo|circ|sine|quad|cubic|quart|quint)\.in)['"`]/.test(line)) return true;
      // A cubic-bezier that starts flat and ends at full speed is ease-in by another name.
      return calls(line, "cubic-bezier").map(cubic).some((c) => c && c[0] >= 0.3 && c[1] === 0 && c[2] >= 0.9 && c[3] === 1);
    },
  },
  {
    rule: "no-reduced-motion", id: "V043", severity: "S1", scope: "project",
    run: noReducedMotion,
  },
];

const BY_RULE = new Map(RULES.map((r) => [r.rule, r]));

// ------------------------------------------------------------------ project rules

const PACK_HEADER = /SHELEG Design — .+? token layer/;

function defaultFont(files) {
  // Faces a copied pack token layer names first are a declared choice: the pack
  // was extracted off a live reference, and the doctrine is that its values win.
  const declared = new Set();
  for (const f of files) {
    if (!PACK_HEADER.test(f.raw)) continue;
    for (const m of f.code.matchAll(/--font[\w-]*\s*:\s*([^;]+)/g)) declared.add(firstFamily(m[1]));
  }
  const out = [];
  for (const f of files) {
    if (PACK_HEADER.test(f.raw)) continue;
    const nextFont = /from\s+['"]next\/font\/(?:google|local)['"]/.test(f.code);
    f.lines.forEach((line, i) => {
      if (/@font-face/.test(f.ctx[i].selector)) return; // defines a face, does not show it
      const faces = [];
      for (const m of line.matchAll(/(?:^|[\s;{"'`])font-family\s*:\s*([^;}{]+)/g)) faces.push(m[1]);
      for (const m of line.matchAll(/(?:^|[\s;{])--font[\w-]*\s*:\s*([^;}{]+)/g)) faces.push(m[1]);
      for (const m of line.matchAll(/\bfontFamily\s*:\s*(['"`])([^'"`]+)\1/g)) faces.push(m[2]);
      for (const m of line.matchAll(/\b(?:sans|serif|body|display|heading|ui|base)\s*:\s*\[\s*(['"`])([^'"`]+)\1/g)) faces.push(m[2]);
      if (nextFont) for (const m of line.matchAll(/\b(Inter|Roboto)\s*\(/g)) faces.push(m[1]);
      for (const m of line.matchAll(/@fontsource(?:-variable)?\/(inter|roboto)\b/gi)) faces.push(m[1]);
      for (const m of line.matchAll(/fonts\.googleapis\.com\/css2?\?[^"'\s]*family=(Inter|Roboto)\b/g)) faces.push(m[1]);
      const hit = faces.map(firstFamily).find((face) => face && !face.startsWith("var(") && DEFAULT_FACES.has(face) && !declared.has(face));
      if (hit) out.push({ file: f, index: i, note: hit });
    });
  }
  return out;
}

function noReducedMotion(files) {
  const evidence = /prefers-reduced-motion|useReducedMotion|\bmotion-(?:reduce|safe):|reducedMotion\s*=|<MotionConfig\b/;
  if (files.some((f) => evidence.test(f.code))) return [];
  const motion = /@keyframes\s+(?!spin\b)[\w-]+|\banimation(?:-name)?\s*:\s*(?!none\b)(?!spin\b)[\w-]|\banimate-(?!spin\b|none\b)[a-z]|from\s+['"](?:framer-motion|motion\/react|gsap)['"]|\bwhileInView\b|\btransition(?:-property)?\s*:[^;]*\btransform\b/;
  for (const f of files) {
    const i = f.lines.findIndex((l) => motion.test(l));
    if (i !== -1) return [{ file: f, index: i, note: "motion with no reduced-motion path in the tree" }];
  }
  return [];
}

// ------------------------------------------------------------------ per-file context

/**
 * The CSS selector chain for every line, and the block each line declares into.
 * A block opened on the line itself counts (`.a { color: … }` on one line), so a
 * one-line rule is read with its selector rather than with none.
 */
function cssContext(lines, ext) {
  const css = CSS_EXTS.has(ext);
  const host = STYLE_HOSTS.has(ext);
  const ctx = [];
  const stack = [];
  let inStyle = css;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (host && /<style\b/i.test(line)) inStyle = true;
    const above = lines.slice(Math.max(0, i - 2), i).join(" ");
    let block = stack[stack.length - 1] || null;
    let selector = stack.map((b) => b.sel).join(" ");
    if (inStyle) {
      let buf = "";
      for (const ch of line) {
        if (ch === "{") {
          stack.push({ sel: buf.trim(), background: "" });
          block = stack[stack.length - 1];
          selector = stack.map((b) => b.sel).join(" ");
          buf = "";
        } else if (ch === "}") { stack.pop(); buf = ""; }
        else buf += ch;
      }
      // A background declared on a later line still belongs to the block: the
      // object is shared, and rules run only after every line has been read.
      const bg = line.match(/background(?:-color)?\s*:\s*([^;}]+)/);
      if (block && bg) block.background = bg[1];
    }
    ctx.push({ selector, above, block });
    if (host && /<\/style>/i.test(line)) { inStyle = false; stack.length = 0; }
  }
  return ctx;
}

// ------------------------------------------------------------------ waivers

const WAIVER = /sheleg-lint-allow:?\s+(V\d{3}(?:\s*,\s*V\d{3})*)(.*)$/;

function waivers(rawLines) {
  const map = new Map(); // line index -> Set(ids)
  rawLines.forEach((raw, i) => {
    const m = raw.match(WAIVER);
    if (!m) return;
    const reason = m[2].replace(/\*\/|-->|\}\s*$/g, "").replace(/[\s—–:,-]+/g, " ").trim();
    if (!reason) return; // a bare id waives nothing
    const ids = new Set(m[1].split(/\s*,\s*/));
    for (const at of [i, i + 1]) {
      if (!map.has(at)) map.set(at, new Set());
      for (const id of ids) map.get(at).add(id);
    }
  });
  return map;
}

// ------------------------------------------------------------------ the core

/** files: [{rel, text}] -> {findings, waived} */
function lintFiles(input, opts) {
  const ratchet = Boolean(opts && opts.ratchet);
  const files = input.map(({ rel, text }) => {
    const ext = path.extname(rel).toLowerCase();
    const code = stripComments(text, ext);
    const lines = code.split("\n");
    const rawLines = text.split("\n");
    // A copied pack token layer carries the pack's MEASURED values: a token it
    // defines on a marker (an overshoot curve "badges only", a measured cream) is
    // the marker's stated exception, written in the pack document. Its
    // definitions are not reported; what the project writes around them is.
    const pack = PACK_HEADER.test(text);
    return { rel, ext, raw: text, code, lines, rawLines, pack, ctx: cssContext(lines, ext), waive: waivers(rawLines) };
  });
  const findings = [];
  let waived = 0;
  const emit = (rule, f, index, times) => {
    const w = f.waive.get(index);
    if (w && w.has(rule.id)) { waived += times || 1; return; }
    const snippet = (f.rawLines[index] || "").trim().slice(0, 160);
    for (let k = 0; k < (times || 1); k++) {
      findings.push({ id: rule.id, rule: rule.rule, severity: rule.severity, file: f.rel, line: index + 1, snippet });
    }
  };
  for (const f of files) {
    f.lines.forEach((line, i) => {
      if (f.pack && /^\s*--[\w-]+\s*:/.test(line)) return;
      const fired = new Set();
      const ctx = Object.assign({}, f.ctx[i], { fired });
      for (const rule of RULES) {
        if (rule.scope !== "line" || (rule.ratchetOnly && !ratchet)) continue;
        if (rule.count) {
          const n = rule.count(line);
          if (n) emit(rule, f, i, n);
        } else if (rule.test(line, ctx)) {
          fired.add(rule.rule);
          emit(rule, f, i);
        }
      }
    });
    for (const rule of RULES) {
      if (rule.scope !== "file") continue;
      for (const hit of rule.run(f.lines)) emit(rule, f, hit.index);
    }
  }
  for (const rule of RULES) {
    if (rule.scope !== "project") continue;
    for (const hit of rule.run(files)) emit(rule, hit.file, hit.index);
  }
  findings.sort((a, b) => (a.file < b.file ? -1 : a.file > b.file ? 1 : a.line - b.line || (a.rule < b.rule ? -1 : 1)));
  return { findings, waived };
}

// ------------------------------------------------------------------ the walk

function walk(root, includeTests) {
  const out = [];
  const skipped = { large: 0 };
  const visit = (dir) => {
    let entries;
    try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return; }
    for (const e of entries) {
      const abs = path.join(dir, e.name);
      if (e.isSymbolicLink()) continue; // never follow a link out of the tree, or round in a loop
      if (e.isDirectory()) {
        if (e.name.startsWith(".") || SKIP_DIRS.has(e.name)) continue;
        if (!includeTests && TEST_DIRS.has(e.name)) continue;
        visit(abs);
      } else if (e.isFile()) {
        const ext = path.extname(e.name).toLowerCase();
        if (!EXTS.has(ext) || /\.min\.[a-z]+$/i.test(e.name)) continue;
        if (!includeTests && TEST_FILE.test(e.name)) continue;
        let st;
        try { st = fs.statSync(abs); } catch (err) { continue; }
        if (st.size > MAX_BYTES) { skipped.large++; continue; }
        const text = fs.readFileSync(abs, "utf8");
        if (text.includes("\u0000")) continue;
        out.push({ rel: path.relative(root, abs).split(path.sep).join("/"), text });
      }
    }
  };
  visit(root);
  out.sort((a, b) => (a.rel < b.rel ? -1 : 1));
  return { files: out, skipped };
}

// ------------------------------------------------------------------ the catalogue

/** Rows of SLOP_MARKERS.md: [{id, group, severity, check}] */
function parseCatalogue(text) {
  const rows = [];
  for (const line of text.split("\n")) {
    const m = line.match(/^\|\s*(V\d{3})\s*\|(.*)\|\s*$/);
    if (!m) continue;
    const cells = m[2].split("|").map((c) => c.trim());
    rows.push({ id: m[1], group: cells[0], severity: cells[1], check: (cells[5] || "").replace(/`/g, "") });
  }
  return rows;
}

function catalogueSync(text) {
  const problems = [];
  const rows = parseCatalogue(text);
  const lintRows = new Map(rows.filter((r) => r.check.startsWith("lint:")).map((r) => [r.check.slice(5), r]));
  for (const rule of RULES) {
    const row = lintRows.get(rule.rule);
    if (!row) problems.push(`lint:${rule.rule} is implemented but no catalogue row checks it`);
    else if (row.id !== rule.id || row.severity !== rule.severity) {
      problems.push(`lint:${rule.rule} is ${rule.id}/${rule.severity} here and ${row.id}/${row.severity} in the catalogue`);
    }
  }
  for (const name of lintRows.keys()) {
    if (!BY_RULE.has(name)) problems.push(`the catalogue checks lint:${name}, which has no implementation`);
  }
  return { rows, problems };
}

// ------------------------------------------------------------------ self-test

// One planted defect and one clean twin per rule. A rule that does not fire on
// its plant is a broken rule; a rule that fires on its twin is a noisy one.
const PLANTS = {
  "purple-gradient": [["a.tsx", '<div className="bg-gradient-to-r from-indigo-500 to-purple-600" />'], ["a.tsx", '<div className="bg-gradient-to-r from-blue-600 to-sky-500" />']],
  "gradient-text": [["a.css", "h1 { background-clip: text; }"], ["a.css", "h1 { background-clip: padding-box; }"]],
  "decorative-blur": [["a.tsx", '<div className="rounded-2xl backdrop-blur-md">x</div>'], ["a.tsx", '<nav className="sticky top-0 backdrop-blur-md">x</nav>']],
  "glow": [["a.css", ".b { box-shadow: 0 0 24px #a855f7; }"], ["a.css", ".b { box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12); }"]],
  "side-stripe": [["a.tsx", '<div className="border-l-4 border-amber-500">x</div>'], ["a.tsx", '<div className="border-l border-zinc-200">x</div>']],
  "grid-background": [["a.css", ".g { background-image: linear-gradient(to right, #e5e7eb 1px, transparent 1px); }"], ["a.css", ".g { background-image: linear-gradient(180deg, var(--bg), var(--panel)); }"]],
  "stripes": [["a.css", ".s { background: repeating-linear-gradient(45deg, #000 0 2px, transparent 2px 8px); }"], ["a.css", ".s { background: var(--panel); }"]],
  "gray-on-color": [["a.tsx", '<div className="bg-emerald-600 text-slate-400">x</div>'], ["a.tsx", '<div className="bg-emerald-600 text-white">x</div>']],
  "uniform-card-chrome": [["a.tsx", Array(4).fill('<div className="rounded-2xl shadow-lg">x</div>').join("\n")], ["a.tsx", '<div className="rounded-2xl shadow-lg">x</div>']],
  "raw-color": [["a.tsx", '<p className="text-zinc-500" style={{ color: "#333" }}>x</p>'], ["a.css", ":root { --ink: #333333; }"]],
  "default-font": [["a.css", "body { font-family: Inter, sans-serif; }"], ["a.css", 'body { font-family: "IBM Plex Sans", sans-serif; }']],
  "emoji-icon": [["a.tsx", 'const cats = { growth: { icon: "📈" } };'], ["a.tsx", "<p>We shipped it 🎉 on Friday</p>"]],
  "sparkles": [["a.tsx", "<Sparkles className=\"h-4 w-4\" /> Ask AI"], ["a.tsx", "<Search className=\"h-4 w-4\" /> Search"]],
  "reveal-everywhere": [["a.tsx", Array(3).fill("<motion.div whileInView={{ opacity: 1 }} />").join("\n")], ["a.tsx", "<motion.div whileInView={{ opacity: 1 }} />"]],
  "bounce-easing": [["a.css", ".p { transition: transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1); }"], ["a.css", ".p { transition: transform 300ms cubic-bezier(0.23, 1, 0.32, 1); }"]],
  "transition-all": [["a.css", ".p { transition: all 200ms ease; }"], ["a.css", ".p { transition: opacity 200ms ease; }"]],
  "layout-transition": [["a.css", ".p { transition: height 200ms ease; }"], ["a.css", ".p { transition: transform 200ms ease; }"]],
  "scale-zero": [["a.css", ".p { transform: scale(0); }"], ["a.css", ".p { transform: scale(0.95); }"]],
  "ease-in": [["a.css", ".p { transition: opacity 200ms ease-in; }"], ["a.css", ".p { transition: opacity 200ms ease-in-out; }"]],
  "no-reduced-motion": [["a.css", "@keyframes rise { from { opacity: 0; } }\n.p { animation: rise 1s; }"], ["a.css", "@keyframes rise { from { opacity: 0; } }\n.p { animation: rise 1s; }\n@media (prefers-reduced-motion: reduce) { .p { animation: none; } }"]],
};

function selfTest(write) {
  let ok = true;
  for (const rule of RULES) {
    const plant = PLANTS[rule.rule];
    if (!plant) { write(`  BROKEN  lint:${rule.rule} has no planted defect`); ok = false; continue; }
    const [dirty, clean] = plant.map(([rel, text]) => lintFiles([{ rel, text: text + "\n" }], { ratchet: true }).findings);
    const caught = dirty.some((f) => f.rule === rule.rule);
    const quiet = !clean.some((f) => f.rule === rule.rule);
    if (caught && quiet) write(`  caught  lint:${rule.rule} (${rule.id} ${rule.severity}), quiet on its clean twin`);
    else {
      ok = false;
      write(`  MISSED  lint:${rule.rule}: ${caught ? "" : "did not fire on its plant"}${!caught && !quiet ? "; " : ""}${quiet ? "" : "fired on its clean twin"}`);
    }
  }
  for (const name of Object.keys(PLANTS)) {
    if (!BY_RULE.has(name)) { write(`  BROKEN  a plant for lint:${name}, which is not a rule`); ok = false; }
  }
  let text = null;
  try { text = fs.readFileSync(CATALOGUE, "utf8"); } catch (e) { text = null; }
  if (text === null) {
    write(`  BROKEN  the catalogue is not readable at ${CATALOGUE}`);
    ok = false;
  } else {
    const { rows, problems } = catalogueSync(text);
    for (const p of problems) write(`  MISSED  catalogue: ${p}`);
    if (problems.length) ok = false;
    else write(`  catalogue: ${rows.length} markers, ${RULES.length} lint rules, every rule has a row and every lint row has a rule`);
  }
  write(ok ? `self-test passed: ${RULES.length} rules` : "self-test FAILED");
  return ok ? 0 : 1;
}

// ------------------------------------------------------------------ the command

function catalogueVersion() {
  try {
    const m = fs.readFileSync(CATALOGUE, "utf8").match(/Catalogue version: (\d{4}-\d{2}-\d{2})/);
    return m ? m[1] : "unknown";
  } catch (e) {
    return "unreadable";
  }
}

/**
 * opts: {dir, json, ratchet, includeTests}; io: {out(line), err(line)}.
 * Returns the exit code; never calls process.exit itself.
 */
function runLint(opts, io) {
  const root = path.resolve(opts.dir);
  let st = null;
  try { st = fs.statSync(root); } catch (e) { st = null; }
  if (!st || !st.isDirectory()) {
    io.err(`sheleg-design-skill --lint: ${opts.dir} is not a directory`);
    return 2;
  }
  let budget = null;
  if (opts.ratchet) {
    const bpath = path.resolve(opts.ratchet);
    if (fs.existsSync(bpath)) {
      try { budget = JSON.parse(fs.readFileSync(bpath, "utf8")); } catch (e) {
        io.err(`sheleg-design-skill --lint: ${opts.ratchet} is not valid JSON (${e.message})`);
        return 2;
      }
      const bad = !budget || typeof budget !== "object" || Array.isArray(budget) ||
        Object.values(budget).some((v) => !Number.isInteger(v) || v < 0);
      if (bad) {
        io.err(`sheleg-design-skill --lint: ${opts.ratchet} must map each file to a whole number of findings, like {"src/app/page.tsx": 3}`);
        return 2;
      }
    }
  }
  const { files, skipped } = walk(root, opts.includeTests);
  if (!files.length) {
    io.err(`sheleg-design-skill --lint: nothing to lint under ${opts.dir} — no html, css, scss, js, jsx, ts, tsx, vue, svelte or astro file outside node_modules, build output, hidden directories${opts.includeTests ? "" : " and tests"}`);
    return 2;
  }
  const { findings, waived } = lintFiles(files, { ratchet: Boolean(opts.ratchet) });

  const counts = {};
  for (const f of findings) counts[f.file] = (counts[f.file] || 0) + 1;

  if (opts.ratchet && budget === null) {
    io.out(JSON.stringify(counts, null, 2));
    io.err(`sheleg-design-skill --lint: no budget at ${opts.ratchet}. The JSON above is today's count per file; save it there to start the ratchet. From then on a file may only lose findings.`);
    return 2;
  }

  const bySev = { S1: 0, S2: 0, S3: 0 };
  for (const f of findings) bySev[f.severity]++;
  const over = [];
  const under = [];
  if (budget) {
    for (const [file, n] of Object.entries(counts)) {
      const allowed = Object.prototype.hasOwnProperty.call(budget, file) ? budget[file] : 0;
      if (n > allowed) over.push(`${file} ${n} > budget ${allowed}`);
    }
    for (const [file, allowed] of Object.entries(budget)) {
      const n = counts[file] || 0;
      if (n < allowed) under.push(`${file} ${n} < budget ${allowed}`);
    }
  }

  if (opts.json) {
    io.out(JSON.stringify(findings, null, 2));
  } else {
    io.out(`sheleg-design lint — ${files.length} file${files.length === 1 ? "" : "s"} read, catalogue ${catalogueVersion()}${opts.includeTests ? ", tests included" : ""}`);
    for (const f of findings) io.out(`${f.file}:${f.line}  lint:${f.rule}  ${f.severity}  ${f.id}  ${f.snippet}`);
    io.out(`${bySev.S1} S1, ${bySev.S2} S2, ${bySev.S3} S3, ${waived} waived${skipped.large ? `, ${skipped.large} file(s) over 2 MB not read` : ""}. Rows marked review in SLOP_MARKERS.md are not checked by this command.`);
  }
  for (const o of over) io.err(`ratchet: ${o} — over budget`);
  for (const u of under) io.err(`ratchet: ${u} — lower the budget to lock the gain in`);
  if (opts.json && waived) io.err(`${waived} waived`);

  const code = bySev.S1 > 0 || over.length > 0 ? 1 : 0;
  if (!opts.json) {
    const why = [bySev.S1 ? `${bySev.S1} S1 finding(s)` : "", over.length ? `${over.length} file(s) over the ratchet budget` : ""].filter(Boolean).join(" and ");
    io.out(code ? `exit 1: ${why}` : "exit 0: no S1 finding" + (budget ? ", every file inside its budget" : ""));
  }
  return code;
}

module.exports = { RULES, PLANTS, lintFiles, walk, parseCatalogue, catalogueSync, selfTest, runLint, stripComments };
