# Retrospective — sheleg-design-skill

One file per project. Stage 0 reads the standing instructions **in full**; they
bind the run. Prune before adding — the list is capped at ten, and every
deletion is logged as a line, never silent.

## Standing instructions

| # | Instruction | Added | Last fired | Retires when |
|---|---|---|---|---|
| 1 | **This repo runs concurrent pipeline branches.** Before any `git checkout`, `git checkout -b`, `git stash` or branch delete, run `git worktree list` *and* `git status --porcelain` and read both. A clean status at session start is not a clean status now. If the tree is dirty and the work is not yours, do not switch — take a worktree under `../sheleg-design-skill-wt/<name>` instead. | 2026-08-04 | 2026-08-04 | a pre-checkout hook refuses a dirty foreign tree |
| 2 | **A new pack needs an addressable origin before it needs anything else.** A production URL that can be re-read, not a product name. No URL, no pack — the contract forbids invented values and a synthesised palette is an invented value wearing a citation. | 2026-08-04 | 2026-08-04 | the validator requires a URL on every pack, not only widened ones |
| 3 | **A gate is not evidence until it has been watched saying no.** Any new check ships with a planted defect it catches — as a `--self-test`, and once against a real file in the tree. | 2026-08-04 | 2026-08-04 | it becomes the review checklist rather than a rule |

## Run stamps

- **2026-08-04** — audit harvest into the skill (motion doctrine, dials, widened
  pack contract, palette validator, slop lint, depth model, dataviz handoff).
  Diverged; see below.

## Entries

### 2026-08-04 — a branch switch in a shared tree carried another run's work onto my branch

**Symptom.** Mid-build the validator failed on `styles/field-notes.md` and
`styles/tokens/field-notes.css` — files this run never authored. `git status`
showed twenty-five modified or untracked paths, timestamps minutes old,
advancing while the run worked: another session was writing to the same working
tree, and `git checkout -b` had carried its uncommitted work onto this run's
branch. The other session believed it was still on `feat/field-notes-pack`.

**Surfaced at.** Stage 6, build — as a confusing gate failure, several edits
after the actual damage.

**Owned by.** Stage 0, grill. The brief recorded `shared state: ungated —
single operator, single worktree, no lease` and treated it as a fact. It was an
assumption, and the evidence against it was already in the repository: three
feature branches, one of them (`feat/lecture-hall-pack`) carrying the commit
message *"held on concurrency"*, and an existing worktree at
`../sheleg-design-skill-wt/design-sync-bridge`. The convention this run needed
was already established and the harvest did not look for it.

**Root cause.** `git status` was read once, at session start, and its answer
("clean") was carried forward as still true across a long turn. Freshness of a
harvested fact was never re-checked at the moment it was acted on.

**Fix, by grade.**
- *Mechanical (wanted, not yet built):* a pre-checkout hook that refuses to
  switch branches when the tree is dirty with changes the session did not make.
  Recorded as the retirement condition for standing instruction 1.
- *Standing instruction (shipped):* instruction 1 above.

**Check that catches it next time.** `git worktree list` is now part of the
stage-0 harvest for this repo, and the answer goes in the source ledger beside
the others — so "single worktree" has to be written down as an observation
rather than assumed as a default.

**What went right.** Nothing was lost. The other run's twenty-five paths were
left untouched, this run's four files were copied out before any revert, the
shared tree was returned to `feat/field-notes-pack`, and the work moved to
`../sheleg-design-skill-wt/audit-harvest` on a branch rebased onto `main`. The
recovery is only cheap because it was noticed at all — a run that had committed
the other session's files as its own would have been expensive and quiet.
