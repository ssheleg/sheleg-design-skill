---
category: Actions
---

The primary button is a **black pill**. Its radius comes from `--radius-button`,
which points at `--radius-full` — the indirection is the only place the system
says why a button is that shape, so keep it rather than writing `9999px`.

Hover changes **two** properties: the fill lightens to `--accent-hover` and the
label moves to `--accent-ink-hover`. Moving only the fill reads as a lightening;
moving both reads as a press. `secondary` is transparent at every state — fill,
hover, active and disabled alike — so its whole identity is the border and the
label, which is why this pack ships two rule weights.

Disabled is a **value**, not an opacity: `--accent-disabled` fill with
`--accent-ink-disabled` content. Nothing in this system fades, so a disabled
control keeps its edges and stays measurable.

```tsx
<Button onClick={start}>Start free trial</Button>
<Button variant="secondary" onClick={demo}>Watch the demo</Button>
<Button variant="ghost" size="sm" onClick={more}>Compare plans</Button>
```
