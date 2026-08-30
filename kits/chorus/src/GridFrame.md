---
category: Foundations
---

The construction grid, and it never switches off. Two 1px verticals in `--line` at the
frame edge — `--frame-max` is 1116px against a `--page-max` of 936px, so the frame is
**wider than the content it holds** and the margin between them is never filled.

`crosshairs` draws the small plus centred on each intersection. That mark is what
makes the sheet read as a drawing surface rather than a table, and removing it is the
fastest way to make this pack look like any other warm-paper page.

`surface="slab"` swaps the ink to `--line-on-slab` and continues the same grid across
the dark band, which is what makes a slab read as cut into the sheet rather than laid
on it.

```tsx
<GridFrame><Heading>The intelligence layer</Heading></GridFrame>
```
