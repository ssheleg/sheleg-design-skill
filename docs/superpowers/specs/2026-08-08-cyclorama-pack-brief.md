# Task brief — `cyclorama` style pack

**Run:** 2026-08-08 · branch `feat/cyclorama-pack` (from `main` @ `8ad3b8a`)
**Pipeline:** task-pipeline, stages 0→10 · **Model:** Opus 5 (1M context), confirmed at preflight
**Operator decisions locked at stage 0:** name, motion class, accent resolution, status
encoding, working location, release scope.

## Scope

Add the **eighth** style pack to the SHELEG Design skill, extracted from the live
reference <https://www.codos.ai/> by reading its computed styles on 2026-08-08.
It is a **cinematic** pack — the first whose reference already implements this
skill's own core pattern — so it carries the fourteenth heading (`## Motion
flavor`) as well as the thirteen the widened contract requires.

Out of scope, stated so it cannot be quietly re-scoped in: no change to the
motion doctrine, no change to the other seven packs, no new gate script.

## Source ledger — phase 1, before the first question

| Source | What it says about this task | Freshness |
|---|---|---|
| `~/.claude/CLAUDE.md` | repo-changing work routes through task-pipeline; visual layer through sheleg-design; post-release DoD includes refreshing local installs | current |
| `~/CLAUDE.md` (machine) | publish flow, one-channel-per-skill invariant, restart after a plugin change | current |
| repo `CLAUDE.md` | **absent** — this repo has none; doctrine comes from the two above | — |
| `docs/DOCMAP.md` | propagation matrix for *New style pack*: pack md · token css · `SKILL.md` route · `bin/cli.js` name · README row · **a kit** · CHANGELOG. Gate = `validate.py`. Ratchet floors 787 / 269 / 184 at `97e7f63` | **verified fresh** — re-measured live on `8ad3b8a`: 787 / 269 / 184, exact match |
| `docs/superpowers/retro.md` | eight standing instructions, all in force. #1 concurrency, #2 release state from registry, #4 negative branch, #5 addressable origin, #6 gate watched saying no, #7 CI parity, #8 reproduce delegated findings | current, read in full |
| `docs/adr/0002` | kits ship in the npm package, never in the installed bundle | current |
| **ADR-0001 `style-pack-naming`** | packs are named for the **register**, never the source brand → `cyclorama` complies, `codos` would not | **absent from `main`** — exists only on `feat/lecture-hall-pack`; the register starts at `0002`. Cherry-picked by this run (REQ-012) |
| `feat/lecture-hall-pack` brief + carryover | a prior eighth-pack attempt, held at stage 0 on concurrency (C1). Its C5 flagged npm 2FA as the step where releases strand | superseded — C5 closed by this run with evidence, below |
| `styles/STYLE_PACK_TEMPLATE.md` + `templates/style-pack-template.md` | the 13-heading widened contract; the pair is enforced byte-identical | current |
| `test/validate.py` | the pack **and kit** contract: `SPINE = Button, Card, Chip, Stat, Heading, Rule` with `*Props` byte-identical to `kits/workbench`; a `.md` per component carrying `category:` from Foundations/Actions/Surfaces/Data/Signature; `styles.css` must *start with* the token layer verbatim, carry `/* ── components ── */`, and hold no colour literal after it; `.design-sync/config.json` with five fields and no `projectId`; `conventions.md` > 200 chars; no committed `guidelines/` | current |
| `test/validate_palette.py` | tokens must be hex / rgb() / oklch() — **`color-mix()` is a FAIL, not a skip**; `--bg`↔`--ink` ≥ 4.5:1; semantic peers ≥ 15 normal and ≥ 8 under each dichromacy, hard floor 10; the literal escape phrase is `never by colour alone` | current |
| `test/sloplint.py` | bans `100vh`, scroll listeners, bare `ease-in`, layout transitions, pure black; a widened pack owes an addressable origin; `## Bans` must exceed 40 chars | current |
| `.github/workflows/validate.yml` | runs all three gates, both self-tests, CLI, installer, `claude plugin validate --strict`, and a **kit matrix derived from `ls -1 kits`** (`:76`) — so `kits/cyclorama` is covered without editing CI | current |
| `.github/workflows/release.yml` | tag `v*` → validate → GitHub release → npx smoke → `npm publish --provenance`, gated on repo vars | current |
| `test/scenarios.md` | T1–T14; **T13 is the negative-branch shape** standing instruction #4 requires | current |
| `graphify-out/graph.json` | built, 987 nodes, carries `built_at_commit` — stage 9 must `--update` | built 2026-08-06 |
| Obsidian wiki | `projects/sheleg-design-skill/` — overview + `concepts/` — stage 9 target | to re-read at stage 9 |
| Live reference `codos.ai` | the measurements below | read 2026-08-08 |

**Therefore not asked:** gate commands, ratchet floors, kit contract, pack
contract, version number, docs homes, CI parity mechanism, retro location.

## Evidence gathered at stage 0, not assumed

**Standing instruction #1 — concurrency.** `git reflog -8` shows no HEAD move this
run did not make. `git status --porcelain` empty. No file under the tree has an
mtime inside six hours. One stale worktree exists at
`…-wt/audit-harvest` on `feat/audit-harvest-v1.5.0`. **The second half of the
instruction is still owed: re-check immediately before `git add`.**

**Standing instruction #2 — release state from the registry and the tags.**
`git tag` and `git ls-remote --tags origin` both stop at `v1.7.0`; `npm view
sheleg-design-skill version` → `1.7.0`. **`v1.8.0` is free.** The manifests were
not consulted for this.

**C5 from the held run — closed with evidence, not with waiting.** Repo variables
`RELEASE_ENABLED=true` and `PUBLISH_NPMJS=true`; secret `NPM_TOKEN` present since
2026-07-30; `release.yml` succeeded for both `v1.6.0` and `v1.7.0`. Local `npm
whoami` returns 401, so publishing is **not** a local act here — the single
outward, irreversible step is `git push origin v1.8.0`, which triggers the
workflow. That is where stage 7 stops and asks.

**Entry audit (`setup.md`) — not offered, with the reason recorded.** It is
offered when the doc map is absent or stale. `docs/DOCMAP.md` exists and its
ratchet floors match a live measurement exactly, so neither trigger fires.

## Measurements — the palette, computed with the gate's own math

Every ratio below was produced by importing `test/validate_palette.py` rather
than by a second implementation, so the pack cannot claim a number the gate
disagrees with. Command: `scratchpad/measure.py`.

**The field is not one colour.** `html.lp-on` runs `ctaCycle`, a **32 s
`ease-in-out` infinite** six-stop cycle. Every contrast claim in this pack is
therefore stated against the **worst** stop, not a representative one.

| Stop | Hex | `--ink` #1a1a1a on it | `--ink-soft` #3a3a3a on it |
|---|---|---|---|
| 0 % / 100 % | `#F9DEF3` | 13.90:1 | 9.08:1 |
| 16.67 % | `#F3D9B8` | **12.79:1** (worst) | **8.36:1** (worst) |
| 33.33 % | `#F9E0E2` | 13.91:1 | 9.09:1 |
| 50 % | `#EAE3EE` | 13.86:1 | 9.06:1 |
| 66.67 % | `#E6EEE3` | **14.67:1** (best) | 9.59:1 |
| 83.33 % | `#EEEAE3` | 14.52:1 | 9.49:1 |

**The accent defect, measured.** `#FF8C00` as text on the field is **1.71–1.97:1**
across the six stops — the reference paints its section eyebrows this way.

**Why darkening is not the fix — the finding that reversed a stage-0 decision.**
The warm-dark region is already occupied by two of the reference's own semantics,
so every orange dark enough to carry text lands on one of them. `--accent-ink`
would not be checked by the gate (it is not a peer), which is exactly why it was
computed by hand:

| Candidate | Worst-stop contrast | Nearest semantic | Separation |
|---|---|---|---|
| `#903A00` | 5.53:1 ✓ | `--danger` `#7a3a1c` | **4.6** normal — under the hard floor of 10 |
| `#A14700` | 4.52:1 ✓ | `--danger` | 9.0 normal, 7.4 protanopia — under both |
| `#C56200` | 3.01:1 (large text only) | `--warning` `#9a6a00` | 8.5 normal, **1.4** protanopia |
| `--ink-soft` `#3a3a3a` | **8.36:1** ✓ | — | a neutral, not a semantic peer |

**Resolution (operator, stage 0): the accent is a fill colour and nothing else.**
No `--accent-ink` token is created; eyebrows take `--ink-soft`. Zero invented
values. `--on-accent` `#1a1a1a` measures **7.46:1** on the accent and 7.39:1 on
`--accent-hover` `#e69900`.

**Status separation.** `--good` `#2c5a44` and `--danger` `#7a3a1c` separate by
14.0 at full colour, **7.2 under protanopia and 5.9 under deuteranopia** — above
the hard floor of 10, below both soft floors. `--warning` / `--danger` sit at 14.8
normal. **Resolution (operator): declare the secondary encoding.** This is a
measurement of the reference, not an excuse for it: the live status pill renders
`● Listening` with the word, and every comparison row pairs its dot with a text
phrase.

## Locked decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Pack name **`cyclorama`** | A register name, per ADR-0001. A cyclorama is a seamless backdrop that changes colour behind a fixed subject — which is what `ctaCycle` does. `codos` would violate the ADR. |
| D2 | **Cinematic**, not standalone | The reference ships GSAP ScrollTrigger with pinning (`pin-spacer-problemPin`) and two WebGL canvases whose formation holds then redeploys. A standalone pack would ban its own reference's defining behaviour. |
| D3 | Accent is **fill-only**; no `--accent-ink` | Measured above. Reverses the stage-0 answer that assumed a second token was clean. |
| D4 | Status carries the **`never by colour alone`** declaration | Measured above; matches the reference's own behaviour. |
| D5 | Work in **this checkout** on `feat/cyclorama-pack` | **Operator override, recorded out loud.** `docs/DOCMAP.md` → *Shared state* says every concurrent run must take its own `git worktree`. The operator outranks the document; the document is logged for the stage-9 update, and instruction #1's pre-staging re-check still runs. |
| D6 | Release **v1.8.0** by tag push, publish via CI | Free per the registry and the tags. Local npm is unauthenticated by design. |

## REQ table — frozen

Adding is free. Removing or narrowing needs the operator's agreement, recorded in
the carry-over ledger.

| ID | Requirement | How it is verified | Status |
|---|---|---|---|
| REQ-001 | `styles/cyclorama.md` carries all thirteen widened headings plus `## Motion flavor`, and an addressable `Origin:` | `python3 test/validate.py` (pack section) + `python3 test/sloplint.py` (`lint_packs`) | open |
| REQ-002 | `styles/tokens/cyclorama.css` parses entirely — no `color-mix()`, no uncomputable value | `python3 test/validate_palette.py` prints a ratio line for the pack | open |
| REQ-003 | `--ink` on `--bg` clears WCAG AA on **every** cycle stop, and the pack states the worst | `validate_palette.py` ratio line ≥ 4.5; the Palette table quotes 12.79:1 | open |
| REQ-004 | The accent is documented as fill-only, with the measured 1.71–1.97:1 and the three rejected candidates in `## Gotchas` | `grep` for the ratios in `styles/cyclorama.md`; read-through at stage 10 | open |
| REQ-005 | The pack declares `never by colour alone`; the palette gate reports the tight pairs as *covered* rather than failing | `validate_palette.py` output contains `covered by secondary encoding` for cyclorama | open |
| REQ-006 | `kits/cyclorama/` exists with the six spine components whose `*Props` match `kits/workbench` byte-for-byte | `validate.py` kit section | open |
| REQ-007 | `kits/cyclorama/src/styles.css` **starts with** the token layer verbatim and holds no colour literal after the components marker | `validate.py` kit checks 6 and 7 | open |
| REQ-008 | The pack is routed from `SKILL.md`, `README.md`, `bin/cli.js` and `cursor/rules/*.mdc` | `validate.py` — four separate checks per pack | open |
| REQ-009 | `.cursor/skills/sheleg-design/` mirrors the bundle file-by-file, both directions | `validate.py` mirror check | open |
| REQ-010 | All three gates exceed their ratchet floors (787 / 269 / 184) and both `--self-test` flags pass | `npm test && npm run selftest`, counts printed | open |
| REQ-011 | `test/scenarios.md` gains **T15a** (must select `cyclorama`) and **T15b** (must still select the neighbour), each run in a separate fresh context | the two subagent runs, verdicts recorded in the file — standing instruction #4 | open |
| REQ-012 | `docs/adr/0001-style-pack-naming.md` exists on this branch, cherry-picked, with its status line noting the second application | `ls docs/adr/`; `validate.py` link check | open |
| REQ-013 | Four-way version sync at 1.8.0 and a CHANGELOG top entry | `validate.py` version-sync check | open |
| REQ-014 | `package.json` scripts and `.github/workflows/validate.yml` steps agree — no gate reachable by command but unrun by CI | the diff, printed — standing instruction #7 | open |
| REQ-015 | `v1.8.0` released: workflow green, `npm view sheleg-design-skill version` → `1.8.0` | `gh run list` + `npm view` | open |
| REQ-016 | Local installs refreshed on this machine | `npx --yes sshlg-skills@latest update`, then the shadow-check prints nothing | open |
| REQ-017 | `DOCMAP.md` floors updated, wiki page updated, `graphify-out/` refreshed and checked against the docs | stage 9 outputs; `/graphify . --update` | open |

## Autonomy sweep

| Row | Answer |
|---|---|
| Model | Opus 5 (1M context) — the most capable available; confirmed once, not re-asked |
| Run mode | Advance without check-in between items; stop only at the two manual gates |
| Manual gates | **stage 3** (design spec) and **stage 7** (`git push origin v1.8.0`) |
| Shared state | `ungated`; D5 override recorded; instruction #1 re-check owed before staging |
| Source of truth | `git rev-list --count HEAD..main` = 0 — this checkout is the one that ships |
| Duplicates | The copy that ships is what `bin/cli.js listBundleFiles()` walks: `plugins/sheleg-design/skills/sheleg-design/`. `.cursor/` is a mirror the validator checks in both directions (`validate.py:280-294`). The pack skeleton is a byte-identical pair: `styles/STYLE_PACK_TEMPLATE.md` ↔ `templates/style-pack-template.md` |
| Fixtures | Nothing persists between runs; the gates are pure Python over files. The kit build needs `npm install --no-save typescript@^5.6.0 @types/react@^18.3.0 react@^18.3.0` |
| Work-list | This session's TaskList plus the carry-over ledger. No external tracker for this repo |
| Branch / commits | `feat/cyclorama-pack` off `main`; Conventional Commits; explicit path lists on `git add`, never `-A` |
| Integration | Merge to `main` after gates pass on the branch, then re-verify on the assembled `main` before tagging |
| Test command | `npm test` (validate → palette → sloplint → `node --check`) and `npm run selftest` |
| Lint / deploy | The gates are the lint. Deploy = tag push; the workflow does the rest |
| Post-deploy | `gh run list -w release.yml`; `npm view`; then the local-install refresh |
| Docs / wiki / graph | `DOCMAP.md`, `retro.md`, the wiki project page, and `graphify-out/` — all three close at stage 9 |
| Escalation | Decide alone inside the repository; escalate the tag push (outward, irreversible) |
| UI verdict | No product UI is being built — this is a design-system artifact. super-ux is not armed; no Figma destination is needed |

## Done criteria

All seventeen REQ rows closed with evidence, three gates above their floors, the
scenario pair green in both directions, `npm` serving 1.8.0, local installs
refreshed, and the retrospective pruned and stamped.

## Open assumptions

- The register positioning and the kit's signature-component list are **proposals
  for the stage-3 manual gate**, not settled here. The prior run deferred exactly
  this call (its C2); this run resolves it at the gate that owns it.
- `GT Alpina Typewriter` is a licensed face. The pack must name substitutes that
  are actually obtainable; verified at stage 1.
