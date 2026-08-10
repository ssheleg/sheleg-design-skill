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

**Result, 2026-08-10 (tree `9312a85`): GREEN, with one finding.** The plan
carried the layer order, SCENES-as-data, the 0.82 hold with its smoothstep tail,
every fallback in the same commit, and a verification step; the agent tagged each
invented value `[mine]` unprompted and enumerated the four sections
`instrument-console` leaves undecided. **The finding is what it copied silently:**
the scrub recipe from `SHELEG_DESIGN.md` §9, which shipped `useLayoutEffect` with
hand-rolled teardown — the pattern `MOTION_DOCTRINE.md` §6 names as the source of
leaked triggers. It went into a plan labelled junior-ready. Fixed in 1.11.0.

## T3 — Retrieval (reference depth)

Ask for exact morph math + timing, the GSAP scrub recipe, and the perf
budget. Pass: HOLD 0.82, smoothstep + per-point arc stagger (spread 0.5,
chase 0.028/±0.04), ease:'none' + pathLength={1} + kill-on-cleanup,
936 particles / DPR [1,1.75] — quoted, not invented.

**Result, 2026-08-10 (tree `9312a85`): GREEN, and it found two absences.** Every
value came back with a `file:line`, nothing was invented, and the one number the
agent derived (a ≥25-frame floor for a full formation transition) was labelled
derived arithmetic rather than quoted. It then reported what the skill does not
contain: **`arcAmp` has no value anywhere** — "what separates *curls between
formations* from *wobbles*" — and neither does `drop`. It also caught the T2
contradiction from the other side, naming both files and refusing to pick without
saying so. Both fixed in 1.11.0.

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
thirteen headings (Register → Gotchas, including Components / Hero / Responsive
/ Signature element; plus Motion flavor if the pack is cinematic), authors
`styles/tokens/<name>.css` in the
same change, states the origin of the values, and does NOT invent tokens
inline in components. Fail: pack written from memory, missing headings, or
no token CSS.

**Result, 2026-08-10 (tree `9312a85`): GREEN.** The agent copied the skeleton
rather than improvising the structure, shipped all thirteen headings with
`Contract: widened`, omitted `Motion flavor` deliberately (standalone pack),
measured a live reference — numeric.io's published stylesheet, named with its
URL — and **read the three gates before authoring**, shaping decisions around
them (no `color-mix()` in the token layer, no one-way fork link). Ratios computed
by importing `validate_palette.py` rather than asserted.

**Three gaps it reported, all in what the bundle does not carry:** the skill
demands a live reference and offers no way to find one; the derive-a-status-set
pattern exists only in `maquette`'s prose, so every author rediscovers it; and
`## Hero` is written for a scrolling page and has no meaning for a standalone
console pack — both packs that could demonstrate it are `core` and skip it. The
first two are fixed in 1.11.0 by moving the authoring rules into the shipped
template. The third is real and open.

**One thing this run proves about the harness itself:** the agent reached
`CONTRIBUTING.md` and `test/*.py` because it had the repository. An installed
agent has neither, and the rule it cited as decisive — *do not ship a pack on the
nine* — lived only in `CONTRIBUTING.md`. A scenario run against a clone cannot
see that class of defect; it took reading the FILES I READ list to notice.

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

**Result, 2026-08-10 (tree `9312a85`): GREEN.** Five states not two, streaming
with a stop control from the first frame, refusal / rate-limit / crash rendered
as three visibly different things, the send confirm built as the artifact itself
rather than a dialog about it, and no invented confidence score. It went further
than the scenario asks in two places worth keeping: it disabled the approve
control **while an artifact is still streaming** ("you cannot consent to
something still being written"), and it refused to offer an undo for a sent
email because there is none.

**Two collisions it resolved out loud instead of silently picking:** the pack's
empty-state atom (*one dim sentence, no illustrations*) against the AI patterns
file's *capability statement plus runnable examples*; and the permitted typing
cursor loop against the doctrine's rule that loops collapse to static under
`prefers-reduced-motion` — the token layer's reduced-motion block zeroes two
durations and cannot touch a keyframe animation, so nothing joined the two rules.
It also named the one custom property it invented (`--accent-hover`, absent from
every pack) and derived it from two existing tokens rather than inventing a hue.

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

## T13 — Developer register, and the fork against the dark console

Two prompts, run in **separate fresh contexts**. The pack is only worth its
seventh row if the agent can tell these apart, so a pass needs both.

**T13a — should select `field-notes`.** "Build the landing page for our
open-source code-provenance tool: it has to convince engineers that every
answer traces back to a real source." Pass: agent routes to
`styles/field-notes.md` *and says why it is not `instrument-console`* (the
product has a source, not a dial), builds **one continuous sheet ruled by
`1px var(--line)` hairlines** with no dark section below the hero, uses the
dawn gradient rather than a dark band with an edge, quotes `#F8F7F0` /
`#16211B` / `#9A3F28` verbatim, puts `--brand-on-dark` `#CF7A52` on any
brand-coloured text over the hero, keeps `--verify` out of running text, and
labels claims with the bracketed provenance tag rather than a confidence
percentage. Fail: `#9A3F28` on the hero (2.29:1), white on `--verify`, an
italic emphasis (the display face has none), a hardcoded `12px` radius, a grey
drop shadow where the ring belongs, a second dark section, or a particle field.

**T13b — should still select `instrument-console`.** "Build the landing page
for our real-time infrastructure monitoring platform — engineers watch it
during incidents." Pass: agent stays on `styles/instrument-console.md` and
names the distinction (live changing state → the console register). Fail:
routing to `field-notes` because the audience is technical, which is the exact
over-generalisation this pair exists to catch.

**Result, 2026-08-04 (`c324d1b`): GREEN on both branches.** Two subagents in
separate fresh contexts. T13a selected `field-notes`, named `instrument-console`
as the alternative, applied the dial-vs-source test unprompted, quoted five
tokens verbatim, and caught three bans it said it would otherwise have broken
(a particle field, a second dark section, a confidence percentage). T13b stayed
on `instrument-console` and named `field-notes` as the alternative it rejected,
citing the same test in reverse. The over-generalisation branch did **not**
fire.

## T14 — The Claude Design bridge (design-sync)

"Push our design system to Claude Design so it stops building with generic
components." Session has `/design-sync`; the agent holds only the installed
bundle. Pass: agent reads `DESIGN_SYNC_BRIDGE.md` before acting, names
`npx sheleg-design-skill --kit <pack> --out <dir>` as the way to get a kit and
says the kits are **not** part of the install, states the three layers that
cross (the pack's bans as the design system's README, `styles.css` from
`tokens/<pack>.css` verbatim, the components), and states that **motion does
not cross** — no particle field, no shader hero, no scroll clock. On the four
reference types it holds the line: references inform layout and never identity,
a Lazyweb sweep is never uploaded, a live-site extraction lands in a pack
before it syncs, and Figma/pack/Claude Design move one direction per change.
Fail: hand-writing card HTML or `@dsCard` markers instead of letting the
converter emit them, linking to a `kits/` path that does not exist in an
install, committing a `projectId`, treating a swept reference as a component,
or shipping motion into the design system. In a session **without**
`/design-sync` (Cursor), the correct behaviour is to ignore all of it — the
bridge is gated on the tool, like Lazyweb.

**Result, 2026-08-10 (tree `9312a85`, bundle-only): GREEN, and it is the run that
named this release.** Given the bundle and told to read nothing above it, the
agent read the gate, the contract and the pack in full, named the `npx` kit
command correctly, said the kits are not part of the install, held every line on
what does not cross, and **refused to hand-author a kit** if the fetch failed —
citing the ban rather than improvising, which is the outcome the whole section
exists to produce.

**Three findings, all the same shape — the bundle instructing what the bundle
does not contain:** §7 says to record the pack version and no version existed
anywhere in the bundle; §1 argues from "the same six component names" and named
none; and a byte-for-byte token copy necessarily ships the `prefers-reduced-motion`
block that §6 says does not ship. The first two are fixed in 1.11.0 and gated by
`validate_bundle_self_sufficiency()`. The third was a genuine collision between
two rules that never adjudicated each other; §6 now states the resolution —
verbatim wins for the token layer, the bullet governs component-level branches.

## T15 — Transformation register, and the fork against the ruled document

Two prompts, run in **separate fresh contexts**. `cyclorama` and `field-notes`
are the two warm, light, monospace-voiced packs, and both serve technical
companies — which makes this the pair most likely to collapse into "the newest
warm pack wins". A pass needs both branches.

**T15a — should select `cyclorama`.** "Build the landing page for our
enterprise AI-transformation company. We run a 30-day diagnostic and then
install AI into a 300–3000 person business. There is no product screenshot —
what we sell is the change." Pass: agent routes to `styles/cyclorama.md` *and
says why it is not `field-notes`* (the argument is *watch this change*, not
*how do you know*), quotes the six `ctaCycle` stops verbatim, states the
contrast floor against `--field-2` rather than a representative stop, keeps
`--accent` out of running text and puts eyebrows on `--ink-soft`, and gives the
app window **no fill**. Fail: an accent-coloured eyebrow (1.71:1), a darkened
orange invented to make one legal, a shadow anywhere, a sticky nav, a
proportional display substitute such as Fraunces, or a status dot shipped
without its word.

**T15b — should still select `field-notes`.** "Build the landing page for our
open-source evaluation harness — engineers need to see that every score traces
back to the run that produced it." Pass: agent stays on
`styles/field-notes.md` and names the distinction (a claim with a source → the
ruled document). Fail: routing to `cyclorama` because the product is technical
and the pack is newer, which is the exact over-generalisation this pair exists
to catch.

**Result, 2026-08-08: GREEN on both branches.** Two subagents in separate fresh
contexts. T15a selected `cyclorama`, named `field-notes` as the alternative and
applied the *how do you know* / *watch this change* test unprompted, then ran the
same test against `instrument-console` in reverse; it quoted all six stops
verbatim, held its contrast floor against `--field-2` rather than `--bg`
("a page whose background moves has to be measured at its worst frame, or the
number is only true 1/6 of the time"), put eyebrows on `--ink-soft`, and gave the
app window no fill. It listed eleven bans it would otherwise have broken —
including both the pack exists to prevent: an accent eyebrow at 1.71:1, and then
"fixing" it by darkening the orange into `--danger`. T15b stayed on
`field-notes`, rejected `instrument-console` by the dial-vs-source test, and did
**not** drift to the newer warm pack; the over-generalisation branch did not
fire.

T15b also reported a contradiction inside `field-notes`: the token layer
annotated `--deep` as a "full-bleed dark band" while the Bans forbid "a dark
band with a hard edge" below the hero. Reproduced against both files, then
**fixed in `20797ef`** — nothing consumed `--deep` either way, so the annotation
was simply wrong. (The line numbers this note originally cited have since moved;
a citation without a commit does not survive the file it points into.)

## T16 — Product-led register, and the fork against the tool itself

Two prompts, run in **separate fresh contexts**.

**T16a — should select `showroom`.** "Build the marketing page for our CRM. The
product is genuinely good-looking and dense — real tables, real status chips —
and our best argument is just showing it." Pass: routes to `styles/showroom.md`
*and says why it is not `workbench`* (the page arguing for the tool, not the
tool); puts **one** specimen in the first viewport under `--shadow-specimen`;
**crops rather than scales** it; keeps `--disabled` `#A4ADBA` out of captions;
renders statuses as chips **containing their word**. Fail: two specimens; a
scaled-down screenshot; `--disabled` as a caption colour (2.27:1); a bare status
dot; a shadow inside the specimen.

**T16b — should still select `workbench`.** "Build the settings screen for our
internal admin tool — dense tables, filters, a detail drawer." Pass: stays on
`styles/workbench.md` and names the distinction (the surface being operated).
Fail: routing to `showroom` because the screen has tables, which is the exact
over-generalisation this pair exists to catch.

**Result, 2026-08-09: GREEN on both branches.** T16a selected `showroom`, applied
the *which surface am I building* test, cropped rather than scaled the specimen,
routed captions away from `--disabled` (2.27:1) unprompted, and listed thirteen
bans it would otherwise have broken — including approximating the seven-layer
shadow and setting Inter 400 as body. T16b stayed on `workbench`, named
`instrument-console`, `blueprint` and `field-notes` as packs that pulled "on
features present in the brief's nouns, none on the brief's actual register", and
did **not** drift to the newer pack.

## T17 — Precision register, and the fork against the ruled document

**T17a — should select `blueprint`.** "Build the landing page for our vector
database. Buyers care about recall at scale and cost per query; they will read
the architecture section first." Pass: routes to `styles/blueprint.md` *and says
why it is not `field-notes`* (precision, not provenance); ships **zero radius**;
puts registration marks on **one** thing; keeps `--ink-faint` out of text; adds
the `prefers-reduced-motion` branch the reference omits. Fail: any radius; marks
on every card; a screenshot as the hero figure; copying the reference's pure
black ink.

**T17b — should still select `field-notes`.** "Build the landing page for our
open-source data-lineage tool — every column in a report has to trace back to
the query that produced it." Pass: stays on `styles/field-notes.md`, names the
*how do you know* test. Fail: routing to `blueprint` because the product is
technical infrastructure.

**Result, 2026-08-09: GREEN on both branches.** T17a selected `blueprint`, held
zero radius globally rather than per component, drew the hero figure instead of
screenshotting it, and named both corrections the pack makes to its reference.
T17b stayed on `field-notes` and — the point of the reciprocity work — quoted the
fork **from both sides**, citing `field-notes.md:55-56` "restated at
`blueprint.md:45-46`", explicitly using the test "as written rather than
inventing one".

T17a also surfaced a real contradiction **inside `blueprint`**: the Signature
element said registration marks go on one thing per viewport while Components and
Hero gave them to both CTAs. Recorded here as "fixed in the same run" — but only
the Signature element half landed. The Components row still read "same metrics
and marks" and the Hero recipe still put marks on both buttons until the
2026-08-10 audit found them. **A fix is verified by the artifact changing, not by
the note saying it changed** (standing instruction 9, pointed at a fix rather
than at a refresh).

## T18 — Project front door, and the fork against the moving field

**T18a — should select `prism`.** "Build the front page for our open-source
vector database. Developers arrive from GitHub; they want the install command,
the benchmarks and the architecture." Pass: routes to `styles/prism.md` *and says
why it is not `cyclorama`* (a field that holds vs one that moves); puts the
**install line in the first viewport**; sets **mono body copy** at 1.65 leading
and a 60ch measure; keeps `--accent` out of body text (2.36:1). Fail: a sans
body; a second gradient; an animated wash; the install line below the fold;
72px display type in `--accent`, which is what the reference itself does wrong.

**T18b — should still select `cyclorama`.** "Build the landing page for our
AI-transformation consultancy — we install AI into a 300–3000 person business
and what we sell is the change." Pass: stays on `styles/cyclorama.md`. Fail:
routing to `prism` because both are pale mono-voiced light fields.

**Result, 2026-08-09: GREEN on both branches.** T18a selected `prism`, set the
body in mono at 1.65 leading and a 60ch measure, put the install line in the
first viewport, and caught the reference's own 2.36:1 headline. T18b stayed on
`cyclorama` and quoted the fork from both sides (`cyclorama.md:60-67`,
`prism.md:32-46`).

T18a also reported that `blueprint` and `prism` did **not** cross-reference each
other, so it had to derive the distinction itself — three packs extracted from
vector-database companies and only some of the edges drawn. Fixed in the same
run: `blueprint`, `prism` and `maquette` now fork against each other explicitly.

## T19 — Architecture register, and the fork against the cockpit

This pair was **probed at stage 0, before the pack was built**, against a draft
register — see the run's brief. It is re-run here against the shipped pack.

**T19a — should select `maquette`.** "Build the landing page for our enterprise
vector lakebase. We separate real-time serving, batch analytics and iterative
discovery on one source of truth, and buyers must understand the architecture
before the cost story lands." Pass: routes to `styles/maquette.md` *and states
the built-object test*; keeps the ink **cream** rather than white; puts black on
the aqua fill; labels every model block; does not move the model. Fail: `#FFFFFF`
as ink; the cream on an aqua fill (1.1:1); a perspective render; an exploded view
on scroll.

**T19b — should still select `instrument-console`.** "Build the landing page for
our real-time observability platform — engineers watch it on a wall screen during
incidents and the numbers update second by second." Pass: stays on
`styles/instrument-console.md` and names the dial-vs-model test. Fail: routing to
`maquette` on surface signals — near-black field, pale accent, mono labels — which
is exactly what this pair exists to catch.

**Result, 2026-08-09: GREEN on both branches**, and the stage-0 probe against the
draft register was green too. T19a selected `maquette`, kept the ink cream rather
than white, put black on the aqua fill, and refused the exploded-view-on-scroll
by name. T19b stayed on `instrument-console`, cited the reciprocal test at
`instrument-console.md:20-25` **and** `maquette.md:32-39`, and reported that
`maquette` pulled on surface features alone — "which is exactly why the
discriminator had to be *what the page renders*, not what the product is".

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

## T20 — The core-contract declaration (does an agent know what it does not know?)

Added 1.10.0, when every pack gained a `Contract: core|widened` line. The
question this pair answers is not "does routing still work" — it is whether
marking six packs as incomplete makes an agent **avoid** them, and whether an
agent on a core pack now *states* what it must decide instead of inventing it
silently. Three prompts, three fresh contexts.

**T20a — a core-contract pack must still be chosen.** "Build the settings screen
for our internal admin tool — dense tables, filters, a detail drawer." Pass:
routes to `workbench` over `showroom` on the *which surface am I building* test,
**and** enumerates what the core contract leaves undecided.

**T20b — the other core pack, against its own fork.** "Build the marketing site
for our at-home blood-testing subscription." Pass: routes to `atrium` over
`orchard`, same requirement.

**T20c — the dataviz handoff, which named tokens no pack defines.** "Style the
charts … give me the actual CSS custom properties for every colour." Pass: the
agent **verifies each token against `styles/tokens/<pack>.css` before writing
it** and says out loud where a token it would reach for does not exist. Fail:
`var(--good)` or a `--chart-*` name emitted for `workbench`, which has neither.

**Result, 2026-08-10 (`3af6d97`): GREEN on all three.** Neither core pack was
avoided; both were chosen on the written fork test and both agents quoted the
`Contract: core` line unprompted. T20a listed ~40 undecided items across
structure, table, filters, drawer, forms and responsive, and named its own
inventions as inventions. T20c verified every token against the CSS, reported
that `workbench` has **no** `--chart-*` set and no intermediate ramp step, ran
`dataviz`'s validator rather than eyeballing (`--accent-weak` → `--accent`
measures **1.14:1** against the surface and fails the ordinal floor), and refused
to recruit `--ok`/`--danger` as series colours because the pack marks them
state-only. That refusal is the whole point of the rewritten handoff.

**Four findings came back from these three runs, all reproduced and fixed in the
same commit:** the `Contract: core` note cited `docs/superpowers/backlog.md`, a
repo-only path absent from any install (the exact failure the 0.9.0 baseline
records for `STYLE_PACK_TEMPLATE.md`); `tokens/atrium.css` still said "three
shadows" after the pack was corrected to four — a fix that half-landed, in the
same run that criticised a fix for half-landing; the status-token sentence in
`SKILL.md` left three packs unaccounted for and licensed `var(--warning)` in
`atrium`, which has no such token; and `workbench`'s five sub-AA pairs were
undocumented while its Gotcha warned about a pair that passes.

## T21 — Building on a core-contract pack (not choosing one)

Added 1.11.0. T20 asked whether an agent *knows* what a `core` pack leaves
undecided. This asks the next question, which nothing in the harness covered:
what does an agent actually *do* with that silence when the user wants working
code? Every scenario before this one tested routing or specification; none
tested application, so "do the usage scenarios work" had no evidence behind it
for the case the library is used in most.

"Build the incident list screen for our internal ops console — dense table with
status, severity and owner, a filter rail, a detail drawer on row click. Use our
`workbench` design system. Give me the React component and the CSS." Pass: every
`var(--…)` verified against `styles/tokens/workbench.css` rather than assumed;
inventions namespaced and declared; the four undecided sections named as the
pack's declaration rather than discovered by failure. Fail: a token that does not
exist, an invented status ramp presented as the pack's, or silence about what the
pack did not decide.

**Result, 2026-08-10 (tree `9312a85`): GREEN.** 25 pack tokens, every one checked
against the CSS; the only five invented are layout scalars (`--ops-rail-w`,
`--ops-drawer-w`, `--ops-row-h`, two z-indexes) scoped to `.ops` so they cannot
leak into the token namespace. `tsc --strict` clean, rendered at four widths in
both themes, all 13 contrast pairs computed and passing, and the drawer's focus
behaviour verified rather than asserted.

**What only building could surface.** Three things no amount of reading would
have found: at 1440px the drawer covered three columns and the search box; the
title column collapsed to eight characters once the drawer took its width; and
the pack's `--bg`/`--panel-2` Gotcha — stated for dense tables and stat tiles —
applies verbatim to the filter rail, which the pack does not say. The agent
generalised it and **said that it was generalising**.

**And one gap the pack does not declare:** `workbench` has four status roles and
no rank ramp, so a severity scale had to be inferred from role descriptions. The
`Contract: core` line names four sections it leaves undecided; a severity ramp is
not among them, so this one was found by hitting it. That is the difference
between a declared silence and an undeclared one, and it is the shape to watch
for in the remaining core packs.
