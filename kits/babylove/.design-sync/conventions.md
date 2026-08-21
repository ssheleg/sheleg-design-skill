# Babylove — what the design agent may not do

Seven brand tokens and Tailwind v4's greys, measured off
<https://www.babylovegrowth.ai/en> and its dashboard on 2026-08-21. Read this pack
against `outrank`: same category, 536 properties there and seven here, and both ship.

## Bans, each with a measurement behind it

- **No shadow.** Separation is a 1px border and a one-step tint. Exactly one 6px
  shadow exists in the whole product.
- **No word in `--brand`.** `#FA5C12` is 3.18:1 on the page and white on it is
  3.18:1 — it fails as text in both directions. `--brand-ink` (`#B73F06`, 5.63:1)
  is the one that carries a word. The reference's own hero CTA is near-black for
  exactly this reason; do not "fix" it to the brand colour.
- **No second hue.** One orange, six steps, Tailwind's greys, nothing else.
- **No skeleton.** A card that is computing wears a `Running analysis` chip; every
  other surface stays drawn.
- **No dark theme.** The reference ships one field, and inventing a twin means
  inventing thirty values with a citation attached.
- **No scroll-driven motion.** The ceiling is 2 and the budget is one 0.15s colour
  transition.

## Two shapes that are easy to get wrong

- **The card inside the card is the layout.** 16px radius on `--surface` outside,
  8px on `--surface-2` inside, tinted one step apart. Flattening it to one level
  loses the grouping that makes a section readable.
- **Leading equals size** — on the headline (76/76) and on the metric (30/30). Do
  not lead either like prose.
