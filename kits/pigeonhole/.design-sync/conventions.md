# Pigeonhole — the design contract

The reference is <https://www.getinboxzero.com/>, measured 2026-08-12 off its
computed styles at 1440×900, 768×1024 and 390×844. The full pack is
`styles/pigeonhole.md`; this file is what a design agent must not get wrong.

## The one thing this pack is

**The label system is the design system.** A white wall, hairlines instead of
borders, a display face that never passes weight 400, and nine pastel categories in
which a hue *is* the category — each rendered as a two-layer chip: the deeper tint
pair outside at 8px, the paler pair inside at 7px, one pixel between them.

## Non-negotiable

- **A category chip always carries its word.** The component's type requires it.
  Darkened to clear WCAG AA, the worst deuteranopic pair among the nine inks sits
  **1.24 ΔE** apart — under the palette gate's hard floor of 10 — so hue is a
  redundant channel and the label is the real one. Status, likewise, is never by
  colour alone.
- **Weight 400 for the display, always.** Level 1 is
  `clamp(34px, 5.6vw, 60px)` on line-height exactly 1. A 600 display is a
  different pack.
- **One italic word per page**, inside the headline, same face, same weight.
- **The primary button's gradient runs light-to-dark.** White on the reference's
  lower stop measures 3.29:1 and on its upper stop 5.04:1; the kit reverses the
  ramp so the label's worst case passes.
- **`:focus-visible` is 2px `--accent-strong` at 2px offset.** The reference ships
  `outline-style: none` on its focused primary CTA. Do not copy that.
- **A tinted card's shadow is tinted to its own hue**, never to black.
- **Elevation is a hairline.** One soft shadow (`--shadow-card`) is a hint, not a
  hierarchy; `--shadow-hero` belongs to the product frame alone.

## Banned

- A chip with no label word. A hue-only category. A status told by colour alone.
- A bolder display, or a second accent hue.
- Any scroll clock: no scrubbing, no parallax, no sticky nav, no
  `animation-timeline`. The reference has none of these, measured.
- **Rotation.** Zero rotated elements at three viewports. A scattered, tilted pile
  is not this pack, however much a screenshot suggests it.
- `<details>` for an answer a crawler should read — the FAQ is a `<dl>`.
- A dark theme. None was measured, and inventing one invents values.
- Black shadows under tinted cards.

## Art direction, not components

The page's set pieces are **raster art** on the reference: the chaos-to-order
diptych at 1152×703 (≈1.64:1), the hero frame at 1150×631, the next section at
1152×539. Compose them as art with a subject, an aspect ratio and a treatment.
`LabelledRow` is the component; the pile is a picture.

## Motion

Entrance and hover only. The one motion worth copying is the headline's
**word-by-word blur-in** — each word its own element, entering on opacity and
`filter: blur()` at `--stagger-word`, settling at `blur(0px)`. `--ease-overshoot`
is spent on exactly one element, as the reference spends it. Everything collapses
under `prefers-reduced-motion`, which the reference honours globally.
