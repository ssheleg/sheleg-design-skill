---
category: Actions
---

Every control is an 8px-radius block at `--control-h` (48px) with `--control-px` of
horizontal padding, 16px at `--weight-control`. `sm` is `--control-h-sm` (32px) — the
nav's measured pair, and the reason `--tap-min` exists as a correction.

`primary` fills with `--action`, labels in `--on-action` at 4.94:1 on `#c04a28`, and is
lit by `--lit-action` — the four-layer coral recipe. Hover moves the fill to
`--action-hover`, the resolved form of the reference's own
`color-mix(in oklab, fill 90%, #000)`. `secondary` is `--surface` with a `--hairline`
border and `--lit-quiet`; hover brightens the glow to `--lit-quiet-hover`, and the
control itself does not move. `ghost` is transparent until hover fills it with
`--hairline`.

Press scales to `--press-scale` (0.95) over `--dur-press`. Focus is one mechanism: a
`--focus-w` outline in `--focus-color` at `--focus-offset`.

```tsx
<Button>Add my website</Button>
<Button variant="secondary" size="sm">Log in</Button>
```
