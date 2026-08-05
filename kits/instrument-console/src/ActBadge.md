---
category: Signature
---

The console's section index — "02 / CONTROL" — in the mono face, tracked out and
upper-cased. On the landing page a store subscription swaps it as the scroll
crosses an act boundary; here it is the static badge that names where the reader
is, so pass the act you are on and let the caller decide when it changes. The
index is a number and the component pads it, because "2 / CONTROL" is a different
typeface rhythm from "02 / CONTROL" and the pack specified the second one.

```tsx
<ActBadge index={2} name="Control" />
<ActBadge index={4} name="Downlink" />
```
