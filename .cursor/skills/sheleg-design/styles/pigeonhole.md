# Style pack — Pigeonhole

Origin: <https://www.getinboxzero.com/> (2026), the marketing site of an
open-source AI email assistant. Every value below was read on 2026-08-12 off its
server-rendered HTML for `/` (399,558 bytes), off its two shipped stylesheets
(`/_next/static/immutable/chunks/0dfx_zuu6iahb.css` and `26l20pon7rs4c.css`,
599,990 bytes together, 152 custom properties), and then off **computed styles on
the live page** through CDP at 1440×900, 768×1024 and 390×844 — 912 rendered
elements. Ratios were computed by importing this repository's own palette gate.

A white wall, one blue that only ever appears as a two-stop gradient, a display
face that never goes bolder than 400, one italic word in the headline — and
**nine categories in which a hue *is* the category**, drawn from an eleven-ramp
pastel system and rendered as a two-layer chip: an outer chip in the deeper tint
holding an inner chip in the paler one.

The identity in one sentence: **the label system is the design system.** Not a
page decorated with pastels — a page whose only bespoke colour is a filing
scheme, lifted straight out of the product's own inbox and shown at a size the
reader can actually read.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **a product whose job is to sort the reader's incoming mess
into named categories**: email triage, ticket routing, notification digests, a
file or photo organiser, a CRM inbox, a capture-and-file knowledge tool. It suits
a product whose promise is *your chaos, filed* — where the honest hero is not a
feature list but the same pile shown twice, and where the reader's first question
is *what will it call this?*, answered by showing the labels.

It rides the SHELEG cinematic layer **at the lowest intensity in the family,
alongside [`manpage`](./manpage.md)**: a word-by-word blur-in on the headline,
one entrance per section, and **no scrubbing, no parallax, no sticky nav and no
scroll clock anywhere** — measured, not assumed: the reference has zero elements
with `animation-timeline`, zero `position: sticky` and zero `position: fixed`.

**Not for:** a product whose best argument is the whole application at real size —
that is [`showroom`](./showroom.md). A control plane narrating live telemetry on a
dark field is `instrument-console`. A page whose subject is an accumulating total
is `scoreboard`. A developer product whose buyer wants to see the call is
[`manpage`](./manpage.md) or `datasheet`. And **not** the sorted inbox itself: this is the
marketing page a user lands on before the product they log into, which is
[`workbench`](./workbench.md).

### The fork against [`cyclorama`](./cyclorama.md), which is the one people get wrong

Both are pastel, and that is the whole trap. In `cyclorama` the pastel is a
**field** — a full-bleed backdrop cycling on a 32-second loop behind a fixed
subject, and its meaning is atmosphere. Here the pastel is a **taxonomy**: eleven
hues, nine of them bound to a named category, each appearing only inside a chip
the size of a word, and **none of them ever moves**. One pack colours the room; this
one colours the filing.

The give-away is what happens when you remove the colour. Remove `cyclorama`'s
wash and the page loses its mood. Remove this pack's tints and the page loses its
*information* — which is exactly why the label word is mandatory here and why the
hue is only ever the second channel.

### The fork against [`showroom`](./showroom.md)

Both are white, both are product-led, both put a screenshot in the first
viewport. `showroom` frames the application **whole** and lets a seven-layer
shadow do the lifting — the app is the subject and the page is a gallery wall.
This pack has no framing shadow system at all: 40 of its elements carry the same
single soft shadow (`0 3px 12.9px rgba(151,151,151,0.08)`), and its subject is
not the application but **one row of it, labelled**. If the argument is *look how
good this looks*, use `showroom`. If it is *look what it calls your mail*, use
this.

### The fork against [`orchard`](./orchard.md)

Both are friendly and tinted, and both round things generously. `orchard` works
on **warm oat slabs** with soft-3D pills, and its tint is decoration in service
of approachability. This pack works on **white** with hairlines, and its tint
carries meaning. A warm field says *this is pleasant*; a white field with nine
labelled hues says *this is sorted*.

### The fork against [`workbench`](./workbench.md)

`workbench` is the product UI — a dashboard you log into, standalone, no
cinematic layer. This is the page that sells it. They are adjacent on purpose: a
product using this pack for its marketing page and `workbench` for its
application is a coherent pair, and the chip system is the seam where they should
agree.

## Palette

Ratios recomputed from `styles/tokens/pigeonhole.css` by the palette gate.

| Token | Value | On `--bg` |
|---|---|---|
| `--bg` | `#ffffff` | the field, measured at every viewport |
| `--surface-2` | `#f9fafb` | the alternating section band |
| `--ink` | `#242424` | 15.52:1 — display and every section head |
| `--ink-body` | `#3d3d3d` | 10.86:1 — body copy that carries weight |
| `--ink-soft` | `#6b7280` | 4.83:1 — the dominant body ink |
| `--ink-lede` | `#6b7280` | 4.83:1 — the lede, corrected (see Gotchas) |
| `--ink-faint` | `#9ca3af` | 2.54:1 — **non-text only**: an icon, a disabled glyph |
| `--accent-strong` | `#2965ec` | 5.04:1 — the accent that may carry a word |
| `--good` | `#008931` | 4.54:1 |
| `--warn` | `#9f6d00` | 4.50:1 |
| `--danger` | `#c94244` | 4.83:1 |
| `--info` | `#2965ec` | 5.04:1 — an alias of the accent, on purpose |
| `--surface` | `#ffffff` | the card fill: at field level, separated by hairline |
| `--surface-3` | `#fcfcfc` | the third, barely-there step |
| `--accent` / `--accent-2` | `#2965ec` / `#5c89f8` | the CTA gradient's two stops — a fill, never a word |
| `--on-accent` | `#ffffff` | 5.04:1 on `--accent`, and 3.29:1 on `--accent-2`; see Gotchas |
| `--accent-wash` / `--accent-edge` | `#eff3ff` / `#d9e2ff` | the functional wash and edge — **and they collide with To Reply's two palest tints; see Gotchas** |

The thirty-six tint tokens are not listed here: a table of them would be a
transcription, and `styles/tokens/pigeonhole.css` is the copy to take. What the
table above is for is the functional half — the tokens a component names by hand.

**Status is never by colour alone.** The four status tokens are close under
dichromacy — the gate measures `--danger`/`--good` at ΔE 3.4 and `--good`/`--warn`
at 5.0 under deuteranopia — so every status in this pack carries a word, an icon
or a position as well as a hue. That is not a mitigation bolted on afterwards; it
is the same rule the taxonomy below is built on.

### The taxonomy — the reason this pack exists

Nine categories, measured. Each is an ink plus a four-step tint ramp of its own
hue; the reference's stylesheet declares eleven such ramps, two of which it never
spends on a category.

| Category | Ink | Clears |
|---|---|---|
| To Reply | `--cat-reply-ink` `#0940f3` | 4.51:1 on `--cat-reply-200` |
| Newsletter | `--cat-newsletter-ink` `#6100fb` | 4.52:1 on `--cat-newsletter-200` |
| Marketing | `--cat-marketing-ink` `#007b22` | 4.50:1 on `--cat-marketing-200` |
| Calendar | `--cat-calendar-ink` `#875600` | 4.53:1 on `--cat-calendar-200` |
| Notification | `--cat-notification-ink` `#aa222b` | 4.52:1 on `--cat-notification-200` |
| Cold Email | `--cat-cold-ink` `#00759a` | 4.50:1 on `--cat-cold-200` |
| Team | `--cat-team-ink` `#ba2b00` | 4.53:1 on `--cat-team-200` |
| Urgent | `--cat-urgent-ink` `#a2138e` | 4.54:1 on `--cat-urgent-200` |
| STEP *n* | `--cat-step-ink` `#525252` | 6.26:1 on `--cat-step-200` |

Every ink except the neutral is **DERIVED**: the reference's own inks fail 4.5:1
against the very tints it paints them on, eight of nine of them, and the token
layer marks each derivation at its declaration. The four tint steps per hue are
measured literals.

**Why the hue is only the second channel, with the numbers.** Neither set clears
the bar. As the reference paints them, the worst deuteranopic pair (marketing
against notification) is ΔE **4.42** — already less than half the palette gate's
hard floor of 10, so these hues were never distinguishable to that reader.
Deriving them to clear AA makes it worse rather than causing it: the same pair
falls to **1.24**. Nine hues cannot be simultaneously AA-compliant and mutually
distinguishable to a dichromatic reader, and no re-stepping fixes either number,
because that reader is working with one axis where this system wants nine points.
So the choice is not *accessible colour or legible colour* — it is that colour
cannot carry this meaning at all. The chip's **word** is the category and the hue
reinforces it. A chip without its label is not a quieter chip, it is an unreadable
one.

These tokens are therefore deliberately outside the palette gate's semantic peer
set. When board B-017's widening reaches that set, read this section first: the
exclusion is the design decision, not an oversight.

## Type

Two families, and the display face is both rare and light: over 912 rendered
elements, Geist appears on 878 and the display face on 34.

| Role | Token | Measured |
|---|---|---|
| Display | `--size-display` | 60px at 1440 **and at 768**, 34px at 390 — `clamp(34px, 7.82vw, 60px)`, a ramp fitted to those three readings |
| Display line-height | `--lh-display` | **1** at 1440 and 768 — 60px on 60px, the tightest in the library. **1.25 at 390** (34px/42.5px), which the token layer switches below 768px |
| Section head | `--size-head` | 40px at 1440 and 768, 27.2px at 390 — `clamp(27.2px, 5.21vw, 40px)`, fitted the same way |
| Sub-head | `--size-sub` | 20px/24px |
| Lede | `--size-lede` | 18px/28px |
| Body | `--size-body` | 14px/24px — the dominant pairing, on 59 elements |
| Body large | `--size-body-lg` | 16px/24px |
| Chip label | `--size-chip` | 12px/16px, weight 500 |
| Smallest | `--size-micro` | 10px/15px |

**The display never gets louder.** `--weight-display` is **400** at every size the
display face appears at — never 500, never 600. A heavier display is the single
fastest way to stop looking like this pack, and it is also the value a reference
library got wrong about a different site in this library's history, so it was read
off computed styles rather than assumed.

**One italic word.** The headline's emphasis is a real `<em>` in the display face
at the same size and the same weight, italic — 213px of the 780px column. Not a
colour change, not a weight change, not a highlight, and **exactly one per page.**

**The two ramps are fitted, not copied, and that is a pack decision.** The
reference ships seven `clamp()` declarations and its display resolves from none of
them alone: the widest, `clamp(40px, 5.6vw, 60px)`, yields 43.01px at 768 where
60px was measured, and its 40px floor cannot reach the 34px measured at 390. The
coefficients above are the ones that reproduce all three readings — 7.82vw caps at
exactly 768. Re-measure before trusting either number at a viewport not in the
table.

Body copy sits at `--measure-body` (650px) and the lede at `--measure-lede`
(640px); the display column is wider than both at `--measure-hero` (780px), which
is what lets a two-line headline break where it means to.

## Texture & surface

- **Hairlines, not borders.** `--rule` `#f3f3f3` on 43 elements, `--rule-soft`
  `#f7f7f7` on 19, and exactly one 2px `--rule-strong` `#e3e3e3` on the page.
- **One shadow does almost all the work.** `--shadow-card`
  (`0 3px 12.9px rgba(151,151,151,0.08)`) on 40 elements. `--shadow-hero` is the
  single exception and belongs to the product frame alone.
- **A tinted card's shadow is tinted to its own hue.** `--shadow-tint-a` and
  `--shadow-tint-b` are the measured pair from the green card; the rule
  generalises — mix the shadow toward the card's own tint rather than toward
  black. This is why the page reads coloured while remaining white, and it is the
  detail most often dropped when this look is copied.
- **Radii are a vocabulary, not a scale:** `--radius-chip` 8px outside,
  `--radius-chip-inner` 7px inside, `--radius-control` 13px (and
  `--radius-control-lg` 14px, which the reference uses in-page — see Gotchas),
  `--radius-panel-sm` 20px, `--radius-panel` 32px, `--radius-band` 52px,
  `--radius-pill` 9999px. All seven are measured; the frequencies are 12 for the
  chip pair, 10 for the control, 12 for 20px, 21 for the panel, 8 for the band and
  35 for the pill.
- **Surfaces are barely gradients.** 19 of them carry
  `linear-gradient(var(--surface-grad-from), var(--surface-grad-to))` — white to
  `#f9f9f9`, a fall so shallow it reads as a single tone with a lit top edge.
- **The container is 1152px** with 24px gutters at mobile.

## Components

The reference specifies none of these states — it is a marketing page and paints
one — so `:hover`, `:focus-visible`, `:disabled` and selected are this pack's
decisions, and they are stated rather than left to the reader.

**Category chip — the signature.** Two nested elements. The outer carries
`--radius-chip` (8px) and a `linear-gradient(--cat-X-150, --cat-X-200)`; the
inner carries `--radius-chip-inner` (7px), `linear-gradient(--cat-X-50,
--cat-X-100)`, `--cat-X-ink`, `--size-chip` at `--weight-label`, and 1px of
padding from its parent — which is exactly the 8px→7px step. The label word is
**required**. `:hover` deepens the outer pair by one step. There is no
pressed state, because a chip is a label rather than a control — but a product
whose categories are *filters* needs the state a label does not have, so
**selected** is specified: the inner layer takes its category's `-150` step instead
of `-50`, the outer keeps `-200`, and a 2px inset of `--cat-X-ink` marks it. That is
the one place a chip may carry a border. `:focus-visible` is the button's ring.

**Primary button.** `linear-gradient(var(--accent), var(--accent-2))`,
`--radius-control` (13px), `--on-accent` label at `--size-body-lg`
`--weight-label`, padding 11.7px/22px, and `--shadow-cta` — a shadow tinted to
the accent rather than to black. **Ship the ramp light-to-dark, not
dark-to-light**: the reference runs `#2965ec` → `#5c89f8`, and white clears
5.04:1 at the top and only 3.29:1 at the bottom of the same button. Reverse the
stops so the label's worst case is the passing one. `:hover` **deepens its own tinted
shadow** and translates −1px — never swap it for `--shadow-card`, which is greyer
*and* fainter, so the button would read as sinking. `:focus-visible` takes a 2px
`--accent-strong` ring at 2px offset — the reference ships `outline-style: none`
here, which is the one defect in it a keyboard user meets immediately. `:disabled`
drops to `--surface-2` with `--ink-faint` and no shadow: that pair is 2.43:1, which
WCAG 1.4.3 exempts for a disabled control and which is the only word
`--ink-faint` may ever carry.

**Secondary button.** `--surface` fill, `--rule` hairline, `--ink-body` label,
same radius. `:hover` fills `--surface-2`.

**Panel and card.** `--surface`, `--radius-panel` (32px), `--rule` hairline,
`--shadow-card`. A pastel feature card swaps the fill for its category's 50→100
gradient and its shadow for the tinted pair. Two-column at ≥768px, one below.

**Step card.** A panel whose first child is a neutral chip reading `STEP 1` —
`--cat-step-*`, the same two-layer construction. Three across at 1440.

**FAQ.** A `<dl>`: `<dt>` at `--size-body-lg` `--weight-emphasis`, `<dd>` at
`--size-body` `--ink-soft`, one `--rule` hairline between pairs, two columns
at ≥1024px and one below — the middle breakpoint takes one column, because two
543px columns do not fit inside 720px. **Never `<details>`** — the reference ships 7 `dt`/`dd` pairs in served
HTML, and an answer a crawler cannot read without running JS is an answer that is
not there.

**Nav.** Transparent over the field, `--size-body` at `--weight-label`, a
`--radius-control` primary button at the right, and it **does not stick** —
measured: zero `position: sticky` on the page. Below 768px it collapses to the
wordmark plus one `--radius-control` button, with the links behind a disclosure: at
a 342px container the row does not fit, and this is the only element on the page
whose mobile shape is not a stacked version of its desktop one.

**Logo wall.** A marquee at `--dur-marquee` (100s, linear), logos as SVG at 32px
height, `--ink-faint` treatment. It is the one continuous animation in the pack, and
under reduced motion it is **paused** rather than shortened — see Motion flavor,
because collapsing its duration would strobe it.

## Hero

The first viewport, at 1440×900, holds exactly this and in this order: the nav,
then the display headline centred in a 780px column at `--size-display` with
`--lh-display` 1 — **two lines, and two is the ceiling**; the lede in 640px at
`--size-lede` `--ink-lede`; two buttons side by side, primary then secondary; one
microline of provider marks; and the top of the social-proof line. The product
frame with `--shadow-hero` starts at **y≈713**, which is inside a 900px viewport by
187px: the first screen shows its top edge and nothing more, and the screenshot
itself resolves below the fold. That is the proportion to copy — not *the frame is
below the fold*, which the measurement refutes, but *the frame is cut by it* — and
it is what leaves the headline room to be 60px on 60px.

The display column at 780px against a 1152px container is the pack's proportion:
the headline is narrower than the page, so the eye reads a paragraph shape rather
than a banner.

**Two lines is the ceiling at 1440, and three is correct at 768 and below** — the
display holds 60px down to 768 while the column narrows from 780px to 720px, so the
same headline takes a third line there. Measured at all three viewports. If a
headline needs three lines at 1440, cut the headline.

## Responsive

Measured at three viewports rather than derived from breakpoint names.

| | 1440×900 | 768×1024 | 390×844 |
|---|---|---|---|
| Container | 1152px | 720px | 342px, 24px gutters |
| Display | 60px/60px, 2 lines | 60px/60px, 3 lines | 34px/42.5px, 3 lines |
| Section head | 40px/50px | 40px | 27.2px/34px |
| Lede | 18px/28px | 18px/28px | 18px/28px |
| Body | 14px/24px | 14px/24px | 14px/24px |
| Document height | 11,091px | — | 16,632px |

**Body copy never scales.** 14px/24px and 18px/28px are identical at all three
widths; only the display pair moves. The `clamp()` on the display caps at 768 —
it is already at its ceiling there — so the whole responsive story is: *the
headline shrinks, the columns stack, nothing else changes.*

What stacks below 768px: the two-column card grids collapse to one, the FAQ's two
columns to one, the three step cards to a vertical run, and the hero's two buttons
to full width. The marquee keeps running at the same 100s.

## Motion tokens

| Token | Value | Where it was measured |
|---|---|---|
| `--dur-quick` | 0.15s | the default transition, on 10 elements |
| `--dur-base` | 0.2s | 4 elements |
| `--dur-slow` | 0.3s | 4 elements |
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | every transition but one |
| `--ease-overshoot` | `cubic-bezier(0.175, 0.885, 0.32, 2.2)` | **exactly one element on the page** |
| `--dur-marquee` | 100s, linear | the logo wall — the page's only keyframe animation |
| `--blur-enter` | 6px | SELECTED: the settled state measures 0px and the start value lives in a motion library rather than in CSS |
| `--stagger-word` | 0.04s | SELECTED, same reason — 20 word spans enter in sequence |

## Signature motifs

1. **The two-layer chip.** 8px outside, 7px inside, deeper tint outside, paler
   inside, saturated ink, a word in the middle. Twelve of each radius on the page.
2. **A shadow tinted to its own hue**, never toward black.
3. **The pastel wash card** — a panel whose fill is its category's palest pair, so
   the hue reads as a family resemblance to the chip rather than as decoration.
4. **One italic word** in the display face, once per page.
5. **The hairline instead of a border** — `#f3f3f3` at 1px, 43 times.
6. **The 100-second marquee**, slow enough that a logo wall reads as a fact
   rather than as an animation.

## Signature element

**The two-layer category chip.** It is the one element the page is remembered by
and the one an implementer must get exactly right: the 1px step between 8px and
7px, the deeper pair outside and the paler inside, the ink derived to clear its
own darkest tint, and the label word that makes the hue redundant rather than
load-bearing.

A note on what is **not** a component. The page's set pieces — the chaos-to-order
diptych, the composer with its connector lines, the integration constellation —
are **raster art**, served through the reference's image pipeline at 1152×703,
1150×631 and 1152×539 (≈1.64:1, ≈1.82:1, ≈2.14:1). Fourteen of the page's
`<img>` elements are product art. Specify them as art direction — subject, aspect
ratio, treatment — and never hand an agent "build the diptych", which invites a
DOM technique the reference does not use. The measured page has **zero rotated
elements**: a scattered, tilted pile is not this pack, however much a screenshot
of it suggests otherwise.

## Motion flavor

Entrance and hover, and nothing else. There is no scroll clock: nothing scrubs,
nothing parallaxes, the nav does not stick, `scroll-behavior` is `auto`.

The one motion worth copying is the **headline's word-by-word blur-in** — each
word its own element, entering on `opacity` and `filter: blur()` at
`--stagger-word` intervals, settling at `blur(0px)`. It is 20 elements on the
reference and it is the only place the page spends motion on type.

Everything else arrives once per section and then holds still. `--ease-overshoot`
exists because the reference spends it exactly once; spend it the same way — one
element, never a set.

**The entrance curve is `--ease`, and it is named here because a pack that ships no
curve inherits the motion doctrine's three.** The word-by-word blur-in and every
section entrance run on `--ease`; this pack declares no `--ease-out` because the
reference declares none, and `--ease-overshoot` is reserved for the single element
above.

Under `prefers-reduced-motion: reduce` every duration in the token layer collapses
to 0.01ms, the blur goes to 0, the stagger goes to 0 and the overshoot degrades to
`--ease`. **One case needs more than a duration:** an infinite animation at 0.01ms
does not stop, it strobes — so the marquee is paused with
`animation-play-state: paused` in the component layer, which no custom property can
express. The reference honours reduced motion globally and a pack that regressed
that would be worse than its own source; a duration alone would have regressed it.

## Micro-interactions

- **Chip `:hover`** — the outer gradient deepens one step; 0.15s, `--ease`.
- **Card `:hover`** — `--shadow-card` grows and the card lifts 1px. No scale: a
  scaling card in a grid pushes its neighbours' baselines out of alignment.
- **Button `:hover`** — its own tinted shadow deepens, translate −1px. Stated in
  the same words as Components, because these two sections disagreeing is how an
  implementer ends up choosing for themselves.
- **`:focus-visible`, everywhere** — 2px `--accent-strong`, 2px offset. This pack
  ships it because the reference does not; see Gotchas.
- **The overshoot**, once — a single element may arrive on `--ease-overshoot`.
  Two is a bounce house.

## Bans

- **Never a hue-only chip.** No category may be communicated by colour without
  its word. Status, likewise, is never by colour alone.
- **Never a bolder display.** `--weight-display` is 400. A 600 display is a
  different pack.
- **Never the reference's own category inks.** They fail their own tints; the
  derived set is in the token layer and the numbers are in Gotchas.
- **No scroll clock.** No scrubbing, no parallax, no sticky nav, no
  `animation-timeline`.
- **No rotation.** Measured zero on the reference at three viewports.
- **No shadow as the elevation system.** Hairlines separate; the one soft shadow
  is a hint, not a hierarchy. The seven-layer framing shadow belongs to
  [`showroom`](./showroom.md).
- **No black shadows under tinted cards** — tint the shadow to the card's hue.
- **Never `<details>` for an answer** a crawler should read.
- **No dark theme.** None was measured; inventing one would be inventing values.

## Gotchas

**The reference's own accessibility failures, with their numbers.** Recorded
rather than inherited, each recomputed by the palette gate at write time.

1. **Eight of nine category inks fail 4.5:1 against the tints the reference paints
   them on.** Worst first: `#49d1fa` at 1.53:1, `#d8a40c` at 1.65:1, `#e65707` at
   2.71:1, `#17a34a` at 2.72:1, `#c942b2` at 2.79:1, `#c94244` at 3.09:1,
   `#124dff` at 3.89:1, `#6410ff` at 4.28:1. Only the neutral `#525252` clears it,
   at 6.26:1. Every one is corrected in the token layer and marked `DERIVED`.
2. **The lede ink fails.** `#848484` measures 3.74:1 on white, painted at 18px
   regular — which is not large text under WCAG. This pack ships the reference's
   own `#6b7280` at 4.83:1 instead.
3. **The primary button's label passes at the top and fails at the bottom.** White
   on `#2965ec` is 5.04:1; on `#5c89f8`, the same button's lower stop, 3.29:1.
   Reverse the ramp.
4. **The focused primary CTA has no visible ring.** Computed `outline-style: none`
   with no compensating box-shadow — the resting tinted shadow is all a keyboard
   user gets. This pack's `:focus-visible` exists because of this.
5. **A small badge at 2.31:1.** `#9ca3af` on `#f3f4f6` — the *Coming soon* chip.
   Legible only as decoration, and it is carrying a word.

**Two neutral families ship side by side.** The bespoke ramp
(`#242424`/`#3d3d3d`/`#848484`) carries display and ledes; Tailwind's
`gray`/`slate` defaults carry the dominant body copy — `#6b7280` on 79 elements
against `#848484` on 47. The application's own token block is *unmodified shadcn
slate*, so the entire bespoke layer lives in the marketing page. Do not read the
framework leftovers as brand decisions; both are in the token layer because both
are load-bearing on the page, and `--ink-soft` is deliberately the one that clears
AA.

**Two of the nine chips do not render two layers, and the signature depends on
it.** `--cat-cold-150` and `--cat-cold-100` are the same measured literal
(`#e5f9ff` — the reference repeats the step), so on a Cold Email chip the inner
gradient's foot equals the outer gradient's head and the 8px→7px step is invisible;
its inner fill `#feffff` is one unit off the page white. `--cat-step-50` is
`#ffffff`, identical to `--bg` and `--surface`, so a STEP chip on a white panel
shows only its `#eeeeee`→`#e6e6e6` ring. Both are faithful to the reference, and
both are exceptions to the construction the Signature element calls the thing to get
exactly right. Where a chip must read as two layers on those two hues, put it on
`--surface-2` rather than on the field.

**The functional accent collides with To Reply.** `--accent-wash` `#eff3ff` and
`--accent-edge` `#d9e2ff` are byte-identical to `--cat-reply-50` and
`--cat-reply-100`, and `--accent` `#2965ec` is the same blue family as
`--cat-reply-ink` `#0940f3`. In a pack whose thesis is that the label system *is*
the design system, an accent wash and a To Reply card are the same colour. Do not
place one beside the other; where a surface needs both, the accent takes
`--surface-2`.

**The reference is not consistent about its control radius** — 13px in the hero and
nav, 14px in-page. Both are recorded; pick one per surface and stay with it.

**Its nesting satisfies neither radius rule.** The enterprise band is 52px outer
and 32px inner at 21px of padding: subtraction predicts 31px and a proportional
rule predicts about 32px. This is evidence for board B-020, which is open, and not
a resolution of it. The chip, by contrast, is exactly 8px→7px at 1px — where
subtraction happens to hold.

**Two claims from the screenshots did not survive the DOM**, and they are recorded
because a claim disproved and never written down comes back as folklore. There is
no rotation anywhere on the page. And the before/after diptych is not built from
DOM rows: the words `Before` and `After` appear zero times in the served HTML and
zero times in the live DOM after a full scroll pass — the section is a raster.

**Fluid type does less than it looks like it does.** The *reference* ships seven
`clamp()` ramps; this pack ships **two** — the display and the section head — and
every other size is fixed, body copy included at 14px/24px across all three
viewports. So the whole responsive story is: the headline shrinks, the columns
stack, nothing else changes. The display's ramp caps at 768px, which is why 768 and
1440 measure the same 60px and differ only in how many lines it takes.
