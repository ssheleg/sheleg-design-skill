---
category: Signature
---

**The signature element.** Eight columns on a 70px pitch, twelve 70 × 170 capsules each
at `rx: 35`, stepped 34.5px apart so every capsule covers all but a 34.5px band of the one
above it — a stack of overlapping paperclip ends falling from the top of the page.

The fills are **generated, not chosen**. The top stop rotates forward around the hue wheel
by ~12.4° per capsule and the bottom stop rotates backward by ~10.3°, at near-constant
saturation and lightness, so the two stops stay near-complementary and the column inverts
its own gradient between its first capsule and its last. The reference ships 45 gradients
and 89 distinct stops from that one rule.

Over all of it, the pack's single noise recipe — `fractalNoise`, `baseFrequency 2.95`,
5 octaves, seed 9 — masked by the capsules themselves and composited `overlay`. Without
it a twelve-gradient artwork bands on any 8-bit panel.

**It is decoration and it must stay decoration.** `aria-hidden`, no pointer events, no
information. The composition only works when the copy sits *on top of it*: the reference
pushes the artwork up by `translateY(-310px)` so only its lower half is in frame and gives
the headline `margin-top: 124px` to land in the curtain's lower third. A hero that puts
the art beside the copy is a different pack.

Entrance and parallax belong to the page, not to this component — 1.1s rise on
`--ease-hero`, then a native `animation-timeline: view-timeline` inside `@supports`.

```tsx
<div className="pc-hero__art" aria-hidden>
  <CapsuleCurtain />
</div>
```
