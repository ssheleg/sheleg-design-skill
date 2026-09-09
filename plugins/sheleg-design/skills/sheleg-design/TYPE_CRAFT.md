# Type craft — the portable half of typography

What makes text READ well is portable across every pack: roles, hierarchy,
measure, loading and the content that breaks pretty demos. This file carries
that half. What face a pack chooses is the pack's own signature and lives in
its style file — **there is no banned-font list here, and no font is fetched to
follow this reference. One font family — or the system face — is a complete
answer when it does the brief's job.**

## Semantic text roles

Text is styled by ROLE, never ad hoc: `display`, `heading`, `body`, `caption`,
`label`, `code`, `numeric`. A role maps to the pack's tokens; a screen invents
no new role mid-layout. Two visually different headings with one role are a
theme decision; one visual style shared by two roles is a collision waiting for
a redesign.

## Relative hierarchy

Hierarchy is a RATIO ladder, not a pixel list: each level relates to `body` (a
modular scale, or the pack's declared steps), so the whole ladder moves when
body moves. A jump of less than ~15% between adjacent levels reads as noise,
not hierarchy — merge the levels or widen the step.

## Measure, leading, weight, width

- **Line length**: 45–75 characters for body prose (30–50 for narrow columns);
  past ~90 the eye loses the return sweep. Set it in `ch`/`em`, not px.
- **Line height**: body ≈ 1.4–1.6; headings tighten as size grows (≥1.1);
  never below 1 for multi-line text.
- **Weight**: hierarchy prefers ONE family varying weight/size over a second
  family; two weights apart read as different, one apart reads as a rendering
  glitch.
- **Width (condensed/expanded)**: a width axis is a display device; body text
  stays at normal width.
- **Numeric alignment**: tabular figures (`font-variant-numeric: tabular-nums`)
  for any column of numbers; lining figures in tables and UI; never let
  proportional oldstyle figures wobble a total column.

## Checks against reality — run, not assumed

- **Real font loading**: verify the face actually rendered (a capture before
  webfonts settle shows fallback metrics — a different layout;
  `VISUAL_REVIEW.md` disqualifies such a frame). `font-display` is declared,
  and the fallback stack is a real stack, not a decorative one.
- **Fallback parity**: the fallback face is metric-compatible enough that
  nothing reflows into truncation when it renders.
- **Missing glyphs**: test the actual character set — Cyrillic, the currency
  signs, arrows, the letters of every shipped locale. A tofu box in production
  is a failed check, not a font quirk.
- **Long strings**: German compounds, long Cyrillic words, RTL runs and long
  numbers go through every label and button. **Content is never shortened to
  keep a demo pretty** — the layout accommodates (wrap, truncate WITH title,
  or widen), the string stays.
- **Native text scaling**: the layout survives the platform's own text-size
  settings (Dynamic Type, Android font scale) up to at least 1.3× without
  clipping.

## Scoped fixes — before → after

Each fix names its scope; none requires a new font, a CDN, or a fetch:

| Before | After | Scope |
|---|---|---|
| body at 92ch full-width | `max-width: 65ch` on the prose block | one container |
| totals column wobbles | `font-variant-numeric: tabular-nums` on the column | one role (`numeric`) |
| heading ladder 14/15/16px | ratio steps off body (e.g. 1.25 scale) | the pack's scale tokens |
| label clips «Betriebsanleitung» | wrap to two lines, min-width on the label | one component |
| second family for emphasis | same family, one weight step up | one role |

**Licensing and any NEW font connection are per-brief decisions, outside this
baseline** — this reference never obliges one.
