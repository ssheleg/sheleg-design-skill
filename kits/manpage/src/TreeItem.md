---
category: Signature
---

Terminal output as a typographic device: a box-drawing glyph in **its own grid
column**, never a text prefix.

That distinction is the whole component. As a two-column grid the glyph cannot
wrap into the text, cannot be selected with it, and cannot land inside an
extracted snippet — which matters because this is what the reference hangs its FAQ
answers off, and those answers are what an answer engine quotes. It is
`aria-hidden`, so a screen reader hears the answer and not the drawing.

```tsx
<TreeItem>Custom integrations take 8-12 months. This takes under an hour.</TreeItem>
<TreeItem kind="branch">Calls and inbox included.</TreeItem>
```
