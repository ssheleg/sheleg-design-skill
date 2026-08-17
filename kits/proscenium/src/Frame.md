---
category: Signature
---

**The proscenium arch** — a translucent fill, a 1px `--frame-edge` hairline and
an inset white glow around a product view. Measured off the reference's hero
container, `--shadow-frame` and `--frame-fill` together.

`cropped` is the part that carries the pack. The panel is meant to be **cut off
by the fold**: it drops its bottom padding, its bottom border and its bottom
radii so the product runs off the viewport rather than sitting complete inside
it. A page in this pack is remembered as the one where the product was already
there, and a frame that closes politely above the fold is the version nobody
remembers.

`foot` is the honesty line: a frame that shows an interface without saying what
it is drawn from is a mock wearing evidence's clothes.

```tsx
<Frame cropped caption="What needs attention" foot="Drawn from the product's own routes">
  <ConsolePanel />
</Frame>
```
