# SHELEG Design — design taste as an agent skill

[![npm version](https://img.shields.io/npm/v/sheleg-design-skill)](https://www.npmjs.com/package/sheleg-design-skill)
[![CI](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

An agent can generate a landing page in under a minute, and it will look like
every other generated landing page: three cards, a gradient, a hero that does
nothing. Ask it for a dashboard and you get a different flavor of the same
problem — invented colors, six accent hues, dark mode retrofitted later.

This skill is the taste layer. It gives a coding agent **one motion
methodology** for cinematic, scroll-driven pages and **three locked style
packs** with ready-made design tokens, so what it builds reads as one system
instead of a pile of effects.

```bash
npx sheleg-design-skill
```

That drops the bundle — `SKILL.md`, the `SHELEG_DESIGN.md` reference, the style
packs and their token CSS — into `.cursor/skills/` or `.claude/skills/`, where
your agent discovers it on its own.

---

## The two halves

**Motion** — for landings, heroes, scroll narratives. A page feels *alive* not
from many animations but from a **single source of truth** (measured scroll
position) driving **many cheap, layered responses** that are individually quiet
and collectively cinematic. One scroll "clock" feeds a WebGL particle field, a
2D fallback, attention dimming, parallax, scrubbed instruments and a progress
rail — each an independent, degrade-to-calm layer. Nothing crossfades; things
*redeploy*.

**Style packs** — the visual identity, pluggable per project. The `workbench`
pack is meant to be used **standalone**, with none of the motion layer: quiet
light/dark product UI for dashboards, admin panels, internal and dev tools.

| Pack | Look | Choose for |
|---|---|---|
| `instrument-console` | near-black aerospace console, one electric-blue signal, mono telemetry | technical / systems / infra |
| `editorial-luxury` | warm cream + espresso ink, sage accent, Fraunces/Newsreader, dossier motifs | editorial / research / premium B2B |
| `workbench` | neutral grays, borders as elevation, one blue accent, mono data, light + dark twins | dashboards, admin, internal & dev tools |

Each pack locks palette, type, texture, motion tokens, signature motifs and
bans — and ships a `tokens/<pack>.css` to copy verbatim, so the agent never
invents a hex. Where a pack sets its own ease and durations, the pack wins; the
motion layer never hard-codes a palette.

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

The method was reverse-engineered from a production landing page — a 14-scene
particle narrative that morphs through formations and ends in a brand glyph that
charges and bursts — then generalized so an agent can rebuild that level
anywhere.

## Install

Requires Node ≥ 16 for the installer. Nothing is added to your dependencies:
the skill is documentation an agent reads.

```bash
# Auto-detect (.cursor/ or .claude/), default .cursor/skills/sheleg-design/
npx sheleg-design-skill

# Pick the target explicitly
npx sheleg-design-skill --cursor
npx sheleg-design-skill --claude
npx sheleg-design-skill --dir docs/skills/sheleg-design

# Overwrite an existing install / see all options
npx sheleg-design-skill --force
npx sheleg-design-skill --help
```

Other channels:

```bash
# Claude Code plugin — adds the /sheleg-design command too
/plugin marketplace add ssheleg/sheleg-design-skill
/plugin install sheleg-design@sheleg-design-skill

# vercel-labs skills CLI
npx skills add ssheleg/sheleg-design-skill

# POSIX fallback, no Node
curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
```

Cursor rules users: `cursor/rules/sheleg-design.mdc` is a self-contained
condensed version — copy it into `.cursor/rules/` if you prefer rules over
skills.

### What gets installed

| File | Purpose |
|---|---|
| `SKILL.md` | The agent-facing skill: discovery triggers, the principles, how to apply them, quick-reference rules, common mistakes |
| `SHELEG_DESIGN.md` | The full reference: architecture, layer-by-layer mechanics with code, the exact morph math, the DOM↔WebGL projection bridge, a build-from-scratch recipe, and why each piece works |
| `styles/*.md` | The three style packs — palette, type, texture, motion tokens, motifs, bans, and the traps each one carries |
| `styles/tokens/*.css` | The ready-made token layer per pack, copied verbatim instead of transcribed (workbench ships a light `:root` plus a `data-theme="dark"` twin) |
| `styles/STYLE_PACK_TEMPLATE.md` | The pack contract as a skeleton, so a new style is authored against the same headings rather than improvised |

## What you get out of it

- **A motion methodology, not a component dump.** Scroll-linked animation,
  particle and WebGL backgrounds, parallax layers that stay in phase instead of
  drifting apart as the page grows.
- **Product UI with the boring parts already decided** — tokens, light/dark,
  elevation, state colors, data typography — up front rather than retrofitted.
- **A diagnosis for pages that feel busy or janky**, naming which layer to cut
  instead of telling you to "simplify".
- **Stack-agnostic and dependency-free.** The reference implementation happens
  to use Next.js + React + three / react-three-fiber + GSAP ScrollTrigger +
  Lenis, but the method applies to any stack that can render to a canvas and
  read scroll. It is a way of building, not a framework you now depend on.

## Optional: Lazyweb MCP

A style pack locks *how it looks*. It says nothing about what a good version of
the screen you're about to build actually **contains**. If the
[Lazyweb](https://www.lazyweb.com) MCP server is connected, the skill sweeps
real-world references for the target screen (signup, onboarding, paywall,
pricing, checkout, dashboard, settings) before laying anything out.

The division of labor keeps the result one system: references inform **layout,
hierarchy and content order**; palette, type and motion stay the pack's. Setup
is a Streamable HTTP MCP server plus a per-user token — keep it out of your
repo. Entirely optional; without it the skill works from the pack alone.

## Development

```bash
python3 test/validate.py   # or: npm test
```

The validator is the repo's contract, not a formality — it checks manifests and
four-way version sync, skill/command/rule front-matter and description canon,
the full style-pack section contract, pack ↔ `SKILL.md` ↔ CLI-help agreement,
the bundled template against `templates/`, both installers' file lists, the
entire `.cursor/` mirror against the plugin copy, and every relative link. CI
runs it on each push and PR alongside a negative self-test (the validator must
fail on a corrupted version) and installs the bundle through **both** installers,
diffing the result against the source.

`test/scenarios.md` (T1–T7) is the behavioral harness: fresh subagents given a
task, checking that the skill is discovered, applied and quoted correctly.
Re-run the affected scenarios after any edit to `SKILL.md`, a pack or the
reference.

Adding a style pack, or anything else: see [CONTRIBUTING.md](./CONTRIBUTING.md).

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
