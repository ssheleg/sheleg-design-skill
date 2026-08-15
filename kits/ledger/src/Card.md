---
category: Surfaces
---

A rectangle drawn at 12% ink, radius 15, with **no shadow**. That is the whole
elevation model: 103 of the reference's surfaces are exactly this, and the depth
you feel comes from the fill step (`--bg` → `--panel` → `--panel-2`) rather than
from anything lifting off the page. Hover on an interactive card moves the
border to `--border-strong` and changes nothing else.

`meta` takes a plain string. A card that states a **number** takes a `Seal`
instead: place it as the card's first child and the stylesheet lifts it into the
title row, because the seal belongs beside the figure it qualifies rather than
under it.

```tsx
<Card title="MRR · All plans" meta="12 months">
  <Seal state="verified" href="/metrics/mrr" />
  <Stat value="$4.40M" label="MRR" source="governed metric · Stripe" />
</Card>
```
