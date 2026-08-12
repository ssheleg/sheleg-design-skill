---
category: Actions
---

One accent fill per view, and in this pack that fill is `--action` — the
reference's own orange one ramp step deeper than its brand orange, because white
on the brand step measures 3.32:1 and does not clear AA. `secondary` is the
1px-bordered outline in `--accent-deep`; `ghost` is the bare navigation control
that changes ink and nothing else. Hover moves fill, border and colour over
`--dur-base`; nothing lifts, scales or gains a shadow. Disabled drops to 0.7
opacity with pointer events off, measured off the reference.

```tsx
<Button onClick={start}>Get started</Button>
<Button variant="secondary" onClick={contact}>Contact sales</Button>
<Button variant="ghost" size="sm" onClick={close}>Dismiss</Button>
```
