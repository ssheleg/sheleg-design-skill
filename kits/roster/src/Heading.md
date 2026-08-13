---
category: Foundations
---

Level 1 is the display and it is set in the **body** face at `--size-display`; level 2
is the section head and it is set in `--font-head`. That inversion is the pack: the
display face only ever appears at 52px, and the body face has to hold a poster.

Level 1 steps at breakpoints — 36px, 60px, 68px — because **neither of the
reference's stylesheets contains a single `clamp()`**, and a fluid ramp here would be
an invented value.

**Use the level for the level.** The reference hides its real `h1` in an `.sr-only`
span and marks all sixteen of its eyebrows as `h2`, so its outline says "eyebrow"
where the page says "section head". This kit keeps the outline and the page in
agreement.

```tsx
<Heading level={1}>Grow organic traffic on autopilot</Heading>
```
