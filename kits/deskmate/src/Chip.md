---
category: Data
---

A small tile rather than a pill label: `--r-chip` (19.6px), `--surface`, a `--rule-w`
hairline at the ink's 5%, 10px of padding. It carries a filename, a tool mark, a count
— something the page is quoting.

`accent` swaps the fill for `--accent-wash` and the label for `--accent-deep`, which is
the eyebrow's pair. `selected` moves the hairline to `--accent` and nothing else moves;
for a status, use the word and the glyph, because status here is never by colour alone.

```tsx
<Chip>Weekly-Performance.pdf</Chip>
<Chip tone="accent" selected>3 discrepancies</Chip>
```
