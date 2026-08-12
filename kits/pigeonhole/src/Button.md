---
category: Actions
---

The primary is the only accent fill on a view, and its gradient runs
**light-to-dark** — `--accent-2` at the top into `--accent` at the foot. The
reference runs it the other way, where its white label clears 5.04:1 against the
upper stop and 3.29:1 against the lower one; reversing the stops puts the label's
worst case on the passing colour and changes nothing a reader would notice.

Its shadow is tinted to the accent (`--shadow-cta`), never to black. `:hover`
lifts the shadow and translates 1px; `:focus-visible` draws a 2px
`--accent-strong` ring at 2px offset — the reference computes `outline-style:
none` here and adds no compensating shadow, so this ring is the kit's correction
rather than its copy.

```tsx
<Button>Get started</Button>
<Button variant="secondary">Talk to sales</Button>
```
