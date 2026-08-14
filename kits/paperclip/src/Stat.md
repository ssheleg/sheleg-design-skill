---
category: Data
---

Label above in mono, UPPERCASE, tracked `--track-label`, in `--muted`; value beneath in
the display face at weight 600 with `font-variant-numeric: tabular-nums`.

**The label goes above the value, not beneath it.** This pack's numbers are spends,
budgets and counts that update while the reader watches, and a label that sits under a
changing figure moves with it. Above, it holds still and the number changes inside a
fixed frame.

The value is never in a status colour. A number that is over budget says so in a word
beside it; the figure itself stays `--ink`.

```tsx
<Stat value="$140" label="Spent this month" source="/ $240 budget" />
```
