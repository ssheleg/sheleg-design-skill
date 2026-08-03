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
Russian-language phrasing of "cinematic particle landing"
(«кинематографичный лендинг с частицами»); quiet-light dashboard styling;
admin design tokens light/dark; Russian phrasing of "calm light UI for an
internal tool" («спокойный светлый интерфейс для внутреннего инструмента»).
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

## T7 — Authoring a new pack (contract, not improvisation)

"We need a SHELEG style pack for a warm, high-contrast fintech console —
author it." Pass: agent copies `styles/STYLE_PACK_TEMPLATE.md`, keeps all
ten headings (Register → Gotchas), authors `styles/tokens/<name>.css` in the
same change, states the origin of the values, and does NOT invent tokens
inline in components. Fail: pack written from memory, missing headings, or
no token CSS.

## T8 — Figma direction (the border)

Two prompts, one pass each. (a) "Publish the workbench pack into Figma as
variables." Pass: agent reads `FIGMA_BRIDGE.md`, produces one collection per
token family with names 1:1 to the CSS properties, and puts light+dark as **two
modes of one collection**; states that motion tokens cannot cross. Fail: two
collections for the themes, invented variable names, or a promise to publish the
ease. (b) "Here is a Figma screen — build it with our design system." Pass:
values mapped onto pack tokens, any unmatched value called out as a pack gap or
file drift, no raw hexes inlined, pack bans still enforced.

## T9 — AI product surface (honest state)

"Design the UI for our agent that edits files and sends emails on the user's
behalf — states, streaming, errors, confirmations." Pass: agent reads
`AI_PRODUCT_PATTERNS.md`; produces five states (not two), streams instead of
spinning with a stop control, separates refusal / rate limit / crash, shows the
action in the shape it will take before running it, requires explicit
confirmation for send and offers undo for cheap reversible work, and uses
workbench status tokens. Fail: one red error state, a spinner, an invented
confidence score, or auto-send.

## T10 — Deck register (the fourth pack)

"Build our seed pitch deck as a web page." Pass: agent routes to
`styles/briefing-room.md`, quotes its tokens verbatim (`oklch(0.045 0.008 254)`
field, `oklch(0.643 0.195 254)` accent, Inter + JetBrains Mono at `+0.14em`),
builds fixed 1280×720 frames with mono numbered headers, writes each slide
title as a **claim** rather than a label, replaces bullet lists with one
diagram per slide, and ships no slide transitions. Fail: bullets, a second
accent, animated builds, or an unsourced number.

## T11 — Consumer-health register (the fifth pack)

"Build the marketing site for our at-home blood-testing subscription." Pass:
agent routes to `styles/atrium.md`, quotes its tokens verbatim (`#FEF9EF`
field, `#B05A36` accent, Financier Display at weight 300 with `line-height:
0.9`, a flat `1.5` on every sans size), keeps **one continuous field** with no
dark section used as rhythm, emphasizes with a single italic accent phrase per
heading rather than bold, makes every control a `999px` pill, and ships a
visible `PAUSE MOTION` control beside any marquee or autoplaying hero plus the
still-image fallback for `prefers-reduced-motion`. Fail: alternating light/dark
bands, a second accent, green or blue as text, `transition: all`, an autoplaying
marquee with no off switch, or an unsourced health claim.

## T12 — Consumer register, the friendly half (pack disambiguation)

"Build the landing page for our at-home gut-testing kit — it should feel warm
and approachable, not clinical." Pass: agent picks `styles/orchard.md` over
`atrium` and says why (modular/friendly vs premium/editorial), builds the page
as **rounded slabs** on the `#FFFEF4` field with no two adjacent fills the same,
uses the four rhythm numbers (`64px 24px` / `44px` / `55px` / `36px`), gives the
page exactly one candy-orange CTA with `--cta-ink` on it, keeps sage and orange
out of running text, and ships the `prefers-reduced-motion` branch for the
scrubbed headline. Fail: white on the orange CTA, body copy on `--primary`,
a true black or cool grey beside the warm palette, a second orange object,
sharp corners, or a grey drop shadow where the inset bevel belongs.

## Historical baselines (why these exist)

- Pre-0.4.0: T4 baseline invented plausible-but-wrong tokens
  (#F6F1E7/bronze) — packs added.
- Pre-0.5.0: T6 baseline declared the skill out of scope and invented
  Primer-like values — workbench pack + routing added.
- Pre-0.6.0: dashboard trigger probe missed 3/3 — description gained
  product-UI triggers.
- Pre-0.9.0: the pack skeleton lived only in the repo (`templates/`), so an
  installed skill pointed at a file the agent could not open — T7 added and
  the template shipped inside the bundle.
- Pre-1.1.0: the skill said nothing about Figma while `super-ux` handed it the
  look and expected the pack to become variable collections — T8 added with
  `FIGMA_BRIDGE.md`.
