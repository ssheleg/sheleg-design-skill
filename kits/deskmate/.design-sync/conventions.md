# Deskmate — conventions for a design agent

This kit is the built form of the Deskmate style pack. Read these before generating
anything with it; they are the pack's bans, stated where a design tool will see them.

## Geometry

- **A control is a pill.** `--r-pill` on anything a hand touches, at `--control-h`
  (56px) or `--control-h-sm` (40px), never below `--tap-min` (44px).
- **A container is a slab** at `--r-card` (32px). Sections and the navigation slab take
  `--r-section` and round their **bottom** corners only — nothing here rounds a top
  corner against the page edge.
- **The frame is concentric**: `--r-frame` outside, `--frame-inset` of padding, and
  `--r-frame-inner` = `calc(--r-frame - --frame-inset)` inside. Never the same radius on
  both boxes.

## Colour

- One accent, `--accent`, which both writes and fills. `--peach` is a gradient stop and
  a mark; it is never a word.
- **One ramp**, `--gradient-dusk`, and its origin is always above the top edge of the
  box it fills. A gradient lit from below is not this pack.
- **One gradient word per heading** and one gradient control per page. The word carries
  `--gradient-word-fallback` as a solid `color` first, or it disappears where
  `background-clip: text` is unsupported.
- **Status is never by colour alone.** Every state takes a word or a glyph beside its
  colour, on the light field and on the dusk surface.
- `[data-surface="dusk"]` is a **surface variant, not a dark theme**. Put it on a
  section, never on `:root`, and leave the frame alone — it re-declares its own tokens
  on purpose.

## Type

- `--font-display` for headings only, at `--weight-regular` for the display and
  `--weight-strong` for a section heading, always at `--track-display`.
- `--font-body` at **`--weight-body` (500)** for every sentence. An unset weight gives
  400 and renders the whole page one step light.
- `--font-quoted` only inside the frame. It is the chat client's face, not the brand's.

## Motion

- Two clocks: `--dur-fast` for anything a pointer caused, `--dur-enter` on `--ease-out`
  for anything the scroll revealed. No scroll clock, no parallax, no `animation-timeline`.
- No shimmer on a skeleton.
- Reduced motion collapses every duration and `--enter-y`: colour still changes, nothing
  travels.

## Breakpoints

A component sizes against its own box. `container-type: inline-size` on the root and
`@container` on the descendant; a viewport query is only for the page's gutter and the
display's own size, and both are marked in the stylesheet with the reason.
