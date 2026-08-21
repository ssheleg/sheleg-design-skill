---
category: Actions
---

The pill, and the ring. Every control in this pack is `9999px`; the primary
variant wears a **5px `--accent-ring`** — a wide light border, not a shadow —
which is the one device that makes this brand's button recognisable at thumbnail
size. It is decoration and carries no affordance (1.72:1 on `--bg`), so
`focus-visible` uses a 2px accent outline at 2px offset instead.

`secondary` is the ghost door: on the reference's hero it reads `Join with
Google` beside `Get Started for Free`, and the two are **one job with two doors**
rather than two primary actions competing.

```tsx
<Button>Get Started for Free</Button>
<Button variant="secondary">Join with Google</Button>
```
