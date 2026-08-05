---
category: Signature
---

The pack's table, set like a printed one: a mono caption, a tracked uppercase
header over a strong hairline, hairline row dividers, and numeric columns
right-aligned in the data face with tabular figures so digits line up down the
column. Mark a column `numeric` whenever it holds a quantity — that flag is the
whole reason the table reads at a glance. Rows key on a real `id`, never an
array index, and cells take nodes, so a `Chip` or a `Stamp` drops straight in.
Nothing hovers: a dossier table does not light up under a cursor.

```tsx
<DataTable
  caption="Pricing, as published"
  columns={[
    { key: 'vendor', header: 'Vendor' },
    { key: 'tier', header: 'Tier' },
    { key: 'seat', header: 'Per seat', numeric: true },
  ]}
  rows={[
    {
      id: 'northbeam-team',
      cells: { vendor: 'Northbeam', tier: <Chip>Team</Chip>, seat: '$49' },
    },
    {
      id: 'northbeam-ent',
      cells: {
        vendor: 'Northbeam',
        tier: <Chip tone="accent">Enterprise</Chip>,
        seat: '$180',
      },
    },
  ]}
/>
```
