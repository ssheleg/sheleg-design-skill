# Style pack — Paperclip

Origin: <https://paperclip.ing>. Read 2026-08-14 from the two shipped
stylesheets — `/_next/static/chunks/0sw-z-v7xc9dd.css` (the product and shell
layer, 622 rules) and `/_next/static/chunks/19xj4kovk13jy.css` (the landing
layer, 712 rules) — plus the hero's inline SVG and the `@font-face` block. Both
themes read; the shipped page carries `data-theme="dark"`.

A **neutral coal field with no functional colour at all**, and one loud
chromatic object floating on it. Every control is monochrome: the primary
action is the inverted field, a card is a hairline, a status is a word with a
dot beside it. Colour arrives twice and neither instance can be clicked — the
hero artwork, a curtain of 96 gradient **capsules**, and a row of section
badges, each a two-stop ramp under a noise tile. The shape language is the
paperclip's own: a stadium with fully rounded ends, spent on the button, the
badge, the org node and the schedule dot alike. The type is a tight grotesque
over a plain one over a monospace — Inter Tight, Inter, JetBrains Mono — and the
token names are a stationery catalogue (`--bond`, `--manila`, `--parchment`,
`--graphite`, `--aluminum`) because the product is named after office supply and
says so in its own variables.

Contract: widened

## Register

Choose this pack for products that ask a person to **run something that runs
itself** — agent teams and orchestrators, autonomous back-office, scheduler and
cron surfaces, workflow and job runners, budget-governed compute, anything whose
screenshot is an org chart, a swimlane or a ledger of what a machine spent. It
suits a page that must alternate between a marketing claim and a product mock on
the same scroll, because the mock is built from the same three faces and the same
hairline as the page around it: there is no seam where "the design" stops and
"the app" starts.

Standalone: it does **not** ride the SHELEG cinematic motion layer. Its whole
motion budget, counted: one artwork entrance and one copy entrance behind it;
one native scroll-driven parallax; one marquee; a per-section reveal on a single
140ms stagger; two ambient loops on a running trace; a 1.2s bar fill; a 0.3s
copy-confirmation pop; a 0.4s spring on the one chip that arrives uninvited; and
a modal that rises in 0.25s over a scrim that fades in 0.15s. Ten things, none
of them longer than the bar fill except the marquee — so `MOTION_INTENSITY`
above **5** has nothing legal to buy.
There is no particle field here and adding one would drown the only chromatic
object the page owns.

**Not for:** products with a brand hue. There is no accent colour in this
system — the accent is the inverted field — so a brand red has nowhere to live
except the ornament layer, where it would sit beside eleven other gradients and
stop being a brand. Not for warm, friendly or consumer registers, which
[`orchard`](./orchard.md) owns: this field is a neutral `#0a0a0a` and the copy
around it is set in a grotesque at −0.035em. Not for a page whose argument is a
photograph or a physical object — the entire visual vocabulary is a rounded
rectangle. Not for dense multi-series analytics: four status colours and one
white bar fill is the whole chromatic vocabulary of the data layer, and a fifth
line on a chart has nowhere to come from.

**Two neighbours it is genuinely confusable with.**
[`instrument-console`](./instrument-console.md) is also near-black with mono
telemetry — take it when the page is a *readout* and one electric blue is doing
functional work: a live value, a threshold, a trace. Take Paperclip when the
colour must be ornament and the readout is monochrome, and when the product
being sold is a **team of workers** rather than an instrument.
[`workbench`](./workbench.md) shares the elevation model exactly — borders,
never shadows — and is the better choice for the application itself, in either
theme, at data density. Take Paperclip for the page that sells that application:
`workbench` has no hero, no ornament layer and no marquee, and this pack's whole
composition is the argument that the boring monochrome console behind the
marketing page is the same object.

[`awning`](./awning.md) reaches the same conclusion from the opposite field: it
also refuses functional colour outright and also makes every control monochrome,
but its forecourt is **pure white**, its accent is black rather than an inverted
coal, and it spends nothing on ornament at all — where this pack's whole
chromatic budget goes into a curtain of gradient capsules, Awning's goes nowhere,
so the only colour on its page is the product screenshot. Take Awning when the
product is infrastructure other businesses resell on, and Paperclip when it is a
thing that runs itself.

**And one a screenshot will not separate.** [`ora`](./ora.md) is also dark by
default, also refuses a brand hue, also sets every machine fact in a monospace,
and also spends its accent as the inverted field. Three tests tell them apart.
**Colour:** Ora has none beyond a status set and a six-step verdict ramp, and
every one of those carries meaning; this pack has a great deal of it and none is
functional. **Type:** there a serif does the sans job and every human sentence is
a serif; here there is no serif at all — a tight grotesque over a plain one over
a monospace. **What the page renders:** a machine's verdict *about the reader*
there, against *a team the reader is running* here. A number with a grade goes to
Ora; an org chart, a schedule and a ledger stay here.

## Palette

Ready-made token layer: [`tokens/paperclip.css`](./tokens/paperclip.css) — copy
that file verbatim instead of transcribing this table. Dark is the default and
light is the twin, which is the reference's own arrangement.

**Dark — the default theme.**

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#0a0a0a` | page field, neutral coal | — |
| `--surface` | `#171717` | the default container — card, popover, panel | 1.10:1 |
| `--surface-quiet` | `#262626` | chip fills, bar tracks, quiet segments | 1.31:1 |
| `--terminal` | `#1f1d1a` | the shell block — **the only warm surface in the pack** | 1.18:1 |
| `--terminal-head` | `#161412` | the terminal's own title bar | 1.08:1 |
| `--ink` | `#fafafa` | primary text, and THE accent | 18.97:1 |
| `--muted` | `#a1a1a1` | every caption, lede, description and mono line | 7.66:1 |
| `--border` | `#ffffff1a` | container edge — alpha, so it works over any surface | — |
| `--border-strong` | `#ffffff26` | an input's edge, one step up so it can be found | — |
| `--accent` | `#fafafa` | the single functional accent: the inverted field | 18.97:1 |
| `--accent-ink` | `#0a0a0a` | text ON the accent | — |
| `--good` | `#34d06f` | done, healthy, within budget | 9.80:1 |
| `--warn` | `#fbbf24` | todo, waiting, an interrupt | 11.86:1 |
| `--danger` | `#fb2c36` | blocked, failed, over budget | 5.20:1 |
| `--info` | `#60a5fa` | running, in progress, live — **derived, see below** | 7.79:1 |

**Light — the twin.** Same roles, and the status set drops to the base half of
each ramp, which is the reference's own rule.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#ffffff` | paper | — |
| `--surface` | `#ffffff` | **the same white** — there is no surface step here | 1.00:1 |
| `--surface-quiet` | `#f5f5f5` | the only fill that is not the page | 1.04:1 |
| `--ink` | `#0a0a0a` | primary text | 19.80:1 |
| `--muted` | `#737373` | captions | 4.74:1 |
| `--border` | `#e5e5e5` | the hairline that does all the work | 1.26:1 |
| `--good` | `#22c55e` | done | 2.28:1 |
| `--warn` | `#f59e0b` | todo | 2.15:1 |
| `--danger` | `#dc2626` | blocked | 4.83:1 |
| `--info` | `#2563eb` | running | 5.17:1 |

**In light there is no elevation ladder at all.** `--background` and `--card`
are both `#ffffff` in the reference, so a card is separated from the page by a
1px `#e5e5e5` hairline and by nothing else — no fill step, no shadow. That is
not an oversight to repair: it is why the light theme reads as a sheet of paper
with rules drawn on it, and adding a grey card fill turns the pack into a
generic dashboard in one commit.

**`--info` is derived, and this is the one place the reference is repaired.**
The dark theme block overrides five *icon* status colours and leaves the four
base status colours at their light-theme values, so `--status-task-in_progress`
stays `#2563eb` on the coal field — **3.83:1**, below AA — and the app sets it
as text (`● 1 live` in the sidebar). This pack ships `#60a5fa`, the 400 step of
the same blue ramp, at 7.79:1. Marked DERIVED at the declaration in the token
layer so it is never read later as a measured value.

**Status is never by colour alone.** In dark all four clear AA and may be set as
text. In light `--good` and `--warn` sit at 2.28:1 on `--bg` and 2.15:1 on paper, below
the 3:1 non-text floor, so there they are bar fills, dots and chip tints and the
*word* carries the meaning — which is exactly what the reference does: its
status pill is a coloured chip **with the state written in it** (`In Progress`),
its trace lines are `passed` / `done` / `running` in words, and its org node
announces itself with an `Active` chip rather than a green ring alone. The
measured separations that make this mandatory rather than stylistic: `--good`
and `--warn` separate by 6.2–6.4 under protanopia and `--good` and `--info` by
6.7 under tritanopia, all below the 8.0 dichromacy floor. The word is not
decoration on those pairs; it is the message.

**The chromatic layer is ornament, and the rule is one sentence.** Twelve badge
gradients and one hero artwork carry every colour on the page, and **neither is
ever interactive**. A gradient that can be clicked, hovered or focused has left
this pack. The corollary matters more: because colour is spent entirely on
things that do nothing, an agent reading the page learns that anything coloured
is scenery — so the four status hues, used sparingly and always with a word,
land with full force.

**The twelve badges ship with their own ink.** Each pair carries the label
colour the reference chose for it, hand-picked per gradient rather than
computed, because a 90° ramp has two ends and one label has to clear both:
`g01` white on `#dc2f68 → #1f7a3a`, `g02` `#2a1530` on `#c9a9e8 → #ee79a1`,
`g04` `#3d3010` on `#f3e6c4 → #e3a21a`, `g07` `#1a2a40` on `#7eb6e3 → #ee79a1`,
`g08` `#2a2340` on `#9ce8a7 → #bd7ff0`, `g10` `#1a3a38` on `#f2d95f → #4fbcba`,
and white on the remaining six. Do not compute the ink from one end; do not
reuse a gradient twice on one page.

## Type

Three families, and the display face is a **grotesque wearing a serif's token
name**: the reference declares `--font-serif: var(--font-inter-tight)`. The name
is inherited from a previous system and it is wrong. The role is display.

The pack declares three font tokens — `--font-display`, `--font-body`,
`--font-mono` — and no others. The reference's own names are given beside them
because you will meet them in its stylesheet, not because this pack ships them:
`--font-serif` and `--font-sans` resolve to **nothing** in this token layer.

| Face | Pack token | The reference's name | Where | Weights loaded |
|---|---|---|---|---|
| Inter Tight | `--font-display` | `--font-serif` | every headline, every card title, every proper name, the wordmark | 500 / 600 / 700 |
| Inter | `--font-body` | `--font-sans` | every sentence: lede, description, body, footer link | 400 / 500 |
| JetBrains Mono | `--font-mono` | `--font-mono` | every machine fact: section badges, step numbers, handles, cadences, axis marks, terminal, column headings | 400 / 500 |

**The rule the three encode: display is *tight*, body is *plain*, mono is
*small and tracked open*.** A headline at −0.035em and a caption at +0.08em are
the two ends of the pack, and nothing sits between them by accident. A handle,
a schedule (`every 8h`), a step number (`01`), a time axis (`0h 4h 8h`) and a
shell command are all mono; a sentence a person wrote is never mono.

**Display ramp** (Inter Tight, weight 600 throughout — the display never leaves
semibold):

| Step | Size | Line-height | Tracking |
|---|---|---|---|
| hero | `60px` fixed above 768px; `clamp(2.25rem, 11.5vw, 3.75rem)` below | 0.98 | −0.035em |
| section headline | `clamp(2rem, 4.5vw, 4rem)` | 1.05 | −0.03em |
| section headline, narrow | `clamp(2rem, 4vw, 3.5rem)` | 1.05 | −0.03em |
| two-column feature heading | `clamp(2rem, 4vw, 2.8rem)` | 1.05 | −0.03em |
| step title | `clamp(1.25rem, 2vw, 1.5rem)` | 1.2 | −0.02em |
| card title | `1rem` | 1.3 | −0.01em |
| footer wordmark | `44px` | 1 | −0.045em |

The tracking **closes as the size opens** — −0.01em at 16px, −0.045em at 44px —
and that gradient is the pack's typographic signature. A 60px headline at the
default 0em tracking is the single fastest way to lose it.

**Body ramp** (Inter, weight 400): lede `clamp(1rem, 2vw, 1.125rem)` / 1.6 ·
body-lg `1.125rem` / 1.65 · body `1rem` / 1.65 · body-sm `0.9rem` / 1.6 ·
caption `0.875rem` / 1.6. **No line of body copy drops below 1.5 anywhere in
the pack, including inside a card.** The display ramp above is a different
instrument and runs 0.98 to 1.3 on purpose.

**Mono ramp** (JetBrains Mono, weight 400 with 500 for a badge): badge `12px` /
`.08em` / UPPERCASE · step number `0.8rem` · handle `0.75rem` · cadence
`0.65rem` · axis mark `0.62rem` (`0.55rem` below 768px). A column heading is not
mono but Inter at `0.72rem` / weight 600 / `.05em` / UPPERCASE — the one
uppercase step that stays in the body face, because it heads a table of
sentences rather than a table of values.

**Every number is `tabular-nums`.** Costs, budgets, totals, counts. A ledger
whose rows shift width as they update is a broken ledger.

**Measure.** The hero lede is capped at **520px** and the two-column feature
sub at **420px** — narrow, deliberately: this pack's body copy is never more
than three lines, and a paragraph that needs a fourth belongs in a card. The
page shell is 1600px, which is wide, and the only thing allowed to use that
width is the marquee.

## Texture & surface

**Elevation is a hairline, and two shadows exist in the whole system.** The
modal's `--shadow-modal` (`0 32px 64px -24px`), and `--shadow-alert`, an 8px
`--warn` tint under the one chip that drops onto a lane uninvited. Both sit on
elements that genuinely float over the page; nothing else on the page floats.
`--shadow-alert` is derived from `--warn` with `color-mix()` rather than written
as a literal, because the reference hardcodes its light-theme orange into a
value it only ever paints on the dark field. Cards, panels, mocks, terminals, the nav and the footer are all
separated by 1px of `--border`, and the dark theme's border is *alpha*
(`#ffffff1a`) precisely so the same token reads correctly over the field, over
`--surface` and over the warm terminal without being restated three times.

**The 1px hairline grid, which is the pack's most copied idea.** A grid of
cards is built by making the *gap* the rule:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;                       /* the rule's thickness */
  background: var(--border);      /* the rule's colour, showing through the gap */
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  overflow: hidden;               /* the corners cut the cells, not the cells the corners */
}
.grid > * { background: var(--bg); }
```

No cell owns a border, so no two cells can double one, and the outer radius
clips the cells rather than being fought by them. Every feature grid, step grid
and table on the page is this shape. Below 768px the columns collapse to one and
the horizontal rules become the vertical ones — the same 1px, no rewrite.

**Radius: one root, a ladder of multiples, and an alias row that skips two
steps of its own ladder.** `--radius: .5rem`, then `×0.6 / ×0.8 / ×1 / ×1.4 /
×1.8 / ×2.2`. What components actually spend is:

| Alias | Resolves to | Where |
|---|---|---|
| `--r-sm` | 4.8px | copy buttons, terminal tabs, goal levels, small chips |
| `--r-md` | 8px | cards, inputs, mock frames, terminals, grids |
| `--r-lg` | 11.2px (`--radius-xl`) | modals, the largest panels |
| `--r-pill` | 9999px | **buttons, badges, org nodes, dots, schedule marks** |

`--radius-lg` (8px) is spent directly, five times, and only on the three large
mock panels — `.orgchart-visual`, `.tickets-visual`, `.cost-table-wrap`.
`--radius-md` (6.4px) is declared and spent **zero** times in either bundle.
Keep the alias row for components, reach for `--radius-lg` only for a panel that
frames a mock, and do not add a step.

**Concentric nesting — a pack decision, and the reference does not make it.**
Measured: the reference picks a radius by element *size* off the alias row and
does no arithmetic anywhere. Its terminal tab group is `--r-sm` inside a header
that carries no radius of its own; its ticket mock is `--radius-sm` inside a
panel at `--radius-lg` with 24px of padding between them, where any
outer-minus-padding rule would go negative. So the rule below is the pack's own,
declared as a decision rather than presented as a measurement:

> An inner radius is the outer radius minus the padding between them, snapped
> **down** to the nearest rung of the ladder, and never below `--r-sm`.

Worked: a control inside a panel at `--r-lg` (11.2px) with 3px of padding wants
8.2px and takes `--r-md` (8px). With 24px of padding the arithmetic goes
negative and the rule stops applying — a control that far inside its container
reads as its own object and takes its own radius, which is what the reference
does. When a control sits flush against a container's edge with **no** padding
at all it takes no radius and the container's `overflow: hidden` cuts it: the
feature cell in the hairline grid is that case.

**The capsule is the shape, not a radius value.** `--r-pill` is spent on things
whose width varies (button, badge, org node) *and* on things whose width is
fixed at 10px (the schedule dot, the pulse traveller) — a 10 × 20 rounded
rectangle rather than a circle. That is deliberate: a circle is a point, a
capsule is a paperclip's end, and the whole page is made of them. Data bars are
the one exception and take a flat `4px`, because a bar has to read as a
measurement with a square end, not as a lozenge.

**Grain — one noise recipe, on every saturated surface and nowhere else.**
`feTurbulence type="fractalNoise" baseFrequency="2.95" numOctaves="5" seed="9"
stitchTiles="stitch"`, tiled at 256px, composited `mix-blend-mode: overlay`
under `isolation: isolate`. It sits on each badge at **0.12** and over the hero
artwork at **0.86** through an alpha mask of the capsules themselves — the same
seed, the same recipe, one texture across two very different objects. It is
the reason a twelve-gradient page does not band, and it is the only texture in
the pack: the field itself is flat colour.

**Two numbers, and they do not agree — deliberately, once you know.** The filter
is authored on a **512**-unit canvas and painted into a **256px** tile, so the
grain renders at twice its declared frequency: an effective ~5.9, not 2.95. That
is what the reference ships and what was measured. Re-author the SVG at 256
units and you must halve the tile with it, or the grain doubles again and reads
as dirt.

**Where the grain may sit.** `MOTION_DOCTRINE.md` §5 puts noise on a
`position: fixed; pointer-events: none` layer, because a large tiled overlay
inside a scrolling container repaints every frame. This pack does not, and the
exception is narrow enough to state: a badge is a ~120 × 26px static element
with no animation, and the artwork's noise lives *inside* the SVG rather than in
a CSS layer over it. Neither repaints on scroll. A full-page grain layer in this
pack still goes `fixed`.

**Spacing.** `xs .5rem · sm 1rem · md 1.5rem`, then fluid: `lg clamp(2rem,
1.5rem + 1.5vw, 3rem) · xl clamp(3rem, 2rem + 3vw, 5rem) · 2xl clamp(4rem,
2.5rem + 4.5vw, 7rem) · 3xl clamp(5rem, 3rem + 6vw, 10rem)`. The section rhythm
is `--space-section: clamp(6.25rem, 5.75rem + .75vw, 6.9rem)` — 100px to 110px,
a deliberately *narrow* band, because a page of alternating claim-and-mock needs
a metronome rather than a taper. Container: 1600px max, 1.5rem of gutter.

## Components

Values measured off the reference. Every entry states rest, hover, active and
disabled; where the reference specifies none, the derivation is marked.

- **Primary button.** `--r-pill · fill --accent · label --accent-ink · padding
  .8rem 2rem · .95rem / weight 500 · border 1px --accent`. Rest: solid ink.
  Hover **inverts by theme and this is the detail to keep** — in light it goes
  *whiter* (fill `--bond`, ink `--ink`, border `--ink`); in dark it goes
  **hollow** (`background: transparent`, label and border stay `--accent`). One
  component, two opposite gestures, because on paper there is nowhere brighter
  to go and on coal there is nowhere darker. The reference writes `--cream` for
  the dark half; this pack declares no such token and means `--accent`, which
  resolves to the same white. Active: no transform — this pack
  does not press. Disabled: `opacity .6`, cursor default. **One per viewport.**
- **Secondary button.** `--r-md` — *not* a pill, and that is the only place in
  the pack where a button is not a capsule — `border 1px --border · label
  --muted · padding .8rem 2rem`. Hover: label and border both to `--ink`, fill
  unchanged. It is used once, under the hero's primary action, for the path that
  is not being recommended (`or install the local version`).
- **Nav CTA.** The primary button at `padding .45rem 1rem · .8rem`, with an
  optional count glyph at `.75rem / weight 600 / opacity .7`. Below 480px it
  drops to `.3rem .6rem / .7rem` and the icon shrinks to 11px.
- **Cards / containers.** `--r-md · border 1px --border · fill --surface ·
  padding var(--space-lg) var(--space-md)`. A card is used when a block has its
  own title; three sibling blocks share **one** hairline grid rather than three
  cards. **A card and a grid cell are different objects and only one of them
  hovers.** A card rests at `--surface` and has no hover. A *cell inside the
  hairline grid* rests at `--bg` and hovers to `--parchment` in light and
  `--surface` in dark — one step toward the card's own fill — plus the icon
  moving `--muted → --ink`. Giving a card the cell's hover paints `--surface`
  over `--surface` in dark and nothing happens. Nothing lifts, in either case.
- **Inputs.** `--r-md · border 1px --border · fill --bg · padding .7rem .9rem ·
  .95rem · font: inherit`. Label sits **above** in `--muted` at `.8rem` / weight
  500, never as a placeholder. Focus: border to `--border-strong` **and the
  focus ring is kept** — the reference removes it here and that is a defect this
  pack does not inherit (see Gotchas). Error: message beneath in `--danger` at
  `.85rem`; the border alone is a colour-only signal and is never the whole
  message. Disabled: `opacity .6`.
- **Option chips (a radio group that looks like tags).** `--r-pill · border 1px
  --border · label --muted · padding .45rem .7rem · .8rem`, the real `<input>`
  visually hidden at 1×1px and still focusable. Hover: border and label to
  `--ink`. Selected: **filled** `--ink` with `--bg` label — the same inversion
  as the primary button, which is what makes "selected" and "primary" read as
  one idea. Focus-visible on the input draws `outline: 2px solid var(--ink);
  outline-offset: 2px` on the label.
- **Section badge.** `--r-pill · mono 12px UPPERCASE / .08em / weight 500 ·
  padding .4rem .9rem · margin-bottom 1.5rem`, filled with its gradient and its
  own ink, under the noise tile at 0.12. It is a label and never a control: no
  hover, no focus, no href.
- **Navigation.** Sticky, opaque, 60px (52px below 768px), `border-bottom: 1px
  solid var(--border)` over a solid `--bg`. Links `.85rem` at **weight 500** in
  `--muted → --ink` — the reference asks for 450 and ships neither a variable
  font nor a 450 instance, so 450 is a request the engine rounds; pick the rung
  and know which you got (Gotcha 4). The **only** thing that changes on scroll is nothing — the
  bar does not shrink, blur, or gain a shadow. Below 480px the secondary and
  icon links are removed outright rather than collapsed into a menu.
- **Terminal block.** `--r-md · fill --terminal (#1f1d1a) · border 1px
  --terminal-rule`, a header at `--terminal-head` carrying three 10px
  `--terminal-dot` circles left and a **tab group** right (`--r-sm`, 2px
  padding, 2px gap, inactive `--terminal-mid`, active `--manila` on
  `--terminal-rule`). **The inactive tab label is `--terminal-mid` (5.64:1), not
  the reference's `--terminal-dim` (2.92:1)** — that is below every floor this
  pack enforces, on a label a reader has to click. `--terminal-dim` survives for
  the prompt glyph alone, which is `aria-hidden` punctuation. Body is mono
  `0.9rem` at `1.1rem 1.25rem`, prompt glyph in `--terminal-dim` with `.6rem` of
  right margin, and a copy button that swaps its glyph for a check in `--good`
  with a `copy-pop` scale `.5 → 1.15 → 1` over 0.3s. The block never scrolls the
  page sideways.
- **Org node.** `--r-pill · border 1.5px --border · fill --bg · padding 12px
  14px`, a 28px icon tile at `6px` radius, name at `.8rem` / weight 600, model
  beneath at `.68rem` preceded by a 6px status dot. Connectors are **1.5px**,
  not 1px — a hairline disappears at diagram scale. Live: border `--good` plus a
  `0 0 0 1.5px` ring at 25% alpha **and an `Active` chip** knocked out over the
  top edge. Never the ring alone.
- **Swimlane (a schedule).** A `130px | 1fr` grid (`86px | 1fr` on mobile),
  lanes separated by a top hairline, a 2px track line, and **capsule** marks:
  10 × 20 at rest with a 2px `--mark-rest` border, 12 × 22 filled `--good` with an
  8px glow when active. A travelling 8 × 16 capsule carries the pulse; a work
  label appears above it as a `--good` tint chip with the task written in it.
  The row label dims to 45% while the agent sleeps and returns to full plus a
  `--good` name when it wakes.
- **Ledger row (cost).** A `160px | 1fr | 100px` grid (`80px | 1fr | 76px` on
  mobile, where the icon and the model suffix are dropped), an 18px track at
  `4px` radius filled `--surface-quiet`, and a fill in **`--ink`** — white, not
  green, because a budget bar is a quantity and not a verdict. Amounts are
  `tabular-nums`, the spent figure in `--muted` and the total in `--ink` at
  weight 600.
- **Ticket panel.** The pack's one piece of representational drawing: a
  `--surface` panel at `--radius-lg` with **two 20px `--bg` circles punched into
  its left and right edges** at `--notch-y`, so the panel reads as a torn ticket
  stub. Inside it, a `--bg` mock at 1.5px border carrying a header, a thread and
  a trace.
- **Trace.** One mono line per step, a 6px dot left and a status word right:
  `passed` and `done` in `--good`, `running` in `--good` with a 1.5s
  `ease-in-out` pulse on both dot and word. The word is always present.
- **Interrupt chip.** `--warn` at 1.5px border on `--bg`, `.6rem`, with the
  pack's **only** spring — `cubic-bezier(.34, 1.56, .64, 1)` over 0.4s — because
  it is the only element that arrives unasked.
- **Testimonial card.** `--r-md · border 1px --border · fill --bg · width
  clamp(17rem, 24vw, 21rem) · min-height 14.5rem · padding 1.1rem 1.1rem
  1.2rem`. A 2.5rem circular avatar (the one circle in the pack), name in the
  display face at `.9rem` / 600, handle in mono at `.75rem`, body in `--muted`
  at `.9rem` / 1.62 clamped to **6 lines** (7 on mobile). A source glyph sits
  top-right at 40% opacity.
- **Modal.** `max-width 420px · --r-lg · fill --bg · border 1px --border ·
  padding 2.25rem 2rem 2rem · max-height calc(100dvh - 2.5rem)`, over a
  `--scrim` — the coal field at 55%, and it does **not** flip with the theme:
  the reference veils a light modal in coal too — with a 4px backdrop blur. Title `1.35rem` / 600 / −0.01em,
  description `.95rem` / 1.55 in `--muted`, a 2rem close target at the top
  right. Opens on a 0.25s rise; the scrim fades in 0.15s.
- **Loaders.** No spinner on a data path. The pack's idiom is the **trace**: the
  steps that have run, written out, with the current one pulsing. Where a real
  count exists, a bar fills to it; where nothing can be reported, the element
  simply stays at rest. A skeleton, if one is needed, matches the geometry of
  the block it replaces and pulses opacity — never a shimmer sweep.
- **Empty states.** A mono line naming what is absent, in `--muted`, left
  aligned, with the one action that would fill it beneath. No illustration, no
  centred column.

## Hero

One viewport, five elements, in this order: the artwork behind everything, one
display headline, a two-line lede, the primary action, and one quiet text link
under it for the path not being recommended. Nothing else — no logo wall, no
badge, no second filled button, no video.

**The architecture is a curtain, not a background.** The artwork is absolutely
positioned, `pointer-events: none`, and pushed **up** out of the viewport by
`translateY(-310px)` (−220px below 768px) so only its lower half is visible, and
the headline sits *on top of it* rather than beside it: `.hero-inner` is
`max-width: 900px`, centred, at `z-index: 1`, and the headline carries
`margin-top: 124px` to land in the curtain's lower third. The composition only
works because the copy overlaps the art — a hero that puts them side by side is
a different pack.

**The line ceiling is two lines, and the container is what enforces it.** The
reference's own headline is `A team of agents / for every person.` — sixteen and
seventeen characters, two lines, four words each, in a 900px box at 60px and
−0.035em. Take that as the working ceiling rather than a character count: Inter
Tight's advance varies enough with the string that any single number would be
invented. Set the headline, look at it, and if it takes a third line it is too
long — not the hero too small. Below 768px the size becomes
`clamp(2.25rem, 11.5vw, 3.75rem)` and it wraps freely.

The lede is `clamp(1rem, 2vw, 1.125rem)` in `--muted`, capped at **520px**, two
lines, and says what the product *is for* rather than what it is. The primary
action follows at 2.5rem below it, and the secondary path is a `--muted` text
link — not a button — a further 1.5rem down.

**What the hero must not contain:** a second filled button, a screenshot in a
browser frame, a testimonial, a metric the page has not yet earned, or a
gradient anywhere except the artwork itself.

## Responsive

- **Fluid type — three clamps, and the slopes are shown rather than guessed.**
  The hero display is **not** fluid above 768px: it is a flat `60px`, because the
  headline's job is to sit in a fixed relationship to a fixed-size artwork.
  Below 768px it becomes `clamp(2.25rem, 11.5vw, 3.75rem)`, which crosses
  2.25rem at 313px and 3.75rem at 522px — so it is fluid across the whole phone
  band and locked at both ends. The section headline is `clamp(2rem, 4.5vw,
  4rem)`: locked below 711px, locked above 1422px. Body copy is
  `clamp(1rem, 2vw, 1.125rem)`. The **mono ramp is not fluid** — a 12px tracked
  uppercase badge stays 12px at every width, because a tracked label that shrinks
  stops being legible before it stops being small. One exception, and it is a
  step rather than a ramp: the swimlane's axis mark drops `0.62rem → 0.55rem`
  below 768px, because seven marks have to fit across a phone. It is a
  breakpoint, not a clamp, and it has no token — write the two values.
- **Container queries.** The reference ships **zero** `container-type`
  declarations, and for the page that is correct — every breakpoint it owns is
  PAGE-shaped. Sorted into the three kinds:
  - **CONTAINER** — the four the *kit* must own, because a consumer drops them
    into an arbitrary box: the **ledger row** (`160px | 1fr | 100px` → `80px |
    1fr | 76px`, and the icon and model suffix drop), the **swimlane**
    (`130px | 1fr` → `86px | 1fr`, the cadence line disappears), the **hairline
    grid** (three columns → one), and the **org row** (three nodes → wrapped,
    icons dropped, labels centred). Each takes `container-type: inline-size` on
    its root and `@container` on the descendant.
  - **PAGE** — the nav's height and its link set, the hero's padding, the
    artwork's `translateY` offset and its width rule, the section rhythm, the
    footer's column count, the marquee-to-scroll-snap swap, and the `:root`
    theme switch. All viewport `@media`, and they stay there.
  - **SELF** — the marquee's own `padding-inline`, which is computed from the
    viewport against the 1600px shell (`max(var(--space-md), calc((100vw -
    var(--max-width)) / 2))`), and the hero artwork's own width
    (`min(1200px, 100%)` → `min(1200px, 150vw)`). Both are properties of the
    element that would *establish* the container, and a container cannot query
    itself. Keep the viewport query and mark it.
- **Collapse.** One breakpoint carries the page — **768px** — with a second at
  **480px** for the nav alone. At 768px: every two-column section stacks
  (`5fr 7fr` → `1fr`), every grid goes to one column, the marquee is replaced
  by a horizontally scroll-snapping row with a hidden scrollbar, the hero
  artwork swaps to a *different SVG* built for portrait, the headline goes
  fluid, and the org chart drops its node icons and centres its labels. At
  480px the nav loses its secondary links entirely. **Below the hero, nothing
  in this pack overlaps, rotates or carries a negative margin**, which is why
  the collapse is two rules and not seven. The hero is the one overlap and it
  collapses by moving its own offset (−310px → −220px) and swapping to a
  portrait artwork, never by unstacking: the copy stays on top of the art at
  every width.
- **Viewport.** Full-height shells use `min-height: 100dvh`; the modal's
  `max-height: calc(100dvh - 2.5rem)` is the reference's own and must not be
  simplified back to viewport units.

## Motion tokens

Two declared curves, one that is actually spent on entrances, and one spring
with a single owner.

| Token | Value | Where |
|---|---|---|
| `--ease-enter` | `cubic-bezier(0.2, 0.8, 0.2, 1)` | every hover, every state change |
| `--ease-hero` | `cubic-bezier(0.22, 1, 0.36, 1)` | the artwork's entrance, the headline's, every bar fill |
| `--ease-exit` | `cubic-bezier(0.4, 0, 1, 0.6)` | declared in the reference and **spent nowhere** |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | overshoot — the interrupt chip, and only that |
| `--t-micro` | `0.15s` | colour on hover |
| `--t-short` | `0.25s` | the default state change |
| `--t-medium` | `0.4s` | a card revealing, a lane sliding in |
| `--t-fill` | `1.2s` | a budget bar reaching its value |
| `--t-hero-art` | `1.1s` | the artwork's entrance |
| `--t-hero-copy` | `0.9s` | the headline's and the lede's, 220ms behind it |
| `--stagger` | `0.14s` | **one constant, everywhere** |

Eleven tokens, and the table is the whole set — `tokens/paperclip.css` declares
no twelfth. `--ease-exit` is in it because the reference declares it; the page
spends it nowhere, which is recorded rather than tidied away.

**One stagger, on purpose, and it is spent through the token.** Org nodes
stagger at `calc(var(--i) * var(--stagger) + 80ms)`, swimlanes at
`calc(var(--lane) * var(--stagger) + var(--stagger))`, goal levels and trace
steps at the same interval. Three unrelated diagrams on one page share a
metronome, which is why the scroll reads as one document rather than four
animated widgets. **Write `var(--stagger)`, never the literal** — the reference
hardcodes `.14s` in all three formulas, which is why zeroing a stagger token
under reduced motion would leave every one of them running.

**The hero's entrance is a pair, not a sequence.** The artwork rises 24px and
fades from 0 over 1.1s starting at 80ms; the headline and lede rise 18px and
fade **from 0.55, not from 0** over 0.9s starting at 220ms. Starting the copy
part-visible is the whole trick — the page never looks blank, and the text is
readable before the animation finishes.

**Scroll drives exactly one thing, and it is native.** Inside `@supports
(animation-timeline: scroll())` the hero declares
`view-timeline-name: --hero-timeline; view-timeline-axis: block`, and two
`animation-range: exit` timelines run against it: the artwork translates a
further −15vh and the copy −45vh as the section leaves. No listener, no library,
no observer — and browsers without support simply get no parallax, which is a
complete and correct experience. This is the pattern to copy; it is also the
pack's entire scroll budget.

**Reduced motion is a blanket, not a taper — and half of it cannot be bought
with tokens.** The token layer zeroes seven durations and the stagger; the rest
live inside `animation` shorthands as literals and have to be switched off by
rule. Ship both, in the same change:

```css
@media (prefers-reduced-motion: reduce) {
  .marquee-track,          /* 58s and 62s, both directions */
  .trace-dot--active,      /* the 1.5s pulse */
  .trace-status--active {  /* the 1.5s blink */
    animation: none;
  }
  .hero-art, .hero-inner { animation: none; transform: none; }
  .hero-headline, .hero-lede { animation: none; opacity: 1; transform: none; }
}
```

The reference ships the last two rules and not the first three: its marquee is
calmed, its two 1.5s trace loops are not. Everything holds its final state at
full opacity; nothing is slowed instead of stopped.

## Signature motifs

1. **The capsule.** A stadium with fully rounded ends, at every scale: a
   560 × 630 curtain of hero art inside a 1200 × 675 frame, a 12px badge, an org
   node, a 10 × 20 schedule mark, an 8 × 16 travelling pulse. The product is named after a bent
   piece of wire and the whole page is that shape.
2. **The hairline grid where the gap is the rule.** A 1px gap over a
   border-coloured background, clipped by the container's own radius, so no cell
   owns an edge and no two cells double one.
3. **The gradient badge under noise.** A mono uppercase label on a two-stop
   ramp with its own hand-picked ink and a fractal-noise tile at 12% overlay —
   the page's only recurring use of colour, and it is always a label.
4. **The warm terminal on a neutral field.** `#1f1d1a` against `#0a0a0a`: the
   one surface with a hue, reserved for quoting a real shell.
5. **The mock built from the page's own parts.** Every product screenshot is
   real markup at the page's own hairline, radius and type ramp — org chart,
   swimlane, ledger, ticket — so there is no seam between the argument and the
   thing being argued for.
6. **Status as a word with a mark beside it.** A dot, a ring or a tint never
   travels alone: `Active`, `In Progress`, `passed`, `Crawl audit`.

## Signature element

**The capsule curtain.** Eight columns on a 70px pitch, each holding twelve
70 × 170 rounded rectangles at `rx: 35` stepped 34.5px apart, so each capsule
covers all but a 34.5px band of the one above it and every column reads as a
stack of overlapping paperclip ends falling from the top of the page. Every
capsule is filled with its own two-stop vertical gradient, and the fills are
**generated rather than chosen**: the top stop rotates forward around the hue
wheel by **+12.39°** per capsule (246.9° → 383.2°) and the bottom stop rotates
*backward* by **−10.45°** (28.7° → −86.2°), so the pair sits 141.8° apart at the
first capsule and closes to 109.3° at the twelfth, and the column inverts its
own gradient end to end. Saturation and lightness are near-constant on the top
ramp (S 96→84, L 56→48) and deliberately are **not** on the bottom one
(S 96→69, L 56→33): the bottom stop darkens as it turns, which is what stops the
lower edge of the curtain from glowing against the field.

Forty-five gradients fill ninety-six capsules — a column carries twelve and the
eight columns reuse the same ramps, four of them **in reverse**, which is what
makes two adjacent columns read as one object rather than a repeat. Ninety
stops, eighty-nine distinct: `#fb8b24` is the one value that appears twice, as
the bottom of one ramp and the top of another. Over all of it, the noise tile at
0.86, masked by the capsules themselves.

It is the signature because it is the entire chromatic budget of the product
spent in one object that does nothing: it cannot be clicked, it carries no
information, it is pushed half out of frame, and the headline is set on top of
it in plain white. Every other surface in the pack is a hairline on coal.
That contrast — one loud object, everything else silent — *is* the composition,
and it is why the monochrome console the product actually is reads as
deliberate rather than unfinished. Spend colour here and nowhere else.

## Micro-interactions

- **Focus.** `outline: 2px solid var(--ink); outline-offset: 2px` on every
  interactive element. The one variant is `outline-offset: -2px` on a card that
  sits flush inside the hairline grid, where a positive offset would draw over
  the neighbouring cell. The ring is the ink, so it inverts with the theme and
  is always the highest-contrast mark on screen. Never remove it — including on
  a text input, where the reference does (Gotchas).
- **Hover is colour, border and fill. Never geometry.** Nothing in this pack
  lifts, scales, rotates or shifts on hover. A card changes fill; a button
  inverts; a link changes colour; an icon changes colour with its parent. There
  is no exception.
- **The primary button's hover is theme-dependent and that is the point.**
  Light: fill goes whiter. Dark: fill goes *away*, leaving an outline. Copying
  one gesture into both themes makes the button disappear in one of them.
- **The marquee pauses on hover** (`animation-play-state: paused` on the
  track), which is the only reason an infinite scroll is acceptable here: the
  reader can stop it to finish a sentence.
- **Copy affordances report in place.** The glyph swaps to a check in `--good`
  with a 0.3s overshoot pop; the button does not move and the label does not
  change width.
- **Reveal-on-scroll is opacity plus 16px of `translateY`, once.** Cards do not
  re-animate when they re-enter. Anything that has been seen stays seen.
- **Keyboard.** The option group is a real radio set — arrow keys move the
  selection — with the input hidden at 1 × 1px rather than `display: none`, so
  it keeps focus. The marquee is not keyboard-reachable and its content is
  duplicated in the mobile scroller, which is.

## Bans

- **No brand hue, and no coloured control.** The accent is the inverted field.
  A gradient that can be clicked, hovered or focused has left the pack.
- **No shadow on a resting element**, with exactly one exception: the modal.
  A card does not float; a sticky nav does not gain a shadow on scroll.
- **No blur on a surface.** `backdrop-filter` exists once, on the modal scrim,
  at 4px. A frosted card is not this pack.
- **No circle where a capsule belongs.** Dots, marks and indicators are
  10 × 20 stadiums. The avatar is the single circle in the system.
- **No spinner where a trace is possible**, and no progress bar that is not
  driven by a real number.
- **No status without a word.** A dot, ring, tint or bar in a status colour
  always carries its label.
- **No second display face.** Three families is the ceiling and the third is a
  monospace. A serif has nowhere to go here — the token called `--font-serif`
  is already occupied by a grotesque.
- **No scroll library, no scroll listener, no scroll-jacking.** Scroll drives
  one parallax, declared natively with `animation-timeline` behind `@supports`.
- **No layout property in a transition.** Never `transition: width` on a bar —
  animate `transform: scaleX()` from a left origin. The reference does the
  wrong one; see Gotchas.
- **No icon set.** A plug, a tree, a target, a coin, a ticket, a shield, a
  chevron, a check, a copy glyph — nine, all inheriting the text colour, at
  14–16px everywhere except the nav CTA below 480px, where the glyph goes to
  11px with the button around it. A tenth icon needs an argument.
- **No hero that puts the artwork beside the copy.** The copy sits on top of
  the art or the composition is gone.

## Gotchas

Ten traps, all measured in the reference on 2026-08-14. **Eight of them are
defects in the reference** — 1 through 8 — which is exactly why a copy of it
inherits them. Number 9 is a cost rather than a defect, and number 10 is a
deliberate choice that looks like one.

1. **`--font-serif` is a grotesque.** It resolves to Inter Tight, and it is the
   display face for the entire site. Any component library, chart or third-party
   widget that reaches for the serif slot silently gets a tight sans. Either
   accept it or scope the third party explicitly; do not "fix" it by loading a
   real serif, which puts a fourth family on the page.
2. **The dark theme repairs the status *icons* and forgets the status
   *colours*.** Five `--status-task-icon-*` tokens are re-declared for dark and
   the four base status tokens are not, so `--status-task-in_progress` stays
   `#2563eb` — **3.83:1** on the coal field — and it is rendered as text
   (`● 1 live`). This pack ships `#60a5fa` and marks it derived. If you copy the
   reference's token block wholesale, this is the bug you copy.
3. **Two radius ladders, and the alias row skips two rungs of its own.**
   `--radius-md` (6.4px) and `--radius-lg` (8px) are both declared, and the
   aliases the components actually spend map `--r-md → --radius` and
   `--r-lg → --radius-xl`, so `--radius-md` is never used at all and
   `--radius-lg` only through its identity with the root. Spend the alias row.
   Reaching for `--radius-lg` because the name sounds right gets you 8px where
   you wanted 11.2px.
4. **`font-weight: 450` buys nothing.** The nav links ask for 450 and the
   `@font-face` block ships Inter at 400 and 500 as **static instances**, not a
   variable font — so 450 rounds to whichever the engine picks and the
   intermediate weight never renders. Ask for 400 or 500 and know which you got.
5. **The focus ring is removed on the one input in the system.** The waitlist
   field sets `outline: none` on `:focus` and replaces it with a border colour
   change from `#ffffff1a` to `#a1a1a1` — a 1px hairline as the sole focus
   indicator. Keep the ring; a border change is not a focus indicator.
6. **Two infinite loops survive `prefers-reduced-motion`.** The reference calms
   the hero (artwork, copy, parallax), the governance lines, the marquee tracks
   and the modal — and leaves `dotPulse` and `statusBlink`, both 1.5s
   `ease-in-out` `infinite`, running on the trace. Stop them: a pulsing dot has
   no reduced form worth keeping, and its meaning is already carried by the word
   beside it.
7. **The budget bar animates a layout property, and it must not.** The
   reference writes `transition: width 1.2s` — never that — which lays out
   every frame for a second and a fifth, per bar, with six bars in view. Use
   `transform: scaleX()` with `transform-origin: left`, which costs one
   composited layer and looks identical.
8. **There is no `@media (hover: hover)` anywhere.** Every hover state in the
   reference fires on first touch on a phone, including the marquee's
   pause-on-hover, which on touch means the row stops and does not restart. Gate
   hover-only affordances.
9. **Six breakpoints exist and two of them carry the page.** 768px and 480px do
   the work; 900px, 720px, 1023px and 1200px each appear once, for one rule.
   Those four are the cost of building sections independently. Do not add a
   seventh; fold a one-off into 768 or make it a container query.
10. **The marquee's two rows run at 58s and 62s, and that is not sloppiness.**
    Equal durations make two opposing rows visibly re-sync every cycle and the
    band starts reading as a machine. Keep the durations unequal and
    non-harmonic when you copy it.
