---
category: Foundations
---

`1` is the display at `--t-display` (80px, stepping to 72 and 64) in `--font-display`
at `--weight-regular` and `--track-display`. `2` is 48px at `--weight-strong`, same
tracking. `3` is 24px, and it is the card title.

The display holds **two lines** and the column holds the display — there is no measure
on it. Put one gradient word per heading and no more: wrap it in
`<span className="dm-word">`, which ships `--gradient-word` with its solid fallback
`color` underneath.

```tsx
<Heading level={1}>Not a tool. <span className="dm-word">A hire.</span></Heading>
```
