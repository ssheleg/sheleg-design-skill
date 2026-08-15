# Ledger — the rules this design system is built on

A warm cream console for a product whose answers must be checkable. The field is
paper, elevation is a hairline at 12% ink, and the one accent labels rather than
fills. Extracted from a production reference (basedash.com, 2026-08-15); the full
pack, with every measurement and every trap, is `styles/ledger.md` in the
sheleg-design skill.

**This is the static half of a pack.** Motion does not cross this boundary: build
screens from these components, never a scroll narrative around them.

## Bans — what this system never does

- **The accent never fills a control.** No orange button, no orange tab, no
  orange toggle. The primary button is filled in `--ink`. The accent labels,
  marks, strokes a chart and rules a selected edge.
- **No shadow on a card.** Elevation is a 1px hairline at 12% ink. One shadow
  token exists, for true overlays only, and there is no second one to reach for.
- **No second accent hue**, and no semantic colour used decoratively. The chart
  ramp is the one place five hues coexist, and a series there is labelled at its
  own mark — never by a legend alone.
- **Status is never by colour alone.** Every status ships a word, a sign or a
  glyph beside the colour: four of the five semantic colours sit under 4.5:1 on
  the light field and two under 3:1.
- **No spinner where tokens can stream**, no fake typing delay, no invented
  confidence number, and no single red state covering refusal, rate limit and
  crash.
- **No serif, no fourth family, no weight 700.** Display face for one line per
  page, UI face for the interface, monospace for all data.
- **No gradients on a surface, no grain, no glass, no illustrations, no emoji.**
- **No cinematic motion**: no scroll clock, no parallax, no scrubbing. Three
  loops are legal and all three are state — a typing cursor while tokens stream,
  thinking dots while a run works, a 1.4s heartbeat on a live indicator — and all
  three stop under reduced motion.

## Geometry

Radii are 7.5 / 10 / 15 / 20 and a pill, and they nest **concentrically**: an
inner radius is the outer radius minus the padding between them. A 15px track
with 4px of padding holds a 10px thumb, never a second 15.

Rows are 32px, controls 30px, fields 38px. The grid is 4px.

## Type

Display `--font-display` (licensed; point it at `--font-ui` without one), UI face
Inter at 400/500/600, and the system monospace for **all** data — ids, metrics,
timestamps, row numbers, SQL, chips, logs — with tabular figures wherever digits
align. The large figure on a stat tile is an exception the reference makes: it is
the UI face at 34px, not the monospace.

## Provenance is the point

Every card that states a number carries a `Seal` saying how the number is known:
`verified` when it came from a definition the reader can open, `inferred` when
the system derived it by a step it can name, `unverified` when it cannot. Every
state must be reachable, the label must be derivable from something real, and it
seals a card rather than a screen.
