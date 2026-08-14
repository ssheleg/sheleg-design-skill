---
category: Surfaces
---

The pack's most copied idea, and it is four declarations:

```css
display: grid;
gap: 1px;                     /* the rule's thickness */
background: var(--border);    /* the rule's colour, showing through the gap */
overflow: hidden;             /* the corners cut the cells */
```

The cells fill `--bg`. No cell carries a border of its own, so two adjacent cells cannot
double one, a middle cell needs no `:not(:last-child)` special case, and the container's
`--r-md` clips the corner cells instead of being fought by them. A cell inside this grid
therefore has **no radius**.

**This component sizes against its container, not the viewport.** It takes
`container-type: inline-size` on its root and collapses to one column below 34rem of
*its own* width — a three-across grid dropped into a 320px sidebar on a 1440px screen
would otherwise keep its columns and overflow.

`:focus-visible` on an interactive cell uses `outline-offset: -2px`, drawing the ring
inside the cell: a positive offset would paint over the neighbour, because there is no gap
to spare — the gap is the rule.

```tsx
<HairlineGrid columns={3}>
  <a className="pc-grid__cell" href="#org">…</a>
  <a className="pc-grid__cell" href="#goals">…</a>
  <a className="pc-grid__cell" href="#cost">…</a>
</HairlineGrid>
```
