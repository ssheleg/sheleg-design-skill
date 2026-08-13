---
category: Foundations
---

The small tracked line above a section head — `--track-eyebrow` 0.4px is the only
tracked type in the pack — in `--accent-ink` rather than `--accent`, because 3.18:1
is not enough for 16px text.

It renders a `<p>`. The reference marks all sixteen of its eyebrows as `<h2>`, which
is how a document outline ends up saying "eyebrow" where the page says "section
head".

```tsx
<Eyebrow>How it works</Eyebrow>
<Heading level={2}>Organic growth made simple</Heading>
```
