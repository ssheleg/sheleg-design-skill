---
category: Surfaces
---

The solid instrument card: `--panel` with a 1px `--accent` border at `--r-cell`, `12px
14px` padding, no shadow. The title is mono 13px/700 in `--accent`; the meta is mono
12px in `--ink-muted` (9.32:1 on the panel).

A card sits on the field or inside a `Panel`. Over the rain, use `Glass` instead: a
solid card over moving glyphs hides them, which is the one thing the signature element
must not lose.

```tsx
<Card title="Live services" meta="4 of 4 up">
  Billing, support, ads and analytics answer.
</Card>
```
