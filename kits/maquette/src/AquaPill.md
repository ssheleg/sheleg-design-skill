---
category: Actions
---

`--accent` fill, `--radius-pill` 36px, **black** label at 17.81:1.

Not the cream — it measures 1.1:1 on the aqua and vanishes. And the focus ring
here is `--ink`, not `--accent`: aqua on aqua is nothing. That conditional is
easy to miss because it shows up only on the primary CTA.

Every action in this pack is a pill, on a page otherwise made of rectangles.

```tsx
<AquaPill onClick={start}>Get Started Free →</AquaPill>
```
