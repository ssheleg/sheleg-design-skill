---
category: Actions
---

The pack's signature and its whole idea: a near-black pill at `--r-glow` (100px)
wearing `--glow-rig` — sixteen shadow layers, six lit and ten held at alpha 0, thrown
from below and to the left. `surface="light"` swaps to `--glow-rig-light`, where the
rim goes black and the inset goes white.

**One per viewport.** Two lit controls and the light stops meaning *this one*.

**The rig does not change on hover.** It is a static light; the fill moves one step
and the rig stays. Pulsing, rotating or growing it is the pack's first ban, and it is
the fastest way to turn this pack into a novelty. Disabled drops the rig entirely.

The label is the monospace at 18px/500 uppercase with `letter-spacing: normal` — the
openness is the face's own width, not tracking.

```tsx
<LitButton>Book a call</LitButton>
<LitButton surface="light">Request a quote</LitButton>
```
