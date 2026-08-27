---
category: Signature
---

The machine's loader: three `--accent` dots pulsing at 1s `ease-in-out`, staggered
0.2s. It carries a `role="status"` label because the dots alone say nothing. The card
layer has no loader in this pack — a waiting card takes a quiet `--surface-2` block at
its own radius, no shimmer.

Under reduced motion the dots hold at full opacity — the final frame, not the hidden
one.

```tsx
<ThinkingDots label="Analyzing traffic" />
```
