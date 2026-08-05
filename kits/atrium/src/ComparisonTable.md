---
category: Signature
---

A wide cream panel of 1px-ruled rows with the "us" column floated above it as a
rounded card filled with `--accent-gradient` and `--shadow-lift`. It reads as a
physical card laid on a printed table, and that reading is the whole motif: the
comparison is not won by colouring a column, it is won by lifting one out.

Mark exactly one column `us`. Rows are `{ id, cells }` keyed on a real id rather
than an array index, and `columns[0]` is the label column. The panel is a grid
rather than a `<table>` because the card is a single element spanning every row
— a column of separately tinted cells does not read as one object — and the row
elements carry the table semantics for assistive technology.

```tsx
<ComparisonTable
  caption="A yearly physical against a Function panel"
  columns={[
    { key: 'what', header: '' },
    { key: 'physical', header: 'Annual physical' },
    { key: 'function', header: 'Function', us: true },
  ]}
  rows={[
    {
      id: 'markers',
      cells: { what: 'Biomarkers measured', physical: '19', function: '128' },
    },
    {
      id: 'review',
      cells: { what: 'Clinician review', physical: 'At the visit', function: 'Every panel' },
    },
  ]}
/>
```
