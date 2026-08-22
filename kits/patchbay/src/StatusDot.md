---
category: Data
---

**`label` has no default and no optional marker, which is the whole point.**
Status in this pack is never by colour alone.

The three status hues are a **pack decision** — the reference paints no success,
warning or error state anywhere — and they are derived against a constraint most
packs do not have: the accent is a mint-cyan, so the ordinary dark-UI green
collides with it under dichromacy. `instrument-console`'s `#46D39A` separates
from this accent by **3.51** under simulated CVD against a floor of 8, and was
rejected for it. Every candidate that clears the floor is light, which is why
`--ok` sits above `--warn` and `--danger` in luminance rather than beside them.

```tsx
<StatusDot state="ok" label="Connected" />
<StatusDot state="danger" label="Venue unreachable" />
```
