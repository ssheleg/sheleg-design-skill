---
category: Foundations
---

Weight 400 at every level, in the display face. Level 1 is
`clamp(34px, 5.6vw, 60px)` on a line-height of exactly **1** — 60px on 60px, the
tightest in the library, and the reason a two-line headline reads as one block.

Two lines is the ceiling at desktop. If a headline needs three at 1440px, cut the
headline rather than the size.

One italic word per page is the pack's typographic event: wrap it in `<em>`,
inside the heading, at the same size and the same weight.

```tsx
<Heading level={1}>Meet your AI email assistant that <em>actually</em> works</Heading>
```
