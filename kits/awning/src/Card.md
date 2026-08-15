---
category: Surfaces
---

`raised` carries the system's **one** shadow — three layers: a wide ambient, a
close contact, and a `0 0 2px` hairline edge. That third layer is what people
drop when they copy a shadow by eye, and dropping it is why a copied card floats
on white without sitting on it. There is no second shadow and no elevation
scale, so a card that needs to feel heavier needs a different layout, not a
bigger blur.

`flat` sits on `--bg-deep` with no shadow — use it when cards are tiled and the
shadows would otherwise stack into noise.

```tsx
<Card><Heading level={3}>Point of sale</Heading><p>Sell anywhere.</p></Card>
<Card elevation="flat" radius="2xl">…</Card>
```
