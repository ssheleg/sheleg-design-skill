---
category: Foundations
---

Level 1 is the human voice: Inter 800 at `clamp(38px, 4.4vw, 68px)`, line-height 1,
tracking -0.03em, `--ink`, balanced and held at 16ch so it never runs past four lines.
Level 2 is the machine voice: mono 700 at `clamp(20px, 2.2vw, 28px)`/1.15 in `--accent`.
Level 3 is a mono 12px/700 caps label at 0.1em in `--ink-muted`.

No gradient text at any level. The emphasis is `--accent`, lit with `--glow-text`.

```tsx
<Heading level={1}>Your business runs itself</Heading>
```
