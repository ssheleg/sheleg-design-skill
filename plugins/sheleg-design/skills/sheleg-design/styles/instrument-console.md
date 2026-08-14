# Style pack — Instrument Console

Origin: Nicegram Business OS landing (the SHELEG reference implementation).
A near-black aerospace console: deep layered surfaces, hairline seams, one
electric-blue signal accent, mono telemetry labels. The particle field and
every instrument read as one precision device responding to the hand.

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

Choose this pack for technical, systems, infra, or "operating system"
products where the aesthetic is calm precision hardware. Single dark
register across landing and app; brightness (energy) varies per scene, hue
does not.

**Not for:** a developer marketing page on light paper whose argument is a code
sample — [`manpage`](./manpage.md). A console persuades by looking like the
running system; that pack persuades by looking like the documentation.

**The fork against [`maquette`](./maquette.md), which is the one people get
wrong.** Both are near-black with one pale accent, mono labels and an
enterprise-infrastructure buyer; on product *category* they overlap completely,
so a keyword match sends every infra brief here. The test is not the category —
it is what the page has to render. **Does it show a number that changes while
the reader watches?** A dial, a stream, request rates, saturation, an error
budget → this pack: the single signal, the scrubbed telemetry and the progress
rail exist to make a moving value readable. Nothing moves, but the reader has to
decompose a structure before they can judge it → `maquette`, whose subject is a
static axonometric model. **A cockpit answers *what is happening now*; a maquette
answers *what is this made of*.**

### Against [`datasheet`](./datasheet.md)

Both put an instrument at the centre of the page, and the difference is which way
round the page and the instrument sit. This pack is the cockpit: the field is dark
throughout, and the one electric accent exists to make a value readable **while it
changes**. `datasheet` is paper with a single instrument set into it, and its
readings are already settled — a verdict about a visit that has happened. If the
number ticks while the reader watches, it belongs here. If it is a result, it
belongs there. That pack does ship a dark surface, but as an alarm state on the
instrument alone, never as the page's field.

### Against [`paperclip`](./paperclip.md)

Both are near-black pages about machines doing work, and the test is **what the
colour is for**. Here the one electric accent is functional: it marks the live
value, the threshold, the trace the reader is meant to follow. In `paperclip`
nothing coloured can be clicked — the whole chromatic budget is spent on an
ornament the copy sits on top of, and every control, card and readout is
monochrome. Ask what happens if you delete every colour from the page: this pack
loses its meaning, that one loses only its poster.

## Palette

Ready-made token layer: [`tokens/instrument-console.css`](./tokens/instrument-console.css)
— copy it verbatim instead of transcribing this table.

**This table declares its base**, which until 1.16.0 it did not — and the
consequence was not cosmetic: `validate_stated_ratios` reads the base out of a
table header, so with none declared, **not one of this pack's per-token ratios
was gate-covered.** The library's default dark infrastructure pack was its least
checked. Every number below is now recomputed from `tokens/instrument-console.css`
on each run.

| Token | Value | Role | On `--base` |
|---|---|---|---|
| `--base` | `#05070a` | page field (near-black) | — |
| `--surface-1` / `-2` / `-3` | `#0a0e14` / `#10151d` / `#161c26` | ascending raised panels | 1.04 / 1.10 / 1.18 — steps, not contrast |
| `--hairline` / `-strong` | `#1e2630` / `#2b3542` | panel seams, rules | 1.32 / 1.62 — rules, never text |
| `--ink` | `#eef2f7` | primary text | **17.94:1** |
| `--ink-muted` | `#9aa7b6` | secondary text | **8.24:1** |
| `--ink-faint` | `#5f6b7a` | captions — see Gotchas | 3.72:1 |
| `--accent` | `#3392ff` | THE electric-blue signal (CTA, links, particles) | **6.43:1** |
| `--accent-dim` | `#1f5fb0` | pressed signal | 3.19:1 — a fill, not a label |
| `--accent-bright` | `#6bb3ff` | highlighted signal | **9.14:1** |
| `--accent-ink` | `#0a0e14` | text **on** the accent — 6.17:1 there; white on `#3392ff` is 3.14 and fails | 1.04 |
| `--accent-glow` | `rgba(51,146,255,0.18)` | the only permitted glow | — |
| `--ok` / `--warn` | `#46d39a` / `#e0a030` | status semantics only | **10.61:1** / **8.87:1** |

The particle field, progress rail, and all instruments are tinted with
`--accent` only — energy per scene changes brightness, never hue.

## Type

- Display + body: **Geist Sans** (or an equivalent neutral grotesk) —
  weight 600 headlines, clamp-scaled (hero ~5.25rem ceiling), tight but
  not tracked-negative.
- Data: **Geist Mono** (or ui-monospace) — telemetry eyebrows, numeric
  readouts, section indices ("02 / CONTROL"), code.
- Two families; mono is a signature, not a garnish — every label that
  narrates system state is mono.

## Texture & surface

- Flat panels separated by 1px hairlines; radii 4 / 8 / 14px (+ pill) —
  machined, not squircle.
- Elevation via surface steps (`--surface-1..3`), not shadows; the single
  glow `0 0 0 1px rgba(51,146,255,0.4), 0 8px 30px rgba(51,146,255,0.18)`
  is reserved for the active signal element.
- No grain, no blur; darkness itself is the texture.

## Motion tokens

- Ease `cubic-bezier(0.16, 1, 0.3, 1)` — the one site-wide curve
  (the SHELEG default token set: 0.18 / 0.32 / 0.55 / 0.8s, stagger 0.07).
- Section rhythm `clamp(9rem, 24vh, 20rem)` vertical padding.

## Signature motifs

- WebGL particle formations as the narrative backdrop (SCENES registry),
  electric-blue, hold-then-redeploy per the SHELEG core.
- Right-edge progress rail with act markers; nav act badge ("02 /
  CONTROL") driven by the coarse store subscription.
- Frame/HUD chrome: thin viewport frame, corner ticks, scan/dim of
  off-band sections (attention spotlight).
- Scrubbed SVG instruments (charts, step flows) drawn hairline-thin with
  mono annotations.

## Motion flavor

How this pack rides the SHELEG motion layer:

- Particle field: single-hue `--accent` tint; SCENES `energy` 0.45–0.7,
  climax only reaching 1.0; formations lean geometric (frame, lattice,
  orbit, constellation, glyph).
- Reveal set: full act-themed range — Scatter (problem acts), Lock
  (control/system acts), Clip (headlines/panels), Pulse (climax).
- Instruments: hairline-thin scrubbed SVG with mono annotations; progress
  rail and act badge are first-class chrome.

## Micro-interactions

- Buttons: surface-step + accent fill on primary; press = 1 shade dimmer
  (`--accent-dim`), no bounce.
- Reveal primitives themed per act: Scatter (drift+blur resolve), Lock
  (snap into slot), Clip (mechanical wipe), Pulse (lock acquired).
- Focus-visible: 1px `--accent` ring + `--accent-glow` halo.

## Bans

- Status carried by hue alone. Success, warning, danger and info always
  ship with an icon or a word beside the fill — **status is never by
  colour alone**. Measured off a production reference, several of these
  pairs sit inside a dichromat's confusion line; re-stepping them would
  invent a colour this pack does not own, so the second signal carries
  the meaning instead.
- One accent hue — no second color except `--ok`/`--warn` status semantics.
- No gradient text, no glassmorphism/backdrop blur, no purple/neon
  rainbow, no colored shadows besides `--accent-glow`.
- No light sections — contrast comes from surface steps, not inversion.
- No decorative serif/display fonts; the console voice is grotesk + mono.

## Gotchas

- Glow discipline: `--accent-glow` on more than one element per viewport
  destroys the "single signal" read — the page becomes a christmas tree.
- Dark UIs hide low-contrast text: `--ink-faint` is for captions only,
  never sustained reading (fails 4.5:1 on `--surface-1`).
