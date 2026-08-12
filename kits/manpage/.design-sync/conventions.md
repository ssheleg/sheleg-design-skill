# Manpage — the contract this design system ships under

**Register.** Choose Manpage for **a developer product whose buyer reads code for
a living**: an API, an SDK, a CLI, a protocol, an MCP server, developer
infrastructure. The landing page *is* the documentation, set in the typeface of
the documentation — the honest hero is not a screenshot but six lines of a request.
The fork people get wrong is against `datasheet`, which shares the off-white
paper, the hairlines and the one warm orange-red: there the page is about **the
reader** and its mono carries a reading the product produced (*what did you get?*);
here the page is about **the product** and its mono is the whole body face, showing
a call the reader will write (*what will you type?*). Build every screen against
`var(--…)` and never a literal.

**The display face is free, and that is the identity.** One webfont ships — a
single variable Geist Sans — and everything visible is set in `--font-mono`, which
is the **system** monospace stack: Menlo, Consolas, Monaco. There is nothing to
download for the face that carries the whole page, no swap window on the headline,
and the slight variation between machines is the point — it reads as the terminal
rather than as art direction. Substituting a webfont mono costs a render-blocking
request to look less native. Do not.

**The accent is a mark, a fill and a wash — almost never a word.** `--accent`
measures 3.61:1 on the field: enough for a non-text mark and for large text at 24px
and above, not enough at body size. Where a word must be coral, use `--accent-ink`
at 11.59:1. The primary button keeps the coral fill — the coral button *is* the
identity — but its label is `--on-action`, which is ink at 4.55:1, because white on
coral measures 4.16:1 and fails AA. `--action-strong` is the burgundy that carries
white at 13.34:1.

**The section heading is a chip, and the chip is a real heading.** `LabelChip`
wraps its span in an `<h2>`. That single decision is why the page keeps a clean
outline — one `h1`, one `h2` per section — while reading as a printed specification.
An eyebrow that merely sits above a heading is not this component and does not earn
the identity.

**The width ladder is the layout.** The argument runs in `--measure-text` (576px),
narrower than most prose; the hero and its code frame take `--measure-hero`
(768px); only evidence widens — `--measure-proof` for the testimonial grid,
`--measure-foot` for the footer, `--measure-wall` for the logo wall. Below 896px
every step collapses to `--measure-text` and the rhythm carries the structure
instead.

**Radii stay small and nothing is a pill.** 2px on the label chip, 6px on a
control, 8px on a button, 12px on a card, 16px on a panel. A fully round control
breaks the printed-tag reading immediately.

**One hairline, no shadow.** `--lift-card` is a single 1px bottom line. Nothing
casts downward, nothing lifts on hover, nothing scales. The one glow that exists,
`--glow-accent`, is a glow and not an elevation.

**The 4px frame is load-bearing.** `body { padding: var(--frame) }` insets the
whole document from the window edge so every panel closes against a visible margin
of paper. It is the cheapest identity move in the system and the easiest to delete
by accident in a layout refactor — it has a token name so it has something worth
preserving.

**Status is never by colour alone.** Every status carries its word, exactly as the
reference does — `online`, `Done`, `GET`, `POST`. The light set clears both gate
floors (17.5 at full colour, 8.1 under dichromacy); the dark set clears the hard
floor at 10.1 and runs tight at 6.8 under dichromacy, which the word covers. Note
that `--warning` is a near-black brown by arithmetic rather than by taste: the
coral accent occupies the warning hue, and every amber that reads as a warning
collides either with the accent under dichromacy or with danger at full colour.

**Motion is entry only, and then the page holds still.** One `fadeInBlur` on the
headline (0.6s, `--ease-out`, after `--stagger`), one entrance per section on the
way down, and nothing moves again — no hover lift, no drifting gradient, no
counter that keeps counting. **No scroll clock, no scrubbing, no parallax:** this
is the calmest pack in the family. At `prefers-reduced-motion: reduce` every
duration and the stagger go to zero, the blur never applies, and infinite motion
**stops** rather than shortens.

**The FAQ does not open.** `FaqList` is a `<dl>` whose answers are always visible,
because a collapsed answer is an answer no machine can extract. There is no
`collapsed` prop and there will not be one.
