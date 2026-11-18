---
category: Surfaces
---

The story panel, this pack's card: `--glass-panel` with a 2px `--accent-rim` border,
`--r-panel` (6px), `--offset-panel` (a hard 8px offset in the phosphor at 13%) and
`26px 28px` padding, at most 760px wide (`wide`: 1000px). The title row carries a mono
12px/700 number tag in `--on-accent` on `--accent` at `--r-tag`, then the panel title
in mono 700 `clamp(20px, 2.2vw, 28px)` in `--accent`.

`Cells` lays instrument cells (`--panel`, a 1px `--accent` border, `--r-cell`,
`--offset-cell`) in a four-column grid that steps to two and then one by the panel's
own width: the panel is a container, so a panel in a narrow column stacks on any
screen.

```tsx
<Panel number="03" title="Every department, staffed">
  <Cells items={['Sales', 'Support', 'Finance', 'Ops']} />
</Panel>
```
