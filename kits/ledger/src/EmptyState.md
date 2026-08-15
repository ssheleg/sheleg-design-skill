---
category: Signature
---

The blank input is where a person decides what this product is, so the empty
state states what the model can answer **here, in this scope**, and offers two or
three real questions as accent kickers that run when clicked. "Ask me anything"
is banned: it is both false and useless.

Derived rather than measured — the reference ships no empty state — and taken
from `AI_PRODUCT_PATTERNS.md` §6.

```tsx
<EmptyState
  message="This workspace can answer questions about Stripe revenue and product events."
  examples={['MRR by plan, last 12 months', 'Signups by channel since March']}
  onExample={ask}
/>
```
