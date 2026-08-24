---
category: Surfaces
---

A card is `--surface` at `--r-md`, and it is drawn two ways on purpose: **no border
and no shadow** when it stands on `--field`, a 1px `--line-soft` when it stands on
white. Its separation comes from the field it is on, which is why the same component
changes clothes.

It never wears `--shadow-frame`. That shadow belongs to `Frame`, once per screen.

```tsx
<Card title="Guaranteed placement" meta="48h">…</Card>
```
