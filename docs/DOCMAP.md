# Doc map — sheleg-design-skill

Where each kind of fact lives, what a change of each type obliges, and what proves
it. Seeded 2026-08-04 by the `2026-08-04-design-sync-bridge` pipeline run.

## Registers — one home each, never two

| Register | Home | Id form |
|---|---|---|
| **Decisions** | `docs/adr/` | `ADR-NNNN` (`0001-slug.md`, sequential, never renumbered) |
| Design records (per pipeline run) | `docs/evidence/specs/` | `YYYY-MM-DD-<topic>-{brief,design,carryover}.md` |
| Plans | `docs/evidence/plans/` | `YYYY-MM-DD-<topic>.md` |
| Retrospective | `docs/evidence/retro.md` | standing instructions, capped at ten |

There is **no** `docs/DECISIONS.md` and there must not be: `docs/adr/` is the
decision home. A run that settles something records it as an ADR.

## Single homes — the one place each fact is allowed to live

| Fact | Its single home | Everywhere else must derive, never restate |
|---|---|---|
| Style-pack token values | `plugins/sheleg-design/skills/sheleg-design/styles/tokens/<pack>.css` | pack markdown tables are documentation; kit `styles.css` copies the file verbatim |
| Style-pack rules (palette/type/motifs/bans) | `styles/<pack>.md` (the thirteen-heading contract, plus `## Motion flavor` for a cinematic pack; a pack still on the always-required nine declares `Contract: core` and says what it leaves undecided) | `SKILL.md` table routes to it and marks the core packs; README summarises in one line |
| **A stated contrast ratio** | the token layer — it is derived, not authored | `validate_stated_ratios()` recomputes every claim whose base the document declares |
| **A count of anything** (packs, kits, scenarios, headings) | derived at check time from the directory | `validate_counted_claims()` |
| The motion methodology | `SHELEG_DESIGN.md` | `SKILL.md` states the five principles only |
| The Figma contract | `FIGMA_BRIDGE.md` | — |
| The Claude Design contract | `DESIGN_SYNC_BRIDGE.md` | — |
| AI-surface patterns | `AI_PRODUCT_PATTERNS.md` | — |
| The version | `package.json` → mirrored into `marketplace.json`, `plugin.json`, CHANGELOG top entry **and `SKILL.md`'s `metadata.version`** | five-way sync enforced by `test/validate.py` |
| What ships in the bundle | the bundle directory itself | `install.sh` file list and `README` install table derive from it |

## Propagation matrix — what a change of type X obliges

| Change | Obliges | Proof |
|---|---|---|
| **New file in the skill bundle** | add to `install.sh`'s `for f in …` list · mirror into `.cursor/skills/sheleg-design/` · link it from `SKILL.md` if it is a companion doc · add it to the README install table | `python3 test/validate.py` |
| **New style pack** | `styles/<pack>.md` with **all thirteen headings** and a `Contract:` line (plus `## Motion flavor` for a cinematic pack) · `styles/tokens/<pack>.css` · the `.cursor/` mirror · **`install.sh`'s file list** · route from the `SKILL.md` pack table · name it in `bin/cli.js` output · README pack table · name it in a `cursor/rules/*.mdc` · **a kit under `kits/<pack>/`** · a routing scenario **with its negative branch** · CHANGELOG | `python3 test/validate.py` |
| **New kit component** | the shared spine stays identical across **every** kit — the count is derived, never typed, in both `validate.py` and the CI matrix · no raw color literal outside the token block · **`<Component>.md` beside it, with a `category:` from the taxonomy** | `python3 test/validate.py` |
| **Any release** | five-way version sync · CHANGELOG entry · tag · GitHub release · `npm publish` · refresh local installs | `test/validate.py` + `npm view sheleg-design-skill version` + `gh run list` |
| **Behavior an agent must follow** | a scenario in `test/scenarios.md` | the scenario run by a fresh subagent — **`validate.py` does not read that file**, so this row's proof is a person running it, and the result is stamped with a commit |
| **A fork between two packs** | the pack it forks against gains the mirror clause, as a markdown link in both directions | `validate_fork_reciprocity()` in `test/validate.py` |
| **A settled decision** | an ADR in `docs/adr/`; if it overrides an earlier record, that record's status line says so | reviewed by hand — `validate.py` resolves relative links but has no ADR status logic. ADR-0001 named a pack that never shipped for four days without any check noticing |

## The gate

```bash
python3 test/validate.py
```

```bash
npm test      # all four gates and all three self-tests — this is the gate
```

`test/validate.py` is one of four, and about a third of the contract.
`validate_palette.py` and `sloplint.py` joined it in 1.6.0; `node --check
bin/cli.js` and the three `--self-test` runs joined `npm test` in 1.10.0, because
until then a developer running `npm test` never watched any gate say no.

**Ratchet floors are enforced, not asserted.** They live in
[`test/floors.json`](../test/floors.json) and every gate compares its own count
before printing OK. Until 1.10.0 "each may rise, never fall" was a sentence in
this file and nothing else — and it mattered: stripping a pack's four widened
headings took `validate.py` 1270 → 1269 and `sloplint.py` 224 → 223, **both still
exit 0**. Deleting a requirement made the gates quieter.

The floors also have to be *measured*, not restated. This file claimed 1252 for
`validate.py` on 2026-08-09; the actual count on that commit was **1270**, and
the branch it named no longer exists, so it could not be re-derived. Read the
floor from `floors.json`; it is the number a machine wrote.

**A floor names its commit or it cannot be re-derived.** On 2026-08-10 the tree
computed 1368 against a recorded floor of 1366, which looked like drift and was
not: the floor was measured at `3af6d97`, and two commits landed after it adding
two relative links the link checker counts. Running the gate at `3af6d97` in a
throwaway worktree returned exactly 1366. A ratchet is allowed to rise; the pair
*number + commit* is what says whether a gap is growth or rot, and a number alone
says neither.

**The bundle stands alone, and that is checked.** `validate_bundle_self_sufficiency()`
(1.11.0) enforces three forms of one class: a repo-only path cited to a reader who
has no repo, a rule whose input the bundle does not carry, and a counted claim
whose members it never enumerates. Each shipped at least once. It covers the three
shapes that have actually occurred and is **not** a general proof — a fourth
instance has to be a new shape, and when one appears it becomes a fourth form here
rather than a fourth ledger row.

CI (`.github/workflows/validate.yml`) runs all four gates, all three self-tests,
a negative test that corrupts a version and requires a failure, a check that each
gate refuses an unknown argument, both installers with a `diff -r` against the
source, `claude plugin validate --strict`, and a fourteen-kit build matrix.
`release.yml` runs every gate too — until 1.10.0 it gated a publish on one of
three.

## Shared state

`ungated` — no lease mechanism is in force in this repo. agent-sync v1.4.3 is
installed on the machine but this repo does not use it; concurrent agents are not
arbitrated here.

This is not theoretical. On 2026-08-04 two pipeline runs worked in the same checkout
at once: one committed the other's draft brief into an unrelated commit (`d042b41`)
and minted `ADR-0001` for a decision the other run had just taken. Until a lease
mechanism exists, **every concurrent run must take its own `git worktree`**, and
`docs/adr/` numbers are provisional until merge.

**Overridden once, on the record.** The 2026-08-08 `cyclorama` run worked in this
checkout rather than a worktree, by the operator's explicit choice, after
evidence showed no live concurrent run (`git reflog`, `git branch -vv`, and no
working-tree mtime inside six hours). The rule stands as written for the
concurrent case; what the override changes is that "no worktree" now has to be a
decision taken against evidence, not a default taken from assumption. The run
still discharged the second half of the concurrency instruction — the tree was
re-checked immediately before `git add`, and every staged path was listed
explicitly.

**Branch hygiene, because it is what makes the concurrency check readable.**
Standing instruction 1 treats "a `feat/*` branch you did not create" as evidence
that another run is live. That signal is worthless while dead branches
accumulate: by 2026-08-08 there were five, four of them long since merged, so
every run had to re-adjudicate the same list and the honest answer was always
"probably nothing". On 2026-08-08 all five were retired — the held branch's
unique records were brought onto `main` first, and one merged branch was pinned
by a clean, seven-day-idle worktree at `…-wt/audit-harvest`, which was removed
with it. **No `feat/*` branches and one worktree remain.**

The rule that keeps it that way: **delete a feature branch when it merges, and
land a held run's records on `main` rather than leaving them on a branch.** From
here, *any* `feat/*` branch means a live run — which is the only state in which
instruction 1 is checking something.

That `ADR-0001` is also no longer provisional: it never merged, so the decision
register began at `0002` for four days while the rule it records was binding. The
`cyclorama` run restored it. **A held branch's ADR is not filed** — if a run
mints a decision and then parks, the decision needs a home on `main` or the next
run rediscovers it by accident.
