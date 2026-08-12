---
category: Signature
---

The pack's signature element: the frame that reads the visitor's own data back to
them. `--r-frame` on `--surface`, 8px of padding so an inner shell resolves to
`--r-inner` (16 − 8 = 8, which the reference proves on itself), and a grid of
cells whose walls are hairlines at radius 0.

`alarm` is the whole idea. On the reference, 134 rules re-skin this frame dark
when it detects the reader is in incognito — the argument completes itself with no
copy. It is a **state, not a theme**: drive it from what was detected, never from
a preference or a media query. Build the light state first and completely.

```tsx
<Instrument title="Hello, visitor JzzA01Muat9b30Sh60KJ" badge="This is real data">
  <Cell label="Weekly visit summary">You visited 1 time</Cell>
  <Cell label="IP address" mono>83.175.182.157</Cell>
  <StatusCell label="Incognito" reading="success">Not detected</StatusCell>
</Instrument>
```
