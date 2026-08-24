---
category: Signature
---

The `--tile` (80px) square at `--r-tile` (20px) that opens a hero or a section: a
white fill, `--shadow-tile`, holding a 68px glyph at `--r-tile-inner` with
`--shadow-tile-inner`.

It is one of only two objects in the pack allowed an ordinary shadow — the other is
the tile's own inner image — and it is **never interactive**. In the reference it
sits above the headline and tells a reader which service page they are on before they
read a word.

```tsx
<Tile label="Web design">{/* glyph */}</Tile>
```
