---
category: Foundations
---

A pill at `--r-pill`, 13px, weight 500. `neutral` sits on `--panel` inside a
`--border-strong` hairline; `accent` takes `--accent-weak` with `--accent-deep`
as its word.

**Radius 16 on a chip is a mistake, not a variant.** A 28px-tall chip at
`--r-card` is a lozenge — the pack names this one explicitly because it is what
happens when a card token gets reused for a control.

`selected` keeps its state after the pointer leaves; hover does not.

```tsx
<Chip>Client / Acme · 10:42</Chip>
<Chip tone="accent" selected>Needs attention</Chip>
```
