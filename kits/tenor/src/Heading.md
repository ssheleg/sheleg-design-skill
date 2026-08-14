---
category: Foundations
---

Instrument Sans at **weight 400 and only 400**, tracked negative, at a line-height below
one. Level 1 takes the hero slope `clamp(2.55rem, 4.6vw, 4.65rem)` at `0.91`; level 2 the
section slope `clamp(3rem, 6.5vw, 6.6rem)` at `0.93`; level 3 the card slope.

**The measure is the component.** `max-width` is set in `ch` — 12 at level 1, 9.5 at
level 2, 11 at level 3 — which is what turns every heading into a three- or four-line
stack. Do not widen it to fit a long headline; shorten the headline.

For the hero's two-tone sentence use `SplitHeadline`.

```tsx
<Heading level={2}>From role to results in three steps.</Heading>
```
