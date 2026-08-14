---
category: Signature
---

The weighted score bar: one segment per scoring layer, each sized by the points it can
contribute, each carrying its own tone, its name and its raw fraction.

**A layer that does not apply is hatched and reads `N/A`.** It is never drawn as an
empty track, because an empty track reads as zero — a different verdict about the same
product, and the one failure this component exists to prevent.

The fill animates with `transform: scaleX()` from a left origin. Do not animate its
width; the reference does, with `transition-all`, and lays out every frame.

The legend sizes against its **container** and stacks below 380px.

```tsx
<LayerBar
  segments={[
    { label: 'Discovery', score: 2, outOf: 20, tone: 'bad' },
    { label: 'Access', score: 23, outOf: 30, tone: 'good' },
    { label: 'Usability', score: 29, outOf: 40, tone: 'warn' },
    { label: 'Payments', score: null, outOf: 10, tone: 'na' },
  ]}
/>
```
