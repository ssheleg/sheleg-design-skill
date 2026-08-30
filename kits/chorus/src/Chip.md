---
category: Actions
---

The eyebrow and the tab: `--surface` at `--r-chip` with a 1px `--line`, 8px/10px
padding and a 14px/500 label in `--ink-body` at 9.15:1.

`accent` does **not** paint the label coral — `--coral` may not be a word. It moves
the label to `--coral-ink` at 4.59:1 on `--bg` and tints the border. Selected adds a
1px `--coral` ring, which is a mark rather than text and is legal at that role.

```tsx
<Chip>AI Search</Chip>
<Chip tone="accent" selected>Ranked</Chip>
```
