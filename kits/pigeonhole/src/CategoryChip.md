---
category: Signature
---

**The pack's signature element.** Two nested chips: the outer carries the deeper
tint pair at `--radius-chip` (8px), the inner the paler pair at
`--radius-chip-inner` (7px) with 1px of padding between them — exactly the step
the reference uses, and the one place in it where radius-by-subtraction happens
to hold.

`children` is **required**, and that is a design decision enforced by the type.
Neither set of inks clears the bar: as the reference paints them, the worst
deuteranopic pair (Marketing against Notification) is **4.42 ΔE** against the
palette gate's hard floor of 10, so these hues were never distinguishable to that
reader. Deriving them to clear WCAG AA makes it worse rather than causing it — the
same pair falls to **1.24**. Nine hues cannot be simultaneously AA-compliant and
mutually distinguishable to a dichromatic reader, so the word carries the category
and the hue reinforces it. A chip without its label is not a quieter chip, it is an
unreadable one.

Each ink clears 4.5:1 against the deepest tint of its own ramp. All nine are
derived from the reference's values, which fail that floor in eight cases out of
nine; the numbers are in the pack's Gotchas.

## Selected, for categories that are filters

A chip is a label, so it has no pressed state — but where the product's categories
*are* filters, the reader needs to know which one is on. Add `pg-cat--selected` (or
`aria-pressed="true"`, which the stylesheet matches): the inner layer takes its
category's `-150` step instead of `-50` and the ink marks a 2px inset. That inset is
the one border a chip may carry.

## Two of the nine do not render two layers

`--cat-cold-150` and `--cat-cold-100` are the same measured literal, and
`--cat-step-50` is the page white — so on Cold Email and on STEP the 8px→7px step
is invisible against `--surface`. Both are faithful to the reference. Where those
two must read as two layers, put them on `--surface-2`.

```tsx
<CategoryChip category="reply">To Reply</CategoryChip>
<CategoryChip category="newsletter">Newsletter</CategoryChip>
<CategoryChip category="marketing" className="pg-cat--selected">Marketing</CategoryChip>
```
