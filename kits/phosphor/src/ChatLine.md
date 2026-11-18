---
category: Signature
---

One line in a `Glass` window: an initials disc (`--face` with `--ink-bright`, 12.40:1)
or a portrait, the speaker in mono 13px/600 `--ink-muted`, and the line itself in Inter
19px/1.4 on `--panel-raised` with a 1px `--line` border and the radius `4px 14px 14px
14px`, whose sharp corner points at the speaker.

`agent` moves the border to `--accent` and adds a `0 0 18px --accent-trace` glow: the
machine's lines are the lit ones. `system` drops the bubble for a centred mono line in
`--accent`.

```tsx
<ChatLine who="Mila" initials="MK">Can someone own onboarding this week?</ChatLine>
<ChatLine who="Agent" agent>Taking it. Plan in ten minutes.</ChatLine>
<ChatLine who="" system>Agent joined the channel</ChatLine>
```
