---
category: Actions
---

A pill. `primary` is the reference's action: `--accent` fill, an `--on-accent` label
(13.45:1), Inter 14px/700, `8px 14px`, 37px tall, wearing a 2px `--keyline` ring, a hard
`--offset-keyline` and `--glow-action`. Hover moves the fill to
`--accent-hover` over `--dur-hover`; the press sits the button into its own offset over
the same 120ms, which is inside the doctrine's press band. **A white label on the
phosphor is banned at every size.**

`secondary` is the ghost: no fill, a 1px `--line-strong` border, an `--ink` label;
hover lights border and label to `--accent`. `ghost` is a bare text link in `--ink`
that lights on hover.

`lg` is the hero size: 18px, `14px 22px`, 55px tall. On a coarse pointer every size
grows to the 44px tap floor (a pack decision; the reference's bar button is 37px).

Disabled: `--panel-raised` fill, `--ink-muted` label, no offset and no glow.

```tsx
<Button size="lg">Start the story</Button>
<Button variant="secondary">See how it runs</Button>
```
