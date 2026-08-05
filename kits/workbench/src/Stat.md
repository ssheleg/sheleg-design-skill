---
category: Data
---

The quiet stat tile: an uppercase 12px label, a 20–28px tabular-nums value in
the data face, and an optional `source` line underneath. `source` is the
honest half — a figure whose window and query are unstated is a figure nobody
can act on, so name them ("last 24h · p95 across all regions"). The tile sits
on `--panel-2` inside a 1px border and carries no meaning-free colour.

```tsx
<Stat value="128 ms" label="p95 latency" source="last 24h · all regions" />
<Stat value="3" label="Open incidents" source="pagerduty · live" />
```
