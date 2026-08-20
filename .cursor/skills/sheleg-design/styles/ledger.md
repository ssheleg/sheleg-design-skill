# Style pack — Ledger

Origin: <https://www.basedash.com> — read on 2026-08-15 from the live computed
styles and from the two stylesheets the page ships (`/_astro/index.D2eYbzAo.css`,
`/_astro/Section.D_BwVTGj.css`). Every value below is that measurement unless
the line says it is derived.

A warm cream ledger page for a product whose answers must be checkable: the
field is `#fcf9f5` paper, the ink is `#14100c`, elevation is a **hairline at 12%
ink** and never a shadow, and the one accent — a terracotta `#c2410c` — spends
almost its entire budget on a 10px monospace uppercase kicker. The primary
button is **ink**, not accent. Data sets in a monospace on 32px rows; every card
that states a number carries a seal saying how the number is known.

Contract: widened — all thirteen headings are answered here. Where the reference
does not paint something a product console needs (a focus ring, a disabled
control, a warning state, an empty state), the value is this pack's decision and
says so **at the point it is declared**, in the token layer as well as here.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose this pack for **the console of a product that answers questions about
data** — an AI analyst, a BI surface, a query workspace, an agent that reads a
warehouse and writes back a number. It is a product-UI pack and it is used
**standalone**: the SHELEG cinematic layer is out of scope, and `MOTION_INTENSITY`
above **3** on it has nothing legal to buy. Light is the default register; dark
is a first-class twin from the same tokens.

The register's real subject is **provenance**. A dashboard that a model filled in
is only worth as much as the reader's ability to check it, so this pack gives the
seal, the kicker and the mono data plane the space that another pack would spend
on ornament, and pairs with [`AI_PRODUCT_PATTERNS.md`](../AI_PRODUCT_PATTERNS.md)
— whose three provenance states map onto three tokens this pack already ships
(`--info` extracted · `--accent` inferred · `--warn` ambiguous), so implementing
the pattern adds no hue.

**Not for:** the marketing page in front of the console — the reference's own
landing page is a different animal, and a page arguing *for* a tool belongs to
[`showroom`](./showroom.md). Not for a page whose argument is one accumulating
number ([`scoreboard`](./scoreboard.md)), and not for a surface with no data on
it at all: with nothing to verify, this pack's whole apparatus is decoration.

**The fork against [`workbench`](./workbench.md)** is the one to get right,
because both are standalone product-UI packs, both build elevation out of
hairlines, both set data in a monospace. The test is **who the reader is arguing
with**. `workbench` is the tool you operate: cool neutral greys, a blue accent
that fills the primary button, and a surface that means to disappear. This pack
is the tool you *audit*: warm paper, an accent that is forbidden from filling a
control, and a per-card seal stating how each number was obtained. Pick
`workbench` when the user's question is "what is the state of the system"; pick
this one when it is "is this number right, and where did it come from".

## Palette

Ready-made token layer: [`tokens/ledger.css`](./tokens/ledger.css) (light
`:root` + `[data-theme="dark"]` twin) — copy it verbatim instead of transcribing
this table.

The neutral ramp is **alpha over the ink**, as the reference builds it, so one
ramp reads correctly on the field, on a card and on a table row. Alpha steps
differ per theme (light 72/55/22/12/5, dark 70/50/20/10/4) — the dark theme is
not the light one inverted.

| Token | Light | Dark | Role | On `--bg` |
|---|---|---|---|---|
| `--bg` | `#fcf9f5` | `#080706` | the page | — |
| `--panel` | `#fffdfa` | `#0c0b0a` | the raised card | — |
| `--panel-2` | `#ffffff` | `#171513` | the data plane: tables, menus, popovers | — |
| `--ink` | `#14100c` | `#fffcf8` | primary text | 18.04 light · 19.68 dark |
| `--ink-2` | ink 72% | ink 70% | secondary prose | 7.47 light · 9.58 dark |
| `--muted` | ink 55% | ink 50% | column heads, axis ticks, row numbers | 4.13 light · 5.22 dark |
| `--faint` | ink 22% | ink 20% | disabled, hairline ticks | — |
| `--border` | ink 12% | ink 10% | **the elevation device** | — |
| `--border-strong` | ink 22% | ink 20% | the hover edge | — |
| `--accent` | `#c2410c` | `#f49556` | THE accent — labels and marks, never a fill | 4.93 light · 8.89 dark |
| `--accent-mark` | `#e8792f` | `#e8792f` | the accent as a fill or a stroke | 2.78 light · 6.91 dark |
| `--on-ink` | `#fcf9f5` | `#14100c` | text **on** `--ink` — it flips with the theme | — |
| `--ok` | `#2fa86b` | `#2fa86b` | positive delta, healthy | 2.89 light · 6.65 dark |
| `--warn` | `oklch(76.9% .188 70.08)` | `oklch(87.9% .169 91.605)` | needs a human, ambiguous | 2.06 light · 13.95 dark |
| `--danger` | `#f84747` | `#f84747` | negative delta, failed | 3.34 light · 5.73 dark |
| `--info` | `#0891b2` | `#22d3ee` | verified, running | 3.51 light · 11.14 dark |

**Status is never by colour alone in this pack**, and that is a floor rather than
a preference: four of the five semantic colours sit under 4.5:1 on the light
field and two of them under 3:1, so in light mode the colour is reinforcement and
the *word or the sign* is the message — `+23.9%` carries its plus, `Verified`
carries its word and its check, a failed run says "failed". The values are the
reference's own and are not re-stepped here, because a colour invented at this
keyboard would be exactly what a measured pack exists to prevent. In dark mode
all five clear AA and the rule still holds, so one component works in both.

Two pairs run tight and both are covered by that rule: `--ok`/`--danger` separate
by 6.4 under deuteranopia, and `--ok`/`--info` by 6.0 under tritanopia. Neither
falls below the hard floor where a colour carries two meanings.

`--warn` is **derived, not measured in use**: the reference declares amber in its
own theme layer and never paints a warning on the page. The step differs per
theme on purpose — at amber-500 the *dark* accent and the warning are 7.1 apart
at full colour, which is one colour with two jobs.

## Type

Three families, which is the ceiling:

- **Display — `"Alpha Lyrae"`, weight 500, 48px, line-height 1.1, tracking
  normal.** One line per page and no more. The face is licensed and self-hosted
  by the reference; a project without that licence points `--font-display` at
  `--font-ui` and loses nothing structural, because nothing but that one line
  uses it. Substituting a *different* display face is the drift to avoid — a
  wide technical grotesque at 500 or the UI face, not a serif.
- **UI — Inter**, weights 400 / 500 / 600 only. 34px titles at `-0.03em`
  (`−1.02px`, as measured), 18px card titles at 500, 15px running text, 14px
  dense UI and table cells, 12px labels and meta.
- **Data — the system monospace** (`ui-monospace, SFMono-Regular, Menlo, …`) for
  **all** data: ids, metrics, timestamps, row numbers, SQL, chips, logs.
  `font-variant-numeric: tabular-nums` wherever digits align.

The scale ships as tokens — `--t-display` 48 · `--t-title` 34 · `--t-card` 18 ·
`--t-prose` 15 · `--t-body` 14 · `--t-meta` 12 · `--t-kicker` 10 — so "no ad-hoc
font size anywhere in the diff" is a check rather than an aspiration.

Running text ≤65ch; headings `text-wrap: balance`. Weight 700 exists in the
reference's theme and is **not used** on the page; do not reach for it.

## Texture & surface

- **Elevation is a 1px hairline at 12% ink, and there is no shadow on a card.**
  103 of the reference's surfaces are exactly this: transparent fill, 1px
  `--border`, `--r-card`. Depth comes from the fill step (`--bg` → `--panel` →
  `--panel-2`) and from the line, never from a drop shadow. One shadow token
  exists, `--shadow-1`, for true overlays only — dialogs, popovers, menus.
- **Radii are the reference's ×1.25 ramp**: `--r-inset` 7.5 · `--r-control` 10 ·
  `--r-card` 15 · `--r-panel` 20 · `--r-pill` 999. Nothing else.
- **Radius arithmetic is concentric and it is measured, not asserted**: the
  segmented control is a 15px track with 4px of padding holding a 10px thumb —
  outer minus the padding between them, rounded to the ramp. Two identical radii
  nested inside one another is the tell of a stuck-together interface.
- 4px base grid; steps 4 / 8 / 12 / 16 / 20 / 24 / 32. Buttons pad 8×20, cards
  14×20, table cells 0×8, the segmented track 4.
- **Fixed row heights**: data row 32px, control 30px, field and segmented track
  38px. Dense by default, and the density is what makes the cream field read as
  a ledger rather than as a brochure.
- No gradients on a surface, no grain, no glass. The only gradient in the
  reference is inside a chart mark.

## Components

Measured off the reference; every entry states rest, hover, active and disabled.
Hover states are gated on `@media (hover: hover)`, which is how the reference
ships them — a touch device never gets a stuck hover.

- **Button.** Primary is `--ink` fill, `--on-ink` text, 1px border of the same
  ink, `--r-control` (10px), 8×20 padding, 14px/600. Hover darkens the fill
  (`#0c0c0e` in the reference's own light theme) — never a translate, never a
  shadow. Active is `scale(var(--press-scale))` = 0.97. Secondary is the same
  geometry with a translucent panel fill and a `--border` edge; hover moves the
  edge to `--border-strong`. Ghost is bare, hover fills `--inset`. Disabled is
  `--faint` text on `--inset` with `cursor: not-allowed` and no hover — **this
  one is derived**, because the reference has no disabled control on the page.
  **The accent never fills a button**, in any variant; the destructive action is
  a `--danger`-bordered ghost that fills `--danger-weak` on hover and demands a
  typed confirmation for anything irreversible.
- **Card.** `--panel` fill or transparent, 1px `--border`, `--r-card`, 20px
  padding, a title row at `--t-card`/500 with its meta pushed right. Hover on an
  interactive card moves the border to `--border-strong` and nothing else. A card
  that states a number carries the seal (see Signature element) in the title row.
- **Inputs.** 38px tall, `--panel-2` fill, 1px `--border`, `--r-control`, label
  above at `--t-meta` in `--muted`, placeholder in `--faint`. Focus is the ring
  below, not a border swap. Errors sit under the field in `--t-meta`, in `--ink`,
  with a `--danger` dot at the line start — colour and word together. Field
  geometry is measured; the error placement is **derived**, the reference showing
  no form.
- **Navigation.** A single hairline under a 60px bar, no shadow, no colour
  change on scroll. The current item is `--ink` at 500 with a 2px `--accent-mark`
  inset rule at its leading edge; every other item is `--ink-2`. Below 48rem the
  bar collapses to a sheet.
- **Table.** `--panel-2` plane, 32px rows, header at `--t-meta` in `--muted` with
  a hairline under it, hairline row dividers, numeric columns right-aligned in
  the data face with tabular numerals, and a mono row number in `--muted` in the
  first column. Row hover is `--row-hover` (`#f7f7f7` light, `#212121` dark) —
  which is why a dense table always sits on `--panel-2` and never directly on the
  field.
- **Segmented control.** `--inset` track, `--r-card`, 4px padding, 38px tall; the
  selected thumb is `--panel-2` at `--r-control`, 30px tall, 12px label. The
  unselected label is `--ink-2`. This is the pack's range/scope switch and it
  replaces a select wherever the options are three or fewer.
- **Chip.** 10px mono, uppercase, `--track-kicker`, transparent fill, 1px border
  of its own colour at 30% alpha, `--r-control`. This is the same atom as the
  kicker, boxed; the provenance tag in `AI_PRODUCT_PATTERNS.md` §4 is this chip.
- **Loaders.** A skeleton whose geometry matches the real layout — a 32px row
  block for a table, a title bar plus a number block for a stat — in `--inset`,
  no shimmer sweep. Where tokens can stream, there is no loader at all: the text
  is the progress, and the stop control is present from the first frame.
- **Empty states.** One `--ink-2` sentence stating what this surface can answer,
  and two or three real example questions as `--accent` kickers that run when
  clicked. No illustration, no "Ask me anything". **Derived** — the reference has
  no empty state on the page — and taken straight from
  [`AI_PRODUCT_PATTERNS.md`](../AI_PRODUCT_PATTERNS.md) §6.

## Hero

A console's hero is its **first viewport after sign-in**, and this pack pins what
must be in it:

- One kicker (10px mono, uppercase, `--accent`), then the page title at
  `--t-title` in weight 400 with `--track-title`. **Ceiling: two lines**, held by
  a 42rem (`--container-2xl`) measure. A title that wraps to three lines is a
  broken hero, not a long one. The 48px display face appears **only** on a
  signed-out or marketing surface; inside the console the title is 34px.
- The **answer before its evidence**: the number, its delta and its seal come
  first; the chart that explains it comes second; the table that sources it
  comes third. A chart above the number it illustrates inverts the pack.
- At most three stat tiles across, on `--panel` with a hairline. A fourth means
  the screen has not decided what it is for.
- What it must not contain: a carousel, a hero image, an illustration, a second
  accent, or any control filled in `--accent`.

## Responsive

The reference's breakpoints are the Tailwind ramp and it uses no `clamp()` at
all — **the type ramp is stepped, not fluid**, and this pack keeps it that way:
34px titles do not grow on a wide screen, they get more white space.

- **PAGE** — 40rem / 48rem / 64rem / 80rem / 96rem, viewport `@media`, and they
  stay there. 64rem is the one that matters in a console: the chat or inspector
  rail leaves the grid and becomes a sheet over the content. Below 48rem the nav
  collapses and stat tiles stack.
- **CONTAINER** — the card grid, the stat tile and the chart card size against
  their container, not the viewport: `container-type: inline-size` on the card
  root, `@container` on the tile row and on the chart's legend, which drops from
  a row to a stack. This is the half a component library owns, and it is the
  reason a card looks right both in a full-width page and in a 380px rail.
- **SELF** — the table's own horizontal scroll and the sticky header offset are
  properties of the element that establishes the container, so they keep a
  viewport query and no container answer exists for them.
- **Collapse** — nothing here overlaps or rotates, so collapse is only reflow:
  the segmented control becomes a select below 40rem, right-aligned numeric
  columns stay right-aligned, and the mono row number is the first column to be
  dropped.
- **Viewport** — `min-h-[100dvh]`, never `100vh`. The reference uses `100dvh`
  twice and `100vh` nowhere.

## Motion tokens

- **One curve carries the interface**: `--ease` = `cubic-bezier(0.22, 1, 0.36, 1)`,
  which is the reference's own default timing function. `--ease-out`
  (`cubic-bezier(0.17, 1, 0.32, 1)`) for things entering, `--ease-in-out`
  (`cubic-bezier(0.66, 0, 0.34, 1)`) for movement on screen. The reference also
  declares an `ease-in`; it is **deliberately not carried over**, because
  [`MOTION_DOCTRINE.md`](../MOTION_DOCTRINE.md) §2 bans it in UI and this pack
  has no exception to claim.
- **Durations**: `--dur-xs` 75ms · `--dur-sm` 0.1s · `--dur` 0.15s (the default)
  · `--dur-lg` 0.2s · `--dur-xl` 0.3s. Nothing in this pack runs longer than
  0.3s, which is the doctrine's UI ceiling and the reference's own longest step.
- **Press** is `scale(0.97)` on controls and nothing else moves.
- **Exactly three loops are legal**, all of them state and all of them stopping
  when the state does: the typing cursor while tokens stream, the thinking dots
  while a run is working, and a 1.4s heartbeat on a live indicator. The reference
  ships all three and stops all three under reduced motion.
- `prefers-reduced-motion: reduce` zeroes every duration token and the press
  scale, and stops the three loops. The interface is fully static-safe: nothing
  here gates content on motion.

## Signature motifs

- **The mono kicker.** 10px, uppercase, `+0.1em`, `--accent`. It labels a
  section, a card, an example query, a capability. On the reference it is where
  the accent lives: of eleven accent-coloured elements on the page, five are this
  kicker and none is a button.
- **The hairline card at radius 15.** No shadow, no fill step needed — a
  rectangle drawn at 12% ink. Repeated at every scale from a 380px rail to a
  full-width table, it is what makes the cream field read as ruled paper.
- **Ink primary, accent never a control.** The one filled button on a screen is
  `--ink`; the accent marks and labels. A page that fills a button orange is not
  this pack.
- **Concentric nesting.** Every nested radius is the outer radius minus the
  padding between them.
- **The mono data plane.** 32px rows, mono row numbers at `--muted`, right-aligned
  tabular numerals, hairline dividers, header in 12px `--muted`.

## Signature element

**The seal in the card's title row** — a 16px-high chip that states how this
card's number is known, and the single thing a page in this pack is remembered
by.

It is a check glyph plus one word in `--info`, sitting hard right in the title
row of every card that states a figure: `Verified` when the number came from a
governed definition the reader can open, `Inferred` in `--accent` when the system
derived it by a step it can name, `Unverified` in `--warn` when it cannot. It is
the pack's whole argument compressed into 90 pixels: this is a surface a model
filled in, and here is the part of it you can trust.

Three rules decide whether it is honest rather than decorative, and they are the
provenance rules from [`AI_PRODUCT_PATTERNS.md`](../AI_PRODUCT_PATTERNS.md) §4
applied to a card instead of a span:

1. **Every state must be reachable.** If nothing on the surface is ever
   `Unverified`, the seal is a sticker and the reader learns to skip it.
2. **The label must be derivable from something real** — a metric definition, a
   query, a retrieval hit. A seal assigned by a second model call guessing at the
   first is confidence theatre with better typography.
3. **It seals a card, not a screen.** A single badge over a dashboard of twelve
   numbers hides exactly the number the reader needed to check.

Everything around it stays quiet: this is where the pack spends its boldness, and
it is the reason no other element gets a colour fill.

## Micro-interactions

- **Hover** moves background, border and colour only — `--inset` on a ghost
  control, `--row-hover` on a table row, `--border` → `--border-strong` on a
  card. Nothing translates, nothing scales up, nothing casts a shadow it did not
  have. All of it inside `@media (hover: hover)`.
- **Active** is the 0.97 press, on controls only.
- **Focus-visible** is a 2px `--accent` outline at 2px offset on every
  interactive element — **derived**, and the one place this pack overrules its
  reference: the reference answers focus by swapping a border colour, which
  leaves a borderless control with no focus state at all.
- **Selected** is `--accent-weak` fill plus a 2px `--accent-mark` inset rule on
  the leading edge — the rule, not the fill, is what makes it legible for a
  reader who cannot see the wash.
- **Keyboard first.** Nothing on the 100+/day path animates: the command palette
  opens instantly, tab switches are instant, the segmented control responds on
  the keypress. Frequency decides before taste does.

## Bans

- **The accent never fills a control.** No orange button, no orange tab, no
  orange toggle. The accent labels, marks, strokes a chart and rules a selected
  edge.
- **No shadow on a card.** Elevation is the hairline. `--shadow-1` is for
  overlays and there is no second shadow token to reach for.
- **No second accent hue**, and no semantic colour used decoratively. The chart
  ramp is the one place five hues coexist, and a series there is labelled at its
  own mark — never by a legend the reader must hold in their head — because
  `--chart-2` and `--chart-5` are one hue apart under protanopia.
- **Status is never by colour alone.** Every status ships a word, a sign or a
  glyph beside the colour.
- **No spinner where tokens can stream**, no fake typing delay, no invented
  confidence number, and no single red state covering refusal, rate limit and
  crash — the four bans this pack inherits wholesale from
  [`AI_PRODUCT_PATTERNS.md`](../AI_PRODUCT_PATTERNS.md) §9.
- **No serif, no fourth family, no weight 700.**
- **No cinematic motion**: no scroll clock, no parallax, no scrubbing, no
  `animation-timeline`. Three loops, all of them state.
- No illustrations, no mascots, no emoji in the console, no icon that repeats the
  word beside it.

## Gotchas

- **The reference paints `--ok` and `--danger` as text and both miss AA on the
  light field** — `+23.9%` renders at 2.89:1 and `-6%` at 3.34:1. The values are
  kept because they are what was measured; the resolution is the rule, not a new
  hex: the sign carries the delta, and where a status must be a *word* the word
  is `--ink` with the colour on the dot, the fill or the mark beside it. In dark
  mode both clear AA, so this is a light-mode-only trap and it will not show up
  in a dark-first review.
- **`--muted` is 4.13:1 on the field, under AA by 0.37.** It is measured, it is
  the reference's own `--color-neutral-3`, and it is correct for column heads,
  axis ticks and row numbers where position repeats the word. A label a decision
  rests on takes `--ink-2` (7.47:1). Do not "fix" this by darkening the token —
  that inverts every surface it also paints.
- **`--panel-2` is pure white in light mode and the row hover is `#f7f7f7`, so a
  table sitting directly on `--bg` shows almost no hover at all** (`#fcf9f5` and
  `#f7f7f7` are neighbours). Dense tables go on `--panel-2`, always. This is the
  same class of trap `workbench` documents for its own two identical greys, in a
  different place.
- **The display face is licensed.** `Alpha Lyrae` is served from the reference's
  own origin under its own licence. Shipping it without one is a legal problem,
  not a design one; point `--font-display` at `--font-ui` and the pack survives
  intact, because exactly one line per page uses it.
- **Relative colour is Baseline 2024.** The neutral ramp ships the literal first
  and `rgb(from var(--ink) …)` second on purpose: an older browser drops the
  second declaration and keeps a correct colour. If you re-order those two lines,
  that browser gets an undefined custom property and inherits whatever the parent
  had — which fails silently and looks like a theming bug.
- **The dark theme is not the light one inverted.** Its alpha steps differ (70 /
  50 / 20 / 10 / 4 against 72 / 55 / 22 / 12 / 5), its accent is a different hex,
  its warning is a different amber, and its `--on-ink` flips. Ship both from the
  token layer on day one; retrofitting a theme leaves inverted hardcodes that no
  linter will find.
- **The chart ramp is named for shadcn/ui.** `--chart-1` … `--chart-5` are the
  variable names Recharts reads through that library's `ChartConfig`, so a series
  can point at `var(--chart-3)` with no adapter. Hand the pack to `dataviz`
  before drawing anything: token names are not uniform across this library, and
  an undefined custom property does not error — it silently falls back.
