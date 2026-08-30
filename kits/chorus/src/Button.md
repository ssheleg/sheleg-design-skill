---
category: Actions
---

36px tall at `--r-control`, 8px/16px padding on a 14px/500 label, and a fill that
only ever changes colour — nothing lifts, scales or travels.

`primary` is the reference's own coral with the pack's correction: `--coral` fill and
an `--on-coral` label at 6.20:1. **A white label here measures 2.84:1 and is banned at
every size** — that is the whole reason this variant exists in this shape. `secondary`
is `--ink-strong` with `--on-slab`. `ghost` is `--surface` with a 1px `--line`.

Hover steps the fill one value; active repeats hover. Focus paints a 2px
`--focus-color` ring **and** keeps the fill step. On a slab the ring resolves to
`--focus-color-on-dark`, because the ink ring is 1.00:1 there.

The 36px height is measured and misses the 44px tap floor: the hit area is padded to
`--tap-min` on touch rather than the button being resized.

```tsx
<Button>Start free trial</Button>
<Button variant="secondary">Book a demo</Button>
```
