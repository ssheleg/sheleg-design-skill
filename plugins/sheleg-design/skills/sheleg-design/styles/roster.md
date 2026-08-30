# Style pack — Roster

Origin: <https://www.babylovegrowth.ai/en> (2026), the marketing site of an AI-search
visibility product — SEO content and backlinks, sold on being recommended by Google and
ChatGPT. Every value below was read on 2026-08-13 off its server-rendered HTML for `/en`
(1,415,414 bytes), off its two shipped stylesheets
(`/_next/static/chunks/5c41227b903d5dae.css` and `9ae1360431bd741f.css`, 466,577 bytes
together, 410 custom properties), and then off **computed styles on the live page**
through CDP at 1440×900, 768×1168 and 390×790 — 5,936 rendered elements at the widest.
Thirty-four `lab()` values were resolved by painting each into a 1×1 canvas and reading
the sRGB bytes back. Ratios were computed by importing this repository's own palette gate.

A white field in a faint grid of squares, hairlines instead of shadows, a pill as the
most frequent shape, a body face set at 68px for the headline and a *different* family
for the section heads — and one orange that may never carry a word.

The identity in one sentence: **the proof is a name, not a number.** The page does not
claim a result; it shows you the roster — the engine whose wordmark sits inside the
headline, the client logotypes sorted into labelled industry columns, the review score
someone else computed — and lets the roster do the claiming.

Contract: widened — all thirteen headings.

Themes: light only — no second block of any kind ships here.
Rank: unordered — 3 status role(s) and no severity ramp; a rank scale is yours.

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
- Motion flavor
- Micro-interactions
- Bans
- Gotchas

## Register

Choose this pack for **a product whose argument is who already carries it**: AI-search
and GEO visibility, SEO and content platforms, agencies, marketplaces, integration-led
tooling — anything whose honest first screen is other companies' marks rather than its
own screenshot. It suits a page whose reader asks *who else uses this*, and it answers by
showing them, sorted.

It rides the SHELEG cinematic layer at low intensity: entrance and hover, two slow
offset floats on the hero art, and **no scroll clock anywhere** — measured, not assumed:
zero elements carry an `animation-timeline`, the document's `scroll-behavior` computes to
`auto` rather than `smooth`, and exactly two elements are positioned — one sticky and one
fixed, both the nav.

**Not for:** a page whose subject is an accumulating figure — that is
[`scoreboard`](./scoreboard.md), and it is the fork worth reading twice. A product whose
best argument is the application at real size is [`showroom`](./showroom.md). A product
whose labels are its *own* taxonomy applied to the reader's mess is
[`pigeonhole`](./pigeonhole.md). An open-source front door whose step one is a command is
`prism`. A page that also spends one orange and also forbids it from carrying a word, but
argues **how the work is organised** rather than who is already on the list —
[`tenor`](./tenor.md); it puts the orange on hover only, refuses radius entirely, and
proves itself with video instead of other people's marks.
And not a warm consumer field: this one is cold white over a framework's greys.
A page whose proof is also a borrowed name, but a name the product **will get you**
rather than one it already has — press placement, trust marks, certification — is
[`nameplate`](./nameplate.md). It is the closest neighbour in the library and the
easiest to confuse from the register alone, so the axis that separates them is
measured rather than argued: `nameplate` is a **square** page (87% of its elements at
zero radius) where the pill is rare and therefore means something, and its body sits
at weight 500 against this pack's 300. Here the pill is the most frequent shape on
the page. If the brief is a grid of client logos, stay; if it is a wall of
publication names set as type, go.

### The fork against [`scoreboard`](./scoreboard.md), which is the one a router will get wrong

Both serve growth, ads and SEO products. A router reading the category alone lands on
`scoreboard` every time, and the category is not the distinction. **The kind of proof is.**

`scoreboard` is built around a figure that ticks up: warm paper, an aliased pixel
numeral, a dotted-leader ledger, a dark band of results. Its reader is watching a number
grow. This pack is built around a **name that appears** — an engine's wordmark inside the
headline, a client's logotype in a column, a score a third party computed and badged. Its
reader is checking who is already on the list.

The give-away is what the page would lose if you deleted its proof. Delete
`scoreboard`'s numerals and there is no argument left. Delete this page's logotypes and
there is no argument left — and no number anywhere replaces them, because the biggest
figure on the page (*4,000+*) is set in the same 16px eyebrow as everything else.

### The fork against [`showroom`](./showroom.md)

Both are white and product-led, and both are chosen when the product is the point.
`showroom` puts the application in the first viewport at real size under a seven-layer
framing shadow. Here the first viewport carries **no product screenshot at all** — a
claim, a black CTA, a review badge — and the product appears far below, inside a step
card, cropped in a browser chrome. And this pack has no shadow system: 101 elements carry
an all-transparent ring composite, which is a shadow slot with nothing in it.

### The fork against [`pigeonhole`](./pigeonhole.md)

Both are white pages built on labelled things, and the labels belong to opposite parties.
`pigeonhole` labels **the reader's own mess** with the product's taxonomy — nine
categories the product invented. This pack's labels are **other companies' identities**,
and none of them is the product's to design: the six industry pills are the only naming
the page does, and every mark under them arrives with its own colours, its own weight and
its own opinion about spacing.

**Motion ceiling:** entrance, hover and two slow floats are its whole budget, and it bans scrubbing, parallax and `animation-timeline`, so `MOTION_INTENSITY` above **4** has nothing legal to buy — it keeps a sticky nav, which is the only difference from `pigeonhole`.

## Palette

Ratios recomputed from `tokens/roster.css`, which sits beside this file.

| Token | Value | On `--bg` |
|---|---|---|
| `--bg` | `#ffffff` | the field, on 169 elements |
| `--surface-2` | `#f0f3f8` | the pale blue-grey section band |
| `--surface-3` | `#f9fafb` | the near-white step under it, on 5 elements |
| `--surface-mint` | `#e8f7f4` | the mint panel |
| `--ink` | `#171717` | 17.93:1 — display, heads |
| `--ink-body` | `#364153` | 10.30:1 — body copy that carries weight |
| `--ink-soft` | `#676f7f` | 5.05:1 — secondary copy, corrected (see Gotchas) |
| `--ink-faint` | `#9f9fa9` | 2.62:1 — **non-text only**, or a disabled control's label |
| `--accent` | `#fa5c12` | 3.18:1 — **a fill and large text only** |
| `--accent-ink` | `#da3d00` | 4.52:1 — the accent that may carry a word |
| `--cta` | `#0f0a0a` | white on it is 19.66:1 |
| `--good` | `#008850` | 4.53:1 |
| `--danger` | `#ec0f28` | 4.50:1 |
| `--link` | `#2470f0` | 4.52:1 — and **4.06:1 on `--surface-2`**, so a link inside a band takes `--ink-body` underlined, at 9.26:1 there |

**Four of the derived colours are white-field only, and this is the pack's sharpest
constraint.** `--accent-ink`, `--good`, `--danger` and `--link` each clear 4.5:1 on `--bg`
and on **none** of the three tinted surfaces this pack ships: on `--surface-3` they measure
4.31–4.33, on `--surface-mint` 4.08–4.11, on `--surface-2` 4.05–4.07. Only `--ink-soft`
survives everywhere (5.05 / 4.83 / 4.58 / 4.54). So a word in one of those four colours
belongs on the white field; inside any tinted panel it becomes `--ink-body`, which is
9.26:1 on `--surface-2`. **That includes the eyebrow** — an eyebrow on the mint panel in
`--accent-ink` renders at 4.10:1, which is the one trap this pack sets for someone who reads
only the Components section.

**Status is never by colour alone, and here the number says why.** An orange accent and a
red danger cannot be far apart: the gate measures `--accent` against `--danger` at **10.2**
at full colour, against a hard floor of 10, and **8.1** under deuteranopia against a floor
of 8. That is the entire margin. So a danger state in this pack always carries its word or
its icon, and so does every other status.

**There is no `--warn`, and that is a decision rather than an omission.** The reference
paints no amber anywhere on the page. A warn here would be invented, not selected, so the
pack leaves it out and says so: a product that needs one adds it, states the value, and
checks it against `--accent` before shipping — the two hues are neighbours.

**The neutrals are a framework's, not the brand's.** The reference computes them in
`lab()` — 7,234 borders at `lab(91.6229 …)`, 458 ink elements at `lab(27.1134 …)` — which
resolve to Tailwind v4's defaults. They are in the token layer because they carry the
page, not because anyone chose them, and the bespoke layer beside them is four near-blacks
and two oranges wide.

## Type

Two families, and the division of labour is the inverse of the usual one.

| Role | Tokens | Measured |
|---|---|---|
| Hero display | `--font-display`, `--size-display` 68px, `--lh-display` 1.176, `--weight-display` | in the **body** face — see below |
| Section head | `--font-head`, `--size-head` 52px, `--lh-head` 1.25, `--weight-head` | Raleway 600, on 6 elements |
| Eyebrow | `--font-head`, `--size-eyebrow` 16px, `--lh-eyebrow` 1.5, `--track-eyebrow` 0.4px | uppercase, `--accent-ink`, the only tracked type on the page |
| Body | `--font-body`, `--size-body` 16px, `--lh-body` 1.75, `--weight-body` | **300** — the dominant pairing, on 44 elements |
| Body, emphasis | `--weight-emphasis` | 600, on 49 |
| Small | `--size-small` 14px, `--lh-small` 1.429 | on 44 |
| Chip | `--size-chip` 12px, `--lh-chip` 1.333, `--weight-label` | 500, on 60 |

**`--font-display` is not a second family.** It is byte-identical to `--font-body`, because
this reference sets its 68px headline in the body face; the other family is `--font-head`.
The token keeps its name so a component written against another pack still resolves — and
setting a section head in `--font-display` silently discards the pack's most distinctive
decision, which is why the name is flagged here and at its declaration.

**The hero is set in the body face and the section heads are not.** Plus Jakarta Sans
covers 5,738 of 5,936 rendered elements including the 68px headline; Raleway covers 78, of
which the six section heads and the sixteen eyebrows are the twenty-two this pack
specifies — the rest are chrome the pack does not model. (`Inter` covers a further 116 and
is given no token: it is a leftover, not a decision.) Copying this pack means accepting that
inversion: a display face that only ever appears at 52px, and a body face that has to
hold a poster.

**The body is light.** Weight 300 at 16px/28px is the page's default paragraph, which is
what keeps a very long page (13,627px at 1440) from reading as dense.

**The display steps; it does not slide.** 36px at 390, 60px at 768, 68px at 1440, and
**neither stylesheet contains a single `clamp()`**. A fluid ramp here would be an invented
value dressed as a measured one.

### What this pack does *not* copy: the heading structure

The reference's `h1` is `.sr-only` — 1×1px, white, `clip-path: inset(50%)`, carrying
*"Grow organic traffic from AI Search on autopilot"* — and the 68px line a reader sees is
a `<span>`. All sixteen `h2`s are the small orange eyebrows. So the document outline says
*eyebrow* where the page says *section head*, and the page's largest text is not a heading
at all.

**This pack teaches the opposite:** the visible display line **is** the `h1`, the section
head **is** the `h2`, and the eyebrow is a `<p>` or a `<span>` above it. A screen-reader
heading duplicated out of sight is two things to keep in sync, and the one a machine
quotes is the one nobody proof-reads. [`manpage`](./manpage.md) makes the same point from
the other end, where its visible label chip is a real `<h2>`.

## Texture & surface

- **The pill is the page's most frequent shape** — 102 elements, computed as
  `3.35544e+07px`, which is a clamped maximum rather than a chosen radius. It belongs to
  labels, chips and industry heads. **Both CTAs are `--radius-control` 12px, not pills.**
- **Radii otherwise:** `--radius-chip` 8px (78), `--radius-control` 12px (77),
  `--radius-card` 16px (46), `--radius-panel` 24px (7).
- **There is no elevation system.** The value on 101 elements is an all-transparent ring
  composite. Separation is by hairline — `--rule` `#e5e7eb` on 7,234 borders,
  `--rule-strong` `#cecece` on 30 — and by pill. Adding a shadow adds a layer the
  reference does not have.
- **The field is patterned, and the pattern is five numbers rather than a file.**
  `--pattern-square` 8.367px at `--pattern-radius` 0.85px in `--pattern-tile` `#f4f6fa`
  (the reference's `#7f99d1` at 12% over white), separated by a white
  `--pattern-stroke` 0.3px on a `--pattern-pitch` of 9.667px. A
  `repeating-linear-gradient` or a small inline data URI reproduces it, so nothing has to
  ship an asset. **34 square logo tiles** at `--tile` 40px or less are scattered over it:
  the tiles are other people's marks, and the grid is what stops them reading as a random
  scatter.
- **Two tinted surfaces and the wide radius have one home each.** `--surface-mint`
  `#e8f7f4` is the callout panel behind a claim (11 elements on the reference);
  `--surface-3` `#f9fafb` is the near-white step under a band (5); `--radius-panel` 24px is
  the corner of both. Anything set on them obeys the white-field restriction in the Palette:
  `--ink` and `--ink-body` are safe there, the four derived colours are not.
- **Gradients interpolate in oklab**, and copying that is the point rather than the
  colours: `linear-gradient(to right in oklab, var(--accent), var(--accent-grad-to))`,
  plus a radial `--accent-glow` behind the hero.
- **Container `--container` 1152px**, measured at 1440 and **capped by the viewport below
  it** — at 768 and 390 the declared max-width is the same 1152px and the rendered width is
  the screen minus its gutter, which is a different statement from "1152px at three
  viewports". `--shell` 1440px is the full-bleed width the patterned bands run to while the
  content stays at 1152.

## Components

The reference specifies none of these states — it is a marketing page and paints one — so
`:hover`, `:focus-visible`, `:disabled` and selected are this pack's decisions.

**Primary CTA.** `--cta` fill, `--on-cta` label at 18px `--weight-cta`, `--radius-control`,
padding 16px 32px, **no shadow** — 19.66:1. `:hover` lightens the fill one step and
translates −1px; `:focus-visible` takes a 2px `--accent-ink` ring at 2px offset;
`:disabled` drops to `--surface-2` with `--ink-faint`.

**Accent CTA.** `--accent-2` fill with a white label is what the reference ships and it
measures **3.43:1** at 16px/600 — a fail. This pack's accent CTA therefore either takes
`--ink` as its label, or stays at large text (≥24px, or ≥18.66px bold). Never white on
orange below that.

**Eyebrow.** `--size-eyebrow` uppercase in `--accent-ink` with `--track-eyebrow`, above a
section head. It is a `<p>`, never an `<h2>`.

**Industry column.** A `--radius-pill` label above a column of client logotypes, six
across at 1440, divided by 1px `--rule` verticals. Logos are greyscale at rest and never
resized to match each other's optical weight — a roster that has been normalised stops
looking like a roster.

**Logo tile.** A `--tile` square at `--radius-control` on `--surface`, 1px `--rule`,
holding one third-party mark. Scattered over the square grid in the hero, gridded
elsewhere.

**Step card.** `--surface`, `--radius-card`, 1px `--rule`: an orange number, a head, body
at `--weight-body`, two check chips, and a product screenshot cropped in browser chrome on
the right. Below it a progress rail of three segments and a prev/next pair — the rail is
the only place this pack shows position.

**Case card.** `--surface`, `--radius-card`, a chart or a portrait at the top, a coloured
`--link` in the title, a quote at `--size-body`.

**Chip.** `--radius-chip`, `--size-chip` at `--weight-label`, 1px `--rule`, an optional
check glyph in `--good`.

**Accordion.** `max-height` over `--dur-accordion`, a `--rule` hairline between rows, no
shadow. The chevron rotates 180°.

**Nav.** Sticky at the top of the page — one of exactly two positioned elements — with
`--surface` fill, a `--radius-control` accent CTA at the right, and a 1px `--rule` bottom
edge that appears on scroll.

**Input — two shapes, and the second lives on a dark panel.** Measured 2026-08-26 by
rendering the reference and reading its four visible fields.

The *light* one is the hero's URL field: **44px tall, zero radius, 16px**, a transparent
background and **no border of its own** — it sits inside a bordered wrapper ruled by
the pack's own `--rule`, which the render resolved to the same `#e5e7eb` the token layer
carries. `#e5e7eb` measures 1.24:1 on `#ffffff`: a rule rather than a mark.
Its text is `--ink`, which is 17.93:1 on `--bg`.
Its placeholder is `--ink-faint`, which WCAG exempts as a placeholder and which this
pack forbids as live text.

The *dark* one is the closing form's email and URL fields: **52px tall, 12px radius,
14px, `0 16px` padding**, filled with **white at 8%** and bordered with **white at 15%**
on the dark panel. The two shapes are not interchangeable — the zero-radius one belongs
to a field standing on the white sheet, the 12px one to a control on ink.

**Loaders — none, and that is the answer.** The reference runs exactly three perpetual
animations and none of them is a loader: `ebook-float-primary`, `-secondary` and
`-tertiary`, at 5.5s, 6.5s and 7.5s, which drift the ebook mockups. There is no async
surface on the page to wait for. If you build one, the pack's Motion tokens have no
loader duration to spend, and inventing a shimmer here would be the only perpetual motion
on a page whose whole budget is entrance, hover and two slow floats.

**Empty states — none, and for the same reason.** Three forms and no data surface: there
is nothing on this page that can be empty. A product built on this pack that *does* have
one should take the `--surface-2` band, a `--rule` hairline, body copy at `--ink-soft`
and no illustration — the page's own vocabulary for a quiet region — but that is an
extension of the pack rather than a reading of it, and it is marked as one here.

## Hero

The first viewport at 1440×900 holds, in this order: the sticky nav; the display headline
centred at `--size-display` over two lines, whose second line carries the accent phrase in
`--accent` and **one third-party wordmark set inline after the word "from"**; a two-line
lede in `--ink-soft`; a single `--cta` button; a money-back line at `--size-small`; and a
third-party review badge. The square grid runs behind all of it with logo tiles scattered
over it.

**No product screenshot appears above the fold.** That is the pack's proportion: the first
screen spends its space on the claim and on other people's marks, and the product itself
arrives 1,400px later inside a step card.

Two lines is the display's ceiling here. At 390 the same headline takes three at 36px.

## Responsive

Measured at three viewports rather than derived from breakpoint names.

| | 1440×900 | 768×1168 | 390×790 |
|---|---|---|---|
| Display | 68px/80px, 2 lines | 60px/70px | 36px/54px, 3 lines |
| Eyebrow | 16px | 16px | 14px |
| Container | 1152px | 1152px capped by the viewport | 1152px capped by the viewport |
| Document height | 13,627px | 15,602px | 16,686px |

The industry wall goes six columns → three → two, and its hairline dividers survive every
step, because the divider is what makes it a wall rather than a pile.

- **Viewport.** Full-height sections use `100dvh`, never bare `100vh` — and the reference
  is the argument rather than the authority here: it ships `100dvh` once and `80dvh` twice
  while leaving **13 bare `100vh`** in its stylesheets, which is the address-bar jump the
  rule exists to prevent, on a page whose mobile document is 16,686px tall.
- **Container queries.** The **industry column** and the **step card** are the container
  cases: both are dropped into grids of different widths on the same page, so each takes
  `container-type: inline-size` and its own contents answer to that box — the column's
  logo rows and the step card's screenshot-versus-text split. The **case card** is the
  same kind. The **hero**, the **nav** and the display's own steps are **PAGE**: they are
  the page's opening viewport and its chrome. And the pattern grid's tile density is
  **SELF** — the property sits on the element that would establish the container, so it
  cannot query its own width and it stays a viewport rule.

## Motion tokens

| Token | Value | Where it was measured |
|---|---|---|
| `--dur-quick` | 0.15s | 54 elements — the default transition |
| `--dur-base` | 0.2s | 4 elements, opacity |
| `--dur-slow` | 0.3s | opacity reveals |
| `--dur-reveal` | 0.5s | 3 elements: the section entrance |
| `--dur-accordion` | 0.7s | the one `max-height` transition on the page |
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | **every** transition on the page |
| `--dur-float-a` | 5.5s, ease-in-out | `ebook-float-primary` |
| `--dur-float-b` | 6.5s, ease-in-out | `ebook-float-secondary` — and the one-second offset is the whole effect |

## Signature motifs

1. **A third party's wordmark set inside the headline** — the engine's own logotype after
   the word *from*, at display size, in its own colours.
2. **The industry-column logo wall** — six pill-labelled columns, hairline dividers, real
   logotypes at their own optical weights.
3. **The faint square grid with tiles scattered on it** — a pattern that makes a scatter
   read as an index.
4. **The orange eyebrow**, uppercase and tracked, as the only tracked type in the pack.
5. **Two floats at 5.5s and 6.5s**, offset so the pair never syncs.
6. **The hairline as the whole elevation system.**

## Signature element

**The industry-column logo wall.** Six pill labels, six columns of other companies' marks,
1px dividers. It is the element the page is remembered by and the one an implementer must
resist tidying: equalising the logos' optical sizes, tinting them to one colour, or
dropping the dividers all turn a roster into a decoration. Greyscale at rest is the only
normalisation allowed.

A note on what is **not** a component: the hero's inline wordmark is **art direction**. It
was sampled seven times across 5.4 seconds with no change, so this pack specifies **one
mark, chosen per page** and makes no claim that it rotates. If a later reading catches a
carousel, that is a correction with a measurement beside it.

## Motion flavor

Entrance and hover, plus two floats. The floats are the only continuous motion and they
exist to keep the hero art from reading as a screenshot; at 5.5s and 6.5s they drift out
of phase, which is why both tokens exist instead of one.

Every **transition** on the page runs on `--ease`, and the pack names it here because a
pack that ships no curve inherits the motion doctrine's three. The two floats are
**animations**, not transitions, and they run `ease-in-out` — the one curve in this pack
that `--ease` does not govern, stated because the exception is otherwise invisible.

Under `prefers-reduced-motion: reduce` the token layer collapses **five** of its seven
durations to 0.01ms and deliberately leaves `--dur-float-a` and `--dur-float-b` at their
measured values, because those two drive **infinite** animations and **0.01ms does not stop
an infinite animation — it strobes it.** Measured in Chrome 151: an infinite animation at
`0.01ms` yields two different computed transforms when sampled 40ms apart, while the same
animation at **`0s` yields `none` and never moves.** So a duration *can* stop an infinite
animation, but only at exactly zero, and 0.01ms — which is what a global reduced-motion
rule usually writes — is the value that strobes. This pack pauses the floats in the
component layer instead, with `animation-play-state: paused`, which no custom property can
express and which holds whichever number the durations carry. That lesson is one release old and it is applied here rather
than relearned. **The kit ships that rule; a bundle-only implementer has to write it**, and
this paragraph is the whole of it.

## Micro-interactions

- **Logo tile `:hover`** — greyscale lifts to full colour over `--dur-quick`. Nothing
  moves: a mark that jumps is a mark you read as an advert.
- **Card `:hover`** — the hairline goes `--rule-strong`. No shadow, because there is no
  shadow system.
- **Button `:hover`** — the fill lightens one step, translate −1px.
- **`:focus-visible`, everywhere** — 2px `--accent-ink` at 2px offset. Not `--accent`:
  3.18:1 is too little for a ring a keyboard user has to find.
- **Accordion** — `max-height` over `--dur-accordion`, chevron 180°.
- **The progress rail** — the active segment fills over `--dur-slow`; it never animates
  backwards.

## Bans

- **Never white on `--accent` or `--accent-2` below large text.** Both fail AA there,
  and Gotchas carries the two measurements.
- **Never a status by colour alone.** `--accent` and `--danger` are 10.2 apart, which is
  the hard floor and nothing more.
- **Never an invented `--warn`.** The reference paints no amber; add one deliberately or
  not at all.
- **No shadow as an elevation system.** Hairline and pill.
- **No scroll clock** — no scrubbing, parallax or `animation-timeline`. Measured absent.
- **Never normalise the roster.** No equalising logo sizes, no single-colour tinting, no
  dividerless wall.
- **Never a hidden `h1`.** The visible display line is the heading; see Type.
- **No dark theme.** None was measured.

## Gotchas

**The reference's own failures, with their numbers.** Recorded rather than inherited, each
recomputed by the palette gate at write time.

1. **The nav CTA's label fails.** White on `#f25533` at 16px/600 measures **3.43:1**. The
   hero's black CTA measures 19.66:1, so the page's own hierarchy already had the answer.
2. **The headline's accent phrase passes only because it is huge.** `#fa5c12` on white is
   **3.18:1** — legal for the 68px phrase as large text and illegal for anything smaller.
   The reference's *other* orange, `#f25533`, is the one on the nav fill (item 1); between
   them the page has two oranges and neither can carry a word.
3. **The dominant secondary ink fails on its own band.** `#6a7282` measures 4.84:1 on
   white, and `#6a7282` on the `#f0f3f8` band it is actually painted on is **4.35:1**.
   `--ink-soft` is the darkened form and clears both.
4. **Reduced motion covers six animations out of roughly twenty.** The branch names classes
   one by one — `.pricing-card-enter`, `.pricing-price-swap`, `.promo-rotate-in`,
   `.ebook-float-primary`, `.ebook-float-secondary`, `.promo-animated-gradient` — while
   `arrow-nudge`, `skeleton-blink`, both spinners, `settings-ripple`, `meta-preview-float`
   and the accordions keep running. A per-class list is a list somebody has to remember to
   extend; this pack collapses unconditionally instead.
5. **The review badge's greens are a third party's.** `#00b67a` and `#2ee5ac` arrive inside
   an embedded widget. They are not in this pack's palette and should not be matched.

**Four near-blacks and two oranges ship side by side.** `#2c2f2e` (42 elements), `#212427`
(34), `#171717` (30), `#0f0a0a` (the CTA); `#fa5c12` and `#f25533`. The pack ships one ink
and one accent and marks both as selected. If a value here looks arbitrary, that is
because the choice was between four arbitrary values and the criterion is written at the
declaration.

**The grid is the reference's `squares-bg-1.svg`**, a 480×572 file of `<rect>`s, and the
pack deliberately does not point at it: a token holding `url("squares-bg-1.svg")` resolves
to nothing in anybody else's tree and paints silently, so the five measured numbers are in
the token layer instead. The filename is here only so the two can be compared.

**A cream `#f6f1eb` appears twice** and the pack does not adopt it. Two elements is not a
surface.

**The `52px` section head has no small-viewport measurement in this pack.** Only the
display's three steps and the eyebrow's two were captured; the head was measured at 1440
only. Stated rather than interpolated.
