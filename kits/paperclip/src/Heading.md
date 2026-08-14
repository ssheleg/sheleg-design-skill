---
category: Foundations
---

Inter Tight at weight 600 — the display never leaves semibold — and **the tracking closes
as the size opens**: −0.01em at 16px, −0.03em at the section scale, −0.035em at the hero,
−0.045em on the footer wordmark. That gradient is the pack's typographic signature, and a
60px headline left at the browser default 0em is the single fastest way to lose it.

Level 1 is **not fluid above 768px**: a flat 60px at line-height 0.98, because the
headline's job is to hold a fixed relationship to a fixed-size artwork behind it. Below
768px it becomes `clamp(2.25rem, 11.5vw, 3.75rem)` and wraps freely.

The line ceiling is two lines inside a 900px container — roughly 22 characters a line at
this size and tracking. Three lines means the headline is too long, not that the type is
too big.

```tsx
<Heading level={1}>A team of agents for every person.</Heading>
<Heading>Manage business goals not pull requests.</Heading>
```
