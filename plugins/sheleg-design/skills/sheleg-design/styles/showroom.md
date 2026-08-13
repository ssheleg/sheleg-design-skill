# Style pack — Showroom

Origin: <https://attio.com/> (2026), the marketing site of a CRM. Every value
below was read off its live computed styles on 2026-08-09, and every ratio was
computed by importing this repository's own palette gate. A white gallery, ink
that is nearly black, one blue that works equally as a link and as a fill, three
type families where every size carries its own weight and tracking, and a
**seven-layer shadow** that makes one product screenshot read as a physical
specimen.

The identity in one sentence: **the product is the exhibit.** Not a hero
illustration, not a blurred mock behind a gradient — one real application
surface, at real size, lit and framed, with the whole page arranged to make you
look at it.

Contract: widened — all thirteen headings.

## Register

Choose this pack for a **product-led company whose best argument is the product
on screen**: CRMs, project and planning tools, analytics, developer platforms
with a real console — anything where a dense surface with real rows, real column
headers and real status chips persuades faster than a paragraph about it. The
first viewport carries a claim and then the application itself.

It rides the SHELEG cinematic layer, but sparingly: the specimen is the subject
and motion exists to deliver it, not to compete with it.

**Not for:** a product with no screenshot worth showing — where what is sold is a
change of state rather than a surface, use `cyclorama`. An open-source project
whose front door is a command rather than a UI — `prism`. A page that must read
as a technical drawing rather than a gallery — `blueprint`. A product with no UI
to exhibit because the interface *is* the call — [`manpage`](./manpage.md). A product whose
argument is not how the app looks but what it *calls each thing* — a filing scheme shown as
labelled chips — is [`pigeonhole`](./pigeonhole.md). And **not** the
dashboard itself: this is the page that displays such a dashboard.

**The fork against [`pigeonhole`](./pigeonhole.md).** Both are white, both are
product-led, both open with a screenshot. The subject is what separates them: this
pack frames the application **whole** and lets a seven-layer shadow lift it off the
page, where that one has no framing shadow system at all and puts **one row of the
app, labelled**, at the centre. *Look how good this looks* is this pack; *look what
it calls your mail* is that one.

### The fork against [`workbench`](./workbench.md), which is the one people get wrong

Both render dense product UI, both use borders rather than shadows inside that
UI, both carry a single blue accent. They are not interchangeable, and the test
is *which surface you are building*.

`workbench` **is** the tool. It is meant to disappear, it caps state transitions
at 150–200 ms, and it bans scroll-driven motion outright. A page built in it is
an application.

`showroom` is the page **arguing for** the tool. Its product surface is a
specimen under glass — lit, framed, cropped by the viewport — and around it sits
a marketing page with a hero, a proof strip and a CTA. Build the dashboard in
`workbench`; build the page that sells it in `showroom`. A real product usually
needs both, and the specimen in the page should be a screenshot of the
`workbench` build.

### Against `blueprint`

Both are white, both are dense, both serve technical buyers. `blueprint` draws
the mechanism — grid, rules, registration marks, no radius at all. `showroom`
photographs the product — soft radii, a deep stacked shadow, and no drafting
furniture anywhere. Route by whether the page shows *how it is built* or *what it
looks like to use*.

### Against [`datasheet`](./datasheet.md)

Both are light pages whose argument is the product, shown rather than described.
The difference is what gets shown. Here it is a **whole application surface at
real size**, framed and lit like a specimen: real rows, real column headers, real
chrome. In `datasheet` it is a **payload** — a few dozen values the API returned
about the person reading the page, laid out in hairline-ruled cells at radius zero.
A gallery frame with a seven-layer shadow versus a ruled grid with none is the
fastest tell, and the deeper one is whose data is on screen: a customer's, or the
reader's own.

**The fork against [`roster`](./roster.md).** Both are white, both are product-led, and
both are chosen when the product is the point. The first viewport separates them: this pack
puts the application in it at real size under a seven-layer framing shadow, where `roster`
puts **no screenshot above the fold at all** — a claim, a black button, a review badge — and
lets the product arrive 1,400px later inside a step card. And `roster` has no shadow system
to lift anything with: its reference paints an all-transparent ring composite on 101
elements, so it separates by hairline. If the app is the exhibit, it is this pack. If the
exhibit is who already uses the app, it is that one.

## Palette

Ready-made token layer: [`tokens/showroom.css`](./tokens/showroom.css) — copy it
verbatim instead of transcribing this table.

**The reference declares its palette in CIE Lab.** This repository's palette gate
cannot parse `lab()`, so every value below was converted by painting the declared
colour into a 1×1 canvas and reading the sRGB bytes back. That is the browser's
own conversion, not arithmetic of this pack's — the colour is unchanged, only its
notation is.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#FFFFFF` | the gallery | — |
| `--surface` | `#FAFAFB` | card, popover | — |
| `--surface-2` | `#EDEFF3` | the sunken well a specimen sits in | — |
| `--ink` | `#1C1D1F` | body and display | **16.87:1** |
| `--ink-2` | `#232529` | secondary headings | 15.35:1 |
| `--ink-soft` | `#505967` | captions, meta, secondary copy | **7.08:1** |
| `--disabled` | `#A4ADBA` | **disabled and placeholder only** | 2.27:1 — see Gotchas |
| `--line-weak` / `--line` / `--line-strong` | `#EDEFF3` / `#D3D8DF` / `#CAD0D9` | inside a specimen · panel edge · emphasis | rules, not text |
| `--accent` | `#266DF0` | link **and** primary fill | **4.64:1** — and 4.64:1 under white |
| `--accent-wash` | `#E8F0FF` | selected row, hovered cell | — |
| `--good` / `--warning` / `--danger` | `#0FC27B` / `#F5B900` / `#FF5B59` | status chips | see the rule below |

Three rules carry this palette.

- **One blue does every job, and that is a decision rather than a discovery.**
  `#266DF0` measures 4.64:1 against the field, which here *is* white — so "and
  4.64:1 under white" was the same measurement stated twice. WCAG contrast is
  symmetric for every pair by definition; it is never evidence about one blue.
  The reason there is one token is that 4.64:1 clears AA in the hardest role it
  takes (text), so the link, the focus ring and the filled button can share it
  with no "on-dark" variant. Do not add one.
- **[CORRECTION — 1.26.0] The chip's label is `--ink`, not its status colour.** Until
  1.26.0 this row read *"that status's ink"*, and the kit did what it said: the label was
  painted in the status colour, which measures **2.03:1** for `--good` on
  `--accent-wash`, **1.54:1** for `--warning` and **2.65:1** for `--danger` on
  `--surface-2` — the pack's own status colours, unreadable at the 12px the same row
  specifies. `--ink` on those fills is 14.65–14.73:1. The status colour keeps the tint
  and gains a 6px dot, which is the *"never by colour alone"* rule below applied to the
  component that exists to serve it. The three status tokens are declared
  `@role non-text:` in the token layer as a result.
- **Status is never by colour alone.** `--good` and `--danger` separate by 33.7 at
  full colour but only **4.9 under deuteranopia**, which is the classic pair and
  the one nobody catches by looking. Every status renders as a chip containing its
  word — which is what the reference already does in its ICP-fit and ARR columns.
  A bare coloured dot in a table is a bug in this pack.
- **`--disabled` is not a caption colour**, whatever the reference calls it. See
  Gotchas.

## Type

Three families, and the reference ships a fourth this pack does not take.

- **Display — Inter Display at 600.** Tight: `-0.02em` at 64px, `-0.015em` at
  56px. The display face is a separate optical size from the body face, and using
  Inter alone at 64px is the most common way this pack is diluted.
- **Body and UI — Inter, weight 500.** Not 400. The reference sets 500 as its
  body weight and the page reads noticeably firmer for it.
- **Data — JetBrains Mono.** Identifiers, amounts, timestamps, anything in a
  column that must align.
- **Tiempos is vestigial.** It appears on one editorial surface of the reference
  and is **not** part of this pack. A serif in a showroom page is a different
  register wearing this one's clothes.

**The ramp's shape is the thing to copy, more than its numbers:** every step
carries its own weight, line-height *and* tracking as one unit. A size never
travels alone here.

| Token | Size / line-height | Tracking | Weight |
|---|---|---|---|
| `--t-display` | 64 / 0.95 | −0.02em | 600 |
| `--t-h1` … `--t-h4` | 56 / 40 / 32 / 28 | −0.015em, then −0.01em | 600 |
| `--t-xl` / `--t-lg` | 20 / 1.3 · 18 / 1.333 | −0.01em | 500 |
| `--t-base` / `--t-sm` | 16 / 1.375 · 14 / 1.429 | −0.01em | 500 |
| `--t-xs` | 12 / 1.5 | 0 | 500 |

## Texture & surface

- **The seven-layer shadow is the pack.** A 1px inner ring plus six offsets, from
  `0 1px 2px` to `0 32px 64px -8px`, at 2–6% alpha. It ships as **one token**,
  `--shadow-specimen`, on purpose: split it and somebody uses three of the seven,
  and the specimen stops sitting in the page. Do not add an eighth layer and do
  not tint it — the alphas are the entire effect.
- **Inside the specimen there are no shadows at all.** The product surface uses
  `--line-weak` hairlines the way `workbench` does. The stack lifts the *frame*;
  everything within it is flat. Mixing the two is what makes a screenshot look
  like a collage.
- **Radii: `2 / 4 / 6 / 8 / 12 / 16 / 20`**, and they nest — a `--radius-sm` chip
  inside a `--radius-lg` row inside a `--radius-2xl` specimen frame. An inner
  radius is the outer minus the padding between them, never the same value twice.
- Spacing is a 4px ramp; the page column is `--page-max` 80rem and the nav is a
  fixed 68px.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary CTA** | `--ink` fill, `--on-ink` label, `--radius-xl`, `10px 18px`, 16px/500 | fill lightens one step over `--dur-fast` | `translateY(1px)` | `--disabled` label on `--surface-2`, `cursor: not-allowed` |
| **Secondary CTA** | `--surface` fill, `1px --line`, `--ink` label, same metrics | border → `--line-strong` | as above | as above |
| **Accent button** | `--accent` fill, white label | `--accent-hover` | as above | as above |
| **Nav item** | transparent, `--radius-lg`, `0 12px`, 15px/500, `--ink-2` | fill → `--surface-2`, colour → `--ink` over `0.3s` | — | — |
| **Specimen frame** | `--surface` fill, `--radius-3xl`, `--shadow-specimen`, a 3-dot title bar | none — it is an exhibit, not a control | — | — |
| **Data row** | transparent on `--surface`, `1px --line-weak` bottom rule, 36px tall | fill → `--accent-wash` | fill → `--accent-wash`, left edge 2px `--accent` | — |
| **Status chip** | tinted fill of its own status, **`--ink` as the label**, a 6px dot of the status colour before the word, `--radius-sm`, `2px 8px`, 12px mono, **always with its word** | none | — | — |
| **Column header** | `--ink-soft`, 12px/500, an icon at 14px, `1px --line` bottom | fill → `--surface-2` | sorted: `--ink` plus a caret | — |
| **Input** | `--surface`, `1px --line`, `--radius-lg`, `8px 12px`, **16px** Inter | border → `--line-strong` | focus: `--accent` border plus `--ring-focus` | `--disabled` text |
| **Loader** | **pack decision:** a skeleton whose geometry matches the row it replaces — same height, same radius, `--surface-2` fill, no shimmer | — | — | — |
| **Empty state** | **pack decision:** one `--ink` line naming what would be here, one `--ink-soft` line saying how to fill it, one accent button. No illustration | — | — | — |

The input's 16px is not a style choice: anything smaller triggers zoom-on-focus
on iOS.

## Hero

- **Height** `--hero-min-h: 100dvh`. Never `100vh`.
- **Composition, top to bottom:** a pill announcement link, the display headline
  centred, a two-line lede, two buttons, and then **the specimen**, entering the
  viewport from below and cropped by it.
- **The headline is centred and the specimen is centred.** This is the one pack
  in the library that centres its hero; the symmetry is what makes the page read
  as a gallery wall rather than a document.
- **Line ceiling: two.** At `--lh-display` 0.95 a third line closes the block up
  and the specimen loses the room it needs to be the subject.
- **The specimen is cropped, never scaled.** Shrinking a product surface until it
  fits is the single fastest way to break this pack: the chips become unreadable,
  the type inside it stops matching the type around it, and the page starts
  looking like a stock photo of software. Show the top 60% at 100% and let the
  viewport cut it.
- The first viewport does **not** carry a feature grid, a logo wall or a metric
  row. Those start below the fold.

## Responsive

- **Type is fixed px with breakpoint steps**, not fluid. The display drops
  64 → 48 → 36 at the breakpoints rather than sliding; the ramp's tracking is
  tuned per size and a `clamp()` would slide between two tuned values and land on
  neither.
- **Breakpoint** `992px` is the reference's only declared one; the layout also
  branches at `768px` for the nav.
- **The specimen crops harder rather than scaling.** Below `992px` it keeps its
  scale and shows less of itself — the left rail goes first, then the trailing
  columns. It never becomes a full-width image.
- **The centred hero stays centred**, and the two buttons stack only below
  `480px`.
- Full-height sections use `dvh`; bare `100vh` is banned.

- **Container queries.** The **data row** and the **column header** are the container
  cases: the specimen's own table is laid out at whatever width the **specimen frame**
  gives it, which is not the viewport minus gutters — so the frame is the container
  (`container-type: inline-size` on it) and the row and header query it. The specimen frame's seven-layer
  shadow is **SELF** — it is a property of the frame itself — and the centred hero is
  **PAGE**.

## Motion tokens

- **One curve, `cubic-bezier(0.2, 0, 0, 1)`**, for every state change and reveal;
  `cubic-bezier(0.65, 0, 0.35, 1)` for panels and drawers only.
- Durations `--dur-fast .15s` (colour, opacity), `--dur-base .3s` (nav, hover),
  `--dur-panel .5s` (disclosure).
- **The specimen enters once and then holds.** A translate-and-fade on first
  view, and after that it does not move again — no parallax, no tilt, no
  scroll-linked scale. It is an exhibit.
- `prefers-reduced-motion` zeroes every duration; the reference ships the branch
  and this pack requires it.

## Signature motifs

- **The specimen under seven layers.** One product surface, framed, shadowed,
  cropped by the viewport.
- **The tinted status chip with its word inside it** — never a bare dot.
- **Column headers with a 14px icon** ahead of the label, which is what makes a
  table read as a real application rather than a styled `<table>`.
- **The pill announcement link** above the headline: `--surface` fill, full
  radius, `1px --line`, a chevron, 14px.
- **Centred hero, left-aligned everything below it.**
- **Type that never travels without its tracking** — the ramp's coupling, visible
  as an unusually even colour of text down the page.

## Signature element

**The specimen.** Not the shadow — the shadow is how the specimen is presented,
and it recurs on cards and popovers besides. The specimen is the single product
surface in the first viewport, at real size.

It carries the identity because it is the pack's whole argument compressed into
one object: this company's case is that the software is good, so the page shows
the software rather than describing it. Every other decision serves that — the
white field so nothing competes, the quiet type so the chips inside the specimen
are the brightest colour on the page, the centred composition so the eye arrives
at it, the ban on parallax so it holds still long enough to be read.

Spend everything here. A page in this pack with two specimens has none, and a
page with a specimen too small to read has a decoration.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack: keep the scroll clock, use the Reveal set
at `--dur-panel` on the one curve, and give the specimen **one** scroll-linked
move — it rises into place as the hero resolves, and then it is done. There is no
particle field, no mesh gradient and no WebGL in this pack; the only ambient
layer permitted is a very faint lavender wash at the bottom of the hero, which is
what the reference uses to seat the specimen against the white.

Formations, scrubbed instruments and act-based scenes belong to the darker,
narrative packs. Here the page is a room with one object in it.

## Micro-interactions

- **Buttons** transition fill and border over `--dur-fast` and press to
  `translateY(1px)`. Nothing scales.
- **Rows** tint to `--accent-wash` on hover and take a 2px `--accent` left edge
  when selected. The tint is the whole feedback; rows do not lift.
- **Focus-visible** is `--ring-focus`, a 3px accent halo at 35% alpha, following
  the target's own radius — plus the accent border on inputs.
- **The nav** transitions colour and background over `0.3s`, which is slower than
  everything else on the page and deliberately so: nav items are large targets and
  a fast tint on them reads as a flicker.
- Chips, headers and leaders have no hover state at all. They are labels.

## Bans

- **A second specimen.** One per page. Two exhibits is a catalogue, not a
  showroom.
- **Scaling the specimen to fit.** Crop it. A product surface below ~85% scale
  stops being evidence and becomes an illustration of evidence.
- **`--disabled` as a caption, label or meta colour** — 2.27:1. It is for
  disabled controls and placeholder text, which are not content.
- A bare status dot with no word; a status colour used for anything that is not
  a status.
- A shadow inside the specimen; a hairline used to lift something outside it. The
  stack lifts frames, hairlines divide contents, and they do not swap.
- A second accent, an "accent on dark" variant, or a gradient anywhere except the
  hero's seating wash.
- A serif. Tiempos is on the reference and is not in this pack.
- Fluid `clamp()` type; a hardcoded radius; `transition: all`; `100vh`.
- Parallax, tilt, or scroll-linked scale on the specimen.

## Gotchas

- **The reference's caption colour cannot carry a caption.**
  `--color-caption-foreground` `#A4ADBA` measures **2.27:1** on the reference's
  own white field — it fails WCAG at every size. This pack keeps the value,
  because the reference genuinely uses it, and renames it to what it is safe for:
  `--disabled`. Captions take `--ink-soft` `#505967` at 7.08:1. If you port the
  reference verbatim you inherit an unreadable caption class with a name that
  invites you to use it for captions.
- **The palette is declared in `lab()` and most tooling will not round-trip it.**
  Converted here through the browser's own canvas. If you re-convert with a
  different method you will get values a shade off, and the greys are close
  enough together that a shade is visible in a stack of hairlines.
- **The body weight is 500, not 400.** Setting Inter 400 makes the whole page go
  soft, and it is the single most common way this pack is diluted — more visible
  than getting the blue slightly wrong.
- **Inter and Inter Display are different faces.** The reference loads both; at
  64px the display cut is noticeably tighter. Using Inter alone at display sizes
  is legible but flat.
- **The seven-layer shadow is expensive to fake and cheap to copy.** Do not
  approximate it with `0 20px 40px rgba(0,0,0,.1)`. The stack's whole point is
  that no single layer is visible.
- **Values are a snapshot** taken 2026-08-09 from a live production site. Treat
  them as extracted, not eternal.
