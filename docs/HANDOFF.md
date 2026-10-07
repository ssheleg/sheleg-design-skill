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
