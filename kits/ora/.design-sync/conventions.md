# Ora — the design contract

The reference is <https://ora.ai> and <https://journey.ora.ai> (era labs), read
2026-08-14 from the shipped stylesheet `/_next/static/chunks/feb8eaf5618096ba.css` and
the route bundles beside it. The full pack is `styles/ora.md`; this file is what a
design agent must not get wrong.

## The one thing this pack is

**A page that tells a person what a machine concluded about them.** A warm coal field,
cream ink, and no third hue — the accent is the inverted field. A serif carries every
human sentence and a monospace every machine fact. The only surface that leaves the
page plane goes *down*, into a terminal block cut below the field.

## Non-negotiable

- **There is no brand colour.** `--accent` is the ink: cream on coal, near-black on
  paper, 16.72:1 and 16.90:1 on their own fields. One filled element per view. A second
  filled button is a design error, not a variant.
- **No sans-serif.** `--font-sans`, `--font-serif` and the default family all resolve to
  Lora in the reference. Adding a real sans dismantles the rule the whole page is read
  through: a serif means a person said it, mono means a machine reported it.
- **Status is never by colour alone.** Every dot, bar and number in a status colour
  carries its word; the six-step grade ramp carries its letter. Under deuteranopia
  `--good` and `--danger` separate by 6.5 in dark and 7.4 in light, and under protanopia
  `--good` and `--warn` by 6.4 in light. In the light theme `--good` (2.13:1) and
  `--warn` (2.01:1) are below the non-text floor on paper and may not set text at all.
- **Elevation is a hairline.** `--border` at 1.15:1 is a seam. Shadows exist for things
  that float over the page — overlays, popovers, tooltips — and a card does not float.
- **The terminal is darker than the page**, in both themes, and never carries a shadow.
- **One radius root.** `--radius: 0.5rem`, and every other radius is a ratio of it:
  chip ×0.5, control ×1, card ×1.5, plus the pill. Do not add a step.
- **A layer that does not apply is hatched and reads `N/A`.** Never an empty bar — an
  empty bar reads as zero, which is a different verdict about the same product.
- **Motion is entrance, hover and two ambient loops.** No scroll-jacking, no parallax,
  no `animation-timeline`, no scroll library — zero occurrences of any of them in the
  reference's shipped bundles. Scroll drives two things only: the sticky nav's 1px
  hairline shadow and one pinned two-panel comparison. Hover changes colour, border and
  opacity and never geometry. Under reduced motion every duration token collapses to
  zero and the page keeps every value it was showing.
- **Numbers are `tabular-nums`, always.** A count that changes while the reader watches
  must not reflow.

## What this kit is not

It is the **static half** of the pack. The hero's breathing glows, the drifting agent
marks and the scroll-pinned comparison section are page-level motion and do not cross
into a component library. Nothing here invents motion to fill that silence.

## The traps the reference itself carries

Four of them, so a design agent does not reproduce them from a screenshot:

1. `--border-strong` is never re-declared for dark, so the reference paints a
   paper-coloured hairline at 12.02:1 on coal. This kit ships a dark value of its own.
2. `--shadow-pop` is a complete shadow in one scope and a bare colour in the other.
   Here it is always complete.
3. The reference's shadcn `--accent` is a raised *surface*, not an accent. The real one
   is `--accent-signature`, which points at the foreground.
4. The progress fill is animated with `transition-all`, which animates `width` and lays
   out every frame. Here it is `transform: scaleX()` from a left origin.
