---
category: Signature
---

The act separator, and it is drawn rather than ruled: a `--wave-h` (150px) arc
overspilling to `--wave-w` — `calc(150% + 1.3px)` — filled in the colour of the act
**below**, so it reads as the next field rising rather than as an object.

The overspill is the whole trick. At exactly 100% width the same path reads as a
bubble, and the 1.3px hides the seam at fractional device pixel ratios.

Hidden under `--wave-hidden-below` (768px), where the acts butt directly: 150px of
scroll for a curve nobody reads is a bad trade on a phone.

```tsx
<section className="np-act--slab">…<Wave into="page" /></section>
```
