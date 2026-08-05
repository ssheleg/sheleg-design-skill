# Instrument Console — the contract this design system ships under

**Register.** Choose Instrument Console for **technical, systems, infra or
"operating system" products** where the aesthetic is calm precision hardware:
deep layered near-black surfaces, hairline seams, one electric-blue signal, mono
telemetry labels. There is a **single dark register** — no light twin, no
`[data-theme]` switch, no inverted section. Brightness (energy) varies per scene;
hue does not. Elevation is a surface step (`--surface-1` → `--surface-3`) plus a
1px `--hairline`, never a shadow, and darkness itself is the texture: no grain,
no blur.

**The accent rule.** There is exactly one accent hue (`--accent`, electric blue)
and it carries the CTA, links and the active signal. Text **on** the accent is
`--accent-ink` — white on `#3392ff` fails AA, so a light label there is a defect,
not a taste call. `--accent-bright` is the highlighted signal (hover) and
`--accent-dim` is the pressed one; press is one shade dimmer with no bounce.
`--accent-glow` is the only permitted glow, and glow on more than one element per
viewport destroys the single-signal read — this kit spends it on `:focus-visible`
alone. `--ok` and `--warn` are status semantics only, never decoration, and
`--ink-faint` is for captions and tick marks, never sustained reading.

**Bans** (verbatim from the pack):

- One accent hue — no second color except `--ok`/`--warn` status semantics.
- No gradient text, no glassmorphism/backdrop blur, no purple/neon
  rainbow, no colored shadows besides `--accent-glow`.
- No light sections — contrast comes from surface steps, not inversion.
- No decorative serif/display fonts; the console voice is grotesk + mono.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, so the particle field, the scrubbed SVG instruments, the
scroll-driven rail and every act-themed reveal stay behind in the pack.
