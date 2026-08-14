---
category: Surfaces
---

The container half of the hairline lattice: it draws the top and left edge, and each
`LatticeCell` draws its own right and bottom. Assembling it this way — rather than with
`border-collapse` or a background grid — is what lets a cell invert to solid on hover
without a seam appearing along its border.

It sizes against its **own container**, so a lattice dropped into a narrow column
collapses from three to two to one without a viewport query.

```tsx
<Lattice columns={3}>
  <LatticeCell index="01" title="Role + responsibility">…</LatticeCell>
  <LatticeCell index="02" title="Identity + access">…</LatticeCell>
  <LatticeCell index="03" title="Self-built workflows">…</LatticeCell>
</Lattice>
```
