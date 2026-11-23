# Run ledger: UI mechanics doctrine (2026-11-23)

Task in one line: research modern interface guidelines, audit app P and app D against them, close the
gaps in the design pipeline (sheleg-design, super-ux, task-pipeline) with a packaged doctrine (UIM rules),
and trial the new pipeline on one screen of each app, before and after.

- Origin: operator order, Telegram 2026-11-23 00:47 Europe/Warsaw, relayed by the Fabric CEO (request
  dcc725be, thread 46688454). Fabric task 4cb64120-754f-417d-9f7d-038f989cc91c.
- Model: claude-opus-5-5 (this session) for every stage. Fable 5.2 through the Anthropic API is the
  operator-ordered author of the packaging only (concept, pipeline, rules); spend is in the ledger below.
- Profile: default. Triage: full flow (`short_path.py`: 8 files, a public contract, agent-observable, R2).
- Run mode: `run.loop` off.
- Companions: super-ux (scenarios, owns the action map), sheleg-design (this repo, owns look), make-skill
  (release). Agent architect consulted 2026-11-23: no template applies (skill change, not a Fabric agent).

## Stage 0: brief (locked)

What: a UI mechanics doctrine the three skill packages enforce, so an overloaded or unclear screen fails a
check instead of passing every stage; plus the research report, two app audits and a trial run.
Why: the operator's order (verbatim in the Fabric task); the gap analysis showed that almost no existing
check can fail an ordinary `product` screen.
Expected: see the REQ spine. Out of scope: changing the two apps' code (their own sessions build the
after); the app D and app P captures and audits never enter this public repository.
Must not change: existing rules keep working; new rules are additions or versioned clauses, staged where
a gate tightens (warning first, failure in the next release).

### REQ spine

| REQ | Row | Verified by |
|---|---|---|
| REQ-1 | Research of 2025-2026 guidelines with author and date per source, trusted sources only | `docs/reports/2026-11-23-ui-guidelines/` + `reports.py check` exit 0; one figure re-read at source |
| REQ-2 | Audit of app P and app D: good, exotic-good, weak, with screens | audit files delivered to each app session for its own repo; their receipt |
| REQ-3 | sheleg-design: control profiles, iPad layout, grouping and type ceilings, Anchor and Signature, provenance | `npm test` exit 0 on the branch; the new sections present and linked |
| REQ-4 | super-ux: action map format, lint U096 to U105, novice level in the test panel | super-ux gate exit 0; lint seen failing on a plant |
| REQ-5 | task-pipeline: novice walk (panel level, finding vocabulary), word-neutral design-tester edit, Anchor and Signature on product | task-pipeline gate exit 0; design_gate seen failing on a panel without novices |
| REQ-6 | Trial run before and after: app D lyrics-and-beat screen and app P metronome SCR-08 | scorecards with the decision rule applied |
| REQ-7 | Coordination: rough cut to app D and app P by 2026-11-24 14:00 Warsaw; super-ux and task-pipeline told on the board | message receipts; board message ids |
| REQ-8 | Fable spend reported, under USD 100 | `fable-ledger.jsonl` totals in the report |
| REQ-9 | Result to the operator's thread | board message id |
| REQ-10 | Skills released through make-skill after 2026-11-27 | tags, npm versions, hub pins |

### Source ledger

| Source | Read | Note |
|---|---|---|
| `docs/evidence/retro.md` floor | 2026-11-23, 8,760 bytes, budget 12,000 | Standing 8 and 10 apply: delegated findings reproduced; new artifacts checked against each other |
| Research (subagent) | 2026-11-23 | 61 sources, V or U marks; the NN/g tutorial figures re-read at source by the lead (Alita Kendrick, 2020-03-08) |
| Pipeline gap analysis (subagent) | 2026-11-23 | file:line evidence; three citations reproduced by the lead (`design_gate.py:48`, `ux-audit/SKILL.md:274`, `MOBILE_SURFACES.md:169`) |
| app D pack (app D session) | 2026-11-23 | captures 2026-11-18; two app P files misfiled, confirmed by headers and fixed by the app D session |
| app P pack (app P session) | 2026-11-23 | build 0.8.1 frames; metronome target sizes reproduced on the capture (minus and plus about 43 pt) |
| Fable 5.2 package | 2026-11-23 | two calls; every source id it cites resolves in the research |

Contradictions: the app P session's unmeasured 60/44 pt rule against the doctrine's 44/60/72 profiles
(resolved: 44 standard, 60 frequent, 72 performance, measured in the trial's hands test).

## Fable 5.2 spend (price: USD 8 per million input, 40 per million output, 2026-11-23 pricing page)

| Call | Input | Output | Cost |
|---|---|---|---|
| 1 (package) | 36,307 | 64,000 (40,874 thinking) | USD 2.85 |
| 2 (trial plans, amendments, rough cut) | 44,845 | 55,986 (37,873 thinking) | USD 2.60 |
| **Total** | 81,152 | 119,986 | **USD 5.45** of the USD 100 limit |

## Stages

- [x] 0 Intake (brief, REQ spine, source ledger, retro floor read)
- [x] 1 Docs study (research report `docs/reports/2026-11-23-ui-guidelines/`)
- [x] 2 Brainstorm and decompose (Fable package; order super-ux, sheleg-design, task-pipeline)
- [x] 3 Spec (UIM-01..34; private copy with app evidence `~/DATA/_artifacts/ui-mechanics-2026-11-23/doctrine/`, public neutral copy `docs/reports/2026-11-23-ui-guidelines/doctrine.md`)
- [x] 4 Plan (pipeline-changes.md, amended)

REQ-7: rough cut, audits and trial plans delivered to the app D session and the app P session on 2026-11-23 about 01:30 (SendMessage receipts 22ca4b6e, fe39a14b).
- [x] 5 Dev (sheleg-design PR #67, super-ux PR #67, task-pipeline PR #184)
- [x] 6 Tests (all three `npm test` exit 0; blind review round 1: 1 blocker fixed in super-ux 143286f; round 2: 3 blockers fixed in super-ux 3b16d9f and the HANDOFFs; round 3 running)
- [ ] 7 Lint and integrate (PRs)
- [ ] 8 Post-integrate (installed skills read the new text)
- [ ] 9 Docs and wiki
- [ ] 10 Acceptance and retro

REQ-6 first run: app D lyrics-and-beat screen, linter 18 to 0, find-it 2 to 5 of 5 (scorecard on the operator machine, summary in doctrine.md *Read this first*). Second run on app D's additions 2026-11-25 to 26; app P metronome after its build (estimate 2026-12-04).

holds: 2 (merge and release wait on the trial's second run, from 2026-11-27; app P captures)
