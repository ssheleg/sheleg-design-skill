# Design record — `roster`

Every value below was read off <https://www.babylovegrowth.ai/en> on 2026-08-13 through
CDP against computed styles at three viewports (5,936 rendered elements at 1440×900), and
every ratio was recomputed by importing `test/validate_palette.py`. A `lab()` value was
resolved by painting it into a 1×1 canvas and reading the sRGB bytes back; where a value
is a pack decision rather than a reading it says so, here and at its declaration.

## Type — two families with an unusual division of labour

| Role | Measured | Instances |
|---|---|---|
| Hero display | **Plus Jakarta Sans** 600, 68px/80px | the visible headline — a `<span>`, not the `h1` |
| Section head | **Raleway** 600, 52px/65px | 6 |
| Eyebrow | Raleway 400, 16px/24px, letter-spacing **0.4px**, uppercase, orange | 16, and each is marked up as an `<h2>` |
| Body, dominant | Plus Jakarta Sans 300, 16px/28px | 44 |
| Body, emphasis | Plus Jakarta Sans 600, 16px/28px | 49 |
| Control label | Plus Jakarta Sans 500, 12px/16px | 60 |
| Small | Plus Jakarta Sans 400, 14px/20px | 44 |

Font stacks over 5,936 elements: **Plus Jakarta Sans 5,738, Inter 116, Raleway 78,
`ui-serif` 4.** The display face is the *body* face at 68px, and the section heads are a
different family entirely — the inverse of the usual arrangement, and the thing that
makes the page feel like a document with a poster on the front.

**The display steps; it does not slide.** 36px/54px at 390, 60px/70px at 768, 68px/80px
at 1440, and **no `clamp()` appears anywhere in either stylesheet**. A fluid ramp here
would be an invented value.

**The `h1` is invisible, and the visible headline is not a heading.** The `h1` is
`.sr-only` — 1×1px, white, `position: absolute`, `clip-path: inset(50%)`,
`white-space: nowrap` — carrying *"Grow organic traffic from AI Search on autopilot"*.
The 68px line a reader sees is a `<span>`. Meanwhile all 16 `h2`s are the small orange
eyebrows, so the document outline reads *eyebrow* where the page reads *section head*.
This is the exact opposite of `manpage`, whose signature is that the visible label chip
**is** a real `<h2>`, and the pack says which of the two it teaches.

## Palette — a framework's greys, and a small undisciplined bespoke layer

**The neutrals are Tailwind v4 defaults emitted as `lab()`.** Thirty-four distinct
`lab()`/`oklab()` values were resolved from painted pixels; the ones that carry the page:

| `lab()` as computed | Resolves to | Where | On `#ffffff` |
|---|---|---|---|
| `lab(91.6229 -0.159115 -2.26791)` | `#e5e7eb` | **7,234** borders | — |
| `lab(27.1134 -0.956401 -12.3224)` | `#364153` | 458 ink | 10.30:1 |
| `lab(8.11897 0.811279 -12.254)` | `#101828` | 242 ink | 17.75:1 |
| `lab(96.1596 …)` | `#f3f4f6` | 24 fills | — |
| `lab(47.7841 …)` | `#6a7282` | 53 ink | 4.84:1 |
| `lab(65.6464 …)` | `#9f9fa9` | 63 ink | — |
| `oklab(0 0 0 / 0.05)` | `#000000` at α 0.051 | 8 borders | — |

**The bespoke layer is small and it is not disciplined.** Four near-blacks —
`#2c2f2e` (42), `#212427` (34), `#171717` (30) and `#0f0a0a` (the hero CTA's fill) — and
**two oranges**: `#fa5c12` on the headline phrase and `#f25533` on the nav pill. Also
`#00b67a` and `#2ee5ac` (the review badge's greens, which belong to a third party),
`#e8f7f4` a pale mint, `#f0f3f8` the section band, `#f6f1eb` a cream, `#2a76f6` a blue.

A pack cannot ship four inks and two accents, so it picks one of each and marks the
choice. Ratios, recomputed:

| | On `#ffffff` |
|---|---|
| `#0f0a0a` | 19.66:1 |
| `#171717` | 17.93:1 |
| `#212427` | 15.60:1 |
| `#2c2f2e` | 13.52:1 |
| `#6a7282` | 4.84:1 — and **4.35:1** on the `#f0f3f8` band it is painted on |
| `#fa5c12` | **3.18:1** |
| `#f25533` | **3.43:1** |
| white on `#0f0a0a` | 19.66:1 |

**Gradients interpolate in oklab**, which is worth copying:
`linear-gradient(to right in oklab, #fa5c12, #b73f06)` on three elements, plus radial
coral glows at `rgba(242, 85, 51, 0.18)`.

## Texture & surface

- **Radii:** the full pill on 102 elements (computed as `3.35544e+07px`, the clamped
  maximum), then 8px (78), 12px (77), 16px (46), 24px (7), and 4/5/6/7 in single figures.
  Both CTAs are 12px, not pills; the pills are labels and chips.
- **Shadow is essentially absent.** The value on 101 elements is Tailwind's
  all-transparent ring composite — a shadow slot with nothing in it. The page separates
  by **hairline and pill**: 1px `#e5e7eb` on 53 elements, `#cecece` on 30, `#e5e5e5` on
  25, `#e0e0e0` on 21.
- **The field is patterned, not plain.** A repeating SVG grid of small squares
  (`squares-bg-1.svg`) under the hero, with **34 square logo tiles** ≤40px scattered on
  it — the AI engines and the product's own feature marks.
- **Container 1152px** at all three viewports; one 1440px full-bleed shell.

## Motion — two floats, no clock, and reduced motion honoured six times out of twenty

- **Transitions:** `.15s cubic-bezier(0.4, 0, 0.2, 1)` on 54 elements, `box-shadow .15s`
  on 21, `opacity` at .15s/.2s/.3s/.5s/.7s, `transform .15s` on 5, and one
  `max-height 0.7s` (an accordion).
- **There is no scroll clock:** 0 elements with `animation-timeline`, `scroll-behavior:
  auto`, 1 sticky and 1 fixed element (the nav).
- **Its own keyframes**, beside the framework's: `ebook-float-primary` (5.5s ease-in-out),
  `ebook-float-secondary` (6.5s), `pricing-card-enter`, `pricing-price-swap`,
  `promo-rotate-in`, `promo-gradient-shift`, `accordion-down`/`up`, `fadeIn`,
  `arrow-nudge`, `skeleton-blink`, `spinner-glide`, `spinner-hop`, `settings-ripple`,
  `meta-preview-float`, `meta-preview-gradient`, `ga4-initial-sync-bar`.
- **And the reduced-motion branch names classes one by one.** Two rules, covering
  `.pricing-card-enter`, `.pricing-price-swap`, `.promo-rotate-in`,
  `.ebook-float-primary`, `.ebook-float-secondary` and `.promo-animated-gradient` —
  **six of roughly twenty.** `arrow-nudge`, `skeleton-blink`, both spinners,
  `settings-ripple`, `meta-preview-float` and the accordions keep running. This is the
  opposite failure to `pigeonhole`'s reference, which collapsed everything globally with
  one `*` rule and got the marquee wrong by doing so: here the list is explicit and
  incomplete, which is the failure mode of a per-class approach.

## Components, as measured

| | Measured |
|---|---|
| Hero CTA | `#0f0a0a` fill, white **18px/700**, radius 12px, padding 16px 32px, no shadow — 19.66:1 |
| Nav CTA | `#f25533` fill, white **16px/600**, radius 12px, padding 12px 32px — **3.43:1** |
| Industry column head | a pill label above a hairline-divided column of client logotypes, six across |
| Step card | a number in orange, a head, body, two check chips, a product screenshot, and a progress rail with prev/next |
| Case card | a chart or a portrait, a coloured link, a quote |

## What the measurement refuted

**The engine wordmark does not rotate — at least not inside six seconds.** The hero sets
a third party's logotype inline after the word *from*, and it was sampled seven times
across 5.4 seconds with no change to the hero's text or its marks. So the pack specifies
it as **one wordmark set inline, chosen per page** and explicitly does not claim a
carousel. If a later reading catches it rotating, that is a correction to make with a
measurement beside it — not a guess to ship now.
