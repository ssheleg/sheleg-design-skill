---
category: Surfaces
---

`--surface` at `--r-card` with **32px padding and a 32px internal gap, unchanged at
every width** — that constancy is measured, and halving it at 390 makes a different
pack.

The one correction the pack applies to the reference: a 1px `--line` edge. The
reference draws none, and `--surface` is 1.04:1 on `--bg`, which is a value step
rather than an edge.

No shadow. Only four objects in this pack carry one — the bubble, the floating panel,
the hero deck and the nav — and a card is none of them.

```tsx
<Card title="Prompt Tracking" meta="ChatGPT">
  Which prompts trigger your brand in AI answers.
</Card>
```
