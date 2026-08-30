---
category: Surfaces
---

The floating navigation: `--surface` at `--r-panel` under `--shadow-nav`, **inset from
the frame rather than pinned to the viewport edge** — it sits on the sheet, not above
it.

Items are 14px/500 in `--ink-muted` at 5.36:1 on `--bg`, at `--r-pill`, and hover
fills `--line-quiet` behind them. The action is a `Button` at `secondary`.

`--shadow-nav` is one of the four shadows this pack has, and it belongs to this
component alone.

```tsx
<NavPill brand={<Logo />} action={<Button variant="secondary">Login</Button>}>
  <a href="/pricing">Pricing</a>
</NavPill>
```
