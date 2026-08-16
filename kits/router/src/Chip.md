---
category: Foundations
---

A pill at `--r-pill`, 12px, weight 500. `neutral` sits on `--panel-2`;
`accent` takes the accent at 7.8% with the accent as its word — the reference's
own tint alpha, and the same pair its selected sidebar item wears.

`selected` adds a 2px rail on the leading edge. **Selected is not hover:** a
selected chip keeps its tint and rail after the pointer leaves, and a hovered
one does not.

```tsx
<Chip>30d</Chip>
<Chip tone="accent" selected>Overview</Chip>
```
