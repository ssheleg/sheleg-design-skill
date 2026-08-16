---
category: Actions
---

Height 36, radius 6, weight 500, label at 14 — the reference's own control, and
every variant wears the same radius. `primary` fills with the accent and states
its label colour on the rule rather than inheriting it, because an anchor reset
that says `color: inherit` will otherwise win the label and paint ink on accent.
`secondary` is the 1px `--edge` bordered one; `ghost` carries no border at all
and belongs in toolbars and table rows, where a border adds a line the eye has
to parse.

Hover moves background, border and colour. **Nothing translates and nothing
scales** — the reference presses nothing, and a button that pops on click has
left this pack.

```tsx
<Button onClick={connect}>Connect account</Button>
<Button variant="secondary" onClick={exportAll}>Export</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Dismiss</Button>
```
