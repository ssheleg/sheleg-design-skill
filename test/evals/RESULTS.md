# Evaluation results

**Status: executed 2026-08-31 — one dated row per model probed, method and
limits stated below.** Before that date the suite was authored and
schema-validated only; the vacant row is kept so the table's history stays
readable.

CI still proves only that the files are shaped correctly and that the
validator catches a planted invalid trigger class. The rows below are model
runs, executed by hand-driven harness sessions, and each carries the method
that produced it. A number without its method is not a measurement.

| Date | Version | Model | Trigger pass rate (train / validation) | Scenario lines passed | Installed alongside | Notes |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | no run yet (authored 2026-08-27) |
| 2026-08-31 | 1.58.2 | claude-haiku-4-5-20251001 | 8/8 / 7/7 (15/15) | 9/10 scored, 2 not reproducible | 31-skill list, see Method | coexistence negatives q13–q15 all landed on their intended neighbours |
| 2026-08-31 | 1.58.2 | claude-sonnet-5 | 8/8 / 6/7 (14/15) | 10/10 scored, 2 not reproducible | 31-skill list, see Method | one false positive: q10 (mechanical CSS-selector fix) routed here |

## Run 2026-08-31 — detail

### Method

- **Trigger probes.** One fresh, isolated headless session per query per model:
  `claude -p --setting-sources "" --output-format json`, working directory an
  empty temp dir. The whole prompt was the query verbatim, then the line
  `Installed skills:` followed by 31 `name: description` pairs, then
  *"Which ONE skill would you invoke, or none? Answer with the name only. Do
  not use any tools."* The 31 candidates are the ssheleg family's 28 skills
  (descriptions read from each member's shipped `SKILL.md` front matter) plus
  the three installed neighbours the coexistence negatives name:
  `frontend-design`, `theme-factory`, `figma-generate-design`. A positive case
  passes when the answer is `sheleg-design`; a negative passes when it is
  anything else, `none` included.
- **Model identity** is read from the CLI's `modelUsage`, not assumed:
  `claude-haiku-4-5-20251001` and `claude-sonnet-5` (the sonnet sessions'
  usage also lists claude-haiku-4-5 for the CLI's internal auxiliary calls;
  the answering model is claude-sonnet-5).
- **Scenarios.** One fresh isolated headless session per scenario per model,
  working directory the shipped skill bundle, tools limited to
  `Read,Glob,Grep`, prompted to read `SKILL.md` first, follow it, and answer
  with a concrete plan without writing files. Each `expected_behavior` line
  was then scored against the transcript; a line whose subject is conduct
  during a live build or a live Figma file operation — things a headless
  session cannot perform — is recorded as **not reproducible from this
  harness**, never guessed.
- **Limits, stated rather than hidden.** (1) The eval README asks for each
  query three times in a fresh session; this run asked each query **once**
  per model — a wider run remains owed. (2) The wave protocol named the
  harness Agent tool as the probe transport; the shared 20-subagent pool was
  exhausted by concurrent wave agents, so probes ran as headless CLI sessions
  instead — the same blind fresh context, and additionally free of the
  harness agent system prompt. (3) The isolated sessions still see the CLI's
  bundled built-in skills (dataviz and friends) as ambient candidates beside
  the prompted list. (4) The CLI's stdin detection killed 8 first-attempt
  sessions (`no stdin data received`); those were re-run with stdin closed
  and the errors were never scored as answers. (5) The scenario sessions ran
  inside the repository checkout, and one transcript (s03 / haiku) visibly
  read repository context (the git branch name) before planning — a
  contamination path a packaged install would not have.

### Trigger probes, per query

| Query | Expected | claude-haiku-4-5 | claude-sonnet-5 |
|---|---|---|---|
| q01 dark dashboard + token layer | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q02 кинематографичный лендинг со скролл-анимацией | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q03 light/dark themes into shadcn | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q04 дизайн-токены в переменные Figma | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q05 mobile agent screen calmer | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q06 презентация как 16:9 веб-дек | trigger | sheleg-design ✓ | sheleg-design ✓ |
| q07 which screens onboarding needs | no | ux-flows ✓ | ux-flows ✓ |
| q08 перепиши текст ошибки и CTA | no | copywriting ✓ | copywriting ✓ |
| q09 API endpoint behind dashboard | no | none ✓ | none ✓ |
| q10 fix CSS selector, existing tokens | no | none ✓ | **sheleg-design ✗** |
| q11 тарифы и состав планов | no | copywriting ✓ | none ✓ |
| q12 accessibility audit of checkout | no | none ✓ | none ✓ |
| q13 pre-set theme for a report artifact | no (coexistence) | theme-factory ✓ | theme-factory ✓ |
| q14 собери страницу в Figma из компонентов дизайн-системы | no (coexistence) | figma-generate-design ✓ | figma-generate-design ✓ |
| q15 bespoke direction, no pre-made pack | no (coexistence) | frontend-design ✓ | frontend-design ✓ |

The single miss is a real reading of the description: q10 mentions tokens and
CSS, and sonnet weighed the vocabulary over the "mechanical fix, no visual
decision" frame. Haiku declined it. Recorded, not tuned away — the negative
exists to keep measuring exactly this edge.

All three coexistence negatives routed to the neighbour they were written
against, on both models: the pre-set-theme artifact ask to `theme-factory`,
the design-system-to-Figma rebuild to `figma-generate-design`, the
explicitly-no-pack brief to `frontend-design`.

### Scenarios, line by line

**s01 Product UI pack** — haiku 4/4, sonnet 4/4.
Both transcripts chose `workbench` as the index default, stated the dial
values with the product-UI row as the reason (haiku: VARIANCE 4 / MOTION 2 /
DENSITY 7; sonnet: 4 / 2 / 8 with "dense is explicit" argued), directed the
token layer to be copied verbatim from `styles/tokens/workbench.css`
("do not transcribe" in both), and kept cinematic motion out (haiku: "no
cinematic/scroll-driven motion"; sonnet: "the scroll-clock architecture
doesn't apply").

**s02 Cinematic landing** — haiku 3/3 scored + 1 not reproducible; sonnet
3/3 scored + 1 not reproducible.
Both loaded the cinematic reference and the motion doctrine before planning,
built every layer on the single measured scroll store, and shipped the
reduced-motion fallback per layer in the same change ("not a feature: a
contract" / "same commit as each layer, not at the end"). Line 4 — actually
verifying mid-hold, mid-morph and narrow-viewport states — needs a built page
in a browser; both plans name all three states in their verification lists,
and the verification itself is **not reproducible from this harness**.

**s03 Figma crossing** — haiku 2/3 scored (one line failed) + 1 not
reproducible; sonnet 3/3 scored + 1 not reproducible.
Both read `FIGMA_BRIDGE.md` in full before any operation and both refused
hand-copied values (haiku: "map ONLY to existing pack tokens", round-trip
re-read per collection; sonnet: "I will not hand-copy values from memory or a
screenshot"). Line 4 — naming the destination instead of guessing — sonnet
passed by stopping: it asked which pack is "the chosen pack" and surfaced the
unauthenticated Figma connector as a hard blocker before any call; haiku
**failed** it by electing a default pack and inventing a file name rather
than asking. Line 2 — treating drawing in a shared frame as publishing — is
conduct during a live file operation; no Figma file was reachable from the
harness (the fresh session's connector is unauthenticated), so it is
recorded as **not reproducible from this harness**.

### Raw material

Probe and scenario transcripts were produced under `/tmp/shd-evals/`
(`probes.jsonl`, `probes-rerun.jsonl`, `scenarios.jsonl`,
`scenarios-rerun.jsonl`) on the machine that ran this; the scored evidence —
answers per query and the quoted plan lines above — is carried in this file
so the row survives the temp directory.
