# Style pack — Notation

Origin: [twenty.com](https://twenty.com) — read off its live computed styles on
2026-08-15, not transcribed from a screenshot.

A near-white field on which structure is drawn entirely in **hairlines instead
of cards**, radii of 2 and 4px, and a serif at weight 300 set against a
monospace. Almost no surface is filled. The primary control is the **ink**, not
the accent — on a page with this little colour, spending it on a button leaves
nothing to mark a link with. The signature is a **chamfer**: a 10px corner cut
on the primary, which is the one non-rectangular shape in the pack.

Contract: widened — all thirteen headings.

## Register

Choose Notation for **developer and technical products sold on restraint**: open
source front pages, CRMs and workspaces aimed at people who dislike being sold
to, documentation homes, and any surface where looking expensive would cost
trust. **Standalone.**

**Not for:** consumer products that need warmth, anything selling on emotion or
delight, a brand whose differentiator is visual richness, or a marketing page
that has to convert on first impression rather than on reading. At weight 300
with 2px radii and no fills, this pack whispers; asked to shout it just looks
underdesigned.

## Palette

Ready-made token layer: [`tokens/notation.css`](tokens/notation.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#ffffff` | page field |
| `--panel` | `#fafafa` | the barely-there surface step |
| `--panel-2` | `#f2f2f2` | the band that changes subject |
| `--ink` | `#1c1c1c` | primary text, **and the primary control** |
| `--muted` | `#5f5f5f` | secondary text |
| `--border` | `#dfdfdf` | the hairline that draws every structure |
| `--edge` | `#8d8d8d` | the visual boundary of a **control** |
| `--accent` | `#1f5fb0` | THE single accent — links and marks, never a fill |
| `--control` | `#1c1c1c` | the primary control is the ink |

### Floors, and what each colour may mean

Body and secondary text clear AA on the field and on the panel in both
registers. The accent's whole job is to mark what can be **read**; the ink's job
is to mark what can be **pressed**. Swapping them is the single change that
stops this pack working.

**Status is never by colour alone.** Every state is a dot or an icon **plus a
word**. Under deuteranopia `--danger` and `--warn` separate by 1.6 and `--ok`
and `--warn` by 7.9 — no palette solves the green/amber/red triple, so the word
carries the meaning.

**`--danger` is derived, not measured**, and the token layer says so at the
declaration: the reference paints no error state, so a red was authored to clear
AA on the field, the panel and its own tint (6.54 / 6.26 / 5.50).

**`--info` is the accent value**, because a second blue would separate from
`--ok` by less than the palette gate's hard floor.

## Type

Three families, and each has exactly one job.

- **Display — Aleo at weight 300.** A slab serif, used light. It carries every
  headline and nothing else. The lightness is the point: a 300-weight serif at
  60px reads as considered rather than loud.
- **Body — Inter at 400.** Every sentence.
- **Data — Geist Mono at 400**, tracked `+0.08em` and used uppercase for labels,
  identifiers and units. It never says a sentence.

Scale: `--t-meta` 12, `--t-body` 16, `--t-card` 19, `--t-title` 24,
`--t-section` 32, `--t-page` 38, `--t-hero` 60. Measures: 64ch prose, 54ch lede.

**There is no bold in this pack.** `--w-semi` and `--w-bold` are both 500,
deliberately. Emphasis is made with the serif, with the mono, or with a rule —
never by getting heavier.

## Texture & surface

**Structure is drawn, not filled.** A group is a hairline box or a hairline
above and below; `--panel` exists but is only 2% off the field and is used
sparingly. There is one shadow token, `--shadow-1`, and it is 4% at 2px — it
exists so a dropdown does not merge with the page and for nothing else. The dark
theme re-declares it at 50%, because 4% of black on a dark field is nothing.

Radii: `--r-control` 4, `--r-card` 4, `--r-pill` 999, and `--chamfer` 10.

**The chamfer is built from two clipped layers.** `clip-path` clips an inset
`box-shadow`, so a chamfered outline drawn the obvious way has a border on three
edges and nothing on its diagonal. The working construction is a clipped
background layer under a slightly inset clipped fill; the difference between
them is the line.

**Radius arithmetic when containers nest:** at 4px the arithmetic is nearly
moot, which is a property rather than an excuse — a control inside a 4px box is
`calc(4px - padding)`, which goes negative immediately, and the honest reading is
that this pack does not nest rounded things. Boxes hold flat content.

Spacing is a 4px grid. The page is 1180 with a `--margin` of 4.5rem, which is
what leaves the field looking empty on purpose.

## Components

- **Buttons.** Radius 4, 16px label, weight 500. *Primary:* the **ink** fill
  with `--control-ink` label, and the chamfer. *Secondary:* no fill, 1px
  `--edge`. *Ghost:* no fill, no border, `--muted` label. **Hover** darkens the
  ink or moves the border; **active** presses nothing; **disabled** is opacity
  .45.
- **Cards / containers.** A 1px `--border` box at radius 4, no fill, no shadow.
  **Use a divider before a box:** the reference's default is a hairline between
  two things, and a page of boxes in this pack reads as a form.
- **Inputs / forms.** Label above at 16/500, a 1px `--edge` field at radius 4 on
  `--bg`, hint below in `--muted`. **Focus** is a 2px `--accent` outline at 2px
  offset — an outline rather than a ring, because a ring implies a fill this
  pack does not have. **Error** puts `--danger` on the border and replaces the
  hint.
- **Navigation.** A bar with a bottom hairline and no fill change on scroll. The
  sign-in is a ghost; the one chamfered primary on the page is the hero's.
- **Loaders.** A hairline progress rule, 1px, filling left to right in
  `--accent`. No skeleton blocks: filled grey rectangles on a page with no fills
  read as broken layout rather than as pending data.
- **Empty states.** A hairline box, one serif line at `--t-card`, one sentence
  at 44ch in `--muted`, and a secondary action. No illustration.

## Hero

A single column, left-aligned, on a wide margin. The display is the page: Aleo
at `--t-hero`, weight 300, tracking `-0.02em`, line-height 1.1, capped at
**20ch** — which holds it to **three lines at 1440**. The container is `--page`
1180 with `--margin` 4.5rem on the left.

The first viewport must contain: the display, one lede at 54ch, one chamfered
primary and one ghost beside it, and an uppercase mono eyebrow above the
display. It must not contain: a filled panel, an image, a logo wall, or a second
chamfer — the chamfer is a signature and a second one makes it a pattern.

## Responsive

- **Fluid type.** `--t-hero` ships as `clamp(2.5rem, 4.4vw, 3.75rem)` — 40px at
  390 and 60px at 1364 and above, a slope of 4.4vw. `--t-section` is
  `clamp(1.75rem, 2.6vw, 2.375rem)`. Body does not scale.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | A hairline box's rows going from two columns to one | CONTAINER | `container-type: inline-size` on the box, `@container` on the rows |
  | Mono label row wrapping | CONTAINER | container on the row, `@container` on the label |
  | The 4.5rem margin collapsing to the page gutter | PAGE | viewport `@media` — the margin is the page's |
  | The bar collapsing to a disclosure | PAGE | viewport |
  | The chamfer's own size at narrow | SELF | **no container answer exists** — the chamfer is a property of the element that establishes the container. Keep the viewport query |

- **Collapse.** Nothing overlaps, nothing rotates, and there are no negative
  margins, so collapse is only the wide margin becoming the gutter. The
  comparison table hides its head below the breakpoint and **every cell prints
  its own column name**, the row header included — a stacked comparison labelled
  on one side shows a phone reader the argument as the answer.
- **Viewport.** `min-h-[100dvh]`, never `100vh`.

## Motion tokens

One curve, `cubic-bezier(0.2, 0, 0, 1)`. `--dur-state` 0.14s, `--dur-hover`
0.1s. Nothing else moves.

No entrance animation and no scroll reveal. A page this quiet that animates its
own arrival has broken its own argument.

Reduced motion sets both durations to `0s` at the token layer.

## Signature motifs

1. **The hairline instead of the card.** Structure is drawn.
2. **The chamfer.** One 10px corner cut, on the primary, once per page.
3. **The light serif.** Aleo at 300, and no bold anywhere in the pack.
4. **The uppercase mono eyebrow**, tracked `+0.08em`, naming the section above
   its serif heading.
5. **The ink primary.** The loudest control on the page carries no colour.

## Signature element

**The chamfered primary.** One control, one cut corner, once per page. It is the
only non-rectangular shape in a pack built entirely from straight lines and 2px
radii, which is exactly why it is remembered — and exactly why a second one
would erase it.

Everything around it stays rectangular and unfilled so that the cut reads as a
decision rather than as a style.

## Micro-interactions

- **Hover** moves colour and border. No transform, no shadow, no fill appearing
  where there was none.
- **focus-visible** is a 2px `--accent` outline at 2px offset — an outline, not
  a ring, because a ring implies a surface.
- **Keyboard.** The nav disclosure is a `<details>` and works with script off.
- **Selected** is a 1px rule under the item in `--ink`, not a fill.

## Bans

- **No accent fill on a control.** The accent marks what can be read; the ink
  marks what can be pressed.
- **No bold.** Emphasis is the serif, the mono or a rule.
- **No second chamfer** on a page.
- **No card fill** where a hairline will do, and no shadow used as elevation.
- **No skeleton blocks** — a grey rectangle on a page with no fills reads as
  broken layout.
- **No illustration, no photograph, no logo wall** in the first viewport.
- **No status by colour alone.**

## Gotchas

- **The chamfer has no line on its diagonal if you draw it the obvious way.**
  `clip-path` clips an inset `box-shadow`, so a clipped box with a border shows
  three edges and a gap. Build it as two clipped layers — a background layer and
  a slightly inset fill — and the difference between them is the line. This was
  found by rendering, not by reading.
- **Swapping the ink primary for an accent primary is the one change that
  destroys the pack**, and it looks like an improvement in isolation: the button
  gets "brand colour". What it costs is the accent's only job, and every link on
  the page goes with it.
- **The `--panel` step is 2% and will disappear under a rendering that
  approximates.** If a surface must be distinguishable, use a hairline. The panel
  fill is for grouping the eye already believes in, not for creating it.
- **At weight 300 an Aleo display below 32px stops being legible as a
  headline** and starts reading as body copy that lost its way. The serif is for
  `--t-title` and above; below that, the sans.
- **Radius 4 everywhere means a chip at radius 4 looks like a button.** Chips
  take `--r-pill`; the 4px radius belongs to boxes and controls only.
