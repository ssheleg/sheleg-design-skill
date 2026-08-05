---
category: Data
---

The small labelled token of this pack: `20px` radius, `8px 16px` padding, body
face at 14px. `neutral` is the floating `--surface-2` fill on a hairline;
`accent` is the quiet sage wash with a `--primary-deep` label, because sage
itself is a fill and never a text colour; `selected` is the cacao fill under
`--on-ink`.

A standalone `Chip` states something already true — a symptom, a nutrient, a
batch. When chips are a filter, use `ChipRail` instead: it owns the "exactly one
selected" rule that a lone chip cannot know about.

```tsx
<Chip>Vitamin D</Chip>
<Chip tone="accent">In your blend</Chip>
<Chip selected>Sleep</Chip>
```
