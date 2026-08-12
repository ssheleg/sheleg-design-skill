---
category: Data
---

Where a verdict lands: the mono face at 15px with -0.03em on a `--r-chip` corner,
padding `0 4px`, text in a status token over that status's tint. The reference
sets its `suspicious` verdict exactly this way, inside a sentence, so the chip
reads as a value the system produced rather than as a label someone applied.

Without `reading` it is a neutral machine value — a version, a rule id.

```tsx
You look like a <ValueChip reading="danger">suspicious</ValueChip> user
```
