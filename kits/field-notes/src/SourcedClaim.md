---
category: Signature
---

A claim and the name of whoever produced it, in one block. `source` is
**required** — not a footnote, not a superscript, not a tooltip. On a pack whose
product is provenance the attribution is the argument rather than decoration, and
moving it to the bottom of the page is how a provenance product quietly stops
being one. The pack's ban list says it plainly: *a claim with no source in the
same block*.

`provenance` renders a `ProvenanceTag` inline right after the claim, which is
where the tag belongs. The source line is mono at 10px in `--ink-soft`, and the
`<cite>` is reset to `font-style: normal` because italic is banned pack-wide: the
display face has none, so a browser would synthesise a slant.

Use it for sentences. For a figure, `Stat` is the same discipline applied to a
number.

```tsx
<SourcedClaim source="static pass · main@4f2a91c" provenance="extracted">
  Every call site in this package resolves to a definition in the graph.
</SourcedClaim>
<SourcedClaim source="type inference · 3 hops" provenance="ambiguous">
  Two candidate definitions survive for the dynamic dispatch in loader.ts.
</SourcedClaim>
```
