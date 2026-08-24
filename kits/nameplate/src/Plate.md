---
category: Signature
---

**The pack's reason to exist.** A white pill with a 1px `--line` border and
`--shadow-pill` (4% at 2px), carrying one borrowed name as 15px/500 type at
`--pill-h` (50px). It is the plate you were issued: a publication, an authority, a
certification.

It carries **type, never a logo** — that is what lets thirty of them sit together
without becoming a ransom note of thirty typefaces, and it is why a reader can read
the list rather than scan it.

Hover lifts by `--lift` and grows the shadow to `--shadow-pill-hover` in the same
`--dur-base`; animating one without the other is the fastest way to break the pack.
`pending` drops to `--ink-faint` and takes no shadow.

One name per plate. No fill, ever — the border is the plate.

```tsx
<Plate name="Business Insider" href="https://…" />
<Plate name="AP News" />
<Plate name="Your outlet here" state="pending" />
```
