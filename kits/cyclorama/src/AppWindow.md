---
category: Surfaces
---

A `1px var(--line)` frame at `--radius-lg` with 12px of padding and **no fill at
all**, so the field cycle shows straight through it. Traffic-light dots at the
left, a mono title and sub-line in the centre, a slot for a `StatusPill` at the
right, and a row of chips along the foot.

**Giving it a background is the most common way to break this pack.** The window
is a frame, not a surface. Fill it and the page's signature stops at its border:
the screenshot inside becomes a foreign object pasted onto a pastel page,
instead of a product glimpsed through it.

Its 12px of padding is also what sets the chips inside to `--radius-sm`, since
`16 − 12 = 4`. Change the padding and the inner radius has to move with it.

```tsx
<AppWindow
  title="diagnostic interviews"
  meta="Session ID4611.4 · VP Sales · 01:55"
  status={<StatusPill status="live" label="Listening" />}
  footer={<><Chip>Mic on</Chip><Chip>Phase 2 of 5</Chip></>}
>
  Most start inbound — a founder demo request.
</AppWindow>
```
