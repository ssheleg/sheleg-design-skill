# Design record — `pigeonhole`

Every number below was read off <https://www.getinboxzero.com/> on 2026-08-12
through CDP `Runtime.evaluate` against computed styles, at three viewports, and
every ratio was recomputed by importing `test/validate_palette.py`. Where a value
is a pack decision rather than a reading it says so, here and at its declaration.

## Type — two families, and the display never gets louder

| Role | Measured | Instances |
|---|---|---|
| Display | `aeonikFont` **400**, 60px/60px at 1440 | 2 (the `h1`, 2 lines in a 780px column) |
| Section head | `aeonikFont` 400, 40px/50px | 11 |
| Sub-head | `aeonikFont` 400, 20px/24px | 9 |
| Body, dominant | `Geist` 400, 14px/24px | 59 |
| Body, larger | `Geist` 400, 16px/24px | 34 |
| Body, emphasis | `Geist` 600, 16px/24px | 19 |
| Control label | `Geist` 500, 14px/20px | 14 |
| Lede | `Geist` 400, 18px/28px | 11 |
| Chip label | `Geist` 500, 12px/16px | 9 |
| Smallest | `Geist` 500, 10px/15px | 1 |

Font stacks over 912 rendered elements: **Geist 878, Aeonik 34.** The display
face is rare *and* light — weight 400 at every size it appears at, never 500,
never 600. The retrospective's most recent entry exists because a reference
library reported a display weight of 600 where the computed value was 500, so
this was read rather than assumed.

**One italic word.** The headline's emphasis is a real `<em>` — `aeonikFont` 400
italic, 60px, 213px wide inside the 780px column. Not a colour change, not a
weight change, not a highlight: the one typographic event in the hero.

**Fluid, by `clamp()`.** Seven ramps ship: `clamp(24px,2.8vw,32px)`,
`clamp(28px,4.4vw,52px)`, `clamp(32px,4vw,48px)`, `clamp(40px,4.6vw,56px)`,
`clamp(40px,5.6vw,60px)`, `clamp(40px,6vw,64px)`, and one width
`clamp(258px,32vw,400px)`. Measured display size: **60px at 1440 and at 768**
(both cap), **34px at 390** in 3 lines. Section heads: 40px → **27.2px**.

## Palette — a white field, a two-stop blue, and a taxonomy

Base against `#ffffff`, recomputed by the gate:

| Token role | Measured | On `#ffffff` | On `#f9fafb` |
|---|---|---|---|
| Display ink | `#242424` | **15.52:1** | 14.85:1 |
| Strong ink | `#3d3d3d` | **10.86:1** | 10.39:1 |
| Muted ink | `#848484` | **3.74:1** — fails AA | 3.58:1 |
| Framework body ink | `#6b7280` (79 elements) | 4.83:1 | 4.63:1 |
| Framework heading ink | `#111827` | 17.74:1 | 16.98:1 |
| Faint ink | `#9ca3af` | 2.54:1 | 2.43:1 |

**Two neutral families ship side by side.** The bespoke ramp
(`#242424`/`#3d3d3d`/`#848484`) carries the display and the ledes; Tailwind's
`gray`/`slate` defaults carry the dominant body text — `#6b7280` on 79 elements
against the bespoke `#848484` on 47. The application's own token block is
**unmodified shadcn slate** (`--primary: 222.2 47.4% 11.2%`), so the whole
bespoke layer lives in the marketing page and nowhere else.

**The CTA is a gradient, not a fill.** `linear-gradient(#2965ec, #5c89f8)`,
radius 13px in the hero and 14px in-page, label `Geist` 500 16px/24px, padding
11.7px / 22px, and a shadow tinted to its own hue:
`rgba(75,131,253,0.2) 0 2px 10.1px`. White on the upper stop is **5.04:1**; on
the lower stop **3.29:1**.

### The taxonomy — nine categories, measured

Each chip renders **twice**: an outer chip at radius 8px in the deeper tint pair
holding an inner chip at radius 7px in the paler one. Ink is saturated, the wash
is the same hue.

| Category | Ink | 50 | 100 | 150 | 200 | Worst on its own ramp |
|---|---|---|---|---|---|---|
| To Reply | `#124dff` | `#eff3ff` | `#d9e2ff` | `#d5defc` | `#c2d0fc` | **3.89:1** |
| Newsletter | `#6410ff` | `#f3eafe` | `#e7daff` | `#e1d5fc` | `#d7c3fc` | **4.28:1** |
| Marketing | `#17a34a` | `#f3ffef` | `#e1ffd8` | `#ddf4d3` | `#cff4c0` | **2.72:1** |
| Calendar | `#d8a40c` | `#fffbef` | `#fff3da` | `#e7e0cb` | `#e7dbb9` | **1.65:1** |
| Notification | `#c94244` | `#ffeef0` | `#ffdadb` | `#fdd3d4` | `#fcc0c0` | **3.09:1** |
| Cold Email | `#49d1fa` | `#feffff` | `#e5f9ff` | `#e5f9ff` | `#d0f4ff` | **1.53:1** |
| Team | `#e65707` | `#fff5ef` | `#ffe7da` | `#fce2d5` | `#fcd6c2` | **2.71:1** |
| Urgent | `#c942b2` | `#ffeef8` | `#ffdaec` | `#fdd3eb` | `#fdbfe0` | **2.79:1** |
| STEP *n* | `#525252` | `#ffffff` | `#f6f6f6` | `#eeeeee` | `#e6e6e6` | 6.26:1 |

**Eight of nine fail 4.5:1 against the very tint the reference paints them on.**
The CSS declares two further hues the page does not use as categories
(`new-brown`, `new-pink` beyond Urgent's ramp), for eleven in total.

### The decision this forced, and the number behind it

The register is worth keeping and the ink is not, so each failing ink is darkened
along OKLab **L** — hue and chroma held — until it clears 4.5:1 against the
deepest tint in its own ramp. That is a **pack decision**, marked `SELECTED` at
its declaration, and its cost is measured rather than assumed:

| Set | protanopia | deuteranopia | tritanopia |
|---|---|---|---|
| As measured on the reference | ΔE 7.48 (marketing/calendar) | ΔE **4.42** (marketing/notification) | ΔE 7.03 (notification/urgent) |
| Darkened to clear AA | ΔE 4.47 (calendar/team) | ΔE **1.24** (marketing/notification) | ΔE 3.83 (notification/team) |

> The darkened figures are read off the **rounded** hexes the token layer ships.
> An earlier pass took them from the unrounded OKLab candidates and reported ΔE
> 1.84 and a 4.50:1 floor that `#007b22`'s parent satisfied and `#007b22` itself
> did not (4.38:1). Eight bits per channel is where a derivation is finished, not
> where it is rounded off for display — the repository has shipped four ratios
> stated from an OKLCH parent before, and this is the same class caught earlier.

Compliance and discriminability pull against each other here: pushing L down
compresses the space, so the accessible set is *harder* for a dichromatic reader
to tell apart than the inaccessible one. Eleven hues cannot be simultaneously
AA-compliant and mutually distinguishable under deuteranopia, and pretending
otherwise would be the failure this repository's palette gate exists to catch.

**So the pack does not pretend.** The category hue is declared a *redundant*
channel, the label word is mandatory (a Ban), and the category tokens are
deliberately outside the gate's semantic peer set — with ΔE 1.84 written at the
declaration so that when B-017's widening lands, the next run reads the reason
instead of assuming an oversight.

## Texture & surface

- **Radii, by frequency:** `9999px` (35 — badges), `32px` (21 — panels and FAQ
  cards), `20px` (12), `13px` (10 — buttons), `8px` / `7px` (12 each — the outer
  and inner chip), `52px` (8 — the enterprise band), `14px`, `38px`, `43px`.
- **One shadow does almost all the work:** `rgba(151,151,151,0.08) 0 3px 12.9px`
  on 40 elements. The hero frame is the exception:
  `rgba(0,0,0,0.1) 0 14.3px 38.74px 3.9px, rgba(0,0,0,0.05) 0 0 4.16px`.
- **Tinted shadows.** A pastel card's shadow is mixed toward its own hue —
  green `rgba(207,249,222,0.22) 0 2px 3.4px` + `rgba(118,217,143,0.11) 0 1px 1px`,
  blue `rgba(207,217,249,0.22)`, red `rgba(249,207,211,0.15)`. The hue leaks past
  the edge of its own card, which is why the page reads tinted while remaining
  white.
- **Hairlines, not borders:** `1px rgba(231,231,231,0.5)` on 43 elements, then
  `#f7f7f7` (19), `#f3f3f3` (12), and one `2px #e3e3e3` (12).
- **Surfaces are barely gradients:** `linear-gradient(#ffffff, #f9f9f9)` on 19.
- **Measure:** container `1152px`, hero column `780px`, lede `640px`, a
  `650px` body measure on 10 elements, 24px gutters at 390.
- **Nesting, and it settles nothing:** the enterprise band is 52px outer / 32px
  inner at 21px padding. Subtraction predicts 31px, proportional predicts ~32px.
  Evidence for B-020, not a resolution of it.

## Motion — entrance only, and no clock

- **Transitions:** `all .15s cubic-bezier(.4,0,.2,1)` (10), `.2s` (4), `.3s` (4),
  and exactly one overshoot: `.3s cubic-bezier(0.175,0.885,0.32,2.2)`.
- **Own keyframes:** `marquee` at **100s linear** (the logo wall). `bounce`,
  `pulse`, `spin` are framework defaults; the rest belong to a toast library.
- **The hero enters word by word.** Each of the headline's words is its own span
  carrying inline `opacity`, `filter: blur()` and `transform` — 20 of them,
  settled at `opacity: 1; filter: blur(0px)` once the entrance finishes. A
  per-word blur-in, driven by a motion library rather than CSS.
- **There is no scroll clock.** Zero elements with `animation-timeline`, zero
  `position: sticky`, zero `position: fixed`, `scroll-behavior: auto`. Nothing
  scrubs, nothing parallaxes, the nav does not stick.
- **Reduced motion is honoured globally** — two rules, the first collapsing
  `transition-duration` and `animation-duration` to `0.01ms` on `*`. The pack
  inherits this as a hard requirement rather than a nicety, because the reference
  passes it and a pack that regressed it would be worse than its own source.

## Structure worth borrowing

The FAQ is a `<dl>` with **7** `<dt>`/`<dd>` pairs and no `<details>`, so every
answer is in the served HTML; 2 JSON-LD blocks; 23 `h2`s and 9 `h3`s. The same
choice `manpage` records from a different reference, and it belongs in the pack
because a chip that is also a real heading is the cheapest structural win on the
page.

## What the page is made of, and what it is not

The product art is **raster**, served through `/_next/image`: hero 1150×631, the
before/after section 1152×703, the next 1152×539, then 722×250, 355×171, 331×201.
Fourteen of the page's 74 `<img>` elements are product art; the rest are the nine
logo SVGs, duplicated for the marquee. The pack therefore specifies the set piece
as art direction — subject, aspect ratio, treatment — and never as a component,
because an agent handed "build the diptych" would invent a DOM technique the
reference does not use.
