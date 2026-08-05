---
category: Signature
---

**This renders a claim, not a label.** A slide's headline is a full sentence
asserting something — "Financial access is already global; the gap is guidance" —
and never a noun like "Market". That is the whole component: the claim is the
argument, and the diagram beneath it is the evidence for that claim. A deck whose
titles are nouns has no argument, only chapters, and the audience has to assemble
the case themselves while the presenter talks.

`slide` (the default) is 64px at weight 500; `cover` is the 128px display face for
slide one. Both balance their wrap and cap their measure, because at these sizes a
one-word orphan is a visible defect. If the claim will not fit at 64px, cut the
claim — do not shrink the ramp.

```tsx
<ClaimTitle>Financial access is already global; the gap is guidance.</ClaimTitle>
<ClaimTitle size="cover">We are building the guidance layer for banked adults.</ClaimTitle>
```
