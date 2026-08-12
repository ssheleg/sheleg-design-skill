---
category: Foundations
---

The uppercase mono micro-label, 8–11px at 0.09em in `--ink-muted`. It states a
condition about the *data* rather than about the product: *this is real data*,
*this is a demo, production accuracy will be higher*, *measuring*.

The reference sets it in `--gray-6`, which measures 2.51:1 on the field — below
even the 3:1 non-text floor, at the smallest size on the page. This pack refuses
that ink: a badge meant to be read takes `--ink-muted` at 5.06:1. Copying the 8px
size without the ink step is the trap.

```tsx
<MonoBadge>This is real data</MonoBadge>
```
