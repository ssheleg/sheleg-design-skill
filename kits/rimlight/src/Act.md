---
category: Surfaces
---

A full-bleed section on one of the pack's three fields. `field="dark"` sets
`data-surface="dark"`, which remaps the palette **for that band only**.

**It is not a dark mode.** The reference has no toggle and no second palette for the
document: one section carries the dark treatment and the rest of the page stays light.
Putting `data-surface="dark"` on `:root` inverts a page that was never designed to
invert.

The dark act is where the reference's colours finally work — every one of its
secondary hues is 6.5–10.5:1 there against 1.65–2.65:1 on white.

```tsx
<Act>…</Act>
<Act field="dark">…</Act>
```
