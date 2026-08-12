# Acceptance — `pigeonhole`, v1.21.0

Run: `feat/pigeonhole-pack-v1.21.0`, merged at `149324c`, tagged `v1.21.0`,
published to npm as `1.21.0`. Gates on the branch: **1920 / 906 / 436** against
floors raised from 1788 / 791 / 422 in the same commits.

## The ladder walk, first

The REQ table finds what was named and lost; the walk finds what was never named.
Each row of the brief was walked decision → spec → contract *and its failure
behaviour* → task → change → executed test → surface, ordered by seam. Three
absences surfaced, and all three became work rather than notes:

1. **A token declared and never named.** `--radius-panel-sm` (20px, measured on 12
   elements) was added when a fresh-context read asked for it, and the pack's radius
   vocabulary still listed six of seven. A value an implementer cannot reach for is
   the same as a value that does not exist. Fixed: the list carries all seven with
   their frequencies (`98722cd`).
2. **A state specified and undocumented.** `selected` was written into the pack and
   shipped in the stylesheet, and `CategoryChip.md` — the doc an implementer reads
   *at* the component — said nothing about it. Fixed in the same commit, along with
   the two categories whose layers collapse, which belong where the implementer
   meets them rather than in Gotchas.
3. **An exclusion held only by prose.** The category tokens sit outside the palette
   gate's semantic peer set on purpose, and nothing but a paragraph enforces it:
   `STATUS_TOKENS` matches by name, so `--cat-*-ink` can never join the peer set and
   can never be *checked* for having left it. That is B-017's own defect shape
   pointed at this pack, and it is filed as **B-026** rather than fixed here,
   because the fix is the peer-set widening B-017 already owns.

## Coverage — one row per REQ

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 | **green** | `validate.py` heading + contract checks and `sloplint.py`'s origin check, green at 1920: thirteen headings plus `## Motion flavor`, `Contract: widened`, an `Origin:` with the URL, the date and the byte counts read |
| REQ-02 | **green** | Grepped rather than asserted, and the grep found two silent declarations before it passed: **121 declarations, 120 marked inline, one (`--font-display`) marked in the comment above, zero unmarked** (`3b413b0`) |
| REQ-03 | **green** | `npm run palette` OK (906). No `color-mix()` or `lab()` in the layer |
| REQ-04 | **green** | `validate_stated_ratios()` — and it earned its keep: it refused **nine** of this run's own lines where the reference's *failing* number sat on the derived token's declaration, plus `--ink-lede`. Now every stated ratio recomputes |
| REQ-05 | **green** | `## Gotchas` carries the eight failing inks with their numbers (worst `#49d1fa` 1.53:1), the lede at 3.74:1, the CTA's 5.04 / 3.29 split, the badge at 2.31:1 and `outline-style: none` — each recomputed by the gate at write time |
| REQ-06 | **green, and its argument was wrong until T25a** | The declaration carries ΔE 4.42 → 1.24 and the pack states *never by colour alone*. The **causal** claim (derivation *caused* the collapse) was refuted: 4.42 is already under the floor of 10. Restated in pack, kit, doc and README (`931d954`) |
| REQ-07 | **green** | `validate_kits()` green; `tsc` emitted 11 modules with declarations, verified by listing `dist/` rather than by the exit code |
| REQ-08 | **green** | `validate_fork_reciprocity()` green. Five forks written from both sides — `cyclorama`, `showroom`, `orchard`, `workbench`, `manpage`. Three routing mentions were deliberately left as bare names: a link is a claim of confusability, and `instrument-console`, `scoreboard` and `datasheet` are not confusable with a white pastel-taxonomy page |
| REQ-09 | **green** | `validate_counted_claims()` + `validate_contract_split()`. The gate found three sites the sweep missed (`bin/cli.js`, `package.json`, `MOBILE_SURFACES.md`) and two more in `README.md` |
| REQ-10 | **green** | `validate_pack_enumerations()` green; its first run enumerated more than twenty missing sites, which is how the integration list was built |
| REQ-11 | **green** | `test/floors.json` raised with the reason in the same commit, twice (906 the second time). The ratchet was **watched refusing 1921** with its own message |
| REQ-12 | **green** | T25a and T25b, both branches, fresh contexts, **run before the tag**: green, 49 findings, 22 fixed in `931d954`, one refuted, 26 filed |
| REQ-13 | **green** | `docs/adr/0001-style-pack-naming.md` — the ninth application, with `diptych` and `mailroom` rejected on the ADR's own criteria |
| REQ-14 | **green** | `validate.py` version sync: `package.json`, `marketplace.json`, `plugin.json`, CHANGELOG top entry, `SKILL.md metadata.version` all 1.21.0 |
| REQ-15 | **green** | CI read **before** the tag on the exact commit tagged — run 31642256634 on `98722cd`, 18 jobs, `kits (pigeonhole)` success. `npm view` 1.21.0, `latest` 1.21.0. The published tarball pulled from the registry and read: **509 files**, carrying `styles/pigeonhole.md` (29,203 bytes), its token layer (21,797) and 27 kit files, with `version: 1.21.0` inside the bundle and the fitted `7.82vw` ramp present. Local channels read from disk: the plugin resolves to `…/1.21.0` and that directory carries the pack; the hub copy reads `version: 1.21.0`; the shadow invariant printed nothing |
| REQ-16 | **green** | Both refuted claims recorded in the brief, the design record, the pack's Gotchas and the CHANGELOG's Notes: zero rotated elements at three viewports, and a diptych that is raster art — `Before`/`After` appear zero times in the served HTML and zero times in the live DOM after a full scroll pass |
| REQ-17 | **green as restated** | The graph is `9312a85` against a merged HEAD of `149324c` — 1703 nodes, 2537 links, 31 hyperedges. B-009's two candidate fixes are a decision this run does not own, so the staleness is restated rather than forced past the shrink guard |
| REQ-18 | **green** | `.tmp-fp-hero.png` removed from the tree and `.gitignore` given the `.tmp*` rule. This run produced six screenshots and four measurement dumps and committed none of them; B-015 closed |
| REQ-19 | **green** | Both runs stamped — this one at `98722cd` and the **1.20.0 run backfilled at `e97a8cc`**, which had left none. The ten instructions walked; all ten fired, none retired, and the walk is written into the prune log rather than claimed |
| REQ-20 | **green** | `main == origin/main == 149324c`, the tag's commit is an ancestor, every tree clean and pushed |

**No REQ was removed.** REQ-06's evidence changed shape when its argument was
refuted; the requirement did not.

## What the two blind runs cost and bought

Forty-nine findings for two subagent runs. Twenty-two were real defects in a pack
that three green gates and a green CI had passed hours earlier, and the four that
mattered most were arithmetic the gates structurally cannot see: a `clamp()` whose
coefficient does not produce the size the prose claims, a line-height that cannot
produce its own stated pairing, a hero frame described as below a fold it sits
inside, and a reduced-motion branch that strobes an infinite animation instead of
stopping it.

The root cause of the first three is one habit: the ramps were **transcribed from
the reference's declared values** instead of **fitted to this run's own readings**.
That is the same class as reading a ratio off an OKLCH parent instead of the shipped
hex, which this repository already caught once — one layer up, in a different unit.

## Ledgers, closed

- **Verification ledger** — twenty rows added, REQ-01 … REQ-20, each with the date
  and the thing that was watched. Rows at `never`: still **1** (REQ-10 from the
  2026-08-10 audit, carried at B-004). This run added none.
- **Board** — 25 rows, **19 open**. Closed here: B-015. Filed here: B-021 … B-024
  against `showroom` (its status chip measures 2.33 / 1.78 / 3.05 on white at the
  size the pack specifies; two tokens share one hex; three motion values contradict
  the doctrine in the same bundle), B-025 against the skeleton's Components
  contract, and B-026 for the peer-set exclusion this pack now depends on.
- **Carry-over** — B-013, B-016, B-017, B-020 and B-009 leave open, each with a
  board id and a reason. B-016 gained a second instance, found and fixed by hand
  (`SURFACE_COMPOSITION.md`'s accent-role tally, recounted from the token layers as
  fourteen of sixteen); its class is still unguarded.

Every gate verdict in this document is printed beside a count, so *green* cannot be
read as *verified*.
