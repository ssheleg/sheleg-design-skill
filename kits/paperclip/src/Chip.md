---
category: Data
---

A capsule at `--r-pill` with a hairline border and a `--muted` label. `selected` fills it
with `--accent` and sets the label in `--accent-ink` — **the same inversion as the primary
button**, which is what makes "selected" and "primary" read as one idea rather than two
visual languages in one form.

Used as a radio group, keep the real `<input>` visually hidden at 1×1px rather than
`display: none`, so arrow keys still move the selection and `:focus-visible` can draw the
ring on the label.

A chip is never the only place a state is written. Where it carries a status, the status
word goes **inside** it (`In Progress`, `Active`) — status is never by colour alone in
this pack, in either theme.

```tsx
<Chip>Codex</Chip>
<Chip selected>Claude</Chip>
```
