---
category: Surfaces
---

The one step up from the field: `--surface` inside a 1px `--line` at 12px. The
border is doing the work — cream on cream is a 1.05:1 fill difference and
invisible on its own — so do not reach for a shadow, and do not give a static
card a hover state. `title` is sans 600 (the serif is for sentences and never
appears at card-title size); `meta` is the quiet second line that says when,
how many, or from where.

Cards do not alternate their background to mark a section. The page is one
continuous field, and rhythm plus a change of layout is what separates sections.

```tsx
<Card title="Whole-body MRI" meta="Available in 14 cities">
  <p>A 60-minute scan read by two radiologists, with your results in the app.</p>
</Card>
```
