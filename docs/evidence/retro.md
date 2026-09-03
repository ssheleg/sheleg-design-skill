# Retrospective — sheleg-design-skill

The project's standing instructions and run log for task-pipeline. Stage 0
reads this file **in full**; stage 10 prunes, stamps, and writes an entry only
if the run diverged.

## Standing instructions (cap: 10 · current: 10)

Each one binds every run in this project until it is retired. Retire when it
became a mechanical check, when the paths it names are gone, or when it has not
fired in five run stamps.

**The third trigger is unavailable over reconstructed rows, and that is a rule
rather than a caution.** A stamp whose `Diverged?` reads *unrecorded* carries no
record of which instructions fired, so five such rows are five absences of evidence
rather than five observations of silence — and retiring on them retires whatever
happens to be oldest. **An instruction may only be retired on the third trigger when
all five of the newest stamps answer `Diverged?`.** `validate_retirement_window()`
reports whether the window is currently open, so the answer is read rather than
assumed (B-051).

1. **Never assume this checkout is yours alone.** Before stage 0 records shared
   state, run `git reflog -8`, `git branch -vv`, and look at working-tree
   mtimes. A HEAD move you did not make, a `feat/*` branch you did not create,
   or a file changing while you test means another pipeline run is live in the
   same directory. Recheck immediately before staging anything — the tree can
   turn hostile mid-run.

   **Widened 2026-08-13: "before staging" is not the last moment the tree can turn.**
   The 1.26.0 run did recheck before staging — `git reflog -2` showed only its own
   reset — and then merged into `main` and found a commit it had never seen sitting
   between its base and its merge, with the version it had planned already tagged and
   published. Staging is one of four moments, and the other three are the ones that
   touch shared state: **`git fetch` immediately before the merge, before the push, and
   before the tag.** The check that costs one command is the one that catches a
   collision while it is still only a version number.

   **Widened 2026-08-12: detection was never the missing half — the remedy was.**
   This instruction has caught a concurrent run four times and has never said what
   to do next, so each time the answer was improvised. It is two commands: build in
   an isolated `git worktree` (under a gitignored path, so the other run's
   `git add -A` cannot see it), and commit an **explicit path list**, never `-A`.
   The run that forced this widening lost nothing only because the collision was
   caught before staging; the concurrent run's `git add -A` had already swept this
   run's in-flight brief and a scratch screenshot into its own commit. *(Last fired:
   2026-08-13 · `a9c497e` — **its fifth catch, its second on a live run, and its first
   late one.** The recheck before staging was clean, so the run staged 21 paths by name
   and merged — and the merge brought in a commit from a concurrent session that had
   bumped every manifest to 1.25.0, tagged it and published it to npm while this run
   was building the same number. Caught by the merged tree not matching the tree CI had
   verified, which is a downstream symptom: the tag was withheld, the version moved to
   1.26.0, and nothing on either side was discarded. Cost: a version number and 22
   version references in prose. Had the run tagged on the strength of its branch's green,
   it would have overwritten a published release. This is the firing that widened the
   instruction above. Previously: 2026-08-12 · `f4f25ce` — **the first time it
   caught a live one.** `git reflog` showed a commit this session did not make sitting at
   `HEAD@{1}`, between the stage-0 snapshot and the run's own `git checkout -b`: a
   concurrent agent had committed on `main`, bumped every manifest to the version this run
   had planned, tagged `v1.18.0` and published it to npm — and swept this run's brief and a
   scratch screenshot into its commit. The run moved to `1.19.0`, rebuilt in an isolated
   worktree, and committed an explicit 41-path list. Everything downstream of that catch —
   the version, the base, the whole release — would have collided. Previously: 2026-08-12 · `e9b753f` — and it fired **late**: the
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
   published. *(Last fired: 2026-08-13 · `a9c497e` — **and it is the only reason the
   collision resolved without loss.** The manifests said 1.25.0 and so did the CHANGELOG,
   on both sides; three sources disagreed with none of it. `git tag --sort=v:refname`,
   `git ls-remote --tags origin` and `npm view` all answered v1.25.0 **already shipped**,
   which is what turned "two entries claim one number" into "theirs is published, mine
   moves." Read from the registry the manifests could not have answered it: the other run
   bumped the same three files this one did. Previously: 2026-08-12 · `e9b753f` — `npm view` 1.13.0 against
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

5. **No reachable reference, no claim — for a pack's origin, and for anything else
   you cannot open right now.** A pack needs a production reference a reader can go
   and look at: a URL or a bare host, not a product name. No reference, no pack —
   the contract forbids invented values, and a synthesised palette with a citation
   attached is an invented value that looks sourced. This retired an eighth pack and
   a six-pack backfill in one run rather than shipping either.

   **Widened 2026-08-12, because the same failure arrived wearing different
   clothes.** 1.14.0 shipped the sentence *"Refero — alone among the three — returns
   flows"* into two repositories. Mobbin returns flows too; its tool surface was
   invisible because it was registered and unauthenticated, so the comparison could
   not be checked by the session that wrote it. Nothing stopped it, because the rule
   was scoped to *palettes* and the claim was about *a tool*. It is the same class:
   an assertion about something outside the session's reach, written in the voice of
   something measured, sitting beside things that were. So the rule now reads: **a
   comparative claim about a capability you cannot exercise in this session is
   unverified — mark it so, or do not write it.** The sharpest form is a claim
   written next to the rule that forbids it — `DESIGN_SYNC_BRIDGE.md` §4 says *gate
   on the tools present, not on the config* two paragraphs above where the sentence
   went in.
   *(Last fired: 2026-08-12 · `ada7462` — the widened half, within the hour: signing
   in to Mobbin exposed `search_flows`, one live query returned a twenty-screen flow,
   and both repositories were corrected with the wrong claim named rather than
   quietly replaced. Previously, the original half: 2026-08-12 · `e9b753f` — one reference, one URL, and the pack was
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
   *(Last fired: 2026-08-13 · `a9c497e` — the class was **a measurement that moves with
   local scratch state**, and its shape here was `validate.py` walking every `.md` under
   ROOT while this project's own concurrency remedy puts a full second copy of the tree at
   `.claude/worktrees/<name>`: 2361 checks against 2067 on one commit. Watched saying no
   in the only form that fits a defect whose symptom is silence — the plant asserts a
   nested checkout changes neither verdict nor count, and with the guard replaced by
   `if False:` it reported `MISSED`. Class swept rather than the string grepped: the other
   two gates were read, not searched — `sloplint.py` walks `SKILL_DIR.rglob`,
   `validate_palette.py` does not recurse at all, so only these two sites were ever
   exposed. Previously: 2026-08-12 · `e9b753f` — the class was **the entry point that
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
   *(Last fired: 2026-08-13 · `a9c497e` — diffed and cited, not assumed: `validate.yml:30-32`
   runs all three `--self-test` invocations, so the new nested-checkout plant was already
   watched by CI in the same commit that introduced it (run 31661837515, 19 jobs). No
   workflow change was needed, and the reason is a line number rather than a memory.
   Previously: 2026-08-12 · `e9b753f` — diffed again, and this is the run where it
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

   **Widened 2026-08-13: the report you must not trust includes the one your own script
   just printed.** A throwaway script written for this run printed `floors: _measured_on
   now names the merged tree` after a `str.replace` that matched nothing — the file it
   was editing was not in the list the earlier step had bumped, so the pattern searched
   for a string that did not exist yet. Exit 0, a confident line of output, no change on
   disk. A tool's success line is somebody else's claim about your artifact; your own
   script's success line is your claim about it, which is worse, because you will believe
   it. Read the file.
   *(Last fired: 2026-08-13 · `a9c497e` — three artifacts read rather than reported: the
   published tarball pulled from the registry (1.26.0 in both manifests, `@role non-text`
   present, **0** stale `1.25.0` references outside the CHANGELOG, 17 packs), the local
   channels read as installed files (`~/.claude/plugins/cache/.../1.26.0/skills/sheleg-design/SKILL.md`
   and the hub copy both `version: 1.26.0`, no shadowing plain copy), and `floors.json`
   read after the script that claimed to have edited it — which is the read that caught
   the widening above. Previously: 2026-08-12 · `e9b753f` — the published tarball was pulled from the
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

**2026-08-13, the status-on-field run (`a9c497e`) — nothing retired, two widened, and
the retirement trigger itself is the finding.** Five instructions fired here: 1 (a
concurrent run, its fifth catch — and its first *late* one, see the entry below), 2
(`git tag`, `ls-remote --tags` and `npm view` are what proved 1.25.0 was already
published rather than merely claimed), 6 (a defect found in one gate, the class named
and swept across both siblings), 7 (`npm test` diffed against `validate.yml:30-32`;
all three self-tests run in CI, so the new plant shipped already watched), 9 (the
tarball read from the registry, the installed files read rather than the updater's
output — and my own script's success line caught lying about a no-op). 3, 4, 8 and 10
did not fire: no scenario was written or run, nothing was delegated, and no batch of
artifacts landed to check against itself.

**By the letter of the third trigger, that should have retired instruction 2 — and
it would have been wrong.** Its note says *last fired 2026-08-12 · `e9b753f`*, which
is thirteen stamps back, but stamp 23 records `v1.24.0` reading the registry before
its tag and stamps 21–23 all did the same. The trigger is computed from annotations
runs forget to update, so an instruction that fires every release can look dormant.
Same shape on 3, 4, 5 and 8: stamp 23 alone evidences firings none of their notes
record. The arithmetic is only as good as the bookkeeping, and the bookkeeping is the
part a run does last. Noted rather than fixed by inventing firings I did not make:
the five that fired here have their notes updated, and the rest keep theirs.

Cap 10, current 10, none retired; 1 and 9 widened, so no slot was needed for either
of this run's two new classes.


**2026-08-12, the `pigeonhole` run (`98722cd`) — nothing retired, and the walk is
recorded because "I checked" is not a check.** All ten instructions fired in this
run, several of them hard, so none met a retirement trigger:

1 fired twice, at stage 0 and again immediately before staging — clean both times,
one worktree, no foreign HEAD move; and its remedy was used rather than merely
cited (an isolated worktree under a gitignored path, an explicit 66-path commit).
2 settled the version before the brief wrote it anywhere: `v1.20.0` on the tags, on
`origin` and on npm, three manifests agreeing, so 1.21.0 with no ghost. 3 and 4 both
fired on T25, which was written **and run** the same day with its negative branch,
and the negative branch is what proved the fork reads from both sides. 5 fired in
its widened form: two claims taken from screenshots — rotation, and a DOM-built
diptych — could not be verified against the artifact and are recorded as refuted
rather than dropped. 6 fired on the ratchet, watched refusing 1921 with its own
message, and on the palette gate, watched refusing nine of this run's own ratio
claims. 7 was checked rather than assumed: no new gate shipped, and `npm test` was
diffed against the workflow that ran 18 jobs. 8 fired forty-nine times and corrected
**me** twice — the type ramps and the deuteranopia causation were both mine. 9 fired
at the close-out. 10 fired weakly, as it does on a single-artifact run: the pairwise
question was asked against the existing fifteen and found five genuine forks, each
written from both sides.

Cap 10, current 10, none retired.


- **2026-08-12 (`f4f25ce`) · nothing retired, nothing added (still 10, at cap);
  instruction 1 widened.** All ten walked against the three triggers and **all ten
  fired**, which has not happened before. Instruction 1 caught a live concurrent run
  (see its own note); 2 caught the registry moving from 1.17.0 to 1.18.0 mid-session,
  which is what set this run's version; 3 and 4 were satisfied inside the run rather
  than deferred — T24 shipped with both branches **and** both verdicts, which is the
  first time a new pack's routing test has not left a debt row; 5 held, and an agent
  found the half of it this run had missed (54 of 118 token declarations carried
  neither MEASURED nor SELECTED); 6 fired twice, two new checks each watched saying no
  with its own message and each given a permanent self-test plant; 7 fired on **my own
  new check**, which was defined and never called — the same class one layer down, and
  it was only visible because a stray line broke the suite's syntax and made a grep go
  quiet; 8 fired twenty-two times, eleven findings confirmed against my own pack, one
  refuted; 9 read the published tarball, both install channels and the wiki page rather
  than trusting three green summaries; 10 fired weakly again — one artifact, so the
  pairwise question went to the existing thirteen and produced five reciprocal forks.

  **Instruction 1 was widened rather than duplicated, for the fourth time this list has
  chosen widening over addition.** It has now caught a concurrent run four times and
  had never said what to do about one; the remedy — an isolated worktree under a
  gitignored path, plus an explicit path list at commit time — is written into it.
  **An eleventh instruction was considered and rejected on the list's own rule:** the
  count-edit defect that shipped in two consecutive releases is now
  `validate_contract_split()`, and a rule that duplicates a mechanical check is a rule
  nobody reads.


- **2026-08-12 (`ada7462`) · nothing retired, nothing added (still 10, at cap);
  instruction 5 widened.** Walked against the three triggers after two same-day
  releases. **Six fired** — 2 (registry and tags checked before both tags), 5 (the
  widened half, within the hour of widening it), 6, 7, 8 (nine delegated findings
  reproduced, one refuted), 9 (published tarballs unpacked and read, both install
  channels verified by reading files). Instruction 3 fired and **closed its own first
  debt the same day**, which is the shortest life a board row has had here.
  Instructions 1, 4 and 10 were walked and found not applicable: no shared-tree
  hazard arose in `sheleg-design`, though the `super-ux` checkout turned out to be two
  release commits behind `origin/main` with `package.json` reading a version older
  than both — caught by that repository's own `release_preflight.py`, which is
  instruction 1's job done by a script in the other repo.
  **Instruction 5 was widened rather than duplicated, for the third time this list has
  chosen widening over addition.** The pattern is now explicit: when a rule catches a
  defect one noun away from what it says, the rule was right and its scope was narrow.
  Adding an eleventh would have split one class across two rules, and a class split
  across two rules is a class nobody owns.

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

**Thirty-five rows below are marked *unrecorded* in the `Diverged?` column** — five
backfilled on 2026-08-12 by the `datasheet` run, twenty-six covering `v1.27.0` to
`v1.44.0` reconstructed the same way on 2026-08-20 after the table sat at `v1.26.0`
for eighteen versions, and three written on 2026-08-20 by runs that could have
answered and did not. **That count is computed on every run, not restated here**:
`validate_reconstructed_stamp_count()` recomputes it and fails when this paragraph
disagrees with the table, because the number this paragraph exists to report is the
one a reader will trust and nobody was recounting. Between `v1.14.1` and `v1.18.0` this table went five releases
without a stamp, so the retirement trigger in the standing instructions above —
*has not fired in five run stamps* — was not computable: a list that is short by
five rows retires whatever it likes. Date, commit and task were derived from
`git log`, tags and the CHANGELOG; **`Diverged?` cannot be derived**, because the
question is whether the run hit something worth an entry in the Log, and only the
run knows. It is left as *unrecorded* instead of guessed. Nothing here is a
substitute for the entries those runs owed; it restores the arithmetic, not the
knowledge.

**The arithmetic was the whole point, and it had stopped working.** The
retirement trigger above — *has not fired in five run stamps* — reads a stamp
count, so a table eighteen releases short made every standing instruction look
dormant and any of them retirable on a count that did not exist. That is worse
than a table with no trigger. `validate_release_register()` now fails when a
CHANGELOG release at or after `1.5.0` has no row here, so this register cannot
fall behind again without the gate saying so; the reconstructed rows carry no
*fired-instruction* record, which means the trigger counts stamps and not
evidence until runs start writing their own again.

| Date | Commit | Task | Diverged? |
|---|---|---|---|
| 2026-09-03 | working tree | **1.58.4** — the committed card is the umbrella's own render, byte for byte, with the corrected fit metric; the install line no longer overruns the padding box. The pixels are committed here and byte-checked from the umbrella, so `scripts/site.js` had to keep this member in a `LEGACY_FIT` set until its own release recommitted them — this release is that recommit, and the umbrella drops the entry in the same pass (`B-118`). | no |
| 2026-09-01 | working tree | **1.58.3** — the registry card stopped being six releases stale. `SKILL-CARD.md` said `1.52.0` against a shipped `1.58.2`; nothing read it, because the version moves in three manifests on every release and the card was in no list. `validate_registry_card_names_the_version_that_ships` refuses a card whose `Version` row disagrees with `package.json`, and refuses one that states no version at all — a card a reader cannot see go stale is worse than one that lags visibly. Watched failing first. Measured across the family the same day: four of nine cards behind, this one second worst after `agent-stack`'s ten; the same check now sits in each of the four. | no |
| 2026-08-31 | working tree | wave-3 family-audit closures SHD-02/04/08 — `$schema` added to both manifests (marketplace → `json.schemastore.org/claude-code-marketplace.json`, plugin → `…/claude-code-plugin-manifest.json`; `claude plugin validate` green); the GitHub About description regenerated via `gh api` WITHOUT a pack count (it said "35 style packs" over a 39-pack tree; nothing in the release path can rewrite repo metadata — the workflow's `GITHUB_TOKEN` cannot carry `administration` — so the count is dropped rather than left to go stale, decision recorded in CONTRIBUTING); and the evals actually ran — 15 trigger queries (12 authored + 3 NEW coexistence negatives naming `theme-factory` / `figma-generate-design` / `frontend-design`) probed blind in fresh isolated headless sessions (`claude -p --setting-sources ""`; prompt = query + installed-skill list + one question): `claude-haiku-4-5-20251001` 15/15, `claude-sonnet-5` 14/15 (the miss recorded: q10, a mechanical CSS-selector fix routed here); three scenarios run per model with the skill on disk, scored line by line, browser/Figma-bound lines recorded `not reproducible from this harness`. **Diverged from the wave brief's probe transport**: the Agent-tool path was exhausted by sibling agents (20-slot shared cap), so probes ran as headless CLI sessions — the same blind fresh context, stated in RESULTS.md's Method line; and the CLI's stdin-detection killed 8 first-attempt sessions (`no stdin data received`), re-run with stdin closed rather than scored as answers. **`v1.58.2` — shipped**: PR #19 squash-merged as `4bfb148`, whose tree (`05df3cf…`) is byte-identical to the CI-verified branch head `bbaab48`; ANNOTATED tag (`git cat-file -t v1.58.2` → `tag`, `git describe origin/main` → `v1.58.2`); release run 33349913269 green on both jobs, GitHub release published 2026-08-31T02:14:02Z, `npm view sheleg-design-skill version` → 1.58.2 (shasum `567d000`) | **yes** |
| 2026-08-30 | working tree | hotfix: the front-matter description was not valid YAML **for the second time** (`Triggers: "…"` from the 1.57.0 trigger rewrite, same class as 1.37.4's `style packs: dashboards`) — every gate here reads the field with a regex, 5598 checks stayed green twice, and the umbrella's YAML gate refused the file when pinning v1.58.0. Fixed as `Triggers - "…"` (the siblings' shape; all 35 routed triggers survive, `advertised_check.js` re-run green), mirror synced byte-identical; and the reason 1.37.4 did not hold is closed — its strict gate lived in the umbrella, which CI never has above it, so `validate_front_matter_is_yaml()` now parses every shipped front-matter block with `yaml.safe_load` in THIS repo's gate, fails closed without PyYAML, watched failing on the real defect pre-fix and planted permanently in the self-test; the three workflows install PyYAML rather than assume it. **`v1.58.1` — shipped**: PR #17 squash-merged as `b0ee45f`, whose tree (`173ca7b…`) is byte-identical to the CI-verified branch head `6342fb1`; ANNOTATED tag (`git cat-file -t v1.58.1` → `tag`, `git describe origin/main` → `v1.58.1`); release run 33322813809 green on both jobs, GitHub release published 2026-08-30T16:35:29Z, `npm view sheleg-design-skill version` → 1.58.1 | **yes** |
| 2026-08-30 | working tree | the catalogue stops being the one surface nobody designed, and T37 runs — **standing instruction 1 fired, and this time on a tree that had already turned**: `git log` answered `94ebde2` while the reflog's last entry was this session's own checkout of `03362e2`, and 111 files read as staged. Diagnosed before anything was touched: the index and working tree were byte-identical to `03362e2`, so the 'staged' set was the *reverse* of a v1.57.0 another run had merged under it, and a commit here would have reverted their release. Repaired with a reset that could lose nothing, then all work moved into an isolated worktree under a gitignored path with its own lease. Their close-out PR merged mid-run and freed the ledgers, which is why this row is written rather than raced. The work: 67 colour literals removed from the site generators, which now inline a pack's token layer and are gated against reaching for a hex; a catalogue parse that had been reading the wrong file since the table moved, publishing 39 empty cards and 39 empty JSON-LD descriptions; T37's two blind branches run and passed, returning 29 findings of which 13 are fixed here; and a superlative in the doctrine that had been false for four releases, now recomputed by a gate. **`v1.58.0`** prepared on this branch | **yes** |
| 2026-08-30 | working tree | wave-2 family-audit closures SHD-05/01/03/09/11 — the three sibling skills declared optional in `compatibility` with an absent-branch written at every mention (the `SURFACE_COMPOSITION.md` role table named as the chart contract where no `dataviz` skill exists); `## Contents` lists derived from each file's own headings by `scripts/gen_contents.py` across 47 qualifying references, gated by `validate_contents_lists()`; both manifest descriptions regenerated from `STYLE_PACK_INDEX.md` by `scripts/gen_manifest_descriptions.py` and gated against hand-appends; the deck trigger narrowed to the web-published register; the root-layout deviation recorded in CONTRIBUTING. Both new gates watched failing against the real tree (46 references + 2 manifests red) and planted in the self-test. **Diverged on the version, twice**: the brief said v1.55.0, `chorus` (a concurrent run in the same directory, its PR merging mid-read) took it, and the same run had `v1.56.0` in flight — so this run built in an isolated worktree per standing instruction 1 and took **`v1.57.0` — shipped**: PR #14 squash-merged as `94ebde2`, whose tree (`98cbc3e…`) is byte-identical to the CI-verified branch head `dd15eb3`; ANNOTATED tag (`git cat-file -t v1.57.0` → `tag`, `git describe origin/main` → `v1.57.0`); release run 33318452212 green on both jobs, GitHub release published 2026-08-30T15:03:22Z, `npm view sheleg-design-skill version` → 1.57.0 | **yes** |
| 2026-08-30 | working tree | `MOTION_PRODUCTION.md`, the render seam — the doctrine decides whether a page may move, and nothing owned the question of what happens when the motion becomes a file. The document takes its position before it names a tool: a rendered asset gives up the reduced-motion contract, the theme, the text and the first frame's decode, and the reduced-motion obligation MOVES to the embedding page rather than disappearing. Two tools measured on the day rather than characterised — Remotion's licence is free only to individuals, ≤3-employee for-profits and non-profits and it is on 4.0.518 after six years; HyperFrames is Apache-2.0 and **pre-1.0** at 0.8.20, which is stated as a risk. Recommended HyperFrames on this library's own copy-never-transcribe rule — an HTML composition links the pack's token layer unmodified — with three named conditions that reverse it. Requested mid-run by the operator while the `chorus` release was in flight, and taken as a second release rather than folded into the first; **`v1.56.0`** prepared on this branch | **yes** |
| 2026-08-30 | working tree | `chorus`, the thirty-ninth pack from crowdreply.io — a Framer site whose 52 declared tokens disagree with what paints, so an area-weighted census over 2,439 elements decided every value; six corrections, of which the sharpest are a primary CTA at **2.84:1** fixed by changing the LABEL to ink (6.20:1) rather than darkening the brand hue, a card separated from its field by **1.04:1** with no border and no shadow, and **zero `:focus-visible` rules in 274KB** with two `outline: none`, so the whole focus mechanism including its dark-surface re-declaration is the pack's; the reduced-motion contract is stated as TWO halves because 383 script-set inline transforms are unreachable from a media query; the mint is declared dark-only after the derivation collapsed to near-black; kit rendered and read back at 1440/768/390 pre-tag, and its button lost its 1px border because that border measured 38px against the reference's 36; **T37 written, not yet run** — no subagents were available to this session, debt on the board per standing instruction 3; **`v1.55.0`** prepared on this branch — the tag, the GitHub release and the npm publish are stamped in the close-out that follows the merge, and nothing above claims them | **yes** |
| 2026-08-29 | working tree | the installers refuse the shadow they document (family canon, make-skill v0.25.0 `distribution.md`): both `bin/cli.js` and `install.sh` now read the target home's `installed_plugins.json` before writing that home's `~/.claude/skills/sheleg-design`, refuse with exit 3 and the real spec's remedy, fail open on absent or corrupt JSON, and gate only the Claude Code channel; thirteen installer cases against throwaway HOMEs wired into `npm test` and CI, watched failing first against the pre-fix installers (7 red); CONTRIBUTING now requires ANNOTATED release tags — v1.53.0 *and* v1.54.0 were lightweight, so `git describe`/`git submodule status` misreport them (SHD-07/UM-03), old tags not re-cut; landed as PR #10 — main's rulesets refuse direct pushes and merge commits, so `agent_sync.py merge --push` cannot deliver `main` here and the branch goes through a squash PR; **`v1.54.1` shipped** (`663ff2e`, `git describe` now answers `v1.54.1` where the lightweight v1.54.0 answers `v1.52.0-3-g2cc989b`) | **no** |
| 2026-08-29 | working tree | `surveyor`, the thirty-eighth pack from visible.seranking.com — the authored `se-uikit` layer dug out of a WordPress site whose vendor preset palette paints nothing; the AA corrections climb the reference's own button ladder (`#0a7269` promoted to the text-bearing fill over a 3.74:1 CTA), the answering pink gains a speaking step, the missing warn is a stated decision, and the page's one shadow is recorded as a scroll event on the nav; the catalogue's leak guard refused its own site on the word `visible` and was rewritten two-tier while its miss on `seranking` was closed; **`v1.54.0` shipped** | **yes** |
| 2026-08-27 | working tree | `test-drive`, the thirty-seventh pack from datafa.st — the live product embedded in drawn browser chrome as the set piece, a founder's hand annotating from the margin, one coral split into two tokens because the reference's own CTA is 3.42:1 under white, and a declared teal accent the render proved dead; the render step caught a 66px nav against a stated 65, a 428px link row on a 390px page, and a missing touch floor; T35 ran blind both ways and its defect-read out-hit the author's own ladder; **`v1.53.0` shipped** | **yes** |
| 2026-08-27 | working tree | the public site opens on the designs behind three tabbed screens with a full machine layer (ItemList of every pack, one publisher node, 404, three-URL sitemap) — and the pass found `method.html` emitting two canonicals and an `oklch()` field the gallery could not parse, so the published dark count was five where six ship; `deskmate` corrected by its own blind audit, the white-on-white card being the one no gate can see; `validate_token_population_counts` added after SURFACE_COMPOSITION.md claimed twenty-nine at a true thirty-three; **`v1.52.0` prepared** | **yes** |
| 2026-08-27 | working tree | `deskmate`, the thirty-sixth pack from viktor.com — one light source above the top edge and one four-stop ramp doing three jobs, with a framed transcript whose quoted client keeps its own face and colours under a `--quoted-*` namespace; the status set lifted out of that transcript because the brand layer paints no state; the render caught a nav slab 515px wide on a 390px page, a dusk secondary painting white on white, a chip label at 3.36:1 and an underlined pill; **`v1.51.1` shipped** — `v1.51.0` was pushed before its branch, the workflow's reachability guard refused it, and a `v*` tag cannot be moved here | **yes** |
| 2026-08-26 | working tree | both shared validator headers explicitly state `diverges: none`, completing the umbrella mechanism contract; **`v1.50.3` prepared** | **yes** |
| 2026-08-26 | working tree | the umbrella drift gate restored three exact router carriers and required the two copied public-contract validators to name their shared mechanism; **`v1.50.2` prepared** | **yes** |
| 2026-08-26 | working tree | the 35-pack chooser moved to `STYLE_PACK_INDEX.md`, keeping the exhaustive routing table while returning the skill body below the house budget; public contract, eval fixtures, CI house audit, and a 1200×630 social card prepared for **`v1.50.1`** | **yes** |
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
| 2026-08-12 | `8df0ede` | T23 run the day it shipped; nine findings reproduced, eight confirmed and one refuted; **`v1.13.1` shipped** | **yes** |
| 2026-08-12 | `ada7462` | Refero joins the reference-sweep slot in both repositories, and the claim written about the slot was wrong; **`v1.14.0` + `v1.14.1` shipped** | **yes** |
| 2026-08-12 | `a993a8e` | T5 and T6 run; two scenarios go green and the kit stops being invisible; **`v1.15.0` shipped** | *unrecorded* |
| 2026-08-12 | `b1e7d31` | the five T5/T6 findings actioned — the default dark pack's ratios finally reach a check; **`v1.16.0` shipped** | *unrecorded* |
| 2026-08-12 | `771dd86` | the skill body brought back inside the token budget (~5478 → ~4988 of 5000); **`v1.16.1` shipped** | *unrecorded* |
| 2026-08-12 | `abc0ec8` | the scenario harness reaches zero unrun; 121 stated ratios measured and 71 found unguarded (B-013); **`v1.17.0` shipped** | *unrecorded* |
| 2026-08-12 | `0c23558` | the installer offers the family's routing block (B-06); **`v1.18.0` shipped** — a concurrent run, not this one | *unrecorded* |
| 2026-08-12 | `f4f25ce` | `datasheet` style pack from fingerprint.com, fourteenth kit, two gate holes closed, T24 run on the day it shipped; **`v1.19.0` shipped** | **yes** |
| 2026-08-12 | `e97a8cc` | `manpage` style pack from zernio.com, fifteenth kit; **`v1.20.0` shipped** | *unrecorded* |
| 2026-08-12 | `98722cd` | `pigeonhole` style pack from getinboxzero.com, sixteenth kit; the taxonomy's inks re-derived and the deuteranopia argument corrected; T25 written and run before the tag; **`v1.21.0` shipped** | **yes** |
| 2026-08-13 | `4f78dff` | the modern-CSS audit, and the `color-mix()` ban lifted by teaching the palette gate to compute it — verified against Chrome rather than against the spec; **`v1.22.0` shipped** | **yes** |
| 2026-08-13 | `c2b271b` | container queries in the kits: a pack's spec the kit had ignored, three kinds of breakpoint rather than two, two new checks; **`v1.23.0` + `v1.23.1` shipped** | **yes** |
| 2026-08-13 | `cf06b75` | `roster` style pack from babylovegrowth.ai, seventeenth kit; a lab() palette resolved from painted pixels, T26 run before the tag, and a refuted finding that corrected two shipped packs; **`v1.24.0` shipped** | **yes** |
| 2026-08-13 | `a9c497e` | a status colour measured against the field it sits on: `validate_status_on_field()`, `@role non-text:`, 28 findings and three real fixes; then a version a concurrent run had already published, and `validate.py` found counting its own worktree as content; **`v1.26.0` shipped**, 1.25.0 left to the other run | **yes** |
| 2026-08-13 | `083509d` | `editorial-luxury`'s side-stripe ban narrowed to the ornament it was always about; **`v1.27.0` shipped** | *unrecorded* |
| 2026-08-13 | `7ac05cf` | the artifact root follows task-pipeline's new default; **`v1.27.1` shipped** | *unrecorded* |
| 2026-08-14 | `572bb0e` | `paperclip`, an eighteenth pack, where colour is ornament and nothing coloured can be clicked — **`1.28.0` never tagged**, shipped inside a later version | *unrecorded* |
| 2026-08-14 | `f8f8996` | `ora` and `tenor`, two references measured off live sites rather than composed; **`v1.29.0` shipped** | *unrecorded* |
| 2026-08-14 | `e35a26f` | the paperclip merge at twenty packs, and a version that had to move twice — **`1.30.0` never tagged** | *unrecorded* |
| 2026-08-14 | `02a73bc` | T29 ran and twenty-six defects survived three gates to be found by it; **`v1.31.0` shipped** | *unrecorded* |
| 2026-08-15 | `40e1a1f` | `tenor` met a product surface and three of its own measurements did not survive it; **`v1.32.0` shipped** | *unrecorded* |
| 2026-08-15 | `80fc33f` | three things `tenor` asserted that a running page disproved; **`v1.33.0` shipped** | *unrecorded* |
| 2026-08-15 | `8037f05` | `tenor` applied correctly and still reading flat — the ramp, the lattice and the colour that carried nothing; **`v1.34.0` shipped** | *unrecorded* |
| 2026-08-15 | `48f24d9` | `ledger`, a twenty-first pack, and two gates that counted with a table stopping at twenty — **the number 1.35.0 was taken by a concurrent run**, so this one was never tagged | *unrecorded* |
| 2026-08-15 | `e9c0bf6` | `awning`, a twenty-second pack, and the reference it was asked for did not survive measurement; **`v1.35.0` shipped** — the second run to claim that number | *unrecorded* |
| 2026-08-16 | `fdc99b0` | `awning` had shipped as a specification and had never been rendered; rendering it found two accessibility defects; **`v1.36.0` shipped** | *unrecorded* |
| 2026-08-16 | `7fb0c6c` | a header saying six traps over a list of eight, and the gate that would have caught it did not exist; **`v1.36.1` shipped** | *unrecorded* |
| 2026-08-16 | `4c57784` | the description advertises the words an operator types; **`v1.37.0` shipped** | *unrecorded* |
| 2026-08-16 | `2d59acb` | the 1.37.0 rewrite dropped a phrase a router still fires on; **`v1.37.1` shipped** | *unrecorded* |
| 2026-08-16 | `792bc6f` | the gate can see an invariant it breaks one repository away; **`v1.37.2` shipped** | *unrecorded* |
| 2026-08-16 | `809d8f5` | the phrase that reached no route, and the word that could not fix it; **`v1.37.3` shipped** | *unrecorded* |
| 2026-08-16 | `e331dff` | the description was not valid YAML, and every gate in the family read it with a regex; **`v1.37.4` shipped** | *unrecorded* |
| 2026-08-16 | `de09f9e` | an unqualified landing page reaches both crafts; **`v1.37.5` shipped** | *unrecorded* |
| 2026-08-16 | `da33e37` | the routing table stopped being a second copy of the packs — 6203 tokens against a 5000 budget, down to 4595; **`v1.38.0` shipped** | *unrecorded* |
| 2026-08-17 | `0d4e805` | five packs ported from live references, twenty-two to twenty-seven; **`v1.39.0` shipped** | *unrecorded* |
| 2026-08-17 | `74ed099` | visual references become askable, and the natural phrasing is refused; **`v1.40.0` shipped** | *unrecorded* |
| 2026-08-17 | `41b9eca` | the component layer — the pack decides the tokens, the kit renders them; **`v1.41.0` shipped** | *unrecorded* |
| 2026-08-17 | `b8bf235` | `proscenium`, a twenty-eighth pack, measured for its tempo rather than its surface; **`v1.42.0` shipped** | *unrecorded* |
| 2026-08-17 | `001a0bd` | `bulletin`, a twenty-ninth pack, elevation drawn rather than blurred; **`v1.43.0` shipped** | *unrecorded* |
| 2026-08-19 | `30bfbc3` | degrade to calm had no observable, and a hyphenated count had no guard; **`v1.44.0` shipped** | *unrecorded* |

| 2026-08-20 | `94c1774` | four packs contradicted their own token layers; six sweeps added, which found 24 more defects on their first run (v1.45.0) | *unrecorded* |
| 2026-08-20 | `0f8fa82` | B-001/B-002: three packs stay core by decision, and `core` must name what it declines | *unrecorded* |
| 2026-08-20 | `e24ee5b` | B-042: a mandated scrub carves its own easing exception; five packs share the shape | **yes** |
| 2026-08-20 | `84ba82c` | B-043: a pack prescribed a token its layer never defined, and the library's last raw `vh` | **yes** |
| 2026-08-20 | `f88c14b` | B-045: every duration answers reduce, and a promised component-layer stop is verified in the kit | **yes** |
| 2026-08-20 | `3d0429a` | B-047: two `scoreboard` ratios described pairings that never render | **yes** |
| 2026-08-20 | `f36961a` | B-049: the doctrine's duration bands reach the token layer's own comments | **yes** |
| 2026-08-22 | `469503d` | two production references measured and packed — `outrank` (536 tokens over two borrowed systems) and `babylove` (seven over Tailwind defaults); **`v1.46.0` shipped** | **yes** |
| 2026-08-22 | `e129f67` | `patchbay`, the thirty-second pack — a dark live schematic measured off nautilustrader.io with `getComputedStyle` because the reference declares no tokens at all; §9 gained the three layers a blanket reduced-motion rule cannot reach; **`v1.47.0` shipped** | **yes** |
| 2026-08-24 | `514ff16` | `nameplate`, the thirty-third pack from brandpush.co — a square page whose one round shape is a plate carrying somebody else's publication name; five measured corrections, and the first pack in four to move no ratio pin; rendering the kit caught a plate 28px taller than its own spec and a body weight the token layer declared and no component consumed; **`v1.48.0` shipped** | **yes** |
| 2026-08-25 | `19e02b8` | `onionskin`, the thirty-fifth pack from supermemory.ai — two bases where everything quiet is an alpha of one, so the pack has no grey ramp at all; 96.5% zero radius, the squarest page here; the first pass composited alpha in linear light and would have shipped a correction to something that was never broken; **`v1.50.0` shipped** | **yes** |
| 2026-08-24 | `0f3170a` | `rimlight`, the thirty-fourth pack from peppermint.global — elevation made of coloured light rather than shadow, a sixteen-layer rig with six layers lit and ten held at alpha 0; the palette split by field, because the reference's hues are 6.5-10.5:1 on its dark act and 1.65-2.65:1 on white; the render caught a light control that followed the field into the dark and stopped being light; **`v1.49.0` shipped** | **yes** |
| 2026-08-24 | `2745c09` | the assembly rule written down where each part already lives — template rules 7 and 8, CONTRIBUTING step 8 — plus `nameplate`'s mark set carried as a mechanism rather than a taxonomy, and one claim narrowed to the width it was measured at; the new render step caught a 60px tile against a declared 50 within the hour; **`v1.48.1` shipped** | **yes** |
| 2026-08-25 | `28d9303` | README names where its test commands run — the published package ships no `test/`, so `python3 test/validate.py` resolved in a clone and nowhere else (**`v1.49.1`** shipped) | *unrecorded* |
## Log

### 2026-08-29 — the guard that refused its own site, and the brand it never saw

**Symptom.** The Pages build failed on every page after the `surveyor` merge:
`FAIL index.html: leaks 1 source term(s): visible` — including `404.html`, a page
with almost no prose. The published catalogue kept serving 37 packs while the tree
said 38.

**Surfaced at** stage 8, by the deploy's own gate. **Owned by** the leak guard's
term derivation, which had never met a multi-label host whose first label is an
English word.

**Root cause, twice over.** `source_terms()` took only the FIRST label of a host as
a brand stem: `visible.seranking.com` therefore contributed `visible` — which is a
CSS pseudo-class fragment, and the site's own stylesheet says `:focus-visible` on
every page — while `seranking`, the actual registrable brand, never entered the term
set at all. One derivation produced a false positive that blocked the deploy and a
false negative that would have let the real name through. The raw substring scan
(`t in low`) finished the job by reading CSS as prose.

**Fix by grade.** Two tiers, matching what NAMING means: a full host (contains a
dot) stays a raw substring over the whole file, because a URL inside a stylesheet
still makes a network request; a bare stem is matched at word boundaries over the
page with `<style>`/`<script>` stripped, and hyphen compounds (`focus-visible`) do
not count as the word. Stems now come from ALL labels. Watched saying no on five
plants before shipping: a host inside a CSS `url()` fails, a stem in prose fails,
the bare English word in prose fails (the stem IS the product's name here, so prose
saying it is naming it), the pseudo-class passes, a hyphen compound passes. Then the
real site built: 38 packs, 0 of 90 terms present.

**The lesson that travels.** A guard's term set is itself a measurement, and it can
be wrong in both directions at once from a single bad derivation. The failure that
LOOKS like over-blocking (the deploy refused) can be the only visible symptom of
under-blocking (the brand that was never guarded) — this run would not have read
`source_terms()` at all if the false positive had not stopped the build. When a gate
misfires, read what it should have caught, not just what it wrongly caught.

### 2026-08-27 — the blind reader out-hit the author, and the rule that split across two files

**Symptom.** T35a — the routing scenario for the pack this run had just written, run
blind in a fresh context — returned four defects that three green gates, a render pass
at three widths and the author's own re-reads had not: the body-coral ban stated
unqualified in the pack prose while the token layer's dark block mandated the opposite
swap; a 0.9s clock attributed to spinners that measure 2s/1.5s; a dark hover token
byte-identical to its resting pair under prose promising a brightening glow; and a
tint whose stated derivation computes a different hex than the one shipped.

**Surfaced at** stage 6, by the scenario's defect-read half. **Owned by** the
authoring method: the pack file and the token layer were written hours apart, and
nothing — gate or author — compares their *prose* for agreement about a rule.

**Root cause.** The sharpest of the four is a class one level above B-122 (nothing
checks that a pack's two files agree about what a token drives): here the files agreed
about the tokens and disagreed about the RULE. The dark swap was decided at the
declaration, correctly, and the prose ban was written from the light theme's
arithmetic and never re-read against the dark block. A ban that says "always" is a
claim about every theme the pack ships, and the gate that recomputes ratios cannot see
a quantifier.

**Fix by grade.** All four reproduced against the artifacts before any edit
(instruction 8), then fixed in the same change: the ban qualified with the dark
arithmetic on the line, the spinner noun corrected, the identical dark pair kept and
DECLARED as the measurement with the border named as the dark hover's carrier, the
tint recomputed to its own derivation. The nine datasheet findings from the negative
branch went to the board (B-134) rather than into this run, per the shipped-pack
precedent of 2026-08-08.

**The check that catches it next time** is not a new gate — it is the scenario
harness's defect-read half, which T34 exercised first and this run confirms: a blind
reader with the two files and no memory of writing them finds quantifier splits that
the author structurally cannot. The standing practice is already in the scenarios'
own template ("both branches read their chosen pack in full and report defects");
what this entry adds is the priority: run it BEFORE the tag, because all four fixes
were free on the branch and would each have been a release on main.

### 2026-08-22 — the reference that could not be read from its stylesheet, and the gate that priced every alpha

**Symptom.** Two of them, and neither was visible from reading anything. First,
`nautilustrader.io` declares **zero CSS custom properties** — it is MUI with Emotion — so the
usual method for authoring a pack (open the stylesheet, lift the token layer, verify a sample
against the running page) had nothing to open. Second, once the layer was written from
`getComputedStyle` alone, the palette gate refused it four times in a row, and every refusal was
correct.

**Surfaced at** the first `validate_palette.py` run. **Owned by** the authoring method, which
had never been exercised against a tokenless reference.

**Root cause, and it is a property of the gate worth writing down.** Three of the four refusals
were one shape: *a ratio binds to the token named on its own line, and a line naming two tokens
binds to the wrong one.* `--wash` stated 1.06:1 in a sentence that also mentioned `--ink` at
14.02, and the gate computed 14.82 and said so. The fix is not a phrasing trick — it is that a
declaration should state **one pair per line**, which is better writing independent of any gate.

The fourth was real and unrelated: the derived status green separated from this pack's mint-cyan
accent by **13.4 at full colour against a floor of 15**, and the set shipped by
`instrument-console` — the obvious thing to copy — was worse, at **3.51 under simulated CVD**.
The accent's hue is the constraint, and it is a constraint most packs never meet because most
accents are not within 40° of green.

**What was nearly written down wrong.** The unpairable-claim ratchet stood at 22 and the first
draft of the layer took it to 30. The reflex is to move the pin by 8 and write a reason. What
the pin actually asked was *which of these eight numbers is load-bearing* — and the answer was
three: two that say why nothing may be written on a tint, and one that is a button's only
visible edge at 3.10:1 against a 3:1 floor. For the other five the **alpha is the
specification** and the ratio was a derived restatement of it. Deleting them took the
contribution from 8 to 3 and made the layer say more, not less.

**The general lesson, and it left this repository.** `MOTION_DOCTRINE.md` §9 said an animation
without a reduced-motion path is a bug and stopped there. This reference demonstrates three
layers the one-rule remedy cannot reach — SMIL, which does not read `animation-duration`;
JavaScript writing inline styles per scroll frame, where zeroing durations only makes the hidden
state arrive faster; and any loop whose last keyframe differs from its first, which the remedy
teleports. All three are on one page, and the third is why that page's blanket rule happens to
be safe: its four ambient loops are written `0%` == `100%`. **The query is a signal, not a
mechanism.**

**Three numbers beside the change were already stale**, none of them this run's: a count that
named no noun (`the twenty-nine are`, over thirty-one), `sixteen` token layers declaring
`@role non-text:` against a tree of nineteen, and `ten` theme twins against a derived eleven.
The first is exactly the failure the skeleton's rule 6 describes, sitting unfixed in the file
that ships the rule's own fast path.

### 2026-08-13 — the remedy for one concurrent run became a defect in the gate that measures it

**Symptom.** Two things, and the second is only visible because of the first. A concurrent
session bumped every manifest to 1.25.0, tagged it and published it to npm while this run was
building the same number; the collision surfaced *after* the merge, when `main`'s tree stopped
matching the tree CI had verified. Then, while re-verifying the merged tree, the gates
disagreed with arithmetic: `validate_palette.py` was cleanly additive (958 base + 8 from their
status set + 35 from this run's check = 1001) and `validate.py` reported **2361** where both
parents measure 2066 and 2067. Neither side had added 294 checks.

**Surfaced at** stage 7, twice — once by the tree-hash comparison before the tag, once by the
count not adding up. **Owned by** stage 5 for the collision (the recheck ran before staging and
not before the merge) and by instruction 1's own remedy for the count.

**Root cause.** `validate.py` walks every `.md` under ROOT, and this project's standing answer
to a concurrent run is *build in an isolated `git worktree` under a gitignored path* —
`.claude/worktrees/<name>`, which is a full second copy of the tree. The gate counted the
remedy as content. So the instruction that exists to survive concurrency is what made the
measurement of concurrency wrong, and the two only ever fire together: a run without a
collision never has a worktree to double-count.

The ratchet in `floors.json` was one commit from enshrining 2361. That is the expensive shape,
not the inflated number: a floor measured with a worktree present fails the **next** clean run,
which reports a regression that never happened and names a count rather than a cause.

**Fixes by grade.** *Code:* both ROOT walks skip nested checkouts, identified by what they are
— a directory carrying its own `.git` — rather than by name, because the name is a convention
and the next one will differ. *Test:* the only plant in this suite whose pass condition is
silence — a nested checkout must change neither verdict nor count — watched reporting `MISSED`
with the guard replaced by `if False:`. *Process:* instruction 1 widened, because "recheck
before staging" named the wrong last moment; the moments that touch shared state are the merge,
the push and the tag. *Class:* **a measurement that moves with local scratch state.** Swept by
reading the siblings rather than grepping them — `sloplint.py` walks `SKILL_DIR.rglob`,
`validate_palette.py` does not recurse — so only these two sites were ever exposed.

**What the collision cost, and what it did not.** A version number and 22 version references
in prose and token comments (`since 1.25.0`, `[CORRECTION — 1.25.0]`, `Closed in v1.25.0`),
each of which would otherwise have named a release it is not in. Nothing was discarded and
nothing of theirs was rewritten: 1.25.0 stays exactly as published, its CHANGELOG entry only
moved under the preamble it had landed above. The tag was withheld until the **merged** commit
had its own CI verdict — run 31661837515, 19 jobs, tree `279af78` identical to `main^{tree}`.

**A third, smaller one, with the same shape as instruction 9.** A throwaway script for the
version move printed `floors: _measured_on now names the merged tree` after a replacement that
matched nothing — `floors.json` was not in the list the previous step had bumped, so the
pattern searched for a string that did not exist yet. Exit 0, confident output, no change on
disk. Caught by reading the file. A tool's success line is someone else's claim about your
artifact; your own script's is your claim about it, and you will believe that one.

### 2026-08-13 — a rule I had shipped twice was too strong, and a subagent's wrong finding is what proved it

**Symptom.** `pigeonhole` (1.21.0) and `roster` both stated, in their Motion flavor sections,
that *a duration cannot stop an infinite animation — at 0.01ms it strobes*. A blind routing
run then accused a third pack, `scoreboard`, of shipping that very defect: its reduced-motion
branch sets `--scan-period: 0s` on an infinite scan line.

**Surfaced at** stage 6, by T26b, as a finding **against the wrong pack**. **Owned by** the
two packs that had generalised from one measurement.

**Root cause, and the finding was wrong in a way that made it valuable.** Measured in Chrome
151 rather than argued from the spec: an infinite animation at `0.01ms` yields **two
different computed transforms** when sampled 40ms apart, and the same animation at **`0s`
yields `none` and never moves.** So `scoreboard` is correct — and my sentence was not. A
duration *can* stop an infinite animation; it just has to be exactly zero, and 0.01ms — which
is what a global `*` reduced-motion rule almost always writes, and what `pigeonhole`'s
reference wrote — is the one value that strobes. I had measured the 0.01ms case, drawn a rule
about durations in general, and shipped it in two packs.

**Fixes by grade.** *Doc:* both packs now carry the precise rule with the measurement, and
the accusation against `scoreboard` is recorded as refuted in `test/scenarios.md` rather than
dropped. *Process:* the class is **a rule generalised from one instance of a two-valued
question.** The instance was true; the generalisation covered a value I never tested.

**A second thing the same run found, and it was this session's own regression.**
`scoreboard`'s pack still documented *"Below 768 the label column drops"* while its kit has
used `@container (max-width: 231px)` since 1.23.0 — a divergence I introduced yesterday while
fixing the kit and not its pack. `SKILL.md` calls a pack/kit difference a defect in one of
them, and nothing checks it: the gate compares a kit's spine to `workbench` and its token
block to the pack, and never compares a kit's *breakpoints* to the pack's prose. Fixed in the
pack; the missing check is not filed because a check that reads prose against CSS is the
"tell a measurement from an argument" problem that B-013 has been open on since 2026-08-12.

**And the finding that paid for the whole run.** Four of `roster`'s five derived colours clear
AA on the white field and on **none** of its three tinted surfaces — 4.32, 4.10, 4.06 — while
the token layer claimed they cleared "BOTH surfaces", meaning two of the four it ships. The
eyebrow is one of those colours, so an eyebrow on the mint panel rendered at 4.10:1. I had
derived each colour against `--bg` and `--surface-2`, written "both", and never enumerated
what the layer actually ships.

**What stays human.** Nothing here can tell a *tested* rule from an *extrapolated* one. Both
read the same on the page: a sentence with a number in it. The habit that catches the next
one: when a rule quantifies over a range — every duration, both surfaces, all four — count
the range and test its ends, because the sentence will not tell you which member you actually
measured.

### 2026-08-13 — the measurement kept improving the finding, twice

**Symptom, and it was mine to begin with.** My own audit wrote the gap as *"0 of 16 kits
use container queries"*. Two measurements later that sentence was wrong in both
directions, and each correction made the finding sharper.

**First correction: it was not a missing feature, it was a spec being ignored.**
`scoreboard.md` has said since it shipped — *"Container queries for the report surface
and the ledger: `container-type: inline-size`, because both appear inside columns of
different widths on the same page and neither should size against the viewport"* — and
the kit was switching on the viewport anyway. So a ledger in a 320px sidebar on a 1440px
screen kept its wide columns and crushed its leader. "The library has not adopted X" and
"the pack specified X and the kit did not do it" call for different work: the first is a
roadmap item, the second is a defect with a check.

**Second correction: only two of the seven queries had a container answer at all.** Five
turned out to be **PAGE** (a hero's padding, a root token switch — `:root` is inside
nobody's container) or **SELF**: a property on the element that would *establish* the
container, which cannot query its own width. A category error was hiding inside the
count. Sorting them produced the doctrine the release is actually about — three kinds of
breakpoint, not two — and it is a better artifact than the conversion would have been.

**And the same class bit the prose I wrote in the same hour.** `pigeonhole`'s new answer
told an implementer to put `container-type` on the labelled row's and the FAQ's
"wrapper", when those properties sit on the row and the `<dl>` themselves — the SELF case
verbatim, defined two files away in the same release. Caught by checking every component
the seven answers name against what each kit exports: five right, two wrong. It shipped
in 1.23.0 and was corrected in 1.23.1, which is the honest cost of writing seven
paragraphs of doctrine and its application at the same time.

**A process slip worth writing down.** I staged this release with `git add -A`, which is
the one thing standing instruction 1's remedy names — *commit an explicit path list,
never `-A`* — then caught it, reset, and staged 31 paths by name. Nothing was swept,
because no other run was live. That is luck rather than compliance. **Two days running,
the remedy was known and the habit was not**: yesterday it was reading a gate from the
wrong tree, today it was `-A`. Both are instruction 1, and neither is a detection
problem.

**One thing the new check taught me about checks.** Its first draft looked back a fixed
400 characters for the marker and missed a five-line reason whose marker sat at
character 425 — so a block with a *longer* explanation failed while a terse one passed.
A check that punishes a longer reason teaches authors to write shorter ones, which is
the opposite of what a declared-exception rule is for. It reads the whole comment now.

**What stays human.** The count was the easy part; the categories were the work. Nothing
mechanical would have told me that five of seven breakpoints have no container answer —
that came from asking, per block, *which element establishes the container here*, which
is the same question as *what is this component, actually*.

### 2026-08-13 — a green from the wrong tree, and a ban that was really a parser

**Symptom, the process one.** Mid-run I ran `python3 test/validate_palette.py`, read
`OK (906 checks)`, and moved on. The gate that ran was the **main tree's** — the old one,
without the extension I was testing — because the shell's working directory had silently
returned to the project root after a command that `cd`-ed into a scratch directory
outside it. The same session then printed `has parse_relative: False` for a function
sitting in the file I had just edited. Two commands earlier, that green would have been
read as evidence the extension worked.

**Surfaced at** the first debugging print, by luck rather than by design. **Owned by**
whichever step assumed the working directory is stable across tool calls. It is not, and
the harness says so in its own output when it resets.

**Root cause.** An isolated `git worktree` is the remedy standing instruction 1
prescribes, and it introduces a second tree with **the same relative paths**. Every
relative path is then ambiguous, and the one thing that disambiguates it is not owned by
the run. The previous release hit the same class from the other side: two close-out
documents landed in the main tree while two others went to the worktree, and it took a
four-way `grep -c` to establish where each had gone.

**Fix by grade.** *Process, one line:* in a worktree run, every command that touches the
tree opens with `cd <worktree> &&` in the same invocation, and every read states an
absolute path. **A verification that cannot say which tree it read is not a
verification** — which is standing instruction 9 pointed one level down, at the
filesystem instead of the artifact.

**The substantive finding, and it was hiding in plain sight for eleven releases.**
`STYLE_PACK_TEMPLATE.md` told authors to keep `color-mix()` out of the token layer *and
gave the reason in the same sentence*: the palette gate cannot compute a value it cannot
parse. A tooling limitation had been written down as doctrine and was read as taste. The
cost, once measured: **42 `rgba()` literals across eight token layers are ΔE 0.00 from a
token in their own file** — a token's channels restated by hand, which is the live
mechanism behind B-023/B-024.

Two things made the fix trustworthy rather than plausible. The arithmetic was checked
against **Chrome 151's own computed values** across eleven cases, worst ΔE 0.004, rather
than against my reading of the interpolation spec — the browser is the thing being
modelled, so it is the oracle, and this is the same move as measuring a reference's
rendering instead of its stylesheet. And two of the four plants assert on the **ratio**
message rather than on the parse: a mix that misses AA can only fail that way if the
value was really computed, which is the difference between a code path that is tolerated
and one that is checked.

**A blind spot was closed in the commit that would otherwise have opened it.**
`themes()` decided whether a block was a theme by testing for a `#` or `oklch(` prefix,
so a dark theme written in `color-mix()` would have been read as "overrides no colour"
and skipped entirely. Teaching the parser two new forms without widening that test would
have opened a hole in the same change that closed a limitation.

**And the sweep's own framing needed correcting before it shipped.** The script first
called the 13 near-miss literals "a derivation that no longer tracks". They are not:
`rgba(255, 255, 255, 0.8)` beside an off-white `--bg` may be deliberately pure white.
Near is *ambiguous*, not wrong, and that distinction decides whether the follow-up is one
sweep or thirteen conversations. It is written into B-028 rather than left in the tone.

**What stays human.** No check can tell a limitation from a decision. The sentence that
hid this one was **true** — the gate really could not parse `color-mix()` — and it sat
inside a rule phrased as a preference. The habit that catches the next one: **when a rule
states its own reason, check whether the reason is still true.**

### 2026-08-12 — the ramp was copied from the reference instead of fitted to my own readings

**Symptom.** `pigeonhole` shipped with `--size-display: clamp(34px, 5.6vw, 60px)`
and a Responsive table claiming 60px at 768. A blind routing run recomputed it:
5.6vw of 768 is **43.01px**, and the clamp reaches its 60px ceiling only at
1071.4px. The section head had the same shape — `clamp(27.2px, 3.6vw, 40px)` gives
27.65px where the table claimed 40px. Two more in the same family: `--lh-display: 1`
cannot produce the 34px/42.5px the same row states (42.5/34 = 1.25), and the Hero
section described the product frame as beginning **below** a 900px fold at y≈713.

**Surfaced at** stage 6, by the pack's own routing scenario, hours after three green
gates and a green CI had passed the pack. **Owned by** stage 5, which wrote the
token layer.

**Root cause, and it is one habit rather than four mistakes.** I measured the page at
three viewports and got display sizes of 34 / 60 / 60. Then, writing the token
layer, I reached for the reference's **declared** `clamp()` list — seven of them in
its stylesheet — picked the one whose ceiling matched (`clamp(40px, 5.6vw, 60px)`),
adjusted its floor to the 34px I had measured, and shipped it. The declaration and
the measurement were never reconciled: the reference's display does not resolve from
that clamp at all, and its 40px floor cannot reach 34px. **A value read off the
reference's source is not the same claim as a value read off the reference's
rendering**, and where they disagree the rendering is the fact. The ramps are now
*fitted* — 7.82vw and 5.21vw, which reproduce all three readings — and the token
layer says they are fitted, because a coefficient nobody can re-derive is a number
the next reader has to trust.

This is the same class as the previous entry's *four ratios stated from the OKLCH
instead of the shipped hex*, one unit up: **stating a number computed from a parent
representation rather than from the thing that ships.** It had already been caught in
colour and was not looked for in type. Earlier in this very run the same class was
caught a third time, in the derivation script: candidates were tested for 4.5:1
before being rounded to eight bits, so `#007b22` would have shipped claiming its
parent's 4.50:1 where the hex measures 4.38.

**The finding that mattered more than the arithmetic.** Under
`prefers-reduced-motion: reduce` the token layer collapsed `--dur-marquee` to
0.01ms, in parity with the reference's global rule. On an **infinite** animation that
does not stop anything — it strobes it roughly a hundred thousand times a second, at
exactly the reader the media query protects. A duration cannot switch off an
animation, and no custom property can express `animation-play-state`. The marquee is
paused in the component layer now. The pack's closing boast — *a pack that regressed
that would be worse than its own source* — was describing what the pack itself had
done.

**And one argument that was wrong while its conclusion was right.** The pack claimed
that deriving the category inks to clear AA **caused** the hues to collapse under
deuteranopia, citing ΔE 4.42 → 1.24. The agent pointed out that 4.42 is already less
than half the gate's hard floor of 10: the reference's brighter inks were never
distinguishable to that reader either. Derivation makes it worse; it does not make it
true. The conclusion — colour cannot carry this meaning, so the label word is the
channel — survives on stronger ground.

**Fixes by grade.** *Mechanical:* the derivation script now reads its ratio off the
rounded hex, and the type ramps are fitted with the arithmetic written beside them.
*Doc:* twenty-two findings actioned in the pack, its token layer, its kit and four
enumeration sites; six tokens added that the pack stated and the layer lacked.
*Process:* nothing new — instruction 8 already covers reproducing a delegated
finding, and it is what caught all four.

**What stays human.** No gate in this repository can evaluate a `clamp()` against a
measurement taken in a browser, and one that tried would need the browser. The
available substitute is the one that worked twice in a row now: **run the pack's own
routing scenario before the tag, and read every finding as a hypothesis.** The
cheaper half is a habit rather than a check — when a pack states a size at a
viewport, the number in the token layer has to be *derived from that reading*, not
recognised in the reference's source and adopted.

### 2026-08-12 — the style card was wrong, and so was the sentence I wrote about my own table

**Symptom, the one that shaped the pack.** The run opened from a Refero style card
describing `fingerprint.com` as putting its product panels in *"dark and terminal-like"*
containers, and the brief's register said the data lives in a dark window cut into the
page. Measured at 1440x900: the hero's focal element is **light** — a hairline-ruled
grid of label-over-value cells — and no element on the page has a dark background at
all. The dark surface exists in 97 rules and every one of them is an incognito
selector: 134 rules re-skin the instrument **when it detects the reader is hiding**.

**Surfaced at** the first screenshot, before a token was written. **Owned by** stage 0,
which took a reference-library description as a premise instead of as a hypothesis.

**Root cause.** `DESIGN_SYNC_BRIDGE.md` §4 already says a style found in a reference
server is a *candidate source* and that identity comes from live extraction. The rule
was obeyed in the end — but the brief had already written the candidate's claim into
its register section as though it were measured, and that section is what the design
would have been built from if the screenshot had come later. Four of the card's
statements were checkable and wrong: the display weight (600 against a computed **500**),
the container (1232 against **1248**), the section rhythm (a 48px gap against
full-bleed alternating bands with `margin: -1px`), and the dark focal panel.

**The better outcome, and it is worth naming.** The measurement did not just correct
the register, it produced a sharper one. *A dark window in a page* is a layout idea. *An
instrument that turns dark when it catches you hiding* is the product's argument
finishing itself without a sentence of copy, and it is the pack's signature element.

**Symptom, the sharper one.** The pack's own routing scenario returned eleven defects
in the pack shipped in the same commit. Two mattered: in the alarm state the danger
text on its own tint measured **4.44:1** — a fail, in the one cell that state exists to
render — and the focus ring at `--accent` measured **2.85:1** on `--accent-wash`, the
surface the pack's own Micro-interactions section mandates for a selected cell. Both
were pairs I had never computed: I checked every status against `--bg` and never
against the tint the components actually put it on.

**Root cause.** A palette gate that checks *field against ink* and *peer against peer*
does not check *text against the surface a component rule pairs it with*. The gate was
green through both defects and remains green through the fixes; what found them was an
agent reading the pack as an implementer would, and asking what the Components section
would render.

**Symptom, the one that is mine twice over.** `SKILL.md` shipped "Six of the fourteen
are on the core contract … The other **seven** answer all four" — six plus seven
against a fourteen-row table, with the new pack as the one left out. I introduced it by
changing `thirteen` to `fourteen` and leaving the remainder alone. **The identical
defect shipped in the previous pack release** and was found the same way, by a scenario
agent, and fixed then as an instance.

**Fixes by grade.** *Mechanical:* `validate_contract_split()` derives all three numbers
from the pack table, watched saying no on a planted remainder and shipped with a plant
that reads whatever the paragraph currently claims. *Mechanical:*
`validate_counted_claims()` now reads the three manifests, where `marketplace.json` had
said "twelve pluggable style packs" above a list of thirteen for two releases. *Doc:*
eleven pack fixes, each with its number in Gotchas. *Process:* instruction 1 widened
with the remedy it never carried.

**What stays human.** Two things a gate here cannot do. It cannot tell whether a
reference description was measured or repeated — the answer is to open the site before
writing the register, not after. And it cannot pair a colour with the surface a prose
rule puts it on; a gate that tried would have to parse Components, which is judgement.
The available substitute is the one that worked: run the pack's own routing scenario
**before the tag**, and read every finding as a hypothesis.


### 2026-08-12 — the rule was two paragraphs above the sentence that broke it

**Symptom.** `DESIGN_SYNC_BRIDGE.md` §4 shipped in 1.14.0 saying Refero was *"alone
among the three"* in returning flows, and `super-ux`'s `ux-flows` said the same. Both
were false: `mcp__mobbin__search_flows` has always existed. The correction went out an
hour later, in two repositories, as `1.14.1` and `0.35.1`.

**Surfaced at** the moment Mobbin was authenticated — the tools appeared, and the first
one in the list refuted the sentence. **Owned by** the session that wrote it, which had
Mobbin registered, unauthenticated, and invisible.

**Root cause.** The claim was comparative and one of the three things compared could not
be inspected. Nothing in the session could have confirmed or denied it; it was written
anyway, in the same declarative voice as the two halves that *were* checked, and it sat
between them where it inherited their credibility. The rule that forbids exactly this —
**gate on the tools present in the session, not on the config** — is two paragraphs above
it in the same file. It was written for the *reader* of the skill and never turned on the
*author* of the paragraph.

**Why nothing caught it.** Standing instruction 5 covered the same class and was scoped
to the wrong noun: it said a *pack* needs a reachable reference, and this was a claim
about a *tool*. Three gates, 2,455 checks and a green CI cannot see it either — no check
in this repository can open an MCP server and ask what it exposes, and one that tried
would fail for every reader who has not signed in. This is a class the gates structurally
cannot hold.

**Fixes by grade.** *Doc:* both files corrected against Mobbin's live tool surface, with
the wrong claim named as a `[CORRECTION]` rather than silently replaced — the same
discipline the packs use, for the same reason. *Better than the fix:* the replacement
distinction is more useful than the false one. Both servers return flows **in different
media** — Mobbin as preview images per step, Refero as goal/action/system-response text —
so the guidance is now "read one to draw the diagram, look at the other to check it",
which is actionable in a way "only one has flows" never was. *Process:* instruction 5
widened from *a pack's origin* to *any claim about something outside the session's
reach*.

**The check that catches it next time.** There isn't one, and pretending otherwise would
be the same defect one level up. What stays human, and is now written into instruction 5:
**before a comparative sentence ships, ask whether every thing it compares was reachable
when it was written.** If one was not, mark it unverified or leave it out. An
authentication prompt is not an obstacle to route around — it is the session telling you
which half of your sentence you cannot see.

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
