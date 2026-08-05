---
category: Signature
---

One dim sentence and one action — no illustration, no mascot, no framed box.
The sentence has to earn its place: say what is absent and why, because "No
data" tells an operator nothing they did not already see. The action is
optional and singular; where there is genuinely nothing to do, ship the
sentence alone rather than inventing a button.

```tsx
<EmptyState
  message="No runs in the last 24 hours. The scheduler was paused on 3 Aug."
  actionLabel="Resume scheduler"
  onAction={resumeScheduler}
/>
```
