---
category: Signature
---

The one light object in the pack: a comic speech balloon. `--balloon` fill, a 2px
`--keyline` outline, `--r-balloon` (18px), `--offset-keyline` (a hard 4px black offset),
`10px 16px` padding and a tail drawn in `--keyline` pointing at the speaker. The line is
Inter 18px/1.35 in `--on-balloon` (18.34:1); the speaker label is mono 11px/700 caps at
0.08em in `--balloon-who` (6.18:1 on the fill).

**The text colour is pinned with a selector that outranks any surrounding panel.** The
live reference declares this colour and then loses it to a later `.panel p` rule, so
its balloons paint pale text on a pale fill at 1.01:1. The kit's `.ph-balloon
.ph-balloon__text` cannot be overridden by `.ph-panel p`.

```tsx
<Balloon who="Guide" side="left">Every task has an owner now. Watch.</Balloon>
```
