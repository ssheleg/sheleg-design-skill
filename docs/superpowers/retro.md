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
   turn hostile mid-run. *(Last fired: 2026-08-05 · `75f3748` — fired three
   times in one run: a stolen ADR number, a stolen scenario number, a stolen
   and already-published version number.)*

2. **Release state comes from the registry and the tags, never from the
   manifests or the CHANGELOG.** Verify with `git tag`, `git ls-remote --tags
   origin` and `npm view <pkg> version` before a brief writes a version
   anywhere. This repo carried `1.4.0` in three manifests, a full CHANGELOG
   entry and a commit subject for a release that was never tagged and never
   published. *(Last fired: 2026-08-05 · `75f3748` — `npm view` is what revealed
   that this run's chosen 1.6.0 was taken **and already shipped**.)*

3. **A stage-0 "absent" is perishable.** Decisions taken because a file does not
   exist — skipping the entry audit because there is no `DOCMAP.md`, no ADR
   directory, no register — must be re-checked before they are acted on. In a
   shared tree those files can appear an hour into the run.
   *(Last fired: 2026-08-05 · `75f3748` — `docs/adr/` was absent at stage 0 and
   held a committed ADR-0001 by stage 5.)*

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
   *(Last fired: 2026-08-05 · `75f3748` — twelve planted defects, one per kit
   check, each FAIL line recorded before the check was allowed to land.)*

7. **A delegated finding is a hypothesis until you check it against the
   artifact.** A subagent reports what it believes; belief arrives in the same
   prose as evidence. Reproduce the claim yourself before acting on it —
   especially when acting means editing something already shipped. This run was
   one step from "fixing" `--cta-sheen` in a released token layer on a report
   that it was invalid CSS; `CSS.supports` in a real browser said it is valid,
   and the discriminating control case (a genuinely invalid gradient) returned
   false, so the test itself was trustworthy. Record refuted claims too — a
   claim that is disproved and never written down comes back as folklore.
   *(Last fired: 2026-08-05 · `75f3748`)*

## Run stamps

| Date | Commit | Task | Diverged? |
|---|---|---|---|
| 2026-08-04 | `491d422` | `field-notes` style pack from graphify.com (v1.5.0, built; release held) | **yes** |
| 2026-08-05 | `564ecec` | audit harvest — motion doctrine, dials, widened contract, two computed gates (v1.6.0) | **yes** |
| 2026-08-05 | `75f3748` | Claude Design bridge + seven React reference kits (v1.7.0, released) | **yes** |

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

### 2026-08-05 — the check caught what memory would have missed, and a report nearly cost a shipped pack

**Symptom, the good one.** The merge brought a seventh style pack from a
concurrent run. The first line out of the validator was
`kits/field-notes: no kit for style pack 'field-notes'` — a contract written
three hours earlier, watched failing on a planted defect at the time, catching a
real gap created by someone else at the one moment two branches met. Nobody
remembered the rule; the check did.

**Symptom, the bad one.** A subagent reported that `--cta-sheen` in the shipped
`orchard` token layer was syntactically invalid CSS and its sheen therefore
dead. It reads like a finding, it names a file and a value, and the fix looked
like one line. `radial-gradient(50% 50%, …)` is **valid**: two
`<length-percentage>` values are a legal radial size and the shape then defaults
to ellipse. `CSS.supports` returned true in a real browser and the parser kept
the declaration, while a control case (`radial-gradient(nonsense, …)`) returned
false, so the test discriminated. The token layer was not touched.

**Stage it surfaced at:** 5 (build), on reviewing a subagent's report.
**Stage that owned it:** 5 — the review step exists precisely so a report is not
the same thing as a result.

**Root cause.** A subagent's report arrives in the register of a conclusion. It
had already been right about a genuine, subtle gap in the same file (no token for
text on the accent), which is exactly what makes the next claim easy to believe.
Confidence is not correlated with correctness, and a wrong "fix" to a released
token layer would have shipped to everyone who copied it.

**Fix, by grade.**
- *Standing instruction* (7) — reproduce a delegated finding against the artifact
  before acting, and record refuted claims so they do not return as folklore.
- *Mechanical* — none possible: no check can tell a true report from a plausible
  one. This is one of the rules a machine cannot decide.

**A second, cheaper finding, already mechanical.** The CI matrix listed six packs
by hand, so the seventh kit was built, green, and invisible to CI. Fixed by
**deriving the matrix from `kits/`** rather than adding a seventh line — a
hand-maintained list is the same defect class the kit check catches, one layer
up. No standing instruction, because the mechanical fix removes the need for one.

**What went right, worth keeping.** Resolving every merge conflict by *taking the
other run's side first and re-applying this run's change on top* meant eighteen
commits of concurrent work survived byte-for-byte while the overlay stayed
reviewable. And writing one reusable ten-point verification script paid for
itself seven times over — reading seven subagent reports would have been
believing seven of them.

**The check that catches it next time.** For findings: reproduce, with a control
case that must fail, before editing anything shipped. For lists: derive them.
