---
category: Actions
---

Every control is a pill at `--control-h` (56px) with `--control-px` of horizontal
padding and a `--rule-w` border, 16px at `--weight-body` and `--track-control`. `sm` is
`--control-h-sm` (40px) at 24px and 14px — the navigation's size.

`primary` fills with `--ink` and labels in `--on-ink`, 17.36:1. `secondary` is
`--surface` with the ink at 12% and hover mixes 6% of the ink into the fill.
`ghost` is transparent until hover, which fills with the ink at 5%.

Press travels 1px down and nothing scales. Focus moves the border to `--focus-color`
and adds `--focus-ring` — both, always.

```tsx
<Button>Get started for free</Button>
<Button variant="secondary">Book a demo</Button>
```
