---
category: Data
---

A `160px | 1fr | 100px` grid: who spent it, how much of the ceiling that is, and the two
figures. Both figures are `tabular-nums`; the spent one is `--muted` and the ceiling
`--ink` at weight 600, so a column of rows reads as one number changing rather than twelve
numbers competing.

**The fill is `--ink`, not `--good`.** A budget bar is a quantity, not a verdict — the
reference paints every bar white regardless of how close to the limit it is, and the
verdict, when there is one, is a word. Colour here would mean the reader has to decode a
scale before reading a number they can already see.

**The fill animates `transform: scaleX()` from a left origin, never `width`.** The
reference writes `transition: width 1.2s`, which lays out every frame for a second and a
fifth, per bar, with six bars in view. The `fraction` prop drives a transform for exactly
that reason.

The track is 18px at a flat **4px** radius — the one place in this pack that is not a
capsule, because a bar has to read as a measurement with a square end rather than as a
lozenge.

Inside a narrow container the icon and the model line are dropped and the columns close
to `80px | 1fr | 76px`. That is a `@container` rule: a ledger in a 320px panel needs it
whatever the screen is doing.

```tsx
<LedgerRow name="CEO" model="Hermes" spent="$42" budget="$60" fraction={0.7} />
<LedgerRow name="COO" model="Claude" spent="$26" budget="$30" fraction={0.87} note="near limit" />
```
