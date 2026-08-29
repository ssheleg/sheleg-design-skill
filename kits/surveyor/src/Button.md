---
category: Actions
---

One height (`--control-h`, 48px: 12×24 padding on 16px/500) at `--r-control`, and a
fill that only ever changes colour — no shadow, no scale, no travel. `primary` rests
on `--action` (the reference's own hover step, promoted for AA: `#ffffff` on
`#0a7269` is 5.79:1) and hovers to `--action-hover`. `secondary` is the measured
outline: transparent on the field with a 1px `--ink` border. `ghost` tints `--mint`
on hover. Disabled keeps the reference's own literal pair.

Focus is the pack's correction: the fill step **and** a 2px `--focus-color` outline.

```tsx
<Button>Start free trial</Button>
<Button variant="secondary">Book a demo</Button>
```
