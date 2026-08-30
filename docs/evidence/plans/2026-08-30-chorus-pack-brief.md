# Brief — the thirty-ninth pack, from crowdreply.io

- **Run opened:** 2026-08-30, on the request *"https://crowdreply.io/ Разбери вот этот
  лендинг и добавь его в наш брендпак"* — an address and an instruction to add it to
  the collection. Answered per ADR-0001 before any file was written; the pack is named
  for its register (`chorus`), with `switchboard`, `soapbox`, `quorum` and `earshot`
  weighed and rejected — the record goes into the ADR with this change.
- **Model:** Opus 5 (1M). **Baseline:** `main` == `origin/main` == `7d20da9`, tree
  clean; `git tag --sort=v:refname`, `git ls-remote --tags origin | sort -V` and
  `npm view sheleg-design-skill version` all agree on **v1.54.1 shipped**. Target:
  **1.55.0**.
- **Companions:** sheleg-design (the doctrine it extends), task-pipeline (this run
  order), agent-sync (lease `SG-CHORUS` taken before any guarded file), evidence-docs
  (every ratio below computed, none restated), chrome-devtools MCP (the render).
  The resolutions of the `surveyor` run of 2026-08-29 hold: branch → PR → checks →
  tag; release durably authorized as Definition of Done; text-only design surface.

## Standing instructions — read in full this session

All ten. Instruction 1 fired: `git reflog -8` shows only this session's own
`pull --ff-only` and checkout; `git branch -vv` shows thirteen stale `feat/*`
branches, all at their own merged tips, none moving; no foreign HEAD move.
Instruction 2 fired: the version was read from the registry and both tag lists,
never from a manifest — v1.54.1 is shipped on all three, so 1.55.0 is free.

## Source ledger

Board **35 open** (B-135 newest), verification **1 row at `never`** (REQ-10 →
B-004), the ten standing instructions, CONTRIBUTING's procedure, the
thirteen-heading contract in `test/validate.py`, ADR-0001..0003, and the
`surveyor` run's own retro entry — the blind defect-reads run BEFORE the tag.

## Measurement method (the pack's `Origin:` restates this)

Rendered at 1440×900, an emulated 768×1024×2 and an emulated 390×844×2 through
CDP on 2026-08-30. Census of `background-color` and `background-image` over every
element, weighted by painted area, on an 11,750px page carrying 2,439 elements.
Authored layer separated from vendor: the site is **Framer**, and the authored
system is its 52 `--token-<uuid>` custom properties plus the per-element Framer
classes — 274,355 bytes of CSS across 11 stylesheets, 1,106 rules. What the token
dump claims and what actually paints were checked against each other: of the 52
declared tokens, 15 are referenced once and never reach a large surface, so the
census — not the dump — decided every value below.

Motion was read the same way: the corpus holds **exactly one `@keyframes`**
(`__framer-loading-spin`), **two** `transition` declarations with a duration
(`color .5s cubic-bezier(.44,0,.56,1)`, `opacity .4s ease-out`) and **zero**
`prefers-reduced-motion` rules. The real choreography is JavaScript: 383 elements
carry an inline `transform`, 1,057 an inline `opacity`, and 43 compute a
`will-change` other than `auto`. That distinction is load-bearing and is recorded
in the pack — a reduced-motion branch in CSS cannot stop a transform a script sets.

Ratios were computed by importing this repository's own palette gate
(`test/validate_palette.py` → `parse_color()` + `contrast()`), never by hand.

## REQ table (frozen)

| REQ | The requirement | Verified by |
|---|---|---|
| REQ-1 | A 39th pack from `https://crowdreply.io/`, register-named per ADR-0001, method in `Origin:` | pack header; ADR entry; `tools/audit_packs.py` |
| REQ-2 | Thirteen headings, `Themes:`/`Rank:` derived | `test/validate.py` |
| REQ-3 | Token layer in the same change, provenance marked per value, gate-parseable | `test/validate_palette.py` |
| REQ-4 | The reference's failures recorded with numbers and never applied: white on `#f96f4b` 2.84:1 at 14px/500 (the primary CTA); coral as a word 2.72:1 on the field; the `#ff5d30` link 2.94:1; muted `#8a8692` 3.41:1 at 14px/400; a card separated from the field by **1.04:1** with no border and no shadow; 0 reduced-motion rules against 383 script-set transforms | pack Gotchas, recomputed by the gate |
| REQ-5 | Kit: the shared spine + signature components, token CSS byte-identical, `.design-sync/` pair | `validate.py`, `tools/check_kit_vars.py` |
| REQ-6 | Routing: SKILL/index/cli/install/commands/mdc/README + `.cursor/` mirrors; every counted claim moves 38→39 | `validate.py` |
| REQ-7 | Reciprocal forks against the confusable neighbours (`surveyor`, `deskmate`) | `validate_fork_reciprocity()` |
| REQ-8 | Kit rendered at 1440/768/390, computed values read back against the pack's claims, pre-tag | render log in acceptance |
| REQ-9 | Scenario T37 with its negative branch, RUN blind before the tag | `test/scenarios.md` result line |
| REQ-10 | v1.55.0 released: five version homes, PR + checks, tag, GitHub release, npm; verified from registry + tarball | `npm view`, tarball read |
| REQ-11 | Launcher pinned + local installs refreshed, shadow check empty | `npx sshlg-skills list`, the checks |
| REQ-12 | Docs/wiki/graph trio, artifacts re-read | diffs; `built_at_commit` == HEAD |

Carry-over ledger: opened empty.
