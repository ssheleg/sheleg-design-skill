---
category: Signature
---

The navigation hangs from the top edge: `--surface`, inset from both sides, bottom
corners rounded and top corners square against the page. No shadow, no
`backdrop-filter`, and no rule appearing on scroll — the scrolled shape is the resting
shape, measured.

Its items are ghost pills that fill with the ink at 5% on hover, each at the
`--tap-min` floor. The trailing edge carries at most one control.

**Below 40rem the link row is hidden and `action` carries the toggle.** A slab is one
flex row: keeping the links at 390px pushes the trailing control 515px wide, off the
page. Put a disclosure button in `action` at that width.

```tsx
<NavSlab brand={<strong>acme</strong>} action={<Button size="sm">Get started</Button>}>
  <a href="#product">Product</a>
  <a href="#pricing">Pricing</a>
</NavSlab>
```
