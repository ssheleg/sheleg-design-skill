---
category: Signature
---

One of the pack's recurring bespoke diagrams: a comparison with **exactly one
column marked as *us***. That column is the only place the accent appears in the
table, which is what makes the argument readable from the back of the room in
one second. Only the first column flagged `us` is honoured, so a second flag
cannot quietly produce two accent columns and no comparison at all.

Rows are `{ id, cells }` keyed on a real id, never an array index, and cells take
nodes — a `Chip` or a `SourcedNumber` drops straight in. Nothing hovers: this is
a slide, and a row that highlights under a cursor is noise during a presentation.
Keep it to four or five rows; a comparison that needs ten is two slides.

```tsx
<ComparisonTable
  caption="Against the incumbents"
  columns={[
    { key: 'criterion', header: 'Criterion' },
    { key: 'banks', header: 'Retail banks' },
    { key: 'robo', header: 'Robo-advisors' },
    { key: 'us', header: 'Meridian', us: true },
  ]}
  rows={[
    {
      id: 'advice',
      cells: {
        criterion: 'Regulated advice',
        banks: 'Branch only',
        robo: 'Guidance only',
        us: 'In-app, regulated',
      },
    },
    {
      id: 'cac',
      cells: {
        criterion: 'Blended CAC',
        banks: '£310',
        robo: '£95',
        us: <Chip tone="accent">£31</Chip>,
      },
    },
  ]}
/>
```
