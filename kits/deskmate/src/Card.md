---
category: Surfaces
---

`--surface` on `--bg` at `--r-card`, no border and no shadow: the field step **is** the
elevation, and the page has two shadows in total, both spent elsewhere.

Padding is 24px above the title and 32px around the body, which is the reference's own
asymmetry — the title row sits closer to the top edge than the body does to the sides.
For the two-half card the page is actually made of, see `QuotedCard`.

```tsx
<Card title="Payroll prep" meta="10:20 AM">
  <p>Attendance and collections reconciled.</p>
</Card>
```
