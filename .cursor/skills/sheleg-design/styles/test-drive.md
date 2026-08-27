# Style pack — Test-drive

Origin: <https://datafa.st> (2026), the front page of a revenue-analytics product. The
site is Next.js with Tailwind and DaisyUI, so the authored layer is the DaisyUI oklch
theme block inside one 382,404-byte stylesheet plus four Next-font CSS files, and the
vendor layer is the utility corpus around it. Every value below was **verified against
the render** on 2026-08-27 through CDP at 1440×900 — a census of `background-color`
and `background-image` over every element, weighted by area, on a 14,329px page — with
the dark twin read under `[data-theme=dark]`, narrow behaviour at an emulated
390×844×2, and the product's own dashboard read separately at `/demo`, because the
landing embeds the live product in an iframe. Control states were read out of the
reference's own authored classes (`.btn-primary`, `.btn-simple`) rather than inferred
from screenshots. Ratios were computed by importing this repository's own palette gate.

Warm paper, white cards, one coral that acts and a declared teal that never paints; a
single working face doing display, body and data, with a second, handwritten face that
only ever annotates; controls lit by a four-layer shadow in their own hue; the page's
machine surfaces — terminal, CLI, agent panel — quarantined in a small dark ladder
that ignores the theme.

The identity in one sentence: **the visitor is handed the keys** — the page's set
piece is the live product running inside a drawn browser frame, and a founder's hand
(a script face, a yellow marker, a drawn arrow) points at what to notice while you
drive it.

Contract: widened — all thirteen headings.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Test-drive for **products that are their own best salesman once someone is
inside**: analytics and dashboards sold self-serve, developer tools with a visible
console, indie and solo-founder SaaS, any product page whose honest pitch is *stop
reading and try it*. The proof this pack organizes a page around is **operation**: an
embedded live instance or a self-narrating demo loop as the centerpiece, metric tiles
with real numbers, and a human hand annotating the tour — the register of a
dealership, not a gallery.

Standalone: it does **not** ride the SHELEG cinematic motion layer. The budget is
looping self-demonstrations (13–18s narrative loops, `steps()` typewriters, a 0.9s
caret), an ambient background drift (8–25s), and 0.2s control transitions — and none
of it is scroll-driven: `animation-timeline` appears zero times in 382,404 bytes.
`MOTION_INTENSITY` above **5** has nothing legal to buy here — and what the dial does
buy is spent inside the demos, never on the page around them.

**Not for:** enterprise procurement pages, where a handwritten annotation reads as a
liability rather than a voice — that register is [`showroom`](./showroom.md) or
`tenor`. Not for regulated, clinical or public-sector surfaces: a yellow marker over a
compliance claim is a joke the reader did not ask for. Not for dense operator chrome —
the elevation model is one card ring and one lit control, and a fourth nested panel
has nothing to sit on; that is `workbench`'s half.

### The fork against [`datasheet`](./datasheet.md), which is the live-instrument collision

Both packs put a working instrument in the first screen, and a router reading "the
page proves the product live" cannot separate them. The separation is **whose data the
instrument reads**. `datasheet`'s specimen is *you* — it returns the visitor's own id,
city and IP, and the page around it is a cold spec sheet: mono data, hairlines at
radius 0, a ten-ramp palette held back. Test-drive's specimen is *the product's own
workspace* — a sample dashboard you are free to drive — and the page around it is a
founder talking: warm paper, a handwritten margin, one coral. If the instrument's
output is a verdict about the reader, go there; if it is the product's day-to-day
screen handed over, stay here.

### The fork against [`showroom`](./showroom.md), which is the centerpiece collision

Both arrange the whole page around one product surface at real size. The separation is
**whether it runs**. `showroom` frames a still: one screenshot as a lit exhibit under a
seven-layer neutral shadow, museum posture, three type families. Test-drive hands over
a running one: an iframe or a self-narrating loop with a caret still blinking, framed
in browser chrome with traffic-light dots, annotated by hand. A specimen you look at
is `showroom`; a machine you are invited to operate is this pack — and the give-away
is motion inside the frame.

### The fork against [`scoreboard`](./scoreboard.md), which is the visual collision

Both live on warm paper with one orange-red accent and big counted figures, and a
thumbnail of either could pass for the other. The separation is **what the number is
doing**. `scoreboard`'s subject is an accumulating total — the board exists so one
figure can grow in public, and its accent may never carry a word. Test-drive's numbers
are a dashboard's vital signs (seven tiles, 26.4px, each with its delta arrow), the
accent both fills the one CTA and lights it, and the page's subject is the instrument
those numbers live in. A page built to watch one number rise is `scoreboard`; a page
built to hand over the machine that produces the numbers is this one.

## Palette

Copy [`tokens/test-drive.css`](./tokens/test-drive.css) verbatim. Every colour there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio. The geometry
ramps carry a provenance note per band.

| Role | Token | Value | Notes |
|---|---|---|---|
| Field | `--bg` | `#fbfaf9` | MEASURED — the warm off-white the page and nav share |
| Card | `--surface` | `#ffffff` | MEASURED — every card and the demo frame's interior |
| Panel step | `--surface-2` | `#fcfbfa` | MEASURED — the base-200 step |
| Ink | `--ink` | `#262626` | 14.52:1 on `--bg` |
| Mute | `--ink-mute` | `#595451` | 7.16:1 on `--bg` — secondary text AND the annotation ink |
| Brand coral | `--accent` | `#e16540` | non-text and large-only — see below |
| Action | `--action` | `#c04a28` | DERIVED — 4.74:1 on `--bg`, and the only coral that writes |
| Traffic | `--chart-traffic` | `#8dcdff` | non-text — the visitors series |
| Money | `--chart-money` | `#e78468` | non-text — the revenue series |
| Marker | `--marker` | `rgba(254,249,195,.8)` | the highlighter — its arithmetic is in the paragraph below |

**The marker stays legible, measured:** ink `#262626` on the composited stripe `#fefacf` is 14.26:1.

**The coral is two tokens, and the split is the pack's central correction.** The
reference paints its CTA fill, its links, its caret and its money bars in one
`#e16540` — and its CTA label measures `#ffffff` on `#e16540` at 3.42:1, while
its links measure `#e16540` on `#fbfaf9` at 3.28:1, both under AA. So the brand hue
stays `--accent` for what it does well — lighting controls, filling bars, blinking
carets, and carrying text only at display sizes, where that same 3.42:1 clears the
large-text floor — while `--action` is the same hue pulled down until both jobs
clear: `#ffffff` on `#c04a28` is 4.94:1, and `#c04a28` on the field `#fbfaf9` is 4.74:1.
On the light theme a body-size word in coral is always `--action` — and the dark twin
swaps the jobs, because the arithmetic inverts there: `#c04a28` on `#1f1f1f` is 3.34:1
while `#e16540` on `#1f1f1f` is 4.82:1, so a coral word on the dark field takes
`--accent`, and a link on a dark card keeps `--ink` with the accent underline. The
token layer states the swap at the declaration.

**The declared accent is not the acting accent.** The reference's theme block declares
a teal at full strength and the render paints it nowhere — a dead token wearing the
costume of a brand. The teal ships nowhere in this pack. Read the render.

**"Revenue-first" is encoded in colour.** The chart duo is fixed: money draws in the
brand's own coral family (`#e78468` over `rgba(255,199,182,.58)`), traffic in a blue
that may never carry a word (`#8dcdff` over `rgba(218,239,255,.58)`, and `#8dcdff` is
1.71:1 on white `#ffffff`). Swapping the two hues inverts the page's one argument. A chart label
takes `--ink-mute` at 7.47:1 on the card `#ffffff`, which is what the reference's own
dashboard does.

**Status is never by colour alone.** The reference ships DaisyUI's status hues and
paints text with none of them — its warning `#ffbe00` is 1.66:1 on `#ffffff`, and
its error `#ff5861` is 3.08:1 on `#ffffff`. Each pack status is the same hue pulled down to AA
as a word on both light fields; the dark twin raises them instead. The tight pairs
under colour-vision deficiency are stated at the declaration, and every state carries
a word or a glyph beside its colour — the reference's own dashboard writes the
percentage next to every delta arrow.

## Type

One working face and one hand — the second is the voice, not a display face.

| Role | Family | Size / line | Weight | Tracking |
|---|---|---|---|---|
| Display | DM Sans | 60px/60px → 36px/40px | 800 | −0.025em |
| Section head | DM Sans | 48px/48px → 30px/36px | 800 | −0.025em |
| Card head | DM Sans | 36px/40px | 800 | −0.025em |
| Metric figure | DM Sans | 26.4px | 700 | 0 |
| Body | DM Sans | 16px/24px | 400 | 0 |
| Control label | DM Sans | 16px | 500 | 0 |
| Metric label | DM Sans | 14px | 400 | 0 |
| Annotation | Fuzzy Bubbles | 14–16px | 400 | 0 |

- **DM Sans is display, body and data alike** — a variable face (100–1000 shipped),
  spent at exactly four weights: 800 for anything that announces, 700 for a counted
  figure, 500 for a control label, 400 for reading. A fifth weight is somebody else's
  page.
- **The hand annotates; it never announces.** Fuzzy Bubbles appears at 14–16px in
  `--ink-mute` or `--action`, on marginal notes ("Interactive demo", "No-code",
  "2 months free") — always beside or above the thing it points at, never as a
  heading, never in a control. The reference ships it with a metric-matched Arial
  fallback (`size-adjust: 116.87%`), which is the consumer's `@font-face` business,
  by this library's own rule.
- **Tracking is display-only and single-valued**: −0.025em at 60, 48 and 36px
  (−1.5px, −1.2px, −0.9px). Body and controls are untracked.
- **The display's line-height is 1** — 60px on 60px — so the face's own leading is
  the whole optical margin. `text-box-trim` would close the gap the stated metric
  leaves; Firefox still lacks it, so the pack states the metric and trims nothing.
- **A measure in `ch`, stated as a decision:** the reference holds its lede in a
  659px column with `max-width` on nothing; `--measure-body: 72ch` against DM Sans
  at 16px is the measure that column implies.

## Texture & surface

**Elevation has two vocabularies, and which one an object takes depends on whether a
hand touches it.** A *card* is white on warm paper with `--ring-card` — a 1px black
ring at 6% plus a 1–2px soft drop, no border property at all. A *control* is lit:
the four-layer recipe (contact shadow, 1px ring, 8px/16px/−8px glow, 1px inner bottom
bevel) in the control's own hue — coral under the primary (`--lit-action`), neutral
grey under the quiet one (`--lit-quiet`). The one big drop on the page is
`--shadow-frame` under the demo frame. There is no shadow ramp; there are these three
jobs.

**Radii: the ramp defines the token set.** Proportional from a 1rem root — ×0.5 for
everything the hand touches (`--r-control`, 8px: buttons, inputs, tabs), ×1 for the
card (`--r-card`, 16px), ×1.3 for the frame (`--r-frame`, 20.8px). The badge pill
(`--r-badge`, 1.9rem) is a literal beside the ramp because the reference declares it
as one. **Subtraction adjusts a nested instance:** the demo frame's window is
concentric — with the frame's 5px chrome inset, inner = outer − inset = 20.8px − 5px
= 15.8px, which the reference rounds to the card's own 16px. Never the same radius on
both boxes.

**Hairlines are alphas of the ink** — 5% under the nav and the quiet control's
border, 10% around the input. The 5% line composites to `#f0efee`, which is 1.10:1
on the field `#fbfaf9`; the 10% line composites to `#e9e9e9`, which is 1.21:1 on
white `#ffffff` — far under the mark floor, which is correct for a hairline and is
why no state change ever rides on one.

**The machine ladder is the only texture that ignores the theme.** Terminal, CLI and
agent surfaces sit at `--machine-chrome` `#101010`, `--machine` `#171717`,
`--machine-2` `#202020` — dark on the light page and dark on the dark one, namespaced
so a card cannot reach them by accident.

## Components

Read off the reference's authored classes and the `/demo` dashboard; states are the
reference's own.

- **Buttons.** Two heights (`--control-h` 48px for the page's offers, `--control-h-sm`
  32px in the nav), both at `--r-control` with `--control-px` of side padding,
  16px/500 label. *Primary*: `--action` fill, `--on-action` label at 4.94:1 on
  `#c04a28`, `--lit-action` shadow. Hover mixes 10% black into its own fill
  (`color-mix(in oklab, var(--action) 90%, #000)`) — the reference's own rule. Press
  scales to `--press-scale` (0.95) over `--dur-press`. Disabled: 40% opacity, no lit
  shadow. *Quiet*: `--surface` fill, `--ink` label, a 0.5px hairline border and
  `--lit-quiet`; hover brightens the glow to `--lit-quiet-hover` and raises the border
  to `--hairline-strong` — the control itself does not move. *Ghost* (nav links):
  transparent, `--ink`, hover fills with the ink at 5%.
- **Cards / containers.** `--surface` at `--r-card` with `--ring-card`; internal
  padding 24–32px. A card head is 36px/800; card body 16px/400 in `--ink` with
  supporting copy in `--ink-mute`. When a card quotes the machine, the quoted panel
  sits at `--machine` with `--r-card` and does not flip with the theme. Plain
  negative space divides sections; hairlines divide rows inside a card; a card is
  never nested in a card.
- **Inputs / forms.** `--control-h`, `--surface` fill, 1px border in
  `--hairline-strong`, `--r-control`, 16px text with the placeholder in `--ink-mute`.
  A joined input+button group shares one 8px outer radius (the seam edges are 0).
  Focus: the pack's one focus contract below. Invalid: the border takes `--danger`
  **and** a message in it — never the colour alone.
- **Navigation.** A `--nav-h` (65px) bar in the field's own `--bg` — not white, not
  frosted — with a 1px `--hairline` rule under it, static at every scroll offset,
  measured: no shadow, no shrink, no `backdrop-filter`. Log-in is the quiet lit
  control at `--control-h-sm`. Below 48rem the link row gives way to a toggle at the
  `--tap-min` floor — the measured pair is 32px tall, which is the pack's recorded
  correction, not its rule.
- **Loaders.** The machine has one: three `--accent` dots at 1s `ease-in-out`
  (`df-cli-thinking`) or the masked ring spinner (2s rotate, 1.5s dash). The card
  layer ships **none, and that is measured**: the vendor layer defines a `skeleton`
  class that appears exactly once in 382,404 bytes — its own definition — and no
  shimmer paints anywhere. The pack decision for a card that must wait: a
  `--surface-2` block at the shape's own radius, no shimmer, because the fastest
  thing on this page outside the demos is 0.2s.
- **Empty states.** The measured dashboard renders a zero as a figure, not as an
  absence — "Online **0**" ships as a tile like any other. The pack decision for a
  screen with no data at all: a `--surface` card at `--r-card` holding one 16px/500
  line in `--ink`, one sentence in `--ink-mute`, and one quiet control that starts
  the demo — this pack always has a demo to offer, which is its own empty-state
  answer.

## Hero

A marketing opening, and its argument is a working instrument below the words.

- One centered copy column — measured 659px — carrying, in order: the display at
  `--t-display` (60px/60px, 800, −1.5px), two lines of 16px lede in `--ink`, then a
  joined input+button pair (48px tall: the URL field and the one coral CTA), a
  reassurance line, an avatar row with a counted social proof ("Loved by 23,237
  users" — the number in 700).
- **The headline's ceiling is two lines at 60px, and what holds it is the 659px
  column plus a word budget**: the reference's own headline is two words
  ("Revenue-first analytics"), and the column wraps a third-word headline to two
  lines before anything breaks. Past two lines the hero is broken, not long.
- Below the column, full-content-width (1280px): **the framed live demo** — browser
  chrome at `--r-frame` in `--machine-chrome` with three traffic-light dots and a
  URL bar, interior at `--surface`, `--shadow-frame` under it — with the handwritten
  annotation and its drawn arrow anchored to the frame's top-right corner
  ("Interactive demo", 14px Fuzzy Bubbles in `--ink-mute`).
- What it must not carry: a second CTA hue, a video lightbox in place of the live
  frame, a logo wall (that is a later section's), or an annotation set in the
  working face — the hand annotates, the sans announces.

## Responsive

Measured at 1440, and at an emulated 390×844×2; the reference's one display
breakpoint is Tailwind's `md` (48rem).

- **Type steps, it does not flow**: the display is 36px/40px below 48rem and
  60px/60px from it — one step, nothing between, and the reference ships no `clamp()`
  on any type size. The section head steps 30px/36px → 48px/48px the same way.
  Tracking stays −0.025em on both sides of the step.
- **The nav does not shrink** — 65px at 1440 and at 390 — the link row is replaced by
  a toggle below 48rem (see Components for the tap-floor correction).
- **The hero pair stays 48px** and goes full-column; the demo frame keeps
  `--r-frame` and its 5px chrome inset at every width — the concentric relationship
  is the object's identity.
- **Container queries.** Sorted by kind, because only the first has a container
  answer. The reference itself ships zero `@container` blocks, so this table is
  mostly a statement about what belongs to the page:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | The metric-tile row stepping 7 → 4 → 2 columns | CONTAINER | `container-type: inline-size` on the tile row, `@container` on the tracks |
  | A feature-card grid stepping 3 → 2 → 1 | CONTAINER | container on the grid, `@container` on the tracks |
  | Display 36 → 60px | PAGE | the headline answers to the viewport |
  | The nav's toggle swap at 48rem | PAGE | the nav is the page's |
  | Section rhythm 112 → 64px | PAGE | the page owns its rhythm |
  | The demo frame's own radius and chrome inset | SELF | **no container answer exists** — the frame establishes the container, a container cannot query itself, and neither value changes anyway |

- **No horizontal overflow**: `documentElement.scrollWidth` equals the viewport at
  1440 and at 390, measured with the census running.
- **Viewport:** `100dvh` for any full-height surface, never `100vh`.

## Motion tokens

| Token | Value | Spends on |
|---|---|---|
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | every control transition — MEASURED |
| `--ease-pop` | `cubic-bezier(0.16, 1, 0.3, 1)` | the pop-in spring — MEASURED |
| `--dur-fast` | 0.2s | colour, border, opacity — MEASURED |
| `--dur-press` | 0.15s | DERIVED — the reference's 0.25s pop is over the press band |
| `--dur-pop` | 0.65s | a small object arriving — MEASURED |
| `--press-scale` | 0.95 | the press — the reference's own `--btn-focus-scale` |
| `--dur-caret` | 0.9s | the CLI caret and the CLI/agent spinners — MEASURED; the masked ring spinner keeps its own 2s/1.5s |
| `--dur-demo` | 14s | the demo loop's clock (the chat demo runs 18s) — MEASURED |
| `--dur-ambient` | 18s | the background drift, middle of an 8–25s family — MEASURED |

Three clocks and a hierarchy: 0.2s for anything a pointer caused, 0.65s for a small
object arriving, and double-digit seconds for the demos narrating themselves. The
demos are the only place the page is allowed to be busy, and they earn it by being
the product.

**Reduced motion is behavioural here, not just zeroed clocks.** The typewriters and
demo steps end on a different frame than they start, so a zeroed loop teleports to
its hidden state. Under `prefers-reduced-motion` the token layer collapses every
duration and the press scale, and the demo **shows its final frame** — the full
command, the finished answer, the caret solid — as a still; the ambient layer stops
at its resting offset. The reference itself ships two reduced-motion rules against 53
keyframes, which is its recorded failure, not its contract.

## Signature motifs

- **The lit control** — one four-layer shadow recipe (contact, 1px ring, 8/16/−8
  glow, 1px inner bottom bevel) hue-matched to its control: coral under the primary,
  neutral under the quiet one, re-mixed darker on the dark theme. Elevation for the
  hand, everywhere.
- **The founder's hand** — Fuzzy Bubbles marginalia in `--ink-mute` or `--action`, a
  square-edged yellow `--marker` stripe over the praise inside testimonials, and a
  thin drawn arrow from the note to the thing. Three devices, one voice, always
  marginal.
- **The machine quarantine** — terminal, CLI and agent panels in their own
  #101010–#202020 ladder that ignores the theme, with the coral caret and thinking
  dots as the only colour inside.
- **The chart duo** — money in coral, traffic in a wordless blue, deltas as arrow +
  percentage, never colour alone.
- **Counted proof** — "23,237 users", seven metric tiles, "3 steps": numbers set in
  700 inside otherwise quiet sentences.

## Signature element

**The framed live demo.** Browser chrome at `--r-frame` — `--machine-chrome` title
bar, three traffic-light dots, a real URL in the address bar — around the product
itself running at `--surface`, with `--shadow-frame` under it and one handwritten
annotation pointing at it from outside the frame.

It carries the pack's identity because it is the register made visible: the page does
not describe the product, it hands the product over, and the drawn chrome is the seam
between the founder's warm page and the working machine. Build it once: on the
reference it is an iframe of the live app; where an embed is impossible, a
self-narrating demo loop (the `--dur-demo` clock, a `steps()` typewriter, the caret)
is the same element one step down. A static screenshot inside the chrome is the one
thing it must never hold — that is `showroom`'s exhibit, and the whole point of this
frame is that the engine is on.

## Micro-interactions

- **Primary press:** scale to `--press-scale` over `--dur-press`, label never moves
  alone. Hover: the fill mixes 10% black into itself; the lit shadow stays.
- **Quiet hover:** on the light theme the glow brightens (`--lit-quiet` →
  `--lit-quiet-hover`) and the border rises to `--hairline-hover`; on the dark theme
  the two shadow tokens are measured identical and the border alone carries the hover
  — the control itself never moves on either.
- **Focus-visible:** a `--focus-w` (2px) solid outline in `--focus-color`, offset
  `--focus-offset` — measured. `#e16540` on `#fbfaf9` is 3.28:1. `#e16540` on `#1f1f1f` is 4.82:1.
  Over the mark floor on both fields; one mechanism, no ring stack.
- **The caret blinks at `--dur-caret` in the machine only.** A blinking element on
  the card layer is a defect.
- **Card hover: nothing.** Cards are furniture; the demo inside them is the moving
  part. `@media (hover: hover)` gates the two hovers above.

## Bans

- **No second acting hue.** The teal the reference declares and never paints stays
  unpainted. One coral, in two tokens.
- **No body-size words in `--accent` on the light theme** — there that is
  `--action`'s job. `#ffffff` on `#e16540` is 3.42:1; `#ffffff` on `#c04a28` is 4.94:1.
  Those two numbers are why both exist — and on the dark field the ban flips to
  `--action`, per the swap the Palette states.
- **No lit shadow under a card.** The recipe is the hand's; a card takes
  `--ring-card` and nothing else. A `shadow-md` utility here is a foreign object.
- **No handwriting in headings or controls.** The hand annotates from the margin;
  the moment it announces, the page is a child's menu.
- **No marker over interface text** — the highlighter quotes praise; it never
  highlights a label, a metric or an error.
- **No machine tokens on cards** — `--machine-*` is quoted, not themed.
- **No frozen screenshot inside the browser frame.** The frame's contract is a
  running interior.
- **No traffic blue carrying a word** — `#8dcdff` is 1.71:1 on white `#ffffff`.
- **No scroll clock, no parallax, no `animation-timeline`** — zero occurrences,
  measured.
- **No frosted nav, no scroll-shrink** — the bar is the field's own colour with one
  hairline, static at every offset.
- **No shimmer on a skeleton.** The card layer's fastest clock is 0.2s.
- **No `100vh`.**
- **No `ease-in`.**

## Gotchas

**The declared accent is dead, and the render is the only witness.** The theme block
declares a full-strength teal as its accent; the area-weighted census over every
element's `background-color` and `background-image` finds it painting nothing on the
page, while the census's largest authored colour is the coral. A pack extracted from
the stylesheet alone would have shipped a teal brand. Read the render.

**Four corrections travel with this pack, each with its number at the declaration.**

1. *The CTA label misses AA.* The reference's CTA label is 16px/500, and `#ffffff` on `#e16540` is 3.42:1.
   The remedy is `--action`: `#ffffff` on `#c04a28` is 4.94:1. The brand
   coral keeps every non-text job and display-size text, where the same 3.42:1
   clears the large floor.
2. *The links miss AA on the field.* `#e16540` on `#fbfaf9` is 3.28:1 — the measured
   link colour of the whole page. A link here is `--action`, because `#c04a28` on `#fbfaf9` is 4.74:1.
3. *The status set cannot write.* The reference's warning measures `#ffbe00` on `#ffffff` at 1.66:1,
   and its error measures `#ff5861` on `#ffffff` at 3.08:1; each pack
   status is the hue held and darkened to AA on both light fields, raised instead
   on the dark twin.
4. *The press is over the band.* The reference's `button-pop` runs 0.25s where the
   doctrine's press band ends at 160ms; `--dur-press` ships at 0.15s and keeps the
   reference's own 0.95 scale.

**53 keyframes, two reduced-motion rules.** The reference's demos, typewriters,
spinners and six ambient drifts run regardless of the user's motion setting; only two
rules in 382,404 bytes mention `prefers-reduced-motion`. The pack's reduce contract
(final frame as a still, ambient stopped at rest) is stated in Motion tokens and
ships in the token layer — zeroing clocks alone would teleport the `steps()` loops to
their hidden state, because their last keyframe differs from their first.

**The nav measures quieter than it looks.** No shadow, no `backdrop-filter`, no
scroll listener — a static 65px bar in the field's own colour with a 5%-ink rule. The
frosted sticky bar every kit reaches for is not in this reference; adding one is the
fastest way to lose the pack.

**The demo frame's 20.8px is a ramp step, not a magic number** — 1.3 × the 1rem
root, measured as the reference's own `1.3rem` class. Its interior rounds to the
card's 16px because 20.8 − 5 = 15.8 rounds up; state the subtraction when nesting
anything else inside the chrome.

**The dark twin re-mixes the lit recipe; it does not delete it.** Measured off
`.btn-primary:is([data-theme=dark] *)`: the bevel deepens to rust
`rgba(114,36,13,.64)`, the ring drops to 6%, the glow to 32%. A dark theme that keeps
the light theme's shadow literals paints halos; one that drops the shadow entirely
un-lights every control. Both twins ship in the token layer.
