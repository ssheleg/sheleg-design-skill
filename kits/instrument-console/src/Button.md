---
category: Actions
---

The console has one signal, so `primary` is the accent fill and the screen gets
one: its label is `--accent-ink`, because white on this blue fails AA. Hover
brightens to `--accent-bright` and press drops to `--accent-dim` — the pack's
"one shade dimmer, no bounce"; nothing translates, scales or springs.
`secondary` is a surface step (`--surface-2` on a `--hairline-strong` border) and
`ghost` is the bare one for dense toolbars. Focus-visible is the pack's own
1px `--accent` ring with an `--accent-glow` halo on every variant.

```tsx
<Button onClick={deploy}>Arm sequence</Button>
<Button variant="secondary" onClick={openLog}>Open flight log</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Dismiss</Button>
```
