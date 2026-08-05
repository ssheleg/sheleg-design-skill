---
category: Foundations
---

The light serif, and the reason this pack sounds the way it does. Financier
Display ships at **weight 300 only**: `1` is the hero claim (57→80px), `2` every
section heading (48→64px), `3` a category name inside a grid (34→45px). There is
no smaller rung, because the serif is banned below ~27px — if a line is too small
for 300, it is not the serif, it is sans. Level 1 closes up to `--lh-display`
(0.9) and levels 2–3 sit solid at 1.0; the block carries explicit vertical
padding so descenders survive a container with `overflow: hidden`.

A heading is where `ItalicAside` lives: one phrase, italic and terracotta, once.

```tsx
<Heading level={1}>
  Life is short? <ItalicAside>We disagree.</ItalicAside>
</Heading>
<Heading>What your results actually mean</Heading>
```
