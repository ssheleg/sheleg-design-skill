# Brief — `roster`, the seventeenth style pack

- **Run:** `feat/roster-pack-v1.24.0`, opened 2026-08-13 from `main` at `bbae23c`
- **Reference:** <https://www.babylovegrowth.ai/en> — the marketing site of an AI-search
  visibility product (SEO content plus backlinks, sold on being recommended by Google
  and ChatGPT)
- **Opening request:** *"https://www.babylovegrowth.ai/en этот сайт тоже добавь"* — the
  address and nothing else, which is the fourth time in this repository. ADR-0001
  requires it be answered by pointing at the naming rule rather than by complying
  silently: the pack is named for the register it encodes, **`roster`**, and the address
  lives in its `Origin:`.

## What was measured, and with what

| Instrument | What it produced |
|---|---|
| `curl` | `/en` at 1,415,414 bytes; two stylesheets at 7,464 + 459,113 = 466,577 bytes, declaring 410 custom properties |
| headless Chrome, CDP `Runtime.evaluate` at 1440×900 | computed styles for **5,936** rendered elements |
| the same at 768×1168 and 390×790 | the responsive steps, measured rather than read off breakpoint names |
| a 1×1 canvas, painted and read back | every `lab()` / `oklab()` the page computes, resolved to the sRGB it actually paints — **34 distinct values** |
| `test/validate_palette.py`, imported | every ratio this brief and the pack state |

Screenshots at 1440×1000 and full-page 1440×3400 were read as well; both are scratch and
neither is committed.

## The register, in one sentence

A white page in a faint grid of squares whose whole argument is **other people's
names**: the AI engine's own wordmark set inside the headline, a wall of client
logotypes sorted into six labelled industry columns, a third-party review badge, and
case cards with real charts.

The identity in one sentence: **the proof is a name, not a number.** Not a page that
claims a result — a page that shows you the roster and lets the roster do the claiming.

## Why the library has room for it, at seventeen packs

The pairwise question, asked against all sixteen (standing instruction 10). One fork is
sharp enough to be the pack's reason for existing:

- **`scoreboard`** — warm paper, pixel numerals, *"products whose argument is an
  accumulating number — growth, ads, SEO"*. This reference **is** an SEO product, so a
  router reading the category alone will land there. The fork is the kind of proof: on
  `scoreboard` the subject is a **figure that ticks up**; here it is a **name that
  appears** — an engine's wordmark, a client's logotype, a review score someone else
  computed. A page can only be built around one of the two.
- **`showroom`** — white and product-led, but its hero is the application at real size.
  Here the first viewport carries no product screenshot at all: it carries a claim and
  other companies' marks.
- **`pigeonhole`** — also white with a labelled system, but its labels are the
  *product's own* taxonomy applied to the reader's mess. These labels are other
  companies' identities, and none of them is the product's to design.
- **`prism`** — an OSS front door whose step one is a command; nothing here is installed.
- **`atrium` / `orchard`** — warm consumer fields; this one is cold white with a
  framework's grey.

## Source ledger — what the project already knew

| Source | State |
|---|---|
| `docs/DOCMAP.md` | present |
| `docs/superpowers/retro.md` | **all ten standing instructions read in full**; the log queried for pack authoring, ramps, colour and counts |
| `docs/superpowers/backlog.md` | 32 rows, **19 open**; B-027, B-028, B-030 and B-032 touch colour and breakpoints and are not this run's |
| `docs/superpowers/verification.md` | 31 + 20 + 10 + 10 rows; **1 at `never`** (REQ-10, carried at B-004) |
| `docs/audit/2026-08-13-modern-css-audit.md` | binding on this pack: it is the first authored after the audit, so it inherits the container-query answer as a requirement rather than a suggestion |
| ADR-0001 | binding — the naming rule; this run is its tenth application |
| ADR-0002 | binding — the kit ships as source, `dist/` gitignored |
| release state | `v1.23.1` on the tags, on `origin` and on npm; four manifests agree. Next is **1.24.0**, no ghost |
| concurrency (instruction 1) | clean at stage 0: one worktree, no foreign HEAD move, no recent foreign mtime. Re-checked before staging |

## Decisions taken in the grill

1. **Scope: the full treatment**, as `datasheet`, `manpage` and `pigeonhole` had — pack,
   token layer, kit, reciprocal forks, every enumeration, the floors ratchet, the
   release, the local channels. Precedent, not a new decision.
2. **Name: `roster`.** The register is proof-by-name, and a roster is the list of names
   that already belong. Rejected: `pegboard`, which names the square-grid *texture*
   rather than the register and would route a brief by its wallpaper; `directory`, which
   reads as a product category and would mis-route anyone building a listing site;
   `lobby`, which is the best metaphor for a logo wall and collides with `atrium` in the
   same building-space family. **This is the one decision in the run that is cheap to
   reverse today and expensive after release.**
3. **Contract: `widened`** — all thirteen headings, and the container-query answer the
   1.23.0 gate requires of every widened pack.
4. **The palette is resolved, not re-picked.** The reference paints its neutrals in
   `lab()`, which the palette gate still refuses on purpose. Each was resolved by
   painting it into a 1×1 canvas and reading the sRGB bytes — the technique this
   repository's own 2026-08-09 brief prescribes. *(`ctx.fillStyle` read-back no longer
   converts in Chrome 151; it returns the value in its original space. The pixel is the
   oracle, not the serialisation.)*
5. **Design surface: text-only.** No Figma file is recorded for this repository.

## REQ table — frozen; adding is free, removing needs the operator

| REQ | Requirement | How it is verified |
|---|---|---|
| REQ-01 | `styles/roster.md` carries all thirteen headings, `Contract: widened`, and a dated addressable `Origin:` naming what was read | `validate.py` heading + contract checks; `sloplint.py` origin check |
| REQ-02 | Every value is `MEASURED`, `RESOLVED`, `SELECTED` or `DERIVED` at its declaration — and `RESOLVED` is new, for a `lab()` value read off a painted pixel | the token layer's header defines all four; grep at every declaration |
| REQ-03 | `styles/tokens/roster.css` passes the palette gate, with no `lab()` the gate cannot compute | `npm run palette` |
| REQ-04 | Every ratio the pack states recomputes from the token layer | `validate_stated_ratios()` |
| REQ-05 | The reference's own failures are recorded with numbers, never applied: the nav CTA's white 16px label on `#f25533` at **3.43:1**, the dominant grey `#6a7282` at **4.35:1** on its own `#f0f3f8` band, and **reduced motion covering six animations out of roughly twenty** | the Gotchas, each number recomputed or recounted at write time |
| REQ-06 | The `h1` is recorded as what it is — `.sr-only`, 1×1px, `clip-path: inset(50%)` — and the pack states which of the two conventions it teaches | the pack's Type section |
| REQ-07 | The container-query answer the 1.23.0 contract requires is present and specific to this pack's components | `validate_pack_container_answer()` |
| REQ-08 | `kits/roster` exists with the identical spine, a doc per component, and `src/styles.css` opening with the token layer byte for byte | `validate_kits()`; `dist/` listed after `tsc` |
| REQ-09 | Every width query the kit ships is a container query or carries a declared PAGE / SELF reason | `validate_kit_breakpoints()` |
| REQ-10 | `roster` names every pack a reader could confuse it with, and each names it back | `validate_fork_reciprocity()` |
| REQ-11 | The count word moves sixteen → seventeen everywhere, manifests included | `validate_counted_claims()`, `validate_contract_split()` |
| REQ-12 | Every pack enumeration gains the pack | `validate_pack_enumerations()` |
| REQ-13 | `test/floors.json` rises with the reason in the same commit | the three gates |
| REQ-14 | A routing scenario against `scoreboard` is written **with both branches and run** | two fresh-context runs; findings reproduced per instruction 8 |
| REQ-15 | ADR-0001 records this application — `babylovegrowth.ai` → `roster` — with the rejected names and why | the file |
| REQ-16 | Version 1.24.0 synced five ways | `validate.py` version sync |
| REQ-17 | `v1.24.0` tagged, released, published; CI read **before** the tag; every channel verified by reading installed files | `gh run view`, `npm view`, the tarball, the shadow invariant |
| REQ-18 | Any claim the measurement refutes is recorded as refuted | the brief, the design record, the Gotchas |
| REQ-19 | The run is stamped and the ten instructions pruned | `retro.md` |
| REQ-20 | Every repository clean and pushed, the tag reachable from `origin/main` | `git status`, `git merge-base` |

## Carry-over ledger

| Item | Why not in this run | Home |
|---|---|---|
| B-027 / B-028 | the relative-colour migration and the 13 near-miss literals; this pack ships derived colour where it needs it and does not touch the other sixteen | board, open |
| B-030 | `text-box-trim`, measure in `ch`, metric fallbacks, `@property`, fluid spacing | board, open |
| B-032 | the two held container conversions in `blueprint` and `datasheet` | board, open |
| `lab()` in the gate | not needed: the reference's `lab()` values are resolved to sRGB before they reach the token layer, so the gate never sees one. Extending the parser would be scope this pack does not require | not filed — recorded here as considered and declined |
