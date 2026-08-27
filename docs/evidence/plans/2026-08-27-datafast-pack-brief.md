# Brief — the thirty-seventh pack, from datafa.st

- **Run opened:** 2026-08-27, on the request *"https://datafa.st/ проработай дизайн и
  добавь его как пример в мой бандл"* — an address and nothing else, the shape
  ADR-0001 exists to answer. Answered by pointing at the ADR before any file was
  written; the pack is named for its register (decision recorded below and in the ADR).
- **Model:** Fable 5 (the most capable available this session).
- **Baseline:** `main` == `origin/main` == `3cbda95`, tree clean; registry and tags agree
  on **v1.52.0 shipped** (`npm view sheleg-design-skill version` → 1.52.0;
  `git ls-remote --tags origin` → v1.52.0 at 3cbda95). Target version: **1.53.0**.
- **Companions:** sheleg-design (this repo; loaded), task-pipeline (running), agent-sync
  (active — lease before guarded files), graphify (`graphify-out/graph.json` present),
  wiki (`~/.obsidian-wiki/config` present). super-ux / copywriting: out of boundary —
  the deliverable is developer-facing pack documentation, not product UI or product copy.

## Source ledger

| Source | Read | What it gave |
|---|---|---|
| `CONTRIBUTING.md` | in full | the 8-step pack procedure, four gates, release homes, family-launcher coordination |
| `styles/STYLE_PACK_TEMPLATE.md` | in full | the 13-heading contract, rules 1–8 (render-not-stylesheet, ratio phrasing, Themes/Rank lines) |
| `docs/adr/0001..0003` | in full | register naming; kits ship in the package; three packs stay core |
| `docs/evidence/retro.md` — standing instructions | **in full, all 10** | concurrency, registry-truth, scenario debt, negative branches, no-reference-no-claim, gates watched failing, CI parity, reproduce delegated findings, read the artifact, pairwise batch check |
| retro Log, queried by task nouns | 2026-08-22 entry | the tokenless-reference method (`getComputedStyle`), one-pair-per-line ratios, load-bearing-ratio triage |
| `docs/evidence/backlog.md` | open rows | **29 open**; none blocks a new pack; B-115/B-131 warn: component classes need their own reference read, and count-anchored self-test plants break on every pack add — expect `test/floors.json` moves |
| `docs/evidence/verification.md` | counts | **1 row at `never`** (REQ-10 → B-004, not this run's) |
| git history | deskmate commits `4aeb01b`, `3cbda95` | the full file perimeter of the previous pack |
| code graph | `graphify-out/` present | refresh + check at stage 9 |

## Grill — resolved against sources (operator outranks; nothing here contradicts them)

- **Route:** repo change → task-pipeline; visual layer → sheleg-design pack procedure.
- **Naming:** per ADR-0001, decided by the run after measurement, alternatives weighed.
- **Branch/tracker:** protected `main` (PR + checks required — measured on the deskmate
  release); branch `feat/<pack>-pack-v1.53.0`; explicit path-list commits, never `-A`.
- **Tests:** `npm test` (4 gates) + `npm run selftest` + `tools/check_kit_vars.py` +
  render-verify per CONTRIBUTING step 8; scenario with negative branch (instr. 3/4).
- **Deploy:** tag `v1.53.0` after PR merge + fetch; the workflow is the release
  (RELEASE_ENABLED + PUBLISH_NPMJS measured active on 2026-08-27). Authorization: the
  request is "add it to my bundle" and the operator's global rules make post-release
  ops part of Definition of Done — the family launcher pin and local installs included.
- **Design surface:** text-only (a pack is prose + CSS); Figma not touched.

## Measurement method (the pack's `Origin:` will restate this)

Rendered at 1440×900, 768 and an emulated 390×844×2 in Chrome; census of
`background-color` **and** `background-image` over every element, weighted by area;
authored layer separated from vendor: the reference is Tailwind + DaisyUI, so the
authored theme is the DaisyUI oklch theme block in `0f35acd5a102ee22.css` (~382 KB,
plus 4 Next-font CSS files) **verified against the render** — the declared teal accent
`--a` (#00d7c0) paints nothing on the page and is recorded as a dead token, not the
brand. Buttons, inputs, cards, nav, focus, hover and press read from computed styles
and the stylesheet's own `.btn-simple` rules; the demo dashboard measured separately at
`https://datafa.st/demo` (it is an iframe of the live product). Both themes measured —
`data-theme` light and dark are full twins.

## REQ table (frozen — adding is free, removing needs the operator)

| REQ | The requirement | Verified by |
|---|---|---|
| REQ-1 | A 37th style pack measured off `https://datafa.st/`, named for its register per ADR-0001, with the address and method in `Origin:` | pack file header; ADR-0001 entry; `tools/audit_packs.py` |
| REQ-2 | All thirteen headings filled (`widened`), `Themes:` and `Rank:` derived from the token layer | `python3 test/validate.py` |
| REQ-3 | `styles/tokens/<name>.css` in the same change; values measured or marked as pack decisions at the declaration; parseable by the palette gate (hex/rgb, no bare oklch) | `python3 test/validate_palette.py` |
| REQ-4 | The reference's own failures recorded with numbers, never applied: CTA label 3.42:1 on #e16540; statuses 1.66–3.08:1 on white; 53 keyframes vs 2 reduced-motion rules | pack `## Gotchas`, ratios recomputed by the gate |
| REQ-5 | React kit under `kits/<name>/` — six-name spine + signature components, token CSS byte-identical, `.design-sync/` pair | `validate.py` kit parity; `tools/check_kit_vars.py` |
| REQ-6 | Routing: SKILL.md pack list + STYLE_PACK_INDEX row + `bin/cli.js`; mirrors byte-identical (`.cursor/`, `plugins/`) | `validate.py` |
| REQ-7 | Pairwise check against the closest existing packs, forks written from both sides where confusable (instr. 10) | `validate_fork_reciprocity()`; the forks named in both packs |
| REQ-8 | Kit rendered at 1440/768/390 and computed values compared to the pack's claims (CONTRIBUTING step 8) | render log in the acceptance doc; defects fixed pre-tag |
| REQ-9 | A routing scenario with its negative branch; run with fresh subagents or shipped as stated debt with the reason | `test/scenarios.md` result line |
| REQ-10 | v1.53.0 released: five version homes, CHANGELOG, PR + checks, tag, GitHub release, npm; verified from the registry and the tarball | `npm view`; tarball read; release run read |
| REQ-11 | Family launcher updated (skills.json pin + submodule pointer + README row + launcher release) and local installs refreshed, shadow check empty | `npx sshlg-skills list`; the shadow check's empty output |
| REQ-12 | Close-out trio: module docs, wiki page, graph refreshed — each verified by the artifact changing | file diffs; `built_at_commit` == HEAD |

Carry-over ledger: opened empty; anything deferred lands here with a board id at close.
