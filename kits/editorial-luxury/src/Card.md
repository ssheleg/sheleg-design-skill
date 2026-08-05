---
category: Surfaces
---

The raised surface of whichever field it sits on: `--paper-2` on cream,
`--espresso-2` on espresso, a 22px squircle, one hairline border, a double
bezel and a soft ambient shadow. On hover it lifts 2px and its border warms
toward terracotta. The title row carries its metadata on the right in mono — a
date, an issue number, a byline — because that is where a printed page puts it.

**Never nest a card in a card.** The pack says so, and the stylesheet enforces
it: a `Card` or `DossierCard` inside another one loses its padding, border,
radius and shadow and reads as plain content. If a card seems to need a card
inside it, it needed a `Rule` or a `DataTable`.

```tsx
<Card title="Signal density" meta="Issue 14 · March">
  <p>
    Sage marks every synthesized claim; raw excerpts stay unmarked so a reader
    can always tell what the pipeline wrote from what it merely found.
  </p>
</Card>
```
