---
category: Data
---

One row of a schedule: a `130px | 1fr` grid, a 2px track line, and ticks that are
**capsules, not circles** — 10 × 20 at rest with a 2px border, 12 × 22 filled `--good`
with an 8px glow when running. That shape is the pack: a circle is a point, a capsule is a
paperclip's end, and everything from the hero artwork down repeats it.

**A sleeping lane dims its label to 45%; a waking one returns it to full and turns the
name `--good`.** Both states are also written — the cadence line says `every 8h` in mono,
and the active tick carries `activeLabel` in a tinted chip above it. Status is never by
colour alone here, and a lane that only changes opacity has no state a screen reader can
reach.

Lanes reveal on `calc(var(--lane) * var(--stagger) + var(--stagger))` — the same 140ms
constant as the org tree.

Inside a narrow container the label column closes to 86px and the cadence line is dropped;
that is a `@container` rule, not a viewport one.

```tsx
<ScheduleLane name="Copywriter" cadence="every 4h" marks={[0, 0.17, 0.33, 0.5, 0.67, 0.83, 1]} />
<ScheduleLane
  name="SEO Analyst"
  cadence="every 8h"
  marks={[0, 0.33, 0.67, 1]}
  activeIndex={0}
  activeLabel="Crawl audit"
/>
```
