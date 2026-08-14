---
category: Surfaces
---

The unit of structure in this pack. A mono index at the top, the title pushed to the
bottom by `margin-top: auto` so a row of cells aligns on its titles regardless of how
much copy each carries, and one sentence in the `32ch` measure beneath.

`invert` is the pack's only hover fill: the whole cell goes solid over `--dur-panel`, and
the index and body text move with it in the same transition. It never lifts and never
gains a shadow — there is no elevation model to lift into.

Below 22rem of **container** width the index moves onto the title's line and the body
sentence drops.

```tsx
<LatticeCell index="04" title="Standing responsibilities">
  A worker owns the job between runs, not just during one.
</LatticeCell>
```
