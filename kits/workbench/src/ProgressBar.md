---
category: Signature
---

A 5px bordered track with an accent fill — the pack's answer to a spinner
wherever live state actually exists. Use it when the work has a denominator; if
it does not, say so in words instead of animating a guess. `tone` is a state
claim rather than a palette choice: `ok` for a finished run, `warn` for one
parked on a human, `danger` for one that failed part-way. The fill transitions
on `--dur-state` and stops dead under `prefers-reduced-motion`.

```tsx
<ProgressBar label="Backfill shard 3" value={412} max={1200} />
<ProgressBar label="Nightly rebuild" value={100} tone="ok" />
<ProgressBar label="Export to warehouse" value={38} tone="danger" />
```
