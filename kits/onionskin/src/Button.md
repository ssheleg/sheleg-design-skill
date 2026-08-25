---
category: Actions
---

`primary` fills with `--accent` and takes `--on-accent` — 5.25:1, and the same number
in both directions, which is why this pack needs no derived accent twin. `secondary` is
`--surface` with a 1px `--rule` and an `--ink` label; hover moves the border to
`--accent-rule` and never adds a fill.

`--r-sm` (4px), and every size clears `--tap-min` (44px). The reference's own controls
are 36px — that is the one geometry this pack corrects rather than copies.

```tsx
<Button>Get an API key</Button>
<Button variant="secondary">Read the docs</Button>
```
