---
category: Surfaces
---

`--surface` inside a 1px `--border`, at `--radius-card`. The border is 1.15:1 against
the field: a seam, not a line. There is no shadow, because a card does not float —
`--shadow-pop` exists for overlays and nothing else.

A row of facts inside a card is separated by a top border and padding, never by a
nested card. Three equal blocks share **one** card with internal dividers.

The head sizes against its **container** (`container-type: inline-size`), so a card in a
narrow column wraps its title and meta instead of overflowing.

```tsx
<Card title="Can an agent discover and trust you?" meta="5/100">
  …
</Card>
```
