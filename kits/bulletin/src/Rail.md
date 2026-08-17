---
category: Signature
---

The row of outlined circles that says *many*. Each mark is a 60px chip at
`--r-pill` with a 1px `--line` and `--shadow-2-wide`; the rail of them is how
this pack states breadth without a paragraph.

It belongs in the first viewport. Putting it below the fold is the most common
way to build this hero wrong — the rail *is* the argument, and the headline only
introduces it. The circles carry no text, so `name` is what assistive tech
reads and what the visible caption renders.

```tsx
<Rail items={[{ mark: 'in', name: 'LinkedIn' }, { mark: 'ig', name: 'Instagram' }]} />
```
