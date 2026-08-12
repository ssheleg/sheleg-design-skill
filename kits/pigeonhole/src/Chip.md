---
category: Data
---

The generic tag. For a **category**, use `CategoryChip` instead — that one is the
two-layer construction this pack is remembered by, and its label word is required
by its type.

`neutral` is `--surface-2` under `--ink-soft`. `accent` is `--accent-wash` under
`--accent-strong` at 5.04:1 on the field. `selected` adds an `--accent-edge`
border rather than a second fill.

```tsx
<Chip>Open source</Chip>
<Chip tone="accent" selected>Free for 7 days</Chip>
```
