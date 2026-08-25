---
category: Surfaces
---

The page's only texture: a `radial-gradient` dot of `--grid-color` at `--grid-dot`
(0.8px) repeated every `--grid-step` (24px).

It is a **field**. It belongs under a section, and it is never a border and never
inside a panel. The step does not rescale at narrow widths — a field that rescales
stops reading as paper.

```tsx
<Grid><section>…</section></Grid>
```
