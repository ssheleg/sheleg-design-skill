---
category: Actions
---

One shape at three sizes, square, filled `--ink`, labelled `--accent-ink` in tracked
mono caps. **Hover is the accent** — the fill goes orange and the control lifts 1px
(2px at `lg`). That inversion is the pack: at rest the page has no colour in it.

The measured trap, and the reason `secondary` exists: contrast is symmetric, so a paper
label on the orange fill is the same **3.02:1** the orange measures on the paper. A mono
label at ~10.4px is not large text, so a `primary` button's label stops being conformant
at the moment it is hovered. Use `primary` where the label is duplicated or decorative;
where the label is the only statement of what the control does, use `secondary`, whose
hover moves the **border** to the accent and leaves the ink fill alone.

`ghost` is mono in `--ink-soft` with no fill, gaining `--ink` on hover.

```tsx
<Button size="lg">Book a demo</Button>
<Button variant="secondary">See how it works</Button>
```
