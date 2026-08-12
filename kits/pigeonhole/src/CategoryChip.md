---
category: Signature
---

**The pack's signature element.** Two nested chips: the outer carries the deeper
tint pair at `--radius-chip` (8px), the inner the paler pair at
`--radius-chip-inner` (7px) with 1px of padding between them — exactly the step
the reference uses, and the one place in it where radius-by-subtraction happens
to hold.

`children` is **required**, and that is a design decision enforced by the type.
Darkening the nine measured inks to clear WCAG AA compresses them in OKLab: the
worst deuteranopic pair, Marketing against Notification, ends up **1.24 ΔE**
apart, far under the palette gate's hard floor of 10. Eleven hues cannot be
simultaneously AA-compliant and mutually distinguishable to a dichromatic
reader — so the word carries the category and the hue reinforces it. A chip
without its label is not a quieter chip, it is an unreadable one.

Each ink clears 4.5:1 against the deepest tint of its own ramp. All nine are
derived from the reference's values, which fail that floor in eight cases out of
nine; the numbers are in the pack's Gotchas.

```tsx
<CategoryChip category="reply">To Reply</CategoryChip>
<CategoryChip category="newsletter">Newsletter</CategoryChip>
```
