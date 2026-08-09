# Prism — the contract this design system ships under

**Register.** Choose Prism for an **open-source infrastructure project's front
door** — the page a developer reaches from a README, where they want the install
line, the numbers and the architecture in that order. The fork people get wrong
is against `cyclorama`: that pack's field *breathes* (six stops on a 32-second
loop, typewriter serif) because its subject is a change of state; this field
*holds* (one static wash, heavy grotesque) because its subject is software that
is ready now. Against `maquette`: same company, two faces — if the next action is
`pip install`, this pack; if it is a demo call, that one. Build every screen
against `var(--…)` and never a literal.

**The body is mono, and that inversion is the pack.** Geist sets the display;
Geist Mono sets paragraphs, ledes, labels, tables and commands. Setting a
paragraph in Geist turns the project page into a company page. Mono needs more
leading than a grotesque — 1.65 for body, 1.7 for the lede — and a tighter
measure: **60 characters, not 75**, because monospace runs wide.

**The accent is a fill, not a text colour.** `--accent` `#00B3FF` measures
**2.36:1** on white; the reference sets 72px display type in it and that fails
even the relaxed large-text floor. Accent-coloured display text takes
`--accent-ink` `#1493CC` at 3.4:1, large only, never below 24px. Ink on the
accent is 8.02:1, which is what `--on-accent` is for.

**The wash is spent once, at the top, with a hard bottom edge** — and it never
animates. A second gradient anywhere is the fastest way to turn this pack into a
generic AI landing page. The four stops sit above 18:1 against `--ink`, so a
headline over them needs no scrim; deepen them and you will need one you should
not need.

**Status is never by colour alone.** `--warning` and `--danger` are two warm reds
**11.3 apart** at full colour. Every status carries its word.

**Bans** (verbatim from the pack):

- `--accent` as body text; anything below 24px in `--accent-ink`.
- A second gradient, anywhere; animating the wash.
- A drop shadow; a lifted card; a glow.
- A sans-serif body.
- Mono paragraphs longer than 60 characters, or mono set at 1.5 leading.
- A status mark without its word.
- `--ink-faint` as text; a third font family.
- Fluid `clamp()` type; `transition: all`; `100vh`; a scroll listener.
- Burying the install line below the fold.

**The reference ships no `prefers-reduced-motion` branch at all.** This system
requires it.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack.
