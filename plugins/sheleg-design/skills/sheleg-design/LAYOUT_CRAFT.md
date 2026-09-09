# Layout craft — composition, observed rather than dialled

Layout advice fails when it ships as uncalibrated axes — "density 7", "rhythm
high" — numbers nobody can check against a screen. This file replaces the dials
with OBSERVABLE composition: what a squint shows, what proximity does before a
container is drawn, and how a layout survives the world changing under it. A
fix here always names **the concrete priority that was lost**, never an
arbitrary dial value. **Density is derived from the task and the device, never
assigned by brand category.**

## The squint test and focal order

Blur the screen (squint, or a 4px blur in a capture). What survives IS the
hierarchy: the first, second and third thing the blurred frame shows are the
focal order the layout actually ships — regardless of what the design intended.

- Observable sign: **one dominant region** survives the squint; two equally
  loud regions mean the screen has no first thing.
- The fix is stated as the lost priority: *"the primary action is not first in
  focal order — the promo panel outweighs it"*, never *"reduce visual weight to
  4"*.

## Proximity before container

Group by SPACE first; draw a box only when spacing alone cannot carry the
grouping. Every container costs a border/fill the eye must discount.

- Observable sign: remove the box in a copy — if the grouping still reads (gap
  within < gap between), the box was decoration; keep it removed.
- **Card, table and grid are all admissible when they do the task's job** —
  a table is not "too dense" for a brand, and a card is not "too soft" for an
  operator tool; the task decides.

## Density is not rhythm

- **Density** = information per viewport: how many decisions the screen offers
  at once. Observable: count actionable/readable units in one viewport.
- **Rhythm** = the regularity of spacing steps: whether gaps come from one
  scale. Observable: the set of distinct gap values on screen — five unrelated
  gaps is broken rhythm even on a sparse screen; a dense operator table with
  two gap values has perfect rhythm.

A dense screen with clean rhythm is calm; a sparse screen with random gaps is
noisy. The two axes move independently, and a critique that says "too dense"
when it means "arrhythmic" prescribes the wrong surgery.

## Adaptation — the world changes under the layout

Checked on a render, per `VISUAL_REVIEW.md` — **source alignment alone is not
proof; optical correction is verified on the rendered frame**:

- **Container**: the layout reflows at container widths, not only page widths;
  a sidebar's card is the phone's card.
- **Zoom**: 200% browser zoom loses no content and no action (reflow, not
  clip).
- **Locale**: the longest shipped locale (German compounds, long Cyrillic)
  fits every label; RTL mirrors the reading order, not the icons' meaning.
- **Keyboard**: focus order follows the VISUAL order — DOM order and focal
  order are the same walk; a grid that reads left-to-right but tabs
  column-first has a broken agreement between DOM and layout.

## Three independent decision pairs — worked, not packaged

Each pair shows the same decision resolved differently BY TASK. These are
composition examples, **not styles and not packs** — do not promote them into
named presets:

| Situation | Decision A | Decision B | What decides |
|---|---|---|---|
| dense operator surface | table, 2 gap values, row hover, no cards | cards with 8px gaps | A when the task is scanning 50 rows for one anomaly; B loses ~70% of rows per viewport |
| editorial read | one column, 65ch, generous leading, no chrome | two-column magazine grid | A when the task is uninterrupted reading; B when the task is browsing among pieces |
| mobile action | one primary action pinned bottom, content scrolls | all actions inline at their objects | A when one action closes the task; B when actions are per-item and the list is short |

## Optical correction

Perfect source geometry can look wrong: a mathematically centred triangle icon
sits left of optical centre; equal padding around a circle looks unequal next
to a square. The correction is a deliberate, small offset — and **it is proven
on the RENDER** (a capture per `VISUAL_REVIEW.md`), because the whole point is
that the source numbers and the perceived result disagree. "The values align in
CSS" is the claim the correction exists to overrule.
