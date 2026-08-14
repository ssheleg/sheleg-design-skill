---
category: Data
---

Mono, `tabular-nums`, weight 700 for the value; the label beneath in the nano step —
10px, uppercase, tracked `.12em`, `--muted`. A count that changes while the reader
watches must not reflow, which is the whole reason the figures are tabular.

A row of stats sizes against its **container**: three across in a card, one column in a
sidebar.

```tsx
<Stat value="17" label="steps" />
<Stat value="0:36" label="elapsed" source="live" />
```
