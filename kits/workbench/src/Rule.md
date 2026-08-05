---
category: Foundations
---

A 1px divider, because elevation in this pack is a border rather than a shadow.
`hairline` is the default `--border` and separates rows or blocks inside one
surface; `strong` steps up to `--border-strong` where two regions of a screen
genuinely part company. If a rule is doing decorative work rather than
separating things, delete it — spacing was the answer.

```tsx
<Card title="Deploy 4f2a91c">
  <p>Rolled out to 3 of 8 regions.</p>
  <Rule />
  <p>Started 14:02 UTC by nadia@.</p>
</Card>
```
