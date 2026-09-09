---
name: sheleg-design
description: Use when deciding how something LOOKS or MOVES — cinematic landing pages and hero sections, particle/WebGL, scrubbed motion, drift, dashboards, admin or internal tools, mobile screens, chat or agent interfaces, tokens, palettes, typography and the Figma border. Triggers - "design a landing" / "дизайн лендинга", "build a landing page" / "сделай лендинг", "scroll animation" / "скролл-анимация", "dashboard style" / "стиль дашборда", "design tokens, style pack" / "дизайн-токены", "light/dark theme" / "светлая/тёмная тема", "figma variables" / "переменные фигмы, фигма в код", "mobile screen" / "мобильный экран", "palette, colors" / "палитра, цвета", "typography, font" / "типографика, шрифт", "how it looks, make it prettier" / "выглядит, красиво, красивее", "visual reference" / "визуальные референсы", "investor deck as a web page" / "веб-презентация", "redesign" / "редизайн, свёрстай, вёрстка". Not for structure, copy, backend behavior, or .pptx decks.
license: MIT
compatibility: Kit/lane commands need node>=16, npx, network. Optional siblings — dataviz, shadcn, migrate-radix-to-base. Each has an in-text fallback when absent or unreachable.
metadata:
  version: 1.59.4
---

# SHELEG Design

## Overview

A page feels cinematic not from many animations, but from a **single source of
truth** (measured scroll position) driving **many cheap, layered,
independently-degradable responses**. Centralize scroll into one store; layers
read it per frame and react in their own language. Nothing crossfades — things
*redeploy*. Every layer degrades to a calm static state.

**READ FIRST, BEFORE ANY OF THE CRAFT BELOW:**
[`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md) — the decision layer. What the
surface is for and **what would prove it failed**; which lane and which mode the
task is in, because a redesign starts by measuring the thing it replaces and an
update changes a token rather than the components that read it; which tools to
cast, measured with `npx sshlg-skills pack design --lane <lane>` rather than
recalled; when to build **two variations with two disjoint casts in parallel
subagents** — and the rule that keeps that honest, which is that the rubric is
written before either one exists; and the validation split that matters, where
alignment to the brief and measurable quality are two different questions and
neither implies the other. **The failure mode of an agent doing design is not
ugliness, it is plausibility**, and that document is what refuses it.

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

**REQUIRED BEFORE ANY ACCESSIBILITY CLAIM:** read
[`ACCESSIBILITY_EVIDENCE.md`](./ACCESSIBILITY_EVIDENCE.md) — which bar a claim
is held to (a WCAG criterion with number/version/level/units/exceptions, or a
platform heuristic), what a screenshot can and cannot prove about the DOM and
assistive technology, and the verdict contract: an absent tool is NOT_RUN,
never PASS, and no check installs a scanner to complete itself.
The connection is **scoped, not routed**: the craft gate's contrast row and
the render critique consume these verdicts at the claim they are making — an
existing capability, no new router, no new entry point. And a quality receipt
keeps two kinds of row apart: **visual judgment** (how the render reads) and
**WCAG conformance** (a computed, scoped check naming its criterion) — and a
render fixed on the critique is judged on the SAME before/after matrix inside a
bounded budget ([`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md)), where an
unresolved observation stays unresolved rather than being renamed shipped. A glance
cannot produce a conformance row — a receipt where it did is refused, because
"looked accessible" is a screenshot claim wearing a criterion's name.

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
open. A widened pack's kit and `## Components` section must agree. Where `npx`
is unreachable — no node, no registry — nothing is blocked: the chosen pack and
its token layer in `styles/tokens/<pack>.css` still carry the rules by reading,
but the component states only a kit materializes are then **unverified** — say
so, rather than presenting a read-off state as a kit-checked one. To author a
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
differentiator left. Context: designers rank what the WORD means to them
(Figma, *State of the Designer 2026*, n=906, an association survey —
https://www.figma.com/blog/state-of-the-designer-2026/): visual polish 58% ·
thoughtful problem solving 47% · clear intuitive UX 36% · emotion and delight
35% · consistency 15%. **Those percentages are how often a definition was
picked — 58% proves an association in a survey, never a causal effect or a
work order.** The gate order below is DERIVED FROM DEPENDENCIES (each gate is
meaningless until the one before it holds) and is this pack's authored
decision, not a research conclusion:

1. **The task** — the core job the brief names actually works. A brief with a
   broken primary task fixes THAT first, with perfect tokens or without them.
2. **States** — flows and states decided; if they aren't, stop and decide them
   first (structure is `super-ux`'s half).
3. **Availability** — the interface can be used at all: keyboard, contrast,
   text scaling — the lane this family delegates and never skips.
4. **System** — the visual decision lives in one place (the token layer, the
   `SCENES` registry) and everything else reads it.
5. **Polish** — the pack applied without exception: tokens, not literals; no
   ad-hoc hex, radius or font size anywhere in the diff.
6. **Emotion** — earned motion only (principle 4), never at the cost of 1–5.
7. **Consistency** — one ease, one duration set, one accent, one atom per job
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
- **Mobile surfaces** ([`MOBILE_SURFACES.md`](./MOBILE_SURFACES.md)) — separate
  the platform target (iOS/Android/RN/web, each with its own component adapter)
  from the prototype renderer, and treat a browser HTML mockup as a
  demonstration with a native-equivalent column, never as native proof — when the
  brief is a native app screen or a mobile-web view — not a desktop page whose
  only mobile concern is collapse. Five mobile rules the packs each state alone,
  a sixth **no pack answers** (the type ramp follows viewport width, not the
  user's text size), and the half no pack decides on a phone: platform
  convention.

## Setting a visual language — invariants locked, axes open

When the visual language is being SET or revised under a preserved brand,
run the split in [`VISUAL_EXPLORATION.md`](./VISUAL_EXPLORATION.md) first:
locked invariants (brand colors, logo, accessibility) versus open axes
(composition, type hierarchy, control anatomy, motion purpose), two to
three direction renders for an under-determined brief, exactly one for an
explicit decision — and exact-Figma reproduction generates none. An
existing token file closes nothing by itself.

## Choosing between packs — mount them, don't imagine them

**The mounting rides the semantic token contract.** Token names are not
uniform across the packs, so the comparison never swaps raw CSS: each pack's
token file ends with an `@adapter` block mapping ten semantic roles
(`--sem-surface`, `--sem-surface-raised`, `--sem-text`, `--sem-text-muted`,
`--sem-line`, `--sem-primary`, `--sem-on-primary`, `--sem-positive`,
`--sem-caution`, `--sem-negative`) onto its own tokens — or declaring a role
`@absent` where the pack has no such concept. A role neither mapped nor
declared blocks the comparison BEFORE any render, because an undefined custom
property does not error, it silently falls back — and a comparison built on
silent fallbacks compares the fallbacks. No CSS-swap promise follows:
components keep consuming the pack's own tokens.

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

**What a comparison records — one component, one content, one viewport at a
time, through the adapters.** A difference is attributable to the pack only
when everything else is pinned: the receipt per candidate names the pack, its
adapter status, the compared component's geometry (positions and sizes as
rendered) and its states (hover, focus, disabled). A content or viewport
mismatch between two records INVALIDATES the pair — it never counts as a pack
difference. A pack switch is *expected* to change rendered semantics — that is
what is being chosen — so identical geometry and states across a compared pair is a
signal the adapter never reached the component, not a finding of equivalence.
And a candidate without a complete adapter makes the whole comparison **not
ready**: the pack is named and either adapted or struck from the candidate
list explicitly — "compared what had adapters" silently is a comparison of a
different question.

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

**Why it composes rather than competes.** `shadcn/ui` is not a theme, but it is
NOT unstyled either — its docs ship "Beautiful Defaults" (styled, opinionated
components you copy INTO your repo and edit), built on HEADLESS primitives
(Radix/Base), themed through CSS custom properties (https://ui.shadcn.com/docs,
checked 2026-09-09). So it arrives with a look and *consumes* a token layer to
change it. That is the seam a pack is: the pack decides the tokens, the kit
decides what a `DropdownMenu` is — and because the components are yours to edit,
a custom component edit is a normal adaptation, NOT automatically a redesign.

**The two vocabularies are different, and this is the trap.** The packs resolve
`--bg` and `--ink` everywhere and little else by that name; `shadcn/ui` expects
`--background`, `--foreground`, `--primary`, `--muted` and the rest of its own
contract. **Map them explicitly in the pack's token file** — an undefined custom
property does not error, it silently falls back, which is the same failure the
chart rule above exists for. And color is only ONE axis of the adapter contract:
semantic **color + geometry + density + typography + elevation + state/anatomy**.
A kit mounted with only the color vars remapped keeps shadcn's default radius,
padding, shadows and type — so after the token remap **compare the RENDERED
component matrix (Card/Button/Dialog: computed sizes, padding, radius, shadow,
fonts, states) against the chosen direction**, not just the color variables, and
list the defaults you deliberately kept. A kit mounted without any of that
renders in its starter look and looks like nobody chose anything.

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
