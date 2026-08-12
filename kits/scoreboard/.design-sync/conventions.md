# Scoreboard — the contract this design system ships under

**Register.** Choose Scoreboard for a product whose argument is **an
accumulating number**: performance marketing and ads operators, SEO and growth
tools, revenue dashboards sold on results, agency-replacement services. The page
is a running tally — a dated column of figures the product already produced, with
the label on the left, the number on the right, and a line of dots between them.
The fork people get wrong is against `field-notes`, which shares the warm paper
and the orange-red accent: there the numerals are mono and make evidence
*auditable*; here they are pixel and make results *countable*. *How do you know
that?* goes there. *How much, and since when?* stays here. Build every screen
against `var(--…)` and never a literal.

**The accent is a mark, not a voice — and neither is the other orange.**
`--accent` `#FF4801` measures 3.23:1 on the paper and `--accent-hover` `#E03D00`
measures 4.12:1; **no orange in this system reaches the WCAG AA floor for a
word.** The accent is the 3×18px tick, the list marker, the focus ring and the
link underline — and, filled, a selected chip, where `--on-accent` sits on it at
4.92:1. A link is `--ink` with an `--accent` underline, never orange text.

**The focus ring is solid.** 1.13.0 shipped the reference's translucent
`focus-within` glow, which composites to 1.29:1 against the paper — decoration
wearing an affordance's name. `--ring-focus` is now a solid 2px accent ring, and
`--ring-focus-sand` is the ink ring for `--surface-sand`, the one surface where
the accent misses the floor.

**The status chip has no fill.** The word carries the colour on the surface it
sits on. A 10% tint under an 11px `--warn` label lands at 4.38:1, under AA — and
a chip whose whole job is to be the secondary encoding cannot itself be the
thing that fails.

**The action is ink.** `--action` `#0A0A0A` with a white label is the primary
button. This is measured off the reference, and it is why the accent survives:
the loudest colour on the page never competes with the thing you are meant to
click. A view with an orange CTA has two primaries and no accent.

**Status is never by colour alone.** The paper statuses cluster — the accent and
`--warn` separate by only 6.3 under protanopia, `--danger` and `--warn` by 12.6
at full colour. Every status is therefore a chip containing its word, which is
why `StatusChip` takes `label` as a required prop rather than an optional one.

**There are two status sets, not one.** On paper use `--good` / `--warn` /
`--danger` / `--info`; on a `data-surface="panel"` element use the measured
`--*-on-dark` values. The dark set measures 1.6–2.6:1 against the paper and the
paper set disappears on the panel. `StatusChip` takes `onPanel` for exactly this.

**Radii are two and three pixels.** Across the reference, 107 of 143 radius
utilities are 2px or 3px. At 8px everywhere this becomes a generic product page
with an orange tick on it. When containers nest, an inner radius is the outer
minus the padding between them.

**Bans** (verbatim from the pack):

- The accent as body text, a heading, or a button fill.
- A second ledger on the page, a ledger with a rounded marketing number in it,
  or a ledger with no date under it.
- Antialiased pixel type. Without smoothing off, the numerals are a novelty face.
- A bare status dot, and any status carried by colour with no word beside it.
- The paper status set on the dark band, or the dark set on paper.
- Radii above 8px, and any radius on the ledger's own rows.
- A spinner where a number will land. The skeleton is the row.
- Fluid `clamp()` display type; `transition: all`; a second accent; a gradient
  anywhere except the hero's wash.

**The body size is 15px and the numeral column is fixed.** Press Start 2P has no
currency width worth trusting: budget the column in pixels (80px, 70px below the
medium breakpoint) and right-align it.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves — the entrance, the scan line, the
count-up — stays behind in the pack.
