# Release test scenarios (run with subagents before every release)

> **Every scenario carries its own `**Result:**` line, even when the run is
> written up jointly.** A verdict recorded only in a combined section is a
> verdict nobody can audit per scenario, and it miscounted this harness twice in
> one day — once claiming T1 was unrun when it had been green since 1.12.0, once
> claiming six were owed when five were. The one-line check:
>
> ```
> python3 - <<'EOF'
> import re, pathlib
> t = pathlib.Path("test/scenarios.md").read_text()
> s = re.split(r"(?m)^## (T\d+)", t)
> print([s[i] for i in range(1,len(s),2) if not re.search(r"\*\*Result|GREEN", s[i+1])] or "zero unrun")
> EOF
> ```
>
> **Run these against the installed bundle, not this checkout.** Every scenario
> below states its own pass condition one paragraph from its brief, so an agent
> with repository access can find its own exam — T5's run said so, unprompted,
> after selecting the right pack anyway. Point the run at
> `~/.agents/skills/sheleg-design/` (or any install), which carries the bundle
> and no `test/` directory, and hand it only the brief. A run against this
> checkout still has value — the findings are what the last three runs were
> actually worth — but its **verdict** is not blind and should not be recorded
> as if it were.

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
internal tool" («спокойный светлый интерфейс для внутреннего инструмента»);
**iOS onboarding screens; Russian phrasing of "design the mobile payment
screen" («спроектируй мобильный экран оплаты»)** — both added 1.12.0.
MUST NOT load: charts-only dashboard build (dataviz), pricing-table
redesign, three.js FPS drop, copywriting headline.

Pass: 0 misses / 0 false loads across the set.

**Result, 2026-08-11 (`v1.12.0`): GREEN, 14/14 — after one RED and a control.**
The first run of the widened description scored 13/14: the scroll-narrative
storyboard task came back `none`. A control run of the same set against the
**previous** description loaded the skill for it, which is what turned a
suspicion into a cause — the regression was mine, from dropping `scrubbed
sections` out of the prose to make room for the mobile trigger. That phrase was
the only thing carrying "section by section". Restored, paid for by shortening
`marketing site, or hero experience`, and re-run: 14/14 with both new mobile
tasks loading and all four distractors still routing away.

This is why the harness header says a description edit obliges the full trigger
set. The edit looked purely additive; it removed a carrier.

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

**Result:** GREEN, 2026-08-12, blind — see *T4 / T8 / T10 / T11 / T12*.

## T5 — Style self-selection

"Dark, precise, mission-control landing for infra product — which
direction + exact values?" Pass: agent picks instrument-console from the
SKILL.md table and quotes its values (#05070a, #3392ff, Geist, ease
0.16,1,0.3,1).

**Result:** GREEN, 2026-08-12 — see *T5 / T6*.

## T6 — Product-UI routing (standalone pack)

"Quiet light GitHub-like admin/dashboard styling — exact tokens, fonts,
surfaces, interaction states." Pass: agent routes to styles/workbench.md
standalone (no cinematic motion), quotes light+dark tokens verbatim,
references the ready-made tokens css.

**Result:** GREEN, 2026-08-12 — see *T5 / T6*.

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

**Result:** GREEN, 2026-08-12, blind — see *T4 / T8 / T10 / T11 / T12*.

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

**Result:** GREEN, 2026-08-12, blind — see *T4 / T8 / T10 / T11 / T12*.

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

**Result:** GREEN, 2026-08-12, blind — see *T4 / T8 / T10 / T11 / T12*.

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

**Result:** GREEN, 2026-08-12, blind — see *T4 / T8 / T10 / T11 / T12*.

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
same commit:** the `Contract: core` note cited `docs/evidence/backlog.md`, a
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

## T22 — The mobile register and the reference-sweep gate

Added 1.12.0, when `MOBILE_SURFACES.md` and the Mobbin sweep landed. Two
branches, two fresh contexts, one prompt apart.

**T22a — the sweep tools are absent.** "Design the paywall screen for our iOS
meditation app — we're on the `atrium` look. I need the structure and the actual
CSS values." Pass: the agent reads `MOBILE_SURFACES.md`, is **not blocked** by
the absence, declares what a `core` pack plus a phone leaves to it, and every
`var(--…)` resolves in `styles/tokens/atrium.css`.

**T22b — the sweep tools are present.** Same brief plus "have a look at what good
paywalls do and give me your recommendation". Pass: the agent states what it
would ask for and, for each answer class, **what it would and would not let that
answer change** — structure and content order may move; palette, type, radii and
motion may not.

**Result, 2026-08-11 (tree `0f3a866` + this change): GREEN on both.** Neither was
blocked. Both quoted the five rules with their homes, both named platform
convention as theirs, both computed contrast from the token layer rather than
trusting the pack's prose, and both found the same real defect in `atrium`:
`--accent-gradient` cannot carry `--accent-ink` across a full row (2.08:1 at the
pale end), so the selected plan row must use flat `--accent`. T22b's boundary
table is the artifact this scenario exists to produce — five queries, each with a
"may change" and a "may never change" column.

**The finding that changed the release:** both runs independently reported that
**no pack answers iOS Dynamic Type**. Every scale is a `vw`-keyed `clamp()`,
which responds to viewport width and not to the user's text-size setting; the
bundle had zero mentions of it. Reproduced by inspection — `--t-display:
clamp(3.375rem, 4.3233vw + 2.359rem, 6.25rem)` and no occurrence of the term
anywhere — and shipped as rule 6 of `MOBILE_SURFACES.md`, stated as a gap rather
than answered with an invented value.

**A limitation of this harness, recorded rather than smoothed over.** A subagent
inherits the session's MCP tools, so a *genuinely* toolless branch is not
reachable from here: both agents reported seeing `mcp__lazyweb__*` in their
listing, and T22b — briefed that Mobbin was present — checked and said plainly
that `mcp__mobbin__*` was **not** there. That is the new gate rule working
exactly as written (*gate on the tools, never on the config*), and it caught a
false premise in my own briefing. But it means T22a tested *instructed* absence,
not real absence. A true negative branch needs a session with no MCP servers at
all.

## T4 / T8 / T10 / T11 / T12 — run 2026-08-12, blind

The first runs executed against the **installed bundle** rather than this
checkout, under the rule at the top of this file: `~/.agents/skills/sheleg-design/`
carries the bundle and no `test/` directory, so no agent could reach its own pass
condition. Each was handed the brief and nothing else.

**5 of 5 GREEN**, and with that every scenario in this harness has a result.

| | Verdict |
|---|---|
| **T4** — style by name | quoted `#fbf6ec`, `#3f7d5f`, Fraunces / Newsreader / JetBrains Mono and `cubic-bezier(0.22, 1, 0.36, 1)`, and stated the source of values without being asked |
| **T8** — the Figma border | one collection per token family, light and dark as **two modes of one collection**, motion declared uncrossable; reading direction mapped onto tokens with unmatched values called out as a pack gap or file drift |
| **T10** — deck register | routed to `briefing-room`, quoted the OKLCH field and accent and `+0.14em`, built fixed 1280×720 frames, wrote slide titles as claims, replaced bullets with one diagram per slide, shipped no transitions |
| **T11** — consumer health | routed to `atrium`, quoted `#FEF9EF` / `#B05A36` / Financier Display 300 / `line-height: 0.9`, kept one continuous field, used the italic accent aside, made every control a pill, and shipped the `PAUSE MOTION` control with the still fallback |
| **T12** — the friendly half | picked `orchard` over `atrium` with the distinction quoted from the file, used the four rhythm numbers, gave the page one candy CTA with `--cta-ink` computed at 5.61:1, and kept sage and orange out of running text |

### The finding that outweighed the verdicts

T10 asked why `briefing-room` publishes no contrast ratios, and noted that by the
library's own account that means none of them are gate-covered. **It was right,
and it was right about more than one pack.** 1.16.0 had fixed exactly this for
`instrument-console` and swept nothing — an instance fix on a class, which is the
failure this repository has recorded three times.

Measured across the library rather than guessed: **121 stated ratios, and 71 of
them — 59% — reach no check.** Six packs declare no table base, and packs that
*do* declare one still leak, because a Gotchas paragraph is not a table row.

Every one of the 71 was recomputed by hand against its own token layer that day.
**All 71 are correct.** Two do not reproduce from any pair and both are legitimate:
`blueprint` arguing about pure black and `maquette` about pure white, colours those
packs deliberately do not ship.

**Two guards were written for it and both were thrown away**, which is the more
useful half of the finding:

1. *"Can any pair of this pack's tokens produce that number?"* — **cannot fail.**
   Thirty solid tokens are ~435 pairs spanning 1:1 to 20:1, and a planted `9.99:1`
   passed. Caught by planting a defect, which is the only reason it was caught.
2. Narrowing the pool to the token named on the line **does** fail — on nine lines,
   and eight of them are correct writing: floors (*"body on cream must clear
   4.5:1"*), bounds (*"no better than 1.97:1 on any of the six"*), positions in a
   gradient (*"4.06:1 by the 85% stop"*), and candidate colours a pack measures in
   order to reject them. None is a claim about a pair of shipped tokens.

So the guard has to tell a measurement from an argument about a measurement, and
that is work rather than a regex. Filed as B-013 rather than faked. The honest
state, written into `validate_palette.py` where the skip happens: **these 71 are
hand-verified as of 2026-08-12 and unguarded against the next edit.**

One real defect did come out of it: `RATIO_CLAIM` matched `--space-4: 1rem` as a
`4:1` claim. It had never fired because the partnerless branch skipped it — the
same blind spot, one layer down. The pattern now refuses a unit.

## T5 / T6 — run 2026-08-12, and what they found

Two of B-011's eight unrun scenarios, executed in fresh contexts against tree
`1e79c45`. **Both GREEN on their stated pass conditions.**

**T5** picked `instrument-console` from the table, quoted `#05070a`, `#3392ff`,
Geist and `cubic-bezier(0.16, 1, 0.3, 1)`, and forked it against `maquette` using
the library's own tiebreak (a number changing while the reader watches). It also
ran the repo's `near_cluster()` over the pack to answer the "three defaults"
self-check rather than asserting it — the field *is* inside the near-black
cluster and the electric blue is what takes it out.

**T6** routed to `workbench` standalone, quoted both themes verbatim, referenced
the token file rather than transcribing it, and declared the core contract's
silence out loud. It reproduced all five of the pack's stated contrast pairs
exactly.

**What they found is worth more than the verdicts.** Reproduced against the
artifacts before anything was edited:

| Finding | Verdict | Action |
|---|---|---|
| A materialized kit contains authored `:hover` / `:focus-visible` / `:disabled` / selected CSS — the exact states a **core** pack declines to specify — and `SKILL.md` says kits are not installed, so a reader of the bundle invents them from scratch. Neither file points at the other | **confirmed** (`kits/workbench/src/styles.css:134,138`) | fixed — `SKILL.md` now points at `--kit` before those states are invented |
| The dial table fires twice for "a quiet internal admin dashboard": *quiet like Linear* says DENSITY 2–3, *product UI* says 6–8, with no precedence rule | **confirmed** | fixed — the row naming the **surface** wins over the row naming a **mood** |
| `workbench`'s accent gotcha names `--panel-2` and `--accent-weak` but not `--bg`, and in light mode `--bg` **is** `--panel-2` (`#F7F8FA`) — so a plain accent link on the app ground fails the same 4.30:1 while reading as covered | **confirmed** (`tokens/workbench.css:5,7`) | fixed |
| `workbench` ships no type-size or spacing tokens, so the craft bar's "no ad-hoc font size" is unachievable in it; the kit writes 20 raw `font-size:` declarations | **confirmed** (zero `--t-*` / `--space-*` in the token layer) | filed |
| The kit's `DataTable` has no selected state, though the pack mandates `--accent-weak` + a 2px inset — the one atom on an admin dashboard that most needs selection | **confirmed** | filed |
| `instrument-console`'s palette table declares no measurement base, so none of its per-token ratios are gate-covered; the library's default dark infra pack is its least-covered one | **confirmed** | filed |
| `instrument-console` states `--accent-ink` at 6.0:1; the tokens compute 6.17 | **confirmed**, and conservative | filed |
| T5 noticed the expected answer for this scenario is checked into this file | **fair** — the harness cannot be blind while the answers live beside the prompts | filed |

Result: **2 of 8 closed. Six remain — T1, T4, T8, T10, T11, T12.**

## T23 — The tally register, and the fork against the notebook

Added 1.13.0 with the `scoreboard` pack. Two branches, two fresh contexts, one
prompt apart. This pair exists because `scoreboard` and `field-notes` share warm
paper, one warm orange-red accent and hairline rules — the two closest packs in
the library — and the whole distinction lives in what the small type is doing.

**T23a — should select `scoreboard`.** "Build the landing page for our AI ads
operator. We run Google and Meta campaigns for 2,000 clients and the pitch is the
numbers: average ROAS, revenue driven, keywords on page one." Pass: routes to
`styles/scoreboard.md` *and says why it is not `field-notes`* (countable results
vs auditable evidence); puts a **ledger with at least four dotted-leader rows in
the first viewport** and a date under it; keeps the primary button on `--action`
ink; keeps `--accent` out of every word (3.23:1) and uses it as the 3×18px tick;
sets radii at 2–3px. Fail: an orange CTA; a headline or body line in `--accent`;
a bare status dot; 8px radii throughout; antialiased pixel numerals; a second
ledger; a ledger with no date.

**T23b — should still select `field-notes`.** "Build the landing page for our
agent-memory tool. Every answer it returns cites the commit and the file it came
from, and developers audit that before they trust it." Pass: stays on
`styles/field-notes.md`, and can say what would have moved it (a number the page
accumulates rather than a claim it sources). Fail: routing to `scoreboard`
because both are warm paper with an orange-red accent and mono-ish small type.

**Result, 2026-08-12 (tree `50dc7e6`): GREEN on both branches** — and the run
paid for itself twice over in findings.

T23a selected `scoreboard`, quoted the fork from **both** sides
(`scoreboard.md:44-54`, `field-notes.md:50-60`), and closed two further
near-misses from the files rather than from taste: `showroom` (*"a page whose
subject is a screenshot rather than a total"*) and `instrument-console` (*"if the
page has no paper on it, this is the wrong pack"*). It set the dials 6 / 4 / 5
against the pack's own text, put a four-row dated ledger in the first viewport,
kept the primary button on `--action`, and declined the `?variant=` harness for
the reason `SKILL.md` gives — there is no populated page to mount it on.

T23b stayed on `field-notes` and named what would flip it. Worth recording: it
rejected **`blueprint`**, not `scoreboard`, as the nearest alternative, and never
reached for the new fork clause at all. The negative branch passed, but not by
the route the scenario predicted — for a developer-tool brief the confusable
neighbour is the other cold technical pack, and `scoreboard`'s resemblance only
becomes dangerous once a page starts counting. The fork is still correct from
both sides; it is simply not the edge this brief runs along.

**Eight findings came back and each was reproduced against the artifact before
anything was edited** (standing instruction 8). Seven confirmed, one refuted:

| Finding | Verdict |
|---|---|
| The focus ring's 20% halo composites to 1.29:1 and its 40% border to 1.67:1 | **confirmed** — and my own first computation, done in linear light rather than sRGB, was the wrong one. Fixed: a solid ring |
| `--accent-hover` is authorised as a link colour at 4.12:1, two paragraphs after the pack bans the accent from text for the same reason | **confirmed** — the argument was right and was not applied to its own next sentence |
| Four stated status ratios are 0.02–0.08 optimistic; they survive only on the gate's 0.1 tolerance | **confirmed** — they were computed from the OKLCH, not from the shipped hex |
| An 11px `--warn` chip on a 10% tint of itself is 4.38:1 | **confirmed** — the chip carries no fill now, which also removes a pack/kit disagreement neither agent noticed |
| `--bp-md` / `--bp-lg` are referenced in three token comments and defined nowhere | **confirmed** — replaced with the pixel values |
| `SKILL.md`: "Six of the thirteen … the other **six** answer all four" | **confirmed** by both branches independently — 6 core + 7 widened; introduced by this release's own count edit |
| `SURFACE_COMPOSITION.md`: "Only `field-notes` ships a `--chart-1…N` set today" | **confirmed** stale |
| The numeral column overflows: Press Start 2P advances 1em per glyph, so 80px is five glyphs and `$9,840` is six | **confirmed** by arithmetic — stated as a glyph budget now, with the only two legal answers |
| `--on-accent` is a dead token with no legal consumer | **refuted** — its consumer is the selected chip at 4.92:1, and a chip is not body text, a heading or a button fill. Recorded because a refuted claim that goes unwritten comes back as folklore |

All nine fixes shipped in `1.13.1`. **The scenario found more in one pair of runs
than the three gates did in the whole release**, which is the argument for
running the harness rather than writing it.

## T24 — The reading register, and the fork against the notebook

Added 1.19.0 with the `datasheet` pack. Two branches, two fresh contexts, run
**blind against the bundle directory only** — the agents were forbidden `test/`,
`docs/`, `kits/`, the README and the CHANGELOG, because this file carries the
answer beside the prompt (the limitation B-012 recorded). The bundle they read is
the worktree's, not an installed copy: the pack is unreleased, so a truly blind
run against an install is impossible until 1.19.0 ships. Stated rather than
glossed.

This pair exists because `datasheet` and `field-notes` are now the two closest
packs in the library — both off-white technical paper, both hairline-ruled, both
carrying one warm accent and mono small type — and the whole distinction lives in
what that small type is doing: a **source** you can check, or a **reading** about
you.

**T24a — should select `datasheet`.** "The marketing site for an API that tells a
customer, per request, whether the visitor is a bot, is on a device seen
committing fraud before, or is hiding behind a VPN or incognito. It returns a
stable device id and a suspect score in about 20ms. Buyers are engineering and
risk teams at e-commerce and fintech. We want the page itself to prove the thing
works." Pass: routes to `styles/datasheet.md`, quotes the clause that decided it,
and names the closest rejected pack with the clause that ruled it out. Fail:
routing to `showroom` because the page shows the product, or to
`instrument-console` because there is a dark surface in the pack.

**T24b — should still select `field-notes`.** "The marketing site for an
open-source tool that builds a knowledge graph of a codebase. Its whole selling
point is that every answer traces back to the file and line it came from, so a
reader can check it. Buyers are engineers and auditors who do not trust a black
box. There is a dashboard, but the argument is the traceability." Pass: stays on
`styles/field-notes.md` and can say what would have moved it (a reading about the
reader rather than a claim with a source). Fail: routing to `datasheet` because
the newest pack also serves a technical product with an instrument in it — which
is the failure mode a positive-only branch cannot detect, per standing
instruction 4.

Both branches were also asked, after choosing, to read their chosen pack in full
and report defects with file and quoted text — the same shape that returned nine
findings on `scoreboard` in T23.

**Result, 2026-08-12 (tree `feat/datasheet-pack-v1.19.0`): GREEN on both branches**,
and the pair returned twenty-two findings of which eleven were defects in the pack
shipped in the same commit.

T24a selected `datasheet`, quoted the SKILL.md row and the pack's own *"the reader's
first question is what does it actually return"*, and rejected `instrument-console`
using the fork clause **from both sides** — *"If the number ticks while the reader
watches, it belongs here. If it is a result, it belongs there."* It set the dials
5 / 3 / 5 against the pack's own text and named `field-notes` as the runner-up.

T24b stayed on `field-notes` and named what would move it, quoting the new fork at
`field-notes.md:76` and `datasheet`'s own *"Not for"* clause. It also observed that
three separate packs point at `field-notes` for that brief from three directions —
so the negative branch did not merely resist the newest pack, it had positive
evidence.

**Every finding was reproduced against the artifact before any edit** (standing
instruction 8). Eleven confirmed defects in `datasheet` were fixed in this commit:

| Finding | Verdict |
|---|---|
| In the alarm state `--danger` on its own `--danger-weak` tint is **4.44:1** — the one cell the alarm state exists to render | **confirmed** — the tint moves to `--pink-10`, 6.24:1. Every other alarm status tints at step 9; the break is now recorded |
| The focus ring at `--accent` is **2.85:1** on `--accent-wash` — the surface the same section mandates for a selected cell — and below 3:1 on `--surface-3` and all four status tints | **confirmed** — a new `--focus-color` token is `--accent-deep` on paper (worst case 4.59) and the accent in the alarm state |
| The accent's job list includes the reference's 11px mono visitor id, which the pack's own ban forbids | **confirmed** — the pack now states which two of the reference's four accent uses are legal and which two it refuses |
| "a 1px border one ramp step darker than the fill" is unimplementable: that step **is** `--action-hover`, so the border vanishes on hover and no token existed | **confirmed** — `--action-edge` is named, and the vanishing is stated as the reference's measured behaviour |
| The alarm tints and the alarm `--action`/`--accent-deep` carry neither MEASURED nor SELECTED, against the token layer's own contract | **confirmed** — 54 of 118 declarations were unmarked; the alarm group is now marked in full |
| "separate by only 10.0 … the hard floor" — 10.0 is not under a floor of 10 | **confirmed** — the sentence now says the floor is not strict and that zero margin is the reason to move |
| `--dur-reveal: 0.3s` against "UI motion stays **under** 300 ms" | **confirmed** — it is an entrance, governed by the sub-500ms rule, and the pack now says which ceiling applies to which token |
| The empty state fills value cells with `--ink-faint`, which the palette table restricts to "never content" | **confirmed** — `--ink-muted` at 5.06:1 |
| The 15px verdict chip and its -0.03em sit outside the type ramp with no token | **confirmed** — `--t-chip` and `--tr-chip` added, and a table row |
| The responsive clamp and its tracking switch had no tokens, in a pack that orders the token file be copied verbatim | **confirmed** — `--t-display-min` and `--tr-display-min` added |
| `SKILL.md`: "Six of the fourteen … The other **seven** answer all four" — 6 + 7 = 13 against a 14-row table, and `datasheet` is the pack left out | **confirmed, and it was this run's own edit.** The identical defect was found by a T23 agent in the previous pack release. Fixed, and this time the class is gated: `validate_contract_split()` derives all three numbers from the table |

**One claim refuted, and it is recorded because a refutation nobody writes down comes
back as folklore.** T24a reported that `field-notes` carries no fork against
`datasheet` and that the routing is one-directional at the riskiest fork. It is not:
the fork is at `field-notes.md:76`, and T24b quoted it verbatim from that file. The
two branches disagreed about the same line in the same tree.

**Eleven further findings are real and belong to files this run did not author** —
`field-notes`' provenance colours, its undocumented dark theme, and three routing
ambiguities in `SKILL.md`. Reproduced, filed as B-017 through B-020, and not fixed
here: changing a shipped pack's hexes is a visual change to a released design system
and is not this run's call to make quietly.

## T25 — The filing register, and the fork against the gallery

Added 1.21.0 with the `pigeonhole` pack. Two branches, two fresh contexts, run
**blind against the bundle directory only** — the agents are forbidden `test/`,
`docs/`, `kits/`, the README and the CHANGELOG, because this file carries the
answer beside the prompt (the limitation B-012 recorded). The bundle they read is
the worktree's, not an installed copy: the pack is unreleased, so a truly blind run
against an install is impossible until 1.21.0 ships. Stated rather than glossed.

This pair exists because `pigeonhole` and `showroom` are now the two closest packs
for a product-led company on a white page — both open with a screenshot, both are
white, both are chosen when the product itself is the argument — and the whole
distinction is **what the page is about**: the application as an object, or one row
of it with a name attached.

**T25a — should select `pigeonhole`.** "The marketing site for a tool that watches
a support team's shared inbox and files every incoming message into categories the
team defines in plain English — refund request, bug report, billing, press — then
drafts a first reply for the ones that need one. Buyers are support leads at
mid-size SaaS companies who are drowning in an unsorted queue. We want the page to
show what it calls things." Pass: routes to `styles/pigeonhole.md`, quotes the
clause that decided it, and names the closest rejected pack with the clause that
ruled it out. Fail: routing to `showroom` because the page shows the product, or to
`cyclorama` because the palette is pastel.

**T25b — should still select `showroom`.** "The marketing site for a design-review
tool. Its whole selling point is how good the workspace looks and feels — a canvas,
side-by-side versions, a comment layer — and our best asset is a set of very
high-fidelity screenshots of the app at real size. Buyers are design leads. There
are no categories, no labels and no queue; the argument is the surface itself."
Pass: stays on `styles/showroom.md` and can say what would have moved it (a
taxonomy the product names, shown as labelled chips). Fail: routing to
`pigeonhole` because the newest pack is also white and also product-led — which is
the failure mode a positive-only branch cannot detect, per standing instruction 4.

Both branches are also asked, after choosing, to read their chosen pack in full and
report defects with file and quoted text — the same shape that returned nine
findings on `scoreboard` in T23 and twenty-two on the `datasheet` pair in T24.

**Result, 2026-08-12 (tree `feat/pigeonhole-pack-v1.21.0`): GREEN on both branches**,
and the pair returned forty-nine findings of which twenty-two were defects in the pack
shipped in the same commit.

T25a selected `pigeonhole`, quoted the `SKILL.md` row and the pack's own *"the reader's
first question is what will it call this?"*, rejected `showroom` on the fork clause
**from both sides**, and named `cyclorama` as second-closest via the documented pastel
trap. Dials 5 / 4 / 4, each moved off the baseline with the clause it came from — and it
flagged its own VARIANCE reasoning as judgement rather than quotation, which is the
honest form.

T25b stayed on `showroom`, quoted the reciprocal fork from both directions, and answered
what would move it in four separate directions — including the one that matters: *"if the
review tool auto-filed comments into a fixed set of named buckets … the subject shifts."*
So the negative branch did not merely resist the newest pack; it named the boundary.

**Every finding was reproduced before an edit** (standing instruction 8). The arithmetic
ones were recomputed rather than read: `clamp(34px, 5.6vw, 60px)` yields **43.01px** at
768 where the pack claimed the measured 60px, `clamp(27.2px, 3.6vw, 40px)` yields
**27.65px** where it claimed 40px, `42.5 / 34 = 1.25` against a declared `--lh-display: 1`,
and **713 < 900** against a hero frame described as beginning below the fold. All four
confirmed: the ramps had been transcribed from the reference's *declared* clamps instead
of fitted to this run's own three readings — the same class as reading a ratio off an
OKLCH parent instead of the shipped hex, one layer up.

**Twenty-two findings fixed in this commit.** Both ramps refitted (7.82vw and 5.21vw,
which reproduce 34/60/60 and 27.2/40/40 exactly); a width media block for the mobile
line-height; the hero's arithmetic restated as *cut by the fold* rather than *below it*;
the button's hover made one instruction in both sections and stopped swapping its tinted
shadow for a greyer, fainter one; `--ink-faint`'s "never a word" amended to name the
WCAG 1.4.3 exemption it relies on; **the marquee paused rather than shortened under
reduced motion**, because an infinite animation at 0.01ms strobes at the reader the query
protects; the nine-versus-eleven count swept across eleven sites; `--ink-lede` relabelled
(a substitution that holds neither hue nor chroma is not a derivation) and `--good` /
`--warn` relabelled DERIVED with the definition widened to cover a role the reference
never paints; `--cta-shadow` renamed `--cta-shadow-tint` because a colour named like a
shadow is an invalid declaration CSS drops in silence; six tokens added that the pack
stated and the layer lacked (five line-heights and the 20px radius measured on 12
elements); the selected state specified and shipped; the FAQ's middle breakpoint and the
nav's mobile shape stated; the two-line ceiling reconciled with the measured three lines
at 768; a motion ceiling added to `SKILL.md`; the tinted-shadow rule given its mechanism
(`var(--cat-X-150)` / `-200`, which the kit writes out nine times); and three Gotchas
added — the two chips whose layers collapse (`--cat-cold-150` equals `-100`,
`--cat-step-50` equals `--bg`), the collision between `--accent-wash` and To Reply's two
palest tints, and the corrected causal claim about deuteranopia.

**That last one is the finding worth keeping.** The pack had argued that deriving the inks
to clear AA *caused* the hues to collapse under deuteranopia. T25a checked the two numbers
and refuted the causation: 4.42 ΔE is already less than half the floor of 10, so the
reference's brighter inks were never distinguishable either. Derivation makes it worse; it
does not make it true. The conclusion survives and the argument for it is now correct.

**One finding refuted, and the two branches disagreed about it.** T25b called
`Contract: widened — all thirteen headings` an off-by-one, because every widened pack has
fourteen `##` headings. T25a checked the same thing and found the count correct. T25a is
right: the contract is thirteen headings **plus** `## Motion flavor` for a cinematic pack,
which is `validate.py`'s own docstring and which `validate_contract_terminology()` enforces
as the one permitted spelling. Recorded because a claim disproved and never written down
comes back as folklore — and because two capable readers of the same file reached opposite
conclusions, which is evidence the phrasing invites the misreading even though it is true.

**Twenty-six findings filed rather than fixed**, because they belong to artifacts this run
does not own: twenty-three against `showroom` (board B-021 … B-024) and three against the
pack skeleton's Components contract (B-025). Filing them here rather than acting on them is
the boundary this run kept; several are serious, and the board rows carry the numbers.

## T26 — The proof register, and the fork against the ledger

Added 1.24.0 with the `roster` pack. Two branches, two fresh contexts, run **blind against
the bundle directory only** — `test/`, `docs/`, `kits/`, the README and the CHANGELOG are
forbidden, because this file carries the answer beside the prompt.

This pair exists because `roster` and `scoreboard` now serve the **same product category**
— growth, ads, SEO — and the category is not the distinction. `scoreboard` is built around
a figure that ticks up; `roster` around a name that appears. A router that reads the
category and stops will pick wrong half the time, which is precisely what the negative
branch is for.

**T26a — should select `roster`.** "The marketing site for a tool that gets B2B software
companies recommended inside ChatGPT and Google's AI answers. Our strongest assets are the
engines we already show up in and the 300 customers who let us name them, sorted by
industry. Buyers are heads of growth who do not have an SEO team. We want the page to make
the case with who is already on board." Pass: routes to `styles/roster.md`, quotes the
clause that decided it, and names the closest rejected pack with the clause that ruled it
out. Fail: routing to `scoreboard` because the category is SEO, or to `showroom` because
the page is white and product-led.

**T26b — should still select `scoreboard`.** "The marketing site for an ad-spend analytics
product. The hero is a live counter of managed spend, every section is a metric that has
moved since last quarter, and the case studies are all percentage lifts. Buyers are
performance marketers. We have no customer logos we are allowed to show." Pass: stays on
`styles/scoreboard.md` and can say what would have moved it (proof that arrives as a name
rather than a figure). Fail: routing to `roster` because the newest pack also serves an
SEO-adjacent buyer — the failure a positive-only branch cannot detect, per standing
instruction 4.

Both branches are also asked, after choosing, to read their chosen pack in full and report
defects with file and quoted text.

**Result, 2026-08-13 (tree `feat/roster-pack-v1.24.0`): GREEN on both branches**, and the
pair returned thirty-seven findings — fifteen against `roster`, twenty-two against
`scoreboard`.

T26a selected `roster`, quoted the SKILL row and the pack's own *"a product whose argument
is who already carries it"*, rejected `scoreboard` on the fork clause **from both sides**,
and named `pigeonhole` second and `showroom` third. Dials 7 / 4 / 4, each move licensed by a
quotation — and it noticed that `SKILL.md` grants `pigeonhole` a numeric motion ceiling in
writing and gave `roster` none, which is why 1.24.0 states one.

T26b stayed on `scoreboard`, quoted its Register's first sentence, buried `roster` with the
brief's own constraint (*"no customer logos we are allowed to show"* against a pack whose
signature element is a logo wall), and answered what would move it in **six** directions with
a citation each. The negative branch did not merely resist the newest pack; it mapped the
neighbourhood.

**Fifteen findings against `roster`, all reproduced before an edit, all fixed in this
commit.** The sharpest was one the pack had genuinely got wrong: four of its five derived
colours clear AA on the white field and on **none** of its three tinted surfaces — 4.32 on
the near-white step, 4.10 on the mint panel, 4.06 on the band — while the token layer claimed
they cleared "BOTH surfaces", meaning two of the four it ships. The eyebrow is
`--accent-ink`, so an eyebrow on the mint panel rendered at 4.10:1 with nothing warning the
reader. Also fixed: a token comment that read as an instruction to paint the eyebrow at
3.43:1; a Gotcha that attributed the nav fill to the wrong orange; *"Raleway covers 78 — the
six section heads and the sixteen eyebrows"*, where six plus sixteen is twenty-two; a
sentence that parsed as *zero elements have `scroll-behavior: auto`*; the missing **Viewport**
bullet, which the template asks for and eight of the ten widened packs carry; a container
claim measured once and declared three times; two motion tokens with an empty "where
measured" cell; and `--font-display`, which is byte-identical to `--font-body` in the one pack
whose thesis is that the display is set in the body face.

**And one motif went from unbuildable to specified.** `--pattern-grid` held
`url("squares-bg-1.svg")` — a file that ships with nobody, so a faithful copy paints nothing
and raises nothing. The reference's SVG was fetched and measured: 8.367px squares at 0.85px
radius in `#7f99d1` at 12% (`#f4f6fa` over white), hairline-stroked white at 0.3px, on a
9.667px pitch. Five numbers replace the filename, and the filename moved to Gotchas.

**One finding refuted, and it corrected two shipped packs instead.** T26b argued that
`scoreboard`'s `--scan-period: 0s` under reduced motion ships the very defect `roster`
records — that a duration cannot stop an infinite animation. Measured in Chrome 151: an
infinite animation at **0.01ms yields two different computed transforms** sampled 40ms apart,
and the same animation at **`0s` yields `none` and never moves**. So `scoreboard` is correct
and **both `pigeonhole` (1.21.0) and `roster` were over-stating the rule**: a duration *can*
stop an infinite animation, but only at exactly zero, and 0.01ms — what a global
reduced-motion rule usually writes — is the value that strobes. Both packs now carry the
precise version with the measurement.

**One finding was a regression this session introduced.** T26b noticed that `scoreboard`'s
pack still documents *"Below 768 the label column drops"* while its kit has used
`@container (max-width: 231px)` since 1.23.0 — a pack/kit divergence, which `SKILL.md` calls
a defect in one of them. The pack now states the container rule and why the viewport number
was replaced.

**Twenty of `scoreboard`'s twenty-two are filed rather than fixed** (B-033 … B-036), because
they belong to a shipped pack this run does not own. Four were reproduced first: its token
layer still licenses *"the one orange that may carry a link"* at 4.12:1 which the pack
retracted in 1.13.1; `#00D492` is stated at 1.84:1 "on white" and measures **1.94** there
(1.84 is against the paper); the `[data-surface="panel"]` block remaps eleven tokens and
**not** the status set, so `var(--good)` on the dark band paints **3.69:1** where
`--good-on-dark` would give 10.21; and `--ink-faint` collapses onto the panel's `--ink-soft`,
making a disabled control indistinguishable from secondary copy on the pack's own hero
surface.

