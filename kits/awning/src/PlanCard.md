---
category: Signature
---

The commerce front door's load-bearing section. **A featured plan is featured by
fill, not by hue** — it inverts to `--ink` with `--bg` content, exactly as the
primary button does, because there is no accent colour to tint it with. At most
one per row; two featured plans is a row with no recommendation in it.

The price takes the `t1` step and the cadence the `b4`, so the number carries
and the interval does not compete with it.

```tsx
<PlanCard
  name="Basic" price="$29" cadence="per month"
  features={['2 staff accounts', '10 locations']}
  action={<Button size="sm">Start free trial</Button>}
/>
```
