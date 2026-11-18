---
category: Signature
---

The schematic connector between two story panels: one path at a 3px stroke in
`--accent`, round caps and joins, a soft phosphor drop-shadow, and a mono 13px/600 label
in `--accent` naming what it carries. It draws itself once with a dash offset over
`--dur-draw` (1s) when it enters; under reduced motion it renders fully drawn.

One stroke, never a double line, never an arrowhead filled in a second colour.

```tsx
<Connector carries="the plan, with an owner per task" />
```
