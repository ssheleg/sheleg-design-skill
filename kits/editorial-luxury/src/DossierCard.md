---
category: Signature
---

The pack's file-card, and the surface its identity is built on: a 30px
squircle, a heavier hairline, an eyebrow and title on the left, the file
reference and a `Stamp` on the right, then a rule and the body. Use it for the
things the product treats as documents — a report, a case, a finding, a
briefing — and use plain `Card` for everything else. It carries the same
no-nesting rule as `Card`, enforced in CSS: a dossier inside a dossier drops
its chrome, because two folders on top of each other is a layout mistake the
eye reads as a bug.

```tsx
<DossierCard
  eyebrow="Competitor teardown"
  title="Northbeam's pricing page, read end to end"
  reference="Case 0114 · 12 Mar"
  stamp={<Stamp>Verified</Stamp>}
>
  <p>
    Three tiers, one hidden. The enterprise price appears only after a
    calculator interaction, which is why the published comparison undercounts it.
  </p>
</DossierCard>
```
