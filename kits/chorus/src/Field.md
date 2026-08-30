---
category: Actions
---

The reference paints exactly one input — a search field inside a demo well — and this
is it: `--surface` at `--r-control` with a 1px `--line`, a 16px/400 value in
`--ink-body`, the placeholder in `--ink-ghost`, and a filled `--coral` action seated
inside the right edge with its label in `--on-coral`.

Focus paints the ring **and** keeps the border. There is no other field type on the
page: a select or a checkbox built here takes this geometry and the Palette's colours
rather than a new value.

```tsx
<Field label="Prompt" placeholder="best online payment methods" action="Monitor" />
```
