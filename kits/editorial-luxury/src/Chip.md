---
category: Data
---

The mono atom: 11px JetBrains Mono, tracked and uppercased, a hairline border
and a pill radius. Chips label things that are already true — a market, a
source class, a period, a tag — and never stand in for a button. `tone="accent"`
is the sage tint for the one value that is the page's subject; `selected` is
the filter state, an accent border over the same tint. Accent chips take their
text from `--accent-deep` on cream and `--accent-on-dark` on espresso, so an
11px label stays legible on both fields. A chip that wants an action is a
`Button`; a chip that wants a verdict is a `Stamp`.

```tsx
<Chip>Q1 2026</Chip>
<Chip tone="accent">Primary source</Chip>
<Chip selected>Verified only</Chip>
```
