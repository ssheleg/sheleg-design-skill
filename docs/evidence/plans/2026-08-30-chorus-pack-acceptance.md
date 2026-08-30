# Acceptance — the thirty-ninth pack, `chorus`

Run opened 2026-08-30 against the brief of the same date. Baseline `7d20da9`, branch
`feat/chorus-pack-v1.55.0`, lease `SG-CHORUS`. Every row below names the command or
the reading that settled it; nothing here is asserted from confidence.

## REQ verdicts

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-1 | **met** | `styles/chorus.md` header carries `Origin: <https://crowdreply.io>` and the method; ADR-0001 gained the naming entry with the four rejected alternatives |
| REQ-2 | **met** | `python3 test/validate.py` → OK; the pack declares `Contract: widened — all thirteen headings` and the `Themes:`/`Rank:` lines derive |
| REQ-3 | **met** | `python3 test/validate_palette.py` → OK (3,359 checks); every value carries MEASURED / SELECTED / DERIVED |
| REQ-4 | **met** | six Gotchas, every figure recomputed by the gate — see the table below |
| REQ-5 | **met** | `kits/chorus` builds (`tsc -p tsconfig.json`, clean); the token block is byte-identical to `styles/tokens/chorus.css`, checked by `validate.py` |
| REQ-6 | **met** | counted claims moved 38 → 39 across eleven files; the widened remainder 32 → 33; `validate.py` OK |
| REQ-7 | **met** | `validate_fork_reciprocity()` OK — `chorus` ↔ `surveyor`, `chorus` ↔ `deskmate`, both directions, in both the bundle and the `.cursor/` mirror |
| REQ-8 | **met** | render log below |
| REQ-9 | **met, 2026-08-30** | both branches ran blind on fresh contexts and both passed; the negative branch stayed on `surveyor`. 29 findings returned between the two reads, 13 fixed in v1.58.0. B-136 closed |
| REQ-10 | **met** | PR #12 merged with 84 green checks, annotated `v1.55.0` pushed, release workflow green, `npm view` answered 1.55.0, and the published tarball carries `styles/chorus.md`, `styles/tokens/chorus.css` and `kits/chorus/` — read out of `npm pack sheleg-design-skill@1.55.0` |
| REQ-11 | **partly met** | local installs refreshed: the plugin reads 1.56.0, `chorus.md` is present in the cache and in the hub, the shadow check and the broken-symlink check are both empty. **Not done:** the launcher's own pin in `~/DATA/sshlg-skills` still names v1.54.0, because that repository had ~2,100 lines of another session's uncommitted work in its tree. Named in the release notes rather than left silent |
| REQ-12 | **partly met** | the ledgers, the board and this record are current as of v1.58.0. The graph artefact under `graphify-out/` is still stamped at `4b0d827` and is a separate refresh |

## The reference's failures, recomputed

Every figure was produced by importing this repository's own palette gate
(`test/validate_palette.py` → `parse_color()` + `contrast()`), never by hand. The
first draft of this table *was* computed by hand and was wrong in every row, because
`contrast()` takes linear RGB and it was fed 0–255 integers — `#000` on `#fff` came
back as 5101:1 instead of 21:1. That is why the rule is *import the gate*.

| What the reference ships | Measured | Floor it misses | What the pack ships instead |
|---|---|---|---|
| `#ffffff` on `#f96f4b`, 14px/500, the primary CTA | **2.84:1** | 4.5:1, and 3:1 large | the same coral fill with an ink label — `#1b181c` on `#f96f4b` is 6.20:1 |
| `#f96f4b` as a word on `#fbfaf9`, 16px/600 | **2.72:1** | 3:1 large | `--coral-ink` `#cb441f`, 4.59:1 on `--bg` |
| `#ff5d30` link on `#fbfaf9` | **2.94:1** | 4.5:1 | the same derived step |
| `#8a8692` on `#fbfaf9`, 14px/400, 38 instances | **3.41:1** | 4.5:1 | `--ink-muted` `#6a6673` at 5.36:1; the measured value survives as `--ink-ghost`, non-text |
| `#239806` on `#fbfaf9` | **3.62:1** | 4.5:1 | `--good` `#198400` derived at hue 141.1°, 4.64:1 |
| a card against its field, no border, no shadow | **1.04:1** | not an edge at any threshold | every card gains a 1px `--line` |
| the ink focus ring on the dark slab | **1.00:1** | 3:1 mark | `--focus-color` re-declared to `--paper` on the slab, 16.54:1 |

Structural findings, counted rather than described: **zero** `:focus` rules, **zero**
`:focus-visible` rules and two `outline: none` declarations in 274,355 bytes of CSS;
**zero** `prefers-reduced-motion` rules against **383** script-set inline transforms,
**1,057** script-set inline opacities and **43** computed `will-change`; **one**
`@keyframes`, and it is Framer's vendor loading spinner; the declared amber `#ffc300`
paints **zero** elements at any of the three widths, which is why the pack has three
status roles and says so.

## Render log — REQ-8

`kits/chorus/src/styles.css` rendered in a static harness through CDP, computed values
read back with `getComputedStyle` and geometry with `getBoundingClientRect`.

| Claim in `styles/chorus.md` | 1440×900 | 768×1024×2 | 390×844×2 |
|---|---|---|---|
| Display 56px · 1.1 · −0.0625em, 40px · −0.025em below | `56px/61.6px ls-3.5px` Outfit | `40px/44px ls-1px` | `40px/44px ls-1px` |
| Section head 44px · 1.2 · −0.032em, 34px below | `44px/52.8px ls-1.408px` Inter | `34px/40.8px ls-0.85px` | `34px ls-0.85px` |
| The quoted question, 24px · 1.5 · −0.02em, display face | `24px/36px ls-0.48px` Outfit | `24px/36px` | `24px/36px` |
| Body line-height 1.7 | `16px/27.2px` | — | `16px/27.2px` |
| `--r-bubble` = 24px 0 24px 24px | `24px 0px 24px 24px` | unchanged | unchanged |
| Card: `--r-card`, 32px padding **and gap at every width**, 1px `--line`, no shadow | `12px`, `32px`, `32px`, `1px rgba(70,72,77,.12)`, `none` | `32px` | `32px` |
| Primary button: coral fill, ink label, 36px | `rgb(249,111,75)` / `rgb(27,24,28)` / **36px** | 36px | 36px |
| The ruled frame — 1116px around 936px | rules at `x=162` / `x=1277`, inner `936` | `20`/`747`, inner `728` | `20`/`369`, inner `350` |
| The slab, 30px inset, `--r-panel` | `x=30`, `w=1380`, `16px` | `x=30`, `w=708` | `x=30`, `w=330` |
| Focus on the slab resolves to the paper token | `--focus-color` computes `#faf8f0` inside the slab, `#1b181c` at `:root` | — | — |
| Mint only in a well | `rgb(54,255,148)`; the light delta computes `rgb(25,132,0)` | — | — |
| Skeleton does not animate | `animation-name: none` | — | — |
| No horizontal overflow | `scrollWidth − innerWidth = 0` | `0` | `0`, and **0** elements past the viewport |

**One defect the render found and the source did not.** The button measured **38px**
against a claimed 36. The kit had given every variant `border: 1px solid transparent`
so variants could swap without a shift — a pattern borrowed from `surveyor` — and with
`box-sizing: border-box` that border is 2px of height the reference does not spend. The
reference's control is 36px with 8px/16px padding and **no edge**. Fixed by removing
the border from every variant and giving the ghost variant an inset ring instead, which
is an edge rather than elevation and leaves the four-shadow rule untouched. Re-measured:
36 / 36 / 36 across all three variants. A gate reads structure; only a render reads
layout, which is the whole reason this row exists.

## Gate output at the close of the build

```
python3 test/validate.py          OK (5533 checks)
python3 test/validate_palette.py  OK (3359 checks)
python3 test/sloplint.py          OK (776 checks)
npm test                          exit 0
cd kits/chorus && npm run build   clean
```

The palette gate's two ratchets did **not** move: `unresolved` stayed at its pinned 25
and `unguarded` at its pinned 27, which makes `chorus` the fourth pack in a row to add
a full Palette without buying a ceiling. Nine claims had to be rewritten to get there,
and eight of the nine were the same defect — a subject, its partner and its number
split across a line break.

## Carry-over

| # | What | Where it goes |
|---|---|---|
| 1 | ~~T37 written, not run~~ — **closed 2026-08-30**, both branches run blind and both passed | `test/scenarios.md`, B-136 |
| 2 | Nine verified `surveyor` findings from T37b, one fixed and eight filed | board B-137 |
| 3 | Four `chorus` findings that were correct readings of a deliberate choice, now stated in the pack | board B-138 |
| 4 | The launcher's pin still names v1.54.0 — blocked on another session's uncommitted work in that repository | release notes, and the operator |
