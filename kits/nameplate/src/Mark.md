---
category: Signature
---

The report surface's one repeated object: a `--mark-tile` (50px) square at
`--mark-tile-r`, wearing a **5px solid ring** in `--mark-tile-ring` — not a hairline —
with a 1px `--mark-tile-edge` outside it, a wash background at 9–12% alpha and a glyph
in the matching solid.

**`tone` is variety, not meaning, and that is why it is a number.** The five hues do
not separate from each other — seven of their fifteen pairs are tight, and the
reference's own indigo and violet are 5.58 OKLab units apart at full colour — so no
reader can reliably tell two marks apart and nothing may require it. The icon and the
label carry which feature this is. `tone="neutral"` exists because the reference's
sixth hue was its red, 2.92 units from `--action-to`: a mark in the action's colour
reads as a control, so the coral stays with the action.

The glyph clears the 3:1 non-text floor on its own tile and nothing more. It is never
a word, and the tile is never a button.

```tsx
<Mark tone={1} label="Distribution">{/* icon */}</Mark>
<Mark tone="neutral" label="Reporting">{/* icon */}</Mark>
```
