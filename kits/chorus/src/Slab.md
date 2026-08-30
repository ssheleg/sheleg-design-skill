---
category: Surfaces
---

The dark band cut into the paper: `--slab` at `--r-panel`, inset `--slab-inset` (30px,
measured against the viewport rather than a parent), full width otherwise.

It carries `data-surface="slab"` — the library's own unprefixed hook, so this pack
can be A/B'd against any other by swapping the token layer alone — and that
attribute is what re-declares the six tokens that would otherwise resolve to a
light-field value on a dark ground. That re-declaration is not decoration:
the ink focus ring measures 1.00:1 against `--slab` and would vanish on the band that
carries the closing CTA.

**It is a surface, not a theme.** The page never inverts, and there is no dark twin of
this pack.

```tsx
<Slab><Heading>Meet the engagement engine</Heading></Slab>
```
