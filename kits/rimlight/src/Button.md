---
category: Actions
---

The ordinary control: transparent with a `1px solid --ink-faint` border at `--r-pill`
(160px), its label the monospace at 16–18px/500 uppercase, height `--control-h` (48px)
or `--control-h-lg` (60px).

`primary` fills with `--ink` and takes `--on-ink`. **It does not wear the rig** — that
belongs to `LitButton`, one per viewport. Hover moves the border to `--ink` and never
adds a fill; nothing on this page travels in space.

Every size honours `--tap-min` (44px) as a floor.

```tsx
<Button variant="secondary">View project</Button>
```
