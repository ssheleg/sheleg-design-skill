# Style pack — Manpage

Origin: <https://zernio.com> (2026), the marketing site of a unified social-media
and messaging API. Every value below was read on 2026-08-12 off its
server-rendered HTML for `/`, `/pricing` and `/phone-numbers` and off its two
shipped stylesheets (`/_next/static/chunks/0idbh9t-u9vsm.css` and
`11gmwmuo_p3gd.css`, 316,561 bytes together), which declare 398 custom properties
— the Tailwind v4 default ramps plus twelve bespoke brand names: coral, cream,
ink, charcoal and burgundy, each with a `-muted` partner. Ratios were computed by
importing this repository's own palette gate.

Cream paper, one vivid coral, a 48px display that never grows louder, a 576px
column narrower than most prose — and **the entire page set in the reader's own
system monospace, which costs zero bytes to ship.**

The identity in one sentence: **the landing page is the documentation, set in the
typeface of the documentation.** Not a page *about* an API with a code sample
dropped in for proof — a page that has decided the developer already lives in a
terminal, and meets them in that typeface, at that measure, with section headers
that look like printed tags and answers laid out as a definition list.

Contract: widened — all thirteen headings.

> **The heading fork against [`roster`](./roster.md).** These two make the same point
> about markup from opposite ends. Here the visible label chip **is** a real `<h2>`, so the
> page's structure and its outline are the same object. `roster`'s reference does the
> reverse — an `.sr-only` `h1` at 1×1px with the visible 68px line as a `<span>`, and all
> sixteen of its `<h2>`s spent on small eyebrows — which that pack records as a defect and
> refuses to teach. If you are deciding where a heading lives, read both.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose this pack for **a developer product whose buyer reads code for a living**:
an API, an SDK, a CLI, a protocol, an MCP server, developer infrastructure,
anything whose evaluation step is "show me the call." It suits a product where
the honest hero is not a screenshot but six lines of a request, and where the
reader's first question is *what does the call look like* — answered by showing
the call, in the typeface they would read it in anyway.

It rides the SHELEG cinematic layer at the lowest intensity in the family: one
blur-in on the headline at the measured 0.1s delay, one entrance per section, and
**no scrubbing, no parallax and no scroll clock anywhere.** The page animates on
arrival and then holds absolutely still, because a document that moves while you
read it is a document you stop reading.

**Not for:** a product sold on how it *looks* rather than what it returns — a
whole application surface at real size is [`showroom`](./showroom.md). A control
plane narrating live telemetry on a dark field is
[`instrument-console`](./instrument-console.md). A page whose subject is an
accumulating total — [`scoreboard`](./scoreboard.md). A product whose value is a
verdict about the visitor, proven by returning it live —
[`datasheet`](./datasheet.md). A product that sorts the reader's incoming mess into
named categories, and proves it by colour-coding the categories —
[`pigeonhole`](./pigeonhole.md), which shares this pack's motion posture: the two
are the quietest in the family, entrance-only, with no scroll clock between them.
A developer page whose focal element is a score a machine assigned the reader,
on a coal field, with a serif carrying the prose — [`ora`](./ora.md); it refuses
a second family for the same reason this pack does and then spends the freedom
the other way, mono for facts and serif for sentences. And **not** the product UI itself: this is the
marketing page a developer lands on, not the dashboard they log into afterwards,
which is [`workbench`](./workbench.md).

### The fork against [`datasheet`](./datasheet.md), which is the one people get wrong

Both are off-white technical paper with one warm orange-red accent. Both rule
with hairlines rather than shadow. Both set small type in a mono, both refuse a
serif, and both come from an API company's marketing site. They are not
interchangeable, and the test is **who the page is about.**

`datasheet` is about *the reader*: it runs an instrument that reads your visitor
id, your city, your IP back to you, and its register is *what did you get*. This
pack is about *the product*: the focal element is a code frame showing a call
**you** would write, and its register is *what will you type*. One returns a
reading; the other hands you a snippet.

The give-away is the typeface of the body copy. `datasheet` sets its body in a
sans (Inter) and reserves the mono for readings — values the instrument produced.
This pack sets **everything** in mono, body copy included, and reserves the sans
for almost nothing. That is not a decoration: it is the claim that the reader
prefers a fixed pitch, which is true of a developer audience and false of almost
every other.

### The fork against [`field-notes`](./field-notes.md)

Both are cream paper with mono small type. `field-notes` annotates a *source* so
a claim can be checked — its register is *how do you know*. This pack annotates
nothing; its mono is not a citation layer but the whole body face. A page that
needs its claims traceable to evidence is `field-notes`, and it will look
over-engineered here.

### The fork against [`blueprint`](./blueprint.md)

Both use a narrow measure and a technical register. `blueprint` draws
construction — rules, guides and the geometry of a thing being specified. This
pack draws *text*: the only structural device is a label chip and a definition
list. If the page wants to show how something is built, that is `blueprint`; if it
wants to show what to type, it is this.

## Palette

Token layer: [`tokens/manpage.css`](./tokens/manpage.css). Copy it verbatim and
consume only `var(--…)`.

Two themes, both the reference's own. Light is cream paper; dark is `#0d0d0d`
with the cream becoming the ink. The dark theme is a **theme** — a preference the
reader toggles from the sidebar — not a state and not an alarm.

| Role | Light | Dark | Note |
|---|---|---|---|
| Field | `#f0efeb` | `#0d0d0d` | its `--color-cream`; the dark field is *not* `--color-ink` |
| Surface | `#ffffff` | `#1b1818` | card and nav pill |
| Ink | `#2d2d2d` 11.97:1 | `#f0efeb` 16.89:1 | display and headings |
| Body | `#6b6b6b` 4.63:1 | `#b8b2b2` 9.30:1 | **all** body copy, at 14px |
| Accent | `#eb3514` 3.61:1 | `#eb3514` 4.68:1 | coral: a mark, not a word, on light |
| Accent ink | `#660202` 11.59:1 | `#e09282` 7.96:1 | the accent that may carry a word |
| Rule | `#e5e5e5` | `#3d3838` | the only divider |

The one thing to understand about this palette: **the ink family is the dark
theme, not the light ink.** The reference names `--color-ink: #131010` and then
sets its headings in `--color-charcoal: #2d2d2d` and its body in
`--color-charcoal-muted: #6b6b6b`. Reading the token names instead of the markup
gets the light theme wrong by two steps.

Coral is the pack's constraint. At 3.61:1 on cream it clears the 3:1 non-text
floor and misses AA for text, so it may be a wordmark, a button fill, an icon, a
border, a 20px coral glow — and **not a 12px word**, which is precisely what the
reference does with it. Burgundy is the same hue family at 11.59:1 and is what
this pack paints a word in.

Status is four SELECTED values, and the arithmetic is in the token layer's
comments: the reference's own live-status green fails AA at 2.82:1, its ramp
cannot be stepped into a legal set, and emerald can. Warning is forced almost
black because **the accent occupies the warning hue** — every amber that reads as
a warning collides either with coral under dichromacy or with danger at full
colour. Light clears both gate floors (17.5 full, 8.1 CVD); dark clears the hard
floor at 10.1 and runs tight at 6.8 under dichromacy.

**Status is never by colour alone in this pack.** Every status carries its word,
exactly as the reference does — `online`, `Done`, `Key copied to clipboard` — and
on the dark theme the tint is the card rather than an invented wash, because the
reference ships no dark status tint to read one off.

## Type

**One webfont. The display face is free.**

The reference loads exactly one font file — Geist Sans, a single variable `woff2`
at `font-display: swap` — and sets its headline, its body, its chips, its code
frames and its FAQ in the **system monospace stack**:

```
Menlo, Consolas, Monaco, "Liberation Mono", "Courier New", monospace
```

That stack is already on the reader's machine. There is nothing to download,
nothing to swap, and no invisible-text window on the element that carries the
whole identity. **Do not substitute a webfont mono here.** JetBrains Mono or Berkeley
Mono would each cost a render-blocking request to look *less* native: the texture
of this pack is the reader's own Menlo or Consolas, and the fact that it differs
slightly from machine to machine is the point — it reads as the terminal, not as
art direction.

| Role | Size | Weight | Tracking | Line height |
|---|---|---|---|---|
| Display | 48px → 36px → 30px | 700 | -0.025em | 1 (solid) |
| Title | 24px | 600 | — | 1.333 |
| Lead | 16px | 400 | — | 1.5 |
| Body | **14px** | 400 | — | 1.4286 |
| Chip | 12px | 500, uppercase | 0.05em | 1.3333 |
| Mono/code | 12px | 400 | — | 1.5 |

Two things carry the register. The display **stops at 48px** — a man page does
not shout, and there is no step above it. And the body is **14px**, not 16px:
denser than a marketing page and exactly the density of a documentation page.

## Texture & surface

Cream paper, one hairline, no shadows. `--lift-card` is a single 1px bottom line
— the reference's own `--tw-shadow` — and nothing on the surface casts downward.

The device that makes this pack recognisable in one glance costs one declaration:

```css
body { padding: var(--frame); } /* 4px */
```

The reference pads `body` by 4px, so the entire document sits inset from the
window edge and every rounded panel closes against a visible margin of paper. It
reads as a printed sheet laid on a desk rather than a page bolted to the viewport.
It is the cheapest identity move in the whole family — and the easiest to
delete by accident during a layout refactor.

The other surface rule: **radii stay small and nothing is a pill.** The label chip
is 2px, the button 8px, the panel 16px. A fully round control would break the
printed-tag reading instantly.

## Motion tokens

Entry only. Every value MEASURED off the reference's own keyframes.

| Token | Value | Source |
|---|---|---|
| `--dur-instant` | 0.15s | its `--default-transition-duration` |
| `--dur-fast` | 0.2s | `slideInRight` |
| `--dur-base` | 0.5s | `fadeInUp` |
| `--dur-reveal` | 0.6s | `fadeInBlur` — the hero's entrance |
| `--stagger` | 0.1s | `[animation-delay:0.1s]`, written inline on the `h1` |
| `--reveal-y` | 12px | `fadeInBlur`'s `translateY` |
| `--reveal-blur` | 8px | `fadeInBlur`'s `filter` |
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | its `--ease-out` |

Nothing here scrubs. The reference ships no scroll listener and no parallax on
these three pages, and this pack forbids adding one: see Bans.

## Motion flavor

The signature entrance is **`fadeInBlur`**, and it is worth naming because it is
rarer than a rise and reads better on mono:

```css
@keyframes fadeInBlur {
  from { opacity: 0; filter: blur(var(--reveal-blur)); transform: translateY(var(--reveal-y)); }
  to   { opacity: 1; filter: blur(0);                  transform: translateY(0); }
}
```

Text arrives *out of focus* and sharpens. On a fixed-pitch face the effect is
specific: monospace has strong vertical rhythm, so a blur reads as a page
resolving rather than an element sliding. Applied for 0.6s with `ease-out` and
`both`, once, on the headline, after 0.1s.

Then the page stops. One entrance per section on the way down (`fadeInUp`, 0.5s,
20px), and no element on the surface moves again — no hover lift on cards, no
drifting gradient, no counter that keeps counting.

Degrade to calm: at `prefers-reduced-motion: reduce` every duration and the
stagger go to zero, the blur never applies, and the headline is simply already in
place. **Infinite motion stops rather than shortens** — see Gotchas, because this
is the one place the reference gets it wrong.

## Signature motifs

Four devices, in the order a reader meets them.

**1. The coral label chip, which is the section heading.** The most copied thing
on this page. A 12px uppercase mono tag in a coral wash with a coral edge, sitting
where a section title would go — and it is a real `<h2>`:

```html
<h2><span class="chip">How It Works</span></h2>
```

The chip is the semantic heading, not a decoration above one. That single
decision is why the page has a clean outline (one `h1`, one `h2` per section) while
looking like a printed document rather than a marketing page.

**2. The `└` tree glyph.** Answers, sub-points and notes hang off a box-drawing
character in its own grid column:

```html
<dd class="grid grid-cols-[auto_1fr] gap-x-2">
  <span aria-hidden="true">└</span>
  <span>Custom integrations take 8-12 months. Zernio takes under an hour.</span>
</dd>
```

Two columns, not a text prefix — so the glyph never wraps into the answer and
never lands in an extracted snippet. It is terminal output as a typographic
device, and it costs nothing.

**3. The code frame.** A dark panel at 16px radius with three window dots, a
filename, a language label and a copy affordance. It is the only dark element on
the light theme, and it is the hero's focal point — the page's argument is the
snippet.

**4. The width ladder.** The argument runs in 576px; only evidence widens.

| Step | Width | What sits in it |
|---|---|---|
| `--measure-text` | 576px | the argument, the steps, the closing CTA |
| `--measure-hero` | 768px | the headline and its code frame |
| `--measure-proof` | 896px | the testimonial grid |
| `--measure-foot` | 1080px | the footer columns |
| `--measure-wall` | 1152px | the logo wall |

## Micro-interactions

- **Buttons** transition `background-color` only, over `--dur-instant`. No lift,
  no scale, no shadow bloom.
- **Links** underline on hover; coral links take `--accent-ink` so the word clears
  AA.
- **The copy button** on a code frame swaps its icon to a tick and holds it — the
  reference does this and it is the right feedback, because a toast for a copy is
  noise.
- **Focus** is a 2px `--focus-color` ring. Burgundy on light, coral-muted on
  dark — not the accent, which fails the 3:1 non-text floor on this pack's own
  chip wash at 3.24:1.
- **The FAQ does not open.** Every answer is already visible. There is no
  accordion to animate, which is both the accessibility win and the reason this
  section has no micro-interaction at all.

## Bans

- **No scroll clock, no scrubbing, no parallax.** This is the calmest pack in the
  family. The reference ships no scroll listener on these pages and neither may an
  implementation.
- **No mono webfont.** The system stack is the identity. Substituting one costs a
  request and looks less native.
- **No coral word under 24px.** 3.61:1 on cream. Use `--accent-ink`.
- **No white label on a coral fill.** 4.16:1. See Gotchas.
- **No pill radii.** Nothing rounder than 16px, and the chip stays at 2px.
- **No accordion on the FAQ.** Collapsing the answers is the single most
  destructive change available to this page — it costs the extractable answer for
  nothing.
- **No display step above 48px.**
- **No shadow.** One hairline, and the coral glow, which is a glow and not an
  elevation.
- **No status by colour alone.** Every status carries its word.

## Gotchas

Four corrections, all of them accessibility floors the reference misses. Every
replacement is a colour the reference already ships — nothing was invented.

**1. The white button label fails AA.** The hero's `Start for Free` is white on
coral: **4.16:1**, below 4.5:1 at the 16px semibold it ships. Both the hero and the
closing CTA carry it. The correction keeps the coral fill — the coral button *is*
the identity — and darkens the label to `--on-action: #131010`, which clears at
**4.55:1**. Where a white label is non-negotiable, `--action-strong` is the
reference's own burgundy and carries white at **13.34:1**.

**2. The coral chip label fails AA, and it is the signature element.** The section
chip paints 12px coral text on a coral/8 wash: **3.24:1** — worse than coral on
bare cream, because the wash lifts the field. The most recognisable device on the
page is the least readable thing on it. The correction keeps the wash and the edge
so the chip looks identical, and paints the label in `--accent-ink` (burgundy) at
**10.40:1**.

**3. The live-status green fails AA at 2.82:1.** `green-600` (`#00a544`) on cream
carries the credit balance, the `online` badge and both weekly counters — the most
load-bearing small text on the surface. It cannot be rescued by stepping its own
ramp: `green-700` still misses at 4.35:1, and `green-800` clears AA but its best
legal companion set separates by only 3.9 under dichromacy. Emerald — a ramp the
reference also ships in full — clears both floors at step 800. Hence
`--success: #005f46`.

**4. One reduced-motion gate out of eight animations.** The reference gates its
40s logo marquee behind `motion-safe:` and leaves running, for a reader who asked
for stillness: the hero's `fadeInBlur`, every section's `fadeInUp`, `fadeInScale`,
`slideInRight`, `pulse`, `ping`, and a **1.1s infinite `waveform`**. Gating the
most obvious offender and missing the rest is the common shape of this bug — it
looks handled in review. This pack collapses the whole surface, and infinite
motion **stops** rather than shortens.

**5. Not a defect, but the thing most likely to be broken by a refactor:** the
4px `body` padding. Delete it and the page loses its framed reading instantly,
with no error and no failing test. Keep it in the token layer as `--frame` so it
has a name worth preserving.

## Components

Per-component state, using the token layer only.

**Button (primary)** — fill `--action`, label `--on-action`, radius `--r-button`,
padding `--pad-button`, weight 600, 14px mono. Hover: fill `--action-strong` with
`--on-action-strong`. Active: no transform. Focus: 2px `--focus-color` ring, 2px
offset. Disabled: fill `--surface-2`, label `--ink-soft`, no pointer.

**Button (secondary)** — fill `--surface`, 1px `--rule` border, label `--ink`.
Hover: border `--ink-soft`. Same radius and padding.

**Chip (section label)** — fill `--accent-wash`, 1px `--accent-edge` border, label
`--accent-ink` at `--t-chip`, uppercase, `--tr-chip`, radius `--r-chip`, padding
`--pad-chip`. Never interactive.

**Card** — fill `--surface`, 1px `--rule`, radius `--r-card`, padding
`--pad-card`, `--lift-card`. No hover state.

**Code frame** — fill `#131010` on both themes (it is dark on light by design),
radius `--r-panel`, 12px mono. Header row carries filename in `--ink-soft`, three
9px dots, and a copy control that swaps to a tick.

**Definition list (FAQ)** — `<dt>` at 14px weight 600 in `--ink`; `<dd>` a
two-column grid, glyph column `aria-hidden`, answer at 14px in `--ink-soft`. Never
collapsed.

**Endpoint row** — a card whose leading element is a method badge: 12px uppercase
mono, `--success` for `GET`, `--info` for `POST`, each on its `-weak` tint at
`--r-chip`. Path in `--ink`, description in `--ink-soft`.

**Input** — fill `--surface`, 1px `--rule`, radius `--r-control`, 14px mono.
Focus: `--focus-color` ring, border `--accent-ink`. Error: border `--danger`, with
the message in `--danger` **and** an icon.

## Hero

The opening viewport, in order:

1. **An eyebrow line** — a `What's new ↗` link in `--accent-ink` beside a plain
   note, 12px mono. Announcements go here, not in a banner.
2. **The headline**, 48px/700/-0.025em in `--ink`, set solid, three lines at the
   measure. `fadeInBlur` after `--stagger`.
3. **A two-line subhead** at `--t-lead` in `--ink-soft`, stating what the product
   does and the one number that bounds it.
4. **Two actions side by side** — primary coral, secondary white with a border. On
   this pack the secondary is usually an OAuth continue.
5. **A reassurance line**, 12px `--ink-soft`: `No credit card required`, and one
   agent-facing affordance beside it.
6. **The code frame**, `--measure-hero` wide, showing a real call — imports,
   client construction, and the one endpoint the product is for.

The hero does **not** fill the viewport. `--pad-top` is 48px, rising to 96px at
`lg`, and the code frame is deliberately cut off by the fold — the crop is what
signals there is more of it.

## Responsive

Measured at the reference's own breakpoints (Tailwind v4: `sm` 40rem, `lg` 64rem).

- **Display** steps 48 → 36 → 30px. Tracking stays `-0.025em` at every step.
- **Hero measure** collapses `--measure-hero` → `--measure-text` below `lg`; the
  gutter stays 32px throughout, which is what keeps the mono from touching the
  frame.
- **Top padding** halves: 96px → 48px below `lg`.
- **The width ladder flattens.** Below 896px every step becomes
  `--measure-text` + gutter. The ladder is a desktop device; on a phone the page
  is one column and the rhythm carries the structure instead.
- **The testimonial grid** goes 3 → 1 column. It does not go to 2: at 14px mono a
  two-column card grid on a tablet produces a 5-word measure.
- **The nav pill** becomes a full-width bar with a sheet behind it. The pill
  floats only where there is margin for it to float in.
- **The code frame** keeps its 12px type and scrolls horizontally. It never
  reflows and never shrinks its type — a wrapped code sample is a wrong code
  sample.

- **Container queries.** Two components own their own width: the **code frame**,
  which scrolls rather than reflows and must decide that from its box, and the
  **endpoint row**, whose method chip and path share a line only while there is room
  for both. Both take `container-type: inline-size`. The 576px argument column is a
  page measure — **PAGE** — and so is the label chip's position in the flow.

## Signature element

**The coral label chip that is a real `<h2>`.**

Of everything on this page it is the one device that carries the identity, the
semantics and the SEO at once, and it is three lines of markup:

```html
<h2>
  <span class="chip">What You Can Do</span>
</h2>
```

```css
.chip {
  display: inline-flex;
  align-items: center;
  font-family: var(--font-mono);
  font-size: var(--t-chip);
  line-height: var(--lh-chip);
  font-weight: var(--w-medium);
  letter-spacing: var(--tr-chip);
  text-transform: uppercase;
  color: var(--accent-ink);          /* not --accent: 3.24:1 on the wash */
  background-color: var(--accent-wash);
  border: 1px solid var(--accent-edge);
  border-radius: var(--r-chip);
  padding: var(--pad-chip);
}
```

It looks like a printed tag, it is a heading to every crawler and screen reader,
and it replaces the whole apparatus of centred section titles with eyebrows above
them. Remove it and the page becomes an ordinary narrow-column landing page with a
mono font; keep it and the document reads as a specification.
