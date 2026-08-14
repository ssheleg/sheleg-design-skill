---
category: Surfaces
---

A hairline and a fill, and no shadow — the only resting shadow in this pack belongs to a
modal. In dark the fill is `--surface` one step above the field; **in light there is no
step at all**, because the reference sets `--background` and `--card` to the same white
and separates them with a 1px rule. That is not an omission to repair: it is why the
light theme reads as a sheet of paper, and a grey card fill turns the pack into a generic
dashboard in one commit.

Three sibling blocks belong in a [`HairlineGrid`](./HairlineGrid.md), not in three cards.
Use a card when a block has its own title and its own actions.

The title is the display face at `--fs-card-title` / weight 600 / `--track-card-title`;
the meta is mono, muted, and `tabular-nums` so a live count does not reflow the row.

```tsx
<Card title="Backend Eng" meta="$26 / $30">
  Claude · every 8h
</Card>
```
