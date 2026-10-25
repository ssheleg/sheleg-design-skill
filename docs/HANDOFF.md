## v1.66.4: descriptions within a 300-character budget (2026-10-25)

- **Done.** Every skill description in this member is at or under 300 characters (hub measure:
  whitespace collapsed, front matter only), per hub board row B-255 (a); the words a description
  dropped live in its `## Triggers`. Before/after figures are in CHANGELOG.md. Checked: the
  repository gate, and in the sshlg-skills worktree `node test/route_coverage.js` (125 named, 0
  spoke where silence was right, unchanged), `node test/triggers_test.js` (70 OK) and
  `node test/advertised_check.js` for this member.
- **Next task.** After merge: tag `v1.66.4`, watch the release, then the sshlg-skills pin bump; then
  the highest open board row.

## v1.66.3: the family member gate (2026-10-24)

- **Done.** the family member gate: the family member gate (`test/family_gate.py`, with its shared-mechanism
  declaration) and the documentation merged since v1.66.2, released.
- **Next task.** After merge: tag `v1.66.3`, watch the release, then the sshlg-skills pin bump; then
  the highest open board row.

## 1.66.2 released and pinned (2026-10-22)

- **State.** sheleg-design 1.66.2 is tagged, on npm and pinned by sshlg-skills 1.73.2; installed on the operator machine.
- **Next task.** B-052: re-measure discovery for the changed description (`docs/evidence/backlog.md`). B-004 waits on the operator's design call.

## v1.66.2: the ledger records the shipped version (2026-10-22)

- **Objective.** Record the shipped version in the verification ledger (the sshlg-skills validator reads it).
- **Done.** Ledger entry v1.66.2.
- **Next task.** After merge: tag `v1.66.2`, watch the release run, then the sshlg-skills pin bump.

## v1.66.1: no private product name in the origin notes (2026-10-22)

- **Objective.** Remove a private product name from shipped doctrine (operator, 2026-10-22).
- **Done.** Origin notes neutral in the plugin and the `.cursor` mirror; version 1.66.1.
- **Next task.** After merge: tag `v1.66.1`, watch the release run, then the sshlg-skills pin bump.

# Short description, 1.66.0 (2026-10-20)

Branch `desc-budget-1020`. The description went from 964 to 425 characters and
the command from 213 to 75, because the operator's skill listing was full and
81 skills showed no description. Removed trigger phrases live verbatim under
`## Triggers` in SKILL.md; the routing-form check reads that section. Two passages moved
out of the body (to `COMPONENT_LAYER.md` and `STYLE_PACK_INDEX.md`) to stay under
4,750 tokens. Gates:
`npm test` alone, exit 0, and `python3 test/validate.py --self-test`.

Next task: none here; the hub re-pins 1.66.0 in its own change.

---

# WebKit (Safari) first in visual review — 2026-10-16

Branch `docs/safari-first` prepares sheleg-design 1.65.0 (family iteration
ITER-1016, REQ R12): `VISUAL_REVIEW.md` gains *Engine order — WebKit (Safari)
first* and an `engine` field in the capture record; motion review and the
director's verify lane put the WebKit route first, with Chromium as the stated
fallback. Five version homes, `SKILL-CARD.md` and the `.cursor/` mirror moved
together. Regression: `test/audit_regressions/safari-first.py` (watched failing
first: 4 failures, 2 errors; then green). Gate: `npm test` exit 0.

Open: none in this branch. The coordinator owns PR review, the annotated tag,
the umbrella pin and the local install update.

Next task: review the draft PR, then the family release sequence.

---

# FW05 ledger correction — 2026-10-13

The umbrella detected a missing 1.64.2 verification heading after publication.
The [correction receipt](evidence/runs/2026-10-13-fw05-ledger-correction.md)
records reproduction, payload parity and integration scope. The new ledger entry
links accepted source, genuine publication and exact registry bytes. Only excluded
documentation changes; keep 1.64.2 and its existing tag. Next: independent review,
frozen PR promotion and normal merge; then umbrella successor pin. Historical
packaging handoff below is retained as the earlier candidate snapshot.

---

# FW05 release packaging — 2026-10-13

Branch `release/fw05-1.64.2` prepares patch version 1.64.2 from accepted source
`ab7d82e97dc33e22d22de69b8b09c380c68a3ec2` (PR43). The genuine validation run
[38338843437](https://github.com/ssheleg/sheleg-design-skill/actions/runs/38338843437)
passed at candidate `e5055a69b8df44f9182060eba61d3820bcffe77c`; independent review
and local gate detail remain in the [source receipt](evidence/runs/2026-10-13-fw05-design-facts.md).
Registry and remote tags read 1.64.1 before packaging. This branch synchronizes
manifests, skill metadata/mirror, card, changelog and release stamp only.

Local packaging gate: `python3 test/validate.py` passed 6651 checks.
Independent packaging review passed at `a4fe6b23fde92aeb58116eac4b4849196b983a46`: manifests,
metadata, card and changelog only; no code or workflow changes.
Next: frozen PR promotion, normal merge and exact-source release checks before
any annotated tag. Publication, registry readback, umbrella pins and installed/native checks
remain pending. B-145 and other provider/render observations remain open.

---

# FW05 source facts — 2026-10-13

Branch `fix/fw05-derived-design-facts`, based on `f5244f6`, implements
B-055/B-056/B-113/B-126/B-128. The current scope and exact commands live in the
[FW05 receipt](evidence/runs/2026-10-13-fw05-design-facts.md). B-146 was already
resolved in super-ux source; its historical board text is preserved with a
commit-addressed reconciliation. No palette choice or runtime rendering changed.

Independent bounded review passed at `6a24c23` (receipt below).
Next: freeze and deliberately promote [PR43](https://github.com/ssheleg/sheleg-design-skill/pull/43),
then normal integration only after the genuine checks pass. Version/release/umbrella pins/install are
separate. B-145 live Figma observation and other board rows remain open. The next
family packet is super-ux B-025/B-026, owned and validated in that repository.

---

# Annotated-tag release gate — 2026-10-10

Branch `fix/family-round-1010` prepares sheleg-design 1.64.1: one step in
`release.yml`, right after checkout, refuses a tag whose `git cat-file -t` is not
`tag` (umbrella plan 2026-10-10, T5 / REQ-6). No doctrine, kit or installer change.
Receipts: the 1.64.1 section of [verification.md](evidence/verification.md) and the
CHANGELOG.

Open: B-145, B-146 (unchanged). Next task: after the release, the umbrella re-pins
this member at `v1.64.1`.

---

# Figma practices — 2026-10-08

Branch `feat/figma-practices` prepares sheleg-design 1.64.0 from a 2026-10-08 read
of Figma's own guidance (provenance W6, W7). `FIGMA_BRIDGE.md` §1 gains the
family's one token-tier model under `### Token tiers` (anchor `#token-tiers`: two
tiers, primitive → semantic alias), code syntax in `var(--…)` form and a scope
table on every published variable; §4's re-read checks both; new §6 overrides
Figma's guidance where the pack is the authority (Code Connect instructions
generated or unused, labelled placeholder images, declared font failures, 1:1 as
layout only, corrections into the record). `CREATIVE_DIRECTOR.md`'s Redesign row
starts from a `generate_figma_design` capture into the surface's recorded file.
The description carries «сделай дашборд», «админка», «анимации», «макеты».
Gates: `validate_figma_contract()`, `validate_routing_forms_lead()`, four plants.
Receipts: the 1.64.0 section of [verification.md](evidence/verification.md) and
the CHANGELOG.

Open: B-145 (one live Figma call to observe code syntax reaching
`get_design_context`), B-146 (super-ux links `#token-tiers`). The coordinator owns
PR review, release, tag, umbrella pin and local install update.

Next task: review the PR; then merge the parallel super-ux change that links
`FIGMA_BRIDGE.md#token-tiers`.

---

# Director record, ADA rubric and the render eval — 2026-10-07

Branch `feat/director-record-ada` prepares sheleg-design 1.63.0: tasks D3, D4, D5,
D6, D8, D10, the K6 rubric, the first-time-right rules and B-140 of the anti-slop
design plan. The director record is a file with a validator
(`templates/director-record.md`, `npx sheleg-design-skill --check-record <file>`,
`bin/record.js`, exit 0/1/2, per-class field sets for flagship / product /
internal / ad, `Mode: declined` passes); `ADA_RUBRIC.md` carries R1–R25 with G/J/H
types, three profiles and the judge rules, stated as derived; the reference sweep
is mandatory for a new design or a brand redesign; `MOTION_DOCTRINE.md` §12 is
the motion review; `FIGMA_BRIDGE.md` §3 is re-drawn for TIMING/EASING variables
and §5 critiques a frame before approval; `MOBILE_SURFACES.md` gains the axes
matrix; `evals/render/` is the render eval harness; the kits pass their own
floor and CI runs `--lint kits`. Receipts: the 1.63.0 section of
[verification.md](evidence/verification.md) and the CHANGELOG.

Open: B-141 (linter limits), B-142 (a model run of the render eval), B-143 (a
labelled set before J items count), B-144 (one Figma call to confirm §3). The
coordinator owns PR review, release, tag, umbrella pin and local install update.

Next task: review the PR; then task-pipeline T1 can gate stage 3 on
`--check-record` (K3), and super-ux U3 can require the frame critique of
`FIGMA_BRIDGE.md` §5 before approval.

---

# Visual floor and project linter — 2026-10-07

Branch `feat/slop-markers-lint` prepares sheleg-design 1.62.0: tasks D1, D2 and D9
of the anti-slop design plan. `SLOP_MARKERS.md` is the floor (49 markers, reasons
and exceptions, dated); `npx sheleg-design-skill --lint <dir>` is its machine half
(`bin/lint.js`, 20 rules, exit 0/1/2); `CREATIVE_DIRECTOR.md` records
markers-not-bans and follows the umbrella's new lanes. Receipts: the 1.62.0
section of [verification.md](evidence/verification.md) and the CHANGELOG.

Open: B-140 (two kits transition `width`; then gate `--lint kits` in CI), B-141
(three known linter limits). Not done here: the director record as a file and its
validator (D3, `--check-record`), the render eval (D8). The coordinator owns PR
review, release, tag, umbrella pin and local install update.

Next task: review the PR; then D3 builds the director record on the `Markers`
line this branch adds.

---

# Provenance and motion-tool reconciliation — 2026-10-07

Branch `feat/provenance-emil` prepares sheleg-design 1.61.3: tasks P1, D7 and E1b
of the anti-slop design plan. `KNOWLEDGE_PROVENANCE.md` grows from 6 to 16 rows
with MIT and Apache-2.0 notices for the three `adapted` rows; the installed
`emilkowalski/skills` tools are named inside the motion, mobile and visual-review
lanes; eleven rules are reconciled with those tools (RC-01…RC-11); the duplicated
`SKILL.md` sentence and `SHELEG_DESIGN.md` section are gone, and both defect
classes now have a gate. Receipts: the 1.61.3 section of
[verification.md](evidence/verification.md) and the CHANGELOG.

Open: B-139 (28 packs name `100dvh`; hero → `svh` sweep). Not done here, by
decision: carrying impeccable and taste-skill doctrine in by paraphrase (later
plan tasks D1, D11, D12). The coordinator owns PR review, release, tag, umbrella
pin and local install update; this branch alone is not a published update.

Next task: review the PR, then the family release sequence. After it, D1
(`SLOP_MARKERS.md`) can start on top of rows 15–16.

---

# Display-copy review follow-up — 2026-10-01

DC-02 prepares sheleg-design 1.61.2: rendered-copy review now names visible
roles and coverage at the design/copywriting seam. See the
[bounded report](evidence/audits/2026-10-01-display-copy/report.md) for scope,
receipts and limitations. The coordinator owns PR review, release and umbrella
pinning; this branch alone is not a published or installed update.

Next task: review this branch with the companion super-ux punctuation parser
change, then follow the family release sequence. Do not add a second copy parser
here. Model-output improvement remains unmeasured.

---

# Sherlock family audit: handoff

This branch contains the prepared sheleg-design-skill instruction changes from the family
audit. The runtime backlog has not been implemented or released.

Start with the [central handoff](https://github.com/ssheleg/sshlg-skills/blob/codex/sherlock-audit-handoff-20260907/docs/HANDOFF.md).
It links the 139 parent outcomes, 254 bounded task packets, module contracts,
source provenance, execution order and all member branch revisions.

Read the central repository manifest before choosing a task. Filter the plan by
this repository's module, then read one leaf and its prerequisites. Refresh source
hashes against the chosen checkout and materialize predecessor outputs before
editing. A prepared instruction is not evidence that an agent outcome improved.

Validation receipts for these instruction changes are in the central bundle.
Commit and push each completed task with its updated context and checks; leave a
new entry point for the following agent. Follow the [standing handoff rule](https://github.com/ssheleg/sshlg-skills/blob/codex/sherlock-audit-handoff-20260907/docs/working-rules/repository-handoff.md).
