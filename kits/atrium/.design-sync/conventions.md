# Atrium — the contract this design system ships under

**Register.** Choose Atrium for **consumer health and premium care**: longevity
and diagnostics, wellness and testing subscriptions, clinics and telehealth,
insurance alternatives, high-trust DTC where the buyer must feel both *this is
medically serious* and *this will not frighten me*. It generalizes to any premium
consumer subscription that sells calm authority rather than speed. The defining
constraint is the field: **one continuous cream page, no dark bands**. Sections
are separated by `--section-y` rhythm and a change of layout, never by flipping
the background — the inverted `--surface-ink` surface appears once or twice on a
whole page and always for a reason. Elevation is a hairline plus a cream step,
not a shadow.

**The accent rule.** There is exactly one accent — terracotta `--accent`, one per
page — and text on it is `--accent-ink`, the field's own beige, never white. The
accent changes grade with its ground: 4.6:1 on `--bg` and only **4.2:1 on
`--surface`**, so accent text is a field-only device and inside a cream card it
must go up to large-text size or become `--ink`. `--good` and `--info` are fills
and icons, never words; `--danger` is the one semantic that may be text. The
pack's entire emphasis vocabulary is one italic terracotta phrase inside a serif
headline — one per heading, never two in a viewport, and never bold, a highlight
fill or an underline instead.

**Bans** (verbatim from the pack):

- A dark section used as a rhythm device; alternating light/dark bands; any
  second inverted surface beyond the one the page has earned.
- A second accent hue. Green, blue and red are semantic fills with fixed
  meanings and no decorative use whatsoever.
- White (`#FFF`) as a surface or as text on the accent; true-neutral grays
  beside the warm ones.
- The serif at any weight but 300, the serif in ALL CAPS, or the serif below
  ~27px (`--t-h4`); mono anywhere except the motion controls.
- `transition: all`; scaling or lifting a button on hover; hover states on
  static cards.
- **Autoplaying motion without a visible pause control.** A marquee, a rail, or
  a shader that a user cannot stop is not shippable in this pack —
  `prefers-reduced-motion` alone does not discharge it, because the people who
  most need to stop the motion are frequently not the people who set that flag.
- Icon grids, illustration sets, mascots, stock 3D, gradients as decoration
  (the accent card gradient and the hero scrims are functional and are the only
  ones).
- An unsourced number, a claim without an attributed name, or a testimonial
  without a person attached to it.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, so the fluted-glass hero, the marquees and the 7.2s slide
cycle stay behind in the pack. `MotionToggle` is here because the control itself
never moves — it is the one part of that vocabulary that crosses, and the pack
requires it beside every motion the page does run.
