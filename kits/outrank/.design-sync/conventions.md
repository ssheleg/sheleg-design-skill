# Outrank — what the design agent may not do

This pack is the seam between a landing that must convert and a tool that must be
worked in for hours. Both halves were measured off <https://www.outrank.so> and
its `/dashboard` on 2026-08-21; neither was invented.

## Bans, and each one has a measurement behind it

- **No shadow on a resting surface.** Elevation is `1px var(--panel-line)` at
  `--r-card`. A shadow in this pack means an overlay, and nothing else.
- **No status colour on a word.** `--info`, `--success`, `--danger` and
  `--warning` measure 3.34, 3.35, 3.32 and 3.80 on `--bg` — fills, dots and bars.
  When the state must be read, use `--info-ink` or `--success-ink`.
- **No second brand hue.** One violet, `--accent`. The status four are states.
- **No skeleton and no spinner** on a surface that has a previous value. Keep the
  value and date it with `Stat`'s `source` — the reference never blanks a drawn
  surface.
- **No serif.** Plus Jakarta Sans for what is read once, Inter for what is read
  all day, and no third family.
- **No scroll-driven motion.** The ceiling is 2 and the whole budget is a 0.15s
  colour transition. No parallax, no scrub, no entrance reveal.
- **The 5px ring is decoration.** It is 1.72:1 on `--bg` and may never be the
  focus indicator; `focus-visible` is a 2px `--accent` outline at 2px offset.
- **Do not adopt the Intergalactic vocabulary.** The reference's product half
  carries 384 `--intergalactic-*` tokens that belong to Semrush. This pack states
  the same values in its own role names; if you want that system, install it.

## The two shapes that are easy to get wrong

- **Two CTAs in a hero is one job with two doors** — an SSO button beside an email
  button — not two competing primary actions. Do not "fix" it to one.
- **A number is a shape.** `--t-metric` is 32px with leading equal to the size and
  −1.28px tracking. Do not lead a metric like prose.
