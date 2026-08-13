# Style pack — Editorial Luxury

Origin: prowl.chat (production). Warm cream field, espresso ink, one
functional sage-green accent, terracotta as a rare editorial highlight,
classified-red reserved for negatives only. "Design *is* the product" on
public pages; quiet and fast inside the app. Dossier/editorial DNA:
hairline rules, eyebrow labels, stamp/seal motifs, mono data, authored
artifact previews instead of icon cards.

Contract: core — this pack does **not** specify `## Components`, `## Hero`,
`## Responsive` or `## Signature element`. Per-component states (hover,
active, disabled), the opening viewport and its line ceiling, the collapse
rules, and the single element the page is remembered by are **yours to
decide** here, and you must say so out loud when you do. Everything the pack
*does* state is measured; the precision of that half is not evidence about
this half. The backfill is held rather than written from the token layer,
because filling these sections from tokens would be inventing values with a
citation attached — which is the one thing this pack layer exists to prevent.

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
| `--accent-weak` / `-med` | `rgba(63,125,95,0.12)` / `…0.34` | accent tint fill / accent hairline |
| `--accent-ink` | `#fbf6ec` | text **on** the accent — 6.93:1 over `--accent-deep`; 4.52:1 over `--accent`, which clears AA by 0.02, so large text only there |
| `--accent-on-dark` | `#9fd9bc` | the accent brightened for espresso sections |
| `--terra` | `#b5623f` | rare editorial highlight only |
| `--red` | `#a83a2b` | negatives ONLY (comparison "without") |
| `--status-ok` | `#2f5e47` | healthy / active / done — **= `--accent-deep`**, not a new hue |
| `--status-warn` | `#7d5416` | a human is needed, and nothing else |
| `--status-info` | `#2f5c7d` | running / working |
| `--status-danger` | `#a83a2b` | failed — **= `--red`**, unchanged |
| each `-weak` | `rgba(…, 0.12)` of its own hue | chip and banner fill; the status **word** on top is `--ink` |
| `--hair` / `-strong` | `rgba(36,28,20,0.13)` / `rgba(36,28,20,0.22)` | hairline rules |

Contrast: body on cream must clear 4.5:1 — `--ink` / `--ink-soft`, never
`--ink-faint` for sustained reading. On espresso, text is `--cream` and the
sage accent switches to `--accent-on-dark`.

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
  site-wide curve, **overriding** the SHELEG default `cubic-bezier(0.16, 1,
  0.3, 1)`; the pack wins, per SHELEG_DESIGN §10.
- Spring `cubic-bezier(0.32, 0.72, 0, 1)` — press/magnetic feedback only.
- Base duration `0.7s` for brand-register reveals; product register stays in
  the SHELEG fast/base range (≤0.32s), and that range now ships as values rather
  than as a sentence: `--dur-hover` `0.12s` for a paint-only hover, `--dur-state`
  `0.18s` for a state change. Prose-only, every product surface built on this
  pack typed `0.15s` literals — there was nothing to reference.

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

- **The status set is four colours and no more, and three of them already
  existed.** This pack shipped one semantic colour, `--red`, and told any surface
  needing a full set to close the gap *in the pack, deliberately, not at the
  keyboard*. It was closed on 2026-08-13, and what closed it is the evidence for
  why the instruction was worth writing: an admin console had invented
  amber-as-warning and cyan-as-info on top of an amber that was also its entire
  chrome — so the hue meaning "a provider is backing up" was the hue of every
  button on the page, and seven of its pairs sat below AA with three under
  1.1:1. `--status-ok` is `--accent-deep` unchanged, `--status-danger` is `--red`
  unchanged, and only `--status-warn` and `--status-info` are new values, each
  the existing amber and cyan family deepened until it clears **4.5:1 on all
  three grounds this pack renders on** — `--paper`, `--paper-2` and `--paper-3`.
  Two grounds would have been the same enumerated-list hole one level down.
  Status is still **never by colour alone**: the tint carries the colour, the
  word carries the meaning in `--ink` (11.8:1 on every tint).
  *(Corrected 2026-08-10: this bullet was copy-pasted into six of the twelve and
  claimed a measurement across "several pairs" that one colour cannot form.)*
- No gradient text, no glassmorphism, no neon/outer-glow shadows, no purple.
- **No decorative accent stripe on a card** — the full-height rule down the side of a
  panel, in the accent, carrying no state and no semantic role, put there to make the
  card look designed. That is the ornament this list is about, and its neighbours above
  are the same kind of thing.
  *(Narrowed 2026-08-13, and narrowed because the bare wording "no side-stripe accent
  borders" was measured against a real consumer and found to ban the wrong thing.* A
  production app on this pack had **42** `border-left` rules, and reading them one by one
  is what settled it: four are 1px hairlines on code blocks and TOC drawers — not accents
  at all; three are `transparent`, reserving the gutter for a **selected-state** marker;
  the rest are 2–3px rules on TEXT BLOCKS — blockquotes, callouts, toasts, notices, log
  entries — which is the oldest editorial device there is, and a pack whose display face
  is Fraunces and whose field is cream paper has no business banning it. A guard written
  to the literal reading failed on all 42, and a gate nobody can satisfy is a gate that
  gets bypassed. **The line to hold:** a stripe must mean something — state, severity, or
  "this block is quoted" — and must never be drawn in a colour nobody chose.)*
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
