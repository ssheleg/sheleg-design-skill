# Task brief — audit harvest into the skill (v1.5.0)

> Stage-0 intake artifact (task-pipeline). The grill fills this in; the operator
> confirmed it before stage 1.

- **Date:** 2026-08-04
- **Branch:** `feat/audit-harvest-v1.5.0`
- **Task (one line):** fold the results of a 41-skill audit of the machine's
  installed UX/UI-design skills into SHELEG Design — a motion doctrine with
  numeric decision tables, three calibration dials, two runnable token
  validators, a pack contract widened by four sections and backfilled across
  every pack, and two new packs — shipped as 1.5.0 on every channel.
- **UI verdict:** **no.** The deliverable is documentation, token layers and
  test scripts inside an agent-skill bundle. No user-facing surface is built or
  changed, so the stage-3 `super-ux` track is **not** armed. (`super-ux` is
  installed — a scope decision, not a missing tool.)
- **Figma:** not armed. Nothing visual is authored in this run; the existing
  `FIGMA_BRIDGE.md` is untouched.

## Knowledge sources (phase-1 harvest — written BEFORE the first question)

| Source | What it says about this task | Fresh? | Authority | Stale after this run? |
|---|---|---|---|---|
| `test/validate.py` | the repo contract, mechanically. **272 checks, green at `5e59263`** — the ratchet floor this run must raise. Nine required pack headings; a token layer beside every pack; routing from the SKILL.md table; the pack named in `bin/cli.js`; the `.cursor/` mirror byte-identical both ways; four-way version sync | current | **contract** | **yes — headings 9→13, check count rises** |
| `templates/style-pack-template.md` | the skeleton every pack copies; byte-identical to the bundled `styles/STYLE_PACK_TEMPLATE.md` (validator asserts it) | current | contract | **yes — four new headings** |
| `install.sh` | explicit file list; a new companion doc that is not listed ships to nobody using the POSIX installer | current | contract | **yes** |
| `bin/cli.js` | help text names each pack; the validator asserts the pack stem appears here | current | contract | **yes — two new packs** |
| `SKILL.md` | pack table is the router; "never invent token values ad hoc"; craft bar; optional-bridge pattern (`## Optional — …`, tool-presence gated) is the shape a new companion doc joins | current (1.4.0) | contract | **yes — doctrine sections + two rows** |
| `package.json` | description says **"three locked style packs"** while six ship | **stale** | — | **yes — fix at stage 9** |
| pack `Origin:` lines | `atrium`→functionhealth.com, `editorial-luxury`→prowl.chat, `orchard`→gutgutgoose.com are addressable. `briefing-room`, `instrument-console`, `workbench` name a product, **not an address** — provenance is not re-checkable | current | **gap found** | **yes — origins become addressable** |
| `docs/superpowers/specs/2026-08-04-field-notes-pack-brief.md` + carry-over | a **committed but unbuilt** seventh pack (`field-notes`, graphify.com). Harvest and scope already written; the pack does not exist in `styles/` | in flight | decision | **yes — this run finishes it** |
| `docs/superpowers/specs/2026-08-04-design-sync-bridge-brief.md` | a second unbuilt brief; not in this run's scope — recorded so it is not mistaken for done | in flight | decision | no |
| `docs/superpowers/specs/2026-07-19-canon-sync-design.md` | **"the skill seeds no application code — this skill is not a generator"** | partly superseded | **decision** | no — see conflict below |
| wiki `concepts/style-packs-architecture.md` | token layers not tables; **token names are an interface across packs**; a pack nobody routes to does not exist | 2026-07-28 | context | **yes — stage 9** |
| wiki `concepts/skill-canon-and-distribution.md` | four-channel distribution; **npm 2FA is the one human step and where versions strand** | 2026-07-28 | context | **yes — stage 9** |
| `~/.claude/CLAUDE.md` (global) | production-grade bar; ops steps are mine to run; after any release refresh local installs via `npx --yes sshlg-skills@latest update` | current | convention | no |
| `docs/superpowers/retro.md` | **absent** — no standing instructions bind this run | — | — | **yes — seeded at stage 10** |
| `CLAUDE.md`, `CONTEXT.md`, `docs/adr/`, `docs/ux/`, `docs/DOCMAP.md` | **none found** — recorded as an empty row, not as silence | — | — | no |
| `graphify-out/graph.json` | **not built**; already carry-over row 2 from the previous run | — | — | optional at stage 9 |

Precedence for *what is*: code > host docs > wiki > memory. For *what should be*:
the decision register outranks the code. The operator outranks every document —
**but only out loud**.

### Conflict found in the harvest, and its resolution

The canon spec records **"the skill seeds no application code"**. This run adds
two runnable Python validators and a comparison harness.

**Resolved without an override:** both validators live in `test/`, which is not
in the `files` array of `package.json` and not in `install.sh` — they are the
repo's own gate, never shipped to a consumer. The `?variant=` comparison harness
is an *instruction* in the doctrine doc telling an agent how to mount packs in
the consumer's own app; the skill ships no component. The decision holds
unmodified. Logged so a later run does not re-litigate it.

## Documentation (phase-1b inventory)

| Question | Answer |
|---|---|
| **Regime** | lightweight — the repo's docs *are* the product, and `test/validate.py` already enforces cross-file consistency. No DOCMAP seeded (operator declined the entry audit 2026-08-04; recorded, never re-asked). |
| **Decision home** | `docs/superpowers/specs/`. No `docs/adr/`; the contract widening is reversible by editing one tuple, so it does not earn one. |
| **Gate** | `python3 test/validate.py && node --check bin/cli.js`. **Ratchet floor: 272 checks.** This run must raise it and may never lower it. |
| **Shared state** | `ungated` — single operator, single worktree, no lease. Said out loud. |
| **Doc repos / hosted systems** | none. |
| **Knowledge wiki** | installed — `projects/sheleg-design-skill/`. |
| **Retro in force** | none; the file does not exist. Seeded at stage 10. |
| **Code graph** | installed, not built. Carry-over row 2, still not a gate. |

## Operator decisions (grill, 2026-08-04)

| # | Question | Answer |
|---|---|---|
| 1 | Seventh pack: finish `field-notes` or start `industrial-brutalist`? | **Both — `field-notes` first**, `industrial-brutalist` as the eighth |
| 2 | Widening the pack contract breaks all six packs — how are the new sections filled? | **Re-read the live references**; values stay measured, never inferred |
| 3 | Three packs have no addressable origin | **Operator supplies the URLs**; the `Origin:` line becomes addressable in the same change |
| 4 | Where does the run end? | **Release 1.5.0** on every channel + local install refresh + wiki |
| 5 | Where does the work happen? | **Branch** `feat/audit-harvest-v1.5.0`, merged after green CI |

## Scope

**In scope**

1. Motion doctrine with numeric decision tables and a technical ban list.
2. Three calibration dials with inference from the brief.
3. Pack contract widened 9 → 13 headings; every pack backfilled from its live
   reference.
4. Every pack's `Origin:` made addressable.
5. A slop lint over the repo's own token layers and doc examples.
6. A palette validator computing CVD separation, not eyeballing it.
7. Seventh pack `field-notes`; eighth pack `industrial-brutalist`.
8. Release 1.5.0 across all four channels + local refresh + wiki.

**Out of scope**

- The `design-sync` bridge (its own unbuilt brief; untouched here).
- Building the code graph (carry-over row 2).
- Any user-facing surface; any generated application code.

## REQ table

The request as an addressable list. Frozen: adding is free, removing needs the
operator's agreement. Every row names how it is verified.

| REQ | Requirement | Module | Verified by |
|---|---|---|---|
| R1 | Motion doctrine doc exists, ships in the bundle, is linked from `SKILL.md` | M1 | validator: bundle+link checks |
| R2 | Frequency→decision table (100+/day ⇒ never animate) present with all four bands | M1 | slop lint asserts the four rows |
| R3 | Easing decision tree + `ease-in` ban + three named curves as CSS custom properties | M1 | palette/lint check on curve syntax |
| R4 | Duration table, five element classes, 300 ms UI ceiling stated | M1 | lint asserts rows |
| R5 | Forbidden-motion ban list: scroll listener, `useState` for continuous values, rAF touching state, non-GPU properties | M1 | lint greps the repo for each banned form |
| R6 | GSAP rules: `ease:'none'` under scrub, `useGSAP` over `useEffect`, `markers` dev-only | M1 | lint asserts presence |
| R7 | Four Figma-motion rules recorded (no fabricated motion; validate one before batching; factor repeats; Tailwind translate vs Motion transform) | M1 | lint asserts presence |
| R8 | Anti-drift rule recorded as a named contract | M1 | lint asserts presence |
| R9 | Three dials defined with ranges, baseline and inference table | M2 | validator: SKILL.md section check |
| R10 | Three AI-default palettes recorded as a negative test | M3 | palette validator FAILs a planted default |
| R11 | Slop lint script exists and runs in `npm test` | M3 | CI green; planted defect fails it |
| R12 | Palette validator computes OKLab ΔE + CVD separation + contrast per pack | M4 | planted low-ΔE palette FAILs |
| R13 | Pack contract widened to 13 headings in template and validator | M0 | validator check count rises |
| R14 | `Signature` section required and non-empty in every pack | M0/M5 | validator |
| R15 | `Components`, `Hero`, `Responsive` sections backfilled in all six packs from live re-reads | M5 | per-pack evidence line in the pack |
| R16 | Every pack `Origin:` is an addressable URL | M5 | validator: `Origin:` matches a URL form |
| R17 | Seventh pack `field-notes` shipped and routed | M6 | validator: pack contract + routing |
| R18 | Eighth pack `industrial-brutalist` shipped and routed | M7 | same |
| R19 | Depth model (0–5) recorded; `dataviz` parameter handoff table present | M8 | validator: section check |
| R20 | `?variant=` pack-comparison procedure recorded | M8 | validator: section check |
| R21 | 1.5.0 synchronised four ways; CHANGELOG entry; `install.sh` lists every new file; `.cursor/` mirror identical | M9 | validator |
| R22 | Released: tag, GitHub release, npm, local installs refreshed, wiki updated | M9 | `npm view`, e2e `npx` from a clean cwd |
| R23 | `package.json` description corrected from "three" packs | M9 | validator or review |

## Module map (stage-2 decomposition)

The brief describes a platform, not a change, so it is cut into modules. Every
REQ sits in exactly one. **M0 is the walking skeleton** — it moves the whole
chain (template → validator → one pack → green) on the thinnest possible slice
before anything else is built.

| Module | Contents | REQs | Depends on |
|---|---|---|---|
| **M0** | walking skeleton: contract widened, one pack backfilled, validator raised, green | R13, R14 | — |
| **M1** | `MOTION_DOCTRINE.md` companion doc | R1–R8 | M0 |
| **M2** | dials in `SKILL.md` | R9 | M0 |
| **M3** | slop lint | R10, R11 | M1 |
| **M4** | palette validator | R12 | M0 |
| **M5** | backfill of the remaining five packs + addressable origins | R15, R16 | M0, **operator URLs** |
| **M6** | `field-notes` pack | R17 | M0 |
| **M7** | `industrial-brutalist` pack | R18 | M0 |
| **M8** | depth model, `dataviz` handoff, variant harness | R19, R20 | M1 |
| **M9** | release 1.5.0 | R21–R23 | all |

## Carry-over ledger

Append-only. Any stage may add a row; nobody edits or deletes one.

| # | Stage | What | Why it isn't done | REQ | Where it lives now |
|---|---|---|---|---|---|
| 1 | 0 Grill | Code graph for this repo (`/graphify .`) | inherited from the previous run; recommendation only, never a gate | — | backlog |
| 2 | 0 Grill | `design-sync` bridge brief | separate unbuilt brief; deliberately out of this run's scope | — | backlog |
| 3 | 0 Grill | Entry documentation audit (`docs/DOCMAP.md`, decision register) | operator declined 2026-08-04; recorded, never re-asked | — | dropped (operator agreement) |
| 4 | 6 Build | **M6 `field-notes` pack** | a concurrent run owns `feat/field-notes-pack` and had already authored the pack, its token layer, the manifests and the CHANGELOG entry. Building it here would collide | R17 | reassigned to that run |
| 5 | 6 Build | **M5 backfill of all six packs** | three record a product name where an address belongs and cannot be re-read; the operator has no URLs (2026-08-04). Filling the four new sections from the token layer instead would be inventing values with a citation attached. Backfilling only the three addressable packs was rejected at the grill — it ships two classes of pack | R15, R16 | **dropped (operator agreement)** — contract closed by the all-or-nothing gate instead |
| 6 | 6 Build | **M7 `industrial-brutalist` pack** | no addressable production origin; the operator has none (2026-08-04). The register was described from a third-party skill whose palette is synthesised, not measured — shipping it would be the invented-values failure the pack layer exists to prevent | R18 | **dropped (operator agreement)** |
| 7 | 9 Release | **Version number, tag, GitHub release, npm publish** | a concurrent run holds 1.5.0. This branch ships its CHANGELOG under `## Unreleased` and takes a number when it merges. npm publish additionally needs the operator's 2FA | R21, R22 | **open — sequenced behind `feat/field-notes-pack`** |

```
carry-over: 3 open · unresolved: 0 · dropped with agreement: 3 · reassigned: 1
```

### How the contract closes without the backfill

Dropping M5 left the widened four taught by the skeleton and required by
nothing — a dead zone where a new pack copies the thirteen-heading template,
keeps the cheap nine, and still passes the gate. That is resolved without any
origin: the per-pack rule is **all-or-nothing**. Nine are always required; touch
one of the widened four and all four are owed. The six legacy packs stay valid
on nine, and no pack can ever be half-widened. Verified against a planted
half-adoption, which the gate caught and then went quiet on revert.

## Coverage against the REQ table

| REQ | State | Evidence |
|---|---|---|
| R1–R8 | **done** | `MOTION_DOCTRINE.md`; asserted by `sloplint.py` (19 string checks) |
| R9 | **done** | dials in `SKILL.md`; asserted by `sloplint.py` |
| R10 | **done** | three defaults recorded in `SKILL.md`; asserted by `sloplint.py` |
| R11 | **done** | `test/sloplint.py`, wired into `npm test`; planted defect caught in a real token layer, then silent on revert |
| R12 | **done** | `test/validate_palette.py`, 162 checks, `--self-test` watches each check fail |
| R13, R14 | **done** | contract widened to thirteen; template and both mirrors enforced |
| R15, R16 | **dropped (operator agreement)** | carry-over row 5; contract closed by the all-or-nothing gate instead |
| R17 | **reassigned** | carry-over row 4 |
| R18 | **dropped (operator agreement)** | carry-over row 6 |
| R19, R20 | **done** | depth model, `dataviz` handoff, `?variant=` in `SKILL.md`; asserted by `sloplint.py` |
| R21, R22 | **open** | carry-over row 7 |
| R23 | **done** | `package.json` description corrected |

Gate at close: `validate.py` **299** (floor was 272) · `validate_palette.py`
**162** · `sloplint.py` **170**.

## Blocked, waiting on the operator

1. **Merge order** — `feat/field-notes-pack` lands first and takes 1.5.0; this
   branch rebases and takes the next number. npm publish needs 2FA at the end.

Resolved 2026-08-04: the operator has no URLs for the three unaddressable packs
and no reference site for the industrial register. Both modules are dropped by
agreement rather than carried — a pack authored from values nobody can re-read
would break the one promise the pack layer makes.
