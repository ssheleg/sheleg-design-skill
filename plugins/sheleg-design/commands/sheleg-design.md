---
description: Apply the SHELEG Design methodology (single-clock, layered, degrade-to-calm motion) to the current landing-page / hero / scroll-animation task
argument-hint: [what to build or upgrade]
---

Invoke the `sheleg-design` skill and apply it to the current request.

- Read the skill's SKILL.md, then its full reference `SHELEG_DESIGN.md`
  (same directory) before designing anything.
- Task: $ARGUMENTS — if empty, ask what page or section to build/upgrade,
  then proceed per the skill's "How to Apply" order. If the arguments name
  a style pack (instrument-console | editorial-luxury | workbench), use
  that pack without re-asking; otherwise pick per the SKILL.md table.
- Follow the skill's non-negotiables (Quick Reference table) and ship every
  layer's reduced-motion/fallback branch in the same commit.
