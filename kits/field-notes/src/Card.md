---
category: Surfaces
---

A lighter sheet on the paper: `--surface` fill, `--ring-hairline`, `--radius-lg`.
The ring is the elevation — a grey drop shadow anywhere in this pack reads as a
foreign part, and the one deep shadow the token layer ships is warm and exists
for genuinely floating things. `meta` is mono, because in this pack mono is
furniture (a commit, a date, a version) and not data.

**It has no hover state. At all.** The pack says why in as many words: *a page
built from hairlines has nothing to lift off*. So there is no shadow on hover, no
border darkening, no fill change and no translate — and the stylesheet carries a
comment saying so, because "the card doesn't respond to the mouse" reads like an
oversight to anyone who has not read the pack. If the card is clickable, the
control is the thing inside it.

When you nest, subtract: an inner block at `--radius-md` inside this card's
`--radius-lg` reads as concentric, while the same radius on both reads as two
rectangles that happen to touch.

```tsx
<Card title="graph/resolver.ts" meta="4f2a91c · 2026-08-04">
  <SourcedClaim source="static pass · 1 204 refs" provenance="extracted">
    Every call site resolves to a definition in this repo.
  </SourcedClaim>
</Card>
```
