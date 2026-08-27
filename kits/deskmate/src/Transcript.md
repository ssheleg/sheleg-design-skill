---
category: Signature
---

The pack's signature element: a `--surface` frame at `--r-frame` with a
`--frame-ring-w` white ring and `--shadow-panel` under it, holding a chat client's
window inset by `--frame-inset` at `--r-frame-inner` — 48px outside, 33px inside, which
is the concentric subtraction and not a second radius token.

Everything inside the frame is quoted: the window paints in `--quoted-bg` with
`--quoted-ink`, in `--font-quoted`, because the client's interface is evidence rather
than a surface you own. `client` labels which one is being quoted; it does not restyle
the frame.

```tsx
<Transcript channel="finance" client="slack">
  <Message author="Tom Becker" time="10:18 AM">
    Run payroll prep for this cycle.
  </Message>
  <Message author="Agent" kind="app" time="10:20 AM">
    Done. Three discrepancies found and fixed. Ready for your approval.
  </Message>
</Transcript>
```
