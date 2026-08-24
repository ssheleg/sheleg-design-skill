---
category: Actions
---

`primary` is the coral ramp — `--action` — and there is at most one per view. Its
label is 14px/700 uppercase at `--track-caps-control`, and white on it clears AA at
every point along the ramp because the ramp was corrected for exactly that: the
reference's own gradient is 2.90:1 under white.

Hover does **not** change the fill. It spends `--shadow-action-hover` and lifts by
`--lift`, both at `--dur-base` — the reference's own hover here is a glow, and
darkening a coral on hover reads as a disabled state. `active` takes
`--action-pressed` and returns the lift to 0.

`secondary` is a plate that happens to be a button: `--surface` fill, 1px
`--line-soft`, no fill change on hover. `ghost` carries no border.

Every size honours `--tap-min` (44px) as a height floor.

```tsx
<Button>See how it works</Button>
<Button variant="secondary">View real results</Button>
```
