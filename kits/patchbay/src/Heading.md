---
category: Foundations
---

Tracked **negative above 24px and zero below** — which is the pack's decision,
not the reference's behaviour. MUI's theme default `letter-spacing: 0.00938em`
leaks into everything the reference did not override, so its 59.2px hero is
tracked **+0.555px**: positive tracking on a display line, two selectors away
from designed styles that track −0.3px.

The display face steps rather than clamps: 2.8rem below 900px, 3.7rem above.

```tsx
<Heading level={1}>The fastest open-source trading engine</Heading>
```
