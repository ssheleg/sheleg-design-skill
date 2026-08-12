---
category: Signature
---

The pack's table, built once: 34px rows, a sticky `--panel-2` header in tracked
uppercase, hairline row dividers, and numeric columns right-aligned in the data
face with tabular figures so digits line up down the column. Mark a column
`numeric` whenever it holds a quantity — that flag is the whole reason the table
reads at a glance. Cells take nodes, so a `StatusDot` or a `Chip` drops straight
in. Rows hover to `--panel-2` and a selected row takes `--accent-weak` with a 2px accent inset, as the pack mandates; nothing else moves.

```tsx
<DataTable
  caption="Last 5 runs"
  columns={[
    { key: 'run', header: 'Run' },
    { key: 'state', header: 'State' },
    { key: 'rows', header: 'Rows', numeric: true },
  ]}
  rows={[
    {
      id: '8842',
      cells: {
        run: '8842',
        state: <StatusDot status="running" label="Backfilling" />,
        rows: '1 204 883',
      },
    },
  ]}
/>
```
