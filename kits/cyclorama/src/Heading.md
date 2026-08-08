---
category: Foundations
---

The monospaced display face at `--t-h1` / `--t-h2` / `--t-h3`, all tracking at
the one authored `-0.02em`. One decision, not three — keep it as one.

`text-wrap: balance` matters more here than in a proportional pack. When every
glyph is the same width, a short last line does not read as ordinary rag; it
reads as a measured gap, because the eye can count the missing characters.

The display face is **monospaced**, and every substitute must be too. Courier
Prime (advance 0.600) and Cutive Mono (0.605) match the original's 0.590. Zilla
Slab and Bitter are proportional and will not merely restyle a heading — they
reflow it.

```tsx
<Heading level={1}>Ready to run your business like code?</Heading>
<Heading>From zero to running — in days.</Heading>
```
