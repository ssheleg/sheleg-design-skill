---
category: Data
---

The mono atom: 11px in the data face, 1px border, pill radius, 2×8 padding.
Chips label things that are already true — an environment, a shard, a tag, a
count — and they never stand in for a button. `tone="accent"` is for the one
value that is the screen's subject; `selected` is the filter-chip state and
fills with `--accent-weak` behind an accent border. A chip that needs an action
is a `Button`, and a chip that needs a state is a `StatusDot`.

```tsx
<Chip>us-east-1</Chip>
<Chip tone="accent">v2.14.0</Chip>
<Chip selected>Failed only</Chip>
```
