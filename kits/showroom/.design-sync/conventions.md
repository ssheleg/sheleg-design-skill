# Showroom — the contract this design system ships under

**Register.** Choose Showroom for a **product-led company whose best argument is
the product on screen**: CRMs, planning tools, analytics, developer platforms
with a real console. The first viewport carries a claim and then the application
itself, at real size. The fork people get wrong is against `workbench`: that pack
**is** the tool and is meant to disappear; this one is the page **arguing for**
the tool, and its product surface is a specimen under glass. Build the dashboard
in `workbench`; build the page that sells it here. Build every screen against
`var(--…)` and never a literal.

**The palette came from CIE Lab.** The reference declares its colours in
`lab()`; every value in the token layer was converted by painting the declared
colour into a canvas and reading the sRGB bytes back. The colour is unchanged —
only its notation is. Do not re-convert with a different method: the greys sit
close enough together that a shade off is visible in a stack of hairlines.

**One blue, and it is symmetric.** `--accent` `#266DF0` measures 4.64:1 as text
on the field *and* 4.64:1 under white. It is the link, the focus ring and the
filled button, with no second token and no "on-dark" variant. Do not add one.

**Status is never by colour alone.** `--good` and `--danger` separate by 33.7 at
full colour and by only **4.9 under deuteranopia**. Every status is a chip
containing its word — which is why `StatusChip` takes `label` as a required prop
rather than an optional one.

**`--disabled` is not a caption colour.** The reference names `#A4ADBA`
"caption-foreground" and it measures **2.27:1** on its own white field. It is
kept for disabled controls and placeholder text, neither of which is content.
Captions take `--ink-soft` at 7.7:1.

**Bans** (verbatim from the pack):

- A second specimen. One per page.
- Scaling the specimen to fit. Crop it.
- `--disabled` as a caption, label or meta colour.
- A bare status dot with no word; a status colour used for anything that is not
  a status.
- A shadow inside the specimen; a hairline used to lift something outside it.
- A second accent, an "accent on dark" variant, or a gradient anywhere except
  the hero's seating wash.
- A serif. Tiempos is on the reference and is not in this pack.
- Fluid `clamp()` type; a hardcoded radius; `transition: all`; `100vh`.
- Parallax, tilt, or scroll-linked scale on the specimen.

**The body weight is 500, not 400**, and Inter Display is a different face from
Inter. Both are easy to get wrong and both flatten the page.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack.
