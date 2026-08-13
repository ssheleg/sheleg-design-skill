---
category: Actions
---

The primary action is **black**, and that is the reference's own choice rather than
this pack's invention: of its two CTAs, white on `--cta` measures 19.66:1 and white on
the accent 3.43:1. The page had already answered the question.

The `secondary` variant is the accent fill and it carries **`--ink`, not white**. An
accent button that must be light-on-dark has to reach large text first (≥24px, or
≥18.66px bold); below that the contrast is not there.

`:focus-visible` is `--accent-ink`, never `--accent` — 3.18:1 is too little for a ring
a keyboard user has to find.

```tsx
<Button>Start 3-day trial</Button>
<Button variant="secondary">Try free</Button>
```
