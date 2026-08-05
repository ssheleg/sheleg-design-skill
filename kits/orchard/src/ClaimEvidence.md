---
category: Signature
---

An assertion in the display face, followed by a quieter citation line in
`--ink-soft` naming the study or source. On a health page this is not
decoration — it is the reason the page is allowed to make the claim at all,
which is why `source` is a required prop rather than an optional one.

The claim sits at 24px, below the pack's `28px` tracking floor, so it takes
normal tracking; the citation is 14px at `1.5` leading, which is precisely the
job `--ink-soft` exists for. Inside a cacao `Slab` the citation steps to
held-back `--on-ink`, because soft ink on cacao is invisible.

```tsx
<ClaimEvidence
  claim="Personalised dosing beat a fixed multivitamin on six of nine markers."
  source="Randomised, 412 participants, 12 weeks · Nordfeldt et al., 2025"
/>
```
