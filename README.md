# SHELEG Design — agent skill

[![npm version](https://img.shields.io/npm/v/sheleg-design-skill)](https://www.npmjs.com/package/sheleg-design-skill)
[![CI](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

> A motion + particle interface methodology for cinematic, scroll-driven
> landing pages, plus locked visual style packs for product UI — packaged as an
> installable agent skill for Cursor and Claude.

Install it into any project with one command:

```bash
npx sheleg-design-skill
```

That drops the skill bundle — `SKILL.md`, the `SHELEG_DESIGN.md` reference, the
style packs and their ready-made token CSS — into your project so your coding
agent can discover the skill and build on its principles.

## What is SHELEG Design?

A page feels *alive* not from many animations, but from a **single source of
truth** (scroll position) driving **many cheap, layered responses** that are
individually quiet and collectively cinematic. One scroll "clock" feeds a WebGL
particle field, a 2D fallback, attention dimming, parallax, scrubbed
instruments, and a progress rail — each an independent, degrade-to-calm layer.
Nothing crossfades; things *redeploy*. The result reads as one precision
instrument responding to your hand.

It was reverse-engineered from a production landing page (a 14-scene particle
narrative that morphs through formations and culminates in a brand "N" that
charges and bursts). The skill distills the architecture and the principles so
an agent can rebuild that level on a new site.

### The five principles

1. **One clock.** All motion derives from one measured scroll state.
2. **Read per frame, notify rarely.** Hot consumers read imperatively; only
   coarse changes hit the framework's render path.
3. **Hold, then redeploy.** Hold a formation ~80% of a section, then morph in a
   short, phase-staggered, arc-curved wave. No crossfades.
4. **Earned motion.** Scrub is for instruments that narrate state over time;
   entrance motion stays sub-500ms and never gates content.
5. **Degrade to calm.** Reduced-motion / coarse pointer / no-WebGL collapse to a
   static, fully-legible page.

## Usage

```bash
# Auto-detect (.cursor/ or .claude/), default to .cursor/skills/sheleg-design/
npx sheleg-design-skill

# Force a flavor
npx sheleg-design-skill --cursor
npx sheleg-design-skill --claude

# Custom location
npx sheleg-design-skill --dir docs/skills/sheleg-design

# Overwrite an existing install
npx sheleg-design-skill --force

# Help
npx sheleg-design-skill --help
```

### Other install paths

```bash
# Claude Code plugin (adds the /sheleg-design command too)
/plugin marketplace add ssheleg/sheleg-design-skill
/plugin install sheleg-design@sheleg-design-skill

# vercel-labs skills CLI (70+ agents)
npx skills add ssheleg/sheleg-design-skill

# POSIX fallback, no Node
curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
```

### What gets installed

| File | Purpose |
|---|---|
| `SKILL.md` | Agent-facing skill: discovery trigger, the principles, how to apply them, quick-reference rules, common mistakes |
| `SHELEG_DESIGN.md` | The full reference: architecture, layer-by-layer mechanics with code, the exact morph math, the DOM↔WebGL projection bridge, a build-from-scratch recipe, and the "why it works" |
| `styles/*.md` | Style packs — the visual identity layer: `instrument-console` (near-black console, electric-blue signal), `editorial-luxury` (warm cream/espresso/sage, dossier motifs), and `workbench` (quiet light/dark product UI for dashboards & tools, standalone). Each locks palette, type, texture, motion tokens, motifs, and bans |
| `styles/tokens/*.css` | The ready-made token layer per pack — copied verbatim into a project instead of transcribing tables (workbench ships a light `:root` plus a `data-theme="dark"` twin) |
| `styles/STYLE_PACK_TEMPLATE.md` | The pack contract as a skeleton, so a new style is authored against the same headings instead of invented ad hoc |

After installing, a Cursor or Claude agent in that project can discover the
skill and use it when you ask it to build or upgrade a cinematic,
scroll-driven page — or to style product UI (dashboards, admin panels,
internal tools) from the `workbench` pack, without any of the motion layer.

## Style-agnostic motion, pluggable identity

The motion methodology (one clock, layered responses, degrade-to-calm) is
independent of the visual style. The look comes from a **style pack** the
agent picks per project — dark instrument console, warm editorial luxury, or
quiet light/dark workbench out of the box, or a new pack authored against the
same contract. Where a pack sets its own ease and durations, the pack wins;
the motion layer never hard-codes a palette.

## Pairs well with: Lazyweb MCP (optional)

A style pack locks *how it looks*. It says nothing about what a good version of
the screen you're about to build actually contains — which is where generated
product UI usually goes wrong twice over. If the [Lazyweb](https://www.lazyweb.com)
MCP server is connected, the skill will sweep real-world references for the
target screen (signup, onboarding, paywall, pricing, checkout, dashboard,
settings) before laying anything out, then map what it finds onto the pack's
tokens.

The division of labour is deliberate: references inform **layout, hierarchy and
content order**; palette, type and motion stay the pack's, so the result still
reads as one system rather than a collage. Setup is a Streamable HTTP MCP server
plus a per-user token (keep it out of your repo). Entirely optional — nothing in
the skill depends on it, and it degrades to "work from the pack alone".

## Stack-agnostic

The skill teaches **principles and architecture**, not a fixed dependency set.
The reference implementation happens to use Next.js + React + three /
react-three-fiber + GSAP ScrollTrigger + Lenis + Framer Motion, but the method
applies to any stack that can render to a canvas/WebGL surface and read scroll.

## Zero dependencies

The installer is a single zero-dependency Node script, so `npx` runs instantly
with no install step and no supply-chain surface.

## Development

`python3 test/validate.py` checks repo consistency: manifests, version sync,
skill/command/rule front-matter and description canon, the full style-pack
section contract, pack ↔ `SKILL.md` table ↔ CLI-help agreement, the bundled
pack template against `templates/`, installer file lists, the whole
`.cursor/` mirror against the plugin copy, and relative links. CI runs it
plus a CLI smoke test on every push and PR, including a negative self-test
(the validator must fail on a corrupted version).

Versioning is semver; bump `marketplace.json` + `plugin.json` +
`package.json` + `CHANGELOG.md` together — the validator enforces the sync.
`test/scenarios.md` (T1–T7) is the behavioural harness: re-run the affected
scenarios after any edit to `SKILL.md`, a pack, or the reference.

## What this gives you

An agent can generate a landing page in under a minute, and it will look like
every other generated landing page: three cards, a gradient, a hero that does
nothing. This is the taste layer.

- **A motion methodology, not a component dump.** Scroll-linked animation,
  particle and WebGL backgrounds, parallax layers that stay in sync instead of
  drifting apart as the page grows.
- **Style packs for product UI** — dashboards, admin panels, internal and dev
  tools — with design tokens and light/dark handled up front rather than
  retrofitted.
- **A diagnosis for pages that feel busy or janky**, naming which layer to cut
  instead of telling you to "simplify".
- **Stack-agnostic and dependency-free** — it is a way of building, not a
  framework you now depend on.

## Author

Built by ssheleg — [sshlg.me](https://sshlg.me)

- X / Twitter — [@fuck_this_year](https://x.com/fuck_this_year)
- Telegram — [@sshlg](https://t.me/sshlg)

Part of the [ssheleg skill family](https://github.com/ssheleg/sshlg-skills):
`super-ux`, `task-pipeline`, `make-skill`, `sheleg-design`, `seo-aeo-audit`.
One command installs all five for every agent you use:

```bash
npx sshlg-skills install
```

## License

MIT © ssheleg
