---
category: Surfaces
---

A window that floats over the rain: `--glass` (the field at 85%) with an 8px backdrop
blur, a 1px `--accent-rim` border, `--r-window`, and `--glow-window`. The header is mono
17px/700 over a 1px dashed `--accent-edge` rule. `brackets` adds the two 18px AR corner
marks in `--accent`.

Glass exists so the rain stays visible behind something that must be read: `--ink` on
the composited glass stays above 17:1. With nothing moving behind it, use a solid
`--panel` instead; decorative glass is banned in this pack.

The window is a container (`container-type: inline-size`): its lines step from 19px
to 16px when the window itself is narrow, not when the screen is.

```tsx
<Glass title="# ops" meta="6 members" brackets>
  <ChatLine who="Ops lead">Who owns the launch checklist?</ChatLine>
</Glass>
```
