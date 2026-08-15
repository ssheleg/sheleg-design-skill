---
category: Data
---

The kicker, boxed: 10px monospace, uppercase, `+0.1em`, a transparent fill and a
1px border of its own colour at 30% alpha, on `--r-control`. It is the same atom
the provenance tag in `AI_PRODUCT_PATTERNS.md` §4 describes, which is why the
`Seal` is built on it rather than beside it.

`tone="accent"` is for something the system is saying about itself — a scope, a
model, a mode. Neutral is for everything the data says. There is no third tone,
because a third tone is a second accent.

```tsx
<Chip>snowflake · prod</Chip>
<Chip tone="accent">gpt-5 · 2.4s</Chip>
<Chip selected>last 12 months</Chip>
```
