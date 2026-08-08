---
category: Data
---

Ink at 6% on `--radius-sm` with `4px 8px` of padding, DM Mono at `--t-sm`.

The 4px radius is arithmetic, not taste: a chip sits inside a 16px window with
12px of padding, and `16 − 12 = 4`. Concentric curves are what separate a
machined object from two rectangles that happen to touch, and the reference gets
this right throughout — copy the arithmetic, not the number.

`tone="accent"` fills with `--accent` and labels it `--on-accent` at 7.46:1.
Accent-coloured *text* on the field is a different thing and is banned: it
measures 1.71:1 on the pack's worst stop.

```tsx
<Chip>Phase 2 of 5</Chip>
<Chip tone="accent" selected>Go-to-market</Chip>
```
