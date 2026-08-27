---
category: Data
---

The metric tile: label at `--t-label` in `--ink-mute` above a figure at `--t-metric`
(26.4px, the dashboard's own size) in `--weight-strong`. Compose with `Delta` in the
source slot for the vital-signs row.

Wrap tiles in `td-stat-row` + `td-stat-row__grid`: the row is a container
(`container-type: inline-size`) and steps 2 → 4 → 7 columns by its own width, because
the same row lives inside the demo frame and on a bare page.

```tsx
<div className="td-stat-row"><div className="td-stat-row__grid">
  <Stat value="5,292" label="Visitors" />
  <Stat value="$4,342" label="Revenue" />
</div></div>
```
