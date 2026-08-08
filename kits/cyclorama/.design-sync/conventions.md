# Cyclorama — the contract this design system ships under

**Register.** Choose Cyclorama for **a company selling transformation to an
executive buyer**: enterprise AI, AI-transformation and applied-AI services,
technical consultancies whose argument is *we install this and your business
starts running differently*. It suits a product with no screenshot worth showing,
where the thing being sold is a change of state. The fork people get wrong is
against `field-notes`: both are warm, light and monospace-voiced, but that pack
is a **ruled document** selling *auditability* and nothing in it moves, while this
one is a **stage** selling *transformation* and the field itself is the motion.
Route by what the product's argument rests on — *how do you know?* takes
`field-notes`, *watch this change* takes this pack. Against `workbench`: a field
that recolours under you is a defect on a screen held for an hour, so dense
product UI goes there, not here. Build every screen against `var(--…)` and never
a literal.

**The field is not a colour.** It is a 32-second, six-stop, infinite loop, and
the ink never moves with it. Every contrast figure in this system is stated
against the **worst** stop, `--field-2` at 12.79:1 — not against a representative
one. When you prove a screen, prove it there. `FieldStop` exists to make that
possible; the animation itself is not part of this design system, because a kit
is the static half of a pack.

**The accent rule, and it is the one that gets broken.** `--accent` `#FF8C00` is
a **fill, a dot and a chart series — never text on the field.** As text it
measures 1.71–1.97:1 across the six stops. The reference itself paints its
section eyebrows that way and it fails WCAG at every stop; this system does not
propagate it. Eyebrows take `--ink-soft` at 8.36:1. And there is no darkened
orange to reach for instead: the warm-dark region is already occupied by
`--warning` and `--danger`, so every text-capable orange collides with one of
them — `#903A00` sits 4.6 from `--danger` against a hard floor of 10. There is no
text-safe orange in this palette. Ink on the accent is fine at 7.46:1, which is
what `--on-accent` is for.

**Status is never by colour alone.** `--good` and `--danger` separate by 7.2
under protanopia and 5.9 under deuteranopia; `--signal` and `--accent` by 6.8 and
6.7. The floor is 8. Every status therefore renders as a mark **plus its word** —
which is why `StatusPill` takes `label` as a required prop rather than an
optional one. An API that let you omit it would be an API that lets you ship the
bug.

**Bans** (verbatim from the pack):

- `--accent` as text on the field. Also banned: a darkened orange invented to get
  around it — there isn't one.
- `--signal` as text, and any status rendered as a mark without its word.
- A shadow. Anywhere. Elevation is a hairline; there is no `--shadow-*` token
  because there is nothing for it to describe.
- A fill on the app window; a second opaque surface beside `--surface` and
  `--panel`; a gradient of any kind.
- `transition: all`, which the reference itself declares and this pack refuses.
- A proportional display face — Zilla Slab, Bitter, Fraunces or any serif that is
  not monospaced. The hero is laid out per character; a proportional substitute
  does not restyle it, it breaks it. Use Courier Prime.
- A sticky nav, a scrolled nav shape, or a backdrop blur.
- `100vh`; a scroll listener where the scroll store belongs.
- Scrubbing the field cycle to scroll position, or adding a second continuous
  loop beside it.
- A third font family. Urbanist is vestigial, not an invitation.
- Pure black or pure white as ink; white as a label on an ink fill, where the
  field colour belongs.

**Radius arithmetic.** An inner radius is the outer radius minus the padding
between them, never the same value twice. The reference gets this right and it is
worth copying exactly: a 16px window with 12px of padding holds 4px chips.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack. The
cycle is six surfaces here, not an animation.
