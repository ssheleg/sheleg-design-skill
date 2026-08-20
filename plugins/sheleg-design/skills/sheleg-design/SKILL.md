---
name: sheleg-design
description: Use when deciding how something LOOKS or MOVES. Cinematic scroll-driven landing pages and heroes — particle/WebGL backgrounds, scroll-linked animation, parallax — or when one feels busy or its motion drifts. Product UI through its style packs — dashboards, admin panels, internal tools, mobile screens, chat and agent interfaces. Design tokens, light/dark themes, palettes and colours, typography and fonts. Triggers - "design a landing" / "дизайн лендинга", "build a landing page" / "сделай лендинг", "scroll animation" / "скролл-анимация", "dashboard style" / "стиль дашборда", "design tokens" / "дизайн-токены", "light/dark theme" / "светлая/тёмная тема", "figma variables" / "переменные фигмы, фигма в код", "mobile screen" / "мобильный экран", "palette" / "палитра", "colors" / "цвета", "typography" / "типографика", "font" / "шрифт", "how it looks" / "выглядит", "make it prettier" / "красиво, красивее", "visual reference" / "визуальные референсы", "investor deck" / "презентация".
license: MIT
metadata:
  version: 1.45.0
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

The motion methodology is style-agnostic; the visual identity comes from a style
pack in [`styles/`](./styles/). Each pack file opens with its own full description —
this table is for choosing, not for reading instead of the pack:

| Pack | Look | Choose for |
|---|---|---|
| [`instrument-console`](./styles/instrument-console.md) | near-black aerospace console | technical / systems / infra · **core contract** |
| [`editorial-luxury`](./styles/editorial-luxury.md) | cream and espresso ink | editorial / research / premium B2B · **core contract** |
| [`workbench`](./styles/workbench.md) | quiet light/dark product UI | dashboards / admin / internal & dev tools (standalone) · **core contract** |
| [`briefing-room`](./styles/briefing-room.md) | dark 16:9 deck | investor & board decks, briefings, talks as a page (standalone) · **core contract** |
| [`atrium`](./styles/atrium.md) | cream daylight | consumer health, longevity, wellness, high-trust DTC |
| [`orchard`](./styles/orchard.md) | warm oat slabs | friendly consumer biotech, DTC wellness, kits & supplements · **core contract** |
| [`field-notes`](./styles/field-notes.md) | green-cast paper ruled by hairlines | open-source & developer tools sold on auditability (standalone) |
| [`showroom`](./styles/showroom.md) | white gallery | product-led companies whose best argument is the app on screen |
| [`blueprint`](./styles/blueprint.md) | white stock | infrastructure sold on precision — vector search, storage, query engines |
| [`prism`](./styles/prism.md) | iridescent wash with a hard edge | an OSS infrastructure project's front door, where step one is a command |
| [`maquette`](./styles/maquette.md) | near-black table | enterprise data infrastructure sold to an architecture buyer |
| [`cyclorama`](./styles/cyclorama.md) | pastel field on a 32s loop | enterprise AI transformation and applied-AI consultancies |
| [`scoreboard`](./styles/scoreboard.md) | warm paper | products whose argument is an accumulating number — growth, ads, SEO |
| [`datasheet`](./styles/datasheet.md) | off-white spec sheet | B2B SaaS whose product is a verdict about the visitor, request or device — fraud, bot and device intelligence, identity, API products |
| [`manpage`](./styles/manpage.md) | cream paper | developer products whose buyer reads code — APIs, SDKs, CLIs, MCP servers, developer infrastructure |
| [`pigeonhole`](./styles/pigeonhole.md) | white field | products that file the reader's incoming mess into named categories — email triage, ticket routing, digests, organisers, CRM inboxes |
| [`roster`](./styles/roster.md) | white field in a faint square grid | products whose argument is **who already carries them** — AI-search visibility, SEO and content platforms, agencies, marketplaces |
| [`ora`](./styles/ora.md) | warm coal field | products whose output is **a machine's verdict about the reader** — agent-readiness and crawlability scores, SEO/AEO audits, agent-run traces, MCP and protocol surfaces · **dark by default** (standalone) |
| [`tenor`](./styles/tenor.md) | warm paper | products arguing a **management thesis** — AI-workforce and agent-operations platforms, autonomous back-office, revenue and sales operations, sold to the director who will have to manage it (standalone) |
| [`ledger`](./styles/ledger.md) | warm cream paper ruled by a hairline at 12% ink — no shadow on any card — radius 15 nested concentrically | the console of a product that answers questions **about data** — AI analysts, BI surfaces, query workspaces, agents that read a warehouse and write back a figure (standalone) |
| [`paperclip`](./styles/paperclip.md) | neutral coal with **no functional colour at all** — every control monochrome | products that ask a person to **run something that runs itself** — agent teams and orchestrators, autonomous back-office, schedulers, job runners, budget-governed compute (standalone) |
| [`awning`](./styles/awning.md) | white forecourt where **the accent is black** and no hue reaches the chrome at all; a pill whose radius is a declared component token | commerce and platform front doors — the surface that sells a system other businesses will run their storefront, payroll, billing or logistics on (standalone) · **core contract** |
| [`router`](./styles/router.md) | near-white field with a trace of blue, white cards standing on it, **hairline seams instead of shadows anywhere** — body at 14px and weight 450 | **product consoles and the pages that have to look like them** — dashboards, admin and developer platforms, billing and usage surfaces, and a landing page whose argument is an inventory rather than a promise (standalone) |
| [`daylight`](./styles/daylight.md) | cool near-white portal field with generous radii and **one very large soft shadow spent on a single object per screen** | **client-facing portals and the pages that sell them** — onboarding, workspaces a customer logs into, service dashboards, scheduling and billing (standalone) |
| [`notation`](./styles/notation.md) | near-white page drawn **entirely in hairlines**, radii of 2 and 4px, a slab serif at weight 300 against a monospace, **no bold anywhere** | **developer and technical products sold on restraint** — open source front pages, workspaces for people who dislike being sold to, documentation homes (standalone) |
| [`almanac`](./styles/almanac.md) | **oatmeal paper rather than white**, seams at 2px with **no 1px anywhere**, a display set below a line-height of one, mono tags notched through drawn boxes | **pages that assert a category** — a manifesto, a company saying what this kind of thing is, a product whose argument is editorial rather than functional (standalone) |
| [`vitrine`](./styles/vitrine.md) | white field drawn **entirely in hairlines**, a serif display over a sans body, an ink primary, and one framed record with a 1px inset highlight | **the front door of a product sold on trust** — B2B software under evaluation, security and compliance surfaces, specification and comparison pages (standalone) |
| [`proscenium`](./styles/proscenium.md) | white field carrying two cool acts and **one deep indigo act at the middle**, an electric violet filling a control that stays nearly square at 4px against cards at 16, one family at nine weights, and a framed product panel the fold cuts off | **product-led marketing front doors whose argument is a demonstration** — SaaS home pages, launch and tour pages, any page with six or more acts that needs a repeated beat (standalone) |
| [`bulletin`](./styles/bulletin.md) | warm cream paper cut by flat pastel bands, every card and control a 1px ink outline standing on a **hard zero-blur ink offset it travels into when pressed**, a display face at 800 inside controls and 700 in the headline, and **no tracking at any size** | **front doors whose argument is breadth** — a tool doing many things across many channels for many clients, sold cheerfully to a small team or an agency: social and content platforms, scheduling and inbox products, all-in-one SMB SaaS (standalone) |

**A materialized kit answers part of what a core pack leaves out.** `npx
sheleg-design-skill --kit <pack>` produces `src/styles.css`, whose component half is
authored CSS for the states a core pack declines to specify — `:hover`,
`:focus-visible`, `:disabled`, selected. It does not ship with this skill, so an agent
reading only this bundle will invent them. **A kit exists for every pack, not only
the core ones** — fetch it whenever you are building components, and treat any
difference between kit and pack as a defect in one of them rather than a choice.
For a widened pack the kit and the pack's `## Components` must agree; for a core
pack the kit is the only answer either of them gives.

**Six of the twenty-nine are on the core contract, and it changes what you get.**
A pack marked **core contract** does not specify `## Components`, `## Hero`,
`## Responsive` or `## Signature element` — so per-component states, the
opening viewport and its line ceiling, the collapse rules, and the single
element the page is remembered by are **yours to decide**, and you say so out
loud when you do. The other twenty-three answer all four. This asymmetry is the one
thing about the library most likely to make you invent a value and believe you
read it: what a core pack *does* state is measured to two decimals, and that
precision is not evidence about the half it leaves silent. Each pack declares
its own level on a `Contract:` line above its Register.

Read the chosen pack in full before styling anything — it supplies the
palette, type, texture, motion-token values, signature motifs, and bans.
Each pack ships a ready-made token layer in `styles/tokens/<pack>.css` —
copy that file verbatim instead of transcribing tables. For a new style,
copy [`styles/STYLE_PACK_TEMPLATE.md`](./styles/STYLE_PACK_TEMPLATE.md) and
keep every heading — Register / Palette / Type / Texture & surface /
Components / Hero / Responsive / Motion tokens / Signature motifs / Signature
element / Motion flavor (cinematic packs only) / Micro-interactions / Bans /
Gotchas — then author its `tokens/<pack>.css` in the same change; never invent
token values ad hoc.

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
- **Charts — hand the pack to `dataviz`** (same file), before drawing a chart in
  any pack. Token names are not uniform across the twenty-nine — only `--bg` and
  `--ink` resolve everywhere — and an undefined custom property does not error,
  it silently falls back. Guessing one is the quietest way to ship a wrong chart.
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
The `shadcn` skill does the adding, searching and composing, and
`migrate-radix-to-base` handles the Radix→Base move; both are installed and
trigger on their own words. Do not restate their component docs here.

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
