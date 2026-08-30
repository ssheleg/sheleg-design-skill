---
category: Signature
---

**The pack's signature element, and the one component that may not be restyled.**

`--r-bubble` is 24px on three corners and **0 on the top right** — a speech-bubble
tail drawn by subtraction, measured on all 24 instances of this object in the
reference. The question is 24px/600 in `--font-display` at 18.88:1 on `--surface`;
`--shadow-bubble` is its own three-stop shadow and belongs to nothing else.

`surface="slab"` is the same object on the dark side of a pair, `--on-slab` at
16.54:1. `mirrored` swaps the cut to the top left for the answering side and for RTL
— the reference ships only one direction, so the mirror is the pack's decision and is
labelled as one.

Change its corner, its face or its shadow and the pack is gone. If the page has no
stranger's words to put in it, the page does not want this pack.

```tsx
<Bubble question="Best CRM for B2B companies?" source="r/sales · 18 Mar" />
<Bubble question="Have you tried it?" surface="slab" mirrored />
```
