---
category: Surfaces
---

One flat pastel per act, full-bleed, used to **change subject** rather than to
decorate. The ink clears AA on every band — 5.76:1 on the lilac, 6.53 on the
sky, 8.36 on the peach — which is why the bands can be saturated without a
second text colour.

`ink` switches the whole band to the dark register by setting
`data-surface="ink"`, where the outline and the offset both invert to white. A
gradient in a band is banned: the reference paints them flat, and a gradient
reads as a different product.

```tsx
<Band tone="sky"><Heading level={2}>One inbox for every client</Heading></Band>
```
