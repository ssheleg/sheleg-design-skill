---
category: Foundations
---

The rounded geometric display face at Medium, flat `1.2` leading at every size,
tracked `-0.023em`. The roundness *is* the friendliness — a grotesque here turns
the page corporate and a serif turns it into a different pack. The ramp is `1`
= section heading (44px), `2` = slab heading (32px), `3` = sub-claim (28px), and
it stops at 28 because that is the pack's tracking floor: below it, type is body
copy in the body face, not a smaller heading.

The heading takes `color: inherit` rather than `--ink`, so a heading dropped
into a cacao `Slab` becomes `--on-ink` without the caller thinking about it.

```tsx
<Heading level={1}>Nutrition that answers to your own data</Heading>
<Heading level={2}>What the panel actually measures</Heading>
```
