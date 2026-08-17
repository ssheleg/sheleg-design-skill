---
category: Foundations
---

Three levels, all fluid, all one family: level 1 is `--t-hero` (27px at 390 →
62px at 1024, both endpoints measured), level 2 is `--t-act` (28 → 62), level 3
is `--t-feature` (28 → 39).

The weights are the hierarchy, because the family never changes: 600 on the
display and the act heading, 700 on the feature heading. The reference loads
Inter at nine weights and no second face anywhere on the page.

Level 1 is capped at 32ch, which holds it to two lines at 1440. A headline that
reaches five lines is a broken hero, not a long one.

```tsx
<Heading level={1}>Your company runs in Telegram</Heading>
<Heading>Everything around the conversation, in one place</Heading>
<Heading level={3}>Know who holds every account</Heading>
```
