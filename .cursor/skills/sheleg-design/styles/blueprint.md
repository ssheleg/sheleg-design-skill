# Style pack — Blueprint

Origin: <https://www.pinecone.io/> (2026), the marketing site of a vector
database. Every value below was read off its live computed styles on 2026-08-09,
and every ratio was computed by importing this repository's own palette gate. A
white drawing sheet, a faint grid, ruled column edges, registration marks at the
corners of the things that matter, one saturated blue used the way a draftsman
uses ink — and **no radius anywhere at all**.

The identity in one sentence: **the drawing, not the render.** This page does not
photograph the product; it draws it to tolerance, and expects the reader to be
someone who reads drawings.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **infrastructure sold on precision**: vector databases,
search and retrieval, storage and query engines, streaming, anything whose buyer
wants to see the mechanism rather than the marketing. Its argument is *here is
exactly what this does, at what cost, at what scale*, and its whole vocabulary —
grid, rules, ticks, one ink — comes from technical drafting.

It rides the SHELEG cinematic layer only at its quietest setting. A drawing that
performs stops being a drawing.

**Not for:** a page whose subject is a running system with a changing value —
that is `instrument-console`. A warm, humane document arguing from provenance —
`field-notes`. A page that shows the product rather than draws it — `showroom`.
A developer page whose argument is a code sample rather than a drawing, set in the reader's own monospace — [`manpage`](./manpage.md).
And not for **anything that needs a rounded corner**: this pack has no radius
token to give you, and adding one damages it more than changing its blue would.

### The fork against [`field-notes`](./field-notes.md)

Both draw rules on a light field, both use a mono for annotation, both serve
readers who will scroll to the technical section first. The difference is the
stock and what the marks mean.

`field-notes` is **warm paper**: a green-cast off-white, rust ink, crop marks
that say *this was printed and trimmed*. Its argument is provenance — how do you
know this is true.

`blueprint` is **cold stock**: pure white, electric blue, registration marks that
say *this was drawn to tolerance*. Its argument is precision — how exactly is
this built, and what does it cost at scale.

Route by the question the product answers. *How do you know?* → `field-notes`.
*How is it built?* → `blueprint`.

### Against [`prism`](./prism.md) and [`maquette`](./maquette.md)

All three were extracted from vector-database companies, which makes this the
most confusable trio in the library — and category matching cannot separate them,
because the category is identical. Route on **who the reader is and what the page
must contain**.

- **`prism`** is for an evaluator arriving from GitHub, and its first artifact is
  an **install line**. This pack has no install component at all: if the page's
  first action is a command, it is not this one.
- **`maquette`** is for an architecture buyer who must decompose a structure, and
  its centre is **one complete labelled model**. This pack gives you figures,
  ruled data cells and mono columns instead — reach for it when the argument is
  *quantitative* (recall at scale, cost per query) rather than *structural*.
- **`blueprint`** is for a buyer weighing precision and cost, reading a drawing.

A page with two numeric arguments and an architecture section is a sheet of
figures, and that is this pack. A page whose whole hook is a separation of
concerns is `maquette`. A page whose hook is `pip install` is `prism`.

### Against `showroom`

Both are white and dense. `showroom` puts a real product surface under a
seven-layer shadow and asks you to look at it. `blueprint` has **no shadow
vocabulary at all** and asks you to read a figure. If the page's centre is a
screenshot, it is not this pack.

### Against [`datasheet`](./datasheet.md)

Both are light, technical and gridded, and both refuse ornament. This pack is a
**drawing**: white stock, a 32px grid, registration marks, and no radius anywhere,
describing a thing precisely enough to build. `datasheet` is a **datasheet**: an
off-white sheet with a concentric radius family from 16 down to 2, describing a
thing that is already running and printing its output into the page. Zero radius
against a radius family is the tell; the deeper one is tense — a specification of
what will exist, against a reading of what just happened.

## Palette

Ready-made token layer: [`tokens/blueprint.css`](./tokens/blueprint.css) — copy
it verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#FBFBFC` | the drawing stock | — |
| `--surface` / `--surface-2` / `--surface-3` | `#FFFFFF` / `#F8FAFC` / `#F1F5F9` | panel · figure well · deepest step | — |
| `--ink` | `#111827` | body and display | **17.15:1** — see the conflict below |
| `--ink-soft` | `#4B5563` | secondary copy, safe as body | **7.31:1** |
| `--ink-faint` | `#9CA3AF` | **rules and marks only, never text** | 2.5:1 |
| `--line-grid` | `#E7E5E4` | the field grid, the tick marks | — |
| `--line` / `--line-strong` | `#E2E8F0` / `#CBD5E1` | panel edge · the ruled column boundary | — |
| `--accent` | `#002BFF` | ink **and** fill | **7.28:1** |
| `--good` / `--info` / `--danger` / `--warning` | `#86AF80` / `#8BF6FF` / `#A440CE` / `#F5B900` | category marks | every pair clears both floors |

Three rules carry this palette.

- **One blue does everything.** `#002BFF` measures **7.28:1** on the stock
  (`--bg` `#FBFBFC`) and 7.53:1 on pure white. It sets a heading word, draws a
  1.5px rule, fills a button, and rings a focused input — with no second token
  and no lighter "on-dark" variant. It carries text and fill at one value
  because it clears 7:1 in the role that is harder — as text — not because of
  any symmetry: WCAG contrast is symmetric for every colour pair by
  definition, so that is never a finding about a particular blue.
  *(Corrected 2026-08-10: this table's numbers were computed against pure
  white while its own column is headed ``On `--bg` ``, and the stock is not
  white. `validate_palette.py` now recomputes every stated ratio.)*
- **These are category marks, not statuses.** The pack labels *kinds* — an index
  type, a tier, a language — not health. Every pair clears both separation floors
  under all three dichromacies, so no secondary-encoding declaration is required
  here; label them anyway, because a legend of four coloured squares is a legend
  nobody reads.
- **`--ink-faint` is furniture.** At 2.5:1 it draws a grid line or a tick and
  never a word.

### The ink, and why it is not the reference's ink

The reference sets **pure black** as its body ink, on 316 elements. The doctrine
bans pure black as ink — it reads as an unfinished default — and `sloplint.py`
enforces the ban.

So this pack ships `#111827`: the reference's **own second ink**, already used on
136 of its elements. That keeps the value inside the page it came from rather
than inventing one.

**It is a visible substitution, not a rounding, and the pack will not pretend
otherwise.** The two sit **21.2 apart** in OKLab. Pure black measures 20.31:1 on the
stock; `#111827` measures 17.15:1. Both are far above any floor that matters, and
the page reads a shade softer for it. If you require the reference exactly, you
are choosing a value this library bans, and you should do that knowingly.

## Type

Two families and nothing else.

- **GT Planar (Grilli Type, licensed)** for everything that is not data. A
  grotesque with a slightly mechanical axis, which is why it sits with the
  drafting furniture instead of fighting it.
- **JetBrains Mono** for every number, identifier, command and code line.

**Substitutes, measured rather than remembered.** GT Planar is licensed, so this
matters: use **Inter** (the closest widely-available grotesque with the same
vertical proportion) or **Geist**. Do **not** substitute a geometric like Poppins
or a humanist like Open Sans — both round the page off in a way that fights the
zero-radius rule harder than any single wrong colour would.

The ramp is small at the bottom and letterspaced there, which is the pack's
typographic signature:

| Token | Size / line-height | Tracking | Weight |
|---|---|---|---|
| `--t-display` | 44 / 1.1 | −0.02em | 700 |
| `--t-h2` / `--t-h3` | 32 / 1.15 · 24 / 1.2 | −0.02em | 700 |
| `--t-body` / `--t-sm` | 16 / 1.5 · 15 / 1.4 | 0 | 400 |
| `--t-data` | 12 / 1.5 — **JetBrains Mono** | 0 | 400 |
| `--t-label` | 11 / 1.4 | **0.045em** | 600 |
| `--t-annot` | 10 / 1.6 | **0.1em** | 400 |

**The annotation size is the tell.** A 10px label at `0.1em` reads as a drawing
annotation; the same size at 0 reads as small text, and the page loses its
register instantly. Set annotations in caps.

## Texture & surface

- **Zero radius. Everywhere.** `--radius: 0`, and the token exists so the ban is
  greppable. The one exception is `--radius-round: 50%` for dots and avatars.
  Rounding a button in this pack is not a small liberty — it is the change that
  makes the page stop reading as a drawing.
- **Elevation is a hairline.** There is exactly one soft shadow,
  `--shadow-panel`, for a genuinely floating popover, and one `0 0 0 1px` accent
  ring for focus. Nothing else casts.
- **The grid is a real layer**, not a texture: `--grid-step` 32px, 1px dots in
  `--line-grid`, `pointer-events: none`, `aria-hidden`. It sits at depth layer 1
  and never on a scroller.
- **Vertical rules bound the content column** at `--column-max` 1280px, drawn in
  `--line-strong` at 1px, running the full height of the section. They are the
  layout made visible and they are why the page reads as a sheet.
- **Registration marks** are `--tick-len` 8px arms at `--tick-w` 1px, offset
  `--tick-gap` 6px from the object they register, in `--line-grid` — or in
  `--accent` on the primary action.
- Spacing is a 4px ramp; sections are separated by the grid and by space, never
  by a change of background.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary CTA** | `--accent` fill, white label, **0 radius**, `16px 24px`, 16px/400, registration marks at its four corners | fill → a step darker over `--dur-fast` | marks switch to `--accent` at full opacity | `--surface-3` fill, `--ink-faint` label, `cursor: not-allowed` |
| **Secondary CTA** | transparent, `1px --line-strong`, `--ink` label, same metrics, **no marks** | border → `--ink` | — | as above |
| **Panel** | `--surface`, `1px --line`, 0 radius | none | — | — |
| **Figure well** | `--surface-2`, `1px --line`, 0 radius, the grid showing through at 40% | none | — | — |
| **Data cell** | `--t-data` JetBrains Mono, `--ink`, right-aligned when numeric, `1px --line` bottom | row tint → `--accent-wash` | left edge 1.5px `--accent` | — |
| **Category mark** | a 8×8 square — **not a circle** — in its own colour, with its label beside it in `--t-label` | none | — | — |
| **Annotation** | `--t-annot` caps at `0.1em` in `--ink-soft`, with a 1px `--line-grid` leader to what it annotates | none | — | — |
| **Input** | `--surface`, `1px --line-strong`, 0 radius, `10px 12px`, **16px** | border → `--ink-soft` | focus: `--ring-accent` plus an `--accent` border | `--ink-faint` text on `--surface-3` |
| **Tab** | `--t-label` caps, `--ink-soft`, a 1px bottom rule in `--line` | colour → `--ink` | colour → `--accent`, bottom rule → 1.5px `--accent` | — |
| **Loader** | **pack decision:** a skeleton drawn as an empty ruled frame — 1px `--line`, no fill, no shimmer. A drawing in progress is an outline | — | — | — |
| **Empty state** | **pack decision:** a ruled frame with one `--ink` line and one `--ink-soft` line, centred, marks at its corners. No illustration | — | — | — |

## Hero

- **Height** `--hero-min-h: 100dvh`. Never `100vh`.
- **The content column is ruled.** Two 1px vertical lines at the column
  boundaries, running the full hero height, in `--line-strong`. Everything in the
  hero sits between them; the grid continues outside them, fainter.
- **Left-aligned, not centred.** A caps eyebrow in `--accent` at `--t-label`, the
  display headline with **one word in `--accent`**, a two-line lede, then two
  buttons side by side — registration marks on the **primary only**, never on
  both (see *Signature element*: two marked buttons read as a texture rather
  than as an argument).
- **Line ceiling: two.** The display is 44px, which is small for a hero on
  purpose — this pack does not shout, and a third line pushes the figure below
  the fold.
- **The right half carries the figure**, not a screenshot: a diagram, a field of
  plotted points, a drawn mechanism. If the only thing you have is a product
  screenshot, you are in `showroom`.
- The first viewport ends with a logo strip on `--surface-2`, full-bleed, with
  the grid showing through.

## Responsive

- **Type steps at breakpoints**, it does not slide. The display drops 44 → 32 →
  28; the annotation size never changes, because 10px at `0.1em` is already at
  its floor and scaling it destroys the register.
- **The vertical rules are the first thing to go.** Below 1024px they collapse to
  the viewport edges; below 768px they are removed entirely, because two rules
  16px apart from the screen edge read as a rendering error.
- **The grid halves its step** below 768px (32px → 16px) so the density stays
  visually constant as the viewport narrows.
- **Registration marks are desktop-only.** Below 768px they come off the buttons
  — at 8px they become touch-target confetti — and stay only on framed figures.
- Buttons go full-width and stack below 480px. Full-height sections use `dvh`.

## Motion tokens

- **One curve, `cubic-bezier(0.4, 0, 0.2, 1)`**, and three durations:
  `--dur-fast .15s` for colour, `--dur-base .22s` for anything else on a control,
  `--dur-slow .4s` for a section reveal.
- **The grid never animates.** Not on scroll, not on load, not on hover. It is
  the sheet.
- Transitions are scoped to named properties; `transition: all` is banned.
- **The reference ships no `prefers-reduced-motion` branch at all** — see
  Gotchas. This pack requires one, and it must also stop any marquee.

## Signature motifs

- **Registration marks** at the corners of the primary action and of framed
  figures.
- **The dotted field grid** at 32px, always behind, never on a scroller.
- **Ruled column boundaries** — two 1px verticals that make the layout visible.
- **The caps annotation at `0.1em`** with a hairline leader.
- **One word of the headline in `--accent`**, and no other accent text in the
  hero.
- **Square category marks**, never circles. A circle is a status; a square is a
  kind.
- **Mono for every number**, right-aligned in columns.

## Signature element

**The registration marks.** Not the grid — the grid is a field and it recurs
everywhere, which makes it a motif. The marks appear on **one** thing per
viewport: the action the page wants, or the figure it is arguing from.

**One thing means one thing — the primary, not the pair.** A secondary button
beside a marked primary is exactly where this rule gets quietly broken, and two
marked buttons already read as a texture rather than as an argument.

They carry the identity because they are the smallest possible statement of the
pack's thesis. A registration mark exists so two plates line up in a press: it is
a mark about *accuracy*, made by someone who assumed you would recognise it. Put
four 8px brackets around a button and the page says, without a word of copy, that
this is a document produced by people who measure things.

That is also why they must stay rare. Marks on every card is a texture; marks on
the one thing that matters is an argument. Spend them there and let everything
else be plain.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack: keep the scroll clock and use the Reveal
set at `--dur-slow` on the one curve — translate 8px and opacity, nothing larger.

The ambient layer is the **plotted field**: points scattered on a curve, in
`--accent` at low opacity, drifting slowly. It is a *plot*, not a particle
system — the points sit where data would put them, they do not swirl, and they
never form a shape that is not a diagram. If your ambient layer would look at
home behind a crypto landing page, it is wrong for this pack.

Nothing else moves. No morphing formations, no scrubbed instruments, no act
badges: those narrate a system doing something over time, and this page's subject
is a system's *construction*.

## Micro-interactions

- **Buttons** transition fill and border only. Nothing scales, nothing lifts, and
  the press state is a fill change — a 0-radius rectangle that moves looks broken
  in a way a pill does not.
- **Rows** tint; **cells** take a 1.5px accent left edge when selected.
- **Focus-visible** is `--ring-accent`, a sharp 1px accent ring at the element's
  own zero radius, plus an accent border. No halo, no glow — a soft focus ring
  in a hard-edged pack reads as a foreign part.
- **Tabs** move a 1.5px accent rule; the label colour changes with it.
- Annotations, marks and grid lines have no states. They are printed.

## Bans

- **A radius.** Any radius, on anything, except `50%` for a dot or an avatar.
- A shadow used for elevation; `--shadow-panel` is for a floating popover and
  nothing else.
- `--ink-faint` as text; `--accent` as a large field fill (it is ink and a button,
  not a background).
- A circle used as a category mark; a category colour used to mean health.
- The annotation size without its tracking; caps annotations set at 0.
- A geometric or humanist substitute for the display face — Poppins, Open Sans,
  Nunito and their family round the page off.
- Fluid `clamp()` type; `transition: all`; `100vh`; a scroll listener.
- **Animating the grid**, or parallaxing it.
- A screenshot as the hero's figure. Draw it, or use `showroom`.

## Gotchas

- **The reference ships no `prefers-reduced-motion` branch — zero blocks** —
  while running marquee, `ping`, `pulse` and `scroll` animations. A reader with
  vestibular sensitivity gets the full page. This pack requires the branch, and
  it is the first thing to add when porting: the reference cannot be copied
  wholesale on this point.
- **The reference's body ink is pure black**, which this library bans; the pack
  substitutes the reference's own second ink and the two are 21.2 apart in OKLab.
  Recorded above in full — it is a real, visible divergence.
- **The grid, the vertical rules and the registration marks were not reachable
  from any stylesheet rule** at capture time. Background-image tallies, SVG
  `<pattern>` lookups, thin-element scans and absolutely-positioned two-border
  scans all came back empty; they are almost certainly inline SVG or
  pseudo-elements. **The geometry in this pack is therefore observed from the
  rendered page, not measured from a declaration** — treat the step, the arm
  length and the gap as a faithful reading rather than as extracted numbers.
- **Zero radius is load-bearing and it will be the first thing a component
  library fights you on.** Most React kits ship a default radius; you must zero
  it globally rather than per-component, or the page ends up with three rounded
  inputs nobody notices until it looks cheap and nobody can say why.
- **`#002BFF` is unusually saturated** and it vibrates against `--ink` at small
  sizes. Do not set body copy in it; it is a heading word, a rule, a fill and a
  ring.
- **Values are a snapshot** taken 2026-08-09 from a live production site. Treat
  them as extracted, not eternal.
