---
category: Surfaces
---

Radius 16, and **two kinds that are not interchangeable.** The default is the
container card: `--panel`, a 1px `--border`, and `--shadow-hair` — the measured
hard `1px 2px 0` with no blur at all. `--argument` drops the border and takes
`--shadow-card`, which is 94px of blur at 4px of offset in a violet-tinted
black. That one is for the card carrying the act's argument, not for every card
in a grid.

**A card is for a group.** A list of statements takes a seam and no box; boxing
prose is the fastest way to make this pack look like a template.

**Inside the dark act the shadow is gone**, not softened: `--shadow-card` at 9%
is invisible on the gradient and reads as dirt. The stylesheet already swaps a
card inside `.ps-stage` to `--stage-panel` with no shadow.

```tsx
<Card title="Managed accounts" meta="4 held">
  <AccountRows />
</Card>
<Card className="ps-card--argument" title="Know who holds every account">
  <AccessTable />
</Card>
```
