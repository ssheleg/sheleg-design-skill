---
category: Signature
---

**The pack's signature element.** Four rows descending to the right: each 3% narrower and
3% further right than the one above, each a step darker — `--bg`, two neutrals, then
`--ink` with paper text. Rows overlap by `-1px` so their hairlines share an edge rather
than doubling.

The prop type is a **four-tuple, not an array**, and that is the component enforcing the
pack: this is the one place the value hierarchy is spent, and a fifth rung flattens it.

On entry the rows arrive 110ms apart. Under reduced motion the stagger token goes to zero
and all four are simply present.

```tsx
<Staircase
  steps={[
    { index: '01', text: 'Employees manage AI workers.' },
    { index: '02', text: 'AI workers own defined jobs.' },
    { index: '03', text: 'Roles, budgets + guardrails stay attached.' },
    { index: '04', text: 'Output, cost + memory stay accountable.' },
  ]}
/>
```
