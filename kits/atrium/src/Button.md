---
category: Actions
---

**This is the pill triad, and the pack has no other button.** Every control is
`999px` at `12px 25px` with a `14px` icon gap, in exactly three variants:
`primary` is the solid accent, `secondary` the accent-outline on the field, and
`ghost` the beige-on-photo light pill that carries `--shadow-cta`. A fourth
button style is drift, which is why there is no separate pill component to
choose between — the pack's pill *is* the spine's `Button`.

Hover **swaps fill and ink between the accent pair**: nothing scales, nothing
lifts, and the transition names `background-color`, `color` and `border-color`
rather than `all`. Text on the accent is `--accent-ink`, the field's beige,
never white. `size` is not a fourth variant: `md` is the pack's pill exactly and
`sm`/`lg` only rescale that padding.

```tsx
<Button onClick={startTest}>Get started</Button>
<Button variant="secondary" onClick={seePanel}>See the full panel</Button>
<Button variant="ghost" onClick={playFilm}>Watch the film</Button>
```
