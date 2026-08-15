---
category: Signature
---

Status is never by colour alone in this pack, and this component is where that
rule is enforced rather than remembered: the dot always ships either a visible
label or an `aria-label`, and the label renders in `--ink` while the colour stays
on the dot. Four of the five semantic colours sit under 4.5:1 on the light field
and two under 3:1 — the word is the message, the colour is the reinforcement.

`running` is the only state allowed to pulse, at 1.4s, and it stops when the run
does and under reduced motion.

```tsx
<StatusDot status="running" label="Querying Snowflake" />
<StatusDot status="danger" label="Failed" />
```
