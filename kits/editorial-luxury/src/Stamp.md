---
category: Signature
---

The seal: a 2px box of tracked mono, rotated four degrees so it reads as
pressed onto the page rather than laid out on it. The tilt is a static
transform — nothing here animates. A stamp states a verdict the product has
actually reached ("Verified", "Primary source", "Superseded"), so never stamp
something the system has not checked; an unearned seal is worse than none.

`tone="accent"` is the default sage. `terra` is the rare editorial highlight.
`red` is negatives **only** — the "without" column of a comparison, a rejected
claim — and never a warning, a badge or a decoration. Both non-sage tones are
pulled a third of the way toward the surface's ink so an 11px label clears
4.5:1 on cream and on espresso alike.

```tsx
<Stamp>Verified</Stamp>
<Stamp tone="terra">Editor's pick</Stamp>
<Stamp tone="red">Unsourced</Stamp>
```
