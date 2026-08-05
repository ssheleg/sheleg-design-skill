---
category: Actions
---

Buttons here are tactile: they lift 2px on hover with the pack's spring and
settle on press. No glow, ever — an outer glow on a button is a ban in this
pack, and a shadow that grows under the cursor is the same ban in a different
costume, so the primary's soft ambient shadow is held constant. `primary` is
the sage fill (`--accent-deep`, so its `--accent-ink` label clears 6.1:1 at
label sizes); `secondary` is the hairline-bordered one that warms to sage on
hover; `ghost` is the bare one for a third-tier action. Inside an
`.el-espresso` section all three swap to `--accent-on-dark` with no prop
change. Focus-visible is a 2px sage outline at 3px offset on every variant.

```tsx
<Button onClick={runSweep}>Run the sweep</Button>
<Button variant="secondary" onClick={openMethod}>Read the method</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Not now</Button>
```
