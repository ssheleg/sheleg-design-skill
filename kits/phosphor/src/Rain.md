---
category: Signature
---

The signature element: falling glyph columns on a fixed canvas behind the page, at
`--rain-opacity` (0.5). Each column is one glyph wide and falls at 40 to 130px a
second, trailing 8 to 30 glyphs; the head glyph is `--ink-bright` at 0.9 and changes
every `--dur-glyph`, the tail is `--accent` fading out. Glyphs are 16px, 13px when the
window is under 700px. `boost` multiplies the speed (the reference feeds it scroll
velocity, capped at seven).

Colours and sizes are read from the token layer with `getComputedStyle`, so moving a
token moves the rain. Under `prefers-reduced-motion: reduce` the loop never starts and
the canvas is hidden; it also stops while the tab is hidden.

Mount it once per page, behind everything. A second ambient layer breaks it.

```tsx
<Rain />
```
