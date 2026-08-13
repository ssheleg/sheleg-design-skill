# Brief — fresh-eyes audit of the sheleg-design skill (v1.10.0)

**Run:** 2026-08-10 · task-pipeline · branch `feat/skill-audit-v1.10.0`
**Operator ask (verbatim, translated):** look at the skill with fresh eyes for
things that mislead or confuse, gaps in its documentation and descriptions, and
inaccuracies; analyse every command, the whole pipeline and every micro-action;
find the reasons agents may generate nonsense or lie; produce a large detailed
report on everything found and a work plan for the skill/plugin — then fix it
all autonomously through to a published release.

---

## Source ledger — what this run read before asking anything

| Source | What it gave | State |
|---|---|---|
| `docs/superpowers/retro.md` | 10 standing instructions, read in full; 6 run stamps | current, at cap |
| `docs/DOCMAP.md` | register homes, propagation matrix, ratchet floors, shared-state record | current as of `7abe96e` |
| `docs/adr/0001`, `0002` | pack naming; kits ship in the package, not the bundle | current |
| `docs/superpowers/specs/*` (11 files) | four prior runs' briefs, designs, carry-over, acceptance | historical |
| `graphify-out/graph.json` | 1313 nodes, `built_at_commit=b426ccc` | **one commit stale** (HEAD `7abe96e`) |
| Obsidian wiki `projects/sheleg-design-skill/` | project overview + `concepts/` | present, updated 2026-08-09 |
| `git tag`, `git ls-remote --tags`, `npm view` | `v1.9.0` tagged locally **and** on origin; npm serves `1.9.0` | consistent (instruction 2) |
| `git reflog -8`, `git branch -vv`, `git worktree list` | one branch, one worktree, no `feat/*` | **no concurrent run** (instruction 1) |
| `docs/superpowers/backlog.md` | — | **absent → seeded by this run** |
| `docs/superpowers/verification.md` | — | **absent → seeded by this run** |

**Exposure at entry:** board absent (0 rows), verification ledger absent (0 rows),
so every REQ this run ships is the ledger's first content. Prior runs' carry-over
ledgers: 4 files, all closed at their own stage 10.

## Autonomy sweep

| Question | Answer | Evidence |
|---|---|---|
| Shared state | ungated, but **no live run** | `git reflog -8`, `git branch -vv`, mtimes |
| Branch policy | `feat/skill-audit-v1.10.0`, deleted on merge | DOCMAP "Branch hygiene" |
| Test command | `npm test` (4 gates) + `npm run selftest` | `package.json:22,27` |
| Lint | `node --check bin/cli.js`, `sh -n install.sh` | inside `npm test` |
| Deploy target | git tag + `gh release` + `npm publish` | prior runs |
| Deploy authorization | **`npm whoami` → 401**; `gh` logged in as `sshlg`, default account `ssheleg` failed | measured at stage 0 |
| Docs targets | `docs/DOCMAP.md`, wiki, `graphify-out/` | DOCMAP |
| Figma / UI design | **N/A** — this task ships no visual surface | — |
| Subagents | authorized by operator; every finding reproduced before use | instruction 8 |

## Operator decisions taken at the grill

1. **Deliverable** — report **and** fixes **and** a published release, in one run.
2. **Scope** — all four surfaces: skill bundle · shopfront & packaging · gates &
   tests · kits/ADR/doc-map/wiki/graph.
3. **The half-split library** — backfill the three packs whose reference is
   addressable (`atrium`, `orchard`, `editorial-luxury`); **do not invent** the
   four widened sections for the three with no address (`instrument-console`,
   `workbench`, `briefing-room`) — mark them instead, in the pack and in the
   routing table, with what the agent will have to decide itself.
4. **Version** — `1.10.0` (minor: new gates and new pack sections are behaviour).
5. **Gates** — maximum ratchet: every finding class becomes a script with a
   planted defect, not a ledger row.
6. **Report** — `docs/audit/`, in English.
7. **Autonomy** — run every stage gate as `auto`, through to the published release.

## REQ table — the request as an addressable list

Frozen. Adding is free; removing needs the operator.

| REQ | Requirement | Verified by |
|---|---|---|
| **REQ-01** | Every counted/enumerated claim about the skill is true | new `validate.py` check + `grep` of each site |
| **REQ-02** | Status-token vocabulary contradiction resolved: no cross-cutting doc names a token most packs lack | new check: every token named in a bundle doc exists in the packs that doc claims it for |
| **REQ-03** | Ramp/accent vocabulary in the `dataviz` handoff is true of the packs it addresses | same check as REQ-02, plus the handoff table rewritten by role |
| **REQ-04** | `MOTION_DOCTRINE.md` reaches every channel that ships the skill | README table, `cli.js` help, cursor rule; new check |
| **REQ-05** | The pack contract has one name and one count everywhere it is stated | new terminology check across 6 files |
| **REQ-06** | `DESIGN_SYNC_BRIDGE.md` no longer instructs an author to ship a nine-heading pack | edit + check |
| **REQ-07** | The `/sheleg-design` command routes to all twelve packs, not three | edit + new manifest/command enumeration check |
| **REQ-08** | `plugin.json` and `marketplace.json` descriptions name the current library | edit + new check |
| **REQ-09** | Narrow vs widened packs are declared, so an agent knows what a pack does not specify | pack front-matter marker + routing table column + check |
| **REQ-10** | `atrium`, `orchard`, `editorial-luxury` carry the widened four, sourced from their live references | `validate.py` widened-contract check + provenance note per section |
| **REQ-11** | Reference-implementation file paths cannot be mistaken for files that exist | edit at each `**File:**` site |
| **REQ-12** | Every claim in README's "Development" section is backed by code in `test/validate.py` | claim-by-claim diff, recorded in the report |
| **REQ-13** | Every new check is watched failing on a planted defect and against a real file | `--self-test` output + a recorded live failure |
| **REQ-14** | Every gate runnable locally runs in CI | scripts ↔ workflow diff (instruction 7) |
| **REQ-15** | The audit report exists, with `file:line` evidence for every finding | `docs/audit/2026-08-10-skill-audit.md` |
| **REQ-16** | Routing still works after the edits, including negative branches | affected scenarios re-run in fresh contexts (instruction 4) |
| **REQ-17** | `v1.10.0` is tagged, released and published; local installs refreshed | `git ls-remote --tags`, `npm view`, shadow invariant |
| **REQ-18** | Doc map, wiki and code graph refreshed — verified by the artifact, not the exit code | `built_at_commit` vs `HEAD` (instruction 9) |
| **REQ-19** | Board and verification ledger exist and carry this run's rows | the two files |

## Carry-over ledger

Opened at stage 0; every deferral lands here the moment it is said.

| # | Item | Why deferred | Home |
|---|---|---|---|
| C-1 | Widened backfill for `instrument-console`, `workbench`, `briefing-room` | no addressable reference; backfilling would invent values with a citation attached (standing instruction 5) | board |
