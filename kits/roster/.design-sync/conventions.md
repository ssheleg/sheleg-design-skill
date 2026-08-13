# Roster — the design contract

The reference is <https://www.babylovegrowth.ai/en>, measured 2026-08-13 off computed
styles at 1440×900 (5,936 rendered elements), 768×1168 and 390×790. The full pack is
`styles/roster.md`; this file is what a design agent must not get wrong.

## The one thing this pack is

**The proof is a name, not a number.** A white field in a faint grid of squares, hairlines
instead of shadows, and an argument made entirely of other people's marks: an engine's
wordmark inside the headline, client logotypes in six pill-labelled industry columns, a
review score somebody else computed.

## Non-negotiable

- **Never white on the accent below large text.** `#fa5c12` is 3.18:1 on white and the
  reference's own nav pill puts white on `#f25533` at 16px/600 — **3.43:1**, its one clear
  failure. The accent is a fill and a large-text colour; `--accent-ink` (4.52:1) carries a
  word.
- **The primary action is black.** `--cta` at 19.66:1, which is what the reference itself
  uses for the hero.
- **No elevation system.** The reference's shadow slot holds an all-transparent ring
  composite on 101 elements. Separation is hairline (`--rule`, on 7,234 borders) and pill.
- **The display is set in the body face** at 68px, and the section heads in the *other*
  family at 52px. That inversion is the pack.
- **Body weight is 300.** A very long page (13,627px at 1440) stays light because its
  paragraphs are.
- **The display steps, it does not slide** — 36 / 60 / 68 — because neither stylesheet
  contains a `clamp()`.
- **Status never by colour alone.** `--accent` and `--danger` are 10.2 apart at full
  colour against a hard floor of 10; a danger state always carries its word or icon.
- **`:focus-visible` is `--accent-ink`**, never `--accent`.

## Banned

- White on the accent at body size. A shadow used as elevation. A scroll clock — the
  reference has none: zero `animation-timeline`, `scroll-behavior: auto`.
- **An invented `--warn`.** The reference paints no amber anywhere.
- **A hidden `h1`.** The reference's is `.sr-only` at 1×1px and all sixteen of its `h2`s
  are eyebrows; this kit keeps the outline and the page in agreement.
- **A tidied roster.** No equalising logo sizes, no single-colour tinting, no dividerless
  wall. Greyscale at rest is the only normalisation.
- **Pixel numerals.** The biggest figure on the reference is set in a 16px eyebrow; a
  number as the subject is `scoreboard`, not this.
- A dark theme. None was measured.

## Container queries, not viewport ones

`IndustryColumn` and `StepCard` each set `container-type: inline-size`, and their
breakpoints are derived from their own geometry rather than carried over: 220px for the
column's two-up mark grid, 640px for the step card's split. Only the display's three
steps stay viewport rules, and they are marked `PAGE` at the block.

## Motion

Entrance and hover, plus two floats at 5.5s and 6.5s offset by a second so the pair never
syncs. Every transition runs on `--ease`. Under `prefers-reduced-motion` the durations
collapse in the token layer and the floats are **paused** in the component layer — a
duration cannot stop an infinite animation, it strobes it.

The reference's own reduced-motion branch names six classes and leaves roughly fourteen
animations running. Do not copy that shape.
