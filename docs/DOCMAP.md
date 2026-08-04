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
| Style-pack rules (palette/type/motifs/bans) | `styles/<pack>.md` (ten-heading contract) | `SKILL.md` table routes to it; README summarises in one line |
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
| **New style pack** | `styles/<pack>.md` with all nine headings · `styles/tokens/<pack>.css` · route from the `SKILL.md` pack table · name it in `bin/cli.js` output · README pack table · **a kit under `kits/<pack>/`** · CHANGELOG | `python3 test/validate.py` |
| **New kit component** | the shared spine stays identical across all six kits · no raw color literal outside the token block · `.prompt.md` beside it | `python3 test/validate.py` |
| **Any release** | four-way version sync · CHANGELOG entry · tag · GitHub release · `npm publish` · refresh local installs | `test/validate.py` + `npm view sheleg-design-skill version` + `gh run list` |
| **Behavior an agent must follow** | a scenario in `test/scenarios.md` | the scenario run by a fresh subagent |
| **A settled decision** | an ADR in `docs/adr/`; if it overrides an earlier record, that record's status line says so | link check in `test/validate.py` |

## The gate

```bash
python3 test/validate.py
```

`test/validate.py` **is** the documentation gate for this repo — there is no second
`check-docs.sh`. Ratchet floor at seeding: **272 checks**, measured on `main`
(`5e59263`) on 2026-08-04 — computed, not restated; the wiki still carries the stale
v1.2.0 figure of 194. The count may rise, never fall.
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
