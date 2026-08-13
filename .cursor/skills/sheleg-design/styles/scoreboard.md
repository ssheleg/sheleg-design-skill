# Style pack — Scoreboard

Origin: <https://www.get-ryze.ai/> (2026), the marketing site of an AI ads and
SEO operator. Every value below was read on 2026-08-12 off its shipped
stylesheet (`/_next/static/css/7c091e1bb8e23b8b.css`) and the markup of three
pages — the home page, `/seo`, and `/how-to-connect-claude-to-google-meta-ads-mcp`.
Ratios were computed by importing this repository's own palette gate. Warm
paper, a warm near-black ink, one hot orange that is never a text colour, radii
of two and three pixels, and a **ledger of dotted-leader rows whose numbers are
set in an aliased pixel face**.

The identity in one sentence: **the page is a running tally.** Not a promise
about what the product will do — a dated column of numbers it already did, with
the label on the left, the number on the right, and a line of dots between them
so the eye cannot lose the row.

Contract: widened — all thirteen headings.

## Register

Choose this pack for a product whose argument is **an accumulating number**:
performance marketing and ads operators, SEO and growth tools, affiliate and
revenue dashboards sold on results, agency-replacement services, anything whose
landing page ends in a figure rather than a feature. It suits a product that
reports on someone else's money, where the reader's first question is *how much*
and their second is *since when*.

It rides the SHELEG cinematic layer at low intensity: one dark hero band, an
entrance per section, and a single ambient loop inside the ledger. Everything
else holds still, because a number that moves is a number nobody trusts.

**Not for:** a product with nothing counted yet — a pre-launch page in this pack
is a scoreboard reading zero. A surface where the numbers are the user's own
working data rather than a claim about outcomes: that is the dashboard, and it
belongs to [`workbench`](./workbench.md). A page whose subject is a screenshot
rather than a total — `showroom`. A developer page whose argument is the API call
rather than the outcome it produced — [`manpage`](./manpage.md). Anything editorial or premium-consumer: the
pixel numerals read as arcade furniture the moment there is no metric under them.

### The fork against [`field-notes`](./field-notes.md)

This is the one that will be got wrong, because from a distance the two look
identical: warm off-white paper, one warm orange-red accent, hairline rules,
uppercase mono-ish eyebrows, a light page with a dark passage in it.

The distinction is **what the small type is doing**. `field-notes` sets its
numerals in a mono face to make evidence *auditable* — a provenance label, a
commit, a citation you can go and check; its accent is a rust used on paper, and
its register is a laboratory notebook. `scoreboard` sets its numerals in a
**pixel** face to make results *countable* — a total, a multiple, a delta since
last week; its orange never touches body text at all, and its register is a
tally board.

Route by the question the page answers. *"How do you know that?"* → `field-notes`.
*"How much, and since when?"* → `scoreboard`.

### Against `instrument-console`

Both put numbers on a dark field under a live indicator. `instrument-console` is
a near-black cockpit end to end, and its telemetry is a state the reader is
monitoring *now*. `scoreboard` is a warm paper page with **one** dark band in it,
and its numbers are a record of what has already happened. If the page has no
paper on it, this is the wrong pack.

### Against [`datasheet`](./datasheet.md)

Both set warm off-white paper against a near-black ink with one hot orange that is
mostly a mark, and both put their numbers in a ruled grid. The difference is what
the number is. Here it is a **tally**: an accumulating total, dated, about someone
else's outcomes, and the reader's questions are *how much* and *since when*. In
`datasheet` it is a **single live reading** about the reader — this visit, this
device, this verdict — with no history and nothing accumulating. A dotted-leader
row whose figure is set in an aliased pixel face against a label-over-value cell
in Inter at 11px is the visual tell.

## Palette

Ready-made token layer: [`tokens/scoreboard.css`](./tokens/scoreboard.css) — copy
it verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#FAF9F5` | the paper | — |
| `--surface` | `#FFFFFF` | card, report, table | — |
| `--surface-3` | `#F8F9FB` | the cool well a data panel sits in | — |
| `--surface-cream` | `#FEFEF5` | the one cream band per page | — |
| `--ink` | `#221D16` | body and display — warm, not neutral | 15.88:1 |
| `--ink-strong` | `#0A0A0A` | the numeral, the total | 18.79:1 |
| `--ink-soft` | `#71717B` | labels, meta, secondary copy | 4.58:1 |
| `--ink-faint` | `#9F9FA9` | placeholder and disabled **only** | 2.49:1 |
| `--accent` | `#FF4801` | tick, rule, ring, marker — **not text** | 3.23:1 |
| `--accent-hover` | `#E03D00` | the pressed step of a mark | 4.12:1 — see Gotchas |
| `--action` | `#0A0A0A` | the primary button fill | 18.79:1 |
| `--good` / `--warn` / `--danger` / `--info` | `#007A55` / `#BB4D00` / `#9F0712` / `#1447E6` | status on paper | 5.09:1 / 4.78:1 / 7.93:1 / 6.49:1 |

Four rules carry this palette, and the first two are the pack.

- **The accent is a mark, not a voice — and so is every other orange here.**
  `#FF4801` measures 3.23:1 against the paper and `--accent-hover` `#E03D00`
  measures 4.12:1; neither reaches the WCAG AA floor for a word, and **this pack
  ships no orange that does.** The reference obeys the first half without ever
  saying so: across three pages its orange appears as a 3×18px tick, a
  `::marker`, a focus ring, a selection colour, a link underline and one
  oversized chevron. So a link here is `--ink` with an `--accent` underline, not
  orange text. The accent's one filled use is a selected chip, where
  `--on-accent` `#221D16` sits on it at 4.92:1. Text set in either orange is the
  fastest way to break this pack, and it will look fine to you on your monitor.
- **The action is ink.** The primary button is `--action` with a white label, not
  an orange fill. This is measured, not a safety choice — but it is also why the
  accent survives: the loudest colour on the page never competes with the thing
  you are meant to click. A page in this pack with an orange CTA has two
  primaries and no accent.
- **Status is never by colour alone.** The four paper statuses cluster: the
  accent and `--warn` separate by only 6.3 under protanopia, `--danger` and
  `--warn` by 12.6 at full colour. That is structural — a palette whose accent is
  orange cannot also hold an orange warning apart from it. Every status therefore
  renders as a chip with its word inside, or a row with its label; a bare
  coloured dot is a bug in this pack. The one exception the reference itself
  makes is the live indicator, and it is paired with the words *All systems ok*.
- **The dark band has its own statuses, and they are the measured ones.** On
  `--panel` use `--good-on-dark` `#00D492`, `--warn-on-dark` `#FFB900`,
  `--danger-on-dark` `#FF637E`, `--live-on-dark` `#7BF1A8`. The paper set is
  invisible there and the dark set is invisible on paper: `#00D492` measures
  1.84:1 against `#FAF9F5`. They are two sets, not one set with a filter.

## Type

Three families, and the third one only ever sets digits.

- **Display — Satoshi, 700**, self-hosted (Regular / Medium / Bold / Black).
  Tight: `-0.03em` at 72px, `-0.02em` on section headings. Satoshi is what makes
  the headline read as a brand rather than a UI; substituting Inter at display
  size is legible and anonymous.
- **Body and UI — Inter, 400 with 500 for emphasis**, at a real body size of
  **15px**. Not 16. The page is a report, and a report is set slightly small.
- **Numerals — Press Start 2P**, at one size (15px), and with smoothing turned
  **off**: `-webkit-font-smoothing: none`, `text-rendering: geometricPrecision`,
  `font-variant-ligatures: none`. The aliasing is the point. Antialiased pixel
  type is a blurry novelty face; aliased pixel type is a readout.
- **DK Crayonista is on the reference and is not in this pack.** It is an
  annotation face for one hand-drawn aside; adopting it makes a fourth family
  and changes the register from ledger to scrapbook.

| Step | Size / line-height | Tracking | Weight | Face |
|---|---|---|---|---|
| `--t-display` | 72 / 1.08 | −0.03em | 700 | Satoshi |
| `--t-h1` | 55 / 1.1 | −0.03em | 700 | Satoshi |
| `--t-h2` … `--t-h4` | 24 / 21 / 18 | −0.02em | 600 | Satoshi |
| `--t-lede` / `--t-body` | 19 / 17 | 0 | 400 | Inter |
| `--t-base` | 15 / 1.5 | 0 | 400 | Inter |
| `--t-label` | 14, uppercase | **+0.14em** | 700 | Inter |
| `--t-2xs` | 11, uppercase | +0.1em | 500 | Inter |
| `--t-numeral` | 15 | — | 400 | Press Start 2P |

**The label tracking is not decoration.** `+0.14em` on a 14px uppercase label is
what separates a section marker from a heading, and it is the reason this pack
needs no second display weight.

## Texture & surface

- **The page divides with rules, not with shadow.** A card is `--surface` on
  `--bg` with a 1px `--line-weak` and `--shadow-hairline` under it. `--shadow-card`
  (two layers, 5% and 5%, untinted) is reserved for the one report surface a
  section is built around; `--shadow-lift` is for something genuinely floating.
- **Radii: 1 / 2 / 3 / 6 / 8**, and the page lives at 2 and 3. Across the three
  reference pages, 107 of 143 radius utilities are `rounded-[2px]` or
  `rounded-[3px]`. This is the pack's most copyable and most-often-lost value: at
  8px everywhere it becomes a generic SaaS page with an orange tick on it.
- **Radius arithmetic when containers nest:** an inner radius is the outer minus
  the padding between them. A `--radius-sm` chip inside a `--radius-md` card
  padded by 3px is `calc(6px - 3px)`, not 6px twice. At this scale the error is
  visible precisely because the curves are so small.
- **Spacing is a 4px ramp.** The shell is `--page-max` 1800px, the reading column
  `--content-max` 1260px, gutters 24px and 48px from the medium breakpoint up.
- **The dark band is a surface, not a theme.** `[data-surface="panel"]` swaps the
  field, the ink and the lines; it is applied to the hero and the ledger, never to
  a whole page.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary button** | `--action` fill, `--on-action` label, `--radius-sm`, `10px 20px`, 14px/500 | fill → `--action-hover` over `--dur-fast` | `translateY(1px)` | `--ink-faint` label on `--surface-2`, `cursor: not-allowed` |
| **Secondary button** | `--surface-2` fill at 4% ink, `--ink` at 50%, `--radius-sm`, `6px 12px`, 10–12px/600 | fill one step warmer | as above | as above |
| **Section tick + heading** | a 3×18px `--accent` bar, `--radius-pill`, then 10px gap, then the heading | none — it is a label | — | — |
| **Card** | `--surface`, 1px `--line-weak`, `--radius-sm`, `26px 24px` | border → `--line`; no lift | — | — |
| **Report surface** | `--surface`, `--radius-md`, `--shadow-card`, a 3-dot title bar in `#FF5F57` / `#FEBC2E` / `#28C840` | none | — | — |
| **Ledger row** | label `--t-base`/500 left, dotted 1px leader in `--panel-leader`, numeral right in `--font-pixel` on an 80px column | none | — | — |
| **Input / capture form** | `--surface` fill, 1px `--line-weak`, `--radius-sm`, 46px tall, **17px** text, and a visually-hidden label — a placeholder is not one | border → `--line` | focus-within: `--ring-focus`, a solid 2px accent ring | `--ink-faint` text |
| **Status chip** | **no fill** — the word itself in its status colour on the surface, `--radius-xs`, `2px 8px`, 11px uppercase, **always with its word** | none | — | — |
| **Live indicator** | a 4px square in `--live-on-dark` with a 35%-alpha square behind it, both pulsing, beside its sentence | none | — | — |
| **Nav** | fixed, transparent over the hero band, 13px/500 items in `--ink-soft`, 14px gaps | item → `--ink` | — | — |
| **Loader** | **pack decision:** the ledger row with its numeral column filled by a `--line-weak` block of the same width. Never a spinner where a number will land | — | — | — |
| **Empty state** | **pack decision:** the row survives — label, leader, and an em dash where the number goes, with one `--ink-soft` line saying what will fill it. A scoreboard with no rows is a broken scoreboard; a scoreboard with empty rows is an honest one | — | — | — |

The input's 17px is not a style choice: anything under 16px triggers
zoom-on-focus on iOS, and this pack's body size is 15px.

## Hero

- **A dark band, not a viewport.** `--hero-min-h` is 820px at the large
  breakpoint and the band ends; it does not fill the screen and it does not
  scroll-lock. Sections that do want the viewport use `--section-min-h`.
- **Composition, left to right:** a photograph bled to the full width, a
  `linear-gradient(120deg, …)` green-cast wash over it at 65% → transparent by
  70%, the headline in Satoshi over the wash in a column capped at 38% of the
  shell, and the **ledger panel** on the right.
- **Line ceiling: three.** The reference's headline is three lines by hand
  (`AI runs your / ads, SEO, / and website`) at `--lh-display` 1.08. A fourth
  line pushes the ledger below the fold, which costs the pack its argument.
- **The first viewport contains a number.** Not a logo wall, not a feature grid —
  the ledger, with at least four rows. If the number is not in the first
  viewport, this is not a scoreboard.
- The email capture sits under the headline at 373px wide, single field, inline
  submit. One field: a scoreboard page asks for the minimum.

## Responsive

- **Type steps at breakpoints; it does not slide.** The headline runs
  42 → 55 (768) → **44** (1024) → 72px (1280). The drop at 1024 is real and it is
  correct: that is where the ledger moves beside the headline and takes width from
  it. A `clamp()` here would slide straight through the one breakpoint that
  changes the layout.
- **Breakpoints** 400 / 768 / 1024 / 1280 / 1920px. The last one is the
  reference's own fourth tier for ultra-wide displays, where the shell reaches
  `--page-max` and the ledger gains its 95px label column.
- **The ledger never reflows to two lines.** Below 768 the label column drops to
  75px and the numeral column to 70px; the dotted leader absorbs the difference.
  A wrapped ledger row is not a row.
- **The numeral column is a glyph budget, not a width.** Press Start 2P advances
  a full em per glyph, so at `--t-numeral` 15px the 80px column holds **five
  glyphs** and the 70px mobile column holds **four**. `3.4x` and `+18%` fit;
  `$9,840` is six and `$184.6M` is seven, and both overflow. Two legal answers,
  and only two: shorten the figure (`$9.8K`, `$184M`) or widen `--numeral-col`
  in the token layer for the whole ledger at once. Never wrap, never shrink one
  row's face — the column is what makes the rows a column.
- **The hero stacks** — photograph, headline, capture, then the ledger — and the
  band's padding-top goes 116 → 140px rather than shrinking.
- Full-height sections use `100dvh` via `--section-min-h`; bare `100vh` is banned.
- **Container queries** for the report surface and the ledger:
  `container-type: inline-size`, because both appear inside columns of different
  widths on the same page and neither should size against the viewport.

**The fork against [`roster`](./roster.md), and a router will reach for the wrong one.**
Both serve growth, ads and SEO products, so the category cannot decide it. **The kind of
proof can.** This pack is built around a figure that ticks up — the pixel numeral, the
dotted-leader ledger, the dark band of results — and its reader is watching a number grow.
`roster` is built around a name that appears: an engine's wordmark inside the headline,
client logotypes in labelled industry columns, a score a third party computed. Ask what the
page loses if you delete its proof. If the answer is *the numbers*, it is this pack; if the
answer is *the logos*, it is that one. A page cannot be built around both, and the giveaway
is that `roster` sets its largest figure — *4,000+* — in the same 16px eyebrow as
everything else.

## Motion tokens

- **One curve, `cubic-bezier(0.4, 0, 0.2, 1)`**, and `cubic-bezier(0, 0, 0.2, 1)`
  for anything entering. Both are the reference's; nothing here needs a third.
- Durations `--dur-fast .16s` (buttons, chips), `--dur-base .24s` (nav, panels),
  `--dur-reveal .5s` (section entrance only). **UI transitions stay under 300ms**
  — see Gotchas for what the reference does and why this pack does not.
- **Entrances are a translate and a fade, once.** `--reveal-y` 30px from
  `opacity: 0`, or `--reveal-x` 50px for a side entrance. After a section has
  arrived it does not move again.
- **The scan line is the only loop.** One 1px transparent→30%-white→transparent
  gradient crossing the ledger over `--scan-period` 8s. It never runs anywhere
  else on the page.
- `prefers-reduced-motion` zeroes every duration and stops the scan line. The
  reference ships no such branch; this pack requires one.

## Signature motifs

- **The 3×18px tick before every section heading** — `--accent`, pill radius,
  10px gap. The single most recognisable thing in the pack and the cheapest to
  copy.
- **The dotted leader row** — label left, 1px dotted rule stretching, numeral
  right on a fixed column. It is a table of contents' idiom borrowed for results.
- **Aliased pixel numerals**, at one size, only for figures that are claims.
- **Uppercase micro-labels at +0.14em** with a 4px square bullet ahead of them.
- **Two-and-three-pixel radii** everywhere, including the 1px bullets.
- **One cream band per page** (`--surface-cream`) marking the section that
  changes the subject.

## Signature element

**The ledger.** A dark panel carrying four to eight dotted-leader rows, each
ending in a pixel numeral, under a group label with a pulsing square, with a scan
line crossing it every eight seconds and a dated *Last updated* line at the foot.

It carries the identity because it is the pack's entire argument as one object:
the claim is that results accumulate, so the page shows an accumulation —
itemised, aligned, dated, and rendered in a face that cannot be mistaken for
marketing copy. The pixel numerals are doing the work the rest of the page is
forbidden from doing: they are the only element allowed to be loud, which is why
the buttons are ink, the accent is a tick, and the radii are two pixels.

Spend everything here. A page in this pack with two ledgers has none; a ledger
whose numbers are rounded to marketing figures (*10x! 100M!*) has the form and
none of the credibility, and a reader who cannot find the date under it has been
shown a poster.

## Motion flavor (optional — cinematic packs only)

If you ride more of the SHELEG stack: keep the scroll clock, run the Reveal set
at `--dur-reveal` on the entering curve, and give the hero's photograph **one**
slow parallax drift behind the fixed wash. There is no particle field and no
WebGL in this pack — the ambient layer is the scan line, and it belongs to the
ledger.

The one scrubbed instrument this pack permits is a **count-up on the ledger's
numerals**, tied to the ledger's own entrance and not to the scrollbar: each row
runs from zero to its value once, staggered by row, and never again. The
reference ships the zeros to prove the point. Under `prefers-reduced-motion` the
final values render immediately — a number that arrives late is worse than a
number that never moved.

Formations, act-based scenes and morphing fields belong to the darker narrative
packs. Here the page is a board, and a board holds still.

## Micro-interactions

- **Buttons** transition fill over `--dur-fast` and press to `translateY(1px)`.
  Nothing scales and nothing glows.
- **Focus-visible** is `--ring-focus` — a **solid** 2px `--accent` ring following
  the target's own radius, and `--ring-focus-sand` on `--surface-sand`, the one
  surface where the accent misses that floor. 1.13.0 shipped the reference's
  translucent glow here instead; see Gotchas.
- **Links** are `--ink` with an `--accent` underline, and move the underline to
  `--accent-hover` on hover. The text never turns orange.
- **List markers** are `--accent`. This is one of the few places the raw accent is
  correct, because a marker is not read.
- **Rows** tint to `--accent-wash` on hover in a data table. Ledger rows have no
  hover state at all — they are a record, not a control.
- **The live indicator pulses; nothing else does.**

## Bans

- **Either orange as body text, a heading, or a button fill.** It is a tick, a
  rule, a ring, a marker, and — filled — a selected chip. Nothing else.
- **A translucent focus ring.** Solid, or it is decoration.
- **A second ledger on the page**, or a ledger with a rounded marketing number in
  it, or a ledger with no date under it.
- **Antialiased pixel type.** Without `font-smooth: never` the numerals are a
  novelty face; with it, they are a readout.
- **A bare status dot**, and any status carried by colour with no word beside it.
- **The paper status set on the dark band, or the dark set on paper.** They are
  two sets.
- **Radii above 8px**, and any radius on the ledger's own rows.
- **A spinner where a number will land.** The skeleton is the row.
- Fluid `clamp()` display type; `transition: all`; `100vh`; a second accent; a
  gradient anywhere except the hero's wash.
- Scroll-linked motion on the ledger. It arrives once and then it is a record.

## Gotchas

- **[CORRECTION — 1.13.1] The focus ring 1.13.0 shipped was invisible.** The
  reference's capture form uses a `focus-within` glow — a 20% accent halo with a
  40% border — and 1.13.0 promoted it to the pack's focus treatment without
  measuring it. Composited the way a browser does it (in sRGB, not linear
  light), the halo is **1.29:1** against the paper and the border **1.67:1**,
  against a WCAG floor of 3:1 for a non-text indicator. Both were decoration
  wearing an affordance's name. The ring is solid from 1.13.1:

  | Ring | Value | Role | On `--bg` |
  |---|---|---|---|
  | `--ring-focus` | `#FF4801` | solid 2px, every surface but one | 3.23:1 |
  | `--ring-focus-sand` | `#221D16` | `--surface-sand` only, where the accent misses the floor at 2.97:1 | 15.88:1 |

- **[CORRECTION — 1.13.1] No orange in this pack can carry a link.** 1.13.0
  called `--accent-hover` "the one orange that may carry a link" at 4.12:1 —
  below the same WCAG AA threshold the pack cites two paragraphs earlier to ban
  the accent from text. The argument was right and was not applied to its own
  next sentence. Links are `--ink` with an `--accent` underline.

- **[CORRECTION — 1.13.1] Four status ratios were stated 0.02–0.08 optimistic.**
  They were computed from the OKLCH the colours were selected from rather than
  from the 8-bit hex the token layer actually ships. Restated: `--good` 5.09,
  `--warn` 4.78, `--danger` 7.93, `--info` 6.49. All four still clear AA; the
  point is that they passed the repository's own gate only because its tolerance
  is 0.1, which is exactly how a wrong number survives a green check.

- **The reference sets a positive delta in `#00D492` on white — 1.84:1.** It is
  used at 11px, on the metric cards inside the product screenshots, and it is
  unreadable. This pack keeps the colour, because the reference genuinely uses it,
  and confines it to `--good-on-dark` where it measures 10.21:1. On paper a
  positive delta takes `--good` `#007A55`. Porting the reference verbatim
  inherits an invisible success state.
- **The reference's primary button transitions over 500ms.**
  (`transition-all duration-500`.) That is past the 300ms ceiling in
  `MOTION_DOCTRINE.md` §3 and past the 100–160ms band for press feedback; on a
  large ink button it reads as lag rather than smoothness. This pack pins
  `--dur-fast` at .16s. The measurement is recorded here rather than in the token
  layer so that nobody re-derives it from the reference and calls it a finding.
- **The reference's scan line animates `top`.** A layout property, sixty times a
  second, forever. Rebuild it as `transform: translateY()` on a `will-change`d
  1px element — the same effect, on the compositor. This is a correction, not a
  preference: the doctrine's ban on transitioning layout properties applies to
  keyframes for the same reason.
- **`bg-black` is the reference's button fill.** This pack ships `--action`
  `#0A0A0A`, its own darkest measured surface, because a pure-black fill on warm
  paper reads as an unfinished default — the same reason this library's slop gate
  refuses pure black in a field or ink token. The difference is one step and it is
  deliberate.
- **Satoshi is applied inline, not through a class.** On the reference the
  headline carries `style="font-family:'Satoshi', sans-serif"` while the
  stylesheet loads the four `@font-face` files. If you copy the markup without the
  faces, every display size silently falls back to Inter and the page looks
  *nearly* right — which is worse than looking wrong.
- **Press Start 2P has no lowercase worth using and no currency width.** Budget
  the numeral column in pixels (`--numeral-col` 80px, 70px below the medium
  breakpoint) and right-align it. A `$` or a `%` in this face is wider than you
  expect and will push the column.
- **Values are a snapshot** taken 2026-08-12 from a live production site. Treat
  them as extracted, not eternal.
