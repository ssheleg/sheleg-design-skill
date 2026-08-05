# Retrospective — sheleg-design-skill

The project's standing instructions and run log for task-pipeline. Stage 0
reads this file **in full**; stage 10 prunes, stamps, and writes an entry only
if the run diverged.

## Standing instructions (cap: 10 · current: 7)

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

4. **A scenario that asserts disambiguation must ship its negative branch.**
   "Does the agent pick the new pack?" cannot fail in the interesting
   direction — an agent that picks the newest pack for everything passes it.
   Every routing test in `test/scenarios.md` that claims pack A is
   distinguishable from pack B needs a second prompt that must still choose B,
   run in a separate fresh context. T13 is the shape to copy.
   *(Last fired: 2026-08-04 · `c324d1b`)*

5. **A pack needs an addressable origin before it needs anything else.** A
   production reference a reader can go and look at — a URL or a bare host —
   not a product name. No reference, no pack: the contract forbids invented
   values, and a synthesised palette with a citation attached is an invented
   value that looks sourced. This retired an eighth pack and a six-pack
   backfill in one run rather than shipping either.
   *(Last fired: 2026-08-04 · `1cc28f1`)*

6. **A gate is not evidence until it has been watched saying no.** Every new
   check ships with a planted defect it catches — as a `--self-test`, and once
   against a real file in the tree. Writing the self-tests in this run caught a
   `--self-test` flag that was never wired (the suite reported green for a
   self-test that did not run), two wrong fixtures, and a provenance check that
   rejected a real reference for lacking `https://`.
   *(Last fired: 2026-08-04 · `564ecec`)*

7. **A gate that CI does not run is not shipped.** Adding a check to
   `package.json` scripts is half the work; the release gate is
   `.github/workflows/validate.yml`. Before closing any run that adds a check,
   diff the scripts against the workflow steps — `npm test` ran three gates
   while CI ran one for a whole release cycle, so a merge's green described a
   third of the suite. Instruction 6 says a gate must be watched saying no;
   this one says it must be watched saying anything at all.
   *(Last fired: 2026-08-04 · `623d2fb`)*

## Run stamps

| Date | Commit | Task | Diverged? |
|---|---|---|---|
| 2026-08-04 | `491d422` | `field-notes` style pack from graphify.com (v1.5.0, built; release held) | **yes** |
| 2026-08-05 | `564ecec` | audit harvest — motion doctrine, dials, widened contract, two computed gates (v1.6.0) | **yes** |
| 2026-08-04 | `623d2fb` | release close-out — CI wired to all three gates; **`v1.6.0` shipped**: GitHub release + npm, first published version since `v1.3.4` | **yes** |

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

### 2026-08-05 — a self-test flag that did nothing, and a check that rejected real provenance

**Symptom.** `npm run selftest` reported success. `validate_palette.py` had no
argument handling at all, so `--self-test` fell through, the ordinary validation
pass ran, it exited 0, and the suite reported a green for a self-test that did
not exist — inside the script whose own docstring says a green from a check
nobody has watched fail is not evidence.

**Stage it surfaced at:** 9 (release), during a final verification sweep.
**Stage that owned it:** 6 — the script was wired into `package.json` on the
strength of its documented flag rather than a run of it.

**Root cause.** An unknown argument was silently ignored. Nothing distinguishes
"ran the self-test" from "ran something else" when both print `OK` and exit 0.

**Fix, by grade.**
- *Mechanical* — unknown arguments now exit 2 instead of falling through to the
  default path. The silence was the defect, not the missing feature.
- *Mechanical* — a real self-test: five planted defects, one per check, plus a
  clean palette that must stay quiet.
- *Standing instruction* (6) — every new gate is watched saying no.

**Two things it caught immediately, both mine.** Writing the fixtures failed two
of them: the "unreadable pair" was close enough at full colour to trip the hard
floor instead of the CVD floor, and the control "clean" palette used green and
red — the textbook colour-blindness failure, so the suite was right to call the
clean case dirty. Both fixtures were wrong; neither check was.

**And one caught by dry-running across branches.** Before merging, the
neighbouring run's finished pack was run through this branch's new gates. The
slop lint failed it for naming no addressable origin — while its `Origin:` reads
`**graphify.com** … read off its live computed styles`. The pack was right and
the check was wrong: it demanded a URL scheme when packs cite references the way
people say them. Fixed to accept a bare host, with fixtures pinning both
directions.

**The check that catches it next time.** Run the other branch's artifacts
through this branch's gates *before* the merge, not after. It cost one command
and turned a merge-day failure into a pre-merge fix.

### 2026-08-04 — the release found a gate CI had never run

**Symptom.** Verifying `main` before pushing the tag, `npm test` was found to
run `validate.py`, `validate_palette.py` and `sloplint.py`, while
`.github/workflows/validate.yml` ran only the first. The palette gate, the slop
lint and both `--self-test` flags had never executed on a push.

**Stage it surfaced at:** 7 (release), during the pre-push verification.
**Stage that owned it:** 6 — the run that added the gates tested them by hand
and wired them into `package.json`, which is where a human runs them and not
where a merge is judged.

**Root cause.** "Wired up" was read as "reachable by a command" rather than
"executed by the gate that guards the branch". Both readings are true of
`package.json`; only the second is true of CI.

**Fix, by grade.** *Mechanical* — four steps added to the workflow (both gates,
both self-tests), verified green on the tag. *Standing instruction* (7) — diff
the scripts against the workflow steps before closing a run that adds a check.

**The check that catches it next time.** `grep` every `test/*.py` against
`.github/workflows/*.yml`; a script the workflow never names is the finding.
Cheap enough to be worth automating the next time this class appears — which,
per the ratchet rule, would be its second appearance.

**What went right.** The release was gated on verifying a `main` this run did
not assemble. That verification is the only reason the gap was found before it
shipped rather than after, and it cost about a minute.
