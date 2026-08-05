---
category: Signature
---

**A component of this pack, not an accessibility afterthought.** Every
autonomous motion — the logo rail, the condition marquee, the hero — ships a
visible `PAUSE MOTION` control beside it. A marquee a user cannot stop is not
shippable here, and `prefers-reduced-motion` does not discharge the requirement:
the people who most need to stop the motion are frequently not the people who set
that flag.

Mono uppercase at 11px with the pack's tracking — the one place mono appears at
all, which is what makes it read as an instrument label. `aria-pressed` carries
the state and the label swaps to `Play motion`; the DOM text stays sentence case
so the accessible name reads as a sentence while the furniture rule uppercases
what is drawn.

The control renders statically, so it crosses into this kit even though the
motion it governs does not. Wire `onChange` to whatever the pack's motion layer
is doing — the button is the whole of what the design system owns.

```tsx
<MotionToggle paused={paused} onChange={setPaused} controls="Condition marquee" />
```
