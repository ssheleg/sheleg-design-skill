---
category: Foundations
---

The structural ramp on a fixed canvas, so the sizes are fixed too: `1` is the
section-divider slide (96px), `2` a slide label (64px), `3` a subhead inside a
diagram (36px). Every level balances its wrap, because at these sizes a one-word
orphan is a visible defect rather than a nuance. There is no level 4 and no
smaller step: if the content will not fit, the pack's answer is a second slide,
never a shrunken ramp — that is one of its bans. **A slide's headline is a
`ClaimTitle`, not a `Heading`** — a heading names a thing, a claim asserts one,
and this deck argues.

```tsx
<Heading level={1}>03 — Distribution</Heading>
<Heading level={3}>How the money moves</Heading>
```
