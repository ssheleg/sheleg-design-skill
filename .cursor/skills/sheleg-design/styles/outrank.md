# Outrank — a marketing page and a working tool, in one brand

Origin: <https://www.outrank.so> and its `/dashboard`, read 2026-08-21 in a
logged-in Chrome session. Every value below was measured off the served pages
with `getComputedStyle`, in both themes.

Contract: widened
Themes: light + dark — a full theme twin, toggled by daisyUI's `data-theme` and persisted by the reference.
Rank: none — the four status hues are peers, not a severity ladder.

**What this pack actually is, said before anything else.** Outrank ships two
systems under one brand. The marketing site is **Tailwind + daisyUI** — its
`--rounded-box`, `--btn-text-case` and `--p`/`--pc` HSL triplets are daisyUI's
own token names — and the product is **Semrush's Intergalactic**, 384
`--intergalactic-*` custom properties on the dashboard. Neither is Outrank's
invention, and a pack that presented this as a bespoke design language would be
claiming authorship of two published systems.

That is not a weakness; it is the reason to have this pack. **Every other pack in
this library is one surface.** This one is the seam between a landing that must
convert and a tool that must be worked in for hours, and the two halves *disagree*
— on the ink, on the radius, on the type family — while agreeing completely on the
brand. A team shipping both needs that agreement written down, and this is the
first pack that writes it.

## Contents

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

## Register

Confident, operational, slightly playful. The product says *"How we make magic
happen"* and then shows you a table of clicks and impressions. The marketing half
is warm and the working half is quiet, and the seam between them is the violet.

Motion ceiling: **2**. Measured, not chosen — the entire site's motion budget is a
0.15s colour transition. No scroll clock, no parallax, no scrub, no reveal.

## Palette

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--ink` | `#0D0D12` | marketing headline and body | 19.38:1 |
| `--ink-soft` | `#363D4F` | the hero subhead, secondary copy | 10.84:1 |
| `--ink-data` | `#020617` | every number in the product | 20.17:1 |
| `--ink-eyebrow` | `#5B6779` | the uppercase card label — **corrected** | 5.74:1 |
| `--accent` | `#882AFF` | the one brand hue, and it carries text | 5.49:1 |
| `--on-accent` | `#FFFFFF` | the filled button's label | 5.49:1 on `--accent` |
| `--info` / `--success` / `--danger` / `--warning` | `#008FF8` / `#009F81` / `#FF4953` / `#C2740A` | status **fills and dots, never a word** | 3.34 / 3.35 / 3.32 / 3.62 |
| `--info-ink` / `--success-ink` | `#006DCA` / `#007C65` | the same two roles when they carry a word | 5.20:1 / 5.16:1 |

- **The violet carries text in both directions, and that is rare.** `--accent` on
  `--bg` is 5.49:1 and `--on-accent` on `--accent` is 5.49:1, so the filled CTA
  clears AA for its label *and* the accent clears AA as a word on the page. Most
  brand violets at this saturation clear neither. It is why this pack does not
  darken the measured value.
- **Three status colours are not text and the pack says so.** 3.34, 3.35 and 3.32
  clear the 3:1 non-text floor and none reaches 4.5:1. Use them as the dot, the
  bar or the fill; when the state has to be *read*, `--info-ink` and
  `--success-ink` are the ones that carry it.
- **Two corrections, both the smallest the rule permits.** The reference's eyebrow
  `#64748B` measures **4.37:1 on `--surface`** — below AA at the 13px it is set
  at, on the field it appears on most; `#5B6779` is the nearest value that clears
  4.5 on both fields. The reference's warning `#FF642D` measures **2.95:1**, under
  even the non-text floor; `#E5511B` is the smallest darkening that clears it.

## Type

Two families, and the split is the whole typographic idea: **Plus Jakarta Sans**
sets what is read once, **Inter** sets what is read all day. The reference never
mixes them on one surface.

- Hero — Plus Jakarta Sans **700, 68px / 81.6px leading (1.2), −1.2px tracking**,
  centred. One word of the headline is set in `--accent`; the rest is `--ink`.
- Lede — Inter **400, 18px / 28px**, `--ink-soft`, two lines, centred under the hero.
- Metric — Inter **600, 32px / 32px leading (1.0), −1.28px tracking**, `--ink-data`.
  The leading is exactly the size: a number is a shape, not a line of prose.
- Eyebrow — Inter **600, 13px, 1.82px tracking (0.14em)**, uppercase,
  `--ink-eyebrow`. It labels a card and never a section.
- Control — Inter **600, 14px** on every button in both halves.

## Texture & surface

- Flat. Radii **24 / 16 / 8px, plus a full pill** — machined, not soft: the card
  is 24, the banner and modal 16, an action chip 8, and every CTA and status badge
  is `9999px`.
- **Elevation is a hairline, not a shadow.** The dashboard card is
  `1px var(--panel-line)` with `box-shadow: none`, on `--surface`. Measured across
  the whole dashboard: the only shadows in the product are on overlays.
- **The signature is a ring, and it is a border.** The filled CTA wears a **5px
  `--accent-ring`** — a wide light border, not a glow. It reads as a halo at a
  glance and costs nothing to composite, and it is the one device that makes this
  brand's button recognisable at thumbnail size.
- The landing field carries a **faint square grid** behind the hero — a page
  texture, not a component's.

## Components

| Component | Resting | Hover | Active | Disabled |
|---|---|---|---|---|
| **Primary button** | `--accent` fill, `--on-accent` label at 5.49:1, `--r-pill`, `10px 16px`, 14px/600, 5px `--accent-ring` | fill darkens one step; the ring is unchanged | `scale(0.95)` — daisyUI's `--btn-focus-scale`, measured | `--surface-2` fill, `--ink-eyebrow` label at **4.40:1**, ring removed |
| **Ghost button** | transparent, `1.5px --line-control` border, label in `--ink`, `--r-pill`, `12px 20px` | border to `--ink-soft` | as above | border `--surface-2`, and `--ink-eyebrow` on `--surface` is 5.27:1 |
| **Card** | `--bg`, `1px --panel-line`, `--r-card`, `24px` padding, no shadow | unchanged — a card is not a control | n/a | n/a |
| **Metric pair** | eyebrow label above, `--t-metric` number below, optional caption in `--ink-soft` | n/a | n/a | number renders `—`, caption states why |
| **Status chip** | tinted `--r-pill`, 14px/500, `0 4px` | n/a | n/a | n/a |
| **Nav row** | `--ink` label, icon left, optional badge right | `--surface` fill | `--surface` fill + `--ink` at full weight | label `--ink-eyebrow` at **5.27:1** on `--surface`, no fill |
| **Table row** | `--ink` link title, `--ink-soft` slug beneath, right-aligned numerics | row tints to `--surface` | n/a | n/a |
| **Loader** | **none, and here is why.** The reference has no skeleton and no spinner anywhere in the product; every surface renders with its last value and a freshness stamp. That is the pack's position and it is deliberate — see Micro-interactions | | | |
| **Empty state** | the day cell keeps its border and renders nothing inside — the grid's rhythm survives the absence | n/a | n/a | n/a |
| **Input** | **not specified.** The reference's forms are Intergalactic's and were not read in this pass; a pack that invented them would be inventing values with a citation attached | | | |

- **Disabled is a token pair, not an opacity.** WCAG 1.4.3 exempts an inactive
  control from its minimum, and that exemption is the reason most packs reach for
  `opacity: 0.38`. Composited the way a browser does it, that lands a shade
  under 2:1 — the palette gate computes it and refuses it — and it makes the
  control unidentifiable rather than merely inactive. This pack names a pair
  instead, and `--ink-eyebrow` on `--surface-2` is 4.40:1, so a disabled control
  still reads as the control it is.

## Hero

The opening viewport is a **datasheet hero, centred**: a floating pill nav, then a
68px headline with exactly one accent word, a two-line lede, two CTAs side by side,
and a one-line social-proof figure under them.

- **Line ceiling: two**, at 68px and 1.2 leading — measured off the served page,
  where the headline breaks after *"Traffic"* and the second line carries the
  accent word.
- **Two CTAs is one job, not two.** `Join with Google` (ghost) and `Get Started for
  Free` (filled) both begin the same signup; the ghost is a lower-friction door to
  the identical outcome. This is not a second primary action competing with the
  first, and reading it as one is how an audit flags a pattern that works.

## Responsive

- **Breakpoints** 640 / 768 / 1024 / 1280px — Tailwind's own, unchanged.
- **Container queries** for the dashboard card and the metric strip:
  `container-type: inline-size`, because both are dropped into a main column whose
  width depends on whether the 321px rail is open, not on the viewport.
- The rail collapses to icons below 1024 and to a sheet below 768.
- The landing's section padding steps `80px` top / `120px` foot on desktop and
  halves below 768.

## Motion tokens

- Ease `cubic-bezier(0.4, 0, 0.2, 1)` — Tailwind's default, and the one curve.
- `--dur-press` 0.15s, `--dur-fast` 0.15s, `--dur-base` 0.2s. All three are inside
  `MOTION_DOCTRINE.md` §3's bands and all three collapse under reduce.
- **There is nothing else.** No scroll-linked animation, no parallax, no scrub, no
  entrance reveal. Measured across a 20 806px landing page and four product routes.

## Signature motifs

1. **The 5px ring** on the primary button — a border wearing a halo's job.
2. **The accent word** — exactly one word of the headline in `--accent`.
3. **The tinted metric strip** — four cards, each a different hue wash, where the
   tint encodes the *category* and never the status.
4. **The freshness stamp** — a data surface ends with *"Updated 11 minutes ago"*.
5. **The 100% bar with a dot legend** — one horizontal bar split by source, with
   colour-dot + label + count beneath it, in place of a pie.

## Signature element

**The recommended-actions block.** A card headed by a title and a count badge, one
line of purpose, then two suggestion tiles on `--accent-wash` with an icon, a
title, three lines of body and a text-link CTA with a trailing arrow. It is the
one element that makes the product feel like it is working on your behalf, and it
sits above every metric on the page.

## Micro-interactions

- Button press: `scale(0.95)` over `--dur-press`, measured.
- Nav row hover: `--surface` fill over `--dur-fast`, no movement.
- Table sort: the arrow flips; the rows do not animate.
- **The freshness stamp instead of a spinner.** The reference never blanks a
  surface it has already drawn: it keeps the last value and dates it. A pack that
  adds a skeleton here is adding a flicker the design deliberately does not have.
- `focus-visible`: 2px `--accent` ring at 2px offset. **Not** the 5px decorative
  ring, which is ruled out for the job at 1.72:1 on `--bg` — decoration, not an
  affordance.

## Bans

- **No shadow on a resting surface.** Elevation is the hairline; a shadow means an
  overlay.
- **No status colour on a word.** `--info`, `--success`, `--danger` and
  `--warning` are fills and dots; the `-ink` pair carries text.
- **Status is never by colour alone.** Every state in this pack carries a word or
  an icon beside the hue — which is what the reference does: its category chips
  are iconned, its wins feed is checked, its at-risk rows are flagged. Measured
  under simulated CVD, `--info` and `--success` separate by only 6.9 under
  tritanopia and `--accent` and `--info` by 2.9 under deuteranopia, so the hue is
  the second signal here and never the first.
- **No second brand hue.** One violet. The status four are states, not brand.
- **No skeleton, no spinner** on a surface that has a previous value — stamp it.
- **No serif, anywhere.** Two sans families and no third.
- **No scroll-driven motion.** This pack's ceiling is 2 and its budget is a colour
  transition.

## Gotchas

- **[CORRECTION] The reference ships no `prefers-reduced-motion` branch at all.**
  Its whole budget is a 0.15s colour transition, so the omission costs a reader
  little — but this pack requires the branch, and collapsing three durations costs
  the design nothing.
- **The eyebrow fails AA on the field it appears on most.** `#64748B` is 4.76:1 on
  white and refused at **4.37:1 on `--surface`**, at 13px. Corrected to `#5B6779`.
- **The brand violet does not survive the dark theme.** `#882AFF` on the dark card
  is **2.88:1**. The dark twin uses the reference's own `--violet-400` `#AB6CFE` at
  4.76:1 — taken from its scale rather than invented.
- **The warning hue misses even the non-text floor.** `#FF642D` is 2.95:1 on white.
  Corrected to `#C2740A` — an amber at 3.62:1, and the second defect is the
  sharper one: at `#E5511B` the warning sits **7.2 OKLab from `--danger`** against
  a hard floor of 10.0, so red and orange are one state to a reader who cannot
  separate them. The amber is 15.2 away, and it is also the conventional warning
  encoding, so the separation and the convention agree.
- **Do not copy the Intergalactic token names.** They are Semrush's, 384 of them,
  and adopting the vocabulary means adopting the system. This pack states the
  values in its own role names; where you want the system, install the system.
- **The landing is 20 806px tall.** Fourteen sections, and the hero's promise is
  repeated verbatim as the closing CTA. Treat the length as a measurement of what
  this category's buyers read, not as a target.
