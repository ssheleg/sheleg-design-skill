---
category: Surfaces
---

The bounded surface inside a slab: oat on a `--line` hairline at the default
`12px` radius, `36px` padding, and `--shadow-card` — which is 2% black and
should stay that way, because elevation in this pack is light rather than
shadow. `meta` is the quiet line beside the title in `--ink-soft`: a dose, a
cadence, a sample size. The title is set in the display face at `20px`, below
the pack's `28px` tracking floor, so it takes normal tracking.

A card is also the honest way to put small copy on a sage slab — put the card
inside the slab rather than shrinking text onto the sage.

```tsx
<Card title="Daily blend" meta="30 servings · one scoop">
  <p>Built from your panel, remixed each time you retest.</p>
</Card>
```
