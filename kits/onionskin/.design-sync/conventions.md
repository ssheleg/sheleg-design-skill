# Onionskin — the contract this design system ships under

**Register.** Choose Onionskin for **developer and AI infrastructure whose front page is
a working document**: memory and context engines, retrieval and embedding services,
agent runtimes, evaluation and observability surfaces. A white technical sheet at 96.5%
zero radius, ruled by hairlines, over a dot grid. Build every screen against `var(--…)`
and never a literal.

**Two bases, and everything quiet is one of them at an alpha.** Text dims through
`--ink`; structure dims through a navy that is never a word. There is **no grey ramp in
this pack** — introducing `#6b7280` here introduces a third base and dissolves the whole
construction. 199 of the reference's 631 colour-carrying values carry an alpha, from
exactly two bases.

**An alpha composites in sRGB, not in linear light.** `--ink` at 60% is 4.98:1 and
passes; computed in linear space the same value reads 2.32:1 and looks like a failure.
Every ratio in the token layer was computed the way a browser composites.

**The navy is never a word.** At its working alpha it is 1.21:1. It rules and it edges.

**A rule is never the only separator.** At 1.21:1 a hairline is below every floor there
is, so the region it bounds must ALSO change field, gain a label, or gain space. This is
a ban, not a preference.

**Elevation is an edge.** `--edge-lit` — the accent at 28%, inset on the left and right
— marks the one panel per section that is the subject. `--shadow-lift` appears once on
the reference and should appear once on your page. A panel never floats.

**The working size is 11px.** It is the most frequent size on the reference at every
width, and it carries labels, keys, annotations and mono data. Setting it at 13px "for
readability" turns this into a different pack; the density is the argument.

**Tracking is two-sided.** `--track-micro` (+0.18em) on the uppercase label,
`--track-display` (−0.05em) on the display. Collapsing them loses the page's texture.

**Three faces, one job each.** Space Grotesk displays, DM Sans carries every sentence,
DM Mono carries every number, key and identifier. Nothing crosses: a number in the sans
or a sentence in the mono and the page stops reading as a document.

**No bold.** 500 is the ceiling at scale — 205 nodes against 400's 175, with 600 on
seven elements and 700 on four.

**No radius above 5px.** 1,418 of 1,469 rendered elements are square.

**The dot grid is a field.** Under a section, never inside a panel, never a border, and
its 24px step does not rescale at narrow widths.

**The accent needed no correction.** `#0562ef` is 5.25:1 on white and 5.25:1 under
white — one token for the fill and the word.

**Status is never by colour alone**, on either field, and the dark band carries its own
four because the light set measures 1.4–2.6:1 there.

**`[data-surface="dark"]` is one section, never the document.** Its rules invert base
rather than alpha — white at 14% instead of navy at 10% — because a navy at 10% over
near-black is nothing at all.

**Every control clears `--tap-min` (44px).** A correction: 88 of the reference's 123
interactive elements at 1440 are shorter, and 73 of 106 at 390.

**Nothing travels in space.** No parallax, no scrub, no `animation-timeline`, no press
translation. `MOTION_INTENSITY` above 2 has nothing legal to buy, and reduced motion
collapses every duration to zero.
