---
category: Signature
---

The stat row at display scale: two to four figures in **sans 600** at 48→64px,
each with a light sublabel beneath and the source it carries. Sans, not serif,
not mono — the numbers are claims, and the serif is reserved for sentences.

`source` is required, unlike the spine's `Stat`. On a health page an unsourced
number is a liability, and the source line is also what keeps the section from
looking like marketing.

Lay them out in a plain flex row: the 1px `--line` divider between neighbours is
drawn by the stylesheet, because that hairline is the only separator this row
gets and it should not depend on a wrapper anyone can forget.

```tsx
<div style={{ display: 'flex' }}>
  <SourcedFigure value="128" label="Biomarkers" source="Function panel, 2026" />
  <SourcedFigure value="5 days" label="Median time to results" source="2026 member data" />
  <SourcedFigure value="1 in 4" label="Found an actionable finding" source="NEJM, 2024" />
</div>
```
