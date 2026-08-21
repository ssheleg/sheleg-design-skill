---
category: Surfaces
---

The OUTER level: `--r-outer` 16px on `--surface` with a 1px `--hairline-soft`.
Add `bl-card--inner` for the level inside it — 8px on `--surface-2` — and the
difference between the two *is* the layout: a section owns a subject, each inner
card owns one figure of it.

No shadow at either level. Exactly one 6px shadow exists in the whole reference
product, and it is not this.

```tsx
<Card title="Blog content">
  <div className="bl-card bl-card--inner">…</div>
</Card>
```
