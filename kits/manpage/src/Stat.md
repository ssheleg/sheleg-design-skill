---
category: Data
---

A figure with its label above and its provenance below, all in mono. The
reference sets two of these beside sparklines — `423,207 posts this week` — and
the `source` slot is where the window belongs, so the number is never a bare
claim.

The figure sets in `--ink` at `--t-title`, tabular. Note what it does **not** do:
it never counts up. An animated counter on this pack contradicts the register —
a document states a number, it does not perform it.

```tsx
<Stat value="423,207" label="Posts" source="this week" />
```
