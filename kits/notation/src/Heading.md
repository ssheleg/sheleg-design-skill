---
category: Foundations
---

Three levels and no more: `--t-page` 30, `--t-section` 24, `--t-card` 16. All
three carry `--track-tight`; level 3 is the same size as body and separates by
weight alone, which is what keeps a dense screen from turning into a ladder of
sizes.

The hero's 36px display is **not** in this component. It belongs to the landing
register, is fluid, and is capped at 17ch — a headline that reaches five lines
is a broken hero, not a long one.

```tsx
<Heading level={1}>Managed accounts</Heading>
<Heading>Volume by account</Heading>
```
