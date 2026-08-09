# SHELEG Design — design taste as an agent skill

[![npm version](https://img.shields.io/npm/v/sheleg-design-skill)](https://www.npmjs.com/package/sheleg-design-skill)
[![CI](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

An agent can generate a landing page in under a minute, and it will look like
every other generated landing page: three cards, a gradient, a hero that does
nothing. Ask it for a dashboard and you get a different flavor of the same
problem — invented colors, six accent hues, dark mode retrofitted later.

This skill is the taste layer. It gives a coding agent **one motion
methodology** for cinematic, scroll-driven pages and **six locked style
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

**Style packs** — the visual identity, pluggable per project. Two of them are
meant to be used **standalone**, with none of the motion layer: `workbench`
(quiet light/dark product UI for dashboards, admin panels, internal and dev
tools) and `briefing-room` (a dark 16:9 presentation deck, where the presenter's
voice is the timeline and slides therefore never animate).

| Pack | Look | Choose for |
|---|---|---|
| `instrument-console` | near-black aerospace console, one electric-blue signal, mono telemetry | technical / systems / infra |
| `editorial-luxury` | warm cream + espresso ink, sage accent, Fraunces/Newsreader, dossier motifs | editorial / research / premium B2B |
| `workbench` | neutral grays, borders as elevation, one blue accent, mono data, light + dark twins | dashboards, admin, internal & dev tools |
| `briefing-room` | dark 16:9 deck: one blue hue top to bottom (OKLCH), mono slide furniture, 1-bit dithered art, claims as titles | investor & board decks, technical briefings, talks published as a page |
| `atrium` | warm cream daylight field with no dark bands, one terracotta accent, light serif with italic asides, fluted-glass hero over photography | consumer health, longevity & diagnostics, wellness, premium care, high-trust DTC |
| `orchard` | warm oat field of rounded slabs, sage brand + one candy-orange action, rounded geometric display, soft-3D pills built from inset light | friendly consumer biotech, DTC wellness, testing kits & supplements |
| `field-notes` | warm green-cast paper ruled by hairlines, one rust accent, a hero that dissolves into the page instead of ending, numbered mono eyebrows, crop marks, colour that encodes how a claim is known | open-source & developer tools sold on auditability — code intelligence, provenance, evals, agent memory |
| `showroom` | white gallery, near-black ink, one blue that works as link and as fill, Inter Display + Inter + JetBrains Mono, a seven-layer shadow framing one real product surface | product-led companies whose best argument is the application on screen |
| `blueprint` | white drawing stock, 32px grid, ruled column edges, corner registration marks, one electric blue, zero radius anywhere | infrastructure sold on precision — vector databases, search, storage and query engines |
| `prism` | one static iridescent wash with a hard bottom edge, heavy grotesque display over mono body copy, cyan as a fill only | an open-source project's front door, where the first action is a command |
| `maquette` | near-black table, cream ink and cream axonometric models, mono block labels, pale aqua that works as text, one offset shadow | enterprise data infrastructure sold to an architecture buyer |
| `cyclorama` | a pale field cycling through six pastel stops on a 32s loop under near-black ink that never moves with it, a monospaced typewriter serif over mono, one orange used only as a fill, a particle organ that holds then redeploys, no shadows anywhere | enterprise AI transformation, applied-AI services, technical consultancies — where what is sold is a change of state and there is no screenshot worth showing |

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
the skill is documentation an agent reads. The React reference kits are the one
thing that is code, and they are deliberately **not** installed — they ship in
the npm package and only appear when you ask for one by name (see *Claude
Design*, below).

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
| `DESIGN_SYNC_BRIDGE.md` | The Claude Design contract: what a pack sends to claude.ai/design and in what shape, the rule for each of the four reference types, and the border motion does not cross |
| `FIGMA_BRIDGE.md` | The design↔code contract: how a pack's tokens map onto Figma variable collections and modes, how to implement a design without importing raw values, and what cannot cross the border |
| `AI_PRODUCT_PATTERNS.md` | The surfaces a model drives: the five states of a call, streaming instead of spinners, latency, provenance and uncertainty, agent confirmations, and the bans that keep it honest |
| `styles/*.md` | The twelve style packs — palette, type, texture, motion tokens, motifs, bans, and the traps each one carries |
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

## AI product surfaces

Chat, agent runs, streaming output and generated content are the surfaces most
design systems were written before — and the ones everyone is now building.
`AI_PRODUCT_PATTERNS.md` covers them with one organizing rule, **honest state**:
a model's output is slow, uncertain, occasionally refused and sometimes wrong,
and an interface that hides any of that is not calmer, it is lying.

Concretely: five states per call, not two (idle · working · complete · refused ·
failed — a refusal is not an error and a rate limit is not a crash); streaming
instead of spinners, with a stop control from the first frame and no reflow; the
context the model actually used, because most "wrong answer" reports are
wrong-context reports; an agent's action shown in the shape it will take before
it runs; and no confidence number with nothing behind it.

This is where the skill's positioning is externally measured rather than
asserted: in Figma's *State of the Designer 2026* (NewtonX, 906 designers,
Sept–Oct 2025), designing AI-driven products is the **third most in-demand
skill (37%)** — ahead of motion design and information architecture — while
**visual polish tops the list at 58%**, and craft is named the differentiator
now that anyone can prompt their way to a prototype.

## Figma, in both directions

Design files and design tokens are two encodings of one system, and the usual
outcome is that they drift until nobody trusts either. The skill's rule is that
**the pack is the source of truth on both sides**: publishing writes a pack's
values into Figma variable collections; implementing a design maps the file's
values *onto* the pack's tokens instead of inlining hexes.

The bridge is specific because the traps are: `workbench`'s light and dark are
two **modes of one collection**, while `editorial-luxury`'s espresso sections
are surfaces and not a mode at all; Figma colors are 0..1 floats, not hex; and
motion never crosses — Figma has no easing variable type, so the ease, durations
and stagger stay code-only, and shadows are effect styles whose parts bind to
variables. A value in a file with no matching token is either a gap in the pack
or drift in the file — the one thing it is never is a literal in a component.

## Claude Design, in one direction

claude.ai/design is a design agent that builds working UI from real React. Out of
the box it builds with generic components — three cards, a gradient, a hero that
does nothing — which is the failure this skill exists to prevent. Push a pack and
it builds from that pack's real parts instead.

```bash
npx sheleg-design-skill --kit workbench --out ./ds-workbench
cd ./ds-workbench && npm install && npm run build
```

then `/design-sync` in that directory, from Claude Code. Three layers cross: the
pack's **bans** as the design system's own README, `styles.css` built from
`tokens/<pack>.css` verbatim, and the components — a six-name spine that is
identical in all six kits, so switching packs swaps identity rather than API,
plus each pack's signature parts. **Motion does not cross**, exactly as it does
not cross into Figma: a kit is the static half of a pack, and saying so is what
stops an agent inventing motion to fill the silence.

The kits are not part of the install. `--kit` fetches one on demand, which is how
the skill stays documentation while still having real components to hand.

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

Adding a style pack, or anything else: see [CONTRIBUTING.md](./CONTRIBUTING.md)
and the [Code of Conduct](./CODE_OF_CONDUCT.md). To report a vulnerability, see
[SECURITY.md](./SECURITY.md).

## Author

Built by ssheleg — [sshlg.me](https://sshlg.me)

- X / Twitter — [@sshlg93](https://x.com/sshlg93)
- Telegram — [@sshlg](https://t.me/sshlg)

Part of the [ssheleg skill family](https://github.com/ssheleg/sshlg-skills):
`super-ux`, `task-pipeline`, `agent-sync`, `make-skill`, `sheleg-design`, `seo-aeo-audit`.
**The family installs and updates as one package**, for every agent you use — a bundle with one
member current and the rest stale is a combination nobody tested:

```bash
npx sshlg-skills install              # nothing installed yet — the whole family, any agent
npx sshlg-skills update               # installed but behind — updates everything
npx --yes sshlg-skills@latest list    # what the current release of each member is
```

Restart your agent afterwards: skills and hooks load at session start, so the session that
updates is not the session that gets the new ones.

## License

MIT © ssheleg
