---
category: Signature
---

The terminal headline: a mono 11px/600 chapter at 0.14em in `--accent` wrapped in `[ CH
` and ` ]`, then the line in mono 700 `clamp(22px, 2.4vw, 34px)`/1.1 in `--accent` with
`--glow-text`, after a `> ` prompt at 55% opacity. `typed` reveals it with a clip on
`steps(24)` over `--dur-type`: a stepped reveal is a terminal, an eased one is a slide.
Under reduced motion it is simply there.

```tsx
<Prompt chapter="03" typed>The plan has an owner for every task</Prompt>
```
