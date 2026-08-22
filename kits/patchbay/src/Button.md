---
category: Actions
---

Three variants and none of them is a fill. `primary` is a 135° accent-to-blue
wash behind a **1.5px `--accent-rim`** border — 3.10:1, which clears the
boundary floor by 0.10 — with the label in `--ink`. Do not thin that border and
do not drop its alpha: it is the only edge the control has.

Disabled is a named pair (`--ink-soft` on `--wash`, 4.60:1), never an
`opacity` multiplier, because a multiplier composites against whatever sits
behind and the ratio then cannot be computed.

```tsx
<Button variant="primary">Explore docs</Button>
<Button>Join the channel</Button>
```
