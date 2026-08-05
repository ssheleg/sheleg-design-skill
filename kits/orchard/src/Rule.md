---
category: Foundations
---

A 1px divider in `--line`, the pack's one hairline colour. `strong` steps to
`--ink-soft` rather than inventing a second line token — the palette is three
colours and a fourth would mean one of them stopped meaning something.

Reach for it rarely. This pack separates things with the field between slabs and
with `44px` of space inside them; a rule that is doing decorative work is a gap
that was measured wrong.

```tsx
<Card title="What is in the blend">
  <p>Twelve actives, dosed from your panel.</p>
  <Rule />
  <p>Reformulated free every time you retest.</p>
</Card>
```
