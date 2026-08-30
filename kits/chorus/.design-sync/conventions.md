# Chorus — conventions for a design agent

This kit is the built form of the Chorus style pack. Read these before generating
anything with it; they are the pack's bans, stated where a design tool will see them.

## Colour

- **The coral fills and never writes.** `--coral` (#f96f4b) is a fill, a flat block, a
  gradient stop and an icon beside a label that carries the meaning. As a word it is
  2.72:1 on the field; under a white label it is 2.84:1. Both are below the 3:1
  large-text floor, so no size rescues either. A coral word takes `--coral-ink`
  (#cb441f, 4.59:1 on the field).
- **The primary button's label is INK**, `--on-coral` at 6.20:1. This is the pack's
  correction to the reference and it keeps the brand hue exactly rather than darkening
  it.
- **The mint lives only on the dark.** `--good-on-dark` (#36ff94) is 13.31:1 in a
  well and does not exist on paper — held at its own hue it reaches AA on paper only
  at near-black. A green figure on a card takes `--good` (#198400).
- **Status is never by colour alone.** `--good` and `--danger` are 6.2 apart under
  deuteranopia. Every delta ships its arrow and its number, both.
- **There is no warn.** Three status roles. The reference declares an amber that paints
  nothing; a fourth severity here would be invented.
- The periwinkle is a gradient stop and a series line on the dark. It is not a second
  button colour and never carries a word on paper.

## Surface and edge

- A card is `--surface` at `--r-card` with a 1px `--line` — **32px padding and 32px
  gap at every width**, including 390. Do not tighten it on narrow screens.
- Four objects carry a shadow and nothing else may: the bubble, the floating panel,
  the hero deck, the nav. Everything else takes `--line` for its edge.
- The construction grid never switches off, and it continues across the dark slab.
  The plus at each intersection is part of it.
- The dark slab is a **surface**, not a theme. The page never inverts.

## Type

- Outfit sets two things: the display, and the question inside a bubble. Nothing else.
- Display tracking **relaxes** as the type shrinks. Do not tighten a small display.
- Body line-height is 1.7. No italic anywhere; nothing above weight 700.

## Geometry and motion

- `--r-bubble` is 24px on three corners and 0 on the top right. It is the pack's whole
  geometry, and it belongs to one object.
- Nothing lifts, scales or parallaxes; there is no scroll clock; gradients do not move.
- Loading is a static skeleton, never a spinner and never a shimmer.
- The reduced-motion contract has a JavaScript half: a reveal observer must read
  `matchMedia('(prefers-reduced-motion: reduce)')` and mount at the final transform.
  The media query in the token layer cannot reach a transform a script sets.
