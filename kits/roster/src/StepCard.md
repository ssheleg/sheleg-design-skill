---
category: Surfaces
---

Copy on the left, the product on the right, a two-digit number in `--accent-ink`, and
capability chips under the copy.

It sets `container-type: inline-size` and collapses to one column below **640px of its
own width** — derived from what the split needs (two ~280px columns of 16px/28px copy
plus the 32px gap plus 80px of padding), not from a viewport. The same card runs
full-bleed and inside a narrower column on one page, which is exactly the case a
viewport query gets wrong.

```tsx
<StepCard step="01" title="Business Analysis" chips={['Keyword Discovery', 'User Prompts']}
  figure={<img src="/analysis.png" alt="" />}>
  We analyze your business, audience, niche and competitors.
</StepCard>
```
