---
category: Actions
---

`primary` is the **inverted field**: `--accent` is the ink, so the button is a solid
cream slab on coal and a solid near-black slab on paper, and the label takes
`--accent-ink`. At 16.72:1 in dark and 16.90:1 in light it is the highest-contrast
object on the page, which is why the pack allows **one per view**.

Hover is the reference's own: the fill drops to 90% opacity. Nothing translates,
scales or lifts — this pack does not press.

`secondary` is a hairline over `--surface-raised`; its hover moves the **border** to
`--border-strong` and leaves the fill where it is. `ghost` is mono, `--muted`, and
gains `--ink` on hover.

```tsx
<Button>Run</Button>
<Button variant="secondary">Rescan</Button>
<Button variant="ghost">View logs</Button>
```
