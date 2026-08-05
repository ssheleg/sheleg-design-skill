---
category: Signature
---

Honest state, in 8 pixels. Workbench reserves semantic colour for state alone,
and this is where that vocabulary lives: `running` is `--info` (deliberately
the accent hue, because "working" is the product's own signal and not a new
colour), `ok` is `--ok`, `warn` is `--warn` and means a human is needed, `danger`
is `--danger`, `idle` is muted. Never show a dot the system has not verified —
no optimistic green, no fake "connected". Pass `label` whenever the row does not
already spell the state out; without one the dot carries its own `aria-label`.

```tsx
<StatusDot status="running" label="Backfilling shard 3 of 12" />
<StatusDot status="warn" label="Waiting on schema approval" />
<StatusDot status="danger" label="Failed — connection refused" />
```
