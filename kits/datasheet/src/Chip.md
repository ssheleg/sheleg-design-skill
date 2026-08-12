---
category: Data
---

The small static label: 11px in the data face at `--r-chip`, 1px `--rule`,
padding of 2 by 8. Chips name things that are already true — a region, a plan, a
version — and never stand in for a button. `tone="accent"` is for the one value
that is the screen's subject; `selected` fills with `--accent-wash` behind an
accent edge, which is how the reference marks its active summary cell. A chip
carrying a verdict is a `ValueChip`; a chip carrying an action is a `Button`.

```tsx
<Chip>eu-central-1</Chip>
<Chip tone="accent">v3</Chip>
<Chip selected>Suspect only</Chip>
```
