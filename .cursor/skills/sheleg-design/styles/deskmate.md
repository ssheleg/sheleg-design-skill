# Style pack — Deskmate

Origin: <https://viktor.com> (2026), the front page of an AI employee that works inside
a chat client. The site is Next.js and there is no vendor layer to separate out: three
authored stylesheets totalling 364,905 bytes, declaring a primitive ramp, a semantic
layer over it and a per-component slot layer over that. Every value below was read on
2026-08-27 off **computed styles on the live page** through CDP at 1440×900 — 1,191
visible of 1,888 elements on a 10,211px page — with four more pages read for the
components the front page does not paint: `/contact-sales` for the form field,
`/integrations` for the search shell and for what a search with no match does, `/business`
for the dusk surface, and `/brand`, which publishes the palette and both faces by name.
Narrow behaviour was read at 500×844, Chrome's minimum window width on macOS; the
reference's smallest breakpoint is 40rem and nothing sits between 390 and 500, so that is
the same branch a phone takes. Ratios were computed by importing this repository's own
palette gate.

A warm beige working day with **one light source, and it is above the top edge**: every
gradient in the reference's own library originates at or above `y=0` and runs the same
four stops — peach, lilac, violet, deep navy. One ramp, three jobs: it washes the field
under the first screen, it fills a panel, and with `background-clip: text` it fills one
word of a heading. Two faces carry the brand and a third belongs to the quoted chat
client. Everything a hand touches is a pill; everything else is a 32px slab.

The identity in one sentence: **the product's own messages are the page's
illustrations** — a card here is a quoted line of work with the artefact it produced
underneath it, and the page's set piece is a framed transcript.

Contract: widened — all thirteen headings.

Themes: light only — the second block (`[data-surface="dusk"]`) is a SURFACE variant, not a theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Deskmate for **products sold as a colleague rather than a tool** — AI employees
and chat-native agents, assistants that live in Slack, Teams or Discord, delegation and
approval surfaces, anything whose promise is *you ask in the channel you already use and
the work comes back there*. It suits a page whose proof is **a conversation**: a request,
a reply, and the file, dashboard or deployment the reply produced.

It also suits the harder half of that pitch — the page has to show a third party's
interface without letting that interface become the design. This pack's answer is a
quarantine, and it is the reason to reach for it over building one: the quoted client
keeps its own face, its own ink and its own two status colours under a `--quoted-*`
namespace, and the brand keeps everything outside the frame.

Standalone: it does **not** ride the SHELEG cinematic motion layer. Counted on the front
page, the whole budget is an entrance on a 0.64s ease-out, a 0.15s state clock on 115
elements, three linear loops (42s, 20s and a 16s drift), one stepped logo lockstep, and a
transcript that scrolls itself. There is no scroll clock at all — `animation-timeline`
appears zero times in 364,905 bytes and exactly one element is fixed — so
`MOTION_INTENSITY` above **4** has nothing legal to buy here.

**Not for:** dense operator chrome. The elevation model is a field step and a 1.25px
hairline, the smallest radius in the ramp is 8.4px, and a control is 56px tall or 44px
at the small size — a fourth nested panel has nothing to sit on and a toolbar of pills
is a novelty item. That
is `workbench`'s half, and `router`'s. Not for regulated, clinical or public-sector
pages, where a peach-to-violet bleed under the fold reads as a consumer app. Not for
anything sold on austerity: this page spends 38 gradient fills, and a pack that spends
none of them is `notation`.

### The fork against [`tenor`](./tenor.md), which is the register collision

Both are sold to the person who will be asked to manage an autonomous worker. `tenor`
names "AI workforce and agent-operations platforms, autonomous back-office"; that is a
description of this reference too, and a router reading either register alone cannot
separate them.

The separation is **what the page offers as proof**, and it is visible in the first
screen:

| | `tenor` | Deskmate |
|---|---|---|
| Proof | a recording of the product working | **a quoted conversation** and the artefact under it |
| Colour's job | one hue, and it only appears under the cursor | **one four-stop ramp carrying the identity** — 38 gradient fills |
| Radius | none | **43 pills and 52 slabs at 32px** |
| Field | warm management paper | warm beige with a dusk bleed under the fold |
| Faces | three, all the brand's | **two brand faces and a third that is the client's** |
| Argument | a management thesis, set large and tight | a colleague's message, quoted |

So: `tenor` when the buyer must be persuaded that a category exists and the page has to
read like a memo. Deskmate when the product is already legible as a person and the page's
job is to show them working. The give-away is the screenshot: if it is a product
dashboard, it is `tenor`; if it is somebody's chat client with a message in it, it is
this one.

### The fork against [`cyclorama`](./cyclorama.md), which is the gradient collision

Both spend a colour ramp as their signature. Here it is **anchored** — a static
peach-to-navy radial whose origin is always above the top edge of the box it lights,
painted once per section and never animated. There it is a **loop**: a field that cycles
behind a fixed subject, with WebGL and real pinning. A ramp that moves is `cyclorama`; a
ramp that hangs is this one.

### The fork against [`chorus`](./chorus.md), which is the speech-bubble collision

Both make a chat bubble the page's illustration and both sit on warm paper, so a
thumbnail cannot separate them. The separation is **whose bubble it is**. Deskmate's
transcript is the *product's own* — a request the user made and the work that came
back — and its geometry is a pill over a 32px slab. [`chorus`](./chorus.md)'s bubble
is a *stranger's*, asked on a forum the brand does not own, and its geometry is one
squared corner on three 24px ones. If the quoted words belong to your product, stay
here.

## Palette

Copy [`tokens/deskmate.css`](./tokens/deskmate.css) verbatim. Every **colour** there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio. The geometry
ramps (spacing, radii, type sizes) carry a provenance note per band rather than per
value, because a band was measured as a band.

| Role | Token | Value | On `--bg` |
|---|---|---|---|
| Field | `--bg` | `#faf5f1` | MEASURED — 11 wide fills |
| Card | `--surface` | `#ffffff` | MEASURED — 68 fills, and the whole elevation model |
| Wash | `--wash` | `#f1edff` | MEASURED — 5 fills, the badge and the eyebrow |
| Ink | `--ink` | `#1a182b` | 16.04:1 — every dark word on the page |
| Secondary | `--ink-soft` | `#716f7e` | 4.53:1 — the lede and the caption |
| Bars and icons | `--ink-faint` | `#9693a3` | 2.77:1 — declared non-text, see Gotchas |
| Accent | `--accent` | `#6e47ff` | 4.84:1 |
| Eyebrow | `--accent-deep` | `#4e32b5` | 7.93:1 |
| Warm stop | `--peach` | `#ffbb98` | 1.51:1 — declared non-text, a stop and a star |
| Last stop | `--dusk` | `#150079` | 14.83:1 — and the dusk surface's own field |
| On a card | `--on-surface` | `#1a182b` | 17.36:1 on `--surface`, and it does NOT invert |
| On a card, quiet | `--on-surface-soft` | `#716f7e` | 4.91:1 on `--surface` |

**`--ink` is for words on `--bg`; `--on-surface` is for words on a card.** On the light
field the two are the same value and the distinction reads as decoration. On the dusk
surface it is the whole difference: `--surface` stays white there — measured on
`/business`, where a card inside an inverted section keeps its white fill — so a card
that paints its heading in `--ink` paints **white on white**. Every component that sits
on a card takes the `--on-surface` pair, and the four that sit on the field
(the display, the lede, a stat's figure, a section's own heading) take `--ink`.

**One accent, and it needed no correction.** It writes and it fills: `#6e47ff` is
4.84:1 on the field `#faf5f1`, and `#ffffff` on `#6e47ff` is 5.24:1. A single token
carrying both jobs is rare enough in this library to say out loud. The eyebrow's darker
step exists because the reference uses it, and it is safe on both fields it lands on:
`#4e32b5` is 7.93:1 on the field `#faf5f1`, and `#4e32b5` on the wash `#f1edff` is
7.48:1.

**The peach is the second brand colour and it is never a word.** `#ffbb98` is 1.51:1 on
`--bg`. It is the ramp's warm stop, a rating star, and a rule inside a dusk panel. A
sentence in it is unreadable on any field this pack ships.

**Status is never by colour alone**, and the reason is structural: the brand
layer paints no state at all. The one place the reference paints one is inside the quoted
transcript, in the chat client's palette — an approve green `#007c58`, a mention blue
`#1264a3`, a reject rule `#cecece` — and those belong to the quote, not to the page. So
`--good` is that green, which clears AA unchanged at 4.82:1 on `--bg`; `--warn` and
`--danger` are SELECTED from ramps the reference declares itself; and `--info` is
deliberately an alias of `--accent`, because informational **is** the brand violet here
and a fifth hue would be an invented value. Every pair across the four roles and the
accent clears the hard floor at full colour, and all but one clears 15 units at full
colour and 8 under protanopia, deuteranopia and tritanopia. The exception is `--warn`
against `--danger` at 6.4 under protanopia — what an amber and a red do to red-blind
vision at any lightness — which is why every state here takes a glyph or a word beside
its colour, exactly as the reference's own checklist does.

**The dusk surface remaps rather than inherits.** The light status set measures 2.6–4.1:1
on `#150079`, and the accent itself is 3.06:1 there, so the dusk block lightens all five.
Its set is the better of the two ramps: every pair clears 15 units at full colour and 10.4
under all three dichromacies, with no tight pair at all.

## Type

Two brand faces and a third that is not the brand's. That third one is the pack's
unusual claim and it is load-bearing.

| Role | Family | Size | Weight | Tracking |
|---|---|---|---|---|
| Display | Ulm Grotesk | 80px → 72px → 64px | 400 | −0.06em |
| Section | Ulm Grotesk | 48px | 700 | −0.06em |
| Row | Ulm Grotesk | 18px | 500 | 0 |
| Lede | Gellix | 20px | 500 | 0 |
| Body | Gellix | **16px** | **500** | 0 |
| UI | Gellix | 14px | 500 | −0.01em on a control |
| Caps label | Gellix | 12px | 500 | **+0.01em** |
| Quoted transcript | Lato | 16.5px and down | 400–800 | 0 |

**Body copy is weight 500 and that is the pack's most breakable claim.** 146 text nodes
render at 500 against 77 at 400, and 400 is exactly what an unset `font-weight` gives
you — so a kit that declares `--weight-body` and consumes it nowhere renders the entire
page one step light while every gate stays green. That is not hypothetical: it is the
defect `nameplate` shipped in 1.48.0 and the reason the render step exists.

**The display is 400 and the section heading is 700.** The published brand page labels
the display style "Bold"; the rendered `h1` is 400 on 80px and three `h2`s are 700 on
48px. Read the render.

**Tracking is one-sided.** The display is pulled to −0.06em, which is −4.8px on 80px and
−3.84px on 64px, and it is the only large negative value in the pack. Controls are pulled
a tenth as far, −0.16px on 16px. The 12px caps label is the one thing pushed open, and
only to +0.12px. There is no wide-tracked micro-label register here; a pack that adds one
is quoting a different library.

**A measure in `ch`, and the reference has none.** It holds its lede in a grid column
rather than in a measure — `max-width: none` on both the headline and the paragraph — so
this pack states the measure the reference implies and ships it as
`--measure-lede` (62ch) and `--measure-body` (68ch), against Gellix at 16px. Where the two faces are substituted the
column holds and the character count moves, which is the point of stating it in `ch`.

**Both brand faces are licensed and the substitutes are a pack decision.** Ulm Grotesk
and Gellix are named first in `--font-display` and `--font-body`. Named second are Outfit
and Figtree, chosen because Outfit is the closest open geometric grotesque with the
reference's single-storey `a`, and Figtree holds a 16px/1.4 paragraph at weight 500
without widening it. This is a substitution, not a measurement, and it is marked as one
at the declaration. Font loading is the consumer's: there is no `@font-face` here, by the
library's own rule.

## Texture & surface

**Elevation is a field step.** 68 white fills sit on a beige field with 51 hairlines
between them, and the entire 10,211px page carries **two** shadows, which is why the
pack ships exactly two shadow tokens and no ramp: `--shadow-panel` is the 5% whisper
under the signature frame (`0 3.863px 17.769px`), and `--glow-bloom` is the single purple
bloom (`0 0 16px 8px` of purple-900 at 8%) that the reference spends **once on the whole
page**. The pack does not prescribe where — the census records one instance and not which
element carried it — so the rule is the count: one bloom per page, on the object the page
is about, and if you cannot name that object do not spend it. A card is white on beige; a
panel inside a card is beige on white; the third step is a hairline and there is no
fourth.

**The hairline is 1.25px and it is an alpha of the ink.** The reference declares
`--border-main: 1.25px` and every border on the page is that width, at the ink's 8%, 10%
or 12%. Composited on white those are 1.17:1, 1.22:1 and 1.28:1 — far below the 3:1 mark
floor, which is correct for a hairline and is why the Bans below require a second
separator beside it.

**Radii: a pill for the hand, a slab for the eye.** 977 of the 1,191 visible elements
compute 0px; of the rest, 43 are fully round, 52 take the 32px card, 48 take the 14px row
and 26 take the 36.4px section.

- **The ramp defines the token set.** It is proportional from a 14px root — the
  reference's own `--radius` — times 0.6, 1.4, 1.8 and 2.6: `--r-sm` 8.4px, `--r-chip`
  19.6px, `--r-shell` 25.2px, `--r-section` 36.4px. The card's `--r-card: 32px` is a
  literal beside the ramp because the reference writes it as one, 33 times.
- **Subtraction adjusts a nested instance.** The signature frame is the worked example
  and the reference does the arithmetic at runtime: outer 47.319px, a 15px inset, inner
  32.254px. In this pack's tokens that is `--r-frame: 48px`, `--frame-inset: 15px` and
  `--r-frame-inner: calc(48px - 15px)` = **33px**. Never the same value on both boxes;
  the concentric curve is what makes the frame read as machined rather than stacked.

**Sections hang.** The hero's slab takes `border-radius: 0 0 36.4px 36.4px` — bottom
corners only — and so does the navigation, at 30px. Nothing in this pack has its top
corners rounded against the page edge, because the light comes from above and a rounded
top corner would cut it.

**The one texture is the ramp itself.** There is no grid, no noise field and no pattern:
38 gradient fills and a `backdrop-blur(6px)` layer inside the signature frame are the
whole surface vocabulary.

## Components

**Buttons.** Two sizes, three variants, and the geometry is shared with the input on
purpose — a pill at `--control-h` (56px) with `--control-px` (40px) of horizontal
padding, `--rule-w` of border, 16px/500 at −0.01em. The small size is
`--control-h-sm` (40px) with 24px padding at 14px, and it is the navigation's pair —
**and it renders at 44px, not 40**, because `--tap-min` is a floor and the token keeps
the measured value beneath it. That is the one geometry this pack corrects rather than
copies, and the render is where it becomes visible: the token says 40 and the browser
says 44.

- *Primary* — `--ink` fill, `--on-ink` label, border the same ink. Hover: opacity 0.8.
  Active: `translateY(1px)`. Disabled: opacity 0.5 and `pointer-events: none`.
  Focus-visible: the border moves to `--focus-color` and `--focus-ring` appears outside
  it.
- *Secondary* — `--surface` fill, `--ink` label, border the ink at 12%. Hover mixes 6% of
  the ink into the fill rather than changing opacity; everything else is the primary's.
- *Announcement* — `--gradient-dusk` as the fill with an `inset 0 4px 4px` white-at-25%
  highlight along the top edge, white label. It is the only gradient-filled control in
  the pack and it appears **once per page**, on the offer the page exists to make.

**Cards / containers.** The card is the pack's most repeated object and it is built in
two halves, which is what makes the page look like a transcript rather than a feature
grid:

- The **message half** takes `--gradient-dusk`, white text, a byline row (a name, a small
  `APP` badge, a time), and under it an illustration of the artefact produced — a file
  tile, a set of connected tool marks, a checklist. Radius `--r-card` on the top corners.
- The **explanation half** is `--surface`, a 24px heading in `--on-surface` and a 16px
  paragraph in `--on-surface-soft`, with 24px/32px/32px of padding. Radius `--r-card` on
  the bottom corners. Those two tokens rather than `--ink`: a card keeps its white fill
  inside a dusk section, so the ink that sits on it cannot invert with the field.
- No border and no shadow on either half; the two fills are the separation.
- The small tile — a chip, a logo, a status row — is `--surface` at `--r-chip` with a
  `--rule-w` hairline at the ink's 5% and 10px of padding.

**Inputs / forms.** A pill field at `--control-h`, `--surface` fill, `--rule-w` border at
the ink's 12%, 24px of horizontal padding, 16px/400 with the placeholder in `--ink-soft`.
The label sits above at 16px/500 in `--ink` with 8px beneath it. Focus-visible: the border
moves to `--focus-color` and `--focus-ring-field` (the ring at 40% rather than 50%)
appears. Invalid: the border takes `--danger` **and** a message — the reference's own
`aria-invalid` colour misses the mark floor and is corrected in Gotchas.

The second field shape is a **search shell**: a `--r-shell` box, `--surface`, a
`--rule-w` hairline at the ink's 8%, 24px/32px of padding, holding a transparent
borderless input. It is 74px tall and it is what a directory search looks like here.

**Navigation.** A white slab that **hangs from the top edge**: fixed, `z-index: 50`,
inset 40px from each side (12px below 40rem), 65px tall (57px narrow),
`border-radius: 0 0 30px 30px`, padding 12px with 32px on the leading edge. No shadow, no
`backdrop-filter`, no border — measured, and it is the whole difference between this and
every frosted sticky bar. Menu triggers are ghost pills: 12px/6px of padding at 14px,
hover fills with the ink at 5%, focus-visible takes a 2px ring at `--focus-offset`. The
scrolled shape is the resting shape; the slab does not shrink, blur or gain a rule.

**The mobile shape is the one place the slab does change.** Below 40rem it takes
`--slab-h-sm` (57px), its inset drops to 12px, and **the link row is removed** in favour
of a single toggle at the `--tap-min` floor. That is not a preference: a slab is one
flex row, so a link row that survives to 390px pushes the trailing control past the
viewport — measured at 515px against a 390px page in this pack's own kit before the
collapse was written, which is what a render catches and a structural gate cannot.

**Loaders.** The brand layer ships **none** — no authored skeleton, shimmer or spinner
class exists in 364,905 bytes, and the two utilities that could paint one (`pulse` at 2s,
`spin` at 1s) reach no element on any of the four pages read. What the reference actually
draws is a **placeholder bar**: `--ink-faint`, 4px radius, 17px tall, in the quoted
transcript's channel rail, and it is content standing in for content rather than a
loading state. So the loading idiom here is a pack decision, and it follows from the
motion budget: a skeleton block in `--ink-faint` at the shape's own radius, **no
shimmer**, because the fastest clock on the page is 0.15s and a travelling highlight
would be the liveliest thing on it.

**Empty states.** The reference's is a measured refusal, not an absence: a search on
`/integrations` matching nothing collapses the grid to 1280×0 at 1440 and says nothing at
all — no message, no count, no reset. The pack's answer is a `--surface` card at
`--r-card` holding a 16px/500 line in `--on-surface`, one sentence in
`--on-surface-soft`, and a secondary pill that clears the filter. An empty result is a state, and a state that
paints nothing is indistinguishable from a broken query.

Every interactive element takes `--tap-min` (44px) as a height floor. This is a
correction: 47 interactive elements render under 44px tall at the narrow width, including
the navigation toggle at 48×32 and the transcript's reaction pills at 42×24.

## Hero

A marketing opening: full width, not full height, and it ends in the set piece rather
than beginning with it.

- The page holds `--page-max` (90rem) and its gutter steps through four tokens —
  `--gutter` 20px, `--gutter-2` 40px, `--gutter-3` 56px, `--gutter-wide` 80px — because a
  step a consumer cannot reach through a variable is a step the pack did not ship. The
  hero's own top padding is 176px at 1440, because the navigation slab hangs into it.
- Field `--bg` with `--gradient-dawn` blooming from above the headline, and the slab's
  bottom corners rounded at `--r-section` where the field bleeds into `--gradient-fold`.
- A two-column grid at `1.15fr / 1fr` with a 56px gap: **the argument on the left, the
  offer on the right.** Left is an eyebrow row (a rating, a mark, a five-star set in
  `--peach`) then the headline. Right is one lede paragraph in `--ink-soft` at 20px and
  the control pair.
- Headline at `--t-display` in `--font-display`, weight 400, `--track-display`, on
  **exactly two lines** — and what holds that ceiling is the **grid column**, not a
  measure: 655px of the 1280px content width at 1440, with an authored break between the
  two sentences. The reference sets `max-width: none` on the headline and lets the column
  do it, which is a legitimate answer and is why it is stated here rather than guessed.
- **The second line takes the gradient**, filled with `--gradient-word` through
  `background-clip: text`, and it carries a solid `color` underneath first:
  `--gradient-word-fallback` is 4.95:1 on `--bg`. One gradient line per page and one
  word per section heading; a third is where this device stops being a signature.
- Below both columns, the framed transcript at full content width — 1280×663 at 1440 —
  bleeding into the fold. The hero's last object is the product being used, not a
  screenshot of it sitting still.
- What it must not carry: a logo wall (that is the next section's), a video, a second
  gradient control, or a headline over two lines.

## Responsive

Three widths, measured: 1440, 768 and the sub-640 branch read at 500.

- **The display steps, it does not flow.** 64px below 40rem, 72px from 40rem, 80px from
  80rem — and the tracking stays `--track-display`, so it is −3.84px at the small size and
  −4.8px at the large. The reference ships four `clamp()` calls in 364,905 bytes and not
  one of them is a type size; this pack keeps that, because a fluid display at −0.06em
  collides its own ascenders at the awkward widths between the steps.
- **The hero grid collapses to one column** and its gap goes 56px → 32px. The control pair
  goes full width at `--control-h`, which is how a 56px pill stays a 56px pill.
- **Gutters step 80 → 56 → 40 → 20px** through the four `--gutter*` tokens. The
  navigation slab's own inset goes 40px → 12px and its height 65px → 57px — that inset is
  the slab's and not the page's gutter, which is 80px at the same width. Section rhythm
  halves: 112px → 56px.
- **The frame's radius does not scale.** 47.319px at 1440 and at 500, with the same 15px
  inset — the concentric relationship is the object's identity and rescaling it makes the
  frame read as a different component.
- **Container queries.** Sorted by kind, because only the first two have a container
  answer. The reference itself declares one `container-type: inline-size` and two
  `@container` blocks in the whole stylesheet set, so this table is mostly a statement
  about what belongs to the page:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | The card's two halves stacking or sitting side by side | CONTAINER | `container-type: inline-size` on the card, `@container` on the halves |
  | A tile grid stepping 4 → 2 → 1 | CONTAINER | container on the grid, `@container` on the tracks |
  | Display 80 → 72 → 64px | PAGE | the headline answers to the viewport |
  | The hero's two columns | PAGE | it is the page's own grid |
  | The navigation slab's inset and height | PAGE | the slab is the page's |
  | Section rhythm 112 → 56px | PAGE | the page owns its rhythm |
  | The frame's own radius and ring | SELF | **no container answer exists** — the frame establishes the container, a container cannot query itself, and the radius does not change anyway |

- **Viewport.** `100dvh` for any full-height section, never `100vh`. The reference is
  mixed on this — 6 `dvh` against 7 `100vh` — and the pack takes the `dvh` half.
- No horizontal overflow: `documentElement.scrollWidth` equals the viewport at 1440 and at
  500.

## Motion tokens

| Token | Value | Spends on |
|---|---|---|
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | the state clock — MEASURED on 115 elements |
| `--ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | the entrance — MEASURED on 19 |
| `--dur-press` | 0.15s | the press, inside the doctrine's 100–160ms band |
| `--dur-fast` | 0.15s | a colour, a border, an opacity |
| `--dur-base` | 0.2s | MEASURED — 23 elements |
| `--dur-slow` | 0.3s | a disclosure opening — MEASURED on 9 |
| `--dur-enter` | 0.64s | the entrance, on the reference's own token |
| `--stagger` | 60ms | its `enter-delay` steps 0, 40, 60, 80, 120ms |
| `--enter-y` | 16px | the entrance travels 8px or 16px and never further |

Two clocks and no third: 0.15s for anything a pointer caused, 0.64s for anything the
scroll revealed. 1,010 of the 1,191 visible elements do not move at all.

**Reduced motion degrades to calm rather than to nothing**, and the reference already
does this in eleven branches worth copying: a marquee stops **at a static offset** rather
than snapping to zero, the gradient word keeps its fill by restoring
`-webkit-text-fill-color`, and an entrance resolves to `opacity: 1; transform: none`. The
token layer finishes the job by collapsing every duration and `--enter-y` to zero, so a
control still changes colour and still shows its focus ring while nothing travels.
`ease-in` is banned by the doctrine and does not appear in the reference either.

## Signature motifs

- **One light source, above the top edge.** Every gradient origin in the reference's
  library is at or above `y=0` — `at 50% 0%`, `at 52.06% -4.35%`, `at 31.42% -99.18%`.
  A gradient lit from below is the fastest way to lose this pack.
- **One four-stop ramp doing three jobs**: peach `#ffbb98` → lilac `#9e84ff` → violet
  `#6e47ff` → navy `#150079`, as a field bleed, as a panel fill, and as a text fill.
- **One gradient word per heading**, with its fallback colour declared.
- **Pills for the hand, 32px slabs for the eye** — 43 round controls and 52 slabs.
- **Slabs that hang**: bottom corners rounded, top corners square against the page edge.
- **The quoted message as illustration** — the card's top half is the product speaking,
  and the artefact it produced sits under the sentence.
- **Elevation by field step**: 68 white fills on beige, 51 hairlines, two shadows.

## Signature element

**The framed transcript.** A `--surface` frame at `--r-frame` with a 4px white ring, the
5% whisper under it, and inside it — inset by `--frame-inset` — a chat client's window at
`--r-frame-inner`, with the client's own face, its own ink and its own two status colours,
carrying one request and one reply that finishes with a checklist and an approval.

It is what a page in this pack is remembered by, and the reason is the quarantine. The
frame is the seam between the brand and somebody else's interface, and it is drawn as a
seam: a white ring, a concentric curve, and a namespace. Everything inside it is quoted;
nothing inside it is allowed out. Get that boundary wrong and the page's status colours
become a third-party UI's palette, which is exactly what happens to every team that
screenshots a chat client into a marketing page instead of rebuilding it.

Build it once as a component, quote real work in it, and let the rest of the page be
cards made of the same material.

## Micro-interactions

- **Primary press:** opacity to 0.8 over `--dur-fast`, then `translateY(1px)` while held.
  No shadow appears and nothing scales.
- **Secondary hover:** 6% of the ink mixed into the fill. The border does not move.
- **Card hover:** `translateY(-2px)` at most, gated behind `@media (hover: hover)` — the
  reference gates all six of its hover rules that way, and a lift that fires on a tap is
  a flicker.
- **Focus-visible:** the control's own border takes `--focus-color` **and** the ring
  appears outside it. Both, always: the ring alone composites to `#b6a3ff` on white
  `#ffffff`, which is 2.17:1, and that is why the border moves in the same state. The
  ring ships as a **literal first** and derives from the accent inside an `@supports`
  block — see Gotchas, because getting that order wrong removes the ring entirely.
- **Disclosure row:** 62px tall at `--r-root`, transparent until focus, opening over
  `--dur-slow`. The row's chevron rotates; the row does not.
- **Section reveal:** opacity and `--enter-y` on `--ease-out` over `--dur-enter`, with
  `--stagger` between siblings. It never gates content.
- **The transcript scrolls itself** at reading pace with its scrollbar hidden, and reveals
  a thin one (`#1a182b` at 24%, fully round) the moment a pointer takes over.

## Bans

- **No third shadow.** The page has two. Elevation is a field step and a 1.25px hairline;
  a `shadow-md` here is a foreign object.
- **No gradient under body text.** The ramp fills fields, panels and single display
  words. A paragraph on a four-stop ramp cannot hold a contrast ratio anywhere along it.
- **No second gradient control per page.** One announcement button, and the rest are ink
  or white.
- **The peach is never a word** — `#ffbb98` is 1.51:1 on the field `#faf5f1`.
- **No status by colour alone**, on either surface: a state takes a glyph or a word.
- **No square control.** A control is a pill; a container is a slab. Swapping them
  inverts the pack.
- **No top-rounded slab against the page edge.** Slabs hang.
- **No frosted navigation.** No `backdrop-filter`, no scroll-shrink, no rule appearing at
  the top of the page — measured, and the slab is the same shape at every scroll offset.
- **No scroll clock, no parallax scrub, no `animation-timeline`.** Zero occurrences;
  `MOTION_INTENSITY` above 4 has nothing to buy.
- **No shimmer on a skeleton.** The fastest clock is 0.15s.
- **No `100vh`.**
- **No `--quoted-*` token outside the frame.** Those are a third party's colours.
- **No `ease-in`.**

## Gotchas

**The published brand hex and the shipped token disagree, and the render is right.** The
reference's own brand page prints its soft-black as `#1B182A`; every rendered node uses
`#1a182b`. Both clear everything — `#1b182a` is 16.02:1 on the field `#faf5f1` and
`#1a182b` is 16.04:1 on the same field — so this is not a defect, it is a lesson about
which artefact to measure. A brand page is a claim; a computed style is what a reader
sees.

**Four corrections travel with this pack, each with its number at the declaration.**

1. *The error border misses the boundary floor by 0.03.* The reference's `aria-invalid`
   state paints its border in `#b5856c`, which is 2.97:1 on the field `#faf5f1` — under
   the 3:1 non-text floor, on the one state whose whole job is to be noticed. `--danger`
   here is a red that clears AA — `#d0202f` is 4.94:1 on the field `#faf5f1` — and the
   invalid state still takes a message beside the colour.
2. *The icon grey is not text.* `#9693a3` is 2.77:1 on the field `#faf5f1` and 3.00:1 on
   white `#ffffff`, and the reference sets muted icons in it. It is declared non-text
   here; an icon that must be read takes `--ink-soft` at 4.53:1 on `--bg`.
3. *Tap targets.* 47 interactive elements render under 44px tall at the narrow width, the
   navigation toggle at 48×32 and the transcript's reaction pills at 42×24 among them.
   `--tap-min` is a floor for every control.
4. *The dusk status set had to be rebuilt.* The light four measure 2.6–4.1:1 on
   `#150079`, and `--accent` itself is 3.06:1 there. Inheriting them would have shipped
   four unreadable states on the one surface that exists to carry a closing offer.

**`.dark` is not a dark mode and putting it on `:root` breaks the page.** There are zero
`prefers-color-scheme` queries in 364,905 bytes. The class is applied to sections, to
articles and — measured on `/business` — to a 371×56 button group that overrides one
border token locally. It is a surface variant, which is why this pack ships it as
`[data-surface="dusk"]`. Two consequences: the light field above an inverted section is
untouched, and the frame **re-declares its own tokens inside a dusk section** so the
quoted client stays light. That second one looks like a bug in the reference's CSS and is
the correct behaviour — a chat client screenshot that inverts with your marketing page is
a chat client nobody has.

**The gradient headline vanishes without its fallback colour.** `background-clip: text`
with `-webkit-text-fill-color: transparent` paints nothing where it is unsupported, and
the reference declares `color: #6748fd` underneath for exactly that reason. Ship the
`color` first and the clip second, in that order, or the page's largest sentence is the
one that disappears.

**The frame's radius is computed at runtime; do not copy the literal.** 47.319px outer and
32.254px inner are what a script wrote at 1440 on a 1280px-wide panel. The relationship is
the specification — inner = outer − 15px inset — and `--r-frame: 48px` with
`--r-frame-inner: calc(48px - 15px)` reproduces it within a pixel at any width.

**The third face belongs to the client, and so do two of the colours.** Lato on 36 text
nodes, `#1264a3` on `#e8f5fa` for a mention at 5.59:1, `#007c58` for an approval, `#cecece`
for a decline rule. They ship under `--quoted-*` so a status dot cannot reach them by
accident. A page that lifts them into its own palette has adopted somebody else's design
system one token at a time.

**A card does not invert with the field, and painting its text in `--ink` is the trap.**
`--surface` is white on both blocks — measured, because a chat-client card inside an
inverted section is still a white card — while `--ink` inverts to `#ffffff` on the dusk
surface. A card whose heading takes `--ink` therefore renders white on white inside a
dusk section — `#ffffff` on `#ffffff` is 1.00:1 — and no gate can see it: both tokens are
legal, both clear their own field, and the pairing only exists at render time. That is what `--on-surface` and
`--on-surface-soft` are for, and it is why they do not invert. Found by reading this
pack's own kit on a dusk section, which is the second defect that render caught after the
secondary control painting white on white — the same mechanism, one component along.

**The focus ring is declared literal-first, and the order is the guard.** A custom
property accepts almost any token sequence, so `--focus-ring: color-mix(…)` parses even
where `color-mix()` is unsupported, wins the cascade, and fails only at substitution — by
which point the literal is gone and `var(--focus-ring)` resolves to `unset`. An invisible
focus ring is the one degradation this pack may not ship, so the literal sits in `:root`
and the derived form sits in an `@supports (color: color-mix(in srgb, red, red))` block at
the end of the layer. `showroom` is the pack that learned this first; this one copies its
mechanism rather than its syntax, because the derived form here is a mix rather than a
relative colour.
