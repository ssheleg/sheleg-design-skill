---
category: Signature
---

Every photograph in this pack is made of the page's own light: desaturated, then
mapped through three stops, the field (near-black), `--accent` and `--ink-bright`, with
`contrast(1.15)`. The stops are SVG `feFuncR/G/B` table values (0.01, 0, 0.84 / 0.02, 1,
1 / 0.02, 0.4, 0.89), measured off the reference's filter. A custom property cannot feed
an SVG filter, so a token change has to be carried into these numbers by hand.

`round` is a chat avatar (a circle); `tile` is a large portrait at `--r-balloon` with a
2px `--accent` ring and the window glow.

```tsx
<Duotone src="/team/lead.jpg" alt="The team lead" shape="tile" size={240} />
```
