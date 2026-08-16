# Style pack — Vitrine

Origin: [attio.com](https://attio.com) — extracted 2026-08-11.

A white field on which structure is drawn **entirely in hairlines**: no card
fill doing elevation, no shadow doing depth. A serif display over a sans body.
The primary control is the **ink**, never the accent — on a page whose whole
language is a hairline, an accent-filled button is the loudest object by a wide
margin, and the accent's job here is to mark what can be **read**. The signature
is the **framed record**: a hairline rectangle with an inset highlight, holding a
specimen of the thing the product manages.

Contract: widened — all thirteen headings.

## Register

Choose Vitrine for **the page a serious product ships as its front door**: B2B
software sold on trust, security and compliance surfaces, specification and
comparison pages, and any site where the reader is evaluating rather than
browsing. It is the pack for a company that would rather be believed than liked.
**Standalone.**

**Not for:** consumer launches, anything selling on delight, a brand whose
differentiator is warmth, or a product with nothing concrete to show. Vitrine's
whole method is showing the thing in a frame; with nothing to put in the frame
it is a very quiet page about nothing.

## Palette

Ready-made token layer: [`tokens/vitrine.css`](tokens/vitrine.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#ffffff` | page field |
| `--panel` | `#f3f4f6` | the grouping step — grey, not white |
| `--ink` | `#1c1d1f` | primary text, **and the primary control** |
| `--muted` | `#505967` | secondary text |
| `--border` | `#dadde4` | the hairline that draws every structure |
| `--border-strong` | `#c8ced7` | the divider that must be seen |
| `--edge` | `#898e95` | the visual boundary of a **control** |
| `--accent` | `#1f5fb0` | THE single accent — links and marks, never a fill |
| `--control` | `#1c1d1f` | the primary control is the ink |

### Floors, and what each colour may mean

**Three of the reference's own colour roles fail WCAG on its own canvas and are
not copied.** Every value here is the reference's *except* where a measurement
says it cannot be, and the token layer marks each of those.

Body and secondary text clear AA on the field and on the panel in both
registers. The accent marks what can be read; the ink marks what can be pressed.

**Status is never by colour alone.** Every state is a dot or an icon **plus a
word**. The green/amber/red triple is the classic confusion set, so the word
carries the meaning and the colour reinforces it.

**The status set is complete and measured**, including `--danger` — this is the
one pack of the five ported from live references whose reference paints an error
state, so nothing in its semantic set is derived.

## Type

Three families, each with one job.

- **Display — Newsreader**, a serif, for headlines only. It is what makes the
  page read as a document rather than as an app.
- **Body — Inter at 400.** Every sentence.
- **Data — a system mono**, for figures, identifiers and units inside the frame.

Scale: `--t-meta` 12, `--t-body` 16, `--t-card` 18, `--t-title` 24,
`--t-section` 32, `--t-page` 40, `--t-hero` 60. Measures: 64ch prose, 54ch lede.

**The serif is for headings only, which is the reference's own rule.** A serif
paragraph in this pack reads as a magazine and takes the product with it.

## Texture & surface

**Structure is drawn.** A group is a hairline box or a hairline above and below.
`--panel` is a grey step used for grouping, not for lifting: it makes a region
read as *held together*, never as *above*.

There is exactly one shadow token and it is the frame's own — a 1px inset
highlight plus a soft 24px drop at −12px spread. **It is used on one object per
page** and it is not elevation, it is glass: the inset line is what makes a
rectangle read as a case rather than as a box.

Radii: `--r-control` 6, `--r-card` 10, `--r-pill` 999.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them. A control inside a card padded `--space-2` is
`calc(10px - 8px)` = 2, not 6 — so a button inside a card is visibly tighter
than the same button beside it, and matching them is the tell that the layout
was assembled rather than machined.

Spacing is a 4px grid.

## Components

- **Buttons.** Radius 6, 16px label, weight 500. *Primary:* the **ink** fill
  with `--control-ink`. *Secondary:* `--bg` with a 1px `--edge`. *Ghost:* no
  fill. **Hover** darkens the ink or moves the border; **active** presses
  nothing; **disabled** is opacity .45.
- **Cards / containers.** A 1px `--border` box at radius 10 on `--bg`, or a
  `--panel` region with no border at all — one or the other, never both. **The
  framed record is the exception** and carries `--shadow-1`.
- **Inputs / forms.** Label above at 16/500, a 1px `--edge` field at radius 6,
  hint below in `--muted`. **Focus** is a 3px accent ring at 35% — the one place
  the accent appears as a surface. **Error** puts `--danger` on the border and
  replaces the hint.
- **Navigation.** A bar with a bottom hairline, no fill change on scroll. The
  sign-in is a ghost, because the hero already spends the page's one filled
  control.
- **Loaders.** A hairline progress rule in `--accent`, 1px. Skeleton blocks are
  allowed only inside the frame, where a fill already exists.
- **Empty states.** Inside a hairline box: one serif line at `--t-card`, one
  sentence at 44ch in `--muted`, and the action. No illustration.

## Hero

Two columns — the argument left, the **framed record** right. The frame is the
composition: a hairline rectangle with the inset highlight, holding a specimen of
the thing the product manages, with a caption above it and an honesty line
below saying what it is.

Display at `--t-hero`, serif, tracking `-0.02em`, capped at **18ch**, which
holds it to **three lines at 1440** inside a `--page` container. A headline that
reaches five lines is a broken hero.

The first viewport must contain: the display, one lede at 54ch, the promise, the
**limit on the promise**, one ink primary, and the frame. It must not contain: a
second shadow, an accent-filled control, a logo wall, or a photograph.

## Responsive

- **Fluid type.** `--t-hero` ships as `clamp(2.5rem, 4.2vw, 3.75rem)` — 40px at
  390 and 60px at 1429 and above, a slope of 4.2vw. `--t-section` is
  `clamp(1.75rem, 2.6vw, 2rem)`. Body does not scale.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | The frame's rows going from label-beside-value to stacked | CONTAINER | `container-type: inline-size` on the frame, `@container` on the rows |
  | A card head stacking its title and its meta | CONTAINER | container on the card, `@container` on the head |
  | Hero going from two columns to one | PAGE | viewport `@media (max-width: 1000px)` |
  | The bar collapsing to a disclosure | PAGE | viewport |
  | The frame's own inset highlight thinning at narrow | SELF | **no container answer exists** — the highlight is on the element that establishes the container. Keep the viewport query |

- **Collapse.** The frame goes **below** the argument when the hero stacks. The
  comparison table hides its head below the breakpoint and **every cell prints
  its own column name**, the row header included — labelling only the value half
  shows a phone reader the argument as if it were the answer.
- **Viewport.** `min-h-[100dvh]`, never `100vh`.

## Motion tokens

One curve, `cubic-bezier(0.2, 0, 0, 1)`. `--dur-state` 0.16s, `--dur-hover`
0.12s. Nothing else moves.

No entrance animation. A page arguing that it can be trusted does not perform on
arrival.

Reduced motion sets both durations to `0s` at the token layer.

## Signature motifs

1. **The hairline instead of the card.** Structure is drawn, never filled.
2. **The framed record**, with its inset highlight.
3. **The serif display over sans body.**
4. **The ink primary.** The loudest control carries no colour.
5. **The grey panel that groups without lifting.**
6. **The stated limit.** Every promise on the page has its bound written under
   it, marked by a rule rather than painted in the link colour.

## Signature element

**The framed record in the hero.** A hairline rectangle with an inset highlight,
holding a specimen of the thing the product manages, captioned above and
qualified below.

It carries the pack because it is the argument and the evidence in one object:
the page does not describe what the product holds, it puts one in a case next to
the sentence claiming it exists. Everything around it is unfilled and unlifted so
that the frame is the only thing with a surface.

## Micro-interactions

- **Hover** moves colour and border. No transform, no shadow, no fill appearing
  where there was none.
- **focus-visible** is a 3px accent ring — the one place the accent is a
  surface — identical on every control.
- **Keyboard.** The nav disclosure is a `<details>` and works with script off.
  The skip link is the first focusable element and clears the bar.
- **Selected** is a rule under the item in `--ink`, not a fill.

## Bans

- **No accent fill on a control.** The accent marks what can be read.
- **No second shadow.** One framed object per page.
- **No serif paragraph.** The serif is for headings, which is the reference's
  own rule.
- **No card that is both bordered and filled.** One or the other.
- **No photograph and no illustration** in the first viewport.
- **No promise without its limit**, and the limit is marked by a rule rather
  than set in the accent — a bound that looks like a link gets clicked.
- **No status by colour alone.**

## Gotchas

- **`--panel` groups, it does not lift, and the difference is invisible in a
  mockup.** A grey region reads as *these belong together*; the moment it also
  gets a shadow it reads as *this is above*, and the page acquires a depth order
  it was never designed to have.
- **The anchor reset will eat the link colour.** A pack rule of the form
  `.vt a { color: inherit }` scores 0,0,1,1 and beats every single-class utility
  written to colour a link — this site shipped a grey link for a day because of
  it. Write the reset with `:where()` so it drops to zero specificity.
- **Three of the reference's colour roles fail WCAG on the reference's own
  canvas.** They are not copied, and the token layer marks each substitution. A
  future editor "restoring the original values" would be restoring three
  failures.
- **The frame's inset highlight is what makes it a case.** Remove the 1px inset
  and the object becomes a bordered box with a drop shadow, which every pack has.
  The highlight is the whole difference and it is one line.
- **A serif display below 24px stops reading as a headline.** Below `--t-title`
  the sans carries the heading; the serif is for `--t-title` and above.
