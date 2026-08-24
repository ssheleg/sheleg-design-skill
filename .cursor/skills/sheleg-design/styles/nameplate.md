# Style pack — Nameplate

Origin: <https://www.brandpush.co> (2026), the marketing site of a press-release
distribution product — it places your story on named news outlets and gives you the
badge that says so. Every value below was read on 2026-08-24 by enumerating its
sitemap (20 URLs, 12 distinct pages), fetching every page `robots.txt` permits, and
reading the **11 stylesheets the site itself authors** under `/assets/css/` —
500,051 bytes, 20,240 lines, 136 custom properties — then off **computed styles on
the live page** through CDP at 1440×900 (1,251 visible of 5,694 elements), 768×1168
and a device-emulated 390×844. Vendor layers were excluded from every count: the
site also loads Bootstrap 4.6.2, a purchased *ave* theme, a *frest* admin theme and
three Font Awesome versions, and counting those reads Bootstrap's defaults as this
brand's decisions. Ratios were computed by importing this repository's own palette
gate. `robots.txt` `Disallow`s `/r`, so the report
surface was read from the showcase the home page embeds rather than from the report
pages themselves.

A cool near-white slab under the fold-height hero, a page that is **square almost
everywhere**, and one shape that is not: a white pill with a 1px border and a 4%
shadow, carrying the name of somebody else's publication. One family — Poppins —
with the body set at **weight 500**, a display face at 700 pulled in 2%, and two
uppercase registers pushed out by very different amounts. Elevation is a hairline
except once per screen, where a framed panel takes a 70px-blur shadow nothing else
is allowed to spend.

The identity in one sentence: **the proof is a borrowed name, and it is issued rather
than owned.** The page does not claim the authority — it shows you the plate with
somebody else's name on it, and sells you the plate.

Contract: widened — all thirteen headings.

Themes: light only — the reference paints no dark band anywhere, and this pack does not invent one.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Nameplate for **pages whose argument is that named third parties will vouch
for you** — press and media placement, PR distribution, trust marks and badges,
certification and accreditation, review aggregation and score widgets, directory
and "as featured in" surfaces. It is the pack for a page that must show thirty
borrowed names without any of them reading as a logo-soup filler band, because the
name is set as *type in a bordered plate* rather than dropped in as art.

**Standalone**, and it pins its own ceiling: **`MOTION_INTENSITY` above 4 has nothing
legal to buy here.** The reference's whole measured budget is an entrance reveal, a
2px hover lift with a shadow that grows in the same 200ms, and a 140ms press —
1,057 of the 1,251 visible elements compute `transition-duration: 0s`, and
`animation-timeline` appears zero times in 20,240 lines. Same ceiling as
[`roster`](./roster.md) and for the same reason.

**Not for:** anything sold on the reader's own competence — dense operator tooling,
developer products whose buyer reads code, consoles. A page built out of borrowed
names is a page that argues from outside authority, and pointing that argument at
someone who wants to evaluate the thing themselves inverts it.

### The line against `roster`, because they share one sentence and nothing else

[`roster`](./roster.md) is the other pack whose proof is a name, and a brief can
fire both. The measured systems are not close, and the deciding axis is **what the
round shape costs**:

| | `roster` | Nameplate |
|---|---|---|
| Zero radius | not dominant — 8/12/16/24px carry the page | **87%** of the page: 1,091 of 1,251 visible elements |
| The pill | the page's *most frequent* shape (102), on labels, chips and heads | 52 elements, and it is **the proof plate itself** |
| Both CTAs | 12px controls, deliberately **not** pills | pills, uppercase, tracked |
| Body | Plus Jakarta Sans at **300** | Poppins at **500** |
| Families | three | **one** |
| Field | white under a faint square grid | a cool grey slab, **no texture at all** |
| Accent | an orange that may never carry a word | a coral ramp that fills the primary action |

So: `roster` when the proof is *who already uses us* and the page is a grid of
client logos. Nameplate when the proof is *who will carry you*, the page is mostly
square, and the pill is rare enough to mean something. If the brief is a logo wall
on a textured white field, it is `roster`; if it is a wall of publication names in
bordered plates, it is this one.

## Palette

Copy [`tokens/nameplate.css`](./tokens/nameplate.css) verbatim. Every value there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio.

| Role | Token | Value | Note |
|---|---|---|---|
| Page | `--bg` | `#ffffff` | MEASURED — 108 computed fills |
| Slab | `--field` | `#f5f7fa` | MEASURED — the hero stands on it, later acts return to it |
| Well | `--surface-2` | `#eceff3` | MEASURED — 7 |
| Ink | `--ink` | `#1d1d1d` | 16.86:1 on `--bg`, 15.71:1 on `--field` |
| Mid | `--ink-mid` | `#374151` | MEASURED — 25 nodes, 10.31:1 on `--bg` |
| Body | `--ink-body` | `#707070` | DERIVED — 4.95:1 on `--bg`, 4.61:1 on `--field` |
| Action | `--action-from/to` | `#d44500` → `#de2e53` | DERIVED — white clears AA along the whole ramp |
| Link | `--link` | `#0070d4` | DERIVED — 4.92:1 on `--bg`, 4.58:1 on `--field` |
| Ring | `--accent` | `#0587ed` | MEASURED, non-text — 3.69:1 on `--bg`, and it must stay **opaque** |
| Plate edge | `--line` | `#e5e7eb` | MEASURED — the pill's border |
| Rule | `--line-soft` | `#ededed` | MEASURED — 37, the page's dominant seam |

**The dominant text colour is not the ink.** The mid grey carries 121 computed text
nodes against the near-black's 37 — this page is mostly grey type on white, which is
why two of the five corrections are about greys nobody would look at twice.

**Two fields, and every text colour is checked against both.** A value that clears AA
on white and fails on `--field` is broken, because `--field` is the hero. The
reference's own body grey is exactly that case: 4.74:1 on white, 4.42:1 on the slab.

**The accent may not be a state.** `--accent` is the blue; `--info` is therefore the
cyan `#00738b`, not a blue. The two blues came out 7.5 OKLab units apart, and one
colour cannot be both a link and a status.

**Status is never carried by colour alone** — every state takes a glyph or a label
beside its colour. The four were searched, not picked: with a coral action in the
palette a conventional red `--danger` is 2.93 units from it and vanishes under all
three dichromacies, so danger is held at the reference's red hue and taken deep to
`#900004`.

## Type

One family. Poppins paints 262 of the 264 computed text nodes; the Hanken Grotesk
that survives in one declaration paints two, and treating it as a second family is
reading the stylesheet instead of the page.

| Role | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|
| Hero | 45px → 30px at ≤768 | 700 | 1.15 | −0.02em |
| Section | 40.32px | 700 | 1.10 | −0.02em |
| Lede | 20px | 500 | 1.35 | −0.02em |
| Body | **17px** | **500** | 1.6 | 0 |
| Plate name | 15px | 500 | 18px | 0 |
| Control label | 14px | 700 | — | **+0.06em**, uppercase |
| Micro-link | 12px | 700 | — | **+0.175em**, uppercase |

**The body is medium, and this is the pack's quietest decision.** Weight 500 carries
172 computed nodes at 1440, 459 at 768 and 182 at 390 — it is the dominant weight at
every width. Setting body copy at 400 here does not read as lighter, it reads as a
different product: the page's evenness comes from display and body being only two
steps apart.

**The tracking pair is the signature, and the reference's own token describes half of
it.** The display pulls in 2%; the two uppercase registers push out by 0.06em and
0.175em — a threefold difference between a button label and a micro-link. The site
declares `--tracking-caps: 0.06em` and the 12px micro-links compute 0.175em, so the
declared token is true of controls only. Use both; collapsing them to one value is
how the eyebrows stop reading as eyebrows.

**17px, not 16.** It is the most frequent size on the page (78 nodes at 1440, 352 at
768) and it is a real choice: at 500 weight, 16px reads cramped against a 45px
display.

## Texture & surface

There is no texture. No grid, no noise, no pattern, no gradient mesh — the page is
separated by **returning to white**, by a 1px rule, and by a drawn wave.

**Two fields alternate, and white is the resting state.** The hero stands on
`--field`; acts return to white; a later act may take `--field` again. A card on the
slab is white — this pack never separates by going darker, which is why
`--surface-2` is a well (an inset) rather than a card.

**The act separator is drawn, not ruled.** Eleven acts on the home page end in an
SVG wave: `--wave-h` 150px, overspilling to `--wave-w` (`calc(150% + 1.3px)`) so the
curve reads as an arc rather than a bulge, filled in the colour of the act **below**,
and hidden under 768px where the acts butt directly. The overspill is the whole
trick: a wave at exactly 100% width looks like a bubble.

**Elevation is a hairline, with one exception per screen.** `--shadow-pill` is 4% at
2px blur. `--shadow-frame` — 25px offset, 70px blur, 7% — belongs to the framed media
panel and to nothing else (14 elements across a 19,451px page). Spending it on a card
or a control is what makes this pack look like a template.

## Components

The pack states these because it is on the widened contract; the React reference
kit `nameplate` renders them — fetch it with `npx sheleg-design-skill --kit nameplate`.

**Name plate** — the pack's reason to exist. `--surface` fill, `1px solid --line`,
`--r-pill`, `--shadow-pill`, name in `--ink` at 15px/500, padding `12.8px 19.2px`,
height `--pill-h` (50px). Hover: `translateY(---lift)` **and** `--shadow-pill-hover`
in the same `--dur-base`, border to `--ink-faint`. Focus-visible: `--focus-w` solid
`--focus-color` at `--focus-offset`. It never takes a fill, never takes a logo, and
never carries more than one name.

**Primary action** — `--action` ramp, `--on-action` label at 14px/700 uppercase
`--track-caps-control`, `--r-pill`, height `--control-h` (48px), no border. Hover:
`--shadow-action-hover` plus the lift. Active: `--action-pressed`, no lift. Disabled:
`--surface-2` fill, `--ink-faint` label, no shadow, `cursor: not-allowed`.

**Secondary action** — `--surface` fill, `1px solid --line-soft`, `--r-pill`, label
in `--ink` at 14px/700 uppercase. Hover: border to `--ink-faint`, lift, no fill
change. It is a plate that happens to be a button, and it must stay visually below
the primary at every state.

**Card** — `--surface`, `--r-md`, **no border and no shadow** when it sits on
`--field`; `1px solid --line-soft` when it sits on white. The card's separation comes
from the field it is on, which is why the same card is drawn two ways.

**Framed panel** — `--r-md`, `--shadow-frame`, no border. One per screen.

**Input** — `--surface`, `1px solid --line`, `--r-xs`, height `--tap-min` floor, 17px
at 400. Focus: border to `--accent` plus the ring. Invalid: border `--danger` **and**
a message; never the border alone.

**Eyebrow** — 12px/700 uppercase at `--track-caps-micro`, in `--ink-body`. Above a
section head, never inside a control.

Every interactive element takes `--tap-min` (44px) as a height floor. This is a
correction, not a measurement: at 390 the reference has 87 of 137 visible
interactive elements under 44px.

**Navigation** — the bar is `position: absolute` over the hero slab at `--nav-h`
(89px): transparent, no border, no shadow, **not sticky**. Links are 17px at
`--weight-body` in `--ink`; the trailing pair (sign-in, then the primary) sits right;
the whole bar collapses to a wordmark plus a sheet trigger below 991px. It does not
gain a fill on scroll — a bar that materialises here reads as a second act starting.

**Empty states** — a `--r-md` panel on `--field`, no border and no shadow: an
`Eyebrow` in `--ink-soft`, one sentence in `--ink-body` at `--t-body`, at most one
secondary action. **A borrowed name is never invented to fill the space** — an empty
plate band shows a single plate in the pending form (dashed border, `--ink-faint`, no
shadow) and says what will fill it. Faking a publication name into an empty state is
the one failure this pack cannot survive.

**Loaders** — a skeleton in the shape of what is coming: a `--r-pill` block at
`--pill-h` for a plate, a `--r-md` block for a card, filled `--surface-2`, with **no
shimmer**. The reference animates its skeletons and stops them under reduced motion;
here the resting form is already static, so there is nothing to stop. No spinner —
the page has no operation long enough to earn one, and a spinner over a list of names
implies the list is being computed when it is being fetched.

## Hero

Full width, **not** full height: the reference's hero is 818px tall at 1440 against
an 894px viewport, so the next act's top edge is visible at rest. Keep that — it is
what stops a page of thirty borrowed names reading as a splash screen.

- Field `--field`, padding `--hero-pad-top` (130px) / `--hero-pad-bottom` (64px).
- Nav is `position: absolute` over the slab at `--nav-h` (89px), transparent, no
  border and no shadow. Not sticky.
- Two columns at ≥992px: copy left, framed media right (`--r-md`,
  `--shadow-frame`). One column below, media after copy.
- Headline ceiling **two lines** at 45px/1.15; a third line means cutting words, not
  dropping to 40px.
- Above the headline: one borrowed proof mark — a review score, a rating — as a
  plate. Below the CTA pair: one line of plain-text qualifiers in `--ink-body` at
  17px, and one attributed quote.
- The act closes on the wave, and the band of name plates begins immediately under
  it.

## Responsive

Three breakpoints, measured: 1440, 768 and 390.

- **Gutter `--gutter` (24px)** at both narrow widths — 17 containers agree, and it
  does not change between 390 and 768.
- **Content `--content-max` (1170px)**, centred, gutters outside it.
- **Hero display 45px → 30px at ≤768**, tracking staying proportional (−0.9px →
  −0.6px, both −0.02em). The section head does not drop with it.
- **Body stays 17px at every width.** It is the most frequent size at 768 (352
  nodes) as well as at 1440.
- **The wave is hidden below `--wave-hidden-below` (768px)** and the acts butt
  directly. Keeping it at 390 costs 150px of scroll for a curve nobody reads.
- **The plate band wraps rather than scrolls.** A horizontally scrolling row of
  names hides the count, and the count is the argument.
- Two columns collapse to one at 992px; the framed media follows the copy.
- No horizontal overflow at 390: `documentElement.scrollWidth` equals 390.
- **Container queries.** Sorted by kind, because only the first three have a
  container answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | The plate band wrapping its names | CONTAINER | `container-type: inline-size` on the band, `@container` on the plate's padding |
  | Card grid stepping 3 → 2 → 1 | CONTAINER | container on the grid, `@container` on the tracks |
  | A card head stacking its title above its meta | CONTAINER | container on the card |
  | Hero going two-column to one | PAGE | viewport `@media (max-width: 991px)` |
  | The wave appearing and disappearing | PAGE | it closes a full-bleed act, so the page owns it |
  | Section pad 80/96 → 48/64 | PAGE | the page owns its rhythm |
  | Display 45px → 30px | PAGE | the headline answers to the viewport, not to its column |
  | A plate's own radius or border-width changing | SELF | **no container answer exists** — a container cannot query itself, and neither changes here |

- **Viewport.** `100dvh` for any full-height section, never `100vh` — though this
  pack's hero is deliberately not one.

## Motion tokens

From [`tokens/nameplate.css`](./tokens/nameplate.css), and every value is the
reference's own declared ladder confirmed against computed
`transition-duration`.

| Token | Value | Spends on |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | everything; it is the reference's own `--ease-out` |
| `--ease-drawer` | `cubic-bezier(0.32, 0.72, 0, 1)` | a panel opening |
| `--dur-press` | 140ms | the press |
| `--dur-fast` | 160ms | a colour change |
| `--dur-base` | 200ms | the lift and its shadow, together |
| `--dur-reveal` | 400ms | a section entrance |
| `--dur-entrance` | 450ms | the hero entrance |
| `--stagger` | 50ms | between siblings in one reveal |
| `--lift` | 2px | the hover travel |

`ease-in` is banned by the doctrine and does not appear in the reference either.

## Signature motifs

- **The plate.** A white pill with a 1px border and a 4% shadow, carrying one
  borrowed name as type. 52 computed elements against a page that is 87% square.
- **Square everything else.** 1,091 of 1,251 visible elements at `--r-none`. The
  page is not a rounded page with some square parts; it is a square page with one
  round shape, and that is what makes the plate legible.
- **The wave.** A 150px SVG arc closing an act, overspilling to 150% width, filled
  in the colour of the act below, gone below 768px.
- **The lift as one gesture.** Travel and shadow-growth share `--dur-base`, so a
  plate rises *and* separates in one motion. Animating one without the other is the
  single easiest way to break the pack.
- **One framed panel per screen** wearing the 70px-blur shadow, everything else on a
  hairline.
- **Two uppercase registers**, 0.06em on controls and 0.175em on micro-links.

## Signature element

**The plate band.** A wrapping row of white bordered pills, each carrying one
publication's name as 15px/500 type — not a logo — on the cool grey slab, arriving
directly under the hero's wave.

It is the element the page is remembered by, and it is remembered because of what it
refuses: no logos, so no ransom-note of thirty typefaces; no fills, so the border
does the work; no scroll, so the count is visible; one name per plate, so nothing is
crowded. A logo wall says *we are used by*; a plate band says *this is a list you can
read*, and a reader who can read the list believes it.

Build it once, put it directly under the hero, and do not repeat it lower on the
page — a second plate band is how the argument turns into wallpaper.

## Micro-interactions

- **Plate hover:** `translateY(-2px)` + `--shadow-pill-hover` + border to
  `--ink-faint`, all at `--dur-base` on `--ease-out`. Colour at `--dur-fast`.
- **Primary hover:** `--shadow-action-hover` + the lift. The fill does **not**
  change — the reference's own hover here is a glow, and darkening the ramp on hover
  reads as a disabled state.
- **Press:** `--dur-press`, `--action-pressed`, lift returns to 0.
- **Focus-visible:** `--focus-w` solid `--focus-color`, `--focus-offset`. Opaque,
  always.
- **Section reveal:** opacity + `translateY(--reveal-y)` over `--dur-reveal`,
  siblings staggered by `--stagger`. It never gates content — the element is legible
  before, during and after.
- **Input focus:** border to `--accent`, plus the ring. No fill change.

## Bans

- **No scroll clock, no parallax, no scrub, no `animation-timeline`.** Zero
  occurrences across 20,240 lines. `MOTION_INTENSITY` above 4 has nothing to buy.
- **No translucent focus ring.** The reference's `rgba(…, 0.35)` is 1.34:1 on white
  against a 3:1 floor. Opaque or it is not a ring.
- **No white text on the measured coral.** `#fc6a2a`/`#fe506c` are 2.90:1 and 3.19:1
  under white. Use `--action`, which is the same hue corrected.
- **No blue primary action.** The declared layer makes the blue look primary; the
  render says it paints four text nodes and a third-party cookie banner.
- **No second family.** One face, four weights.
- **No logo wall.** The plate carries type. A pack whose proof is a readable name
  loses the argument the moment it becomes art.
- **No rounding for friendliness.** Every radius you add spends the plate's meaning.
- **No `--shadow-frame` on a card or a control.** One object per screen.
- **No dark variant.** The reference has no dark band anywhere; shipping one here is
  inventing, not extending.
- **No horizontally scrolling plate band.** The count is the argument.
- **No `ease-in`.**

## Gotchas

**The declared token layer lies, and this reference is the sharpest case in the
library.** It declares `--primary: #84B761` three times — a green nothing paints. Its
real primary action is a gradient, and a gradient's element has a **transparent**
`background-color`, so any colour census that reads `background-color` alone finds
the blue cookie banner and reports it as the brand. Both facts were caught by
rendering: read computed styles, and read `background-image` too.

**Vendor CSS outnumbers authored CSS here.** The site loads Bootstrap 4.6.2, an
*ave* theme, a *frest* admin theme and three Font Awesome versions. Counting all of
it yields Bootstrap's `--primary`, `--indigo`, `--purple` and `--teal` as this
brand's palette. Only `/assets/css/` is authored, and the counts in this pack are
over those 11 files.

**Five corrections travel with the pack, each with its number at the declaration.**

1. *The primary action fails AA.* White on the measured ramp is 2.90:1 and 3.19:1,
   3.04:1 at the midpoint — under AA and under the 3:1 large-text floor, and the
   reference puts a 12px uppercase label there. `--action` holds both hues in OKLab
   and moves lightness until white clears 4.5:1 everywhere along the ramp.
2. *The body grey fails on the slab, not on the page.* The reference's body grey is
   `#737373`, and it is 4.42:1 on `--field`, where the floor is 4.5. The same
   `#737373` measures 4.74:1 on `--bg` — so the page passes and the slab does not,
   and the hero stands on the slab. This is the correction a white-background-only
   check never finds.
3. *The focus ring is invisible.* `2px solid rgba(5,135,237,0.35)` composites to
   `#d3dff9`, which fails at 1.34:1 on `--bg`, and to `#cbd8f6`, failing at 1.33:1 on
   `--field`; all three of the reference's alpha variants (0.35, 0.40, 0.45) miss the
   3:1 non-text floor on both fields. The hue was never the problem — opaque, the
   same blue clears. Drop the alpha, keep the colour.
4. *Two greys carry live text below every floor.* Against the white page, `#8fa6d0`
   measures 2.46:1 across 25 nodes and `#9ca3af` measures 2.54:1 across 21. Here they
   become `--ink-quiet` and `--ink-soft`, each clearing AA on both fields; the
   measured `#9ca3af` survives as `--ink-faint`, for icons and disabled labels only.
5. *Tap targets.* At an emulated 390×844, 87 of 137 visible interactive elements are
   under 44px tall. `--tap-min` is a floor for every control in this pack.

**The reference gets reduced motion right, which is rarer than the failures above.**
23 blocks across 7 of its 11 authored stylesheets, and its reveal layer restores
`visibility: visible; opacity: 1` — content is never locked behind an animation that
did not run. Keep that shape; it is the one thing here worth copying without
correction.

**`--tracking-caps` is true of half the page.** The declared 0.06em matches the 14px
control label exactly and is wrong for the 12px micro-link, which computes 0.175em.
Two registers, two tokens.

**The hero is not full-height and that is deliberate.** 818px against an 894px
viewport. "Fixing" it to `100dvh` turns a page whose argument is a long readable list
into a splash screen.

**The wave needs the overspill.** `calc(150% + 1.3px)`. At exactly 100% the same path
reads as a bubble, and the 1.3px is what hides the seam at fractional device pixel
ratios.
