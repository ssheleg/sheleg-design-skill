# Style pack — Datasheet

Origin: <https://fingerprint.com> (2026), the marketing site of a device-intelligence
and fraud-detection API. Every value below was read on 2026-08-12 off its live
computed styles at 1440x900 and 500x844 and off its shipped stylesheet
(`/styles.6f4ca5130282f8853ea6.css`), which declares 140 custom properties —
including ten-step ramps for grey, red, orange, yellow, green, teal, blue, purple
and pink. Ratios were computed by importing this repository's own palette gate.
An off-white sheet, a warm near-black ink, one vivid orange, Inter over JetBrains
Mono, radii that nest concentrically from 16 down to 2 — and a **live instrument
ruled out of hairlines at radius 0, which re-skins itself dark when it detects
that the reader is hiding**.

The identity in one sentence: **the page is a spec sheet, and the specimen is
you.** Not a screenshot of someone else's dashboard — an instrument that reads
your own visitor id, your city and your IP back to you while you look at it, and
turns dark the moment it catches you in incognito.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **B2B SaaS whose product is a verdict about the visitor, the
request or the device**: fraud and bot detection, device intelligence, identity
and verification, anti-abuse, payment risk, API products whose value is the
payload they return. It suits a product where the reader's first question is
*what does it actually return*, and the honest answer is to return it on the page.

It rides the SHELEG cinematic layer at low intensity: one word-by-word headline
entrance at the measured 130ms stagger, an entrance per section, and no scrubbing
anywhere. The instrument holds still, because a reading that moves is a reading
nobody trusts.

**Not for:** a product with nothing live to show — if the argument is a whole
application surface at real size, that is [`showroom`](./showroom.md); if it is a
change of state rather than a reading, `cyclorama`. A page whose subject is an
accumulating total rather than a single live record —
[`scoreboard`](./scoreboard.md). A control plane narrating telemetry that changes
while you watch, on a field that is dark throughout —
[`instrument-console`](./instrument-console.md). A developer page whose focal element is a call the reader will write rather than a reading the product returns — [`manpage`](./manpage.md); it sets its body copy in mono too, which this pack reserves for readings.
A product sold on auditability,
whose output is a claim that must be traceable to a source —
[`field-notes`](./field-notes.md). A product whose verdict is a **score with a
grade letter** rather than a row of fields, and which must also show the raw
response a machine received — [`ora`](./ora.md); it is dark by default and
carries no orange, so the two are never confused on a screenshot.
And **not** the product UI itself: this is the
marketing page that embeds a working instrument, not the console the customer logs
into, which is `workbench`.

### The fork against [`field-notes`](./field-notes.md), which is the one people get wrong

Both are off-white technical paper. Both rule with hairlines rather than shadow,
both carry one warm orange-red accent, both set their small type in a mono. They
are not interchangeable, and the test is **what the small type is doing**.

In `field-notes` the mono annotates a *source*: it labels where a claim came from,
so the reader can check it. Its register is *how do you know*. In this pack the
mono carries a *reading*: a visitor id, an IP, a score, a timestamp — values the
instrument produced seconds ago, which the reader cannot check and does not need
to, because the reading is about the reader. Its register is *what did you get*.

The give-away is the dark surface. `field-notes` refuses a dark console on
purpose, because a console makes the reader trust the instrument instead of
reading the evidence. This pack ships one — but only as an **alarm state**, never
as a theme, and that is the second fork: darkness here is a verdict, not a mood.

### The fork against [`instrument-console`](./instrument-console.md)

Both put an instrument at the centre. The difference is which way round the page
and the instrument sit. `instrument-console` is a cockpit: the field is dark
throughout, and the electric accent exists to make a *changing* value readable
while the reader watches. This pack is paper with one instrument set into it, and
its readings are **settled** — a verdict already reached about a visit that
already happened. If the number ticks, use the cockpit.

### The fork against [`blueprint`](./blueprint.md)

Both are light, technical and gridded. `blueprint` is a *drawing*: white stock,
a 32px grid, registration marks, and **no radius anywhere** — the page is a
specification of a thing that does not exist yet. This pack is a *datasheet*: an
off-white sheet with concentric radii from 16 down to 2, describing a thing that
is running right now and printing its output on the page. Zero radius versus a
radius family is the fastest tell.

## Palette

Ready-made token layer: [`tokens/datasheet.css`](./tokens/datasheet.css) — copy
that file verbatim instead of transcribing this table.

| Token | Value | On `--bg` | Role |
|---|---|---|---|
| `--bg` | `#fafaf8` | — | the page field |
| `--surface` | `#ffffff` | — | the alternating band, and every card |
| `--surface-2` | `#f8f8f6` | — | hover fill |
| `--surface-3` | `#f0f0ed` | — | sunken well, switch track |
| `--ink` | `#141415` | 17.62:1 | body, display, cell values |
| `--ink-soft` | `#484946` | 8.67:1 | labels, lead paragraph, navigation |
| `--ink-muted` | `#6b6c69` | 5.06:1 | meta, footer, the trust eyebrow |
| `--ink-faint` | `#8c8c89` | 3.23:1 | placeholder and disabled only, never content |
| `--rule` | `#e4e5e1` | — | every cell wall and section divider |
| `--rule-strong` | `#d9d9d6` | — | the one heavier edge |
| `--accent` | `#f35b22` | 3.17:1 | a mark, a fill, one display word — and the ring only in the alarm state |
| `--accent-deep` | `#be400f` | 5.11:1 | the one orange that may carry a word |
| `--accent-wash` | `#ffeadc` | — | selected cell, hovered row |
| `--action` | `#be400f` | — | the primary button fill |
| `--action-hover` | `#77361c` | — | its pressed and hovered fill |
| `--on-action` | `#ffffff` | — | 5.34:1 on `--action` |
| `--success` | `#165424` | 8.63:1 | detected-clean, verified |
| `--danger` | `#d42035` | 4.95:1 | suspect, blocked |
| `--warning` | `#663d00` | 9.00:1 | degraded, partial signal |
| `--info` | `#0a4c7b` | 8.61:1 | informational reading |

**The accent floor, and it is the rule this pack is most likely to be broken by.**
`--accent` measures 3.17:1 on the field. That clears the 3:1 floor for a non-text
mark and for large text at 24px and above; it does **not** clear AA 4.5:1 for
anything at body size. The reference obeys this in two of its four uses and breaks it in the other two,
and both broken ones are famous. Its orange is one word of a 48px headline (legal —
3.17 clears the 3:1 large-text floor at that size) and a tick (legal — a mark). It is
also **a mono visitor id at 11px**, which is body size and fails, and **a 2px focus
ring**, which clears 3:1 on the field and on white and falls below it on five
surfaces this pack mandates elsewhere. So: where an orange has to carry a word at
body size, that word is `--accent-deep` — the visitor id included. The ring is
`--focus-color`, which is `--accent-deep` on paper and the accent itself in the alarm
state, where every surface clears the floor.

**Status is never by colour alone.** Every status on the reference carries its
word — *Not Detected*, *suspicious* — inside a tinted cell, and this pack requires
the same, because the four statuses do not separate under dichromacy: success and
warning are 4.8 apart under protanopia and 3.7 under deuteranopia, and danger and
success are 3.5 apart under protanopia, against a floor of 8. A tint plus a word
plus, where the row is dense, a glyph. Never a bare dot.

**The light status sets are step 9 of a ramp on step 2 of the same ramp**, which
is the reference's own measured solution: its clean cell is `--green-9` text on a
`--green-2` tint. Danger stops at step 8 because `--red-9` (`#882329`) and the
warning ink (`#663d00`) separate by only 10.0 at full colour, the palette gate's
hard floor. That floor is not strict, so 10.0 would have passed it — by exactly zero
margin, which is a reason to move rather than a reason to ship: two states in one
dark brown is a palette error no label rescues.

**The alarm state's statuses are selected, not measured, and the reason is
arithmetic.** The reference paints no status *text* on its dark surface, so the
set below is this pack's decision, marked as such at every declaration in the
token layer. Danger takes the pink ramp rather than the red one because on a dark
field a red cannot sit beside an orange accent: `--red-6` separates from the dark
accent by 5.2 in OKLab and `--red-5` by 14.3 but then collides with the warning at
9.1 — both under the hard floor of 10. Pink is the nearest hue in the reference's
own system that clears every pair; the set's worst separation is 12.7.

| Alarm token | Value | On `--bg` (`#1a1917`) | Role |
|---|---|---|---|
| `--bg` | `#1a1917` | — | the instrument's dark field |
| `--surface` | `#232321` | — | a cell inside it |
| `--surface-2` | `#2d2d2b` | — | the message panel |
| `--surface-3` | `#141415` | — | the chrome bar |
| `--ink` | `#eeeeec` | 15.12:1 | headings and values |
| `--ink-soft` | `#b7b7b4` | 8.74:1 | secondary values |
| `--ink-muted` | `#a0a09d` | 6.70:1 | labels |
| `--accent` | `#fa7545` | 6.44:1 | the visitor id, and every mark |
| `--success` | `#94cf9a` | 9.75:1 | detected-clean |
| `--danger` | `#f69fb8` | 8.84:1 | suspect — and 6.24:1 on `--danger-weak`, which is `#631634` here |
| `--warning` | `#f2d5a3` | 12.40:1 | degraded |
| `--info` | `#8bc5f3` | 9.52:1 | informational |

## Type

Two families, both self-hosted by the reference: **Inter** (200–700 available;
this pack uses 400, 500 and 600) and **JetBrains Mono** (400–800 available; this
pack uses 500). There is no third face and no serif anywhere.

**The display weight is 500, not 600.** It is the single value a reader of a
second-hand description gets wrong most often, and it changes the whole page: at
48px with -0.0625em tracking, Inter 500 reads as engineered and Inter 600 reads as
an advertisement.

| Role | Size | Line height | Tracking | Weight | Face |
|---|---|---|---|---|---|
| display | 48px | 1.167 | -0.0625em | 500 | Inter |
| title | 36px | 1.222 | -0.0203em | 500 | Inter |
| accented word in a title | 36px | 1.222 | -0.0203em | **600** | Inter |
| figure | 30px | 1 | — | 500 | Inter |
| lead | 16px | 1.5 | — | 400 | Inter |
| body | 14px | 1.5 | — | 400 | Inter |
| navigation | 13px | 1.692 | — | 500 | Inter |
| cell value | 11px | 1.6 | 0.01em | 500 | Inter |
| cell label | 9px | 1.6 | 0.08em | 500 | Inter, uppercase |
| eyebrow | 12px | 1.667 | 0.12em | 400 | Inter, uppercase |
| mono label | 11px | 1.45 | — | 500 | JetBrains Mono |
| verdict chip | 15px | 1.33 | -0.03em | 500 | JetBrains Mono |
| mono badge | 8px | 1 | 0.09em | 500 | JetBrains Mono, uppercase |

**Tracking is a function of size and it runs both ways.** Negative and steep at
display sizes (-0.0625em at 48px, relaxing to -0.0203em at 36px), positive and
wide below 12px (0.08em at 9px, 0.09em at 8px, 0.12em on the 12px eyebrow). A
9px label at neutral tracking is the single fastest way to make this pack look
like a generic admin theme.

**The accented word carries weight and colour together** — 600 and `--accent`
inside a line that is otherwise 500 and `--ink`. One word per heading, never two,
and never a whole phrase.

**Measure:** the lead paragraph holds to two lines at 1248px; body copy runs 60–75
characters. The instrument's own type is never justified and never hyphenated,
because a broken IP address is a wrong IP address.

## Texture & surface

The field is a warm off-white at `#fafaf8`, and the page alternates full-bleed
bands of it against `#ffffff`, separated by a single hairline. Measured on the
reference: adjacent bands carry `margin: -1px` so two touching hairlines collapse
into one. There is no gradient, no grain, no noise and no blur anywhere on the
page.

**Elevation is inset, never dropped.** Cards and the outer frame carry the same
measured two-line inset — a pale top edge and a darker bottom one
(`--lift-card`) — so a surface reads as machined into the sheet rather than
floating above it. Nothing on the reference casts a downward shadow except the
toggle handle.

**The instrument is not a card.** It is a grid of cells whose walls are 1px solid
`--rule` at **radius 0** (`--r-cell`), measured on the reference's own panel: per
side, one hairline, no shadow, no fill change. Rounding those cells is the single
edit that turns this pack into a generic SaaS page.

**The radius family is concentric, and the arithmetic is the reference's own:**

| Token | Value | Applied to |
|---|---|---|
| `--r-frame` | 16px | the outer frame around the instrument |
| `--r-card` | 12px | content cards |
| `--r-inner` | 8px | the frame's inner shell |
| `--r-button` | 6px | buttons |
| `--r-control` | 4px | navigation controls |
| `--r-chip` | 2px | a mono value chip |
| `--r-cell` | 0px | the ruled instrument |

An inner radius is the outer radius minus the padding between them, and the
reference proves it: its 16px frame carries 8px of padding and the shell inside
reads 8px. **16 − 8 = 8.** Never the same radius twice in a nest.

**The grid is 8px** — the reference's own `--grid-base`, and also the rem base it
sets on `html`. Cell padding is `10px 12px`, card padding 12px, button padding
`7px 14px`, the container 1248px, the sticky bar 56px.

## Components

Every state below was read off the reference except where marked as this pack's
decision.

- **Primary button** — fill `--action`, label `--on-action` at 14px/500, radius
  `--r-button`, padding `--pad-button`, a 1px `--action-edge` border — one ramp step
  darker than the fill — and `--lift-action`. Hover and active: fill
  `--action-hover`, which **is** `--action-edge`, so the edge merges into the fill at
  the moment of press; that is the reference's measured behaviour rather than an
  oversight. The label stays white and clears AA in both states. Disabled: `opacity: 0.7` with pointer
  events off, measured. Focus: see Micro-interactions.
- **Secondary button** — transparent fill over `--surface`, label and 1px border
  in `--accent-deep`, same radius and padding, `--lift-control`. Hover: fill
  `--surface-2`, border `--accent-deep`. This is the reference's *primaryOutlined*,
  measured.
- **Ghost / navigation control** — no fill, no border, label `--ink-soft` at
  13px/500, radius `--r-control`, padding `3px 10px`. Hover: label to `--ink`
  over `--dur-base`. Colour only — a nav control in this pack never gains a fill
  on hover.
- **Cards** — `--surface`, radius `--r-card`, `--lift-card`, padding
  `--pad-card`, no border. A card is used for prose and features; the instrument
  is not a card and never becomes one.
- **The instrument (cell grid)** — `--surface` or `--bg`, radius 0, 1px `--rule`
  per side, `--gutter` between cells. Each cell is a label over a value: label in
  the 9px uppercase style in `--ink-soft`, value in the 11px style in `--ink`. A
  status cell tints its whole background with the matching `--*-weak` and sets its
  text in the matching status token, **plus the word**.
- **Mono value chip** — `--r-chip`, padding `0 4px`, the mono face at 15px/500
  with -0.03em, text in a status token over that status's tint. This is where a
  verdict lands: *suspicious*, *bot*, *clean*.
- **Inputs** — this pack's decision, since the reference's home page ships none:
  `--surface`, 1px `--rule`, radius `--r-button`, padding `--pad-button`, label
  above in the 9px uppercase style, error text in `--danger` below with the field
  border switching to `--danger`. Focus takes the standard ring.
- **Navigation** — a 56px bar on `--surface`, no backdrop blur and no shadow
  measured; a single hairline beneath it. Links in the ghost style; the two
  right-hand actions are the secondary and primary buttons at 12px/500.
- **Loaders** — a skeleton whose geometry matches the cell grid it replaces:
  `--surface-3` blocks at radius 0 inside the real hairlines, so the instrument's
  frame never moves when data arrives. No spinner on a data surface. Where a
  reading is genuinely streaming, the value cell holds its label and shows the
  mono badge style reading `MEASURING` rather than an animated ellipsis.
- **Empty states** — the instrument keeps its grid and its labels and fills every
  value with an em dash in `--ink-muted` at 5.06:1 — **not** `--ink-faint`, which
  this pack restricts to placeholder and disabled — plus one line of body copy under
  it saying what would appear. An empty instrument in this pack is still ruled: the
  frame is the promise, and deleting it to show a centred illustration breaks the
  pack.

## Hero

One viewport, four elements, in this order: display headline, lead, two buttons,
instrument. The instrument begins **inside the first scroll** — the reference puts
its top edge 456px down the 894px visible height at 1440x900 — because the page's whole argument is
that the reading is real.

- **Headline** — the display style, centred, **two lines maximum** at a 1248px
  container. Exactly one word takes `--accent` and 600. Three to six words total;
  at seven the 48px size stops reading as a specification and starts reading as a
  slogan.
- **Lead** — the lead style in `--ink-soft`, centred, **two lines maximum**, and
  it names the verdict the product returns rather than the category it belongs to.
- **Actions** — primary then secondary, side by side, `--gutter` apart. Never
  three.
- **The instrument** — the frame at `--r-frame` on `--surface`, 814px wide inside
  a 1248px container, with the reader's own data in it. If the page cannot show
  live data, it shows the last real reading with the mono badge saying so — the
  reference's own badge reads `THIS IS A DEMO. PRODUCTION ACCURACY WILL BE HIGHER`.
  A fabricated reading is the one thing this hero may never contain.

The dashed guides run behind all of it, full-bleed, and the headline sits in the
cell they form. No background image, no illustration, no gradient.

## Responsive

Measured breakpoints, ordered by how much of the stylesheet each carries:
**640px** (1336 rules), 768px, 860px, 1024px, 1200px. 640px is the real one.

- **Fluid type** — the display ramps 48px → 32px and its tracking relaxes with it,
  -0.0625em → -0.021em, both measured. As a clamp:
  `font-size: clamp(32px, 2.2vw + 21px, 48px)`, which passes through both measured
  points. Both endpoints are tokens — `--t-display-min` and `--t-display` — as are
  both tracking values, `--tr-display-min` and `--tr-display`; tracking cannot ride a
  clamp usefully, so it switches at 640px.
- **The headline break is explicit.** The reference ships a break element that is
  `display: none` above 640px and `inline` below it, so the wrap point is a
  decision rather than an accident. Copy that: a display headline in this pack
  never wraps where the browser feels like it.
- **Container** — 1248px with a 20px gutter below 640px, measured.
- **The instrument stacks, it does not scroll.** Its cells go to one column and
  the map cell drops out entirely; a horizontally scrolling data grid on a phone
  is how a reading becomes unreadable. The frame keeps `--r-frame`; the cells keep
  radius 0.
- **The dashed guides collapse to the two outer edges** below 640px. Six vertical
  guides on a 390px screen is noise.
- **Viewport** — use `100dvh` for any full-height section, never the static unit.

- **Container queries.** The **instrument's cell grid** is the one that must: it
  collapses to a single column when *its own* box is narrow, not when the phone is,
  because the instrument is exactly the component a reader embeds in a sidebar. Cards
  follow the same rule. The **navigation** spans the page and stays viewport, and the
  `--1` heading step is page type rather than a component's — **PAGE**, both of them.

## Motion tokens

One ease, one measured base duration, one measured stagger.

| Token | Value | Note |
|---|---|---|
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | the site-wide curve |
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | entrances |
| `--dur-instant` | 0.1s | measured — its fastest transition |
| `--dur-fast` | 0.16s | measured |
| `--dur-base` | 0.25s | measured — its one duration token, `--t-normal` |
| `--dur-reveal` | 0.3s | measured — the headline's per-word rise |
| `--stagger` | 0.13s | measured — between word spans |
| `--reveal-y` | 16px | |

The reference declares exactly one duration token and spends it on 119
transitions, which is why this pack has one base duration rather than a scale.

**Which ceiling governs `--dur-reveal` is worth naming, because it sits on a line.**
`MOTION_DOCTRINE.md` says *UI motion stays **under** 300 ms*, and 0.3s is not under
it. That token is not UI motion: it is the headline's entrance, governed by the
sub-500ms entrance rule, and its value is measured off the reference rather than
chosen. Every token that does drive UI here — `--dur-instant`, `--dur-fast`,
`--dur-base` — is 250ms or less.

**Reduced motion:** every duration and the stagger go to zero and the headline
arrives already in place. The token layer ships that block; the reference ships
one covering a single group of hero animations out of roughly twenty keyframe
sets, which is recorded in Gotchas rather than inherited.

## Signature motifs

1. **Dashed page guides.** 1px dashed `--rule-dash` drawn on the containers'
   own edges, full-bleed, forming the cell the content sits in. The reference
   names these elements *decorators* and puts them at the hero's left and right
   margins and along its section rows.
2. **Label over value, ruled at radius 0.** The 9px uppercase label above the
   11px value, in a cell walled with hairlines. This is the pack's atom.
3. **Uppercase mono micro-badges.** 8–11px JetBrains Mono at 0.09em, in
   `--ink-muted`, stating a condition about the data rather than the product:
   *this is real data*, *this is a demo*.
4. **One word in orange, at 600.** Weight and colour arrive together, once per
   heading.
5. **Status as tint plus word.** The whole cell takes the `--*-weak` fill and the
   verdict is written out. No bare dots, no traffic lights.
6. **Concentric radii.** 16 outside, 8 inside, 12 on cards, 6 on buttons, 4 on
   controls, 2 on a chip, 0 on the instrument.

## Signature element

**The panel that reads the reader's own data back to them.** One frame, set into
the first viewport, containing this visitor's id, city, IP and a verdict — values
produced seconds ago about the person looking at the page. Everything else on the
page is quiet so that this can be the only thing anyone remembers, and its
memorability is not visual: it is that the demo is about *you*.

Its most quoted behaviour is the alarm state. When the instrument detects that the
reader is in incognito, it re-skins itself dark — 134 measured rules — and the
page's argument completes itself without a sentence of copy. Build the light state
first and completely; the alarm state is the reward for having something worth
alarming about.

## Motion flavor

This pack rides the SHELEG layers sparingly, and the scroll clock drives almost
nothing.

- **Particle field:** absent. This page has no atmosphere layer, and adding one
  puts drifting dots behind a table of IP addresses.
- **The one entrance worth copying** is the headline: each word is its own span,
  rising into place over `--dur-reveal` with `--stagger` between them, then
  nothing moves again. Measured delays: 0.000215s, 0.130447s, 0.261s.
- **Reveals:** one per section, opacity and transform only, `--ease-out`, and
  never on the instrument — a reading that fades in reads as rendered rather than
  returned.
- **Scrub:** none. There is no instrument here that narrates state over time; the
  verdict is already reached. If a section genuinely needs scrubbing, it belongs
  in `instrument-console`.
- **The alarm transition** is a state change, not an animation: cross-fade the
  instrument's colour tokens over `--dur-base` and let the layout hold. Nothing
  moves, nothing resizes, no cell shifts by a pixel.

## Micro-interactions

- **Focus** — `outline: var(--focus-ring) solid var(--focus-color)` with a 2px
  offset. The width is measured as `0.25rem` at the reference's 8px rem base and
  applied on 80 separate rules. It is `:focus-visible` and it is never removed.
  `--focus-color` is `--accent-deep` on paper, not the accent: the accent's 3.17:1
  clears the 3:1 non-text floor on the field and fails it on the selected cell this
  same section mandates (2.85:1 on `--accent-wash`). In the alarm state
  `--focus-color` is the accent, which clears the floor on every surface there.
- **Hover on a control** — colour only, over `--dur-base`. Buttons change fill,
  nav links change ink, cells take `--accent-wash`. Nothing lifts, nothing scales,
  nothing gains a shadow it did not have at rest.
- **Selected cell** — `--accent-wash` fill with a 2px `--accent` inset on the
  leading edge. The reference marks its active summary cell exactly this way.
- **Keyboard** — the instrument is a table and behaves like one: arrow keys move
  between rows, the row that has focus takes the selected treatment, and no
  keyboard path animates at all, per the doctrine's frequency table.
- **Disabled** — `opacity: 0.7` and pointer events off, measured. Never a colour
  swap: a disabled status cell that changes hue reads as a different verdict.

## Bans

- **No rounded instrument cells.** `--r-cell` is 0 and it is the pack's spine.
- **No drop shadows.** Elevation is the measured inset pair. A `box-shadow` with a
  positive vertical offset and a blur on a card is not this pack.
- **The accent never carries body text.** 3.17:1. Not a paragraph, not a 14px
  label, not a link in running copy — `--accent-deep` for a word at body size.
- **No second accent.** The reference itself ships two oranges for one job
  (`#f35b22` in the h1, `#ff5e24` in section titles); this pack resolves that to
  one, and adding the other back is drift, not fidelity.
- **No status by colour alone**, and no bare status dot.
- **No dark theme.** The dark surface is `[data-state="alarm"]`, driven by what
  the instrument detected. Wiring it to a user preference or a media query
  destroys the one idea this pack has.
- **No gradient, no grain, no glass, no blur.** Measured: the page has none.
- **No transition on a layout property** — the reference animates `top` and `left`
  in two places and that is a defect, not a licence. Animate transform and opacity.
- **No `ease-in`** in UI, per the doctrine.
- **No `100vh`** — the mobile address bar moves.
- **No scrub, no parallax, no particle field.**
- **No serif.** Two families, and neither has one.
- **Never fabricate a reading.** If the instrument cannot show live data it shows
  a labelled last-known one. A page in this pack that invents an IP address has
  told its only lie in its loudest element.

## Gotchas

**The primary button's label fails AA on the reference, and this pack corrects it
by one ramp step.** Measured: white on `#f35b22` is **3.32:1** at a 14px/500
label. The correction is not a new colour — the resting fill is the reference's
own `--orange-8` (`#be400f`, white at 5.34:1) and the hover is `--orange-9`
(`#77361c`, 9.02:1), so AA holds in both states and the press still darkens. The
reference's own hover already lands on `--orange-8`; only the resting step moved.

**The 8px mono badge is invisible and this pack refuses it.** The reference sets
`THIS IS REAL DATA` in `--gray-6` (`#a0a09d`) at 8px, which measures **2.51:1** on
the field — below even the 3:1 non-text floor, at the smallest size on the page.
`--ink-faint` here is `--gray-7` (`#8c8c89`, 3.23:1) and is restricted to
placeholder and disabled; a badge that must be read takes `--ink-muted` at
5.06:1. Copying the 8px size without the ink step is the trap.

**Two oranges for one job.** The h1's accent word is `#f35b22` (`--orange-7`) and
a section title's accent word is `#ff5e24` (`--orange-gradient`). They are
different colours doing the same thing on the same page. This pack ships
`--orange-7` and states so; if a future measurement finds the reference has
consolidated, this note is the place to correct.

**The reference's ink is not consistent either.** Its `body` computes `#141415`
and its `h1` computes pure black. This pack ships one ink, `#141415` at 17.62:1,
because two near-blacks in one voice is an accident rather than a system — and
because a pure-black ink token is banned by this repository's slop lint as an
unfinished default.

**The focus ring is one ramp step darker than the reference's, and the reference's
own selected cell is why.** Its ring is `--orange-7` at 2px, which clears the 3:1
non-text floor on the field (3.17) and on white (3.32) — and fails it on five
surfaces this pack mandates elsewhere: `--surface-3` (2.91), `--accent-wash` (2.85,
which Micro-interactions requires for a selected cell) and all four status tints
(2.89–2.99). `--focus-color` is therefore `--accent-deep`, which clears every one of
them, worst case 4.59 on `--accent-wash`. In the alarm state no step down is needed:
the accent clears 5.77:1 on the darkest surface there.

**The alarm state's danger tint is step 10, not step 9, and the cell it exists for is
the reason.** The other three alarm statuses tint with step 9 of their ramp. On
`--pink-9` (`#8b1e4a`) the danger text measures **4.44:1** at the 11px value — a
fail, in the one cell the whole alarm state exists to render. `--pink-10`
(`#631634`) measures 6.24:1. The break in the pattern is deliberate, and this is
where it is recorded.

**The rem base is 8px.** `html { font-size: 8px }`, matching its own
`--grid-base`, so every `rem` in that stylesheet means one eighth of what it means
in a default host. This is why the token layer states lengths in px: copying a
`0.9rem` padding out of the reference and into a normal document gives 14.4px
instead of the measured 7.2px. It is also where the odd `7.21px` button padding
comes from.

**Reduced motion is nearly absent.** One `prefers-reduced-motion` block covers one
group of hero bell animations, against roughly twenty keyframe sets including
`scan`, `wiggle`, `pulseRing`, `fieldShake` and `blink`. The token layer supplies
the whole collapse. Do not conclude from the reference's one block that the rest
degrade.

**A `transition` naming a layout property, twice.** The reference transitions
`top` and `left` on two carousel controls. Named here so the next reader does not
measure it and copy it; the ban is in Bans.

**Its palette sits in a default cluster, and this is a measurement rather than
taste.** The palette gate reports this pack's field-plus-accent inside the *warm
cream field with a terracotta accent* cluster that an unguided model reaches for
regardless of subject. That is exactly why `Origin:` above is addressable and
dated: every value here was read off a live production stylesheet, and the gate
passes it only because the provenance is checkable. If a page arrives at this
palette without opening that reference, the default is talking, not the pack.
