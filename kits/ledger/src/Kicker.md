---
category: Signature
---

10px monospace, uppercase, `+0.1em`, in `--accent`. On the reference this is
where the accent actually lives: of eleven accent-coloured elements on the page,
five are this label and **none** is a button.

Use it above a section title, above a stat, or as a clickable example query in an
empty state. Two accent kickers stacked is one too many — the second takes
`tone="muted"`, which is the same shape in `--muted`.

```tsx
<Kicker>Ranked #1 on BI Bench</Kicker>
<Heading level={1}>Revenue overview</Heading>
```
