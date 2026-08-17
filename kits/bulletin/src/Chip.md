---
category: Foundations
---

A chip is the small outlined object the pack repeats everywhere: a tag, a
filter, a platform label. `--r-pill`, a 1px `--line`, and `--shadow-1` at 2px —
the smallest step of the offset ramp, because the offset grows with the object.

`accent` tints with `--accent-wash` rather than filling with `--accent`: the
accent is a fill for exactly one control per view and a chip is never it.
`selected` keeps its state after the pointer leaves.

```tsx
<Chip>Instagram</Chip>
<Chip tone="accent" selected>Agencies</Chip>
```
