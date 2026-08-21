---
category: Surfaces
---

Elevation is a hairline: `1px --panel-line` at `--r-card` on the field, and no
shadow at rest. A shadow in this pack means an overlay.

`meta` is the uppercase eyebrow on the title row — 13px/600 at 1.82px tracking,
the reference's own label rhythm. It carries a count, a source or a state, never
a second title. The card is a container query root, so a metric inside it reflows
on the card's width rather than the viewport's: the rail is 321px and whether it
is open is not the window's business.

```tsx
<Card title="Backlink Exchange" meta="237 verified">…</Card>
```
