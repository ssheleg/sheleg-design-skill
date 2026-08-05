---
category: Data
---

A figure on the paper with no tile around it — no fill, no border, no slab. The
pack composes with hairlines, so a stat that arrives in a box is a component from
another kit. The label is mono at 11px and `0.16em`; the value is the **display**
face at 40px with tabular figures; the source sits underneath in Geist.

That split is the pack's own inversion and the thing to get right: **mono here
means annotation, not number.** In `workbench` mono says *this is data*; in Field
Notes mono is furniture — eyebrows, section numbers, version strings, provenance
tags — and the number itself is set in the display face like the headline it
supports.

`source` is optional in the type because the spine is identical in every kit. It
is not optional in this pack: *a claim with no source in the same block* is on the
ban list. Name the run, the window, the query or the person.

```tsx
<Stat value="1 204 883" label="Edges resolved" source="full index · 2026-08-04" />
<Stat value="98.2%" label="Call sites matched" source="static pass · main@4f2a91c" />
```
