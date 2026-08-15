---
category: Data
---

The figure is 34px UI face at weight 400, tracked `-0.03em` — **not** the
monospace. That surprises people who read "mono for all data" and reach for it
here: the reference sets `$4.40M` in Inter and keeps the monospace for the rows,
ids and timestamps underneath. The big number is prose about the business; the
table is machine output.

`source` is not decoration. A figure with no stated origin is the thing this
pack exists to refuse, so where the number came from goes on the tile — and if
the number is model-derived, the card around it carries a `Seal`.

```tsx
<Stat value="$4.40M" label="MRR · All plans" source="governed metric · Stripe" />
```
