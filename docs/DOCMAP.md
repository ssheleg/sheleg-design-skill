# Doc map — sheleg-design-skill

Where each kind of fact lives, what a change of each type obliges, and what proves
it. Seeded 2026-08-04 by the `2026-08-04-design-sync-bridge` pipeline run.

## Registers — one home each, never two

| Register | Home | Id form |
|---|---|---|
| **Decisions** | `docs/adr/` | `ADR-NNNN` (`0001-slug.md`, sequential, never renumbered) |
| Design records (per pipeline run) | `docs/superpowers/specs/` | `YYYY-MM-DD-<topic>-{brief,design,carryover}.md` |
| Plans | `docs/superpowers/plans/` | `YYYY-MM-DD-<topic>.md` |
| Retrospective | `docs/superpowers/retro.md` | standing instructions, capped at ten |

There is **no** `docs/DECISIONS.md` and there must not be: `docs/adr/` is the
decision home. A run that settles something records it as an ADR.

## Single homes — the one place each fact is allowed to live

| Fact | Its single home | Everywhere else must derive, never restate |
|---|---|---|
| Style-pack token values | `plugins/sheleg-design/skills/sheleg-design/styles/tokens/<pack>.css` | pack markdown tables are documentation; kit `styles.css` copies the file verbatim |
| Style-pack rules (palette/type/motifs/bans) | `styles/<pack>.md` (thirteen-heading contract, plus `## Motion flavor` for a cinematic pack) | `SKILL.md` table routes to it; README summarises in one line |
| The motion methodology | `SHELEG_DESIGN.md` | `SKILL.md` states the five principles only |
| The Figma contract | `FIGMA_BRIDGE.md` | — |
| The Claude Design contract | `DESIGN_SYNC_BRIDGE.md` | — |
| AI-surface patterns | `AI_PRODUCT_PATTERNS.md` | — |
| The version | `package.json` → mirrored into `marketplace.json`, `plugin.json`, CHANGELOG top entry | four-way sync enforced by `test/validate.py` |
| What ships in the bundle | the bundle directory itself | `install.sh` file list and `README` install table derive from it |

## Propagation matrix — what a change of type X obliges

| Change | Obliges | Proof |
|---|---|---|
| **New file in the skill bundle** | add to `install.sh`'s `for f in …` list · mirror into `.cursor/skills/sheleg-design/` · link it from `SKILL.md` if it is a companion doc · add it to the README install table | `python3 test/validate.py` |
| **New style pack** | `styles/<pack>.md` with **all thirteen headings** (plus `## Motion flavor` for a cinematic pack) · `styles/tokens/<pack>.css` · the `.cursor/` mirror · **`install.sh`'s file list** · route from the `SKILL.md` pack table · name it in `bin/cli.js` output · README pack table · name it in a `cursor/rules/*.mdc` · **a kit under `kits/<pack>/`** · a routing scenario **with its negative branch** · CHANGELOG | `python3 test/validate.py` |
| **New kit component** | the shared spine stays identical across **every** kit — the count is derived, never typed, in both `validate.py` and the CI matrix · no raw color literal outside the token block · `.prompt.md` beside it | `python3 test/validate.py` |
| **Any release** | four-way version sync · CHANGELOG entry · tag · GitHub release · `npm publish` · refresh local installs | `test/validate.py` + `npm view sheleg-design-skill version` + `gh run list` |
| **Behavior an agent must follow** | a scenario in `test/scenarios.md` | the scenario run by a fresh subagent |
| **A fork between two packs** | the pack it forks against gains the mirror clause, as a markdown link in both directions | `validate_fork_reciprocity()` in `test/validate.py` |
| **A settled decision** | an ADR in `docs/adr/`; if it overrides an earlier record, that record's status line says so | link check in `test/validate.py` |

## The gate

```bash
python3 test/validate.py
```

`test/validate.py` **is** the documentation gate for this repo — there is no second
`check-docs.sh`, and it is no longer the only gate: `validate_palette.py` and
`sloplint.py` joined it in 1.6.0 and CI runs all three.

Ratchet floors, **measured on `feat/four-packs-v1.9.0` 2026-08-09, not restated**:
`validate.py` **1252** · `validate_palette.py` **412** · `sloplint.py` **224**.
Each may rise, never fall. They were 876 / 305 / 192 at `20797ef` a day earlier,
787 / 269 / 184 at `97e7f63`, and 272 the day before that — a number that goes stale this fast is
exactly why it carries the commit it was measured at.
CI (`.github/workflows/validate.yml`) runs it on every
push and PR, together with a negative self-test that corrupts a version and requires
the validator to fail.

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
