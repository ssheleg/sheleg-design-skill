---
category: Surfaces
---

The bounded surface of a product screen: `--panel` on a 1px `--border` at
`--r-card`, with a title row that carries its metadata on the right. `meta` is
set in the data face — a run id, a count, a timestamp — which is why it belongs
there and not inside the body. No gradient, no shadow: the border is the
elevation. Nest at most one level; a card inside a card inside a card is a
table that has not admitted it yet.

```tsx
<Card title="Ingest pipeline" meta="run 8842 · 14:02 UTC">
  <StatusDot status="running" label="Backfilling shard 3 of 12" />
</Card>
```
