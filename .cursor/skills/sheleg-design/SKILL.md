---
name: sheleg-design
description: Use when deciding how something LOOKS or MOVES — cinematic landing pages and hero sections, particle/WebGL backgrounds, scroll-linked or scrubbed motion, layers that drift, dashboards, admin or internal tools, mobile screens, chat or agent interfaces, tokens, themes, palettes, typography and the Figma border. Triggers: "design a landing" / "дизайн лендинга", "build a landing page" / "сделай лендинг", "scroll animation" / "скролл-анимация", "dashboard style" / "стиль дашборда", "design tokens, style pack" / "дизайн-токены", "light/dark theme" / "светлая/тёмная тема", "figma variables" / "переменные фигмы, фигма в код", "mobile screen" / "мобильный экран", "palette, colors" / "палитра, цвета", "typography, font" / "типографика, шрифт", "how it looks, make it prettier" / "выглядит, красиво, красивее", "visual reference" / "визуальные референсы", "investor deck as a web page" / "веб-презентация". Not for structure, copy, backend behavior, or .pptx decks.
license: MIT
compatibility: Optional siblings — dataviz, shadcn, migrate-radix-to-base; each has an in-text fallback when absent.
metadata:
  version: 1.57.0
---

# SHELEG Design

## Overview

A page feels cinematic not from many animations, but from a **single source of
truth** (measured scroll position) driving **many cheap, layered,
independently-degradable responses**. Centralize scroll into one store; layers
read it per frame and react in their own language. Nothing crossfades — things
*redeploy*. Every layer degrades to a calm static state.

**REQUIRED REFERENCE — for the cinematic path:** read
[`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md) before implementing a scroll-driven page —
architecture, morph math, the DOM↔WebGL bridge, the build recipe (§11), the file map.
**Product-UI work does not owe this read**; the one rule it would owe is repeated
here: where a pack's motion tokens differ from the SHELEG defaults, **the pack wins**.

**REQUIRED BEFORE ANY ANIMATION:** read
[`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md). `SHELEG_DESIGN.md` says how motion
is built; the doctrine says whether to build it — the frequency table that kills
animation on high-repetition paths, the easing tree and the `ease-in` ban, the
duration ceiling, the forbidden forms, and the reduced-motion contract.

## When to Use

- Landing/marketing/hero pages where motion is a stated goal; particle or WebGL
  backgrounds tied to scroll; scroll-linked charts, step flows, rails, parallax
- An existing scroll site that feels nervous, janky, or out of phase
- Product UI needing a locked visual system — dashboards, admin, internal/dev tools,
  tokens, light/dark — **style-pack only**, via [`workbench`](./styles/workbench.md)
- AI product surfaces: chat and agent UI, streaming output, run logs, model errors,
  generated-content and confirmation states ([`AI_PRODUCT_PATTERNS.md`](./AI_PRODUCT_PATTERNS.md))
- Moving a visual system across the Figma border either way ([`FIGMA_BRIDGE.md`](./FIGMA_BRIDGE.md))
- Motion that has to leave the page as a rendered file — a launch video, a feature
  loop, a social cut ([`MOTION_PRODUCTION.md`](./MOTION_PRODUCTION.md)), which also
  names the two programmatic-video tools and which one to reach for

**Never apply the cinematic motion layer to:** product UI, docs sites, static content
sites — or any page whose visual system or copy isn't finished yet. Product UI takes
the style-pack half and nothing else.

## Core Pattern — five principles, in order

1. **One clock.** All motion derives from one measured scroll state; no layer
   measures scroll itself, so layers can never drift out of phase.
2. **Read per frame, notify rarely.** Hot consumers (WebGL/canvas/rail) read
   the store imperatively, zero framework renders; only coarse act/section
   changes notify the framework.
3. **Hold, then redeploy.** Hold a formation ~80% of a section, then morph in a
   short, phase-staggered, arc-curved wave. Crossfades are banned.
4. **Earned motion.** Scrub only for instruments that narrate state over time;
   hover and press stay inside the doctrine's bands, an entrance may run past
   them when measured, and neither ever gates content.
5. **Degrade to calm.** Reduced-motion / coarse pointer / no-WebGL collapse to
   a static, fully-legible page. The effect is a bonus, never a dependency.

## Style packs

The visual identity comes from a style pack. Before choosing one, read
[the style-pack index](./STYLE_PACK_INDEX.md); then read the chosen pack in full
and copy its token layer from `styles/tokens/<pack>.css`. Do not transcribe token
tables or infer values from screenshots.

A materialized kit supplies component states:

```bash
npx sheleg-design-skill --kit <pack>
```

The generated `src/styles.css` is authoritative for states a core pack leaves
open. A widened pack's kit and `## Components` section must agree. To author a
pack, start from
[`styles/STYLE_PACK_TEMPLATE.md`](./styles/STYLE_PACK_TEMPLATE.md) and ship its
token file in the same change.
## Calibration — three dials

A pack answers *which register*. It does not answer *how far*. Two landing
pages on the same pack, one for a regulated insurer and one for a design
studio, are not the same page. Three dials carry that difference, and they are
set once, out loud, before any layout exists.

- **`DESIGN_VARIANCE`** 1–10 — 1 is perfect symmetry, 10 is deliberate
  asymmetry and no two sections alike.
- **`MOTION_INTENSITY`** 1–10 — 1 is static, 10 is cinematic and physical.
- **`VISUAL_DENSITY`** 1–10 — 1 is a gallery wall, 10 is a cockpit.

**Baseline `7 / 5 / 4`.** State the values and one line of reasoning before
building; do not ask the user to edit a file, and do not silently drift from
what you announced.

### Reading them off the brief

| The brief reads as | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| minimalist, calm, editorial, "quiet like Linear" | 5–6 | 3–4 | 2–3 |
| premium consumer, brand-led, "feels expensive" | 7–8 | 5–7 | 3–4 |
| agency, portfolio, experimental, award-bait | 9–10 | 7–9 | 3–4 |
| landing / marketing page, no further signal | 7 | 5 | 4 |
| product UI: dashboards, admin, internal tools | 4–5 | 2–3 | 6–8 |
| trust-first: regulated, public-sector, clinical | 3–4 | 2–3 | 4–5 |
| presentation deck | 5–6 | 1–2 | 3–4 |
| redesign, preserve the existing identity | match | match +1 | match |
| redesign, explicit overhaul | +2 | +2 | match |

**A brief can match two rows, and they can disagree by a factor of three.** "A quiet
internal admin dashboard" fires both *"quiet like Linear"* (DENSITY 2–3) and *"product
UI"* (DENSITY 6–8). The precedence rule: **the row that names the surface wins over the
row that names a mood.** A surface decides how much has to fit; a mood decides how it is
handled — in a product-UI pack, "quiet" is bought with restraint in colour and motion,
not with emptiness. Say which row you took and why when two fire.

**A row that names neither is an audience posture** — *"trust-first: regulated,
public-sector, clinical"* names who reads it, not what they read it on. It does not
arbitrate DENSITY, because a posture says nothing about how much has to fit; it **wins
on MOTION and ornament**, because that is the whole of what it constrains. Both T24
branches hit this and both split two-to-one on MOTION, which is the tell that the rule
above had no third case.

### How they bind

The pack wins on values, the dials win on amount — a dial never invents a colour,
a face or a radius. **`MOTION_INTENSITY` is capped by the frequency table, not the
other way round**, and **motion claimed is motion shown**: a static page announcing
7 is broken, so drop the dial to 3 and ship a clean still page rather than
half-build motion that stalls. Several packs pin their own ceiling and say so in
their Register. The table, the per-pack ceilings and why each one is where it is:
[`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md) → *How the calibration dials bind*.

## The craft bar — what "done" means, in order

When anyone can prompt their way to a prototype, craft is the only
differentiator left. Designers rank what it means (Figma, *State of the
Designer 2026*, n=906): **visual polish 58% · thoughtful problem solving 47% ·
clear intuitive UX 36% · emotion and delight 35% · consistency 15%.** Read that
as a definition of done, in that order:

1. **Polish** — the pack applied without exception: tokens, not literals; no
   ad-hoc hex, radius or font size anywhere in the diff.
2. **Systems thinking** — the visual decision lives in one place (the token
   layer, the `SCENES` registry) and everything else reads it.
3. **Clear UX** — structure and behavior are not this skill's half; if the
   flows and states aren't decided, stop and decide them first.
4. **Emotion** — earned motion only (principle 4), and never at the cost of 1–3.
5. **Consistency** — one ease, one duration set, one accent, one atom per job
   across every screen.

## Load on demand — three things the pack layer does not decide

- **Scene depth — six layers** ([`SURFACE_COMPOSITION.md`](./SURFACE_COMPOSITION.md)),
  before writing CSS for a cinematic page. A scene has planes; everything on one
  plane is the failure no amount of easing repairs.
- **Charts — the role contract in the same file, plus the `dataviz` handoff
  where that skill exists**, before drawing a chart in any pack. Token names are
  not uniform across the thirty-nine packs — only `--bg` and `--ink` resolve in
  every one — and an undefined custom property does not error, it silently falls
  back. Guessing one is the quietest way to ship a wrong chart. A `dataviz`
  skill is an optional neighbour this skill does not ship: where none is
  installed, the role table in `SURFACE_COMPOSITION.md` IS the chart contract,
  applied by hand.
- **Mobile surfaces** ([`MOBILE_SURFACES.md`](./MOBILE_SURFACES.md)), when the
  brief is a native app screen or a mobile-web view — not a desktop page whose
  only mobile concern is collapse. Five mobile rules the packs each state alone,
  a sixth **no pack answers** (the type ramp follows viewport width, not the
  user's text size), and the half no pack decides on a phone: platform
  convention.

## Choosing between packs — mount them, don't imagine them

When more than one pack could carry a product, do not argue about it. Render
them.

Mount the candidate packs on **an existing, populated page** — real header,
real data, real density — switched by a `?variant=<pack>` search parameter, and
flip between them in the browser. Only the token layer changes; the markup
stays.

A throwaway route with placeholder content is a vacuum: every pack looks fine
in it, which is precisely why it settles nothing. If there is genuinely no
populated page yet, the choice is premature — build the page in the pack the
brief's register points at, and revisit once there is something real to switch.
If the brief gives no signal at all, the defaults are **`workbench`** for product
UI and **`showroom`** for a marketing page: both are quiet enough that switching
away later costs layout, not identity. (This used to say "the default pack" and
name none, which is not a fallback.)

The comparison harness is scaffolding, not a deliverable: it comes out with the
same change that records the decision.

## AI-driven product surfaces

An AI surface is not a normal surface: a model streams, it is wrong sometimes,
and the interface has to show both without lying about either. Streaming states,
confidence, citation, correction and the shape of a refusal are in
[`AI_PRODUCT_PATTERNS.md`](./AI_PRODUCT_PATTERNS.md), which is their single home.
Load it when the product has a model in it.

## The component layer — the pack decides the tokens, the kit renders them

A style pack is a **token layer and a set of rules**. It does not ship a button.
Every product UI therefore needs a second decision the packs deliberately do not
make: which component kit draws the controls.

**The default is `shadcn/ui`, and the question is asked once per project.** Ask it
the way `ux-foundation` asks the Figma question — once, at the point design work
starts, never per screen — and record the answer wherever the style pack is
recorded: with `super-ux` installed that is the screens record's *Design system*
line, and without it, whatever file names the pack. Default **yes**; a project
that already has a component layer has already answered, and migrating one on
taste is not a design decision.

**Why it composes rather than competes.** `shadcn/ui` is not a theme. It is
unstyled primitives plus Tailwind, themed through CSS custom properties — so it
*consumes* a token layer instead of bringing its own look. That is exactly the
seam a pack is: the pack decides what `--bg` means, the kit decides what a
`DropdownMenu` is.

**The two vocabularies are different, and this is the trap.** The packs resolve
`--bg` and `--ink` everywhere and little else by that name; `shadcn/ui` expects
`--background`, `--foreground`, `--primary`, `--muted` and the rest of its own
contract. **Map them explicitly in the pack's token file** — an undefined custom
property does not error, it silently falls back, which is the same failure the
chart rule above exists for. A kit mounted without that mapping renders in its
starter palette and looks like nobody chose anything.

**The boundary — product UI, not the cinematic surface.** Dashboards, admin
panels, internal tools, chat and agent interfaces: yes, and the answer is yes by
default. A scroll-driven landing page: **no** — there are no controls to reuse
there, the work is bespoke scroll and WebGL, and reaching for a component kit is
how a hero ends up looking like a settings screen.

**Who does the work.** This section decides *whether* and *against which tokens*.
Where the `shadcn` skill is installed it does the adding, searching and
composing, and `migrate-radix-to-base` handles the Radix→Base move; both are
**optional neighbours** this skill declares in its `compatibility` line and does
not ship, and they trigger on their own words where present. Where they are
absent nothing is blocked: the kit's own CLI (`npx shadcn@latest add
<component>`) does the adding, and the token mapping above binds either way. Do
not restate their component docs here.

## Optional — Figma (design ↔ code)

Touching a Figma file — publishing the pack as variables, or building from a
design — starts at [`FIGMA_BRIDGE.md`](./FIGMA_BRIDGE.md). It owns the contract,
including the one rule worth knowing before you open the tool: **a frame is read
by designers and stakeholders, so drawing in one is publishing**, and creating a
file needs a named destination rather than a guess.

## Optional — Claude Design (design-sync)

Where `/design-sync` is available, a pack can be pushed to claude.ai/design so the
design agent builds screens from **this pack's** tokens rather than its own
defaults. The contract, and what it does not carry across, is in
[`DESIGN_SYNC_BRIDGE.md`](./DESIGN_SYNC_BRIDGE.md).

## Optional — real-world references (Lazyweb, Mobbin, Refero)

A pack fixes *how it looks*; it does not say what a good version of the screen
contains. Where Lazyweb, Mobbin or Refero are connected, look at real products
before inventing a layout — and treat what you find as evidence about **content
and structure**, never as a licence to copy someone's visual. The full rule is
`DESIGN_SYNC_BRIDGE.md` §4.

## How to Apply

1. Visual system first: pick (or author) a style pack, apply its tokens as
   the site-wide design tokens (color, type, spacing, components). If Lazyweb
   MCP is available, sweep references for the target screen at this point —
   before any layout exists to defend.
2. Build bottom-up in the §11 layer order: scroll clock → smooth scroll →
   particle field → 2D fallback → DOM choreography → reveals → scrubbed
   instruments → optional DOM↔WebGL bridge. One small file per layer.
3. Storyboard in data: a `SCENES` registry (`{ anchor, formation, focusX,
   energy }` per section); iterate on the data before touching render loops.
4. Ship each layer's reduced-motion/fallback branch in the same commit.
5. Verify: typecheck/lint/build; screenshot each scene mid-hold and mid-morph;
   reduced-motion pass; narrow-viewport pass.

## Common Mistakes

- Paying the fallback/a11y tax "at the end" → it never ships. Same commit.
- Parallax on everything → nausea. At most one drifting figure per viewport.
- Scrub on hero/entrances → motion feels unearned; reserve scrub for
  instruments.

### Three looks that are defaults, not decisions

Left to itself, generated design lands in one of three places whatever the product
is — warm cream with a serif and terracotta; near-black with one acid accent;
broadsheet hairlines at zero radius. Each is legitimate for some brief, and each
arrives whether or not the brief called for it, which is what makes it a default.
**If a pack's field sits near one of these, that is a measurement; if a page arrives
at one without a pack, that is the default talking** — say which out loud before
shipping. The three documents, in full: [`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md).
