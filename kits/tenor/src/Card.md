---
category: Surfaces
---

Square, `--bg` fill, one hairline. There is no radius and no shadow in this pack, so a
card is a rectangle and nothing more.

Prefer `Lattice` + `LatticeCell` for anything that comes in threes: the pack's structural
unit is a cell in a grid, not a card floating on a page. Reach for `Card` only when a
block genuinely stands alone.

A card is never nested inside a card. If it needs internal structure, it needs a `Rule`.

```tsx
<Card title="Guardrails" meta="03">
  …
</Card>
```
