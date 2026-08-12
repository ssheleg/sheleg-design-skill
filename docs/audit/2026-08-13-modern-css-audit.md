# Audit — how modern is this skill's design and typography?

Measured 2026-08-13 against the tree at `95cb8ed` (v1.21.0, sixteen packs, sixteen
kits). Every count below is a grep or an arithmetic check over the shipped bundle
and the shipped kits; nothing here is an impression. Where a number is a ratio or a
colour it was computed by importing `test/validate_palette.py`.

**The verdict in one line: the colour science is ahead of the field and the
vertical rhythm and layout are about three years behind it.**

## Ahead of the field

| Practice | Coverage | Note |
|---|---|---|
| OKLab ΔE plus protanopia / deuteranopia / tritanopia simulation | the whole palette gate, with hard floors | almost no design system checks dichromatic separation at all |
| `color-scheme` declared | **16 / 16** token layers | consistent, and it is what makes form controls and scrollbars agree with the pack |
| `text-wrap: balance` | **13 / 16** kits | documented in only 3 packs — the code is ahead of the doctrine |
| `font-variant-numeric: tabular-nums` | **10 / 16** kits | correct instinct for a library with three number-led packs |
| `svh` / `dvh` behind `@supports`, bare `100vh` banned | doctrine, with the failure named | `field-notes.md:268-270` |
| `prefers-reduced-motion` as a hard requirement | the whole library | and `pigeonhole` v1.21.0 found the case a duration alone cannot fix |
| A frequency table that caps the motion dial | `MOTION_DOCTRINE.md` | more sophisticated than most systems' "use 200ms" |

## Deliberate positions, not defects

- **WCAG 2.x only.** That is the standard; APCA is a draft. Worth *knowing* about
  the divergence in the one place WCAG 2 is understood to misjudge — dark text on
  saturated mid-tones — which is exactly `pigeonhole`'s taxonomy.
- **Measured literals rather than a modular scale.** The library's whole thesis:
  values come off a live reference. Gated, defensible, and not to be "modernised".
- **Container queries are reasoned about, not ignored.** `field-notes.md:271-274`:
  *"No container queries… If you add them, add them for the app layer's panels —
  not for the page, whose column widths are the layout."* Sound for a page pack.
  The gap is that the reasoning never reached the component library (below).

## The gaps, by descending value

### 1. Container queries: 0 of 16 kits, against 7 viewport media blocks
The doctrine settled the question for a *page* and never covered the *component
library the project ships*. A `Card` or a `LabelledRow` placed in a 360px sidebar
breaks at a viewport breakpoint even though its own width is known. `cqi`/`cqw`
units: 0.

### 2. The `color-mix()` ban was a parser limitation — **closed in 1.22.0**
`STYLE_PACK_TEMPLATE.md` used to read *"the palette gate cannot compute a value it
cannot parse, so keep `color-mix()` and `lab()` out of the token layer."* The cost
was measurable. A sweep of all sixteen token layers for `rgba()` literals against
the tokens in the same file:

| | count | meaning |
|---|---|---|
| **EXACT** | **42** | the literal *is* a token's colour with an alpha — `rgb(from var(--token) r g b / a)` is a byte-for-byte replacement |
| **NEAR** | 13 | within ΔE 2 of a token but not equal. **Not automatically drift** — `rgba(255,255,255,0.8)` beside an off-white `--bg` may be deliberately white. Each needs its author, not a script |
| OWN | 45 | a colour in its own right; leave alone |

The 42 are the live mechanism behind board B-023/B-024: re-tint `--accent` and the
focus ring keeps the old blue. `showroom`'s ring is migrated in 1.22.0 as the worked
example, literal first and derived second — because relative colour is Baseline 2024
and a dropped declaration on a focus ring is an invisible focus indicator.

### 3. `text-box-trim` / `text-box-edge`: 0
A library that specifies line-height to three decimals and radii to the pixel still
trims half-leading by hand. This is the primitive that makes a 60px/1.0 display
measure its cap height instead of its font metrics.

### 4. Measure in pixels: 3 token layers in `px`, **0 in `ch`**
`--measure-body: 650px` stops being a measure the moment the typeface changes. `ch`
(or `ex`) ties the column to the font, which is the point of a measure. Only 3 of 16
packs name a `ch` value anywhere in prose (`editorial-luxury` 66ch, `prism` 48–75ch,
`workbench` 65ch).

### 5. Metric-matched fallbacks: 0
`font-display` appears in 21 files, and `size-adjust` / `ascent-override` /
`descent-override` in none. That pair is the modern zero-CLS technique: without it,
`swap` is a guaranteed reflow on every first paint.

### 6. `@property`: 0 of 16
Every token is untyped, so none can be animated or interpolated, and none declares
`syntax`, `inherits` or `initial-value`. For a library whose product *is* a token
layer this is free rigour left on the table.

### 7. Fluid spacing: 0 of 16
Type is fluid in 5 layers; space never is. A page that scales its headline and not
its rhythm changes proportion as it narrows.

### 8. Variable fonts: `font-variation-settings` 0, `font-optical-sizing` 1
Packs name static weights while their own references ship variable families (Geist,
Inter Display). Optical sizing is the axis a display face most wants.

### 9. Zero across the board
`text-wrap: pretty` (the body-copy half of the pair — widows and orphans), logical
properties (`margin-inline`, `padding-block`), `:has()`, `aspect-ratio` (art-direction
ratios live in prose — `pigeonhole` states "1152×703 ≈1.64:1" in words), View
Transitions, `@starting-style` + `transition-behavior: allow-discrete`, `linear()`
easing, `display-p3` and `@media (color-gamut: p3)`, `light-dark()` — while three
packs duplicate whole blocks under `[data-theme="dark"]`.

### 10. Design-token interop: 0
No `$type`, no `$value`, no DTCG JSON. `FIGMA_BRIDGE.md` exists and Figma variables
are mentioned twice, but Tokens Studio and Style Dictionary cannot read a CSS custom
property file.

## What 1.22.0 does about it

Only the second finding, and only its unlocking half:

- The palette gate computes `color-mix()` in four spaces and `rgb(from …)`, with
  `var()` resolved inside a value. **Verified against Chrome 151 across eleven cases,
  worst ΔE 0.004** — the residual is the browser's own six-digit serialisation.
- Four new self-test plants, two of which prove the new paths are *checked* rather
  than tolerated: a mix and a relative colour that miss AA must fail on the ratio,
  which is only possible if the parser really computed them. Two prove the refusals
  still refuse — an unimplemented mix space, and a `calc()` channel.
- `themes()` now asks `COLOR_SHAPED` instead of a hand-written `#`-or-`oklch(`
  prefix list. Without that, a dark theme written in `color-mix()` would have been
  read as "overrides no colour" and skipped — a blind spot opened by the same commit
  that closed a limitation.
- The skeleton's rule 5 replaces the ban, with the limits and one migration rule.
- `showroom`'s focus ring migrated as the worked example.

Everything else is on the board: **B-027** (the 42-site migration, which needs the
support decision per property), **B-028** (the 13 NEAR literals, one author judgement
each), **B-029** (container queries in the kits), **B-030** (`text-box-trim`, measure
in `ch`, metric fallbacks, `@property`, fluid spacing), **B-031** (DTCG export).
