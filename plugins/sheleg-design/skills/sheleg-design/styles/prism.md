# Style pack — Prism

Origin: <https://milvus.io/> (2026), the front door of an open-source vector
database. Every value below was read off its live computed styles on 2026-08-09,
and every ratio was computed by importing this repository's own palette gate.
White passed through a prism — one static iridescent wash, pink to lilac to mint
to cyan — under near-black type that never picks up its hue, with **mono body
copy** and a heavy grotesque display.

The identity in one sentence: **a project, not a company.** The first action on
this page is a command; the second is a benchmark. The wash is the only warmth it
allows itself, it is spent once at the top, and below it the page is plain white
with a monospaced argument on it.

Contract: widened — all thirteen headings.

## Register

Choose this pack for an **open-source infrastructure project's front door**: the
page a developer arrives at from a GitHub README or a conference talk, where they
want the install line, the numbers, and the architecture, in that order. Its
readers are not buyers yet; they are evaluators, and the page's job is to let
them start in under a minute.

It rides the SHELEG cinematic layer at a low setting: the wash is static and the
page's motion budget goes to reveals, not to atmosphere.

**Not for:** the commercial product built on top of that project — that is
`maquette`, and the two are frequently the same company's two faces. A page
selling auditability of *answers* rather than availability of *software* —
`field-notes`. A product-UI surface, which is `workbench`. A marketing page whose
centre is a screenshot — `showroom`.

### The fork against [`cyclorama`](./cyclorama.md)

Both are pale light fields with mono in the body, and both will be reached for by
an AI-infrastructure brief. The difference is whether the field moves.

`cyclorama`'s field **breathes**: six pastel stops on a 32-second loop, with a
typewriter *serif* display over it. Its subject is a change of state, and the
page is in a state of change to make that structural.

`prism`'s field **holds**: one static gradient, spent at the top, with a heavy
*grotesque* display. Its subject is a piece of software that exists right now and
can be installed in the next thirty seconds.

Route by whether the page is arguing that something will change (`cyclorama`) or
that something is ready (`prism`).

### Against [`blueprint`](./blueprint.md)

Both were extracted from vector-database companies and the category cannot
separate them. `blueprint` is for a **buyer** weighing precision and cost — it
argues in figures, on a drawing sheet, and it ships no install component at all.
This pack is for an **evaluator**, and its first artifact is the install line.
If the reader has a purchase order, that pack; if they have a terminal, this one.

### Against [`maquette`](./maquette.md)

They are the same company's project page and product page in the real world, so
the confusion is structural. `prism` is light, and its centre is a **command**.
`maquette` is dark, and its centre is a **model of the architecture**. If the
reader is meant to run something, this pack; if the reader is meant to understand
a structure before buying it, that one.

## Palette

Ready-made token layer: [`tokens/prism.css`](./tokens/prism.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#FFFFFF` | the field | — |
| `--surface` / `--surface-2` | `#F9F9F9` / `#F5F8FB` | card · the sunken code well | — |
| `--ink` | `#00131A` | near-black with a cyan cast | **18.95:1** |
| `--ink-2` | `#2E373B` | secondary headings | 12.17:1 |
| `--ink-soft` | `#667176` | body-safe secondary copy | **5.01:1 — clears AA** |
| `--ink-faint` | `#9CA6B4` | furniture only, never text | 2.4:1 |
| `--line` / `--line-strong` | `#E9E9ED` / `#D0D7DC` | card border · emphasis | — |
| `--accent` | `#00B3FF` | **fill, rule, chart series, mark** | 2.36:1 as text ✗ |
| `--accent-ink` | `#1493CC` | **large display text only** | 3.4:1 |
| `--on-accent` | `#00131A` | the label on an accent fill | **8.02:1** |
| `--wash-1` … `--wash-4` | `#FBEAF3` / `#ECE9F7` / `#E6F5EC` / `#E3F4FB` | the prism's four stops | ink 15.85–16.82:1 over the four |
| `--good` / `--warning` / `--danger` | `#65F8C3` / `#F25C05` / `#D51F00` | status | see the rule below |

Three rules carry this palette.

- **The accent is a fill, not a text colour.** `#00B3FF` measures **2.36:1** on
  white, and the reference sets 72px display type in it. This pack does not
  propagate that: the cyan fills a button, draws a rule, carries a chart series
  and marks a dot. Where a display word genuinely needs the accent's family it
  takes `--accent-ink` `#1493CC` at 3.4:1 — **large text only**, never body, and
  never below 24px.
- **Status is never by colour alone.** `--warning` `#F25C05` and `--danger`
  `#D51F00` separate by only **11.3** at full colour, under the floor of 15 —
  two warm reds a sixth of a hue apart. Every status carries its word. A page of
  bare orange and red dots is unreadable to more people than it looks.
- **`--ink-soft` is a real body colour** at 5.01:1, which is unusual and worth
  using: secondary copy stays quiet instead of being promoted to full ink.

## Type

**The inversion is the signature: the display face is the grotesque, and the
body is mono.** Most packs do the opposite, and this one reads as a project
precisely because it does not.

- **Display — Geist, 700** (600 for section headings). Heavy, tight, and set at
  72px in the hero.
- **Body, lede, UI, data — Geist Mono, 400.** Paragraphs, list items, labels,
  install lines, benchmark tables. All of it.
- Both are SIL OFL, so there is **no substitution trap in this pack** — a rare
  luxury, and one reason it ports cleanly.

**Mono body copy needs more leading than a grotesque does**, which is the
adjustment most people miss: `--lh-lede` is 1.7 and `--lh-body` is 1.65, against
the 1.5 a sans would take at the same size. Set mono at 1.5 and the paragraph
turns into a wall.

| Token | Size / line-height | Tracking | Weight |
|---|---|---|---|
| `--t-display` | 72 / 1.111 | −0.01em | 700 |
| `--t-h2` / `--t-h3` | 42 / 1.286 · 28 / 1.3 | −0.01em | 600 |
| `--t-lede` | 18 / **1.7** — mono | 0 | 400 |
| `--t-body` / `--t-sm` | 16 / **1.65** · 14 / 1.6 — mono | 0 | 400 |
| `--t-label` | 12 / 1.5 — mono, caps | **0.06em** | 400 |

Measure: keep mono paragraphs to **60 characters**, not the 75 a sans tolerates.
Monospace runs wider per character and a 75ch mono line is a scroll.

## Texture & surface

- **The wash is the pack's one gradient and it is spent at the top.**
  `--wash`, four stops at `100deg`, across the hero and nothing else. Below the
  hero the page is `--bg` white. A second gradient anywhere — a section, a card,
  a button — is the fastest way to turn this pack into a generic AI landing page.
- **The wash is low-saturation on purpose**: `--ink` measures at least **15.85:1**
  over every one of its four stops (18.95:1 on plain `--bg` white), so the
  headline needs no scrim and no text-shadow.
  If you deepen the stops you will need a scrim, and a scrim over a wash is two
  wrongs.
- **Elevation is flat.** A 1px border or nothing; `--ring-hairline` is the only
  "shadow" token and it is a ring. There is no drop shadow in this pack.
- **Radii `4 / 8 / 12`, plus a pill for chips.** 8px is the default for cards,
  buttons and the code well, and inner elements step down to 4px.
- Spacing is a 4px ramp; the page column is 80rem.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary CTA** | `--ink` fill, `--on-ink` label, `--radius`, `14px 28px`, 16px mono | fill → `--ink-2` over `--dur-fast` | `translateY(1px)` | `opacity: .45`, `cursor: not-allowed` |
| **Secondary CTA** | `--surface` fill, `1px --line-strong`, `--ink` label, same metrics | border → `--ink-soft` | as above | as above |
| **Accent CTA** | `--accent` fill, `--on-accent` label (8.02:1) | `--accent-hover` | as above | as above |
| **Install line** | `--surface-2` fill, `1px --line`, `--radius`, `12px 16px`, mono 14px, a `$` prompt in `--ink-faint`, a copy button at the right | copy button tints | copied: label swaps to `copied`, **not** a colour-only change | — |
| **Card** | `--surface`, `1px --line`, `--radius`, 24px padding, no shadow | border → `--line-strong` | — | — |
| **Benchmark row** | mono `--t-sm`, numbers right-aligned, `1px --line` bottom rule | fill → `--surface` | — | — |
| **Status mark** | an 8px dot in its status colour **with its word beside it**, mono `--t-label` | none | — | — |
| **Repo badge** | `--surface` fill, `1px --line`, pill, a star count in mono, 13px | border → `--line-strong` | — | — |
| **Nav item** | mono `--t-sm` caps at `0.06em`, `--ink-soft` | colour → `--ink` | colour → `--ink`, 1px `--accent` underline | — |
| **Input** | `--surface`, `1px --line-strong`, `--radius`, `10px 14px`, **16px** mono | border → `--ink-soft` | focus: `--accent` border, 3px accent halo at 20% | `opacity: .5` |
| **Loader** | **pack decision:** a skeleton at `--surface-2` with the geometry of the block it replaces, no shimmer. The reference ships none on its marketing surface | — | — | — |
| **Empty state** | **pack decision:** one `--ink` line, one `--ink-soft` line, and the install line — for a project page the empty state is always "you have not run it yet" | — | — | — |

## Hero

- **Height** `--hero-min-h: 100dvh`. Never `100vh`.
- **The wash occupies the whole first viewport** and stops at its bottom edge —
  a hard stop, not a fade. The page below is white, and the seam is the point:
  the prism is above, the work is below.
- **Centred composition:** a mono announcement chip, the display headline with
  **one phrase in `--accent`** (this is where `--accent` is a *fill* behind text
  or the phrase takes `--accent-ink` — see Bans), a mono lede at 60ch, two
  buttons, and then the install line.
- **Line ceiling: two.** At 72px and 1.111 leading a third line eats the install
  line, which is the one thing a project page must show above the fold.
- **The install line is in the first viewport.** Not below it, not behind a tab.
  A developer who has to scroll to find how to start has already left.
- The first viewport does not carry a screenshot, a metric row or a logo wall.

## Responsive

- **Type steps at breakpoints:** the display drops 72 → 48 → 36. The mono body
  never goes below 14px, because mono at 13px on a phone is a transcription
  exercise.
- **The measure tightens before the size does.** At tablet the mono paragraph
  goes 60ch → 48ch and keeps its size; only below 640px does the size step down.
- **The wash keeps its four stops** at every width — do not drop to two on mobile.
  It is a spectrum; two stops is a gradient, and a gradient is what every other
  page has.
- **The install line goes full-width and keeps its copy button.** It is the last
  thing to be compromised.
- Full-height sections use `dvh`; bare `100vh` is banned.

## Motion tokens

- **One curve, `cubic-bezier(0.4, 0, 0.2, 1)`**, two durations: `--dur-fast .2s`
  for control states and `--dur-base .3s` for reveals.
- **The wash never animates.** Not a hue rotation, not a slow pan, not a
  scroll-linked shift. It is a static optical fact; animating it is the single
  change that would turn this pack into `cyclorama` badly.
- Transitions are scoped to named properties; `transition: all` is banned.
- **The reference ships no `prefers-reduced-motion` branch at all** — see
  Gotchas. This pack requires one.

## Signature motifs

- **The prism wash**, four stops, once, at the top, with a hard bottom edge.
- **Mono body copy** — the inversion that makes the page a project.
- **The install line** in the first viewport, with a `$` prompt and a copy
  button.
- **Benchmark rows** with right-aligned mono numbers and hairline rules.
- **Caps mono nav** at `0.06em`.
- **The repo badge** with a live star count — social proof stated as a number in
  mono rather than as a logo wall.
- **One accent phrase** in the headline and no other accent text on the page.

## Signature element

**The wash.** One static gradient, four stops, across the first viewport and
nowhere else.

It carries the identity because of where it *stops*. Any page can put a pastel
gradient behind a hero; this one puts it there, gives it a hard bottom edge, and
then spends the rest of the page in plain white with monospaced type on it. The
edge is the argument: the prettiness is bounded, it happens once, and underneath
it is a piece of software with numbers attached.

Everything else is quiet to pay for it — no second gradient, no shadow anywhere,
one accent used only as a fill, and a display face that is heavy rather than
decorative. Spend the colour at the top and let the rest be white, or the pack
has no centre.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack: keep the scroll clock, run the Reveal set
at `--dur-base` on the one curve, translate 10px and opacity.

The ambient layer, if there is one, is a **point cloud in the accent** at low
opacity inside the hero only — points, not particles, and they must die at the
wash's bottom edge along with everything else. Nothing generative appears on the
white.

The wash is layer 1 in the depth model and it is `pointer-events: none`. It is
never put on a scroller, never parallaxed, and never faded — it ends where the
hero ends.

## Micro-interactions

- **Buttons** transition fill and border over `--dur-fast`; press is
  `translateY(1px)`. Nothing scales.
- **The copy button** changes its *label* to `copied`, not just its colour — a
  colour-only confirmation is invisible to a third of the people this page is
  for, and it is the same rule as the status marks.
- **Focus-visible** is an `--accent` border plus a 3px accent halo at 20% alpha,
  following the element's own radius.
- **Nav** takes a 1px accent underline on the current item; the colour changes
  with it.
- Rows tint to `--surface`; nothing lifts, because there is no shadow to lift
  into.

## Bans

- **`--accent` as body text.** 2.36:1. Large display text takes `--accent-ink`
  at 3.4:1, and nothing below 24px takes either.
- **A second gradient.** Anywhere. One wash, at the top, with a hard edge.
- **Animating the wash** — hue rotation, panning, scroll-linked anything.
- A drop shadow; a lifted card; a glow.
- **A sans-serif body.** The mono body is the pack; setting Geist in a paragraph
  turns it into a company page with a nice gradient.
- Mono paragraphs longer than 60 characters, or mono set at 1.5 leading.
- A status mark without its word; `--warning` and `--danger` distinguished by
  colour alone.
- `--ink-faint` as text; a third font family.
- Fluid `clamp()` type; `transition: all`; `100vh`; a scroll listener.
- Burying the install line below the fold.

## Gotchas

- **The reference ships no `prefers-reduced-motion` branch — zero blocks** —
  while running `marquee`, `ping`, `pulse` and `scroll` animations. This pack
  requires the branch, and it is the first thing to add when porting.
- **The reference's own display type fails contrast.** Its 72px headline sets
  "Vector Database" in `#00B3FF` on white: **2.36:1**. Large text still needs
  3:1, so it fails even the relaxed floor. This pack routes accent-coloured
  display text to `--accent-ink` and keeps the bright cyan for fills. If you copy
  the hero verbatim you copy the failure.
- **Mono leading is not sans leading.** 1.65 for body, 1.7 for the lede. This is
  the most common way the pack is ported badly — the values look excessive in a
  spec and are correct on the page.
- **The measure is 60ch, not 75ch.** Monospace runs wide; the sans habit produces
  a line that overflows on a laptop.
- **The wash's stops are lighter than they look in a screenshot.** All four sit
  above 15.8:1 against `--ink` — the 18.95:1 figure belongs to plain white and
  was carried onto the wash by hand until 1.10.0 recomputed it. If you sample them from a JPEG you will get deeper
  values, and then you will need a scrim you should not need.
- **`--good` `#65F8C3` is a fill, not a text colour** — a mint at that lightness
  is below 2:1 on white. It marks, it does not label.
- **Values are a snapshot** taken 2026-08-09 from a live production site. Treat
  them as extracted, not eternal.
