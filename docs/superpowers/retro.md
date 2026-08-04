# Retrospective — sheleg-design-skill

The project's standing instructions and run log for task-pipeline. Stage 0
reads this file **in full**; stage 10 prunes, stamps, and writes an entry only
if the run diverged.

## Standing instructions (cap: 10 · current: 3)

Each one binds every run in this project until it is retired. Retire when it
became a mechanical check, when the paths it names are gone, or when it has not
fired in five run stamps.

1. **Never assume this checkout is yours alone.** Before stage 0 records shared
   state, run `git reflog -8`, `git branch -vv`, and look at working-tree
   mtimes. A HEAD move you did not make, a `feat/*` branch you did not create,
   or a file changing while you test means another pipeline run is live in the
   same directory. Recheck immediately before staging anything — the tree can
   turn hostile mid-run. *(Last fired: 2026-08-04 · `491d422`)*

2. **Release state comes from the registry and the tags, never from the
   manifests or the CHANGELOG.** Verify with `git tag`, `git ls-remote --tags
   origin` and `npm view <pkg> version` before a brief writes a version
   anywhere. This repo carried `1.4.0` in three manifests, a full CHANGELOG
   entry and a commit subject for a release that was never tagged and never
   published. *(Last fired: 2026-08-04 · `491d422`)*

3. **A stage-0 "absent" is perishable.** Decisions taken because a file does not
   exist — skipping the entry audit because there is no `DOCMAP.md`, no ADR
   directory, no register — must be re-checked before they are acted on. In a
   shared tree those files can appear an hour into the run.
   *(Last fired: 2026-08-04 · `491d422`)*

## Run stamps

| Date | Commit | Task | Diverged? |
|---|---|---|---|
| 2026-08-04 | `491d422` | `field-notes` style pack from graphify.com (v1.5.0, built; release held) | **yes** |

## Log

### 2026-08-04 — three runs, one working copy, one version number

**Symptom.** At stage 6, with every gate green, `git status` showed files this
run never touched: a rewritten `STYLE_PACK_TEMPLATE.md`, a `docs/DOCMAP.md`, an
`docs/adr/0001-*.md`, and two other runs' briefs. `git reflog` showed HEAD had
been moved off this run's branch at 19:07:50 by something else. At 19:17:35 a
concurrent run **reverted `test/validate.py`**, deleting two checks this run had
added and leaving the shared tree failing its own validator.

**Stage it surfaced at:** 6 (tests), while staging.
**Stage that owned it:** 0 — the grill's autonomy sweep has a *shared state* row
and this run answered it `ungated — single operator, single worktree`, from
assumption rather than from evidence.

**Root cause.** The sweep's shared-state question was treated as a property of
the operator ("one person, so one run") instead of a property of the
*directory*. Nothing was checked. Three other pipeline runs — `lecture-hall`,
`audit-harvest-v1.5.0` and a design-sync-bridge run — were already live in the
same checkout, and all three claimed `1.5.0`. One of them had detected the
collision and parked itself; this one had not looked.

A second, independent finding rode in on the first: `v1.4.0` exists in every
manifest, in the CHANGELOG and in a commit subject on `main`, and has never been
tagged or published. Tags stop at `v1.3.4`; npm serves `1.3.4`. This run's
REQ-011 ("npm shows 1.5.0") was written on top of a version history that was
not real, and would have gone green against a fiction if the concurrency had not
forced a stop.

**Fix, by grade.**
- *Standing instruction* (1) — check for concurrent runs from evidence, twice:
  at stage 0 and again before staging.
- *Standing instruction* (2) — read release state from tags and the registry.
- *Standing instruction* (3) — re-check stage-0 absences before acting on them.
- *Mechanical check* — none available: no lease mechanism is installed here.
  [agent-sync](https://github.com/ssheleg/agent-sync) is the tool for exactly
  this and is the right next step; until it is in place, instruction 1 is the
  only defence, which is why it is worded as a command rather than a caution.

**The check that catches it next time.** `git reflog -8` plus a branch listing
at stage 0, and a `git status --porcelain` diffed against this run's own file
list immediately before `git add`. Both are seconds; the failure they prevent
cost this run its entire release stage.

**What went right, worth keeping.** Committing an explicit path list rather than
`git add -A` meant three other runs' in-flight work stayed out of this commit,
and verifying the *commit* in a detached worktree rather than the shared tree
gave a trustworthy green (314 checks) from a directory nobody else was writing
to. Both are cheap habits that turned an unrecoverable mess into a clean commit.
