# Task brief — four style packs (`showroom`, `blueprint`, `prism`, `maquette`)

**Run:** 2026-08-09 · branch `feat/four-packs-v1.9.0` (from `main` @ `20797ef`)
**Pipeline:** task-pipeline, stages 0→10 · **Model:** Opus 5 (1M context)
**Target release:** v1.9.0, one tag for all four.

## Scope

Add **four** style packs, taking the library from eight to twelve, each extracted
from a live reference by reading its computed styles on 2026-08-09:

| Pack | Origin | Register in one line |
|---|---|---|
| `showroom` | <https://attio.com/> | the product itself is the hero — a dense, real application surface shown at full fidelity |
| `blueprint` | <https://www.pinecone.io/> | an engineering drawing: white field, zero radius, grid and registration marks, one electric blue |
| `prism` | <https://milvus.io/> | an open-source project's front door: white split into an iridescent spectrum, mono body copy |
| `maquette` | <https://zilliz.com/> | a built object on a dark table: cream axonometric models with mono block labels |

**Names follow ADR-0001** — the register, never the source brand. `attio`,
`pinecone`, `milvus`, `zilliz` would each violate it.

Out of scope, stated so it cannot be re-scoped in quietly: no change to the
motion doctrine or the dials; no change to the *values* of any existing pack.

## Evidence gathered before the first decision

**Standing instruction 1 — concurrency.** `git reflog -4` shows only this
session's own moves. Branch list: `main` alone (all `feat/*` retired on
2026-08-08). One worktree. Tree clean. No file touched in three hours.

**Standing instruction 2 — release state from the registry and the tags.** Local
and remote tags both stop at `v1.8.0`; `npm view` → `1.8.0`; manifests → `1.8.0`;
`npm view sheleg-design-skill@1.9.0` → 404. **v1.9.0 is free.**

**Floors at the start:** `validate.py` **876** · `validate_palette.py` **305** ·
`sloplint.py` **192**, measured on `20797ef`.

## The four references, measured

Every ratio below was computed by importing `test/validate_palette.py`, so the
packs cannot claim a number the repository's own gate disagrees with. Attio's
palette is declared in **CIE Lab**, which that gate cannot parse; each value was
converted by painting it into a 1×1 canvas and reading the sRGB bytes back —
the browser's own conversion, not arithmetic of this run's.

| | `showroom` | `blueprint` | `prism` | `maquette` |
|---|---|---|---|---|
| Field | `#FFFFFF` | `#FBFBFC` / `#FFFFFF` | `#FFFFFF` | `#151515` |
| Ink | `#1C1D1F` — **16.87:1** | see the conflict below | `#00131A` — **18.95:1** | `#FFF9F4` — **17.49:1** |
| Secondary ink | `#232529` | `#4B5563` | `#667176` — **5.01:1** | `#B3B5C1` — **8.95:1** |
| Accent | `#266DF0` — **4.64:1** as text | `#002BFF` — **7.53:1** as text | `#00B3FF` — **2.36:1** ✗ | `#97FDFF` — **15.49:1** |
| On accent | white, 4.64:1 | white, 7.53:1 | ink, 8.02:1 | black, 17.81:1 |
| Type | Inter / InterDisplay / JetBrains Mono / Tiempos | GT Planar + JetBrains Mono | Geist + Geist Mono | Geist + Geist Mono |
| Radius | 2/4/6/8/12/16/20 | **none** | 8-ish | 8 · 36 pill |
| Elevation | a **seven-layer** stacked shadow | one soft shadow + a 1px accent ring | flat | an **offset** shadow, `12px 24px 24px` |
| Reduced motion | present | **absent** | **absent** | present, 4 blocks |

### Four defects the packs correct rather than propagate

1. **`showroom`'s caption colour cannot carry a caption.** The reference's
   `--color-caption-foreground` `#A4ADBA` measures **2.27:1** on its own white
   field. The pack keeps it as a *disabled//placeholder* value and routes real
   captions to a measured ink that passes.
2. **`blueprint`'s ink is pure black**, used on 316 elements. The doctrine bans
   pure black as ink, and `sloplint.py` enforces it. The pack ships the
   reference's **own second ink** `#111827` (136 elements) at **17.74:1** — a
   real value from the same page, not an invention. It is a **visible**
   substitution, not a rounding: the two sit **21.2** apart in OKLab, and the
   pack says so rather than pretending they are the same black.
3. **`prism`'s accent is not a text colour** — `#00B3FF` measures **2.36:1** on
   white, and the reference sets 72px display type in it. Fill-only, like
   `cyclorama`'s orange; ink on it is 8.02:1.
4. **Neither `blueprint` nor `prism` ships a `prefers-reduced-motion` branch** —
   zero blocks each, against live marquee, ping, pulse and scroll animations.
   Both packs require the branch the reference omits.

### Two colour-blindness findings

- `showroom`: `--good` `#0FC27B` and `--danger` `#FF5B59` separate by **4.9
  under deuteranopia** (floor 8) — the classic pair. Above the hard floor, so
  legal with the `never by colour alone` declaration.
- `prism`: `--warning` `#F25C05` and `--danger` `#D51F00` separate by **11.3**
  at full colour (floor 15). Same treatment.
- `blueprint` needs no declaration: every pair clears both floors.
- `maquette`: **corrected after the gate said no.** This brief first claimed the
  pack needed no correction. That claim rested on status values this run had
  *invented* rather than measured — the reference exposes no status palette at
  all — and the palette gate caught them colliding (7.9 under deuteranopia, 7.8
  under protanopia). The set was re-derived inside the pack's own world, marked
  in the token layer as a pack decision rather than an extraction, and the
  declaration added. Green and red remain 6.4 apart under deuteranopia in every
  candidate tried, because no hex separates that pair for a deuteranope.

## The routing defect this run also fixes

Reproduced during stage 0, after a probe subagent reported it: **five of the
eight shipped packs name no other pack at all.** Forks exist only in
`field-notes` (3 mentions), `cyclorama` (5) and `atrium` (1) — and every one of
them points *backwards*, at packs that never point back. `instrument-console`,
the pack any infrastructure brief reaches first, carries no fork whatsoever.

Adding four more one-way forks would make a twelve-pack table with eight dead
ends. So this run also adds **reciprocal pointers**: where a new pack forks
against an existing one, the existing one gains the mirror clause, and a
validator check enforces the reciprocity.

## Locked decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Names `showroom` / `blueprint` / `prism` / `maquette` | ADR-0001: the register, never the brand |
| D2 | `maquette` is a full pack, not a variant | Settled by measurement, not opinion — a two-branch scenario probe run **before** any kit was written. Probe A chose `maquette` for an architecture brief and named the discriminating test; probe B stayed on `instrument-console` for a live-telemetry brief and reported that `maquette` pulled on surface features only |
| D3 | One release, v1.9.0 | Operator's choice; free per the registry and tags |
| D4 | Reciprocal forks + a validator check | The routing table is the pack layer's only entry point; one-way edges make it a list, not a router |
| D5 | Attio's `lab()` is converted, not re-picked | The gate cannot parse `lab()`. Conversion through the browser's own canvas keeps the colour identical; re-choosing values would be invention |

## REQ table — frozen

| ID | Requirement | How it is verified | Status |
|---|---|---|---|
| REQ-001 | Four pack documents, each on the thirteen-heading widened contract with an addressable `Origin:` | `validate.py` pack section + `sloplint.py` `lint_packs` | open |
| REQ-002 | Four token layers, every value hex/rgb/oklch — **no `lab()`, no `color-mix()`** | `validate_palette.py` prints a ratio line for each of the four | open |
| REQ-003 | Each pack's ink clears WCAG AA on its own field, and each pack states the figure it holds | the gate's ratio lines; the Palette tables | open |
| REQ-004 | The four corrections above are each documented in the owning pack's `## Gotchas`, with their measurements | `grep` for the ratios; read-through at stage 10 | open |
| REQ-005 | `showroom` and `prism` declare `never by colour alone`; the gate reports their tight pairs as covered | `validate_palette.py` output contains `covered by secondary encoding` for both | open |
| REQ-006 | Four kits, each with the six-component spine whose `*Props` match `kits/workbench` | `validate.py` kit section | open |
| REQ-007 | Each kit's `styles.css` starts with its token layer verbatim and holds no colour literal after the marker | `validate.py` kit checks 6 and 7 | open |
| REQ-008 | All four routed from `SKILL.md`, `README.md`, `bin/cli.js`, a `cursor/rules/*.mdc`, and `install.sh` | `validate.py` — five checks per pack | open |
| REQ-009 | `.cursor/` mirrors the bundle file-by-file, both directions | `validate.py` mirror check + `diff -r` | open |
| REQ-010 | Three gates above the floors 876 / 305 / 192; both `--self-test` flags pass | `npm test && npm run selftest`, counts printed | open |
| REQ-011 | Four scenario pairs (T16–T19), each with a negative branch, each run in a separate fresh context | the eight subagent runs, verdicts recorded in `test/scenarios.md` | open |
| REQ-012 | **Reciprocal forks**: every pack named in another pack's fork names it back | a new `validate.py` check, watched failing against a planted defect | open |
| REQ-013 | Four-way version sync at 1.9.0 and a CHANGELOG top entry | `validate.py` version-sync check | open |
| REQ-014 | `package.json` scripts and `validate.yml` steps still agree | the diff, printed — standing instruction 7 | open |
| REQ-015 | `v1.9.0` released: workflow green, `npm view` → `1.9.0`, tarball carries all four packs and kits | `gh run list` + `npm view` + unpacking the tarball | open |
| REQ-016 | Local installs refreshed; the shadow check prints nothing | `npx --yes sshlg-skills@latest update` | open |
| REQ-017 | `DOCMAP.md` floors and pack count, the wiki, and the code graph updated | stage 9 outputs | open |

## Autonomy sweep

| Row | Answer |
|---|---|
| Manual gates | **stage 3** (this spec set) and **stage 7** (`git push origin v1.9.0`) |
| Run mode | advance without check-in between packs; stop only at those two |
| Shared state | `ungated`; zero `feat/*` branches at start, so instruction 1's signal is clean. Re-check owed before `git add` |
| Source of truth | `git rev-list --count HEAD..main` = 0 |
| Test command | `npm test` and `npm run selftest`; kit builds via `tsc` |
| Deploy | tag push triggers `release.yml`; local npm is unauthenticated by design |
| Escalation | decide alone inside the repository; escalate the tag push |
| UI verdict | design-system artifacts, not product UI. super-ux not armed; no Figma destination needed |

## Open assumptions

- `blueprint`'s grid, vertical rules and corner registration marks were **not
  reachable from any stylesheet rule** by the selectors tried; they are described
  from the rendered page and will be marked as observed geometry rather than
  measured declarations, the way `cyclorama` marks its status pill.
- GT Planar (blueprint) and Tiempos (showroom) are licensed faces; each pack must
  name obtainable substitutes, verified by measurement as `cyclorama`'s were.
