# Retrospective — sheleg-design-skill

The project's standing instructions and run log for task-pipeline. Stage 0
reads this file **in full**; stage 10 prunes, stamps, and writes an entry only
if the run diverged.

## Standing instructions (cap: 10 · current: 9)

Each one binds every run in this project until it is retired. Retire when it
became a mechanical check, when the paths it names are gone, or when it has not
fired in five run stamps.

1. **Never assume this checkout is yours alone.** Before stage 0 records shared
   state, run `git reflog -8`, `git branch -vv`, and look at working-tree
   mtimes. A HEAD move you did not make, a `feat/*` branch you did not create,
   or a file changing while you test means another pipeline run is live in the
   same directory. Recheck immediately before staging anything — the tree can
   turn hostile mid-run. *(Last fired: 2026-08-05 · `2ad45b2` — fired three
   times in one run: a stolen ADR number, a stolen scenario number, and a
   version number that was not only taken but already published.)*

2. **Release state comes from the registry and the tags, never from the
   manifests or the CHANGELOG.** Verify with `git tag`, `git ls-remote --tags
   origin` and `npm view <pkg> version` before a brief writes a version
   anywhere. This repo carried `1.4.0` in three manifests, a full CHANGELOG
   entry and a commit subject for a release that was never tagged and never
   published. *(Last fired: 2026-08-05 · `2ad45b2` — `npm view` is what showed
   that this run's chosen `1.6.0` was taken **and already shipped**.)*

3. **A stage-0 "absent" is perishable.** Decisions taken because a file does not
   exist — skipping the entry audit because there is no `DOCMAP.md`, no ADR
   directory, no register — must be re-checked before they are acted on. In a
   shared tree those files can appear an hour into the run.
   *(Last fired: 2026-08-05 · `2ad45b2` — `docs/adr/` was absent at stage 0 and
   held a committed `ADR-0001` by stage 5.)*

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
   *(Last fired: 2026-08-05 · `2ad45b2` — twelve planted defects, one per kit
   check, every FAIL line recorded before the check was allowed to land.)*

7. **A gate that CI does not run is not shipped.** Adding a check to
   `package.json` scripts is half the work; the release gate is
   `.github/workflows/validate.yml`. Before closing any run that adds a check,
   diff the scripts against the workflow steps — `npm test` ran three gates
   while CI ran one for a whole release cycle, so a merge's green described a
   third of the suite. Instruction 6 says a gate must be watched saying no;
   this one says it must be watched saying anything at all.
   *(Last fired: 2026-08-04 · `623d2fb`)*

8. **A delegated finding is a hypothesis until you reproduce it against the
   artifact.** A subagent reports what it believes, and belief arrives in the
   same prose as evidence — most convincingly right after the same agent was
   right about something subtle. Reproduce the claim yourself before acting,
   with a control case that must fail, and never edit something already shipped
   on a report alone. This run was one step from "fixing" `--cta-sheen` in a
   released token layer; `CSS.supports` in a real browser said the CSS is valid
   and a genuinely invalid gradient returned false, so the test discriminated
   and the pack was left alone. Record refuted claims too: a claim disproved and
   never written down comes back as folklore.
   *(Last fired: 2026-08-08 · `025f866` — a subagent reported that `field-notes`
   contradicts itself about `--deep`. Reproduced against both files: the claim
   is true. Still not acted on, because the pack is shipped and the fix is a
   judgement call rather than a typo. Logged for its author instead.)*

9. **A close-out artifact is verified by the artifact changing, not by the
   command exiting 0.** Stage 9 refreshes three things — module docs, the wiki,
   the code graph — and each has a command that can succeed at running while
   failing at its job. `graphify . --update` **exited 0** having printed
   `error: no LLM API key found` and changed nothing; the graph kept a
   `built_at_commit` three commits stale, and the run would have reported it
   refreshed. Check the artifact, not the exit code: `built_at_commit` against
   `git rev-parse HEAD`, the wiki page's version string against the tag, a
   doc's numbers against a fresh measurement. This is instruction 6 pointed at
   the close-out instead of at the gates — a green nobody watched land is not
   evidence there either.
   *(Last fired: 2026-08-08 · `025f866` — the run that wrote it.)*

## Prune log

- **2026-08-08 · nothing retired.** All eight were walked against the three
  triggers. Seven fired inside this run (1, 2, 4, 5, 6, 7, 8); instruction 3
  did not fire but is one stamp old, not five. Instruction 5 is the closest to
  retirement — `sloplint.py` now checks an addressable origin mechanically for
  any widened pack — but the check can only fire once a pack file exists, and
  what instruction 5 actually does is stop a pack from being *started* without a
  reference. Kept until that half is covered too.

## Run stamps

| Date | Commit | Task | Diverged? |
|---|---|---|---|
| 2026-08-04 | `491d422` | `field-notes` style pack from graphify.com (v1.5.0, built; release held) | **yes** |
| 2026-08-05 | `564ecec` | audit harvest — motion doctrine, dials, widened contract, two computed gates (v1.6.0) | **yes** |
| 2026-08-04 | `623d2fb` | release close-out — CI wired to all three gates; **`v1.6.0` shipped**: GitHub release + npm, first published version since `v1.3.4` | **yes** |
| 2026-08-05 | `2ad45b2` | Claude Design bridge + seven React reference kits; **`v1.7.0` shipped** | **yes** |
| 2026-08-08 | `025f866` | `cyclorama` style pack from codos.ai, eighth kit, ADR-0001 restored; **`v1.8.0` shipped** | **yes** |

## Log

### 2026-08-08 — a stage-0 decision the measurement refuted, and a refresh that reported success

**Symptom, the first one.** At stage 0 the operator chose, from three options,
to fix the reference's failing accent by adding a second text-safe token —
`--accent-ink`, the shape `field-notes` uses for `--brand-on-dark`. It is the
obvious repair and it was chosen on a reasonable premise. Two hours later, while
deriving the actual value, the premise turned out to be false: **every orange
dark enough to carry text collides with a semantic this palette already has.**
`#903A00` sits **4.6** from `--danger` against a hard floor of 10; `#A14700`
sits 7.4 under protanopia; `#C56200` sits **1.4** from `--warning` under
protanopia. The repair would have traded a WCAG failure for a colour-blindness
failure — and `--accent-ink` is not a name the palette gate treats as semantic,
so **no check would ever have said so.**

**Stage it surfaced at:** 4 (build), while computing the token.
**Stage that owned it:** 0 — the option was offered as though it were clean,
without the separation having been computed first.

**Root cause.** The three options were priced on contrast alone. Contrast is the
number that names the defect, so it is the number that gets checked; separation
is the number that decides whether the *fix* is legal, and it was not computed
until the fix was being written. A palette repair has two constraints and only
one of them is visible in the complaint.

**Fix, by grade.**
- *Mechanical* — none possible in the gate: `--accent-ink` would not be a peer,
  which is the whole trap. The stronger fix was **not to create the token**, so
  the collision cannot exist to be missed.
- *Note that expires in two runs* — when a colour repair is offered as an
  option, compute its separation from every semantic peer **before** offering
  it, not after it is chosen. Two commands, and it changes which options exist.

**What went right, worth keeping.** The reversal was taken back to the operator
out loud with all three candidates measured, rather than quietly substituted.
And the rejected candidates went **into the pack's Gotchas with their numbers**,
so the next person to notice the failing eyebrow does not re-derive the same
three dead ends — a negative result stored where the mistake would be made.

**Symptom, the second one.** `graphify . --update` at stage 9 **exited 0** while
printing `error: no LLM API key found (35 doc/paper/image file(s) need semantic
extraction)` and changing nothing. `built_at_commit` stayed at `97e7f63` while
HEAD was `025f866`. Nothing in the exit status distinguished "refreshed the
graph" from "refused to". Re-run with `--code-only` it did the code half —
987 → 1042 nodes, stamp now current — leaving the doc half a release behind,
which is visible in `god-nodes`, where a hub still reads "T1–T14" although there
are now fifteen scenarios.

**Stage it surfaced at:** 9, and only because the graph was inspected before and
after rather than trusted.
**Stage that owned it:** 9.

**Root cause.** The close-out stage inherited the habit of reading exit codes
from the gate stages, where exit codes are designed to mean something. A
third-party refresh command is not a gate and owes no such contract.

**Fix, by grade.** *Standing instruction* (9) — verify the artifact changed, not
that the command exited 0. Mechanical is possible later (compare
`built_at_commit` to `HEAD`) but `graphify-out/` is gitignored machine state, so
a repo gate cannot assume it exists; the instruction is the right grade for now.

**The check that catches it next time.** Read `built_at_commit` before and after
any graph refresh, and diff the wiki page's version string against the tag. Both
are one command; the failure they prevent is a stale graph carrying the
authority of a machine into the next run's harvest, which is the premise
everything downstream is built on.

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

### 2026-08-05 — the check caught what memory would have missed, and a report nearly cost a shipped pack

**Symptom, the good one.** The merge brought a seventh style pack from a
concurrent run. The first line out of the validator was
`kits/field-notes: no kit for style pack 'field-notes'` — a contract written
hours earlier, watched failing on a planted defect at the time, catching a real
gap created by someone else at the one moment two branches meet. Nobody
remembered the rule. The check did.

**Symptom, the bad one.** A subagent reported that `--cta-sheen` in the shipped
`orchard` token layer was syntactically invalid CSS, so the candy pill's sheen
was dead. It named a file and a value, and the fix looked like one line.
`radial-gradient(50% 50%, …)` is **valid** — two `<length-percentage>` values are
a legal radial size and the shape then defaults to ellipse. `CSS.supports`
returned true in a real browser, the parser kept the declaration, and a control
(`radial-gradient(nonsense, …)`) returned false, so the test discriminated. The
token layer was not touched.

**Stage it surfaced at:** 5 (build), reviewing a subagent's report.
**Stage that owned it:** 5 — the review step exists precisely because a report is
not a result.

**Root cause.** The same agent had just been right about a genuine, subtle gap in
the same file: no token for text on the accent, with `--panel` quietly standing
in for it. Being right about the hard thing is what makes the next claim easy to
believe. Confidence does not correlate with correctness, and a wrong fix to a
released token layer ships to everyone who copied it.

**Fix, by grade.**
- *Standing instruction* (8) — reproduce a delegated finding against the
  artifact, with a control case, before acting; record refutations.
- *Mechanical* — none possible. No check distinguishes a true report from a
  plausible one; this is one the machine cannot decide.

**A second finding, and this one was mechanical.** The CI matrix listed six packs
by hand, so the seventh kit was built, green, and **invisible to CI** — the exact
shape of instruction 7, one layer up. Fixed by deriving the matrix from `kits/`
rather than adding a seventh line, so no instruction was needed.

**What went right, worth keeping.** Every merge conflict across two collisions
was resolved by taking the other run's side first and re-applying this run's
change on top: eighteen commits of concurrent work survived byte-for-byte and the
overlay stayed reviewable. And one reusable ten-point verification script paid
for itself seven times — the alternative was believing seven subagent reports.

**The check that catches it next time.** For findings: reproduce, with a control
that must fail, before editing anything shipped. For lists: derive them.
