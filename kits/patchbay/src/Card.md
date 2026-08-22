---
category: Surfaces
---

**A light, not a fill.** The background is
`radial-gradient(circle at 50% 0, --card-lit, --card-base)` — a teal-black at
the top edge falling to near-black — with a 1px border in the accent at 14% and
no shadow at any state. The card reads as illuminated rather than raised.

Padding is 24px, which is larger than the 14px radius, so **an element flush
against that padding has no concentric radius**: it is a rectangle. Reaching for
`--r-node` there produces two curves that are not concentric.

```tsx
<Card title="Message bus" meta="pub/sub · req/res">
  <p>Every engine event crosses it.</p>
</Card>
```
