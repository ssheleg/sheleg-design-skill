---
category: Foundations
---

1px dots in `--line-grid` at `--grid-step` 32px, halving to 16px below 768px so
the density stays visually constant as the viewport narrows.

Depth layer 1: `pointer-events: none`, `aria-hidden`, never on a scroller, and
**never animated**. The grid is the sheet. A sheet that drifts, parallaxes or
fades in turns a drawing into a screensaver.

```tsx
<GridField />
```
