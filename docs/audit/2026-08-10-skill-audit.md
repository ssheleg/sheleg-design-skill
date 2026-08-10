# Fresh-eyes audit — the `sheleg-design` skill

**Audited at** `7abe96e` (v1.9.0, tagged, released, published).
**Fixed in** `5e00331` and following, shipped as **v1.10.0**.
**Method:** four parallel read-only sweeps (bundle · shopfront · gates · token
layer) plus a direct read of every companion doc. **Every delegated finding was
reproduced against the artifact with a control case before it was acted on**
(standing instruction 8); the contrast numbers were computed twice by two
independent implementations that agree, and the computation was validated
against a known pair (`#000` on `#fff` = 21.00).

---

## The headline

At `7abe96e` all three gates were green — `validate.py` **1270**,
`validate_palette.py` **412**, `sloplint.py` **224** — and CI was green, and the
package was published.

While green, the skill told a reading agent that:

- there were **six** style packs (twelve),
- the chart handoff should use a token ramp that **no pack defines**,
- half the library specifies component states, heroes and breakpoints (six of
  twelve do **not**, and nothing said which),
- thirteen stated contrast ratios that are **wrong**,
- a radius rule whose worked example contradicts it and whose token layer
  implements a third thing,
- and a CSS declaration that the skill's own motion doctrine **forbids**.

None of that is exotic. It is the ordinary decay of a document set that grew from
six packs to twelve in five days — and the reason it decayed *invisibly* is the
subject of this report. **The green was not lying about the checks. The checks
were not looking at the claims.**

---

## Part 1 — Why an agent using this skill produces wrong output

Seven root causes, ordered by how much wrong output each one can produce.

### RC-1 · The token vocabulary is not an interface, though the repo says it is

`CONTRIBUTING.md:60` (at `7abe96e`): *"Token naming is an interface across packs."*
Nothing enforced it. Measured across the twelve token layers:

| Token | Packs defining it |
|---|---|
| `--ink` | 12 / 12 |
| `--bg` | 10 / 12 — `editorial-luxury` uses `--paper`, `instrument-console` `--base` |
| `--accent` | 10 / 12 — `field-notes` uses `--brand`, `orchard` `--cta` |
| `--good` / `--warning` | 5 / 12 |
| `--ok` / `--warn` | 2 / 12 |
| *no status colours at all* | `editorial-luxury`, `orchard` |
| `--accent-tint` | **1 / 12** |
| `--accent-deep` | **3 / 12** |

Every cross-cutting document then had to name tokens some packs lack, and did:

- `SKILL.md:196` promised `dataviz` *"the pack's tint/step scale
  (`--accent-tint` … `--accent-deep`)"* — **no pack defines both.**
- `SKILL.md:200` promised a status palette of `--good` / `--warning` /
  `--danger` — absent from seven packs, two of which have no status colours at
  all.
- `AI_PRODUCT_PATTERNS.md:22-28` names a *different* set (`--ok` / `--warn` /
  `--danger` / `--info`) for the same job.

**Why this is the worst one.** An undefined custom property is not an error.
`color: var(--good)` where `--good` is undefined makes the declaration invalid
at computed-value time, so the property falls back to its inherited or initial
value — silently, with nothing in the console. The agent followed the
instruction *exactly* and the output is wrong. There is no failure signal
anywhere in the loop.

### RC-2 · Half the library is half-specified, and nothing declared which half

Six packs carry `## Components`, `## Hero`, `## Responsive` and
`## Signature element`; six do not:

| Core contract (9 headings) | Widened contract (13) |
|---|---|
| `instrument-console`, `editorial-luxury`, `workbench`, `briefing-room`, `atrium`, `orchard` | `field-notes`, `cyclorama`, `showroom`, `blueprint`, `prism`, `maquette` |

`SKILL.md:82-83` told the agent a pack *"supplies the palette, type, texture,
motion-token values, signature motifs, and bans"* — a list that quietly omits all
four. So an agent choosing `atrium` gets a fluted-glass hero shader specified to
four decimal places (`82.8` ribs, amplitude `0.0255`, bevel `0.0095`) and **no**
hero line ceiling, **no** breakpoints, **no** disabled state for any component.
It will invent them. And because the pack's `## Bans` were written for a page the
pack never specified, the invention passes every check.

**The asymmetry is itself the trap:** the precision of the half that *is*
specified reads as evidence about the half that is silent.

### RC-3 · Counted claims had no home, so they rotted in public

`validate.py` checked that each pack's **name** appears in the README, the CLI
and the rules (`validate.py:368-383`). It never checked a **number**. So twelve
names sat in a table under a sentence that said six:

| Site | Said | True |
|---|---|---|
| `README.md:13-14` | "**six** locked style packs" | twelve |
| `README.md:200` | "identical in all **six** kits" | twelve |
| `README.md:236`, `CONTRIBUTING.md:29` | "(T1–**T7**)" | T1–T19 |
| `DESIGN_SYNC_BRIDGE.md:94` | "**Three** packs … extracted from production sites" | eight |
| `docs/adr/0002:16` | "**six** style packs' worth of components" | twelve |

The one class of claim a machine can settle outright was the only class nothing
checked. `README.md:13-14` is additionally split across a line break — *"six
locked style / packs"* — so even a naive grep would have missed it. The
replacement check normalises whitespace first.

### RC-4 · The contract had four names, and one of them told authors to ship less

At `7abe96e` the pack contract was called:

- **nine** — `validate.py:36`, `sloplint.py:20`, `DESIGN_SYNC_BRIDGE.md:98`
- **ten** — `validate.py:38`, `test/scenarios.md:66`, `CONTRIBUTING.md:40-42`
- **thirteen** — `docs/DOCMAP.md:23,36`
- **fourteen, as an unlabelled list** — `SKILL.md:88-91`

`DESIGN_SYNC_BRIDGE.md:98` is the dangerous one. It instructed:
*"extraction lands in a pack first — **all nine headings** and a
`tokens/<pack>.css`."* An author who follows it ships a nine-heading pack, and
`validate.py` **passes it**, because nine is the floor and the widened four are
all-or-nothing only once one of them is present. The gate cannot catch a pack
that never started.

This is the **second appearance** of this finding class: the 2026-08-08
`cyclorama` run closed exactly it as REQ-018, fixed `DOCMAP.md`, and did not
sweep the other four sites. Per the ratchet rule, its second appearance becomes a
script, not a third ledger row.

### RC-5 · Reference-implementation paths were presented as file headers

`SHELEG_DESIGN.md` §2–§9 each opened with `**File:** src/lib/motion/…` — seven
of them, at lines 84, 164, 189, 198, 332, 349 and 426. The disclaimer that these
belong to the *reference implementation* and not to your project sits at **line
632**, in §13, after all seven. §9's code sample even shows
`import { STAGGER } from "@/lib/motion/tokens"`.

An agent reading in order starts implementing against paths that do not exist and
are not importable — the skill ships no code at all.

### RC-6 · Numbers that were "measured" were not

Thirteen stated contrast ratios were wrong. The mechanism is uniform: a ratio is
computed once by hand, then hand-copied into the palette table, into the prose,
**and** into a CSS comment, and the three copies drift.

| Pack | Claim | Where | Actual |
|---|---|---|---|
| `blueprint` | `--ink` 17.74:1 | `blueprint.md:84`, `tokens/blueprint.css:35` | **17.15** |
| `blueprint` | `--ink-soft` 7.5:1 | `blueprint.md:85` | **7.31** |
| `blueprint` | `--accent` 7.53:1 | `blueprint.md:89`, `:94` | **7.28** |
| `blueprint` | pure black 21:1 | `blueprint.md:118` | **20.31** |
| `showroom` | `--ink-2` 15.9:1 | `showroom.md:75`, `tokens:28` | **15.35** |
| `showroom` | `--ink-soft` 7.7:1 | `showroom.md:76`, `:286`, `tokens:29` | **7.08** |
| `prism` | `--ink-2` 13.6:1 | `prism.md:74` | **12.17** |
| `prism` | ink ≥18:1 over four stops | `prism.md:81`, `:134`, `:292` | **15.85–16.82** |
| `maquette` | `--ink-faint` 5.0:1 | `maquette.md:82`, `tokens:33` | **5.62** |
| `maquette` | `--model-side` 13.9:1 | `maquette.md:86` | **13.57** |
| `editorial-luxury` | `--accent-ink` 6.1:1 | `editorial-luxury.md:34`, `tokens:18` | **6.93** / 4.52 |
| `workbench` | white on accent 5.0:1 | `tokens/workbench.css:14` | **4.57** |

`blueprint`'s four share one cause: its ratio column is headed ``On `--bg` `` and
`--bg` is `#FBFBFC`, but every number in it was computed against pure `#FFFFFF`.
`prism`'s came from carrying the ink-on-white figure (18.95) onto the wash.

Two packs additionally justified a design rule with a mathematical identity:

> `showroom.md:85-86` — *"The accent is symmetric, and that is why there is only
> one of it. `#266DF0` measures 4.64:1 as text on the field **and** 4.64:1 under
> white."*

WCAG contrast is `(L₁+0.05)/(L₂+0.05)` with L₁ the lighter — **symmetric for
every pair by definition**. In `showroom` the field *is* white, so that sentence
states one measurement twice. In `blueprint`, where the field is not white, the
two directions genuinely differ (7.28 vs 7.53) and the pack asserts one number
for both. A rule that happens to be right, resting on an argument that is not.

**None of these crossed an accessibility floor.** The defect is not unreadable
text; it is that a document whose entire authority rests on *"the values come
from a measured reference, never taste at the keyboard"* had thirteen values
nobody had measured recently — which is exactly the habit it exists to prevent.

### RC-7 · Three gates, green, that could not see any of it — and two that got quieter

Reproduced with controls in a scratch tree:

**Defect A — deleting requirements made both gates quieter, and green.**
Strip `## Components`, `## Hero`, `## Responsive`, `## Signature element` from
`blueprint.md`:

```
control (pristine)  validate.py OK (1270)   sloplint.py OK (224)
four headings gone  validate.py OK (1269)   sloplint.py OK (223)   both exit 0
```

`validate.py:355-362` makes the widened four all-or-nothing **only if at least
one is present**; `sloplint.py:206-212` demands an addressable origin **only if
`## Signature element` is present**. Remove all four and both requirements
evaporate together. Nothing enforced the ratchet `DOCMAP.md:55` asserts.

**Defect B — one decoy comment disabled a ban for a whole file, forever.**
`sloplint.py:112-120` took only the **first** match per (file, ban) and, if the
120 characters before it contained a negation word, `continue`d — skipping the
`check()` call entirely, so the counter *fell* and every later occurrence went
unexamined.

```
.real { min-height: 100vh; }                              -> FAIL   (correct)
/* An example of what is banned: never write this. */
.demo { min-height: 100vh; }
.real { min-height: 100vh; }                              -> OK (223)   exit 0
```

Identical CSS. The only difference is a comment.

**Defect C — a green for a self-test that does not exist.**
`python3 test/validate.py --self-test` printed `OK (1270 checks)` and exited 0.
`validate.py` had no argv handling at all; `sloplint.py` matched `--self-test`
against `sys.argv` including `argv[0]`. This is the **same defect the 2026-08-05
retrospective recorded** in `validate_palette.py`, now in two more scripts —
inside a repo whose own docstring says a green from a check nobody has watched
fail is not evidence.

**Coverage the green did not describe.** `validate.py` had no self-test; CI's one
negative test corrupts a version and exercises exactly **1 of 1270** checks.
`sloplint`'s "every fenced example in the shipped docs" was 17 blocks from 3
files — **16 of 19 bundle markdown files, including all twelve packs, were never
linted**, because packs prescribe CSS in inline backticks, not fences. That is
how `atrium.md:224` shipped `transition: padding-top .2s` — a layout property,
transitioned, on a `sticky` element — for two releases, in the bundle that ships
the ban against it.

And the release path was gated on **one of three** gates
(`release.yml:43-46`), with `PUBLISH_NPMJS` and `RELEASE_ENABLED` both armed.

---

## Part 2 — Findings not covered by a root cause

### Contradictions inside a single pack

| Pack | Contradiction |
|---|---|
| `field-notes.md:169-170` | *"an inner radius is the outer radius **minus the padding** … because `12 - 12 ≈ 7.2`"*. 12−12 = 0. `tokens/field-notes.css:142` uses `calc(var(--radius) * 0.6)` — a **ratio**. The rule, its worked example and the implementation were three different systems, and an agent applying the rule as written ships square tags. |
| `blueprint.md:182`, `:201` vs `:255-257` | Components gives the Secondary CTA *"same metrics and marks"* and the Hero recipe puts marks on both buttons — while Signature element says *"One thing means one thing — the primary, not the pair."* **`test/scenarios.md:287-290` records this as "Reproduced and fixed in the same run".** Only the Signature element half landed; the two instructions that cause the violation were never changed. A recorded fix that half-shipped. |
| `atrium.md:109-113` | *"**Three** shadows exist … A fourth shadow means one of these lost its meaning"* — `tokens/atrium.css:123-126` defines **four**. Copying the token layer as the pack instructs breaks the pack's rule on arrival. |
| `MOTION_DOCTRINE.md:159-160` | §5 banned *"animating anything but `transform`, `opacity`, `filter`, `clip-path`"* while §2 prescribes an ease for colour changes and §9 treats a colour change as the baseline. The ban over-reached its own rationale ("trigger layout on every frame"). |

### A measurement asserted in packs that cannot have made it

The colour-blindness ban is **byte-identical in six packs** and is the first
bullet of `## Bans` in each:

> *"Success, warning, danger and info always ship with an icon or a word beside
> the fill … Measured off a production reference, **several of these pairs** sit
> inside a dichromat's confusion line."*

`orchard` defines **zero** status colours. `editorial-luxury` defines one
(`--red`). `briefing-room` defines one (`--good`). One colour cannot form
"several pairs", so the measurement is impossible in three of the six. The
practical damage is not the false provenance — it is that the ban **names four
states as if the pack supported them**, so an agent asked for an error banner in
`orchard` finds the ban, finds no `--danger`, and invents a hue, which
`orchard.md:216` separately forbids.

### The decision register named an artifact that never existed

`docs/adr/0001-style-pack-naming.md:42`: *"The seventh pack is therefore
**`lecture-hall`**, not `graphify`."* No `styles/lecture-hall.md`, no
`kits/lecture-hall/`, no token layer — the pack that shipped from graphify.com is
`field-notes` (`CHANGELOG.md:275`). The ADR was written on a branch that never
merged and was restored verbatim without reconciling its example. The *decision*
was obeyed; the register's example was fiction.

### Discovery gaps in the skill description

`SKILL.md:3`, measured: description **964 chars**, front-matter **1010** against
a 1024 limit — 14 characters of headroom. Every trigger it promised was served,
but whole capabilities had no trigger at all: **presentation decks**
(`briefing-room`, a full standalone register with scenario T10), **the motion
doctrine** ("should this animate?"), **Claude Design / design-sync**, and **all
twelve pack names** — a user saying "use the blueprint pack" hit no trigger.

### Reach: the required doc that reached nobody

`MOTION_DOCTRINE.md` is marked **REQUIRED BEFORE ANY ANIMATION**
(`SKILL.md:21-25`) and appeared on **no** install surface: not `README.md`'s
"What gets installed" table, not `bin/cli.js`'s help or success banner, and not
`cursor/rules/sheleg-design.mdc` at all — so a Cursor-rules user got *how* to
animate and never *whether*.

### Where the docs described checks that do not exist

`README.md:231` claimed the validator checks *"both installers' file lists"*.
`install.sh` is checked exhaustively in both directions
(`validate.py:399-408`); the npx installer is checked by
`check("listBundleFiles" in cli, …)` — a substring test for a function name. It
has no file list by design (it walks at runtime), so the claim describes a check
that cannot exist as stated. `DOCMAP.md` rows citing `test/validate.py` as proof
for "add it to the README install table", "all thirteen headings", "a routing
scenario with its negative branch" and "`.prompt.md` beside it" are likewise
unbacked — the last names a file pattern that exists nowhere in the repo.

---

## Part 3 — What shipped in v1.10.0

### Six new mechanical checks, each watched failing

| Check | Catches | Watched saying no |
|---|---|---|
| `validate_counted_claims` | any wrong "N packs / kits / scenarios / headings", whitespace-normalised across line breaks | planted `six locked style packs` |
| `validate_pack_enumerations` | a manifest, command, CLI, README or rule naming a subset of the packs | planted removal of one pack from `plugin.json` |
| `validate_contract_terminology` | the contract called by any name but thirteen | planted `nine-heading` in `CONTRIBUTING.md` |
| `validate_contract_declaration` | a pack that does not declare `Contract: core\|widened`, or declares one it does not match | planted removal of `workbench`'s line |
| `validate_core_vocabulary` | a pack that does not resolve `--bg`, `--ink` and an accent role | — |
| `validate_stated_ratios` | **every stated contrast ratio, recomputed from the token layer** | planted `19.9:1` in `showroom.md` |

The ratio check is scoped deliberately: it only checks a claim whose base the
document *declares* — a table column headed ``On `--bg` ``, an `on/over/against
--token` phrase, or an `--on-X` token name. A first draft that inferred the
partner produced **22 false positives out of 40**, and a noisy gate is one people
learn to ignore. Prose ratios and worst-stop tables (`cyclorama`) are out of
scope and stay out until they declare a base — recorded on the board as B-003
rather than left as an implied capability.

### Gate integrity

- **Ratchet floors** in `test/floors.json`, enforced by all three gates. Defect A
  now fails instead of going quiet.
- **Per-occurrence suppression** in the slop lint, with ban-quoting sections
  exempted *by heading* rather than by hoping a negation word is nearby. Defect B
  now fails.
- **Unknown arguments exit 2** in all three scripts. Defect C now fails.
- **`validate.py` gained a real self-test** — six planted defects, run by copying
  the tree and re-executing the validator against it, so what is tested is the
  file CI runs rather than a re-implementation of it.
- **Inline CSS in packs is now linted**, closing the 16-of-19-files gap.
- **`npm test` and both workflows run every gate and every self-test.** The
  release path was gated on one of three.

**Gate counts: 1270 → 1364, 412 → 469, 224 → 320.**

### Content corrections

All thirteen ratios recomputed and corrected in both homes, kit token prefixes
regenerated byte-for-byte. Every pack declares `Contract: core|widened`, and the
`SKILL.md` routing table marks the six core packs with what they leave to the
reader. The dataviz handoff is written by role with the non-uniform mappings
named. The `atrium` layout transition, the `field-notes` radius rule, the
`blueprint` marks contradiction, the `atrium` shadow count, the copy-pasted
colour-blindness ban in three packs, ADR-0001's example, and every stale count
are corrected — each with a dated note saying what it said before, because the
packs' own rule is *"correct the record here, do not flatter it."*

---

## Part 4 — What is not fixed, and why

On the board (`docs/superpowers/backlog.md`), not silently dropped:

| id | Item | Why it is not closed here |
|---|---|---|
| **B-001** | Widen `instrument-console`, `workbench`, `briefing-room` to the four sections | Their `Origin:` lines name a product, not an address — the sections cannot be sourced without inventing them, which standing instruction 5 and `sloplint.py` both forbid. Needs a public reference or a re-derivation from a live site. |
| **B-002** | The same three packs violate the library's own "no reference, no pack" rule | They predate it. Either obtain references, re-derive, or record an explicit grandfather clause as an ADR. |
| **B-003** | Prose contrast claims and worst-stop tables are outside the ratio check | Checking them needs the document to declare its base. The honest fix is to make those tables declare one, then widen the check. |
| **B-004** | Widen `atrium`, `orchard`, `editorial-luxury` to the four sections | The operator authorised this; their references *are* addressable. It needs live computed styles read from each site, which is a measurement pass rather than an editing pass. The misleading half is already closed by the `Contract:` declaration — a reader now knows what these packs do not answer. |
| **B-005** | 13 of 19 scenarios in `test/scenarios.md` carry no recorded result; 5 of the 6 that do carry a date with no commit | On a repo whose gate count moved 876 → 1270 in a day, a dated claim without a commit is not re-derivable. |
| **B-006** | The skill description has 14 characters of headroom and no trigger for decks, the motion doctrine, design-sync, or any pack name | Widening it changes discovery behaviour, so it needs the full T1 trigger set re-run in fresh contexts — a test pass of its own. |

---

## Part 5 — The pattern worth keeping

Every defect in this report is one of two shapes.

**Shape one: a claim with no owner.** A number, a count, a token name, a heading
count — stated in prose, true when written, and belonging to no file that would
notice when it stopped being true. The fix is always the same and is always
cheap: make the machine derive it, or make the machine check it. Six of this
run's findings became one-line checks.

**Shape two: a check that cannot fail.** A gate whose count falls when you delete
a requirement; a suppression rule that fires on the first match and skips the
rest; an unknown flag that runs the normal pass; a substring test where a
structural test was meant. These are more dangerous than a missing check,
because they are *reported as coverage*.

Both shapes were already known here. The retrospective has recorded the
self-test-that-does-not-exist since 2026-08-05, and the stale-contract-number
since 2026-08-08. What this run adds is that **a finding recorded in a
retrospective is not a finding fixed** — instruction 6 said "every new gate is
watched saying no", and two of three scripts still accepted an unknown flag;
REQ-018 fixed "nine headings" in `DOCMAP.md` and left it in four other files. The
ratchet rule exists for exactly this: the second appearance becomes a script.
This run made both of them scripts.
