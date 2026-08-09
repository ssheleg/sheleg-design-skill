---
category: Signature
---

A mono chip on `--model-top` with a 1px dotted `--leader` to its block.

**The label never scales.** 13px at every width. Scaling captions with the
drawing makes them illegible exactly when the drawing is hardest to read; below
640px they move outside the model's box with longer leaders instead.

Mono, because in this pack prose is the grotesque and anything the *drawing*
says is monospaced. A block label set in Geist stops reading as part of the
object.

```tsx
<LeaderLabel label="Iterative Discovery" side="top" />
```
