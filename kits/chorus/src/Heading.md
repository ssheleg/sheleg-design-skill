---
category: Foundations
---

Level 1 is the **display face** — Outfit at 56px/1.1/600 with −0.0625em, dropping to
40px with −0.025em from 768 down. The tracking *relaxes* as it shrinks, which is
measured at both widths and is the opposite of the usual move.

Levels 2 and 3 are Inter: 44px/1.2/600 at −0.032em, and 18px/1.7/600.

Outfit does exactly two jobs in this pack — this heading and the question inside a
`Bubble`. Setting body or UI in it loses the pack.

```tsx
<Heading level={1}>Make them mention your brand</Heading>
```
