---
category: Surfaces
---

This pack ships **two** border weights, which is unusual in this library.
`--line` goes between rows; `--line-strong` goes around a control. The
difference is load-bearing: it is what makes an outlined secondary button read
as a control at all, given its fill is transparent in every state.

```tsx
<Rule />
<Rule tone="strong" />
```
