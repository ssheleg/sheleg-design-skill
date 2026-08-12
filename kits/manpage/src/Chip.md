---
category: Data
---

The generic tag. For the section-heading chip that carries this pack's identity,
use `LabelChip` instead — it wraps a real `<h2>` and this one does not.

`neutral` is `--surface-2` under `--ink-soft`. `accent` is `--accent-wash` under
`--accent-ink`, never under `--accent`: coral on its own wash is 3.24:1.
`selected` adds a `--accent-edge` border.

```tsx
<Chip>CASE STUDY</Chip>
<Chip tone="accent" selected>Free credits</Chip>
```
