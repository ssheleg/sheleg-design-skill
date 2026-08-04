# Task brief — `field-notes` style pack (graphify.com)

- **Date:** 2026-08-04
- **Task (one line):** tear graphify.com down to its constituents from live
  computed styles and ship the result as the skill's **seventh style pack**,
  `field-notes` — spec + token layer + registration on every surface the
  validator and the humans read + test scenario + release.
- **UI verdict:** **no.** The deliverable is documentation and a token layer
  inside an agent-skill bundle; no user-facing surface is built or changed. The
  stage-3 super-ux track is therefore **not** armed. (`super-ux` is installed —
  this is a scope decision, not a missing tool.)

## Knowledge sources (the phase-1 harvest — written BEFORE the first question)

| Source | What it says about this task | Fresh? | Authority | Stale after this run? |
|---|---|---|---|---|
| `test/validate.py` | the pack contract, mechanically: **nine required headings**, a `styles/tokens/<pack>.css` beside every pack, routing from the SKILL.md table, the pack named in `bin/cli.js` help, the `.cursor/` mirror byte-identical in **both** directions, four-way version sync | current | contract | **yes — check count rises** |
| `install.sh` | explicit file list; a new pack that is not listed ships to nobody who uses the POSIX installer | current | contract | **yes** |
| `bin/cli.js` | help text says "six style packs" and names each one; the validator asserts the pack stem appears here | current | contract | **yes** |
| `styles/orchard.md` + `tokens/orchard.css` | the shape to match: values read off live computed styles, palette table carrying measured contrast ratios, Gotchas that fix the reference rather than flatter it | 2026-08-03 | exemplar | no |
| `styles/atrium.md` | the neighbouring warm register; needs explicit disambiguation from the new pack | 2026-08-03 | exemplar | no |
| `styles/instrument-console.md` | the incumbent **technical** register (dark, cool, Geist) — the pack `field-notes` is most likely to be confused with | current | exemplar | no |
| `styles/workbench.md` | the incumbent **product-UI** register; `field-notes` ships an app layer too, so the Register section must route between them | current | exemplar | no |
| `SKILL.md` | pack table is the router; "never invent token values ad hoc"; craft bar; AI product surfaces route to `AI_PRODUCT_PATTERNS.md` | current | contract | **yes — new row** |
| `AI_PRODUCT_PATTERNS.md` | the **honest state** doctrine — never a confidence number with nothing behind it | current | doctrine | **yes — provenance section** |
| wiki: `projects/sheleg-design-skill/concepts/style-packs-architecture.md` | token layers not tables; **token names are an interface across packs** (`--accent-dim` → `--accent-weak` incident); the pack wins over the methodology on ease | 2026-07-28 | context | **yes — update at stage 9** |
| `docs/superpowers/specs/2026-07-19-canon-sync-design.md` | repo layout, four-way version sync, one skill/one command | partly superseded | decision | no |
| `CHANGELOG.md` | 1.4.0 is the top entry; the release note voice is prose-first, not bullet-first | 2026-08-03 | convention | **yes — 1.5.0** |
| `~/.claude/CLAUDE.md` (global) | production-grade bar; ops steps are mine to run; after any release, refresh local installs via `npx --yes sshlg-skills@latest update`; never a bare `npx skills update <name>` for a plugin-installed skill | current | convention | no |
| `docs/superpowers/retro.md` | **absent** — no standing instructions bind this run | — | — | **yes — seeded at stage 10** |
| `docs/adr/`, `CONTEXT.md`, `docs/DOCMAP.md`, `docs/ux/`, `CLAUDE.md` (project) | **none found** — recorded as an empty row, not as silence | — | — | no |
| `graphify-out/graph.json` | **not built.** The `graphify` CLI resolves at `~/.local/bin/graphify`; no graph exists for this repo | — | — | optional at stage 9 |

Precedence for this run: the **code and the validator decide** — every claim the
pack makes about the reference is checked against a live computed style, and
every claim the repo makes about itself is checked against `test/validate.py`.
The operator outranks both, out loud.

## Documentation (the phase-1b inventory)

| Question | Answer |
|---|---|
| **Regime** | lightweight — the repo's own docs *are* the product, and `test/validate.py` already enforces cross-file consistency. No DOCMAP/register seeded this run (operator declined the entry audit, 2026-08-04; recorded, never re-asked). |
| **Decision home** | `docs/superpowers/specs/` — design docs and briefs. No `docs/adr/`; nothing this run decides is hard to reverse enough to earn one. |
| **Doc map** | absent by decision; the propagation matrix for this change type is written into the REQ table instead (every surface that must move is its own row). |
| **Gate** | `python3 test/validate.py` — the repo's real documentation gate. It already fails on an unrouted pack, a missing token layer, a drifted mirror, a version skew. Ratchet floor: **272 checks** (the count at `5e59263`); this run must raise it. |
| **Shared state** | `ungated` — single operator, single worktree, no lease mechanism. Said out loud. |
| **Intent vs as-built** | reconciled: the 2026-07-19 canon spec's "no templates" decision is marked superseded in its own header, and the shipped `STYLE_PACK_TEMPLATE.md` matches. No unresolved divergence found. |

- **Doc repos / hosted doc systems:** none.
- **Knowledge wiki:** installed — vault `/Users/sshlg/DATA/obsidian-memory-vault/sshlg-projects-vault`, project folder `projects/sheleg-design-skill/`.
- **Retro, in force:** none — the file does not exist. Seeded at stage 10.
- **Retro archive:** none.
- **Code graph:** installed, not built. Offered as a recommendation; not a gate.

## Scope

**In scope**

- Full teardown of `https://graphify.com/` from **live computed styles** — the
  92 declared custom properties, the type scale, spacing, radii, shadows, the
  component vocabulary, the motion keyframes, and the page's content
  architecture — recorded as the stage-3 design document.
- A seventh style pack, `field-notes`, authored against the nine-heading
  contract, plus `styles/tokens/field-notes.css` carrying a light `:root` and a
  `.dark` twin.
- The pack's **app layer** (sidebar, popover, chart series, destructive) ships,
  with an explicit Register-section routing rule against `workbench`.
- A new section in `AI_PRODUCT_PATTERNS.md` promoting the reference's
  provenance vocabulary (`--verify` / `--witness`, `EXTRACTED · INFERRED ·
  AMBIGUOUS`) into a pack-agnostic pattern under the existing *honest state*
  doctrine.
- Registration on every surface: `SKILL.md`, `README.md`, `bin/cli.js`,
  `install.sh`, `cursor/rules/sheleg-design.mdc`, the `.cursor/` mirror.
- A behavioural test scenario (T13) in `test/scenarios.md`.
- Release: `v1.5.0`, four-way version sync, merge to `main`, tag, npm publish,
  local installs refreshed.

**Out of scope / explicitly deferred**

- The entry documentation audit (`DOCMAP.md`, decision register, open-questions
  file) — operator declined 2026-08-04. Latest sensible moment to revisit: the
  next run that adds a *class* of artifact rather than an instance.
- Building the code graph for this repo — recommendation only.
- Any change to the cinematic motion core (`SHELEG_DESIGN.md`): the new pack is
  standalone, like `workbench` and `briefing-room`.

## Requirements (the REQ spine)

| ID | Requirement | How it's verified | Status |
|---|---|---|---|
| REQ-001 | `styles/field-notes.md` exists and carries all nine contract headings plus `## Motion flavor` | `python3 test/validate.py` (per-pack section loop) | open |
| REQ-002 | `styles/tokens/field-notes.css` ships a light `:root` **and** a `.dark` twin, every value traceable to a live computed style | validator's token-layer check + every value in the CSS present in the stage-3 extraction record | open |
| REQ-003 | The full teardown is recorded: tokens, type scale, spacing, radii, shadows, components, motion, content architecture | `docs/superpowers/specs/2026-08-04-field-notes-pack-design.md` exists and each pack claim cites a measured value | open |
| REQ-004 | Registered on every validator-enforced surface: SKILL.md pack table, `bin/cli.js` help, `install.sh` file list, `.cursor/` mirror byte-identical both ways | `python3 test/validate.py` → `OK (n)` with **n > 272** | open |
| REQ-005 | Registered on the human-facing surfaces: README pack table row, README pack count, `cursor/rules/sheleg-design.mdc` | `grep -c 'field-notes' README.md cursor/rules/sheleg-design.mdc` ≥ 1 each; no "six style packs" string survives anywhere | open |
| REQ-006 | `AI_PRODUCT_PATTERNS.md` carries the provenance-display pattern, pack-agnostic, under *honest state* | section present and linked from SKILL.md's AI paragraph; T13 exercises it | open |
| REQ-007 | Every colour pair the pack proposes is **measured**, and every AA failure in the reference is named in Gotchas with the in-palette fix | contrast ratios computed in the design doc; each Gotchas bullet cites a ratio | open |
| REQ-008 | `CHANGELOG.md` has a `## [1.5.0]` entry and the four manifests agree | validator's version-sync check | open |
| REQ-009 | `test/scenarios.md` gains **T13** covering pack self-selection for the dev-tool register *and* disambiguation from `instrument-console` | scenario present; run against a subagent with a fresh context, expected verdict recorded | open |
| REQ-010 | The full local suite is green: validator, `node --check bin/cli.js`, `sh -n install.sh`, npx-bundle diff, POSIX-bundle diff | all five commands exit 0; the validator probed **both ways** (planted defect fails it) | open |
| REQ-011 | Released: branch merged to `main`, pushed, tagged `v1.5.0`, GitHub Actions green, npm shows `1.5.0` | `gh run list` success + `npm view sheleg-design-skill version` = `1.5.0` | open |
| REQ-012 | Local installs refreshed and no plain copy shadows the plugin | `npx --yes sshlg-skills@latest update`; the shadow-check loop from the global rules prints nothing | open |
| REQ-013 | Wiki updated (`concepts/style-packs-architecture.md` names the seventh pack and what it taught) and `docs/superpowers/retro.md` seeded | both files contain `field-notes`; retro carries this run's stamp with its commit | open |

Frozen as of 2026-08-04. Adding rows is free; removing one needs the operator's
explicit agreement, recorded in the carry-over ledger.

## Users & context

The consumer is an **agent** reading the pack in a fresh context, plus the
human who asked it for "a dev-tool landing that isn't dark". The pack's job is
to make that agent quote measured values instead of inventing plausible ones —
the failure that created the `styles/` layer in the first place (0.4.0).

## Decisions locked

| # | Decision | Rationale |
|---|---|---|
| D1 | The pack is named **`field-notes`** | An object-noun, like `workbench`/`atrium`/`orchard`. It names what the reference actually is: an engineer's notes published as a site — warm paper, mono annotation, crop marks, and a colour system for how well a claim is evidenced. |
| D2 | It ships a **`.dark` twin** | The reference declares a complete dark token set with real values; dropping it would discard extracted data. Precedent: `workbench`. |
| D3 | It is **standalone** — no cinematic motion required | The reference carries no GSAP, Framer, Three or Lenis; its motion is CSS keyframes plus `prefers-reduced-motion`. Same posture as `workbench` and `briefing-room`. |
| D4 | The **app layer ships**, with an explicit routing rule | `--sidebar-*`, `--chart-1…5`, `--popover`, `--destructive` are real extracted values. Register section states: `workbench` stays the default for neutral product UI; `field-notes` is for a product whose console must read as the same warm paper as its site. |
| D5 | Provenance is **promoted to `AI_PRODUCT_PATTERNS.md`** | It is the reference's one genuinely transferable invention and it is a direct extension of the existing *honest state* rule. Kept out of `SHELEG_DESIGN.md`, which is about motion architecture. |
| D6 | Release lands via **feature branch → `main` → tag → npm** | Operator authorization, 2026-08-04, specific: branch `feat/field-notes-pack`, tag `v1.5.0`, npm publish through the existing `release.yml`, then local installs refreshed. |
| D7 | **No entry documentation audit** this run | Operator declined, 2026-08-04. Recorded once; never re-asked. |

## Autonomy (the sweep — stages 1→10 read this instead of asking)

| Stage | Resolved |
|---|---|
| run-wide | Model: **Opus 5** (top tier available), confirmed at preflight. Decide alone while a change is inside this repo and reversible; escalate anything outward. |
| 0 Harvest | Sources: this repo + the obsidian projects vault. No other repos, no hosted doc systems. Stage 9 **may** write the wiki. |
| 1 Docs | External contracts: the two type families (Geist, Bricolage Grotesque) and any CSS feature the token layer leans on. Verified via context7 / vendor docs; no private SDKs. |
| 2 Decompose | One module, not a platform. No module map. |
| 2–3 Spec | UI verdict **no** → super-ux track not armed; no scenario tracing waiver needed. |
| 3 Design surface | N/A — nothing is designed in Figma this run. |
| 4–5 Dev | Base branch `main`; work happens on `feat/field-notes-pack`; conventional commits; tracker = this TaskList. |
| 5 Integration | Branch merges to `main` after the stage-6 gate is green. No PR approver required. |
| 6 Tests | `python3 test/validate.py` (green = `OK (n)`, n > 272), `node --check bin/cli.js`, `sh -n install.sh`, plus the two bundle diffs. Known-red baseline: none. |
| 7 Lint+deploy | No separate linter beyond the validator. Deploy = push `main` + tag `v1.5.0`; `release.yml` publishes to npm when `PUBLISH_NPMJS` is armed. **Authorized** per D6. |
| 8 Post-deploy | GitHub Actions run list for both workflows; `npm view sheleg-design-skill version`. |
| 9 Docs+wiki | README, SKILL.md, cursor rule, CHANGELOG in the same change. Wiki sync **yes**. Code-graph refresh **optional** (none built). |
| 10 Acceptance | Operator signs off. Deferred REQs go to the carry-over ledger. `docs/superpowers/retro.md` seeded by this run. |

## Done-criteria

Every REQ row `verified` with evidence from a check that has been seen failing
at least once, the carry-over ledger carrying no `unresolved` row, the working
tree clean and pushed, and npm serving `1.5.0`.

## Open assumptions / risks

- **A1 — the reference may change under us.** Every value is read from a live
  page on 2026-08-04. The design doc records the capture date; the pack, like
  `orchard` and `atrium`, is a snapshot and says so.
- **A2 — font availability.** Bricolage Grotesque and Geist are both open
  licences, but the pack must name substitutes with the same voice (the
  `orchard` precedent: substituting the display face changes the pack more than
  substituting a colour). Verified at stage 1.
- **R1 — register collision with `instrument-console`.** Both serve technical
  products. Mitigated by an explicit disambiguation paragraph in Register and by
  T13, which tests exactly this fork.
- **R2 — the reference is a shadcn/Tailwind base.** Some declared tokens may be
  framework defaults nobody styled rather than deliberate choices. Mitigation:
  values that are never actually consumed on the page are recorded in the design
  doc but not promoted into the pack.
