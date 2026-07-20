# Style pack — Editorial Luxury

Origin: prowl.chat (production). Warm cream field, espresso ink, one
functional sage-green accent, terracotta as a rare editorial highlight,
classified-red reserved for negatives only. "Design *is* the product" on
public pages; quiet and fast inside the app. Dossier/editorial DNA:
hairline rules, eyebrow labels, stamp/seal motifs, mono data, authored
artifact previews instead of icon cards.

## Register

Choose this pack for warm, editorial, print-inspired products: research /
intelligence tools, content products, premium B2B. Two registers:
**brand** (landing, use-case, legal, shared pages — cinematic, editorial)
and **product** (authenticated app — quiet micro-interactions only, never
cinematic noise).

## Palette

Ready-made token layer: [`tokens/editorial-luxury.css`](./tokens/editorial-luxury.css)
— copy it verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--paper` | `#fbf6ec` | primary cream field |
| `--paper-2` | `#f3ead9` | raised card on cream |
| `--paper-3` | `#ece0cb` | deeper inset |
| `--espresso` | `#1b150e` | dark section field |
| `--espresso-2` | `#241c12` | raised card on espresso |
| `--cream` | `#f4ecdc` | ink on espresso |
| `--ink` / `-soft` / `-faint` | `#241c14` / `#5b4f3d` / `#8a7c64` | text ramp on cream |
| `--accent` (sage) / `-deep` | `#3f7d5f` / `#2f5e47` | THE single functional accent (links, CTA, "signal") |
| `--terra` | `#b5623f` | rare editorial highlight only |
| `--red` | `#a83a2b` | negatives ONLY (comparison "without") |
| `--hair` / `-strong` | `rgba(36,28,20,0.13)` / `rgba(36,28,20,0.22)` | hairline rules |

Contrast: body on cream must clear 4.5:1 — `--ink` / `--ink-soft`, never
`--ink-faint` for sustained reading. On espresso, text is `--cream` and the
sage accent brightens to `#9fd9bc`.

## Type

- Display: **Fraunces** — oversized, optical, tracked `-0.02…-0.03em`, hero
  ceiling ~7rem via clamp.
- Body: **Newsreader** — relaxed, measure ≤66ch.
- Mono: **JetBrains Mono** — eyebrows, labels, numbers, code, "signal" tags.
- Three families, no more; hierarchy through scale + weight.

## Texture & surface

- Fixed warm radial field + ~4% film-grain multiply overlay (cheap, no blur).
- Squircle radii 14 / 22 / 30px; double-bezel cards
  (`inset 0 1px 0 rgba(255,251,242,0.7)` highlight).
- Soft ambient elevation only (`0 18px 50px -28px rgba(36,28,20,0.30)`
  scale); no harsh dark drops, no outer glows on buttons.

## Motion tokens

- Ease `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out-expo feel) — the one
  site-wide curve for the SHELEG token set.
- Spring `cubic-bezier(0.32, 0.72, 0, 1)` — press/magnetic feedback only.
- Base duration `0.7s` for brand-register reveals; product register stays in
  the SHELEG fast/base range (≤0.32s).

## Signature motifs

- A recurring sage **"signal"** motif travels the narrative: raw inputs →
  pipeline → synthesized deliverable. One story, one color.
- **Authored artifact previews** instead of flat icon cards: composed mock
  report/infographic/PDF/PPTX/video frames that assemble on scroll.
- Dossier primitives: `.dossier-card`, hairline `.rule`, `.eyebrow`,
  `.stamp`, `.data-table`, tabular-nums data, footnote captions.
- Visualization rule (key contract): all data-viz animation is **CSS-driven
  off a `.revealed` ancestor** (bars `scaleX/Y`, sparklines/donuts via
  `stroke-dashoffset`) — identical in plain and cinematic reveal paths,
  correct static final state under reduced-motion, **fail-open** if JS/CDN
  dies (content always visible).

## Motion flavor

How this pack rides the SHELEG motion layer (brand register only):

- Reveals: 0.7s base with the pack ease; word-by-word title lighting and
  `.reveal` sections; every reveal is fail-open (final state visible
  without JS).
- The sage "signal" motif is the scroll narrative: it travels raw inputs →
  pipeline → deliverable; scrubbed instruments draw with it.
- Particle field is optional here — if used, tint sage, low density, low
  energy (≤0.6); artifact mock previews assembling on scroll are the
  preferred spectacle.
- Product register: SHELEG fast/base durations only, no cinematic motion.

## Micro-interactions

- Buttons: tactile `translateY(-2px)` + spring; no glow.
- Magnetic primary CTAs and a small sage cursor-ring accent — desktop +
  fine pointer only, gated with the SHELEG degrade rules.
- Focus-visible: 2px sage outline, offset 3px (brightened on espresso).
- Cards lift + border warms on hover; never nested-card-in-card.

## Bans

- No gradient text, no side-stripe accent borders, no glassmorphism, no
  neon/outer-glow shadows, no purple.
- No emojis in product UI; no Inter/system display fonts (Fraunces owns
  display).
- Never flatten the cream identity into generic white; never let motion
  gate content visibility.

## Gotchas

- Token-first re-skin: override the token layer in `:root`, map legacy
  token names onto it — do NOT restyle components one by one.
- After any theme/token migration, **sweep hardcoded literals** (hex/rgba
  left in CSS/JS keep the old palette and read as inverted on the new
  theme).
