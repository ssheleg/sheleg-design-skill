# Task brief — design-sync bridge + React reference kits

> Stage-0 intake artifact (task-pipeline 1.10.2). Confirmed by the operator before
> stage 1.

- **Date:** 2026-08-04
- **Task (one line):** give the SHELEG Design skill a `design-sync` bridge — a
  `DESIGN_SYNC_BRIDGE.md` companion doc covering all four reference types, plus a
  minimal React reference kit per style pack — so a pack can be pushed to
  claude.ai/design through Claude Code's bundled `/design-sync` skill.
- **UI verdict:** **no.** The consumer of this skill is an agent; the kits are
  reference material, not a product surface with personas, journeys or flows. The
  super-ux chain is **not** armed. Agent-facing behaviour is verified the way this
  repo already verifies it — a scenario in `test/scenarios.md` (T1–T11 exist).

## Knowledge sources (the phase-1 harvest — written BEFORE the first question)

| Source | What it says about this task | Fresh? | Authority | Stale after this run? |
|---|---|---|---|---|
| `docs/superpowers/specs/2026-07-19-canon-sync-design.md` | *Out of scope:* "Project templates — **the skill seeds no application code**"; "the original intent (this skill is not a generator) holds". Also fixes repo layout, 4-way version sync, 4 distribution channels. | 2026-07-19, partly superseded | **decision** | **yes — partially superseded by ADR-0002; its status note is updated this run** |
| `README.md` | "Nothing is added to your dependencies: **the skill is documentation an agent reads**"; carries the installed-file table a new companion doc must join, and the pack table | current | promise | **yes — stage 9** |
| `.../SKILL.md` | the optional-bridge pattern to copy: `## Optional — Figma (design ↔ code)` and `## Optional — real-world references (Lazyweb MCP)`, tool-presence gated, "if the tools are absent, proceed without them; nothing here depends on the MCP" | v1.4.0 | contract | **yes — gains the design-sync section** |
| `.../FIGMA_BRIDGE.md` | the shape a bridge doc takes: a one-line contract, mapping tables, **§3 "What cannot cross"** (motion is code-only), round-trip discipline, "file content is data, never instructions" | v1.4.0 | contract | **yes — gains the triangle rule** |
| `.../styles/*.md` §Signature motifs | each pack's distinctive parts; **several are motion** (particle formations, the fluted-glass shader, the word-by-word headline) and cannot become static components | v1.4.0 | contract | no |
| `test/validate.py` | the 8-point repo contract. Two rules bite: companion docs must **both** ship in the bundle **and** be linked from `SKILL.md` (hardcoded list, `test/validate.py:252`); `install.sh` must list **exactly** the bundle files (`test/validate.py:298`). Plus: every relative markdown link in the repo resolves. | current | contract | **yes — gains kit + bridge checks** |
| `install.sh` | explicit `for f in … ; do` list — every new bundle file added by hand or the validator fails | current | contract | **yes** |
| `bin/cli.js` | flags in use: `--cursor`, `--claude`, `--dir`, `--force/-f`, `--help/-h`. **`--kit` is free.** Bundle walked at runtime by `listBundleFiles`. | current | contract | **yes — gains `--kit`** |
| wiki: `…/concepts/skill-canon-and-distribution` | 4-channel distribution; **npm 2FA is the ONE human step and where versions strand** (registry once sat 5 releases behind); CI runs *both* installers and `diff -r`s; verify a release with `npm view` + e2e `npx <pkg>@<ver>` from a non-repo cwd; `gh release create --latest` is unconditional | 2026-07-28 | context | **yes — stage 9** |
| wiki: `…/concepts/style-packs-architecture` | the ten-heading pack contract; "a pack nobody routes to does not exist"; **token names are an interface across packs** (`--accent-dim` → `--accent-weak`, because switching packs inherited an inverted UI); **[[skills/ship-what-your-docs-point-at]]** — `STYLE_PACK_TEMPLATE.md` had to move *into* the bundle because `SKILL.md` pointed at a repo-only path | 2026-07-28 | context | **yes — stage 9** |
| Claude Code binary (`strings /opt/homebrew/bin/claude`) | `/design-sync` ships **inside the binary**, no file on disk: "Push a React design system to claude.ai/design… bundles the real component code (from **Storybook or a bare package**) and uploads it." Upload layout `_ds_bundle.js` + `@ds-bundle`, `styles.css`, `components/<group>/<Name>/{.html,.jsx,.d.ts,.prompt.md}` with first-line `@dsCard group="…"`, `_preview/`, `_vendor/`, `fonts/`, `_ds_sync.json`. Local state under `.design-sync/` (`config.json` pins `projectId` + `shape`, `NOTES.md`, `previews/<Name>.tsx`, `overrides/*.mjs`, self-gitignored `.cache/`). Tool order: list/read → `finalize_plan` → `write_files`/`delete_files`; `_ds_sync.json` written last, alone. Unavailable under `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. | 2026-08-04 | upstream contract | no (external) |
| `DesignSync(list_projects)`, live | **authorized and reachable from this session.** One writable design-system project: `Organic` (`0bc8f96c-cf6c-49e9-82a0-b78f687825b1`), owned, updated 2026-08-03. Not a target — the live proof goes to a new project. | 2026-08-04 | live state | no |
| git + npm | **`v1.4.0` is committed on `main` but never tagged and never published**; tags stop at `v1.3.4`, `npm view` returns `1.3.4`. | 2026-08-04 | live state | resolved by the 1.6.0 decision |
| **the working tree itself, mid-grill** | **a second agent session is live in `/Users/sshlg/DATA/sheleg-design-skill`.** Between the harvest and the brief it moved HEAD off `main`, created `feat/audit-harvest-v1.5.0`, `feat/field-notes-pack` and `feat/lecture-hall-pack`, committed `d042b41` (which **swept this brief's 71-line first draft into a commit about the field-notes pack**) and `e2b3b71` (which **minted `docs/adr/0001-style-pack-naming.md`** — the number this run had just taken), and left uncommitted edits in `README.md`, `bin/cli.js`, `test/validate.py`, `install.sh`, `SKILL.md`, `cursor/rules/sheleg-design.mdc`, `AI_PRODUCT_PATTERNS.md` and both style-pack templates, plus an in-progress `field-notes` pack. Files were being written 41 s before the check. **Five of those files are touched by five of this run's REQs.** | 2026-08-04 19:14 | live state | — |
| `docs/superpowers/retro.md` + `docs/superpowers/retro/` | **absent** — **no standing instructions bind this run**; nothing to query | — | — | seeded at stage 10 |
| `CLAUDE.md` / `CONTEXT.md` / `docs/adr/` / `docs/DOCMAP.md` / `docs/ux/` | **none found** in-repo before this run. House rules come from the user-global `~/.claude/CLAUDE.md`: production-grade bar, pipeline routing, one Obsidian vault, and post-release refresh of local installs via `npx --yes sshlg-skills@latest update`. | — | — | `docs/adr/` + `docs/DOCMAP.md` **seeded this run** |
| `graphify-out/graph.json` | **not built** (binary present at `~/.local/bin/graphify`). No reach queries this run; recommendation printed once, never a gate. | — | — | no refresh this run |

**Conflict found and resolved out loud:** the 2026-07-19 record says the skill seeds
no application code; the chosen scope is React kits. Resolved as **ADR-0002** — the
kits live in the package and are materialized only by an explicit command, so nothing
is seeded into a consuming project. The 2026-07-19 spec gets a *partially superseded*
note at stage 9.

## Documentation (the phase-1b inventory)

| Question | Answer |
|---|---|
| **Regime** | governed — seeded this run (minimal) |
| **Decision home** (exactly one) | `docs/adr/` (`ADR-NNNN`). No `docs/DECISIONS.md`, ever. |
| **Open questions** | none seeded; open items ride the carry-over ledger |
| **Doc map** | `docs/DOCMAP.md` — single homes + propagation matrix, seeded this run |
| **Gate** | `python3 test/validate.py` — the existing validator **is** the doc gate; no second script. Ratchet floor **272 checks**, measured on `main` (`5e59263`) 2026-08-04; may rise, never fall. (The wiki's 194 is a stale v1.2.0 figure — stage 9 fixes it.) |
| **Shared state** | **`ungated`** — no lease mechanism in this repo. Said out loud at 18:50, and it bit at 19:14: a second session committed over this run's artifacts and took its ADR number. Mitigation for this run is **physical, not procedural** — an isolated worktree (below). agent-sync v1.4.3 is installed on the machine but this repo does not use it; adopting it is a carry-over row, not this run's scope. |
| **Intent vs as-built** | reconciled 2026-08-04. One divergence: the "no application code" clause vs the chosen scope → ADR-0001. Second divergence: manifests claim `1.4.0`, no such release exists → folded into 1.5.0. |
| **Setup audit** (`references/setup.md`) | **not run** — the minimal doc regime was chosen instead; seven passes over ~10 docs is disproportionate here. Offer stands for a future run. |
| Doc repos / hosted doc systems | none |
| Knowledge wiki | **installed** — `~/.obsidian-wiki/config` → `sshlg-projects-vault`; queried at stage 0, synced at stage 9 |
| Code graph | **installed, not built** — no reach queries; no refresh owed |

## Scope

**In scope**

- `DESIGN_SYNC_BRIDGE.md` — a bundle companion doc, symmetric with `FIGMA_BRIDGE.md`,
  covering all four reference types and what cannot cross.
- A `## Optional — Claude Design (design-sync)` section in `SKILL.md`, gated on tool
  presence exactly like the Lazyweb section.
- Six React reference kits in `kits/<pack>/` — shared 6-atom spine with identical
  names and props across all six, plus 3–5 signature components per pack.
- `npx sheleg-design-skill --kit <pack> --out <dir>` to materialize one.
- Validator checks for every rule above, each probed against a planted defect.
- One live `/design-sync` push (workbench) as proof the format is real.
- Docs propagation, release 1.5.0, wiki sync.

**Out of scope / explicitly deferred**

- Any motion in a kit. Motion is code-only on the Figma side and is code-only here
  too; the kit is the static half of a pack. (Latest this could change: never — it is
  a contract line, not a deferral.)
- A Storybook in the repo. `/design-sync` accepts a bare package; adding Storybook
  would add a dependency tree this repo does not want.
- Pushing the other five kits live. Deferred to whenever the operator wants them —
  the capability ships either way.
- `docs/ux/` and the super-ux chain (UI verdict: no).
- Building the code graph.

## Requirements (the REQ spine — frozen)

| ID | Requirement | How it's verified | Status |
|---|---|---|---|
| REQ-001 | `DESIGN_SYNC_BRIDGE.md` ships in the bundle **and** is linked from `SKILL.md` | `test/validate.py` companion-doc list extended; probe: drop the link → FAIL | open |
| REQ-002 | `SKILL.md` gains a tool-presence-gated `## Optional — Claude Design (design-sync)` section; front-matter still passes the description canon (< 1024 chars, `Use when`, RU aliases) | `test/validate.py` green + section present; probe: bloat the front-matter → FAIL | open |
| REQ-003 | The bridge carries an explicit rule for **each of the four reference types** — style packs, Figma (the triangle), Lazyweb sweeps, live-site extraction — plus a "what cannot cross" section | `test/validate.py` checks the four required headings in `DESIGN_SYNC_BRIDGE.md`; probe: delete one heading → FAIL | open |
| REQ-004 | Six kits under `kits/<pack>/`, each carrying the **identical** 6-atom spine plus 3–5 pack signature components, per the spec's kit manifest | `test/validate.py` compares the spine component set across all six; probe: rename one atom in one kit → FAIL | open |
| REQ-005 | Each kit's `styles.css` opens with `styles/tokens/<pack>.css` **byte-identical** | `test/validate.py` byte-compare; probe: change one hex → FAIL | open |
| REQ-006 | No raw color literal (hex / `rgb(` / `hsl(` / `oklch(`) anywhere in a kit outside that token block | `test/validate.py` scan; probe: insert `#fff` in a component → FAIL | open |
| REQ-007 | `npx sheleg-design-skill --kit <pack> --out <dir>` materializes a kit that is a valid `/design-sync` **bare-package** source | CI materializes into a temp dir and `diff -r`s against `kits/<pack>/` — the same pattern the repo already uses for both installers | open |
| REQ-008 | `kits/` ships in the npm package and **not** in the skill bundle | `package.json files[]` contains `kits/`; validator asserts no kit file under the bundle dir and no kit path in `install.sh`; probe both ways | open |
| REQ-009 | Live proof: one pack (workbench) pushed to a **new** claude.ai/design design-system project; URL recorded | `DesignSync(list_files)` on the target returns the expected layout; URL in the acceptance table | open |
| REQ-010 | A behavioral scenario `T12` in `test/scenarios.md` covering design-sync discovery and the four reference-type rules | scenario run by a fresh subagent; verdict recorded at stage 10 | open |
| REQ-011 | Docs propagated: README (install table + a design-sync section + kit note), CHANGELOG 1.5.0, CONTRIBUTING (adding a pack now also means adding a kit), cursor rule, `.cursor/` mirror byte-equal | `test/validate.py` mirror check + greps | open |
| REQ-012 | Release **1.6.0**: four-way version sync, tag, GitHub release, npm publish, local installs refreshed | `test/validate.py` + `npm view sheleg-design-skill version` == `1.6.0` + `gh run` green | open |
| REQ-013 | ADR-0002 recorded, the 2026-07-19 spec annotated as partially superseded, `docs/DOCMAP.md` seeded | files exist; validator link check green | open |
| REQ-014 | This run never writes to `/Users/sshlg/DATA/sheleg-design-skill` — every change lands in the isolated worktree and reaches `main` only through one reviewed merge, after the concurrent 1.5.0 run has landed | `git -C /Users/sshlg/DATA/sheleg-design-skill status --porcelain` shows no file authored by this run before the merge; `git worktree list` shows the run's own path | open |

> **Frozen.** Adding a row is free. Removing or narrowing one needs the operator's
> explicit agreement, recorded in the carry-over ledger.

## Users & context

- **Who / for what:** a coding agent (Claude Code, Cursor) holding this skill, working
  in someone's project, that wants claude.ai/design to build screens out of the
  project's real pack rather than generic components. Secondarily: the skill's author,
  keeping six packs and six kits from drifting apart.
- **Where it runs / constraints:** zero-dependency repo; stdlib-only Python validator;
  POSIX-sh installer; Node ≥ 16 CLI. `/design-sync` is a Claude Code capability only —
  the Cursor channel must keep working with the bridge doc alone.

## Decisions locked

| # | Decision | Chosen | Rationale |
|---|---|---|---|
| D1 | Where the React kits live | `kits/<pack>/`, shipped in the npm package, **never** installed by any installer; materialized by `npx sheleg-design-skill --kit <pack> --out <dir>` | Preserves the 2026-07-19 "not a generator" intent and the README promise, while making the kits reachable from any project. Recorded as **ADR-0002**. |
| D2 | What crosses into claude.ai/design | the **static** half of a pack only — motion stays code-side, exactly as in `FIGMA_BRIDGE.md` §3 | claude.ai/design builds screens, not scroll narratives; particle formations and the fluted-glass shader have no component form |
| D3 | Kit composition | fixed 6-atom spine with **identical names and props across all six kits** + 3–5 pack signature components | Direct application of the recorded lesson that names are an interface across packs (`--accent-dim` → `--accent-weak`): switching packs must swap identity, not API |
| D4 | Gate style | tool-presence gated, like Lazyweb — never mandatory | Cursor has no `/design-sync`; a hard requirement would break a shipping channel |
| D5 | React flavor | ~~plain React + plain CSS + `className`, no build step, no dependencies~~ **REFUTED at stage 1 — see D11** | The guess was that a bare package needs no build. The converter reads the package's **built `dist/` entry and its `.d.ts` tree**, runs esbuild + ts-morph, and requires `@types/react` for prop extraction. A no-build kit falls to the documented last-resort "synth entry from `src/`", whose own text says "`.d.ts` contracts will be weaker; recommend adding a build" — and the `.d.ts` **is** what the design agent codes against. |
| D11 | React flavor, corrected | React 18+ **with a real build** producing `dist/` + `.d.ts`; `react`/`react-dom` as peer deps, `typescript` + a bundler + `@types/react` as dev deps — scoped to `kits/`, never to the skill bundle | Grounded in the converter's own requirements (stage 1). ADR-0002 already isolates `kits/` from the bundle and from every installer, so the repo's zero-dependency promise survives where it was actually made: the installed skill. |
| D6 | `styles.css` composition | `tokens/<pack>.css` verbatim, then a component layer beneath it | The pack contract already says *copy the token file verbatim, never transcribe*; byte-equality makes drift mechanically detectable |
| D7 | Color-literal ban | no hex/rgb/hsl/oklch in a kit outside the token block; geometry literals **allowed** | Packs specify exact paddings and radii numerically but never a second palette; banning geometry would ban the pack's own spec |
| D8 | Version | everything lands in **1.6.0**; `v1.4.0` is never tagged | Operator's call, revised at 19:20: 1.5.0 was claimed mid-grill by the concurrent run's `feat/audit-harvest-v1.5.0`. This run ships **after** it. Consequence recorded: the CHANGELOG keeps a 1.4.0 entry for a version that never shipped as a release. |
| D9 | Isolation | the whole run lives in a **separate git worktree** at `/Users/sshlg/DATA/sheleg-design-skill-wt/design-sync-bridge`, branch `feat/design-sync-bridge` cut from `main` (`5e59263`) | A second session is editing the primary checkout live. Isolation is physical rather than procedural because the repo is `ungated` — nothing would stop a second `git add -A` from swallowing this run's files, which already happened once (`d042b41`). |
| D10 | ADR number | this run's ADR is **0002**, not 0001 | `0001` was minted for `style-pack-naming` by the concurrent run and is already committed. ADRs are never renumbered — so the *unmerged* one moves, and stage 9 re-checks `docs/adr/` in `main` before the merge. |

## Autonomy (the sweep — stages 1→10 read this instead of asking)

| Stage | Question | Answer |
|---|---|---|
| run-wide | Model | **Opus 5** — the top tier available; already current, no per-stage overrides |
| run-wide | Escalation | decide alone while it stays inside the repository and is reversible; escalate anything outward or irreversible |
| 0 Harvest | Doc sources beyond this repo; may stage 9 write to them? | wiki **yes** (`sshlg-projects-vault`, `projects/sheleg-design-skill/`). No other repos. Graph not built → nothing owed. |
| 0 Setup audit | Entry audit? | **no** — recorded, not re-asked |
| 0 Docs regime | Decision home / gate / shared state | `docs/adr/` · `python3 test/validate.py` (floor 194) · **`ungated`** |
| 1 Docs | External contracts to ground | the `/design-sync` converter's expected **source** shape (bare package vs Storybook), how `@dsCard group` is derived, and what `.design-sync/config.json` must contain. Primary source: the converter embedded in the Claude Code binary + the `DesignSync` tool schema. React: target 18+, no new deps. |
| 2 Decompose | Platform or one module? | **one module** — a single coherent change to one repo |
| 2–3 Spec | UI verdict | **no** — no super-ux chain; scenario-tracing waiver granted, `test/scenarios.md` T12 is the behavioral check instead |
| 3 Design surface / file | Figma | **n/a** — no UI track |
| 4–5 Dev | Branch policy | **worktree `/Users/sshlg/DATA/sheleg-design-skill-wt/design-sync-bridge`**, branch `feat/design-sync-bridge` from `main` (`5e59263`). The primary checkout is **read-only for this run** — another session owns it. `main` is never written directly. Conventional commits; TaskList is the tracker. The other run's branches (`feat/audit-harvest-v1.5.0`, `feat/field-notes-pack`, `feat/lecture-hall-pack`) are **not mine and are not touched**. |
| 5 Integration | How it lands | merged into `main` before stage 7 — **after** the concurrent 1.5.0 run has landed. Before the merge: re-read `main` for `test/validate.py`, `install.sh`, `SKILL.md`, `README.md`, `bin/cli.js` and `docs/adr/`, since all six are being edited by the other run. No PR. |
| 6 Tests | Command / green | `python3 test/validate.py` (a.k.a. `npm test`); green = exit 0 with `OK (n checks)`, **n ≥ 272** (measured, not restated). Known-red baseline: none. Every new check probed against a planted defect. |
| 7 Lint | Command | the validator + `node --check bin/cli.js`; no other linter in this repo |
| 7 Deploy | Target + path | GitHub `ssheleg/sheleg-design-skill` (tag → release, `.github/workflows/release.yml`) and npm `sheleg-design-skill` |
| 7 Deploy | **Authorization** | **standing go**, specific: tag + GitHub release + `npm publish` for `1.6.0` **once `python3 test/validate.py` is green and CI is green on the pushed commit**. npm 2FA (EOTP) may still demand the operator — if it does, say so plainly rather than reporting success. The merge into `main` waits for the concurrent 1.5.0 run; if that run has not landed, stage 7 **stops and asks** rather than releasing over it. |
| 8 Post-deploy | Where health lives | `gh run list` on the repo · `npm view sheleg-design-skill version` · e2e `npx sheleg-design-skill@1.6.0` from a non-repo cwd · then `npx --yes sshlg-skills@latest update` to refresh local installs |
| 9 Docs+wiki | Targets | README, CHANGELOG, CONTRIBUTING, `cursor/rules/sheleg-design.mdc`, the `.cursor/` mirror, the 2026-07-19 spec's status note; wiki **yes**; graph **no** (not built) |
| 10 Acceptance | Sign-off / deferrals / retro | operator signs off; deferrals live in the carry-over ledger; `docs/superpowers/retro.md` **absent → seeded** at stage 10 |

## Done-criteria

1. `python3 test/validate.py` exits 0 with at least 194 checks, and every check added
   this run has been **watched failing** against a planted defect.
2. A fresh agent holding only the installed bundle can, in a project with
   `/design-sync` available, discover the bridge, materialize a kit with the documented
   command, and push it — verified by scenario T12.
3. The same agent in Cursor (no `/design-sync`) is unaffected.
4. One kit is live in claude.ai/design and its URL is recorded.
5. 1.6.0 is tagged, released, on npm, and every local install on this machine is on it.
6. Every REQ row closed with evidence, or carried with a home.
7. The primary checkout contains nothing this run authored until the single merge —
   verified, not assumed.

## Open assumptions / risks

| # | Assumption | How it's validated | If wrong |
|---|---|---|---|
| A1 | `/design-sync` accepts a bare package and the converter produces the upload layout — we hand-author neither `_ds_bundle.js` nor the card HTML | **RESOLVED at stage 1: half right.** The converter does emit all of it ("You don't write any of these — the converter does"), but it builds from the package's compiled `dist/` + `.d.ts`, not from `src/`. → D11 | — |
| A2 | `@dsCard group` is derivable from config rather than hand-written HTML | **RESOLVED at stage 1.** The group comes from the component's matched doc: a sibling `<Name>.md`/`.mdx` whose **frontmatter `category:`** sets `<group>`, discovered via `cfg.docsDir`. No HTML is ever hand-written. | — |
| A3 | Creating a design-system project is org-visible; the operator will authorize a named one at stage 6 | asked at stage 6, before the call | no live proof; REQ-009 becomes a carry-over row and the format stays unproven — said plainly |
| A4 | npm 2FA will let the release through | stage 7 | 1.5.0 strands on npm like 1.4.0 did; reported honestly, not papered over |
| A5 | Six kits × ~10 components is authorable at production quality in this run | stage 5 progress | the spine ships for all six and signature components are cut per pack **with the operator's explicit agreement**, recorded — never silently |
| A6 | The concurrent 1.5.0 run lands in `main` before this run's stage 7, and its edits to `test/validate.py`, `install.sh`, `SKILL.md`, `README.md`, `bin/cli.js` merge cleanly with this run's | re-read those six paths in `main` immediately before the merge (stage 5 integration row) | conflicts are resolved by hand at merge, against `main` as it then is — never by overwriting the other run's work. If it has not landed, stage 7 stops and asks. |
| A7 | `docs/adr/0002` is still free when this run merges | stage 9 re-checks `docs/adr/` in `main` | this run's ADR is renumbered — it is unmerged, so moving it costs nothing and the never-renumber rule is not broken |

## Stage 1 — grounded contracts (docs study)

Source: the `/design-sync` skill and its **package source shape** sub-skill, extracted
from the Claude Code binary (`/opt/homebrew/bin/claude`) — the skill ships inside the
binary, so there is no file to fetch and no published doc. Working copies:
`scratchpad/design-sync-SKILL.md`, `scratchpad/design-sync-package-shape.md`.
Everything below is quoted behaviour, not recall.

**What the converter does, so we don't.** "Per component, under
`components/<group>/<Name>/`: `<Name>.jsx`, `<Name>.d.ts`, `<Name>.prompt.md`, and
`<Name>.html` (the preview card). **You don't write any of these — the converter
does.**" It also refuses to emit the adherence config, the manifest, a version file
or a barrel — "the app's self-check regenerates those from the uploaded source."

**What it needs from us.**

| Need | Detail |
|---|---|
| A built package | "the built `dist/` entry + its `.d.ts` tree", found via `package.json` `module`/`main`/`exports['.']`. No build → a last-resort synth entry from `src/` with explicitly weaker `.d.ts`. |
| React 18+ | both the bundle and the previews render through React; "a non-React DS has nothing for the claude.ai/design agent to build with" |
| `@types/react` | required for prop extraction; without it inherited props vanish from the emitted `.d.ts` (`[DTS_REACT]`) |
| `.design-sync/config.json` | only `pkg` + `globalName` are required. Relevant keys for a pack: `shape: "package"`, `buildCmd`, `cssEntry`, `tokensGlob`, `docsDir`, `readmeHeader`, `guidelinesGlob`, `provider`, `overrides.<Name>.cardMode` |
| Grouping | frontmatter `category:` in the component's matched `<Name>.md` — that is the whole mechanism behind `@dsCard group` |
| Previews | `.design-sync/previews/<Name>.tsx`, hand-authored, 2–6 named exports each (one export = one graded card cell). Absent → the **floor card**, which is "honest, not broken" |
| Verification | `package-validate.mjs` screenshots every preview via Playwright + chromium (~200 MB if not cached); `--no-render-check` skips it and the run must say renders were never machine-checked |

**Three findings that change the design rather than just informing it.**

1. **A tokens-only sync is a supported first-class mode.** "Tokens-only DS (no
   components): emits `styles.css` only with an empty-bodied `_ds_bundle.js`." A pack
   can therefore reach claude.ai/design with **no React at all**.
2. **`readmeHeader` is a slot for the pack's contract.** A repo-committed file is
   "prepended verbatim to the generated README" that the design agent reads. This is
   where a pack's bans, its one-accent rule and "motion does not cross" belong — the
   rules travel, not just the values.
3. **`guidelinesGlob` ships the pack markdown itself** into `guidelines/`. The pack
   documents are already written; they are the highest-leverage payload in the whole
   bridge and cost nothing to send.

Taken together: the *rules* half of a pack is cheap, needs no build and no React, and
is arguably worth more to a design agent than the components; the *components* half
is the expensive part and is what D11 now prices honestly. Stage 2 chooses how far up
that ladder this run goes.
