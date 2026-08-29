# Style pack — Tenor

Origin: <https://heytenor.com>. Read 2026-08-14 from `/assets/home.css?v=45`,
`/assets/home.js?v=7`, `/assets/recruiting-easter-egg.js?v=7` and the served
HTML. The stylesheet is **33,822 bytes of hand-authored CSS**, not a compiled
utility bundle, so what follows is the reference's own vocabulary rather than a
reconstruction of one: the token names, the ratios between them and the reasons
they exist are all legible in the source.

A warm paper field under near-black ink, ruled by a single hairline weight, with
**no radius anywhere and no shadow anywhere** — zero occurrences of either in the
whole stylesheet. There is one hue, and at rest it is almost invisible: a 25px
orange square behind an investor's initial. Everywhere else the orange is what
happens when you touch something. Ranking is done by **value** — a chip is orange,
grey or black; a four-step argument descends from paper to ink — and the display
face runs at a line-height below one in a measure of eight to twelve characters,
so a sentence arrives as a stack rather than a line.

Contract: widened

Themes: light only — the second block (`[data-surface="dark"]`) is a SURFACE variant, not a theme twin.
Rank: ordered — `--sev-ask` → `--sev-limit` → `--sev-never`.

## Register

Choose this pack for products that argue a **management thesis**: that some new
kind of thing has to be run like an existing organisational structure. AI
workforce and agent-operations platforms, autonomous back-office, revenue and
sales operations automation, anything sold to a director who will be asked to
manage the thing being sold. It suits a page whose proof is **a recording of the
product working** rather than a number, a logo wall or a screenshot.

The register underneath it is the sober enterprise manifesto: assertive short
sentences ending in full stops, set very large and very tight, with the argument
carried by structure rather than by colour. It reads expensive without spending
anything on decoration, which is why it survives a long page.

Standalone: it does **not** ride the SHELEG cinematic motion layer. Its whole
motion budget is a reveal on entry, a hover, a four-step stagger and one slow
ambient gradient, so `MOTION_INTENSITY` above **4** has nothing legal to buy.

**Not for:** consumer, playful or brand-led registers where colour carries
identity — there is one hue here and it only appears under the cursor. Not for
dense operator chrome: with no radius, no shadow and one border weight, a fourth
nested panel has nothing to sit on, and that is `workbench`'s half. That refusal
is narrower than it reads, and
[On a product surface](#on-a-product-surface) measures where it actually bites —
a dashboard's panels and stat lattice carry the pack unchanged; a status chip
repeated down a table column is where the single hairline stops separating. Not for a
page whose argument is an accumulating figure (`scoreboard`) or a documentation
page whose focal element is a command (`manpage`).

**Two neighbours it is genuinely confusable with.**
[`blueprint`](./blueprint.md) also refuses radius entirely and also builds its
structure from hairlines — take it when the subject is **precision** and the page
should read as a drawing, with a visible 32px grid and registration marks. Take
Tenor when the subject is **management** and the structure should read as an
organisation chart: warm paper instead of white stock, no grid marks, and a
lattice assembled from per-cell borders rather than drawn over the page.
[`roster`](./roster.md) also puts one orange on a light field and also forbids it
from carrying a word — take it when the argument is **who already uses you**, made
of other people's marks. Take Tenor when the argument is **how the work is
organised**, made of your own product on video.
[`deskmate`](./deskmate.md) is the third, and it is the register collision rather
than a visual one: it is sold to the same buyer, about the same kind of autonomous
worker. Take it when the proof is **a quoted conversation** — the request, the
reply and the artefact the reply produced — and the page is allowed to spend a
colour ramp and a pill on saying so. Take Tenor when the proof is **the product
working on video** and the page has one hue, no radius and no gradient at all.

## Palette

Ready-made token layer: [`tokens/tenor.css`](./tokens/tenor.css) — copy that file
verbatim instead of transcribing this table.

**Paper — the page, and there is no second theme.**

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#f7f6f2` | the page, and the fill of anything that is not inverted | — |
| `--bg-deep` | `#eeece6` | a different room, not a raised surface | 1.09:1 |
| `--ink` | `#10100f` | display, headings, every filled control | 17.61:1 |
| `--ink-soft` | `#777773` | the tracked mono labels — **not prose**, see Gotcha 1 | 4.16:1 |
| `--ink-soft-aa` | `#6b6b67` | **derived** — supporting prose, on either field | 4.95:1 |
| `--ink-faint` | `#a3a29d` | the hero's grey clause, and nothing smaller | 2.36:1 |
| `--line` | `rgb(16 16 15 / 0.16)` | the only border weight in the system | — |
| `--accent` | `#e9672a` | hover fill, focus ring, one 25px lockup square | 3.02:1 |
| `--accent-ink` | `#10100f` | text ON the accent — **corrected**, see below | — |
| `--good` | `#296b46` | **derived** — success on a product surface | 5.91:1 |
| `--warn` | `#e9672a` | attention as a **mark**, and it is the accent | 3.02:1 |
| `--warn-ink` | `#94400f` | **derived** — attention as a **word** | 6.47:1 |
| `--danger` | `#10100f` | prohibition, and it is the ink | 17.61:1 |

**`--accent-ink` is the coal, and this is the one place the pack overrules its
reference.** The site puts the paper on its orange fills, which measures 3.02:1 —
the same figure as the fill on the field, because contrast is symmetric — so
every CTA in the reference fails AA at the instant it is hovered. The coal on
that same fill measures **5.84:1**. Since the orange does not change between the
paper page and the dark band, neither does the only label that can be read on it,
which is why the token layer declares `--accent-ink` once and the dark block does
not override it. The consequence is worth stating plainly: **the hover fill is
legal after all.** Gotcha 3 used to route around it by moving the border instead
of the fill; that workaround is no longer the answer.

**The dark band is a section, not a theme.** `[data-surface="dark"]` inverts one
strip inside a paper page — the reference uses it for the use-case grid and the
footer, and never for a whole page. Its greys are composites of the paper over
the ink, which is why they are neutral rather than a second warm ramp:
`--ink` `#f7f6f2` at 17.61:1 on `--bg`, `--ink-soft` `#a4a3a0` at 7.55:1 on `--bg`,
`--ink-faint` `#7f7e7c` at 4.69:1 on `--bg`, and `--good` re-derived to `#57c08c` at 8.45:1. On this field the
orange clears AA on its own, so `--warn-ink` is remapped back to the accent — the
value-axis variant exists for the paper alone.

`--bg-deep` on the band is **derived** rather than measured: the reference aliases
it to the field, because a band has no hover and no resting chip and therefore
needs no second room. `#222221` is paper at 8% over the coal, and a product
surface has both — see [On a product surface](#on-a-product-surface).

**The accent is a hover state.** This is the pack's whole colour argument, so it
is stated before anything else follows from it. At rest the page has one orange
object on it: a 25px square carrying the letter Y in the investor lockup. Every
other appearance is triggered — a filled control turning orange under the
cursor, the 2px focus ring, one guardrail chip that means *ask first*. Three
consequences: a page can be screenshotted with no colour in it at all and still
be this pack; a resting orange fill is a design error rather than a variant; and
because the orange sits at 3.02:1 on the paper, **nothing may be set in it**.

Text *on* the orange is the other direction and a different measurement, and the
two get conflated: the paper on it is the same 3.02:1, but the coal on it is
5.84:1. So the rule has two halves and only one of them is a prohibition — the
orange never colours a word, and a word may sit on the orange provided it is
`--accent-ink`. See Gotcha 3.

**Severity is value, not hue.** The guardrail chips prove it in one row: `ALWAYS
ASK` is the orange, `LIMIT` is a grey, `NEVER` is the ink. Three levels, one hue,
and the **word** carries the meaning in every one of them — status is never by
colour alone here. Use `--sev-ask` / `--sev-limit` / `--sev-never` before
reaching for a colour. `--good` is the only value in the pack the reference does
not contain, and it is marked derived at its declaration: a marketing site paints
no success state, and the product surfaces this pack also dresses do need one.

## Type

Two families, two weights, and tracking that runs in opposite directions.

| Face | Where | Weight |
|---|---|---|
| Instrument Sans (`--sans`) | every sentence: hero, section heads, card titles, prose, mobile nav | **400, and only 400** |
| IBM Plex Mono (`--mono`) | every label: nav, eyebrows, step numbers, all CTA text, FAQ indices, footer | **500**, with 400 on the copyright line alone |

**The tracking rule is the pack.** The sans tracks negative and tightens as it
grows — `-0.02em` at 1.12rem, `-0.03em`, `-0.035em`, `-0.04em`, `-0.055em`,
`-0.06em`, and `-0.065em` on the hero. The mono tracks positive and opens as it
shrinks — `0.08em` on the nav, `0.09em` on a CTA, `0.1em` and `0.12em` on the
smallest labels. The two ramps pass through zero and never meet: nothing in this
pack is set in the sans with positive tracking, and nothing in the mono is set
with negative tracking.

**Line-height goes below one, and the measure is set in characters.** The hero is
`0.91` at `12ch`; a section head `0.93` at `8ch` to `9.5ch`; a process step
`0.98` at `10ch`; a card title `1.05` at `11ch`. That narrow measure is what
turns every heading into a three- or four-line stack, which is the shape the
page is recognised by. Prose leaves the `ch` measure and takes pixels — a lead
paragraph is capped at 580px at `1.55`, body copy at `32ch` at `1.48`.

**The display ramp is fluid end to end.** The reference declares twenty distinct
`clamp()` font sizes and not one fixed display value. Do not add a fixed step:
this pack has no `h1` size, it has an `h1` slope.

**Two clauses, two colours, one sentence.** The hero headline is a single
sentence split across two `<span>` blocks — the first in `--ink-faint`, the
second in `--ink`. The grey half is the premise and the black half is the claim,
and the reader parses the emphasis before reading a word. Use it once per page.

## Texture & surface

**There is no radius and there are no shadows.** Zero occurrences of
`border-radius` and zero of `box-shadow` in 33,822 bytes. Every corner is square
and nothing floats. When containers nest, the radius arithmetic is `0` inside
`0`, and that is the point rather than an omission: a system with one corner
value cannot produce the mismatched-curve failure at all.

**Separation is one hairline and one weight.** `--line` is ink at 16% and there
is no strong variant. A lattice is assembled **per cell** — the container draws
its top and left edge, each cell draws its right and bottom — which is why a cell
can invert to solid ink on hover without a seam appearing along its border.
Build grids this way and not with `border-collapse` or a background line.

**Emphasis is a filled rectangle.** With no shadow and no radius, the only ways
to raise something are to fill it (`--ink` on paper, `--bg` on the dark band) or
to move it to `--bg-deep`. `--bg-deep` is a *room*, not an elevation step: a
section may sit on it, a card inside a section may not.

**Two textures, and both are quiet.** The closing panel carries a dot field —
two radial-gradient layers at 17px and 23px pitch, ink at 4.5% and 3.5%, offset
from each other so the pattern does not read as a grid. The hero carries a
point-cloud halftone: a photographic image reduced to a dot screen, 1708px wide,
pulled up under the headline by a negative margin of `clamp(-80px, -5vw, -48px)`
and cropped by `overflow: hidden`. Both are decoration; neither may carry
information.

**Spacing.** `--section-space` `clamp(40px, 4.5vw, 64px)` between sections,
`--section-space-tight` `clamp(24px, 2.5vw, 36px)` where two sections belong
together, `--content-space` `clamp(32px, 3.5vw, 48px)` inside one. The page shell
is `min(100%, 1440px)` with `padding-inline: clamp(22px, 4vw, 68px)`.

## Components

Values measured off the reference. Each entry states rest, hover, active and
disabled; where the reference paints no such state, the derivation is marked.

- **Header.** `position: fixed`, 78px tall (72px below 1080px), a three-column
  grid of `minmax(120px, 1fr) auto minmax(120px, 1fr)` so the nav is optically
  centred regardless of the wordmark's width. Background is the paper at **94%**
  with a 14px backdrop blur and a transparent bottom border; past 12px of scroll
  it goes to **98%** and the border becomes `--line`, over 180ms. Nothing else
  changes — the header never shrinks, never hides and never gains a shadow.
- **Nav link.** Mono at `--fs-nav`, uppercase, tracked `0.08em`, ink at 72%.
  Rest: no underline. Hover and `:focus-visible`: a 1px rule under the word
  scales from 0 to 1 over 260ms, and **the origin flips** — it is `right` at rest
  and `left` on hover, so the line wipes in from the left and out to the right.
  Active: unchanged. Disabled: not a state this component has.
- **Buttons — one shape at three sizes, and the hover is the accent.** All three
  are square, filled `--ink`, labelled `--accent-ink` in tracked mono caps, and
  all three turn `--accent` on hover with a small lift. Header CTA: min-height
  42px, padding `0 19px`, `--fs-nav`, lift 1px. Section CTA: min 158×44, gap 22px
  between label and glyph, `--fs-cta` tracked `0.09em`, lift 1px, and it carries
  a 1px border of its own colour so the orange hover moves the border with the
  fill. Closing CTA: min 170×58, `--fs-cta-lg`, lift 2px. On `[data-surface="dark"]`
  the fill inverts to paper with ink text and the hover is still the orange, with
  paper text. Disabled is **not specified by the reference** — this pack's
  decision: `opacity: 0.45`, no hover, and keep pointer events so a tooltip can
  explain why.
- **Cells / cards — the unit is a cell in a lattice, not a card on a page.** A
  capability cell is min-height 300px, padded `clamp(25px, 3vw, 42px)`, with its
  mono index at the top, its title pushed to the bottom by `margin-top: auto`,
  and a 32ch paragraph beneath. **Hover inverts the whole cell** to `--ink` /
  `--bg` over 240ms, and the paragraph and index go to paper at 63% in the same
  transition. On the dark band the inversion runs the other way, to paper, over
  200ms. Three equal blocks share one lattice; they are never three separate
  cards.
- **The bento row.** The dark use-case grid is a **10-column** grid with an
  explicit `grid-area` per cell: five across the top, one at each end of the
  middle row, five across the bottom, and one wide feature cell spanning columns
  3 to 9 of the middle row. Below 860px every cell drops its area and the grid
  becomes two columns; below 620px, one. Use the explicit-area form only when the
  feature cell is genuinely wider than the others.
- **Inputs.** The reference has **none** — it is a page with no form. This pack's
  decision, derived from the button and the lattice: square, `--bg` fill, 1px
  `--line` border, label above in mono `--ink-soft`, focus taking the 2px orange
  ring at 4px offset rather than a border change, and the error message beneath
  in mono with the word present, because the orange cannot carry the meaning.
- **FAQ.** Native `<details>` / `<summary>`, no JavaScript. The summary is a
  96px-minimum three-column grid — `42px 1fr 24px` — carrying a mono index, the
  question at `clamp(1.12rem, 1.7vw, 1.45rem)` tracked `-0.02em`, and a plus
  built from **two 14×1px bars**; opening rotates the vertical one to horizontal
  over 180ms. The heading beside the list is `position: sticky` at
  `header-height + 50px` and is set at `clamp(4rem, 8vw, 8rem)`, the largest type
  in the pack.
- **Product proof.** Not a screenshot: a **silent looping video** in a 16:9 box
  with a 1px `--line` border and `object-fit: contain`. Muted, `playsinline` and
  loop are set in markup *and* re-applied in script; playback is started and
  paused by an IntersectionObserver at `rootMargin: 20% 0px`, and under reduced
  motion every video is paused rather than hidden. Each one carries a real
  `aria-label` describing what it shows.
- **Loaders.** The reference has none. This pack's decision: the video *is* the
  loading state on a marketing surface; on a product surface, a 1px `--line`
  skeleton whose geometry matches the block it replaces, and no spinner.
- **Empty states.** Also absent from the reference. Derived: a mono label, one
  sentence of `--ink-soft-aa` prose in the `32ch` measure, and the single action
  that fills it, as a section CTA. No illustration.

### On a product surface

Everything above is measured off a marketing page. The pack is also spent on the
dashboards and admin screens behind such a page, and five things break there that
a page never exercises. Each answer below is **derived**; all were found by
mounting the pack on a populated twenty-route dashboard rather than reasoned about.

- **There is no dark theme, and a product that has one needs a decision.** The
  reference inverts a band inside a paper page; it never inverts the page. A
  product with a theme toggle has three options and only the third is honest:
  drop the toggle, invent a second ramp (which is inventing values), or **promote
  the band's own measured greys to a theme** and add the one thing a band does
  not have — a second field, `--bg-deep` `#222221`. Take the third and say so,
  because a reader who knows the pack will otherwise assume the dark screens were
  extracted and they were not.
- **Ranking by value costs the link its affordance.** With `--accent` moved onto
  the ink so it can carry a word, a link is the same colour as the sentence
  beside it. The pack already owns the fix and spends it only in the header: the
  rule under the word whose origin flips, `right` at rest and `left` on hover.
  Use it for a section's action link. For a link repeated down a table, use a
  plain static underline in `--line` instead — fifty animated rules is the
  "more than one marquee" ban wearing a different costume.
- **The selected row of a rail is the lattice cell's inversion, held open.** Not
  an accent tint: there is no second hue to tint with, and `--accent-weak` on
  this pack is just the deeper paper. Fill it `--ink`, set the label `--bg`, and
  drop any suffix count to 63% — the same treatment a capability cell takes on
  hover.
- **A column of chips is where the hairline stops working, and it is the pack's
  own density warning made specific.** One border weight, no radius and no fill
  means fifteen status chips down a table column read as a texture rather than as
  fifteen states. The threshold measured here: a lattice of chips is legible
  while they are *comparable and few* — a header row, a summary strip — and stops
  being legible the moment they repeat per row. In a table, drop the box and set
  the status as the word alone in its severity value, with `--warn` kept for the
  mark beside it. Panels and tiles are unaffected: the same lattice at four cells
  across a dashboard's stat row reads exactly as it does on the page.

  **And dropping the box is only half of it: a colour earns its place where the
  column varies.** Measured across twenty routes of one dashboard — on the screen
  listing agent connections, **82 rows all reading `ACTIVE`, 421 green marks, and
  not one of them told the reader anything**, because a value that never changes
  is not a status. Two screens away the audit log spends the same green across 200
  rows against the warn value, and there it carries the whole distinction. The
  rule: **set the severity value only on the rows that differ from the column's
  own norm**, and leave the norm in `--ink`. A constant column is prose, and prose
  is not coloured here.
- **Prose sits on two fields at once and `--ink-soft` fails on the second.** This
  is what produced `--ink-soft-aa`; see Gotcha 1.
- **A data mark must not borrow the hairline, and in this pack it silently will.**
  Tenor has one border weight and no strong variant, so a design system that
  carries `--border` and `--border-strong` as two steps collapses them onto one
  value here. A sparkline whose resting bars were painted with the *stronger* of
  those two is then painted in the exact colour of the rule between the rows it
  sits in — a quantity rendered in the token reserved for chrome, and nothing
  errors, because both names resolve. Measured on a dashboard's account table:
  the two resolved identically and the bars matched the row separator to the
  byte. **Use `--data-rest`**, which the token layer maps onto the value ramp the
  staircase already spends: `--stair-3` on the paper (3.37:1 on `--bg`, and 2.38
  against `--line`, so it separates from the rule) and `--ink-faint` on the band.
  The emphasised mark stays `--accent-ink`-on-`--ink` or whatever the chart's own
  emphasis rule says; only the resting one changes. Charts in any pack go through
  `dataviz` first — token names are not uniform across the thirty-eight packs, and an aliased
  one fails exactly this quietly.

**The type ramp is where this section was wrong, and the correction matters more
than the error.** It used to say a dashboard has "neither a section rhythm nor
display type" and to keep the product's own scale outright. The first half holds
— the section rhythm is a page value. The second half threw away the thing that
makes this pack legible: **the tracking rule only acts on type large enough to
show it.** A screen title at 30px tracked `-0.02em` is the rule acting on
nothing, and a product mounted that way reads as the pack's palette with somebody
else's typography inside it.

So the distinction is between the *ramp* and the *rule*. The marketing ramp stays
out: no `clamp(3rem, 6.5vw, 6.6rem)`, no 8–12ch measures, no section head at
6.6rem. The tracking rule comes in, and a dashboard has exactly **three steps**
for it to act on:

| Step | Size | Tracking | Weight |
|---|---|---|---|
| The screen title — one per screen | `clamp(2.35rem, 3vw, 3.15rem)` | `-0.04em` | 400 |
| A section head | `clamp(1.2rem, 1.4vw, 1.45rem)` | `-0.03em` | 400 |
| A metric — the argument of the screen | `clamp(2.1rem, 2.4vw, 2.75rem)` | `-0.045em` | 500, mono |

Line-height goes to `0.98` on the title and `1` on the metric — below the prose
leading, which is what makes a title read as a drawn object rather than as a
large sentence. **All three drop to weight 400 in the sans**, because ranking by
size is the pack's device and ranking by weight is the one it replaced; a heading
distinguished by being semibold at body size is a heading with no step under it.
Measured on a dashboard whose ramp was 30 / 16 / 13: the jump from title to
section head was 3:1 with nothing between, and two sizes that far apart stop
reading as a hierarchy and start reading as two unrelated decisions.

**A stat row is a lattice, and it is built per cell or the inversion breaks.**
The `## Components` entry says three equal blocks share one lattice and never read
as three cards; on a product surface that is the row of metric tiles, and the
construction is load-bearing rather than stylistic. The container draws its top
and left edge, each cell draws its right and bottom, and **the gap is zero** — a
lattice has no gap. Build it with four bordered boxes 12px apart and the hover
inversion leaves a seam down every border it touches, which is the exact failure
`border-collapse` and a background line also produce.

**Motion on a product surface is pointer-driven and nothing else.** Tenor's motion
tokens are page values — a 640ms fade, an 820ms travel, a 110ms stagger four steps
deep — and every one of them is spent on a block a reader scrolls to once.
`MOTION_DOCTRINE.md` §1 puts a dashboard's screens in the row where animation is
cut to the floor, because the same screen is opened tens of times a day, so **the
entrance budget on a product surface is zero**: nothing plays on load, on client
navigation, or on a keystroke. What is left is the whole budget and it is enough —
the cell inversion at `--dur-panel`, the nav underline at `--dur-nav`, the focus
ring, and the fill on a hovered control. Each is caused by the reader's own
pointer, which is what makes it feel like a response rather than like a delay.

What still does **not** change: the spacing scale and the section rhythm. Keep the
product's own spacing and take the pack's *surface* — the field, the zero radius,
the single hairline, the hue that only appears under the cursor, and the two
tracking ramps.

## Hero

Four elements and no more: the investor lockup, the two-clause headline, the
point-cloud image, and nothing else. There is no subhead, no button and no form
in the first viewport — the page's argument opens by being read, and the CTA is
already in the fixed header.

**The hero is indented, not centred.** The lockup and the headline both take
`margin-left: clamp(0px, 14vw, 210px)`, so the text block starts about a seventh
of the way across and the image beneath it runs full-bleed. Below 1080px the
indent drops to `clamp(0px, 7vw, 80px)`; below 620px it becomes `margin: 0 auto`
and the headline centres — the only place in the pack where display type is
centred.

**The line ceiling is four lines, and the measure enforces it.** `max-width: 12ch`
at `clamp(2.55rem, 4.6vw, 4.65rem)` and `line-height: 0.91`, with `text-wrap:
balance` and the sentence hand-split into two `<span>` blocks. Below 620px the
measure tightens to `10.8ch` and the size to `clamp(2rem, 9.4vw, 2.75rem)`. A
headline that will not fit four lines at `12ch` is too long; do not widen the
measure to rescue it.

**What the first viewport must not contain:** a second colour, a logo wall, a
form, a testimonial, or a screenshot with browser chrome around it.

## Responsive

- **Fluid type.** Every display size is a `clamp()`, and the slopes are shown
  rather than guessed. The hero, `clamp(2.55rem, 4.6vw, 4.65rem)`: 4.6vw crosses
  2.55rem at 887px and 4.65rem at 1617px, so it is fluid across that band and
  locked outside it. A section head, `clamp(3rem, 6.5vw, 6.6rem)`: fluid from
  738px to 1625px. The FAQ word, `clamp(4rem, 8vw, 8rem)`: fluid from 800px to
  1600px. The mono ramp is **not** fluid — a tracked 10px label that shrinks
  stops being legible before it stops being small.
- **Container queries.** The reference has **none**, and it is a page, so that is
  correct there. Sorting this pack's breakpoints into the three kinds: the page
  shell, the header height and grid, the hero indent and the display slopes are
  **PAGE** and stay on viewport `@media`. The hero image's own negative margin and
  full-bleed crop are **SELF** — the element that would establish a container is
  the one whose size changes, and a container cannot query itself. The
  **CONTAINER** answers belong to the kit, which ships components a consumer drops
  into an arbitrary box: the lattice cell (its index, title and paragraph restack
  below 22rem), the staircase step (its number column collapses below 20rem) and
  the FAQ row (the three-column summary becomes two below 24rem) all take
  `container-type: inline-size` on their root with `@container` on the
  descendant.
- **Collapse — three breakpoints, each with one job.** At **1080px** the header
  loosens its column gaps and the hero indent halves. At **860px** the desktop nav
  and its CTA are replaced by a 44px square menu button and a full-height panel;
  every three-column lattice becomes one column with the cell borders moving from
  right to bottom; the bento grid drops its explicit areas. At **620px** the shell
  padding fixes at 18px, the hero centres, and the section rhythm collapses to a
  flat 48px. Nothing in this pack overlaps, rotates or carries a negative margin
  except the hero image, so there is no asymmetry to unwind.
- **Viewport.** Full-height panels use `min-height: 100dvh`. The reference ships
  the older unit as its base with a `@supports` upgrade; this pack does not — see
  Gotchas.

## Motion tokens

Two curves for the whole site, and the second one only ever moves a grid.

| Token | Value | Where |
|---|---|---|
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | reveals, the nav underline, everything the reader triggers |
| `--ease-grid` | `cubic-bezier(0.25, 1, 0.5, 1)` | a cell inverting, and the one ambient gradient |
| `--dur-hover` | `180ms` | fills, borders, the plus rotating |
| `--dur-cell` | `200ms` | a use-case cell inverting on the dark band |
| `--dur-panel` | `240ms` | a capability cell inverting on paper |
| `--dur-nav` | `260ms` | the underline wipe |
| `--dur-reveal-opacity` | `640ms` | a block fading in |
| `--dur-reveal-shift` | `820ms` | the same block travelling `--shift-reveal` (28px) |
| `--dur-stagger` | `110ms` | per step, four steps deep — 0 / 110 / 220 / 330 |
| `--dur-drift` | `10s` | the one ambient loop, alternating |

**Reveal is once, and it is gated so that no reader ever loses content.** The
hidden state is declared under `html.reveal-ready`, and that class is added by
script only when motion is allowed — so a reader with JavaScript off, or with
reduced motion on, never has anything hidden to begin with. An IntersectionObserver
at `rootMargin: 0px 0px -9% 0px` and `threshold: 0.08` adds `is-visible` and then
stops observing, so a block reveals exactly once and never re-plays on scroll-up.
Copy this arrangement rather than the animation.

**Reduced motion is a blanket.** Every duration token collapses to zero, the
stagger goes to zero, the travel distance goes to zero and the ambient gradient
stops. The page keeps every value it was showing.

## Signature motifs

1. **The two-clause headline** — one sentence, two `<span>` blocks, the premise
   in `--ink-faint` and the claim in `--ink`.
2. **The hairline lattice** — three or ten columns of bordered cells, each
   carrying a mono index at the top and its title pushed to the bottom, each
   inverting to solid on hover.
3. **The accent that only exists on hover** — a page whose screenshot has no
   colour in it, until the cursor lands.
4. **Silent looping product video in a 1px rectangle** — the proof is the product
   moving, gated by an observer, paused under reduced motion.
5. **The mono micro-label** — 10px to 11px, uppercase, tracked `0.08em` to
   `0.12em`, `--ink-soft`, naming a section or numbering a step without adding a
   heading level.
6. **The point-cloud halftone** — a photographic image reduced to a dot screen in
   ink on paper, cropped and pulled under the type.

## Signature element

**The four-step staircase.** A vertical stack of four rows in which each row is
3% narrower than the one above it and offset 3% further right, so the block
descends to the right like a flight of stairs, and each row is a step darker:
`--bg`, then `oklch(89% 0 0)`, then `oklch(62% 0 0)`, then `--ink` with paper
text. Rows overlap by exactly `-1px` so their hairlines share an edge. Each row
carries a mono index and one sentence at `clamp(1.2rem, 1.75vw, 1.65rem)` in a
`24ch` measure. On entry the four rows arrive 110ms apart.

It is the signature because it is this pack's whole colour argument rendered as
geometry: **the only ranking device is value**, and here an argument is literally
ranked by how dark it is. Nothing else on the page may use more than two steps of
that ramp, which is what keeps the staircase readable as the one place the
hierarchy is spent.

## Micro-interactions

- **Focus.** `outline: 2px solid var(--accent); outline-offset: 4px`, declared
  once on `:focus-visible` for the whole document. The orange is at 3.02:1 on the
  paper — above the 3:1 non-text floor and nothing more — so the 4px offset is
  load-bearing rather than decorative, and reducing it is an accessibility
  regression rather than a style choice.
- **Hover is fill, border and a 1px lift. Never a scale, never a shadow.** The
  lift is `translateY(-1px)` on the two smaller CTAs and `-2px` on the closing
  one; a lattice cell does not lift at all, it inverts.
- **The nav underline flips its origin** — `right` at rest, `left` on hover — so
  the rule wipes in from the left and retreats to the right instead of collapsing
  to its centre. It is one line of CSS and it is most of why the header feels
  considered.
- **The mobile menu is a full a11y implementation, and it is worth copying whole:**
  `aria-expanded` and a swapped `aria-label` on the toggle, `inert` on `main` and
  `footer` while it is open, a tab loop between the toggle and the last link,
  Escape to close with focus restored, and it closes itself on resize past 860px.
- **The recruiting console.** The reference freezes a `window.tenor` object into
  the page and puts its hiring pitch there — the buyer profiles, a written
  challenge and a five-point proof checklist — so the careers page is a developer
  console. A motif worth stealing for a technical-buyer product, and one that
  costs nothing on the page.

## Bans

- **No border radius. Anywhere.** Not on a button, a cell, a video frame, a chip
  or an input. One corner value is what makes the lattice read as a single
  drawing.
- **No shadows, and no elevation model at all.** Something is either filled or it
  is not. A card with a shadow is a different pack.
- **No second hue — with one named exception, and it is `--good`.** The orange is
  the chromatic budget of the *page*, spent on hover and focus. The pack also
  ships a derived success value at hue 150 for the product surfaces it dresses,
  because a marketing site paints no success state and a dashboard has to. So the
  ban as it stands is: **no hue you did not find in this file**, and the only two
  in it are the orange and `--good`. A screen may carry both; nothing else.

  *This used to read "the orange is the entire chromatic budget", flatly, while
  the Palette section three hundred lines above derived `--good` and said why.
  Measured on a dashboard running this pack, hue 150 appeared **36 times on one
  screen** — checklist marks and success chips — so the ban was being broken by
  the pack's own token on every render.*

  A resting orange fill larger than 25px is out of register. **That number is a
  measurement of the reference's investor lockup, not a limit derived from
  anything** — a product's own lockup will not be 25px, and the rule it stands
  for is *one small resting orange object per screen*. Treat the size as the
  reference's and the count as the rule.
- **No weight above 500, and no weight above 400 in the sans.** Emphasis comes
  from size, measure and fill.
- **No italics.** The reference contains none.
- **Both of the two above need a base layer, because the browser breaks them for
  you.** `<strong>` renders at **700** and `<em>` renders italic with no
  stylesheet involved, so neither violation appears in any CSS a grep can read
  and neither shows up in review. `tokens/tenor.css` ships the reset; emphasis
  resolves the pack's own way, by **value** — `<strong>` takes weight 500 and the
  full `--ink` against prose set in `--ink-soft-aa`, and `<em>` drops the slant
  and takes the ink too. Any pack in this library that bans a weight or a slant
  owes the same three lines.
- **No gradient with a hue in it.** The one gradient in the system is an
  achromatic greyscale wash behind a single feature cell.
- **No centred display type**, except the hero below 620px and the closing panel.
- **No icon set.** The reference ships a wordmark, a menu glyph built from two
  rules, a plus built from two rules and an arrow. A fifth icon needs an argument.
- **No card inside a card.** A lattice cell is terminal; if it needs internal
  structure, it needs a hairline rule.
- **No `height: 100vh`** — it jumps when the mobile address bar moves. Use
  `100dvh` outright rather than shipping the old unit as a base.
- **No scroll-jacking, no parallax, no `animation-timeline`, no scroll library.**
  Verified against the reference: none of them appear. The header's scrolled
  state and the reveal are the entire scroll budget.

## Gotchas

Nine traps, all measured in the reference on 2026-08-14. Six are defects in the
reference itself, which is exactly why a copy of it inherits them.

1. **`--ink-soft` sets body copy and does not clear AA.** At `#777773` it is
   **4.16:1** on the paper, and it carries every lead paragraph and every
   supporting sentence at `clamp(1rem, 1.35vw, 1.25rem)` — 16px at the small end,
   which is not large text. It is short of 4.5:1 by a margin no one will notice
   and every audit will. Reserve it for the mono labels, where it is used at
   tracked caps, and set prose in `--ink-soft-aa`.

   **The remedy this Gotcha used to give was itself short.** It said "darken it
   to at least `#6f6f6b`", which clears the floor on the paper at 4.67:1 and
   reaches only **4.27:1** on `--bg-deep` — a field the pack spends on a whole
   section, so the fix failed on the pack's own second room and did so silently,
   because nobody re-measures a remedy. `--ink-soft-aa` `#6b6b67` is 4.95:1 and
   4.53:1, the smallest step that holds on both. Found by putting the pack on a
   product surface where muted text sits on both fields at once.
2. **`--ink-faint` sets the hero and fails even the large-text floor.** At
   `#a3a29d` it is **2.36:1**, below the 3:1 that large text is allowed. It
   carries the grey half of the headline at 40.8px to 74.4px. The device is worth
   keeping and the value is not: the pack's rule is that the muted clause must
   clear 3:1, which is `#8a8985` or darker on this paper.
3. **The accent clears its floor by 0.02, and the reference puts the wrong label
   on it.** `#e9672a` is **3.02:1** on `#f7f6f2` — legal as a non-text mark, with
   no margin at all, so one step lighter and the focus ring stops being
   conformant. Contrast is symmetric, so a *paper* label on an orange fill is the
   same 3.02:1, and both places the reference fills with orange put one there
   below the large-text threshold: the investor lockup's `Y` at 12.5px, and
   **every CTA at the moment it is hovered**, where the mono label at ~10.4px
   falls from 17.61:1 to 3.02:1.

   **The fix is the label, not the fill.** The coal on that same orange is
   **5.84:1** — it clears AA at any size, on the paper page and on the dark band
   alike, because the orange is the same orange in both. So a hovered control
   changes two properties rather than one: the fill goes to `--accent` and the
   label goes to `--accent-ink`. Nothing has to give up the hover fill, which is
   this pack's most recognisable interaction.

   *This entry used to end differently.* It said the orange may fill only a
   control whose label is decorative or duplicated, and that a control whose
   label is its only statement should keep its ink fill and move its **border**
   to the accent. That workaround was derived from measuring one direction and
   never the other; it is superseded, and a page still following it is not
   wrong, only more cautious than it needs to be.
4. **A variable font is loaded across two axes and used at one point.**
   Instrument Sans is requested as `wdth,wght@75..100,400..600`; the stylesheet
   contains zero `font-stretch` declarations, zero `font-variation-settings`, and
   exactly one weight — 400. The width axis and the 500–600 range are downloaded
   and never used. Request `wght@400` alone unless you are actually going to move
   an axis.
5. **The old viewport unit ships as the base.** The mobile panel is sized with the
   pre-`dvh` unit and upgraded inside `@supports (height: 100dvh)`. On every
   browser that lacks the upgrade the panel jumps as the address bar moves; do
   not carry the base declaration forward — ship `100dvh` and let old browsers
   scroll.
6. **The reduced-motion blanket is safe only because of a clamp.** It sets every
   duration to `0.01ms !important` **and** `animation-iteration-count: 1`, which
   lands an animation on its final frame; without that second declaration a
   `0.01ms` duration strobes an infinite animation rather than freezing it. The
   one infinite loop is then named separately and stopped outright, which holds
   its *first* frame instead. Two correct decisions that look like one; this pack
   ships `0s`, which cannot be misread either way.
7. **A scroll listener drives the header.** It is passive and it toggles one
   class past 12px, so it is cheap — but the doctrine's answer is an
   IntersectionObserver on a sentinel element at the top of the page, which costs
   nothing per frame at all. The reference already uses observers for the reveal
   and for video playback; this is the one place it did not.
8. **The headline breaks are hand-written and managed per breakpoint.** Seven
   display selectors carry literal `<br>` tags whose visibility the stylesheet
   then controls at 620px — one rule hides four of them, a later rule re-shows
   four, and `.visibility-intro h2 br` is in **both lists**, so it is hidden and
   then un-hidden two declarations later. It works, and it is fragile: a
   copy-edit that changes a word length silently changes the shape of the page at
   one width only. Prefer the `ch` measure plus `text-wrap: balance`, which the
   same stylesheet already uses, and keep the manual break for the one line that
   genuinely needs it.
9. **Two ramps that do not match, and five one-off surfaces.** The staircase's
   middle steps are `oklch(89% 0 0)` and `oklch(62% 0 0)` — pure neutrals sitting
   between a warm paper and a warm ink, so they read faintly cool against their
   own field. The video frames carry five more values on no ramp at all:
   `#e9e8e3`, `#f6f8f8`, `#f3f3f0`, `#f6f6f3` and `#171715`. Put the neutrals on
   the warm axis, or accept the cool step deliberately and say so; either way, do
   not add a sixth frame colour.
