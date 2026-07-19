# Style pack — Instrument Console

Origin: Nicegram Business OS landing (the SHELEG reference implementation).
A near-black aerospace console: deep layered surfaces, hairline seams, one
electric-blue signal accent, mono telemetry labels. The particle field and
every instrument read as one precision device responding to the hand.

## Register

Choose this pack for technical, systems, infra, or "operating system"
products where the aesthetic is calm precision hardware. Single dark
register across landing and app; brightness (energy) varies per scene, hue
does not.

## Palette

| Token | Value | Role |
|---|---|---|
| `--base` | `#05070a` | page field (near-black) |
| `--surface-1/2/3` | `#0a0e14` / `#10151d` / `#161c26` | ascending raised panels |
| `--hairline` / `-strong` | `#1e2630` / `#2b3542` | panel seams, rules |
| `--ink` | `#eef2f7` | primary text |
| `--ink-muted` / `-faint` | `#9aa7b6` / `#5f6b7a` | secondary / captions |
| `--accent` | `#3392ff` | THE electric-blue signal (CTA, links, particles) |
| `--accent-dim` / `-bright` | `#1f5fb0` / `#6bb3ff` | pressed / highlighted signal |
| `--accent-glow` | `rgba(51,146,255,0.18)` | the only permitted glow |
| `--ok` / `--warn` | `#46d39a` / `#e0a030` | status semantics only |

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

## Micro-interactions

- Buttons: surface-step + accent fill on primary; press = 1 shade dimmer
  (`--accent-dim`), no bounce.
- Reveal primitives themed per act: Scatter (drift+blur resolve), Lock
  (snap into slot), Clip (mechanical wipe), Pulse (lock acquired).
- Focus-visible: 1px `--accent` ring + `--accent-glow` halo.

## Bans

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
