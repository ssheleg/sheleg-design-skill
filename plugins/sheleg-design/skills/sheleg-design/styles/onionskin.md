# Style pack — Onionskin

Origin: <https://supermemory.ai> (2026), the front page of a memory and context engine
for AI applications. The site is Astro: two stylesheets totalling 154,143 bytes and
declaring 151 custom properties. Every value below was read on 2026-08-25 off
**computed styles on the live page** through CDP at 1440×900 — 1,469 visible of 1,653
elements on a 14,437px page — and at a device-emulated 390×844 (1,451 visible,
19,963px). Ratios were computed by importing this repository's own palette gate. Its
`robots.txt` carries `Content-Signal: ai-train=no, search=yes, ai-input=yes`; what is
recorded here are measurements of a public surface rather than its content, and the
published catalogue names no source at all.

A white technical sheet at **96.5% zero radius** — the squarest page in the library —
ruled by hairlines that are a navy at 10% and 5.5%, some of them dashed, over a dot
grid of accent at 0.8px. Three faces: a grotesque for display, a sans for every
sentence, a mono for every number and key. The working size is **11px**.

The identity in one sentence: **there are two bases, and everything quiet is one of
them at an alpha** — text dims through the ink, structure dims through a navy that is
never text, and nothing dims by reaching for a lighter grey.

Contract: widened — all thirteen headings.

Themes: light only — the second block (`[data-surface="dark"]`) is a SURFACE variant, not a theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Contents

- Register
- Palette
- Type
- Texture & surface
- Components
- Hero
- Responsive
- Motion tokens
- Signature motifs
- Signature element
- Micro-interactions
- Bans
- Gotchas

## Register

Choose Onionskin for **developer and AI infrastructure whose front page is a working
document** — memory and context engines, retrieval and embedding services, agent
runtimes, evaluation and observability surfaces, anything sold to someone who will read
the page the way they read a spec. It suits a page that has to carry API shapes,
numbers, keys and diagrams at reading density without the reader feeling sold to.

**Standalone**, and it pins its own ceiling: **`MOTION_INTENSITY` above 2 has nothing
legal to buy here.** 1,290 of the 1,469 visible elements compute
`transition-duration: 0s`; what moves does so between 0.12s and 0.3s;
`animation-timeline` appears zero times in 154,143 bytes. Nine elements are sticky and
that is the whole spatial budget.

**Not for:** a consumer page, anything sold on warmth, or a surface a person will only
glance at. An 11px working size is a promise that the reader is going to sit down with
it, and making that promise to someone who will not is how a page reads as unreadable
rather than as dense.

### The fork against [`blueprint`](./blueprint.md), which is the closest call in the library

Both are near-white technical sheets. Both spend **one strong blue that writes and
fills**. Both are zero-radius. Both are sold to an infrastructure buyer — `blueprint`
names "vector databases, search and retrieval, storage and query engines", which is a
description of this reference too. A router reading the register alone cannot separate
them, and a thumbnail will not either.

The separation is **how the quiet layer is built**, and it is measurable:

| | `blueprint` | Onionskin |
|---|---|---|
| Secondary ink | solid greys — `#4b5563`, `#9ca3af` | **the ink itself at an alpha**, 56 nodes at 0.6 |
| Rules | a solid grey, `#e2e8f0` | **a navy at 10%**, 64 nodes, and it is never text |
| Body size | 16px | **11px is the most frequent size on the page** (65 nodes) |
| Families | two | **three** — grotesque, sans, mono |
| Dashed rules | — | 10 elements |
| Grid | a 32px ruled field with tick marks | a 24px **dot** field |

So: `blueprint` when the page argues *precision* and wants the vocabulary of technical
drafting — ruled columns, registration marks, ticks. Onionskin when the page argues
*density* and the reader is expected to work through it. The give-away is the greys:
if the secondary text is its own colour, it is `blueprint`; if it is the ink turned
down, it is this one.

## Palette

Copy [`tokens/onionskin.css`](./tokens/onionskin.css) verbatim. Every value there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio.

| Role | Token | Value | On `--bg` |
|---|---|---|---|
| Sheet | `--bg` | `#ffffff` | MEASURED — 54 fills |
| Panel | `--bg-2` | `#fafafa` | MEASURED — 16 |
| Called-out | `--tint` | `#edf3ff` | MEASURED — 8, and it is the accent's wash |
| Ink | `--ink` | `#0b1015` | 19.11:1 — 123 text nodes |
| Secondary | `--ink-soft` | the ink at 60% | 4.98:1 — 56 nodes |
| Quiet | `--ink-quiet` | `#696f75` | 5.08:1 — DERIVED, see Gotchas |
| Rule | `--rule` | the navy at 10% | 1.21:1 — a rule, never a mark |
| Accent | `--accent` | `#0562ef` | 5.25:1 — and 5.25:1 white-on-it |

**Two bases, and that is the whole system.** 199 of the 631 colour-carrying values on
the page carry an alpha, drawn from exactly two: 97 from `#0f2e5c`, a navy used for
every rule and panel edge and never for a word, and 83 from `#0b1015`, the ink, used
only for words. There is no grey ramp in this pack because the reference has none.

**The accent needed no correction, which is rare here.** `#0562ef` measures 5.25:1 on
white *and* 5.25:1 under white — the same number in both directions — so one token
carries the fill and the word with no derived twin. Most packs in this library need
two.

**Status is never carried by colour alone.** Every state takes a glyph or a word beside
its colour, on both fields. The four roles are SELECTED — the reference paints no error
state — and they were searched rather than chosen: all ten pairs across the four states
and the accent clear 15 OKLab units at full colour and 8 under protanopia, deuteranopia
and tritanopia, on the tint as well as on white. The dark band carries its own four,
because the light set measures 1.4–2.6:1 there.

## Type

Three families, and each has exactly one job. Reaching across them is the fastest way
to lose the pack.

| Role | Family | Size | Weight | Tracking |
|---|---|---|---|---|
| Display | Space Grotesk | 56px → 34px | 500 | −0.05em |
| Section | Space Grotesk | 40px | 500 | −0.05em |
| Lede | DM Sans | 22px | 400 | −0.01em |
| Body | DM Sans | **15px** | 400 | −0.01em |
| Small | DM Sans | 13px | 400 | −0.01em |
| Micro caps | DM Sans | **11px** | 500 | **+0.18em**, uppercase |
| Data / key | DM Mono | 11–13px | 400 | 0 |

**The working size is 11px and that is not a caption.** It is the most frequent size on
the page — 65 nodes at 1440, 67 at 390 — and it carries labels, keys, annotations and
the mono data. A page built on this pack at 16px is a different pack.

**Tracking is two-sided and the two sides are far apart.** The uppercase micro-label is
pushed open to +0.18em; the display is pulled in to −0.05em. Measured: 1.98px on 11px
and −1.76px on 35px. Collapsing them to one value loses the page's whole texture.

**No bold.** The heaviest weight at scale is 500 (205 nodes) against 400 (175); 600
appears on seven elements and 700 on four. A headline is loud because it is 56px.

## Texture & surface

One texture and it is a **dot grid**: `radial-gradient(circle, var(--grid-color)
0.8px, transparent 0.8px)` at a 24px step. It is a *field* — it belongs under a
section, never inside a card and never as a border.

**Everything else is a rule.** `--rule` is the navy at 10%, `--rule-faint` at 5.5%, and
`--rule-dashed` is the same hairline drawn dashed on 10 elements, marking a boundary
that is provisional: a drop target, a planned step, an empty slot.

**Elevation is an edge, not a shadow.** `--edge-lit` is an inset side-rule in the
accent at 28% — 8 elements — that lights a panel's left and right edge without lifting
it. `--shadow-hair` is a 1px seam. `--shadow-lift` (32px offset, 64px blur) appears
**once** on the page and should appear once on yours.

## Components

**Panel** — `--surface` on `--bg`, `1px solid --rule`, `--r-none`. It is a rectangle
with a hairline, and it does not lift. `--edge-lit` marks the one panel per section
that is the subject.

**Buttons.** The pack ships two and no more: a primary and a secondary. There is no
tertiary, no icon-only variant and no split button, because the reference has none —
its whole action vocabulary on a 14,437px page is a filled rectangle and a hairlined
one, and a third would have to be invented.

**Primary control** — `--accent` fill, `--on-accent` label at `--t-xs`/500, height
`--tap-min` floor (`--control-h` 36px is the reference's own and is corrected here),
`--r-sm` (4px). Hover darkens the fill one step; focus takes `--focus-ring`. Disabled:
`--bg-2` fill, `--ink-faint` label, `cursor: not-allowed`.

**Secondary control** — `--surface`, `1px solid --rule`, `--ink` label, same height and
radius. Hover moves the border to `--accent-rule`; no fill change.

**Micro label** — 11px/500 uppercase at `--track-micro` in `--ink-quiet`. It opens a
section, names a column, or tags a value. It is the pack's most repeated object.

**Data cell** — `--font-mono` at `--t-micro` or `--t-xs`, `--ink` for the figure and
`--ink-soft` for its unit. Numbers never take the sans.

**Input** — `--surface`, `1px solid --rule`, `--r-sm`, `--t-body`, `--tap-min` floor.
Focus: border to `--accent` plus `--focus-ring`. Invalid: border `--danger` **and** a
message.

**Navigation** — a hairline-bottomed bar on `--surface`, micro labels, sticky. The
reference keeps nine sticky elements; one bar is the sane share.

**Empty states** — a `--rule-dashed` rectangle on `--bg-2`, a micro label in
`--ink-quiet`, one sentence at `--t-body`. The dashed hairline is exactly the motif for
this: a boundary around something that is not there yet.

**Loaders** — a skeleton in `--bg-2` at the shape's own radius, no shimmer. The page's
whole motion budget is a 0.2s colour transition; a shimmer would be the liveliest thing
on it.

Every interactive element takes `--tap-min` (44px) as a height floor. This is a
correction: 88 of the 123 visible interactive elements at 1440 are under 44px, and 73
of 106 at 390.

## Hero

Full width, not full height.

- Field `--bg`, with `--grid` under the section and fading out before the fold.
- A micro label above the headline — 11px uppercase at `--track-micro` — naming what
  the product is before the headline says what it does.
- Headline at `--t-display` in `--font-display`, **two lines**, `--track-display`.
- One paragraph at `--t-body` in `--ink-soft`, held near 60 characters.
- A control pair: primary in `--accent`, secondary hairlined. Both at `--tap-min`.
- Below them, a mono line — version, latency, a count — at `--t-micro`. This is the
  pack's tell: the hero ends in a fact set in the mono, not in a testimonial.

## Responsive

Three widths, measured: 1440, 768 and 390.

- **The working size does not change.** 11px is the most frequent size at 1440 (65
  nodes) and at 390 (67). Scaling it up on a phone is the single change that would
  break this pack, because the density is the argument.
- **Display 56px → 34px** at ≤768, tracking staying `--track-display`.
- **Gutter `--gutter` (20px)** at narrow.
- **The dot grid stays**, at the same 24px step — it is a field, and a field that
  rescales stops reading as paper.
- **The dashed rules stay.** They carry meaning, not decoration.
- No horizontal overflow at 390: `documentElement.scrollWidth` equals 390.
- **Container queries.** Sorted by kind, because only the first three have a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | A data table collapsing to stacked rows | CONTAINER | `container-type: inline-size` on the panel, `@container` on the rows |
  | A card grid stepping 3 → 2 → 1 | CONTAINER | container on the grid, `@container` on the tracks |
  | A panel head stacking its label above its value | CONTAINER | container on the panel |
  | Display 56px → 34px | PAGE | the headline answers to the viewport, not to its column |
  | The dot grid's step | PAGE | it is a full-bleed field and the page owns it |
  | Nav collapsing | PAGE | the bar is the page's |
  | A rule's own width | SELF | **no container answer exists** — a container cannot query itself, and it does not change |

- **Viewport.** `100dvh` for any full-height section, never `100vh`.

## Motion tokens

| Token | Value | Spends on |
|---|---|---|
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | the default |
| `--ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | an entrance, if the page has one |
| `--dur-press` | 0.12s | the press — MEASURED, and inside the doctrine's 100–160ms band |
| `--dur-fast` | 0.15s | a border or colour change |
| `--dur-base` | 0.2s | the most frequent non-zero duration on the page |
| `--dur-slow` | 0.3s | a panel opening |

`ease-in` is banned by the doctrine and does not appear in the reference either.

## Signature motifs

- **Two bases at an alpha.** Text dims through the ink, structure dims through a navy
  that is never a word. 199 of 631 colour values carry an alpha; there is no grey ramp.
- **96.5% zero radius** — 1,418 of 1,469 visible elements. The record in this library.
- **The dot grid**, 0.8px of accent at a 24px step, under a section and nowhere else.
- **Dashed hairlines** for a provisional boundary — 10 elements.
- **The lit edge**: an inset side-rule in the accent at 28%, which marks a panel
  without lifting it.
- **Three faces, one job each**, and the mono owns every number.
- **11px as the working size**, tracked +0.18em when it is uppercase.

## Signature element

**The ruled data panel.** A zero-radius rectangle with a 1px navy-at-10% hairline, a
micro label in uppercase at +0.18em along its top, rows separated by `--rule-faint`,
every figure in DM Mono, and — on the one panel per section that is the subject — an
inset lit edge in the accent down its left and right sides.

It is what the page is remembered by, and the reason is what it refuses: no radius, so
it reads as a region of a sheet rather than a card; no shadow, so nothing floats; no
grey, because its quiet parts are the ink and the navy turned down. A reader who has
seen one knows where every number on the page will be.

Build it once as a component and let the page be made of them.

## Micro-interactions

- **Panel hover:** `--rule` → `--accent-rule` over `--dur-fast`. Nothing moves.
- **Primary press:** fill one step darker at `--dur-press`, no travel.
- **Focus-visible:** `--focus-ring` — two accent alphas, 4px spread and a 10px throw.
  It is the page's own and it is the loudest thing in the pack.
- **Row hover:** background to `--tint`. Never a border change; the rules are structure.
- **Link hover:** underline appears. The colour does not change — `--accent` is already
  the link.
- **Section reveal:** opacity only, `--dur-slow`. It never gates content.

## Bans

- **No scroll clock, no parallax, no scrub, no `animation-timeline`.** Zero occurrences.
  `MOTION_INTENSITY` above 2 has nothing to buy.
- **No grey ramp.** A quiet value is the ink or the navy at an alpha. Introducing
  `#6b7280` here is introducing a third base, and the pack's whole construction is
  that there are two.
- **The navy is never a word.** It is 1.21:1 at its working alpha. It rules and edges.
- **A rule is never the only separator.** At 1.21:1 a hairline is below every floor
  there is; the region it bounds must also change field, gain a label, or gain space.
- **No status by colour alone**, on either field.
- **No bold.** 500 is the ceiling at scale.
- **No radius above 5px.** The page is square and that is 96.5% of it.
- **No shadow on a panel.** Elevation here is an edge.
- **No scaling the working size up on a phone.** 11px is the argument.
- **No `ease-in`.**

## Gotchas

**An alpha is composited in sRGB, not in linear light, and getting that wrong inverts
the verdict on this pack's central mechanism.** Mixed in linear space, `--ink` at 0.6
computes 2.32:1 and reads as a failure that would force every tier to be redrawn.
Composited the way a browser does it, the same value is **4.98:1** and passes. The
first measurement pass of this pack made exactly that mistake and would have shipped a
correction to something that was never broken.

**Four corrections travel with the pack, each with its number at the declaration.**

1. *A grey that fails on every field it is used on.* The reference sets 48 text nodes
   in `#888e94`: 3.31:1 on white, 3.17:1 on the panel, 2.97:1 on the tint.
   `--ink-quiet` holds the hue and clears AA on all three.
2. *The lowest ink tier is not text.* The ink at 0.45 composites to `#919396`, which is
   3.08:1 on `#ffffff`, and the reference sets six live text nodes in it. Here it is a
   disabled label, a placeholder and an icon.
3. *The rules are below the mark floor and that is correct.* The navy at 10% and 5.5%
   composite to 1.21:1 and 1.10:1. They are rules, not marks — which is why the Bans
   require a second separator rather than a darker hairline.
4. *Tap targets.* 88 of 123 visible interactive elements at 1440 are under 44px, and 73
   of 106 at 390. `--tap-min` is a floor for every control.

**The dark band is not a dark mode.** One section closes the page in `#0b1015`; there
is no toggle and the sheet above is untouched. Its rules invert base rather than alpha
— white at 14% instead of navy at 10% — because a navy at 10% over near-black is
nothing at all. Putting `[data-surface="dark"]` on `:root` inverts a page that was
never designed to invert, and the light field's four statuses measure 1.4–2.6:1 if they
arrive unremapped.

**Three families is a budget, not a licence.** Space Grotesk for display, DM Sans for
sentences, DM Mono for numbers and keys — and nothing crosses. A number in the sans, or
a sentence in the mono, and the page stops being legible as a document.
