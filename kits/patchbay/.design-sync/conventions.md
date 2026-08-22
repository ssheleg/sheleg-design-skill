# Patchbay — what the design agent may not do

A near-black field, one mint-cyan, and a live schematic, measured off
<https://nautilustrader.io/> on 2026-08-22 with `getComputedStyle`. The
reference declares no custom properties at all, so every value in the token
layer was read off a painted element rather than lifted from a stylesheet.

## Bans, each with a measurement behind it

- **No shadow, anywhere.** Not on a card, not on a button, not on the nav. The
  reference paints none. Elevation is the hairline ladder — 8% white — and a
  shadow reads as a different design system bolted on.
- **No white on the accent.** `#00CFBE` takes white at **1.97:1**. A filled
  accent control takes `--on-accent` (9.81:1). The reference never fills one.
- **No second functional hue.** `--accent-far` is one stop in one button's
  gradient. In a diagram, colour means *belongs to the system*; a second hue
  makes the drawing lie.
- **No `opacity` for a disabled state.** It composites against whatever is
  behind it and the resulting ratio is unknowable. Name the pair.
- **No 30% white label.** The reference sets its diagram group labels at 9px in
  `rgba(255,255,255,.30)` — **2.70:1**. Use 50%, which is 5.19:1 and which the
  reference already uses for its own legend.
- **No counter that renders zero when the fetch failed.** The reference ships
  `0+` under `GITHUB STARS` on a live page. `Stat` here refuses.
- **No SMIL animation without a pause path.** CSS `animation-duration` does not
  reach `<animateMotion>`, so a blanket reduced-motion rule cannot stop it.
  `Diagram` calls `pauseAnimations()`.

## Two shapes that are easy to get wrong

- **The card is a light, not a fill.** `radial-gradient(circle at 50% 0,
  --card-lit, --card-base)` with a 1px border in the accent at 14%. The centre
  stop is a teal-black, so the card reads as lit from its top edge. Flattening
  it to a solid background loses the whole surface idea.
- **The node's tint is its only variable.** Every port in the diagram is the
  same box at the same radius with the same type. The ones that belong to the
  system are tinted with the accent; everything else is tinted white. Changing
  the size or the radius to signal importance breaks the drawing's grammar.
