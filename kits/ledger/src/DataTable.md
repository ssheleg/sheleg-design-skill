---
category: Signature
---

32px rows, a `--muted` header over a hairline, hairline dividers, numeric columns
right-aligned in the data face with tabular figures, and a monospace row number
in the first column — the measurements are the reference's, including the row
height.

Two traps this component is shaped around. Row hover is `--row-hover`, which in
light mode is one step from the page field, so a dense table **must** sit on
`--panel-2` or the hover is invisible. And the row number is the first thing to
drop below 40rem: it is a motif, not information.

```tsx
<DataTable
  caption="Top accounts"
  columns={[
    { key: 'account', header: 'Account' },
    { key: 'plan', header: 'Plan' },
    { key: 'mrr', header: 'MRR', numeric: true },
  ]}
  rows={rows}
/>
```
