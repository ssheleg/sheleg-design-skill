---
category: Data
---

A small pill that labels something already true — a city, a panel, a category,
a filter. It is `999px` like every control in this pack, sans 600 at 14px, on
`--surface` inside a hairline.

`tone="accent"` marks the one value that is the subject of the screen, and it
does so with the tint and the border rather than with accent text: terracotta is
4.2:1 on `--surface` and 4.6:1 on the field, so an accent *word* at chip size
fails AA on every ground this pack owns. That is the palette's most common
break. `selected` is the filter state and fills solid, where `--accent-ink` on
`--accent` clears the floor.

```tsx
<Chip>Cardiovascular</Chip>
<Chip tone="accent">Included in membership</Chip>
<Chip selected>Out of range only</Chip>
```
