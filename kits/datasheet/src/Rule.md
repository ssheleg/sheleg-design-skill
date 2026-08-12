---
category: Foundations
---

The divider, and in this pack it is structural rather than decorative: a 1px
`--rule` hairline is what walls every cell of the instrument. `tone="strong"`
takes `--rule-strong` for the one heavier edge a layout is allowed. Adjacent
full-bleed bands on the reference carry a -1px margin so two touching hairlines
collapse into one, which is worth copying wherever bands meet.

```tsx
<Rule />
<Rule tone="strong" />
```
