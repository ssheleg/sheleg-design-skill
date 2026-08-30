# Style pack — Ora

Origin: <https://ora.ai> and <https://journey.ora.ai> (era labs). Read
2026-08-14 from the shipped stylesheet
`/_next/static/chunks/feb8eaf5618096ba.css` and the route bundles under
`/_next/static/chunks/`; both hosts serve the same stylesheet, so the two
surfaces are one system with two scopes. Screens read in both themes.

A coal field with cream ink and **no third hue**: the accent is the inverted
field, so the only thing that arrives in solid colour is the one thing meant to
be pressed. A serif does the sans job — `--font-sans` and `--font-serif` resolve
to the same face — so every human sentence is set in Lora and every machine fact
in Space Mono, and the two are never mixed inside one line. Elevation is a
hairline; the only surface that leaves the page plane goes **down**, into a
terminal block cut below the field. The signature texture is a six-step verdict
ramp: one ordered scale from teal to red that grades the reader's own product,
always rendered with its letter beside it.

Contract: widened

Themes: light only — the second block (`:root[data-theme="light"]`) is a SURFACE variant, not a theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Contents

- Register
- Palette
- Type
- Texture & surface
- Components
- Hero
- Responsive
- Motion tokens
- Signature motifs
- Signature element
- Micro-interactions
- Bans
- Gotchas

## Register

Choose this pack for products whose output is **a machine's verdict about the
reader** — agent-readiness and crawlability scores, SEO and answer-engine
audits, agent-run traces and step graphs, MCP and protocol surfaces, bot and
crawler observability, developer infrastructure whose argument is "here is what
an automated client actually saw." It suits a page that must hold a marketing
argument and an instrument on the same scroll, because both are built from the
same two faces and one accent.

Standalone: it does **not** ride the SHELEG cinematic motion layer. Its whole
motion budget is entrance, hover, two slow breathing glows, a sticky nav's
hairline shadow and one pinned comparison section, so `MOTION_INTENSITY` above
**4** has nothing legal to buy — the same ceiling `pigeonhole` and `roster`
carry, for the same reason.

**Not for:** consumer or brand-led marketing, where colour is asked to carry
identity — there is no brand hue here to carry it, and adding one dismantles the
accent rule in the first commit. Not for warm, friendly or playful registers, which `orchard` owns. Not for multi-series analytics: four
grade steps plus a three-state bar is the entire chromatic vocabulary, and a
sixth line on a chart has nowhere to come from. Not for dense operator chrome
with rails, toolbars and inspectors — the elevation model is one hairline and it
has nothing to say about a fourth nested panel.

**Two neighbours it is genuinely confusable with.**
[`datasheet`](./datasheet.md) also renders a verdict about the visitor, in one
orange on an off-white spec sheet at radius 0 — take it when the artefact is a
**row of cells** and the reader is comparing fields. Take Ora when the artefact
is **a number with a grade**, and when the reader must be shown the raw response
a machine got. [`manpage`](./manpage.md) also sells to a buyer who reads code
and also refuses a second family — take it when the page is documentation and
the display ceiling is 48px. Take Ora when the page is an instrument and the
display opens to 60px. Both of those are light-first; Ora is dark by default,
which is the fastest way to tell them apart on a screenshot.

**And a third that a screenshot will not separate.** [`paperclip`](./paperclip.md)
is also dark by default, also refuses a brand hue, also sets every machine fact
in a monospace, and also spends its accent as the inverted field — on a thumbnail
the two are the same pack. Three tests separate them. **Colour:** Ora has none
beyond its status set and its verdict ramp, and every one of those carries
meaning; Paperclip has a great deal and none of it is functional, because its
whole chromatic budget sits in an ornament nobody can click. **Type:** a serif
does the sans job here, so a human sentence is always a serif; there, two
grotesques and a monospace, and no serif exists. **What the page renders:** a
verdict about the reader, against a team of workers the reader is running. If
the artefact is a number with a grade, it is this pack; if it is an org chart, a
schedule and a ledger, it is that one.

## Palette

Ready-made token layer: [`tokens/ora.css`](./tokens/ora.css) — copy that file
verbatim instead of transcribing this table. Dark is the default and light is
the twin, which is the reference's own arrangement: it paints its dark values on
`:root:not([data-theme=light])`, so an unattributed root is dark.

**Dark — the default theme.**

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#141210` | page field, the warm coal the whole system sits on | — |
| `--surface` | `#1b1917` | the default container | 1.07:1 |
| `--surface-raised` | `#23201d` | popovers, menus, dropdowns | 1.15:1 |
| `--surface-quiet` | `#282521` | chip fills, quiet segments | 1.23:1 |
| `--terminal` | `#0a0908` | machine output, cut **below** the page | 1.06:1 |
| `--ink` | `#f7f2e5` | primary text, and THE accent | 16.72:1 |
| `--muted` | `#c2bdae` | labels, captions, every mono line that is not a value | 9.95:1 |
| `--border` | `#23201c` | container edge — never a mark, never a meaning | 1.15:1 |
| `--border-strong` | `#38342f` | dividers inside a container | 1.51:1 |
| `--accent` | `#f7f2e5` | the single functional accent: the inverted field | 16.72:1 |
| `--accent-ink` | `#141210` | text ON the accent | — |
| `--good` | `#34d399` | pass, healthy, reachable | 9.72:1 |
| `--warn` | `#fbbf24` | partial, degraded, needs work | 11.19:1 |
| `--danger` | `#f87171` | fail, blocked, unreachable | 6.76:1 |
| `--info` | `#60a5fa` | neutral machine state, running, queued | 7.35:1 |

**Light — the twin.** Same roles, and the status set drops to the base half of
each ramp, which is the reference's own rule: `-base` on paper, `-bright` on
coal, one hue at two lightnesses rather than two colours.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#f9f7f2` | warm paper | — |
| `--surface` | `#fcfbf8` | container | 1.03:1 |
| `--surface-raised` | `#ffffff` | the only pure white in the pack | 1.07:1 |
| `--terminal` | `#1e1c19` | still darker than the page, so the idea survives | 15.88:1 |
| `--ink` | `#1a1a1a` | primary text | 16.26:1 |
| `--muted` | `#5c5953` | labels and captions | 6.52:1 |
| `--accent` | `#161616` | the inverted field again | 16.90:1 |
| `--good` | `#22c55e` | pass | 2.13:1 |
| `--warn` | `#f59e0b` | partial | 2.01:1 |
| `--danger` | `#ef4444` | fail | 3.51:1 |
| `--info` | `#2563eb` | running | 4.83:1 |

**Status is never by colour alone.** In dark every status clears AA and may set
text. In light the base half does not: `--good` and `--warn` sit at 2.13:1 and
2.01:1 on paper, below the 3:1 non-text floor, so there they are bar fills, dots
and chip tints and the *word* carries the meaning. That is not a concession — it
is what the reference does on both themes. The verdict is always three things at
once: the number, the letter, and the word (`61` · `C` · `Needs Work`). Under
deuteranopia `--good` and `--danger` separate by only 6.5 in dark and 7.4 in
light, and under protanopia `--good` and `--warn` by 6.4 in light; the letter and
the word are what make those pairs legible, and removing either breaks the pack.

**The accent rule, stated once because everything else follows from it.** There
is no brand hue. The primary action is `bg-foreground text-background` — solid
ink, field-coloured label — and the reference names the pair
`--accent-signature` / `--accent-signature-foreground` to say so out loud. Three
consequences: only one element per viewport may be filled; a second filled
button is a design error rather than a variant; and the accent inverts with the
theme, so a hard-coded cream button is invisible on paper.

**The six-step verdict ramp** is a scale, not a legend, and lives beside the
status set rather than inside it: `--grade-a-plus` `#14b8a6`, `--grade-a`
`#34d399`, `--grade-b` `#a3e635`, `--grade-c` `#fbbf24`, `--grade-d` `#f87171`,
`--grade-f` `#ef4444` in dark. Adjacent steps are deliberately close — a reader
is meant to see *movement along the ramp*, and the exact step is read off the
letter. Never use two grade steps as two categories.

## Type

Two families, and only two. The display face is a **serif doing the sans job**:
`--font-sans`, `--font-serif` and `--default-font-family` all resolve to Lora in
the reference, so there is no sans anywhere in the system.

| Face | Where | Weight |
|---|---|---|
| Lora (`--font-display` / `--font-body`) | every human sentence: display, headings, lead, body, the intent the user typed | 400 throughout — the prose ramp never leaves regular |
| Space Mono (`--font-mono`) | every machine fact: labels, eyebrows, nav, URLs, paths, counts, timings, terminal output, chips, the wordmark | 400, 500 for a label, 700 for a section heading |

**The rule the two families encode: a serif means a person said it, mono means a
machine reported it.** A headline is Lora; a status is Space Mono; a domain name
is Space Mono even inside a serif sentence. Mixing them inside one line is the
fastest way to lose the pack.

**Prose ramp** (rem, serif, weight 400): `display` `clamp(2.5rem, 5vw, 3.75rem)`
/ 1.05 · `h1` 2.25rem / 1.1 · `h2` 1.5rem / 1.2 · `h3` 1.25rem / 1.3 · `lead`
1.25rem / 1.5 · `body-lg` 1.125rem / 1.7 · `body` 1rem / 1.625 · `body-sm`
0.875rem / 1.5.

**Mono ramp** (px, and the tracking opens as the size closes — this is the
pack's typographic signature): `label` 13px / .01em / w500 · `caption` 12px /
.02em · `micro` 11px / .05em · `nano` 10px / .05em / UPPERCASE · `pico` 8px /
.05em / UPPERCASE. Two wider steps exist for eyebrows and the wordmark:
`.14em` on a section label, `.18em` on the sub-wordmark beside the logo. The
run surface pushes an eyebrow to `.22em`; treat that as the ceiling.

**Every number is `tabular-nums`.** Scores, counts, timers, step totals,
percentages. A count that changes while the reader watches it must not reflow.

Measure: body prose is capped at `max-w-2xl` (42rem) on marketing surfaces and
`46rem` on the run surface's subhead. A serif at 1.625 line-height past 46rem is
the one way this pack becomes hard to read.

## Texture & surface

**Elevation is a hairline, and the only thing that leaves the page plane goes
down.** Four coal steps stack by fill alone — `--bg` → `--surface` →
`--surface-raised` → `--surface-quiet` — and `--border` separates them at
1.15:1, which is a seam rather than a line. `--terminal` is *darker* than the
page: a block of machine output reads as cut into the surface, not floating
above it, and that inversion is what stops a page of instruments from looking
like a card deck. Shadows exist for three things only and nothing else:
`--shadow-input`, `--shadow-card`, `--shadow-pop`, and the last is for overlays.

**Radius: one root, and every other value is a ratio of it.**

| Token | Arithmetic | Value | Where |
|---|---|---|---|
| `--radius` | the root | 8px | never used directly |
| `--radius-chip` | `× 0.5` | 4px | chips, tags, badges |
| `--radius-control` | `× 1` | 8px | buttons, inputs, terminal blocks |
| `--radius-card` | `× 1.5` | 12px | cards, panels, modals |
| `--radius-pill` | — | 9999px | dots, live indicators, progress tracks |

Do not add a step. The reference's own second scope already broke this by
writing `rounded-[7px]` and `rounded-[9px]` one-offs, and the result is two
radius systems in one product (see Gotchas).

**Concentric nesting — a pack decision, because the reference does not state
one.** When a container nests, the inner radius is the outer radius minus the
padding between them: a control at `--radius-control` inside a card at
`--radius-card` with 12px of padding needs no adjustment (12 − 12 = 0 leaves the
control's own 8px reading correctly against a 12px shell), but a chip flush
inside a control takes `calc(var(--radius-control) - 4px)`. Two identical radii
in a nest is what makes a layout look assembled rather than machined.

**Grain.** There is none. The field is flat colour. Two textures do the work
instead: a **dot field** at `#ffffff0d` on dark and `#1a1a1a0f` on light, and a
pair of very large, very soft breathing glows behind the hero
(`blur(90px)`, 58% × 66% of the viewport; `blur(64px)`, 40% × 96% below 640px).
Both are decoration and neither may carry information.

**Spacing.** `--space-header` 8px · `--space-stack` 16px · `--space-page-x` 24px
· `--space-section` 64px. Section padding on a marketing surface is 32px
horizontal and 56px vertical below 640px, 56px and 64px above it. The page shell is 72rem
on marketing surfaces and 65rem on the run surface — two containers, chosen by
whether the page is arguing or reporting.

**The rule band.** A section boundary is a 3.5rem strip bordered top and bottom,
with a hand-drawn squiggle running through its centre and a numbered mono label
knocked out over it (`01 THE PROBLEM`). The label is a bordered chip filled
`--bg`, sitting on the line rather than beside it. This is the pack's one piece
of ornament and it is the reason a long marketing page does not read as a stack
of cards.

## Components

Values measured off the reference. Every entry states rest, hover, active and
disabled; where the reference specifies no disabled state, the derivation is
marked.

- **Primary button.** `height 40px · padding 0 24px · --radius-control · fill
  --accent · label --accent-ink · mono 13px / w500 / tracking .04em`. Rest: solid
  ink. Hover: the fill drops to 90% opacity (`--accent-hover`) over
  `--dur-fast`, colour only. Active: no transform — this pack does not press.
  Disabled: `opacity .5`, pointer-events kept so a tooltip can explain why.
  **One per viewport.**
- **Secondary button.** `--radius-control · border 1px --border · fill
  --surface-raised · padding 10px 16px · 14.5px`. Hover: border only, to
  `--border-strong`; the fill does not move. Active: unchanged. Disabled:
  `opacity .5`.
- **Ghost / link action.** Mono, `--muted`, hover to `--ink`, no underline; a
  trailing `→` that shifts 2px on hover and only where a pointer is fine.
- **Cards / containers.** `--radius-card · border 1px --border · fill --surface
  at 40% over the field · padding 20px, 24px above 640px · internal gap 16px,
  20px above`. A card is used when a block has its own heading and its own
  actions. A row of facts inside one card is separated by
  `border-t --border` and 16px of padding, never by a nested card. Three
  equal blocks share **one** card with internal dividers rather than three
  cards.
- **Inputs.** `--radius-control · border 1px --border · fill --surface-raised at
  70% · padding 12px 14px · 15px`. Label sits above in mono `--muted`, never as a
  placeholder. Focus: border to `--accent` at 70%, plus the focus ring below.
  Error: border `--danger`, message beneath in mono 11px `--danger`, and the
  message is required — the border alone is a colour-only signal. Disabled:
  `opacity .5`.
- **The domain input** is the pack's own field type: a globe glyph in `--muted`
  that turns `--accent` on `:focus-within`, then a mono value at
  `clamp(16px, 1.4vw, 19px)` with no border of its own inside a shared shell.
- **Chips.** `--radius-chip · border 1px --border at 70% · padding 4px 8px · mono
  11.5px · --muted`. Hover: border to `--accent` at 40% and text to `--accent`.
  Selected: border `--accent`, text `--ink`. A status chip carries a 6px
  `--radius-pill` dot in the status colour **plus** the word.
- **Navigation.** A plain row at `padding 16px 20px` (20px / 24px above 640px),
  wordmark left in mono 20px w700 tracking `.02em`, links right in mono 12px
  `--muted` → `--ink` on hover. A section wordmark sits beside the logo in mono
  11px UPPERCASE tracking `.18em` at 60% muted, nudged 2px down onto the logo's
  baseline. **Sticky and opaque, never blurred**: `position: sticky; top: 0` over
  a solid `--bg`, and the *only* change on scroll is a 1px hairline shadow faded
  in over 300ms. That shadow is the single exception to "no shadow on a resting
  element", and it exists because an opaque sticky bar over a flat field has no
  other way to say it is in front. The run surface's own header is **not** sticky
  — it scrolls away, because that page has one screen of chrome and nothing to
  return to.
- **Terminal block.** `--radius-control · fill --terminal · label row in mono
  nano UPPERCASE at 45% terminal-ink, with a COPY affordance right`. Body is
  `white-space: pre`, mono caption, `--terminal-ink` at 85%. Horizontal overflow
  scrolls inside the block; the page never scrolls sideways for it.
- **Progress — linear.** A 3px `--radius-pill` track in `--surface-quiet` with a
  fill in the status colour. Animate the fill with `transform: scaleX()` and a
  `transform-origin: left`; never transition `width`, which lays out every frame
  (MOTION_DOCTRINE, and the reference does exactly this — see Gotchas).
- **Progress — segmented.** A 6px pill split into weighted segments, one per
  scoring layer, each carrying its own status colour, its label and its raw
  fraction beneath in mono nano UPPERCASE. A segment that does not apply is
  rendered as diagonal hatching in `--perf-na` and labelled `N/A`; it is never
  rendered as an empty bar, because empty reads as zero.
- **Stat.** Value in mono, `tabular-nums`, w700; label beneath in mono nano
  UPPERCASE `--muted` tracking `.12em`. Values align to their own column and the
  label never wraps.
- **Tooltip.** `--radius-control · border 1px --border · fill --surface-raised ·
  padding 8px 12px · mono 11px at 80% ink · --shadow-pop · max-width 200px`.
  Appears on hover and on focus; never the only home of a fact.
- **Modal.** `width min(520px, 100%) · --radius-card · fill --surface ·
  padding 24px, 36px above 640px · --shadow-pop`, over a scrim of `black / 60%`
  with a 8px backdrop blur. Opens with the eyebrow, not a title.
- **Loaders.** Two idioms and no spinner on a data path. A **step log**: one
  mono line per completed step, prefixed by a status dot and a check, appended
  as it happens, with the current step carrying a blinking caret. A **skeleton**
  whose geometry matches the block it replaces, pulsing opacity between .3 and
  .6 — never a shimmer sweeping across it. A spinner is allowed only for an
  action under 2 seconds with nothing to report.
- **Empty states.** Mono line stating what is absent in the machine's own words
  (`No sitemap found`, `Nothing to read. Nothing to act on.`), in `--muted`, left
  aligned, with the single action that would fix it beneath. No illustration, no
  centred column, no encouragement.

## Hero

One viewport, four elements, in this order: a mono eyebrow, one serif headline,
one serif subhead, and the control that starts the work. Nothing else — no
badges, no logo wall, no secondary CTA.

**The line ceiling is one line, and it is enforced rather than hoped for.** The
run surface sets the headline to `whitespace-nowrap` above 640px and sizes it
with `clamp(1.55rem, 3.3vw, 2.55rem)` at `line-height 1.15` so it cannot wrap;
below 640px it wraps freely and the nowrap is dropped. A marketing hero uses the
display ramp instead — `clamp(2.5rem, 5vw, 3.75rem)` at `line-height 1.05`,
`text-wrap: balance`, **two lines maximum** inside a 42rem measure. Three lines
means the headline is too long, not that the hero is too small.

The subhead is `clamp(0.95rem, 1.6vw, 1.15rem)`, `--muted`, capped at 46rem, and
says what the reader will get rather than what the product is.

The first viewport must contain the input that starts the run, and it must be
usable without scrolling at 800px of height. The marketing variant reserves
`min-height 30rem`, `45rem` above 640px, and fills the space behind the copy
with the breathing glows and a field of drifting agent marks — decoration that
carries no information and is removed entirely under reduced motion.

**What the hero must not contain:** a second filled button, a video, a
screenshot with a browser chrome frame, a testimonial, or a number the page has
not yet earned.

## Responsive

- **Fluid type — three clamps, and the slope is shown rather than guessed.**
  Display `clamp(2.5rem, 5vw, 3.75rem)`: 5vw crosses 2.5rem at 800px and 3.75rem
  at 1200px, so it is fluid only across that band and locked outside it. Run
  headline `clamp(1.55rem, 3.3vw, 2.55rem)`: locked below 752px, locked above
  1237px. Subhead `clamp(0.95rem, 1.6vw, 1.15rem)`. The mono ramp is **not**
  fluid — a 10px label stays 10px at every width, because a tracked uppercase
  label that shrinks stops being legible before it stops being small.
- **Container queries.** Four components size against their container and take
  `container-type: inline-size` on their root with `@container` on the
  descendant: the **segmented progress bar** (segment labels stack below 380px),
  the **stat row** (three across → one column), the **card header** (title and
  actions wrap), and the **check row** (the score and the chevron drop under the
  question). Everything else is PAGE: the hero's padding, the nav's shape, the
  rule band's height, the container widths and the `:root` theme switch are
  values the page owns and stay on viewport `@media`. The hero glows are SELF —
  the element that would establish the container is the one whose size changes,
  and a container cannot query itself, so they keep a viewport query.
- **Collapse.** The single breakpoint that matters is 640px. Above it the hero
  headline is one line, the run controls sit in a row, the primary button is
  `width: auto` and the stat row is three across. Below it every one of those
  stacks full-width, the headline wraps, the desktop glow is swapped for the
  wider, shallower mobile one, and the section rule band keeps its height but
  pulls its label to 32px from the edge. Nothing in this pack overlaps, rotates
  or carries a negative margin, so there is no asymmetry to unwind — which is
  the reason the collapse is one rule and not five.
- **Viewport.** Full-height shells use `min-height: 100dvh`. The reference does
  this already and it is the one thing a copy of it must not simplify.

## Motion tokens

One ease for everything the reader triggers, one for the two ambient loops, and
one overshoot reserved for a single moment.

| Token | Value | Where |
|---|---|---|
| `--motion-ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | the site-wide decelerate: every hover, entrance and state change |
| `--motion-ease-standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | the framework default, kept only where a third-party control already uses it |
| `--motion-ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | overshoot, and **only** the verdict badge stamping in once per run |
| `--dur-fast` | `0.15s` | hover: colour, border and opacity only |
| `--dur` | `0.2s` | the default state change |
| `--dur-slow` | `0.3s` | a panel opening, a row expanding |
| `--dur-slower` | `0.5s` | a bar reaching its final value |
| `--dur-breathe` | `7s` | the hero glows, `ease-in-out`, infinite |
| `--dur-caret` | `1.1s` | the terminal caret, `step-end`, infinite |

These override the SHELEG defaults wherever they differ, and nothing here
exceeds the doctrine's duration ceiling except the two ambient loops, which are
decoration and are removed rather than shortened.

**Reduced motion is a blanket, not a taper.** Under
`prefers-reduced-motion: reduce` every duration token collapses to zero, the
breathing glows stop, the caret stops blinking and holds visible, the live dot
holds at 90% opacity, and the backdrop's fade is removed. The page keeps every
value it was showing. This is the reference's own behaviour and it is the
correct one: an ambient loop has no reduced form worth keeping.

**The step log is the exception that proves the frequency rule.** A run appends
a line every few hundred milliseconds for thirty seconds. Do not animate the
append. The list grows; nothing slides.

## Signature motifs

1. **The inverted accent.** One solid element per viewport, filled with the ink,
   labelled in the field colour, flipping with the theme.
2. **A serif sentence over a mono fact.** Every block pairs them: a serif
   question with a mono score, a serif claim with a mono command.
3. **The terminal cut below the page.** The darkest surface is the one carrying
   raw machine output, and it never has a shadow.
4. **The rule band.** A 3.5rem strip between sections, bordered top and bottom,
   with a hand-drawn squiggle through it and a numbered mono label knocked out
   over the line.
5. **The dotted connector graph.** Agent steps drawn as bordered mono nodes on
   dashed 1px orthogonal connectors with small circular junctions, coloured by
   outcome and never by category.
6. **The tracked uppercase micro-label.** 10px or 11px mono, `.05em` to `.22em`,
   `--muted`, sitting above or beneath the thing it names — the pack's way of
   labelling anything without adding a heading level.

## Signature element

**The verdict numeral.** One number, set in the display serif at the top of the
report, in the grade colour, with a hairline `/ 100` denominator in `--muted` at
roughly half its size and the grade letter plus its word directly beneath
(`61` `/ 100`, then `C  Needs Work`). It is the only place in the pack where a
status colour is allowed at display size, the only place the serif carries a
number, and the only element on the page that is allowed to be large.

It is the signature because it is the product's whole promise compressed into
one glyph: the page exists to tell a person what a machine concluded about them,
and every other element on the screen is an explanation of that number.
Everything around it stays quiet — the surrounding chrome is mono, muted and
11px — and that contrast is the entire composition. Spend boldness here and
nowhere else.

## Micro-interactions

- **Focus.** `outline: 2px solid var(--accent); outline-offset: 2px;
  border-radius: 4px` on every interactive element — links, buttons, roles and
  anything with a `tabindex`, excluding text fields, which take a border change
  instead. The ring is the accent, so it inverts with the theme and is always
  the highest-contrast thing on the screen. Never remove it; never replace it
  with a shadow.
- **Hover is colour, border and opacity. Never geometry.** Nothing in this pack
  lifts, scales or shifts on hover. The two exceptions are a trailing `→` moving
  2px and a bar segment brightening — both gated on `@media (hover: hover)`.
- **The live dot** is a 7px accent pill with a pulsing 5px halo on a 1.6s loop.
  It means work is happening right now. It is never decoration and never appears
  beside a finished state.
- **The caret.** A `▌` in the accent, blinking on a 1.1s `step-end` loop,
  appended to the line the machine is currently writing. Exactly one caret on a
  page.
- **Keyboard.** The intent field is a textarea that grows with its content
  (`field-sizing: content`) between 1.5em and 7.5em, so `Enter` inserts a
  newline and the run is started from the button or `⌘↵`. A chip row scrolls
  horizontally with a hidden scrollbar and stays reachable by tab.
- **Copy affordances** state their result in place: the label becomes `COPIED`
  for 1.2s in `--good`, and the button does not move.

## Bans

- **No third hue.** Every attempt to add a brand colour ends with two accents and
  no hierarchy. The accent is the ink.
- **No sans-serif.** Introducing one breaks the serif-means-a-person rule the
  whole page is read through.
- **No gradient fills, no glass, no blur on a surface.** Blur exists twice: the
  hero glows and the modal scrim. A frosted card is not this pack.
- **No shadow on a resting element**, with exactly one exception: the sticky
  nav's 1px hairline once the page has scrolled. Shadows are otherwise for things
  that float over the page, and a card does not float.
- **No coloured backgrounds behind text blocks.** A tint is a chip or a bar, at
  the size of a word.
- **No pill buttons.** `--radius-pill` belongs to dots and tracks.
- **No spinner where a step log is possible**, and no progress bar that is not
  driven by a real count.
- **No status without a word.** A dot, a bar or a number in a status colour
  always carries its label; the six-step ramp always carries its letter.
- **No scroll-jacking, no parallax, no `animation-timeline`, no scroll library.**
  Verified against the reference: zero occurrences of `animation-timeline`,
  `scroll-timeline`, GSAP or ScrollTrigger in any shipped bundle. Scroll drives
  exactly two things — the nav's hairline shadow and one pinned two-panel
  comparison that holds still while the page passes it — and that pair is the
  ceiling.
- **No icon set.** The pack uses a globe, a magnifier, a check, a chevron and an
  arrow, all at 14px, all inherited from the text colour. A sixth icon needs an
  argument.
- **No screenshot inside a browser frame** and no product illustration. The
  proof is the raw response, rendered in the terminal block.

## Gotchas

Nine traps, all measured in the reference on 2026-08-14. Six of them are
defects in the reference itself, which is exactly why a copy of it inherits
them.

1. **`--border-strong` is never re-declared for the dark theme.** It is set once
   in the light `:root` to `var(--paper-400)` (`#d6cfbc`) and the dark block
   overrides `--border`, `--muted` and eleven other tokens without touching it —
   so every `border-strong` hairline on the coal field renders paper-coloured at
   12.02:1, brighter than the body text's own border by an order of magnitude.
   It reads as deliberate on the `/mcp` timeline ticks and as a mistake on a card
   edge. This pack ships a dark value of its own (`#38342f`) and marks it derived
   at the declaration. If you need a bright instrument hairline on dark, reach
   for `--muted`, not for `--border-strong`.
2. **`--shadow-pop` means two different things in the two scopes.** In the app it
   is a complete shadow (`0 28px 70px -12px …`); in the journey scope it is a
   bare colour (`#000000b3`) consumed inside
   `shadow-[0_28px_70px_-12px_var(--shadow-pop)]`. Copy the wrong one and the
   declaration is invalid, so the shadow silently disappears rather than
   erroring. This pack ships complete shadows only.
3. **The reference's `--accent` is not an accent.** Its shadcn layer names
   `--accent: #282521` — a raised surface. The real accent is
   `--accent-signature`, which points at `--foreground`. An agent reading the
   token names alone will paint every accent surface a dark brown and conclude
   the pack has no accent at all.
4. **There are two dark greys.** The app field is warm coal `#141210`; the
   journey scope's is neutral `#151515` with its own `--jbg2/3/4` ladder and a
   bone accent `#ece4ce` in place of the cream. They are one product and two
   palettes, and the seam is visible when the two surfaces are opened side by
   side. This pack ships the app's warm coal and folds the journey scope's rules
   (the accent inversion, the reduced-motion blanket) into it.
5. **Two radius systems.** The app derives everything from `--radius: .5rem` by
   multiplication; the journey scope writes `rounded-[7px]` and `rounded-[9px]`
   literals that sit on no ladder. Keep the ladder.
6. **Four webfont families are loaded and two are used.** `<html>` carries the
   next/font classes for Lora, Space Mono, Sora and Geist Mono; the stylesheet
   references `--font-lora` ten times, `--font-space-mono` eight, and
   `--font-sora` and `--font-geist-mono` zero. Ship two.
7. **`--font-sans` is a serif.** Any component library, chart or third-party
   widget that reaches for the sans slot gets Lora. Either accept it or scope the
   third party explicitly; do not "fix" it by adding a real sans, which
   dismantles the type rule.
8. **The progress fill transitions a layout property.** The reference animates
   the bar with `transition-all duration-700`, which animates `width` and lays
   out every frame; never do this — use `transform: scaleX()` with a left
   origin, which this pack specifies in Components.
9. **Half-pixel type sizes are everywhere on the run surface** — 11.5px, 13.5px,
   14.5px, 15px, 25px, 26px — none of which sit on the token ramp. They are the
   cost of building a second surface without the first one's scale. Use the
   tokens; if a value is genuinely missing, add a step and name it rather than
   writing a literal.
