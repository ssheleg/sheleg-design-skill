---
category: Foundations
---

The type ramp made visible: 1 is the hero at `--t-hero` 84 / weight 700 /
line-height 1.1, 2 the section at `--t-page` 48 / 1.2, 3 the card title at
`--t-card` 20 / weight 600 / 1.4.

**Tracking is zero at every level.** The reference sets `letter-spacing` seven
times in 58 stylesheets and never on a heading, so a negative track here is the
fastest way to stop the pack looking like itself. Level 1 clamps fluidly and the
clamp is monotonic — the reference's own ramp is not, and that is a correction
rather than a copy.

```tsx
<Heading level={1}>Post once. Show up everywhere</Heading>
```
