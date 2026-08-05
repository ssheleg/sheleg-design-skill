---
category: Data
---

`--surface` on a hairline at `--radius-sm`, 6×14, 14px/400, in `--ink-soft`.
Hover fills to `--surface-2`; `selected` is the rust wash behind a rust border in
`--brand-ink`, and **exactly one chip in a rail is selected at a time** — a rail
with two is a set of toggles wearing chip clothes. `tone="accent"` is the same
rust wash without the border promotion: it marks subject matter, where `selected`
marks state, so the two stay legible side by side.

A chip is not a provenance tag. If the label says how something is known —
extracted, inferred, ambiguous — it is a `ProvenanceTag` and it belongs inline
with the claim, not in a filter rail.

```tsx
<Chip selected>TypeScript</Chip>
<Chip>Python</Chip>
<Chip tone="accent">v2.14.0</Chip>
```
