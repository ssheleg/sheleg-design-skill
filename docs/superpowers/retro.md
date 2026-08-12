# Retrospective — sheleg-design-skill

The project's standing instructions and run log for task-pipeline. Stage 0
reads this file **in full**; stage 10 prunes, stamps, and writes an entry only
if the run diverged.

## Standing instructions (cap: 10 · current: 10)

Each one binds every run in this project until it is retired. Retire when it
became a mechanical check, when the paths it names are gone, or when it has not
fired in five run stamps.

1. **Never assume this checkout is yours alone.** Before stage 0 records shared
   state, run `git reflog -8`, `git branch -vv`, and look at working-tree
   mtimes. A HEAD move you did not make, a `feat/*` branch you did not create,
   or a file changing while you test means another pipeline run is live in the
   same directory. Recheck immediately before staging anything — the tree can
   turn hostile mid-run. *(Last fired: 2026-08-12 · `e9b753f` — and it fired **late**: the
   prescribed commands were run at close-out rather than before staging, on the strength of
   a clean session-start snapshot and `git status`. Clean either way — one worktree, two
   branches both at `e9b753f`, no foreign HEAD move — but a check run after the staging it
   protects is a check that cannot protect it. Previously: 2026-08-10 `89a8798` — clean again: one branch, one
   worktree, no foreign HEAD move. The point stands: the answer is only worth having because it came
   from evidence. Its sharpest firing remains 2026-08-05 `2ad45b2`, where it
   caught a stolen ADR number, a stolen scenario number, and a version already
   published.)*

2. **Release state comes from the registry and the tags, never from the
   manifests or the CHANGELOG.** Verify with `git tag`, `git ls-remote --tags
   origin` and `npm view <pkg> version` before a brief writes a version
   anywhere. This repo carried `1.4.0` in three manifests, a full CHANGELOG
   entry and a commit subject for a release that was never tagged and never
   published. *(Last fired: 2026-08-12 · `e9b753f` — `npm view` 1.13.0 against
   `ls-remote --tags | sort -V` v1.13.0 after the release, and it settled a live
   ambiguity: a local `npm publish` returned 403 "cannot publish over the previously
   published versions" while the registry showed 1.13.0 published *seconds later* with
   provenance and a different shasum. The manifests could not have answered that; the
   registry did — the tag had triggered the release workflow, which published first, and
   the local attempt was correctly refused. Previously: 2026-08-10 `89a8798` — and it nearly produced a false
   negative: `git tag | tail` and `ls-remote | tail` both sort lexically, where
   `v1.10.0` lands **before** `v1.9.0`, so the tag looked missing. `--sort=v:refname`
   and `sort -V` showed it present on both sides. A glance is not the check.
   Previously checked at stage 0 and again immediately before the tag. Its sharpest firing remains 2026-08-05
   `2ad45b2`, where `npm view` showed the chosen `1.6.0` already shipped.)*

3. **A scenario written is not a scenario run, and the difference is stated in the
   scenario.** `test/scenarios.md` is the only place this repository tests the thing it
   actually ships — an agent reading the skill and choosing correctly — and it is a
   harness a human has to start. So every scenario carries a result line, and a scenario
   that has not been executed says **"written, not yet run"** with the reason, in the
   file, at the moment it is written. Never a blank, and never a verdict inferred from
   the author's confidence: the author of a pack cannot pass its routing test, because
   they already know the answer. When a run cannot execute one — no subagents, no
   session, no time — it ships the debt in the same commit as the artifact and names it
   in the release notes, so the next run inherits a list rather than a silence. Five
   application scenarios sat unrecorded across four releases (2026-08-10), which is what
   an unstated debt looks like after it has been left alone.
   *(Added 2026-08-12 · `e9b753f`, replacing the retired "a stage-0 absent is
   perishable". First instance: T23, `scoreboard` against `field-notes`, shipped with
   both branches and no result. **Closed the same day** — the debt was stated, the runs
   were authorised, and the pair went green with nine findings, eight confirmed against
   the artifact and one refuted. The rule's whole value showed up in that gap: a written
   result line is what made the owed run findable an hour later instead of five releases
   later.)*

4. **A scenario that asserts disambiguation must ship its negative branch.**
   "Does the agent pick the new pack?" cannot fail in the interesting
   direction — an agent that picks the newest pack for everything passes it.
   Every routing test in `test/scenarios.md` that claims pack A is
   distinguishable from pack B needs a second prompt that must still choose B,
   run in a separate fresh context. T13 is the shape to copy.
   *(Last fired: 2026-08-12 · `e9b753f` — **half.** T23 ships with its negative branch
   written (`scoreboard` vs `field-notes`, the two closest packs in the library) and with
   **no result**, because subagent runs were disabled for the session. The scenario's
   result line says so rather than claiming a green. This instruction covers the shape of
   the scenario; nothing in it covers a scenario that is never run, which is the gap this
   firing exposes. Previously: 2026-08-09 · `b426ccc` — four pairs, eight fresh contexts, all
   green; and the negative branches are what proved the fork clauses are read
   from both sides.)*

5. **A pack needs an addressable origin before it needs anything else.** A
   production reference a reader can go and look at — a URL or a bare host —
   not a product name. No reference, no pack: the contract forbids invented
   values, and a synthesised palette with a citation attached is an invented
   value that looks sourced. This retired an eighth pack and a six-pack
   backfill in one run rather than shipping either.
   *(Last fired: 2026-08-12 · `e9b753f` — one reference, one URL, and the pack was
   measured off the reference's own shipped stylesheet rather than off a screenshot. The
   two places a value had no reference behind it — the paper status set and the chart
   ramp — are marked `SELECTED` at the declaration, with the file's header defining what
   that word costs against `MEASURED`. Previously: 2026-08-09 · `b426ccc` — four references, four URLs, and the
   one place a value had no reference behind it, `maquette`'s status set, is
   marked as a pack decision at the declaration rather than passed off as
   extracted.)*

6. **A gate is not evidence until it has been watched saying no — and the fix
   goes to every sibling in the same pass.** Every new check ships with a planted
   defect it catches, as a `--self-test` **and** once against a real file in the
   tree. When a defect is found in one gate, apply the fix to the other gates
   before closing: this instruction has existed since 2026-08-05, when
   `validate_palette.py` was found reporting green for a `--self-test` it never
   ran — and on 2026-08-10 `validate.py` and `sloplint.py` were **still** doing
   exactly that, because the 2026-08-05 run fixed the script in front of it. A
   defect class found once is a defect class present everywhere until checked.
   **The sweep is over the class, not the siblings.** "Sibling" first meant
   *the other scripts*; on 2026-08-10 it turned out to be too narrow. The
   1.10.0 run found a rule inside the shipped bundle citing a repo-only path,
   fixed it, and swept the literal form — repo paths in backticks went to zero
   and stayed there. Two more instances shipped anyway, because they were not
   paths: a rule telling the reader to record a version the bundle does not
   carry, and an argument built on "the same six component names" that names
   none. Same class, different shape. So: after fixing a defect, say what
   *class* it belongs to in one sentence, enumerate the shapes that class can
   take, and check each — a sweep that greps for the string you just fixed
   finds only the string you just fixed. And a check that fires on a substring
   can be evaded by rephrasing the very sentence it protects: prefer an
   unconditional assertion, and prove each planted defect fails with **its own
   check's message**, not merely that the suite went red.
   *(Last fired: 2026-08-12 · `e9b753f` — and the class was **the entry point that
   drops a status the script already computed**, which is the 2026-08-05 argv defect one
   layer down: `validate.py --self-test` printed FAILED and exited 0 because `main()`
   returned the status and `__main__` called it bare. Watched saying no by breaking a
   fixture in a copy of the tree — 0 before, 1 after. Shapes enumerated and each checked
   rather than grepped for: the other two gates' entry points (`sys.exit(main())`,
   `raise SystemExit(main())` — clean), every `check_floor` return path, the self-test's
   own `subprocess.returncode`, `package.json`'s six script chains (all `&&`, none `;`),
   and the workflows for `continue-on-error`, `|| true` and pipes that swallow a gate's
   exit — none present. The second defect is the same class pointed at fixtures: a plant
   pinned to `**twelve locked style packs**` stopped mutating anything the first time the
   library grew, and reported BROKEN into an exit code nobody read. Previously:
   2026-08-10 · `89a8798` — three new forms, each watched failing
   and each discriminated by its own message; one of them was found evadable by
   a reviewer and made unconditional before shipping. Its previous sharpest
   firing, 2026-08-10 `3af6d97`, found the same argv defect in two more
   scripts.)*

7. **A gate that CI does not run is not shipped.** Adding a check to
   `package.json` scripts is half the work; the release gate is
   `.github/workflows/validate.yml`. Before closing any run that adds a check,
   diff the scripts against the workflow steps — `npm test` ran three gates
   while CI ran one for a whole release cycle, so a merge's green described a
   third of the suite. Instruction 6 says a gate must be watched saying no;
   this one says it must be watched saying anything at all.
   *(Last fired: 2026-08-12 · `e9b753f` — diffed again, and this is the run where it
   would have mattered: the self-test whose exit code was dropped runs in CI through
   `npm run selftest`, so CI had been reporting green for a self-test that could not fail
   it. No workflow change was needed — the fix was in the script CI already runs — but
   "CI runs it" was true the whole time and worth nothing while the script could not say
   no. Previously: 2026-08-10 · `89a8798` — diffed again; the new self-sufficiency
   check lives inside `validate.py`, which CI already runs, so it needed no workflow
   change. Noted rather than assumed, again. Previously: `b426ccc` — the reciprocity check
   lives inside `validate.py`, which CI already runs, so it needed no workflow
   change. That is worth noting rather than assuming.)*

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
   *(Last fired: 2026-08-12 · `50dc7e6` — nine times, and it corrected **me** rather
   than the agents. Both T23 branches returned findings on a pack I had written that
   morning; every one was recomputed against the token layer before an edit. Eight
   reproduced, including four ratios I had stated from the OKLCH instead of the shipped
   hex. One was refuted — `--on-accent` was called a dead token, and its consumer is the
   selected chip at 4.92:1 — and is written into the scenario's result anyway. The
   sharpest turn: on the focus ring the agents' number (1.29:1) was right and my
   reproduction (1.16:1) was wrong, because I composited alpha in linear light and a
   browser composites in sRGB. Reproducing a claim is not the same as reproducing it
   correctly, and the control that settled it was matching their method rather than
   defending mine. Previously: 2026-08-10 · `89a8798` — eleven times. Six scenario agents'
   findings were each reproduced against the artifact before any edit, and one of
   mine was refuted that way: I predicted the gate's 1368-vs-1366 gap came from
   untracked `graphify-out/` files, hid the directory, and the count did not move —
   the real cause was two commits landing after the floor was measured, proven by
   running the gate at `3af6d97` in a throwaway worktree. Then a code reviewer
   returned five findings on my own diff; two were right about text I had just
   written, and one made me concede that splitting the front-matter budget is a
   loosening rather than a correction. Earlier: 2026-08-08 · `025f866` — a subagent reported that `field-notes`
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
   *(Last fired: 2026-08-12 · `e9b753f` — the published tarball was pulled from the
   registry and read: 418 files carrying `styles/scoreboard.md`, its token layer and the
   whole kit. The local channels were verified by reading installed files rather than the
   updater's output — the hub copy's `SKILL.md` says `version: 1.13.0` and its `styles/`
   holds `scoreboard.md`, and the shadow check printed nothing. In the same output the
   updater failed to refresh one unrelated marketplace and still reported the plugin
   updated, which is the exact shape this instruction exists for. Previously:
   2026-08-10 · `89a8798` — the published tarball was unpacked and
   the three fixed forms checked inside it, and the two local install channels were
   verified by reading their installed files rather than by the updater's output.)*

10. **A batch of new artifacts must be checked against each other, not only
   against what already existed.** When several things land in one run, the
   author has spent hours on how each differs from the *old* set and no time at
   all on how they differ from *each other* — so same-batch relationships are the
   ones that go undrawn. This run added four style packs, wrote a fork from each
   into the existing packs, added a check enforcing reciprocity, and still
   shipped three packs serving one product category with **no fork between
   them**; two test agents found it and one had to derive the distinction itself.
   The check was real and the coverage was not: after any batch, enumerate the
   new set pairwise and ask what happens to a reader who confuses two of them.
   *(Last fired: 2026-08-12 · `e9b753f` — **weakly, and the weakness is worth naming.**
   One pack landed, so there was no new batch to enumerate against itself; the pairwise
   question was asked against the existing thirteen instead, and it found the real edge —
   `scoreboard` and `field-notes` share warm paper, one orange-red accent and hairline
   rules, and differ only in what the small type is doing. Forks written from both sides
   and enforced by `validate_fork_reciprocity()`. A single-artifact run is where this
   instruction is easiest to skip and where the confusable neighbour is likeliest to be an
   old one. Previously: 2026-08-10 · `89a8798` — the three new check forms enumerated
   pairwise, which is how form 2 was found to be gated on a substring and made
   unconditional.)*

## Prune log

- **2026-08-12 (`e9b753f`) · one retired, one added (still 10, at cap).** All ten
  walked against the three triggers. **Eight fired** — 1 (late, and recorded as late),
  2 (it settled a live registry-vs-manifest ambiguity mid-release), 4 (**half**: T23
  ships its negative branch and no result), 5, 6 (the entry point that drops a computed
  status, swept over five shapes), 7, 9 (tarball unpacked, both install channels read),
  10 (weakly — one artifact, so the pairwise question was asked against the old set).
  Instruction 8 was walked and correctly found **not applicable**: no work was delegated,
  because subagent runs were disabled for the session, so there was no delegated finding
  to reproduce.
  **Instruction 3 did not fire for the fifth consecutive stamp and is retired.** Its
  trigger — a stage-0 "absent" acted on later — has not occurred since 2026-08-05, and
  the two things that made it dangerous are now covered mechanically: `validate_links()`
  resolves every relative path in the tree, and `docs/DOCMAP.md` names where each kind of
  artifact lives, so "there is no ADR directory" is a claim the tree answers rather than
  a memory. It is retired for staleness, not because the failure it describes became
  impossible; if a run is ever taken in a genuinely shared checkout again, re-add it.
  **Added in its place, at the same cap: instruction 3 (new) — a scenario written is not
  a scenario run.** This run produced the first scenario in the harness that ships with
  its result line saying *owed*. Instruction 4 governs the scenario's shape and says
  nothing about whether anyone executed it, which is exactly how T2, T3, T7, T9 and T14
  sat unrecorded for four releases (see the 2026-08-10 log entry). The new rule makes the
  debt explicit and time-boxed rather than leaving it to be noticed.

- **2026-08-10 (`89a8798`) · nothing retired; nothing added (still 10, at cap);
  instruction 6 widened.** All ten walked against the three triggers. **Nine
  fired** — 1, 2 (and nearly gave a false negative: lexical tag sort), 5 (the T7
  authoring agent measured a live reference with a URL), 6 (three new forms,
  each discriminated by its own message), 7, 8 (eleven times, including one of
  my own predictions refuted by its control), 9 (tarball unpacked, both install
  channels read), 10 (the new forms enumerated pairwise, which is how form 2 was
  found evadable). Instruction 4 was walked and correctly found **not
  applicable**: T21 asserts application, not disambiguation, so it owes no
  negative branch — a rule that does not fire because it does not apply is not a
  rule going stale.
  **Instruction 3 still did not fire and is now four stamps old.** One more
  silent run retires it. It stays only because the trigger is five, not four.
  **Instruction 6 was widened rather than duplicated, for the second run
  running** — the sweep it mandates now covers the defect *class* and its shapes,
  not the sibling scripts, because this run's whole finding is that the last run
  swept a string and left the class. An eleventh rule saying "sweep the class"
  beside a sixth saying "sweep the siblings" would be two rules for one idea, and
  the cap exists to prevent exactly that.

- **2026-08-10 · nothing retired; nothing added (still 10, at cap).** All ten
  walked against the three triggers. Eight fired inside this run — 1 (twice: at
  stage 0 and again immediately before staging, clean both times), 2 (the release
  path read from tags and the registry, and the local `npm whoami` 401 turned out
  to be irrelevant because the workflow publishes), 4 (routing pairs re-run in
  fresh contexts after the SKILL.md table changed), 5 (it is why three packs were
  *not* backfilled and went to the board instead), 6 (six planted defects), 7
  (scripts diffed against both workflows; the release path was gated on one of
  three and now runs all), 9 (the graph refresh checked by `built_at_commit`, not
  by exit code), 10 (the six new checks enumerated pairwise against each other —
  `validate_contract_declaration` and `validate_contract_terminology` overlap on
  the word "thirteen" and were given non-overlapping messages).
  **Instruction 3 did not fire and is now three stamps old, not five** — it stays
  the retirement candidate. Instruction 6 was **strengthened rather than
  duplicated**: this run's sharpest finding is that a defect fixed in one script
  survived in two siblings for five days, which is a widening of 6, not an
  eleventh rule. The cap held without a deletion.

- **2026-08-09 · nothing retired; one added (9 → 10, at cap).** Nine walked
  against the three triggers. Eight fired inside this run — 1 (twice), 2 (twice),
  4 (four pairs), 5, 6 (a planted defect for the new check), 7, 8 (three times),
  9. Instruction 3 did not fire and is now two stamps old, not five. Instruction
  5 remains the closest to retirement for the same reason as last time and is
  kept for the same reason. **The list is now at its cap: the next run that wants
  to add one must retire one, and instruction 3 is the candidate.**

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
| 2026-08-09 | `b426ccc` | four packs — showroom, blueprint, prism, maquette — plus reciprocal forks and a check for them; **`v1.9.0` shipped** | **yes** |
| 2026-08-10 | `3af6d97` | fresh-eyes audit of the whole skill; six new checks, three gate defects reproduced and fixed, thirteen wrong ratios corrected; **`v1.10.0` shipped** | **yes** |
| 2026-08-10 | `89a8798` | repeat audit run as application scenarios; the bundle made self-sufficient, the defect class gated, the hook contradiction resolved; **`v1.11.0` shipped** | **yes** |
| 2026-08-11 | `eb13099` / `13f0a3f` | mobile becomes a named register; Mobbin joins the sweep slot; **`v1.12.0` and `v1.12.1` shipped** | no |
| 2026-08-12 | `e9b753f` | `scoreboard` style pack from get-ryze.ai, thirteenth kit, two gate defects fixed; **`v1.13.0` shipped** | **yes** |

## Log

### 2026-08-12 — the self-test said FAILED and the gate said 0

**Symptom.** A release-time count change broke one of `validate.py`'s planted defects:
the stale-count plant searched for the literal `**twelve locked style packs**`, which
this run had just rewritten to *thirteen*, so the fixture mutated nothing and the
harness printed `BROKEN … the fixture changed nothing in README.md` followed by
`self-test FAILED: a planted defect went undetected`. The suite it runs inside exited
**0**, and `npm test` was green.

**Surfaced at** the gate-raising step, by reading output that had already scrolled past
a green summary. **Owned by** whichever run added the argv handling in `main()` — the
comment three lines above the bug says, in this repository's own words, *"an unknown
flag silently running the normal pass is how a suite reports green for a self-test it
never ran"*.

**Root cause, in two layers.** `main()` **returned** `self_test()`'s status and
`__main__` called `main()` bare, so the value was computed, formatted into a failure
message, printed to stderr, and dropped. The sibling gates both propagate
(`sys.exit(main())`, `raise SystemExit(main())`); the one that had been repaired at the
argv layer was the one still broken at the exit layer, because the fix had been aimed at
the argument and not at the status. The second layer is the fixture: pinning a plant to
a literal that every release edits guarantees it stops testing the check it exists for,
and the only thing that would have reported that was the exit code nobody read. Two
defects, one class — **a status the program computed and its exit path discarded** —
and each was the other's cover.

**Fixes by grade.** *Structural:* `raise SystemExit(main())`, watched saying no by
breaking a fixture in a copy of the tree (0 before, 1 after). *Structural:* the plant now
reads whatever number the README claims and makes that number wrong, so it cannot go
quiet again. *Process:* the class was swept over its shapes rather than its string — the
other two entry points, every `check_floor` return path, the self-test's own
`subprocess.returncode`, `package.json`'s six script chains, and the workflows for
`continue-on-error`, `|| true` and pipes that swallow a gate's exit. None of the other
shapes was present, which is worth recording precisely because a sweep that finds nothing
is the only kind that can be trusted later.

**What the pack run itself found.** `scoreboard`'s reference sets a positive delta in
`#00D492` **on white** — 1.84:1, an invisible success state — at 11px inside its own
product screenshots. The pack keeps the colour and confines it to the dark panel, where
it measures 10.21:1. Two more corrections went the same way: a 500ms button transition
past the doctrine's 300ms ceiling, and a scan line animating `top`. All three are in
`Gotchas` rather than silently applied, because a correction nobody can see is a value
the next reader will re-derive from the reference and call a finding.

**The debt this run ships.** T23 — `scoreboard` against `field-notes`, the two closest
packs in the library — is written with both branches and **no result**, because subagent
runs were disabled for the session. That is now instruction 3.

**The check that catches it next time.** The exit path is mechanical. What stays human:
*is there anything else this suite computes and then declines to act on?* The honest
limit is that a self-test cannot test its own runner — the proof here came from breaking
a fixture by hand in a throwaway copy, and that is the technique to repeat, not a check
to add.

### 2026-08-10 — the class was not swept, and the harness had never tested using

**Symptom.** Three separate rules inside the shipped bundle instructed the reader
to use something only the repository has: `DESIGN_SYNC_BRIDGE.md` §7 said to
record the pack version into the synced project, and no version existed anywhere
in the bundle; §1 argued from "the same six component names" and named none of
them; and the rule that decides a pack author's contract — *do not ship on the
nine* — lived in `CONTRIBUTING.md`, which no install contains. All three read as
authoritative right up to the moment an agent tried to follow one.

**Surfaced at** stage 0, in a repeat audit, by fresh-context agents doing real
work. **Owned by** stage 10 of the *previous* run, whose acceptance had written
the instruction to check this and whose fix had covered one instance.

**Root cause.** 1.10.0 found this defect once, fixed it, and swept the **literal
form**: repo-only paths in backticks, which went to zero and are still zero. The
two shapes that are not paths were never looked for, because the sweep was a
grep for the thing already fixed. A class-level defect fixed at instance level
leaves the class intact and the count of known instances at one, which reads like
completeness.

**Second finding, and the reason the first went unseen so long.** The scenario
harness had 21 scenarios and had never recorded a result for the ones that test
*application* — T2, T3, T7, T9, T14 all sat unrecorded while every routing pair
carried a verdict. So the repository could not answer "do the usage scenarios
work" for the case the library is used in most, and the bundle-only defects are
invisible to a routing question by construction: choosing a pack never asks the
bundle for a version. The run that found this had to invent T21 — build something
real on a `core` pack — because no scenario covered it.

**Fixes by grade.** *Structural:* `validate_bundle_self_sufficiency()` over the
three shipped shapes, each watched failing and each discriminated by its own
message; `metadata.version` in the bundle making version sync five-way. *Doc:*
the authoring rules moved into the shipped template, the spine named, the
`useGSAP` contradiction resolved, `arcAmp` and `drop` declared as tuning
constants. *Process:* instruction 6 widened from siblings to shapes.

**The check that catches it next time.** The three forms are mechanical now, so a
fourth instance has to be a *new* shape — which is the honest limit and is written
into the check's own comment. The question that stays human: *what else does the
bundle tell a reader to do with something it does not contain?*

**A near-miss worth recording.** I predicted the gate's 1368-vs-1366 gap came from
untracked `graphify-out/` files being walked by the link checker. Plausible,
specific, and wrong: hiding the directory did not move the count. The real cause
was two commits landing after the floor was measured, proven by running the gate
at `3af6d97` in a throwaway worktree — exactly 1366. Had I written the first
version up, the repository would now carry a defect note describing a defect that
does not exist, which is worse than the gap it purported to explain.

### 2026-08-10 — 1270 green checks, and none of them were looking at the claims

**Symptom.** A fresh-eyes audit at `7abe96e`, with all three gates green
(1270 / 412 / 224), CI green and the package published, found that the skill
told a reading agent there were **six** style packs (twelve), handed the chart
layer a token ramp **no pack defines**, left **six of twelve packs** silent on
component states, heroes and breakpoints without saying which, and stated
**thirteen contrast ratios that are wrong**.

**Stage it surfaced at:** 0 — the harvest, before a single question.
**Stage that owned it:** every prior run's stage 6, and this is the point. No
individual run shipped a lie; each shipped a true sentence that a later run made
false, into a file nothing derived from.

**Root cause, and it has two halves.**

*A claim with no owner.* `validate.py` checked that each pack's **name** appears
in the README, the CLI and the rules. It never checked a **number**. So twelve
names sat in a table under a sentence that said six, for four releases. Counts,
token names and contrast ratios are all *derived* facts that were being
hand-copied into three places each — and the one class of claim a machine can
settle outright was the only class nothing checked.

*A check that cannot fail.* Three, reproduced with controls:

- Stripping a pack's four widened headings made **both** gates quieter
  (1270→1269, 224→223) and both exited 0. The ratchet was a sentence in
  `DOCMAP.md` and nothing else.
- One decoy comment disabled a slop-lint ban for a whole file, permanently — the
  check took the first match only and `continue`d, so the counter fell too.
  Identical CSS failed without the comment and passed with it.
- `validate.py --self-test` printed OK for a self-test that did not exist.

**Fix, by grade.**
- *Mechanical* — six new checks, each watched failing on a planted defect and
  against a real file: counted claims (whitespace-normalised, because the
  README's was split across a line break and no line-based grep could see it),
  exhaustive pack enumerations, one name for the contract, the `Contract:`
  declaration, the core role vocabulary, and every stated contrast ratio
  recomputed from the token layer.
- *Mechanical* — ratchet floors in `test/floors.json`, enforced by all three
  gates; unknown arguments exit 2 everywhere; `validate.py` gains a real
  self-test that runs against a copy of the tree.
- *Standing instruction 6, strengthened* — when a defect is found in one gate,
  sweep the siblings in the same pass.

**Two things worth keeping.**

*The scoping lesson.* The first draft of the ratio checker inferred which colour
pair a claim referred to and produced **22 false positives out of 40**. Narrowing
it to claims whose base the document *declares* — a column headed ``On `--bg` ``,
an `on/over --token` phrase, an `--on-X` name — took it to zero false positives
while keeping every true one. A gate people learn to ignore is worse than no
gate, so the scope is written into the code with the reason.

*Three of my own checks were wrong the first time, and each was caught by
running it.* The heading check matched substrings, so the core-contract note —
which names the four sections a pack omits — made six packs look widened the
moment they declared they were not. The em-dash range guard silently dropped four
real defects. A partner-resolution edit dropped explicitly-named partners and
flagged six correct claims in `field-notes`. None of these would have been found
by reading the diff.

**A finding recorded is not a finding fixed.** The self-test defect was recorded
on 2026-08-05 and was still live in two other scripts. `DOCMAP.md`'s "all nine
headings" was closed as REQ-018 on 2026-08-08 and was still live in four other
files — one of which, `DESIGN_SYNC_BRIDGE.md`, actively instructed an author to
ship a nine-heading pack, which the gate then passed because nine is the floor.
`test/scenarios.md` recorded a `blueprint` contradiction as "fixed in the same
run" while only half of it had landed.

**The check that catches it next time.** For claims: derive them, or check them —
never restate them. For fixes: standing instruction 9 already says a close-out
artifact is verified by the artifact changing rather than by the command exiting
0; this run shows the same sentence is true of a *fix*, and of a retrospective
entry. Grep for the class, not for the instance.

### 2026-08-09 — the fix that shipped with the same hole it was fixing

**Symptom.** Stage 0 found that five of the eight shipped packs named no other
pack at all: every disambiguation pointed backwards, at packs that never pointed
back, so an agent entering the table at `instrument-console` learned nothing. The
run fixed it properly — mirror clauses in four existing packs, plus a
`validate_fork_reciprocity()` check watched failing against a planted one-way
edge.

Then two scenario agents, independently, reported that **the three packs added in
this very run for vector-database companies did not fork against each other.**
One said outright that it had to derive the distinction because it was not
written down. `grep` confirmed it in a second.

**Stage it surfaced at:** 6 (tests), from the routing pairs.
**Stage that owned it:** 4 — the same stage that wrote the reciprocity fix.

**Root cause.** The fix was scoped to the relationship the run had been thinking
about: *new pack versus the existing library*. Every one of those edges got
drawn, and the check enforced them. Nobody asked about the edges **inside the
batch** — and those were the most confusable pairs in the whole library, because
three of the four new packs share a product category exactly.

The reason it is invisible is worth naming: after hours of work on four packs,
their differences feel enormous to the author. To a reader matching on category
they are one thing with four names.

**Fix, by grade.**
- *Mechanical* — none available. The reciprocity check can enforce an edge that
  exists; it cannot know which edges *should*. That is a judgement about which
  pairs a reader will confuse.
- *Standing instruction* (10) — after any batch, enumerate the new set pairwise
  and ask what happens to a reader who confuses two of them.

**What went right, worth keeping.** The finding came from the routing scenarios,
not from review — which is what those pairs are for, and the second time in two
runs they have paid for themselves. And both agents were **reproduced before
anything was edited**: instruction 8 held under three separate delegated findings
in one run, including one that turned out to be sharper than reported.

**A second entry, smaller and sharper.** The `maquette` token layer shipped
status colours this run had *invented* — reached for from a framework's defaults
— while the brief simultaneously claimed the pack "needed no correction". The
palette gate caught the collision (7.9 under deuteranopia) within a minute of the
file being written. The values were re-derived, the token layer now marks the
whole set as a pack decision rather than an extraction, **and the brief and
design record were corrected**, because a false claim in a record is worse than
the defect it describes. The lesson is narrow and worth keeping: *the moment you
supply a value the reference does not have, say so at the declaration* — the gate
will catch the collision, but only the comment catches the provenance.

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
