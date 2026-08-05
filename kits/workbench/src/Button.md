---
category: Actions
---

The pack allows exactly one accent fill per view, so `primary` is a budget, not
a style: the single action the screen exists to make easy. `secondary` is the
1px-bordered ghost every other action wears, and `ghost` is the bare one for
toolbars and table rows where a border would add a line the eye has to parse.
Hover moves background, border and colour only — nothing translates or bounces,
and focus-visible is a 2px accent outline at 2px offset on every variant.

```tsx
<Button onClick={deploy}>Deploy to production</Button>
<Button variant="secondary" onClick={openDiff}>Review diff</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Dismiss</Button>
```
