# Style pack — Router

Origin: [openrouter.ai](https://openrouter.ai) — the marketing site and the
signed-in dashboard, measured 2026-08-16.

A near-white field with a trace of blue in it, white cards standing on that
tint, and hairline seams instead of shadows. One accent, a 97%-saturated royal
blue, doing every job an accent does and nothing else. Body at 14px and weight
450 — a half step above normal, which is the whole density of the interface.
Uppercase mono labels that never say a sentence. The signature texture is
**the seam**: a 1px rule at 7.8% of the ink, drawn everywhere a lesser pack
would reach for a shadow.

Contract: widened — all thirteen headings.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Contents

- Before you read the rest — what this pack was measured from
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

## Before you read the rest — what this pack was measured from

**The first pack in this library read from a running product rather than from
a served stylesheet**, and the difference produced three corrections that a
stylesheet-only reading had wrong:

- `--text-xs` is **14px**, not 12. Only `--overline` is 12, so the interface
  has exactly one step below body and it is a label size.
- The sidebar is **224px**, not 244.
- The border asymmetry that looks like a deliberate register decision belongs
  to `--sidebar-border` alone. The main `--border` is symmetric by
  construction — the ink at 7.8% on light, the cloud at 7.8% on dark.

The method: the stylesheets gave the scale, and `getComputedStyle` on the
signed-in dashboard gave what a stylesheet cannot answer — which token flips
in which register, what the selected sidebar item actually paints, how wide a
bar is and how far apart two bars sit.

## Register

Choose this pack for **product consoles and the marketing pages that have to
look like them**: dashboards, admin surfaces, developer platforms, billing and
usage screens, and a landing page whose argument is *here is everything the
thing holds, and its state*. It is the pack for an inventory rather than a
promise. **Standalone** — it does not ride the SHELEG cinematic motion layer,
and the reference has essentially no motion at all.

**Not for:** editorial and long-form reading, anything selling on warmth or
craft, a consumer landing page that has to feel like a magazine, or a brand
whose whole idea is texture. At 14px body on a hairline grid this pack reads
as software. Asked to be a lifestyle page it reads as an admin panel with
photographs in it.

**Motion ceiling:** no pack ceiling is pinned here, so `MOTION_INTENSITY` is cut by §1's frequency table alone — the dial turns up what is left after that table, and nothing in this pack narrows it further.

## Palette

Ready-made token layer: [`tokens/router.css`](tokens/router.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role — every ratio in this column is on `--bg` |
|---|---|---|
| `--bg` | `#f9fbfe` | page field — near-white with a trace of 258° in it |
| `--panel` | `#ffffff` | the card, which is white **on** the tint |
| `--panel-2` | `#f1f3f6` | the band that changes subject |
| `--ink` | `#151b24` | primary text — 16.69:1 on the field |
| `--muted` | `#5c6068` | secondary text — 6.09:1 |
| `--border` | `#e3e6e9` | the seam, and the pack's signature texture |
| `--border-strong` | `#ced1d5` | the divider that must be seen |
| `--edge` | `#8e9197` | the visual boundary of a **control** — 3.05:1 |
| `--accent` | `#035ade` | THE single functional accent — 5.75:1 |
| `--accent-ink` | `#ffffff` | text on the `--accent` fill — 5.96:1 |
| `--ok` `--warn` `--danger` | `#007544` `#8a6100` `#bf0024` | status **words** |
| `--ok-mark` `--warn-mark` `--danger-mark` | `#00bf6f` `#e5a000` `#ff2d55` | status **marks** |
| `--series-1…4` | `#2d88e2` `#025397` `#019d7e` `#00614d` | chart series |

### The triplet, which is the one idea worth carrying out of this reference

Every status holds **three** tokens rather than one. The reference's own delta
is drawn in `#00bf6f` and set in `#007544`: **the colour you paint with is not
the colour you write with.** The `-mark` values are identical in both
registers because only the words have to be read, and the split is what lets a
97%-saturated hue be an accent without becoming an unreadable label.

### Floors, and what each colour may mean

Body and secondary text clear AA on both the field and the panel in both
registers — 16.69 / 17.30 and 6.09 / 6.31 on light, 17.05 / 15.75 and 7.23 /
6.68 on dark. Every semantic word clears 4.5:1 on its own field **and** on its
own chip tint, so this pack declares no `@role non-text:` list at all.

**Status is never by colour alone.** Every state in this pack is a dot plus a
word, never a dot. Under deuteranopia `--danger` and `--warn` separate by 1.2
and `--danger` and `--ok` by 6.4 — the green/amber/red triple is the classic
confusion set and no palette solves it, so the word carries the meaning and the
colour reinforces it. The chip that shows this is the pack's own component: a
6px dot, then the state named in full.

### Two departures from the reference, both measured before they were made

**The accent is the reference's `--or-royal` and not its `--primary`.** Its
primary is the violet `#7624f4`: 6.31 on white, **3.14 on ink**, where it
cannot carry a word. The reference agrees with the finding — flipping its own
register swaps `--primary`, `--ring` and `--link` to the acid `#c8ff00`.
Changing hue by register is its solution too; this pack lifts within one hue
instead, to `#4d8dff` at 5.73.

**The dark `--danger` is `#ff5470`, not the reference's `#ff2d55`.** Theirs is
5.02 on the field and clears — but on its own chip tint it measures **4.38**,
and a danger chip is exactly where the word most needs to be read. Lifted until
it clears the tint it sits on: 5.13.

## Type

Two families and no third.

- **UI — Plus Jakarta Sans.** The reference's brand face is `gordita`,
  self-hosted and not licensable to check a stylesheet against, so it is not
  approximated silently. `jakarta` is the second family the reference already
  serves, and it is the whole voice here.
- **Data — Geist Mono**, theirs unchanged. It sets labels, identifiers, units
  and table captions. It never says a sentence.

Weights `450 / 500 / 600 / 700`. **450 rather than 400 is measured**
(`--font-weight-normal: 450`) and is why the reference's body copy reads denser
than 14px suggests; rounding it to 400 or 500 loses the half step the whole
interface is built on.

Scale, named by role rather than by size: `--t-meta` 12, `--t-body` 14,
`--t-card` 16, `--t-title` 20, `--t-section` 24, `--t-page` 30, `--t-hero` 36.
Body is **14**, and that single decision is what separates this pack from every
marketing-first pack in the library.

Measures: 68ch for prose, 54ch for a lede, 17ch for a display headline.
Tracking `-0.025em` on anything 20px and above, `0.05em` on uppercase mono.

## Texture & surface

**Elevation is border, not shadow.** The reference sets `box-shadow: none`
almost everywhere; exactly one lift exists in the whole product, it is a menu,
and it is the single shadow token `--shadow-1` — re-declared at 32–36% for the
dark theme, because the light values disappear there. A card is `--panel` on
`--bg` with a 1px `--border` and radius 8. That is
the entire elevation model, and a pack that adds a second shadow has stopped
being this pack.

Radii: `--r-control` 6, `--r-card` 8, `--r-pill` 9999. Every control wears 6.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them. A chip inside a card padded `--space-3` is
`calc(8px - 12px)` — which is negative, and the correct reading of a negative
result is *this pair should not nest*. Give the chip the pill radius instead,
or drop the card's padding to 4 and give the chip `calc(8px - 4px)`. Concentric
curves are what separates machined from stuck-together, and two identical radii
at different depths is the tell.

Spacing is a 4px grid: `--space-1` 4 through `--space-6` 32. The shell is
measured, not chosen — topbar 56, sidebar 224 with items 35 tall at 6/12
padding, table header 44, cells at `10px 16px`.

## Components

- **Buttons.** Height 36, radius 6, padding-inline 16, weight 500, label at 14.
  *Primary:* `--accent` fill, `--accent-ink` label — and the label colour is
  stated on the rule, never inherited, because an anchor reset that says
  `color: inherit` will otherwise win it. *Secondary:* `--panel` fill with a
  1px `--edge` border. *Ghost:* no fill, `--muted` label. **Hover:** primary
  moves to a darker step of its own hue, secondary's border moves to
  `--muted`, ghost's label goes to `--ink` — background, border and colour
  only, never a transform. **Active:** no translate and no scale; the reference
  presses nothing. **Disabled:** opacity .45, and the label keeps its colour so
  the shape stays legible.
- **Cards.** `--panel`, 1px `--border`, radius 8, no shadow. Header row is
  `14px 20px` with a bottom seam; body is `20px`. **A card is used when the
  content is a record.** For a list of paragraphs use a seam between them and
  no box at all — the reference's own settings pages are seams, not cards.
- **Inputs.** Height 34, radius 6, 1px `--edge`, `--bg` fill so the field reads
  as recessed against the panel. Label above at 14/500, hint below at 14 in
  `--muted`. **Focus:** a 3px ring at 16% of the ink plus the border moving to
  30% — never an outline colour change alone. **Error:** the border takes
  `--danger`, the hint takes `--danger`, and the hint replaces the help text
  rather than joining it.
- **Navigation.** Topbar 56 with a bottom seam, sticky, `--bg` fill and no
  shadow at any scroll position — the reference's bar does not change shape
  when the page moves, and adding that is the most common way to break this
  pack. Sidebar 224, items 35 tall at radius 6; the **selected** item takes a
  tinted fill and a 2px rail on its leading edge. Mobile: the sidebar becomes a
  disclosure and the bar keeps only the brand, the disclosure and one action.
- **Loaders.** Skeleton blocks whose geometry matches the real layout — same
  heights, same radius 6, filled at 6% of the ink. No spinner anywhere, and no
  shimmer: the reference's skeletons are static.
- **Empty states.** Centred in the card that would have held the data: a 40px
  dashed ring, a 16px/600 line saying what is absent, one sentence in `--muted`
  at 44ch, and the primary that would create the first record.

## Hero

The opening is **two columns, 1.05 : 1**, with the argument on the left and the
record on the right. Not an image and not a screenshot: the right column is a
card holding the shape of the thing the product manages, in the product's own
vocabulary.

The display headline is `--t-hero` at weight 700 and tracking `-0.025em`,
capped at **17ch**, which holds it to **three lines at 1440 and never more than
four**. A headline that wraps to five lines is a broken hero, not a long one —
if the copy will not fit 17ch, the copy is the thing to change.

The first viewport must contain: the headline, one lede at 54ch, the promise,
**the limit on the promise**, and one primary. It must not contain: a logo
wall, a metric that cannot be sourced, a second filled control, or a search
field that searches nothing. That last one is this pack's specific trap — the
reference has a real search box in its bar, and copying it into a marketing
page ships a control that lies.

## Responsive

- **Fluid type.** The dashboard steps are fixed and do not scale; only the
  landing register is fluid. `--t-hero` ships as
  `clamp(2.25rem, 4.6vw, 3.75rem)` — 36px at 390 and 60px at 1304 and above,
  a slope of 4.6vw. The lede is `clamp(1rem, 1.2vw, 1.125rem)`. Nothing below
  `--t-title` is fluid at all: a 14px body that scales is a 12px body on a
  phone, and this pack has no step below 12.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | Card header stacking its title and its action | CONTAINER | `container-type: inline-size` on the card root, `@container (max-width: 30rem)` on the header |
  | Stat grid stepping 4 → 2 → 1 | CONTAINER | container on the grid root, `@container` on the tracks |
  | Chip row wrapping to a second line | CONTAINER | container on the row, `@container` on the chip |
  | Topbar collapsing to the disclosure | PAGE | viewport `@media (max-width: 720px)` — the bar is the page's, not a component's |
  | Hero going from two columns to one | PAGE | viewport `@media (max-width: 1080px)` |
  | Page gutter `clamp(20px, 4vw, 40px)` | PAGE | the page owns it |
  | The card's own shadow-none-to-seam at narrow | SELF | **no container answer exists** — a container cannot query itself, and wrapping a consumer's markup is not the kit's business. Keep the viewport query |

- **Collapse.** The pack has no asymmetry, no overlap, no rotation and no
  negative margins, which is the one advantage of an interface grammar: there
  is nothing to unwind. What does collapse is the comparison table — below 720
  the `thead` is hidden and **every cell prints its own column name**, the row
  header included. A stacked comparison that labels only the value half shows a
  phone reader the argument as if it were the answer.
- **Viewport.** `min-h-[100dvh]` for full-height sections, never `100vh`.

## Motion tokens

One curve: `cubic-bezier(0.16, 1, 0.3, 1)`. Two durations: `--dur-state`
0.14s for a meaningful state change, `--dur-hover` 0.1s for background, border
and colour. Nothing else moves.

There is no stagger, no reveal-on-scroll and no entrance animation in this
pack. The reference has none, and a console that animates its own arrival is
telling the reader it is a brochure.

Reduced motion sets both durations to `0s` at the token layer, so every
consumer inherits it without writing a query.

## Signature motifs

1. **The seam.** A 1px rule at 7.8% of the ink, everywhere a lesser pack would
   put a shadow — under the bar, around every card, between every table row,
   under every section.
2. **The tinted selection with a rail.** A selected item takes the accent at
   7.8% as its fill and a 2px accent rail on its leading edge. It is the one
   place the accent is a shape rather than a word.
3. **The mono label.** Uppercase, tracked `0.05em`, 12px, `--muted`. It names
   things and never explains them.
4. **One column carries the weight.** In every table exactly one column takes
   full ink and the rest sit at `--muted`. The eye is told where the answer is
   instead of comparing six equal cells.
5. **The status chip.** A 6px dot in the mark colour, the state named in full
   in the word colour, on the wash. Three tokens, one object.

## Signature element

**The record card in the hero's right column.** One card, hairline seam, no
shadow, holding several rows of the thing the product manages — each row named
by the role it does, each stating its state as a chip and what can be done to
it next.

It carries the pack because it is the argument and the interface at the same
time: the page is not describing a console, it is standing one next to the
sentence that claims it exists. Everything around it is quiet — one accent, no
second fill, no image — so that the card is the thing a reader remembers.

## Micro-interactions

- **Hover** changes background, border or colour. Never a transform, never a
  shadow, never a scale.
- **focus-visible** is a 3px ring at 16% of the ink plus the border at 30%, on
  every control including the ones a mouse would never reach. The ring is the
  same on a button, an input and a link — one focus idiom, not three.
- **Keyboard.** The disclosure that replaces the sidebar is a `<details>`, so
  it opens with the keyboard and works with scripting off. The skip link is the
  first focusable element and clears the sticky bar.
- **Selected** is not hover. A selected item keeps its tint and rail after the
  pointer leaves; a hovered one does not.

## Bans

- **No shadow as elevation.** One lift exists, for a menu. A card with a shadow
  is not this pack.
- **No second accent.** One functional colour. `--info` is deliberately the
  same value as `--accent`, which is the reference's own decision.
- **No accent in a chart.** A bar wearing the button's colour tells the reader
  the bar is clickable.
- **No status by colour alone.** Dot plus word, every time.
- **No search field that searches nothing**, and no window chrome, title bar or
  traffic lights anywhere. This pack's reference is a real console and the
  temptation to draw a fake one is its specific occupational hazard.
- **No body text below 14px**, and no scaling of the body at any width.
- **No uppercase in a table header.** The reference does not do it, and its
  absence is what makes those tables read as software rather than as a report.
- **No entrance motion.** Nothing animates on arrival.

## Gotchas

- **Six chart series will not fit and the arithmetic says so.** Six
  distinguishable steps need about 60 L\* of range; the dark end is bounded by
  usefulness and the light end runs into the page, so the palest step measures
  **1.38** against the field — present in the picture, absent to the eye. Four
  is what clears, at 3.31 on light and 4.61 on dark. **The number of series is
  a decision of the palette, not of the data**; bucket the tail into an
  *Other* row rather than adding a fifth colour.
- **A monochrome chart palette is the weakest, not the safest.** Pure ink steps
  look like the most austere choice and hold **two** series on white (3.22) and
  three on ink (4.25); a third ink step on white lands at 2.72, under the
  non-text floor. If the design calls for monochrome, it is calling for two
  series.
- **The seam's two registers will not match at one shared alpha.** At 7.8% the
  light seam measures ΔL\* 5.99 against the dark's 8.79 — a 2.79 gap, and the
  register leaning hardest on hairlines gets the weakest one. Both meet at
  ≈7.4, which is what the alphas in the token layer solve for (0.094 light,
  0.068 dark). Raising only the light one coarsens a hairline the pack is drawn
  with; lowering only the dark one flattens the register that reads best.
- **The control edge cannot be reached by tinting the ink on this field.** No
  reasonable alpha gets to 3:1 on `--bg` — 0.46 gives 2.94 — so `--edge` is solved
  directly rather than stepped off `--border`. A pack that reuses the seam as a
  button's boundary ships controls whose edges fail WCAG 1.4.11, which is the
  defect this token exists to prevent.
- **An earlier reading of this reference had three values wrong**, and they are
  named here rather than quietly corrected: `--text-xs` was taken as 12px when
  it is 14, the sidebar as 244px when it is 224, and the border asymmetry was
  attributed to `--border` when it belongs to `--sidebar-border`. All three came
  from reading the served stylesheets alone. The running product is what
  corrected them.
