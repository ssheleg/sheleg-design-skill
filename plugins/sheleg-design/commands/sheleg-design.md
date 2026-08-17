---
description: Apply the SHELEG Design methodology (single-clock, layered, degrade-to-calm motion) to the current landing-page / hero / scroll-animation task — or its style packs to product UI (dashboards, admin, internal tools)
argument-hint: "[what to build or upgrade]"
---

Invoke the `sheleg-design` skill and apply it to the current request.

- Read the skill's `SKILL.md` first, then — **before designing anything** — its
  full reference `SHELEG_DESIGN.md` and, **before any animation**,
  `MOTION_DOCTRINE.md` (same directory). `SHELEG_DESIGN.md` says how motion is
  built; the doctrine says whether to build it at all. Skipping the second is
  how a keyboard path ends up animated.
- Task: $ARGUMENTS — if empty, ask what page or section to build/upgrade.
- **If the arguments name a style pack, use that pack without re-asking.** The
  twenty-nine are `instrument-console`, `editorial-luxury`, `workbench`,
  `briefing-room`, `atrium`, `orchard`, `field-notes`, `cyclorama`, `showroom`,
  `blueprint`, `prism`, `maquette`, `scoreboard`, `datasheet`, `manpage`, `pigeonhole`, `roster`, `ora`, `tenor`, `paperclip`, `ledger`, `awning`, `router`, `daylight`, `notation`, `almanac`, `vitrine`, `proscenium`, `bulletin`. Otherwise pick per the `SKILL.md` table,
  and say which pack you picked and why before you build.
- **Set the three dials out loud before any layout exists** — `DESIGN_VARIANCE`,
  `MOTION_INTENSITY`, `VISUAL_DENSITY`, with one line of reasoning. The
  `SKILL.md` "Reading them off the brief" table gives the starting values;
  baseline is `7 / 5 / 4`. Announcing them and then drifting is the failure this
  step exists to prevent.
- Then proceed per the skill's "How to Apply" order.
- Product UI (dashboard, admin, internal/dev tool, design tokens, theming):
  apply a **standalone** pack and its token CSS — no scroll clock, no particle
  field, no cinematic motion. `workbench` is the default; `field-notes` is the
  fork for a developer product sold on auditability, and `briefing-room` for a
  deck published as a page. The packs state the distinction; read it rather than
  defaulting.
- AI surfaces (chat, agent runs, streaming, generated content): read
  `AI_PRODUCT_PATTERNS.md` as well.
- Follow the skill's non-negotiables (Quick Reference table) and ship every
  layer's reduced-motion/fallback branch in the same commit.
