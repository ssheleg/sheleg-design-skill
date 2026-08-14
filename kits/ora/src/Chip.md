---
category: Data
---

`--radius-chip` (4px, the root radius halved), a 1px border and mono at 11px in
`--muted`. Hover moves the border and the text toward `--accent`; `selected` completes
the move.

A chip that reports a status carries a `StatusDot` **and** the word. A chip is never a
button: if it triggers something, it is a `Button` with `variant="ghost"`.

```tsx
<Chip>find pricing</Chip>
<Chip selected>create an account</Chip>
<Chip tone="accent">MCP</Chip>
```
