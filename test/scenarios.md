# Release test scenarios (run with subagents before every release)

TDD-for-docs harness (superpowers:writing-skills). Each scenario runs as a
fresh single-shot subagent. Any edit to SKILL.md, a style pack, or the
reference requires re-running the affected scenarios; a description edit
requires the full trigger set.

## T1 — Trigger set (discovery)

Give the agent a 5-skill description list (sheleg-design + frontend-design,
dataviz, webgl-performance, copywriting distractors) and tasks; answer =
skill names only.

MUST load sheleg-design: particle-hero landing; WebGL hero upgrade;
scroll-narrative storyboard; "landing janky / layers out of sync";
RU «кинематографичный лендинг с частицами»; quiet-light dashboard styling;
admin design tokens light/dark; RU «спокойный светлый интерфейс для
внутреннего инструмента».
MUST NOT load: charts-only dashboard build (dataviz), pricing-table
redesign, three.js FPS drop, copywriting headline.

Pass: 0 misses / 0 false loads across the set.

## T2 — Application (motion architecture)

"Design the motion architecture for a cinematic scroll landing (particles,
parallax, scrubbed chart, rail); junior-ready plan." + "FILES I READ".

Pass: agent reads SKILL.md AND SHELEG_DESIGN.md; plan has the layer order,
SCENES-as-data, hold-then-morph specifics, fallback-in-same-commit,
verification step.

## T3 — Retrieval (reference depth)

Ask for exact morph math + timing, the GSAP scrub recipe, and the perf
budget. Pass: HOLD 0.82, smoothstep + per-point arc stagger (spread 0.5,
chase 0.028/±0.04), ease:'none' + pathLength={1} + kill-on-cleanup,
936 particles / DPR [1,1.75] — quoted, not invented.

## T4 — Style request by name

"Build the landing in the prowl / editorial-luxury style; exact tokens,
fonts, motion values, bans." Pass: values verbatim from
styles/editorial-luxury.md (#fbf6ec, #3f7d5f, Fraunces/Newsreader/JetBrains
Mono, ease 0.22,1,0.36,1) + "SOURCE OF VALUES: from skill files".

## T5 — Style self-selection

"Dark, precise, mission-control landing for infra product — which
direction + exact values?" Pass: agent picks instrument-console from the
SKILL.md table and quotes its values (#05070a, #3392ff, Geist, ease
0.16,1,0.3,1).

## T6 — Product-UI routing (standalone pack)

"Quiet light GitHub-like admin/dashboard styling — exact tokens, fonts,
surfaces, interaction states." Pass: agent routes to styles/workbench.md
standalone (no cinematic motion), quotes light+dark tokens verbatim,
references the ready-made tokens css.

## Historical baselines (why these exist)

- Pre-0.4.0: T4 baseline invented plausible-but-wrong tokens
  (#F6F1E7/bronze) — packs added.
- Pre-0.5.0: T6 baseline declared the skill out of scope and invented
  Primer-like values — workbench pack + routing added.
- Pre-0.6.0: dashboard trigger probe missed 3/3 — description gained
  product-UI triggers.
