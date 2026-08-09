# Maquette — the contract this design system ships under

**Register.** Choose Maquette for **enterprise data infrastructure sold to an
architecture buyer**, where the reader must understand a structure before they
can evaluate it. The subject is a built object: an axonometric model in cream,
labelled block by block, lit on a near-black table.

**The fork against `instrument-console` is the one people get wrong**, and it was
tested before this pack shipped. Both are near-black with one pale accent and
mono labels, and on product category they overlap completely. The test is not the
category — **does the page have to render a number that changes while the reader
watches?** Yes → `instrument-console`. No, but the reader must decompose a
structure → this pack. A cockpit answers *what is happening now*; a maquette
answers *what is this made of*. Build every screen against `var(--…)` and never a
literal.

**The ink is cream, and every tool will try to make it white.** `--ink`
`#FFF9F4` is the same cream the model is built from, so type and object read as
one material under one lamp. `#FFFFFF` measures *better* (18.4:1 against 17.49:1)
and is wrong — the page's whole coherence is that the type and the model are the
same stuff.

**The accent works as text**, at 15.49:1 — unusual in this library. Under it,
**black** at 17.81:1, never the cream, which falls to 1.1:1. And the focus ring
on an aqua fill is `--ink`, because aqua on aqua is nothing.

**One shadow, and its direction is not adjustable.** `12px 24px 24px` at 25% —
displaced on both axes, one upper-left light for every block. A centred shadow
turns the model from an object on a table into a card in a stack.

**The model does not move.** No parallax, no rotation, no exploded view on
scroll, no hover highlight. A measurable object that drifts stops being
measurable, and an exploded view on scroll is the most tempting and most damaging
thing you can do to this pack.

**Status is a pack decision, not a measurement.** The reference exposes no status
palette; these four are derived, the token layer says so, and green still sits
6.4 from red under deuteranopia. Every status carries its word.

**Bans** (verbatim from the pack):

- Moving the model. Parallax, rotation, exploded views, scroll-linked assembly,
  hover-to-highlight.
- Perspective. Axonometric or it is a different pack.
- `#FFFFFF` as ink; the cream as a label on an aqua fill.
- A gradient on a model face; a drawn stroke where the field colour belongs.
- A second drawing on the page; an unlabelled block.
- Widening the dark family.
- A status mark without its word.
- A rectangle where a pill belongs, or a pill where a panel belongs.
- `transition: all`; `100vh`; a scroll listener; fluid `clamp()` type.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack.
