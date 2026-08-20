# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow [SemVer](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### The library's contrast coverage was 15 claims smaller than it said (B-013)

`stated ratios: … 336 guarded` counted a claim as covered before computing a single
pair. Fifteen of those 336 had never been through the arithmetic — a claim whose only
named partner is itself (`--ink` in a table declaring `--ink` as its base), or whose
subject is a composite the gate cannot resolve to a solid (`ledger.css:33`'s `--muted`).
**The word `guarded` is gone from the line.** What prints now is what happened:
`513 claims — 348 computed, 15 named a partner this pack cannot pair, 150 unguarded`,
and each of the 15 is listed by `file:line` on every run, because a number nobody can
act on is a number nobody acts on.

**The unguarded set is classified instead of lumped.** 177 said nothing about which of
them a person could close. The split says it: `0 in a table declaring no base, 10
placing the ratio at a gradient stop, 140 prose`. The 27 that sat in five tables closed
by declaring the base each table's own numbers already resolve against — `atrium`,
`router` and `orchard` on `--bg`, `cyclorama` on `--ink` with four cells naming
`--field-2`, `prism`'s components row on `--accent`. No ratio was changed and no base
was chosen: each was found by computing which token produces the numbers already
written. `atrium`'s row also had to spell `--ink-2` and `--ink-3` instead of `-2` / `-3`,
because a shorthand is not a token reference.

**A third guard was written and thrown away, and that is the useful half.** A wrapped
comment leaves the partner alone with the number (`4.40:1 on --bg-deep.`), so reading
the subject off the line above looked like free coverage — a probe said it resolved 7 of
the 15. It did not: the probe accepted a match under *either* comparison mode, so any
ratio above the claim counted as agreement. Inside the gate it produced two false
failures at `ledger.css:33`, where the real subject is a composite and the line above
offers a different token. Substituting a subject is the same act as guessing a partner,
which is what killed attempts one and two. The reason is recorded where the code would
have gone.

### A pack's own semantic tokens were compared against nothing (B-017)

`validate_theme`'s peer set is `STATUS_TOKENS` plus `--accent`/`--primary`/`--cta`, so a
pack carrying meaning in tokens of its own naming was checked by nothing. `field-notes`
exists to render provenance, and all four of its provenance tokens were excluded **by
name**: `--brand-ink` (`[INFERRED]`) and `--witness-ink` (`[AMBIGUOUS]`) are **3.2 apart**
at full colour and **0.8 under deuteranopia** — the two labels a reader most needs to tell
apart, on the pack whose reason to exist is provenance. The dark theme is worse than the
board recorded: `--witness` and `--danger` are **1.2 apart** there, 0.4 under deuteranopia.

**The peer group is now whatever the pack declares**, and none of the three forms is new
syntax — all three already ship:

- the state map in a token layer, `[EXTRACTED] → --verify-ink · [INFERRED] → --brand-ink`;
- a distinctness claim, *"destructive — kept distinct from `--witness`"*;
- the pack's own disclosure that two tokens share a hue family.

What it deliberately does **not** do is infer a set from token names. `--brand` and
`--brand-ink` are one colour's two jobs; `--witness` and `--danger` are two meanings that
share a hue. Nothing in the naming separates those cases, so the pack has to say which it
means.

**A disclosure carries its own arithmetic.** *"One hue family, 2.8 apart"* is an honest
answer only while 2.8 is what the values produce, and `validate_stated_ratios` cannot see
it — that check reads contrast ratios and this is an OKLab distance. Any distance a
disclosure states is now computed, bound to the quantity it names: `N apart`, `N at full
colour`, `N under deuteranopia`.

**No hex moved.** `Origin: graphify.com (2026)` makes these values measurements, and a hue
read off a reference may not be re-stepped. So `field-notes` answers in writing: rust and
red-orange are one hue family by measurement, the provenance state is carried by the
bracketed word and its border, and `--danger` is separated from `--witness` by form — a
filled control, never an inline tag. The sentence *"kept distinct from `--witness`"* was
false at 2.8 apart and is gone; the Bans now say the conflation they forbid is **in role**,
and a new ban forbids a provenance state carried by colour alone. `Three semantic hues and
no fourth` became `three semantic ROLES, and two hue families rather than three`.

**Four false-positive shapes were found by measurement and closed, and each is recorded
where the code is.** A one-tier floor called a pair 19.7 apart at full colour a hard
failure. A substring test let a line about `--witness-ink` excuse `--witness`. A
paragraph-wide bind gave every figure in `cyclorama`'s status bullet to every pair — six
failures against six correct sentences. And two separate regexes cut *"6.4 apart under
deuteranopia"* in half, comparing a deuteranopia figure with a full-colour distance.

### A row that states an instruction instead of a ratio was checked by nothing (B-048)

`validate_stated_ratios` reads a number the document states. A Components row often states
none — it states an **instruction**: *"`--surface-2` fill at 4% ink, `--ink` at 50%"* — and
nothing composited it. `scoreboard`'s secondary button shipped a **10–12px/600 label at
3.16:1** that way, below AA, with every gate green over it because there was no number to
check.

**One sub-claim of the board row was itself wrong**, and the measurement says so: the row
held that 4% ink over the paper *"resolves lighter than the declared `--surface-2`"*. It
resolves **darker** — luminance 0.873 against 0.941 — which is precisely why it pushes the
label below AA rather than above it.

The fix replaces two ad-hoc composites with tokens the pack already ships (`--surface-2`
fill, `--ink-soft` label) **and states the ratio it renders**, 4.55:1. The first version of
the fix did not: correcting the spec moved the pair out of every check, which is the same
trap as B-017, where a false distinctness claim was the only thing making a pair
observable. A correction that removes the claim removes the coverage with it.

**Three behaviours with no token now have one.** `--t-display-sm` 42px and `--t-display-md`
44px carry the headline's two unnamed breakpoint steps; `--label-col` 95px,
`--label-col-narrow` 75px and `--numeral-col-narrow` 70px carry the ledger's geometry, which
the kit had as three `width:` literals and the pack as prose numbers. Every value is the
measured one that was already written down — a token names it, it does not choose it.

### A pair a Components row prescribes was computed by nobody (B-050)

A ratio is checked when the document states one. A Components row usually states none: it
**prescribes a pair** — *"`--accent` fill, `--on-accent` label"* — and its hover and active
cells replace one half of it. `contrast(label, fill)` is derivable at every state of every
component, and nothing derived it. That is how `instrument-console` shipped a pressed label
at 3.06:1 (B-039): the press dimmed the fill and the label stayed.

`validate_prescribed_pairs()` reads the resting cell for a fill and a label, applies each
state cell's `fill →` / `label →` swaps, and holds the result to the AA floor for the row's
type size. 13 rows across 7 packs name both halves and carry 8 state swaps between them.

**Both defects it found sit in the two rows the widened phrasings added:**

- **`maquette`'s leader label is invisible.** The row prescribes `--ink` on a `--model-top`
  fill, and those are the same hex — `#FFF9F4`, **1.00:1** — in the pack whose central rule
  is that type and object are built from one cream. The pack now ships `--on-model`
  (`#151515`, the field's own colour) at 17.49:1, and the token layer says why in the place
  a reader hits it.
- **`prism` sets a `$` prompt in `--ink-faint`** at **2.31:1**, a token its own layer calls
  *"furniture only, never text"*. It is `--ink-soft` at 4.70:1 now — the token that layer
  says *"MAY carry body copy"*.

As the board row predicted, this check could **not** have caught B-039: `instrument-console`
is a core-contract pack with no Components table, which is also why the defect survived
there. 16 rows state half a pair and the count prints on every run (B-059).

### 88 prose ratios joined the arithmetic, and four of them were wrong to (B-003, B-053)

140 stated ratios sat in prose that named no partner, so nothing computed them. They were
not closed by widening the check — a heuristic that guesses the other side is what this
file has thrown away three guards for. They were closed by testing **one hypothesis**
against all 140: *this ratio is against the pack's own field.* **88 agreed with it
arithmetically**, claim by claim, on 77 lines.

Those lines now name `--bg`. Many already said *"on the field"* or *"on the paper"* — the
same fact, written so a machine cannot read it — and the rest said nothing. Coverage went
from `353 computed / 150 unguarded` to **`448 / 57`**, 29% unguarded to 11%.

**Four of the 77 went red on the first run and every one was a real find**, because giving
a line a partner puts its *other* claims under the arithmetic too:

- `blueprint`'s `3:1` is the non-text **floor**, and the word *floor* had wrapped to the
  next line, so `RATIO_SKIP` could not see it. Reflowed.
- `proscenium`'s subject was the words *"Body ink"* — no token — and its *"cool act"* is
  `--panel-2`, which the token layer confirms at **16.49:1**. Both named now.
- `tenor`'s subject sat on the line above its claim, the same shape as the fifteen the
  palette run prints as `unpairable`.

The 52 that refused the hypothesis were left alone and stay on the board, because a claim
whose partner is a panel, a literal the pack does not ship, or a token on the previous line
needs its own answer, not a rule.

### Gate

- **Coverage is pinned, in both directions.** `check_ratio_coverage()` reads
  `validate_palette.py:ratios` from `test/floors.json`: `computed` may only rise,
  `unresolved` and `unguarded` may only fall. A check-count floor cannot see this —
  deleting one `on \u0060--bg\u0060` from a table header moved 27 claims out of the
  arithmetic while every other check stayed put. Watched failing at 348 → 342.
- **Five plants, one per bucket**, so the *classification* is watched discriminating and
  not only the arithmetic: a table declaring a base its numbers contradict, the same
  claim with the base removed, prose naming no partner, a ratio placed at a gradient
  stop, and a named partner whose subject cannot be paired.
- `PARTNER_PHRASE` now reads past a determiner — *"text on the `--accent` fill"* named a
  partner the gate could not see. The regex moved rather than the sentence.
- `ARGUED` lists only terms that can reach it. `RATIO_SKIP` already drops a floor, a
  bound and a rejected candidate one step earlier, so repeating those would have been
  alternatives that never match — which reads as coverage and is not.
- Floor `validate_palette.py` 1924 → 1951, all 27 from the newly-checked table claims,
  then 1951 → 2087 for the declared-set sweep.
- **Four plants for the declared sets, and the third is the point**: a file-wide
  *"never by colour alone"* must NOT excuse a pair below the hard floor. Without it the
  check is a phrase-detector and one sentence silences it.
- A figure with no qualifier is skipped rather than guessed, and the count of
  disclosure figures no check could bind prints on every run (7 today, B-055/B-056).
- The `field-notes` kit's token block was re-copied from the pack's layer, which the
  copy-never-transcribe check caught on the first run after the comment changed.
- **`validate_composited_fill_contrast` composites in sRGB gamma space**, because that is
  where the browser does it. A first draft composited this module's linear values and
  reported 1.88:1 where the page renders 3.16 — wrong in the direction that fails a
  correct pack.
- **Composites are read per CELL.** A Components row is resting | hover | active |
  disabled, and reading the whole row made `cyclorama`'s hover fill the resting chip's
  text colour: 1.26:1 reported against a chip that renders at 12.38:1. There is a plant
  for it.
- Two live subjects, one of each verdict — which is what makes it a check. Measured
  first: 44 lines in the library pair a token with a percentage and only two state a
  composite fill AND a type size. The other 42 are filed (B-058), not guessed at.
- Floors `validate_palette.py` 2087 → 2092, `computed_at_least` 348 → 349.
- **Five plants for the prescribed pairs**, including the hover-swap path B-039 is made of
  and the `as above` inheritance. The fixture had to be corrected before they meant
  anything: it used B-039's own values, where the resting pair already fails, so three of
  the five were passing for the wrong reason.
- A claim added in this change had to be rewritten because `on` and its token landed on
  either side of a line break — the same refusal B-039's own fix met, and correct both
  times.
- Floors 2092 → 2119 and `computed_at_least` 349 → 353.
- **`scripts/sync-kit-tokens.py`, and `npm run sync-kits`.** A kit's `styles.css` is its
  pack's token layer verbatim plus its own component half, so every edit to a token
  layer — down to a comment — makes the kit red until the block is copied again. That
  copy was done by hand three times today and the third touched **15 kits at once**. The
  script takes the block boundary from the file's *committed* version instead of guessing
  it, and a kit that was hand-edited inside its token block reports `STUCK` and is left
  byte-identical. Watched refusing in a worktree, with the component half intact.
- Floors 2119 → 2214, `computed_at_least` 353 → 448, `unguarded_at_most` 150 → 57.

### Fixed

- **1.45.0's release notes were stranded under `[Unreleased]`.** The release commit wrote
  a summary above the accumulated section and left it in place, so the shipped version's
  detail was labelled unreleased and the next entry would have landed on top of it. The
  detail is folded into 1.45.0 below, where it belongs. `validate_release_register()`
  now refuses an `[Unreleased]` heading that is not the first section, and refuses a
  second one — the same class as the duplicate `## [1.35.0]` found on 2026-08-20, one
  heading over, and nothing had been looking at it.

## [1.45.0] - 2026-08-20

**Four packs contradicted their own token layers, and the layer is what an implementer
copies.** `scoreboard` still shipped the `--accent-hover` comment the pack retracted in
1.13.1 — *"the one orange that may carry a link"*; its elevation comment said "two soft
stacks and a hairline" where four shadows ship, called both untinted while one is 16% and
another a blue-black, and left `--shadow-panel` in no prose at all; it banned radii above
8px while `--radius-pill: 999px` ships and its own section tick requires it.
`instrument-console` legislated four statuses and shipped two colours, prescribed a pressed
primary whose label lands at **3.06:1**, and banned "colored shadows besides
`--accent-glow`" while mandating a composite the prose never named. `showroom` gave its
signature specimen frame two different radii in two sections, with a subtraction rule keyed
to the wrong one, and shipped one hex for both `--surface-2` and `--line-weak`, so a
hairline on a sunken well is invisible. `atrium` had the same collision, unrecorded.

**Six sweeps replace nine hand edits, and they found 24 more defects on their first run:**
16 shadow or glow tokens no prose names across 11 packs (`proscenium`'s "Elevation is three
shadows" was four), a card at two radii, three status-map errors, two more hairline
collisions, a press outside the doctrine's band, three missing base layers. The motion band
and the UI ceiling are **parsed out of `MOTION_DOCTRINE.md`** rather than restated, and
`@role drawn-on:` is how a pack declares where a colliding hairline is actually drawn.

Registers that had stopped:

- **Run stamps complete to 1.44.0** — 26 rows reconstructed from `git log`, tags and the
  CHANGELOG, with `Diverged?` left honestly *unrecorded*; a release at or above 1.5.0 with
  no row now fails. The register had stopped at v1.26.0, eighteen versions back, which made
  the "not fired in five run stamps" retirement trigger uncomputable.
- **The palette gate's own numbers**: it claimed 71 of 121 unguarded ratio claims measured
  at sixteen packs and asserted all 71 had been hand-verified. Measured today: **513 claims,
  336 guarded, 177 unguarded at 22 packs** — and the run prints that pair every time, with
  the hand-verification dated for what it was. Two more restated counts went the same way.
- **`package.json` said twenty-nine packs and named 27** — `awning` and `bulletin` missing
  from the surface an npm reader chooses from. It is an enumeration site now.
- **Two `## [1.35.0]` sections** under one version, and four releases in the CHANGELOG with
  no tag. The duplicate is resolved; the untagged four are **reported, not created** — a tag
  nobody has is not this run's to invent.
- **Every pack that bans a weight or a slant owes a base layer** and two of 29 shipped one:
  `<strong>` renders 700 and `<em>` italic with no stylesheet involved, so the ban was
  invisible to a grep over CSS.

Two plants found holes in the checks they were written for, and two bugs the gate found in
itself: one sweep was reading a declaration out of a header comment and silently excluding
a whole pack, and a new check emitted a different number of checks with and without git
tags, which broke the ratchet in its own self-test copy.

**Found by the release, in the release's own gate.** The untagged-release check read
`bool(tags)` as "the whole tag set is visible". A release checkout fetches the released
ref and nothing else, so at `v1.45.0` exactly one tag was present and the other 49 shipped
releases read as untagged — the release went red for a reason with nothing to do with the
release. The same commit passed on `main` because a shallow checkout fetches NO tags, the
check switched itself off, and the difference between *no view* and *a one-tag view* was
invisible. Both are named as partial now, and a partial view is disclosed rather than
answered. Verified against a `--depth 1 --branch v1.45.0` clone, which is the environment
that failed.

Checks: `validate.py` 3398 to **3543**, `validate_palette.py` 1912 to **1924**, `sloplint.py`
635. Ten new plants, all caught; 49 planted defects across the three self-tests, 0 missed.



### Four packs contradicted themselves, and six sweeps now say so

A reader copies the token layer verbatim — every pack's Palette section tells
them to — so when the layer and the prose disagree, the layer wins and the prose
lies. Nine such contradictions were filed by hand across `scoreboard`,
`instrument-console`, `showroom` and `prism`. All nine are fixed, and where the
class repeats it is a sweep with a planted defect rather than nine edits.

**`scoreboard`** shipped `--accent-hover: #e03d00; /* the one orange that may
carry a link */` — the exact permission the pack retracted in 1.13.1, still in
the file a reader copies (B-033). Its elevation comment counted "two soft stacks
and a hairline" over four shadows, called `--shadow-card` untinted when
`rgba(16, 24, 40, …)` is a blue-black, and left `--shadow-panel` in no prose at
all (B-035). Its Bans forbade "radii above 8px" while `--radius-pill: 999px`
ships and the section tick requires it, and cited `font-smooth: never` — not a
legal value of the property the pack sets, and not a property any engine
implements (B-036).

**`instrument-console`** legislated four statuses and shipped two colours, so
`var(--danger)` and `var(--info)` were undefined custom properties — invalid at
computed-value time, falling back with no error anywhere — in the pack that
required them (B-038). Its pressed primary kept a label at **3.06:1**, one row
under its own warning that `--accent-dim` is a fill and not a label (B-039). And
it called `--accent-glow` "the only permitted glow" while mandating
`--signal-glow`, a composite its prose never named — so the pack banned its own
signature motif (B-041).

**`showroom`** specified its specimen frame at `--radius-2xl` in one section and
`--radius-3xl` in another, with a subtraction rule keyed to the outer value, so
every inner radius inherited the 4px error (B-022). It shipped one hex for two
jobs — `--line-weak` and `--surface-2` are both `#edeff3`, which makes a hairline
on the sunken well 1.00:1 — and a comment naming a colour the focus ring stopped
using fourteen releases ago (B-023). Three of its motion values contradicted the
doctrine in the same bundle (B-024). **`prism`** prescribed its CTA press over
`--dur-fast` at 200 ms, past the doctrine's 100–160 ms press band, with nothing
faster in the layer to reach for.

### Six sweeps, twenty-four findings beyond the nine

- **`validate_elevation_tokens_named()`** — every `--shadow-*` and `--*-glow` a
  pack declares is named in the pack's prose. **Sixteen unnamed tokens across
  eleven packs** on its first run; `proscenium`'s own "Elevation is three
  shadows" turned out to be four.
- **`validate_radius_single_valued()`** — a component is given one radius. It
  attributes a token to the noun that FOLLOWS it, so the nesting sentence every
  pack writes reads as one rule per noun. Found `scoreboard`'s card at two radii.
- **`validate_motion_bands()`** — a press sits inside the doctrine's press band,
  a duration literal in prose is not a value the layer already holds, and a
  control stays under the UI ceiling. The band and the ceiling are **parsed out of
  `MOTION_DOCTRINE.md`**, so the gate cannot disagree with the document it
  enforces.
- **`validate_emphasis_base_layer()`** — a pack that bans a weight or a slant
  ships the base rule for it. `<strong>` renders 700 and `<em>` renders italic
  with no stylesheet involved, so the ban was invisible to every grep over CSS
  and to every browser. Two of twenty-nine shipped one; `atrium`, `notation` and
  `field-notes` now do too (B-044).
- **`validate_status_vocabulary()`** — the cross-pack status map in
  `SURFACE_COMPOSITION.md` is a table, compared against every token layer with
  set equality. It was prose, and wrong in three places (B-016's live half).
- **`validate_line_surface_collision()`** in the palette gate — a line token and
  a surface token resolving to the same colour fail unless the layer declares
  `@role drawn-on:`. Found the unrecorded instance in `atrium` and the
  deliberate-but-undeclared one in `maquette`.

### The doctrine took two corrections

"UI motion stays **under** 300 ms" is now "**at or under**", because a control may
sit on the ceiling with a reason and 301 ms is over — and a gate needs a boundary.
And the "hover/entrance motion stays sub-500ms" sentence in `SKILL.md`,
`SHELEG_DESIGN.md`, `README.md` and the Cursor rule was the wrong half of its own
contradiction: it lumped hover with entrance and set a bound that `manpage`,
`tenor`, `bulletin`, `scoreboard`, `field-notes` and `roster` all exceed with
measured values. An entrance is not UI motion, may run longer when the value is
measured, and never gates content.

### Three registers that had stopped describing the tree

- `CHANGELOG.md` carried **two `## [1.35.0] - 2026-08-15` sections** — two runs
  took the number, the tag went to the second, and the loser's notes sat *above*
  the winner's, so a release extractor reading the first match would have shipped
  the wrong notes. One heading now, and the superseded section says what happened.
- `docs/evidence/retro.md`'s Run stamps table stopped at `v1.26.0` while `1.44.0`
  shipped — eighteen versions — so the *has not fired in five run stamps*
  retirement trigger read every standing instruction as dormant. Twenty-six rows
  reconstructed from `git log`, the tags and the CHANGELOG, with `Diverged?` left
  *unrecorded* rather than guessed (B-037, SG-04).
- `validate_release_register()` gates all of it: no duplicate version, a stamp for
  every release at or after `1.5.0`, and a missing tag reported against a declared
  list. **Reported, never created** — a tag nobody has is not a gate's to invent.

### Numbers that were restated instead of computed

- `test/validate_palette.py` asserted "71 of 121 (59%) … all 71 were recomputed by
  hand … nothing is wrong today" at sixteen packs. Counted today: **513 claims,
  177 unguarded (35%) at 22 packs**, and the hand-verification covered 71 of 121
  on 2026-08-12 and has never been repeated. The figures print on every run and
  the comment says plainly which of them was ever verified.
- `test/validate.py` said "the six packs shipped before the widening" (seven) and
  "seven of the ten widened packs" (twenty-two widened). The split is printed now.
- `package.json` said "twenty-nine locked style packs" over a list of **27** —
  `awning` and `bulletin` were missing. `ENUMERATION_SITES` gained `package.json`,
  which is the description npmjs.com renders: its count was already policed and
  the names beside it were not.

### Fixed

- `_root_block()` stripped no comments, so `datasheet.css` — whose header explains
  the reference's rem base with `html { font-size: 8px }` — sliced a
  nine-character root block and was silently excluded from two sweeps. A block
  scanner that reads a comment as code skips exactly the packs whose authors
  explained themselves most.
- `validate_release_register()` emitted one check when `git` could see no tags and
  two when it could, so the check count moved with the environment and the floor
  measured on a real checkout failed inside the self-test's copy. Both branches
  emit two now.

### Gate

`npm test` → **3543 / 1924 / 635**, floors raised in `test/floors.json` with the
delta attributed per function. Ten new plants, all watched being refused; two of
them found holes in the checks they were written for.

## [1.44.0] - 2026-08-19

### Degrade to calm gained an observable

The promise had none. `sloplint.py` asserted only that the **string**
`prefers-reduced-motion` appeared in the doctrine — that the rule was mentioned, not that any
shipped artifact obeyed it. Measured: **2 of 29 token layers shipped no reduce branch**,
including the pack that mandates a particle field.

`validate_reduced_motion()` asserts two things per layer: a layer declaring `--dur-*` or
`--ease-*` ships a `prefers-reduced-motion` branch, **and that branch collapses at least one
time-valued property to ≤1ms**. The second half is the row — doctrine §9 says motion collapses
"to static or instant, not to slower", so a branch that merely names the query satisfies a grep
and changes nothing a reader can feel. Durations are matched **by value, not by name**, so
`paperclip`'s `--t-*` and `instrument-console`'s `--motion-ease` are not read as empty.

`editorial-luxury` and `instrument-console` fixed. Where a motif cannot be reached from a custom
property — a rAF particle field is not stoppable by a duration — the still is now stated for each:
field to one static frame, spotlight to every section lit, instruments fully drawn. 29 of 29
layers now carry a branch that bites. B-040 closed.

### A count hyphenated onto its noun was invisible to the gate that counts it

`docs/DOCMAP.md` said "a fourteen-kit build matrix" against **29** kits, and the counted-claims
guard ran green over that string for weeks: `COUNTED` never matched a number spelled as a word and
joined to its noun by a hyphen. A contributor had already routed around the hole rather than
report it.

The separator is now `[ -]`, **captured and back-referenced**, so a compound is read in one
alphabet or the other and a half-and-half form is not silently accepted; the plural is required
for the spaced form only, because a hyphenated count is a singular modifier by grammar.
Blast radius measured old-pattern-against-new on one tree: the policed set 34 → 36 spans with
**zero false positives**, the whole tree 333 → 384.

The coordination claim is **derived** rather than reworded — DOCMAP now points at the generated
`AGENT_SYNC.md`, and a new check holds the derivation from both ends so the page, the config and
the document cannot disagree.

### Plants

Self-test 16 → 19, each asserting its **message** rather than merely the red — every token layer
is copied into its kit byte for byte, so any edit trips the kit-drift check and a plant would
otherwise report "caught" with the intended check never having run.

## [1.43.0] - 2026-08-17

**The twenty-ninth pack, and the first one whose signature is a defect its reference
ships.** `bulletin` is extracted from [socialchamp.com](https://www.socialchamp.com) by
enumerating all 748 URLs in its page sitemap, fetching every one, and reading the 58
distinct stylesheets they resolve to plus the shared layer its theme ships. What it
takes is the *drawn* elevation — a 1px ink outline over a hard zero-blur ink offset, 185
of them against roughly 50 blurred shadows across the whole site — and the press that
goes with it: a control travels exactly as far as its offset shrinks, so the ink
displaced is constant.

The reference's primary CTA is white on `#ff6900` at 2.89:1, on every one of those 748
pages. That is under WCAG AA for body text and under the large-text floor as well, so no
type size rescues it; the pack keeps the measured hue and darkens it in oklab until white
clears AA. Two more corrections travel with it, and all three are in the pack's Gotchas
with their numbers.

### Added

- **`bulletin`**, from [socialchamp.com](https://www.socialchamp.com) — warm cream paper
  (`#fcfaf4`) cut by three flat pastel bands, one ink (`#464646`) doing four jobs at once
  (text, outline, offset and the dark band), an orange that fills and marks but never
  carries a word, a display face at **800 inside controls above the headline's 700**, and
  **zero tracking at every size** — `letter-spacing` appears seven times in 58
  stylesheets and never on a heading. Widened contract, all thirteen headings.
- **`styles/tokens/bulletin.css`** — the ready-made token layer, with a
  `[data-surface="ink"]` block for the dark band measured off the reference's own dark
  footer, where the outline and the offset both invert to white. Every value is marked
  MEASURED, SELECTED or DERIVED at its declaration.
- **`kits/bulletin`** — the twenty-ninth reference kit: the six-name spine plus
  `StatusDot`, `Rail` (the row of outlined circles that says *many*), `Band`, `Panel` and
  `Skeleton`. Its `styles.css` opens with the token layer byte for byte.

### Changed

- **`MOTION_DOCTRINE.md` — a fourth standalone pack pins its own ceiling.** `bulletin`
  caps `MOTION_INTENSITY` at **3**, the lowest in the library, because the reference's
  entire measured motion budget across 748 pages is an entrance fade, a 0.12s press and a
  0.3s hover: no scroll clock, no parallax, no scrub, no pinning. Its depth is drawn
  rather than animated, and animating the offset is what flattens it.
- **Every count that names the library moves to twenty-nine** — the pack tables in
  `SKILL.md` and `README.md`, both manifests, the CLI banner, the Cursor rule, the slash
  command's by-name fast path, and the core-contract remainder (seven core, twenty-two
  widened).

### Fixed

- **The rail collapsed to a column, and only rendering it showed that.**
  `container-type: inline-size` applies inline-size containment, so an element stops
  taking its width from its contents — on a shrink-to-fit box (a grid item under
  `justify-items: center`, a flex item, an inline-block) `.bl-rail` went to near-zero
  width, stacked one circle per line and fired its own narrow branch, hiding every
  platform name. All three gates were green over it, because a gate reads structure and
  not layout. `width: 100%` is the fix and the reason is now a comment beside it.
  Rendered and confirmed at 1440×1000, including the press: the primary's offset goes
  3px → 1px as the control travels 2px, while the secondary beside it keeps its 3px.
- **Three stale counts in `SURFACE_COMPOSITION.md` that no gate could see.** It said the
  token names were not uniform "across the twenty-one" when twenty-nine packs ship, and
  that the accent is `--accent` "in eighteen" when it is twenty-seven — `--brand` in
  `field-notes` and `--cta` in `orchard` are still the only two exceptions, counted. The
  third was a count of packs carrying an `@role non-text:` colour, which is now stated as
  sixteen token layers because that is what the grep returns.

## [1.42.0] - 2026-08-17

**The twenty-eighth pack, and the first one measured for its tempo rather than its
surface.** `proscenium` is extracted from [mailmodo.com](https://www.mailmodo.com/), read
off live computed styles in a headless Chrome at 1440×1000 and at 390, 768 and 1024 for
the ramp. What it takes from the reference is the *cadence* — two acts, then the same call
to action, again, with one dark act at the middle — which is why it forks against
`showroom` on tempo rather than on look.

### Added

- **`proscenium`**, from [mailmodo.com](https://www.mailmodo.com/) — a white field
  carrying two cool acts and **one deep indigo act at the middle** (`#07061d` to `#2a0b78`
  at 86.41%, stops measured), ink that is an indigo rather than a grey, an electric violet
  at `#5a45fe` filling a control that stays **nearly square at 4px against cards at 16**,
  one family at nine weights, and a framed product panel the fold cuts off. Widened
  contract, addressable origin, every stated ratio recomputed by the palette gate.
- **A reference kit**, with the six-component spine plus `StatusDot`, `Skeleton`, `Frame`
  and this pack's own `Stage` — the one dark act, which the kit's stylesheet teaches to
  strip elevation from any card standing inside it.

### Three values the reference has and this pack declines, each marked at its declaration

- **The rem base.** Mailmodo steps the root font size by viewport — 10px at 390 and 768,
  11px at 1024, 13px at 1440 — and lets every rem follow. It is coherent and it overrides
  the reader's own text-size preference, so the pack takes the *endpoints* (27px→62px on
  the display, 28px→62px on an act heading) and ships them as clamp slopes with a rem term
  in the sum.
- **The heading ink.** The reference sets headings to pure black against an indigo body
  ink. The move is worth keeping and the literal is not: pure black as a field or an ink is
  banned library-wide as an unfinished default and the slop lint fails on it, so the pack
  ships `#05041c` — 20.18:1 on the field against black's 21.00.
- **The amber.** `#9e7613` is 4.15:1 on white, under AA for body text. The hue is the
  reference's; the step down to `#8a6510` (5.32 / 4.91 / 4.68) is the pack's.

`--ok`, `--danger` and the entire dark register are pack decisions rather than
measurements — the reference paints no success and no error state and has no dark mode. The
dark register is derived from the one dark thing the reference does have: the stage act's
own two stops carry the field and the panel.

### Fixed

- **A self-test plant that had stopped finding its target.** The core-contract remainder
  fixture matched `The other \w+ answer all four`; at the twenty-eighth pack the remainder
  became "twenty-one", which a bare `\w+` cannot match, so the plant changed nothing and
  the self-test still reported it as caught. A fixture that cannot find its own target is a
  hole in the gate, and it opens on exactly the release the plant exists to catch.

### Ratchet

`test/floors.json` raised 2422/1287/504 → 3222/1811/615.
## [1.41.0] - 2026-08-17

**A style pack is a token layer and a set of rules. It does not ship a button** — and until
now nothing in this pack said what draws the controls. Twenty-seven packs, no component-layer
doctrine at all: no `shadcn`, no Radix, no headless kit named anywhere in the bundle.

**The default is `shadcn/ui`, asked once per project.** Same discipline as
`ux-foundation`'s Figma question — once, when design work starts, never per screen — and the
answer is recorded beside the style pack. Default **yes**; a project that already has a
component layer has already answered, and migrating one on taste is not a design decision.

### Why it composes rather than competes, and the trap in the seam

`shadcn/ui` is not a theme. It is unstyled primitives plus Tailwind, themed through CSS custom
properties, so it **consumes** a token layer instead of bringing its own look. The pack decides
what `--bg` means; the kit decides what a `DropdownMenu` is.

**The two vocabularies are different, and that is the part worth writing down.** The packs
resolve `--bg` and `--ink` and little else by those names; `shadcn/ui` expects `--background`,
`--foreground`, `--primary`, `--muted`. Map them explicitly in the pack's token file — an
undefined custom property does not error, it silently falls back, which is the same failure
the chart rule already exists for. A kit mounted without the mapping renders in its starter
palette and looks like nobody chose anything.

**The boundary is the pack's own split.** Product UI — dashboards, admin panels, internal
tools, chat and agent interfaces — yes, by default. A scroll-driven landing page — no: there
are no controls to reuse, the work is bespoke scroll and WebGL, and reaching for a component
kit is how a hero ends up looking like a settings screen.

The section decides *whether* and *against which tokens*; the `shadcn` and
`migrate-radix-to-base` skills do the work and trigger on their own words, so their component
docs are not restated here.

## [1.40.0] - 2026-08-17

**A reference sweep has been in this pack since the Lazyweb bridge and could never be asked
for.** `SKILL.md` carries an *Optional — real-world references (Lazyweb, Mobbin, Refero)*
section, step 1 of *How to Apply* says to sweep before any layout exists to defend, and
`DESIGN_SYNC_BRIDGE.md` §4 tells the three servers apart by what each returns — Lazyweb web
products and growth mechanics, Mobbin evenly-spaced preview images per step, Refero visually
similar screens and flows as structure. None of it was in the `description`, so
`нужны визуальные референсы` reached no route.

Two triggers now do, and one of them cost nothing at all:

| Trigger | What it cost |
|---|---|
| `style pack` | **zero** — the description has said *"Product UI through its style packs"* since the style packs existed. The word was advertised and unroutable for as long as this router has had a table |
| `visual reference` / `визуальные референсы` | 42 characters, paid for by compressing two clauses |

**The unqualified word went to `super-ux` instead, on this pack's own rule.**
`DESIGN_SYNC_BRIDGE.md` §4 opens with *"A reference sweep answers what a good version of
this screen contains — sections, hierarchy, content order. It never answers what it looks
like."* Structure is `super-ux`'s ground, so `референсы` routes there (`super-ux` 0.43.0) and
only the visual half lands here. A prompt naming both raises both.

### What was refused, and it is the word the operator actually types

`подбери стиль` reaches nothing and stays that way. Measured against control sentences from
this machine's own vocabulary: the bare `стиль` fires on «стиль кода» and «стиль коммитов»,
the phrase `подбери стиль` fires on both as well because the matcher tolerates a qualifier
between the words, and the English `pick a style` fires on *pick a style guide for python*.
Every form an operator would naturally type carries a second trade, so the route takes the
qualified phrases and lets the ambiguous ones reach nothing rather than the wrong craft.
`вдохновение` was refused the same way — it fires on «вдохновение закончилось».

**Budget, and it was tight before this change.** 948 → 955 characters against a 970 working
limit: 15 free. Two clauses were compressed to pay for it, and one of them briefly took
`heroes` out of the description — which the umbrella's `triggers_test.js` caught immediately,
because `hero` is a routed trigger. The word is back.

## [1.39.0] - 2026-08-17

**Five packs at once, and the library goes from twenty-two to twenty-seven.** All five
were extracted from live references while building one product's landing site and are
ported back here whole: `router`, `daylight`, `notation`, `almanac` and `vitrine`. Every
one is on the **widened** contract, carries an addressable origin, a token layer whose
every stated ratio the palette gate recomputes, and a reference kit whose spine props are
byte-identical to `workbench`'s.

### Added

- **`router`**, from [openrouter.ai](https://openrouter.ai) — and **the first pack in this
  library measured from a running product rather than from a served stylesheet.** A
  near-white field with a trace of blue and white cards standing on that tint, hairline
  seams instead of shadows anywhere, body at 14px and weight 450, one royal blue at 97%
  saturation doing every accent job and none of the chart work. The second reading
  corrected three values the first had wrong, all named in the pack's Gotchas: their
  `--text-xs` is 14px and not 12, the sidebar is 224 and not 244, and the border asymmetry
  that reads as a register decision belongs to `--sidebar-border` alone.
- **`daylight`**, from [taskip.net](https://taskip.net) — a cool portal field with generous
  radii whose whole depth is **one very large soft shadow spent on a single object per
  screen**, Inter Tight 700 tracked negative over Manrope 400.
- **`notation`**, from [twenty.com](https://twenty.com) — a near-white page drawn **entirely
  in hairlines instead of cards**, radii of 2 and 4px, a slab serif held at 300 against a
  monospace, **no bold anywhere**, an ink primary, and one chamfered corner per page.
- **`almanac`**, from [auxia.io](https://www.auxia.io) — **oatmeal paper rather than white**,
  seams at 2px with **no 1px anywhere**, a 104px display at weight 500 set **below a
  line-height of one**, and uppercase mono tags notched through the edges of drawn boxes.
- **`vitrine`**, from [attio.com](https://attio.com) — a white hairline field with a serif
  display, an **ink primary** so the accent stays free to mark what can be read, and one
  framed record with a 1px inset highlight carrying the page's evidence.
- **Five reference kits**, each with the six-component spine plus `StatusDot`, `Skeleton`
  and the pack's own signature component — `LiftPanel`, `Eyebrow`, `TaggedBox`, `Frame`.

### The idiom worth naming: the status triplet

Every status in `router` holds **three** tokens rather than one — `--ok-mark` is painted,
`--ok` is written, `--ok-weak` is laid under. The reference's own delta is drawn in
`#00bf6f` and set in `#007544`: *the colour you paint with is not the colour you write
with.* The `-mark` values are identical in both registers because only the words have to
be read, and the split is what lets a 97%-saturated hue be an accent without becoming an
unreadable label. `StatusDot` ships it as one object with a **required** label.

### What the gates decided, rather than taste

- **`router`'s `--info` was authored as a teal and refused**: 9.0 apart from `--ok` at full
  colour against a hard floor of 10.0 — two semantic states in one colour, which secondary
  encoding does not excuse. The reference had already answered it; its `--color-info` and
  its `--or-royal` are the same hex.
- **`almanac`'s derived `--danger` is a crimson, not a red**, for the same reason: an
  orange-red beside its burnt-orange `--warn` measured 6.4 apart. Moved along the hue until
  it separated at the floor.
- **`router`'s dark `--danger` is not the reference's.** Theirs is 5.02 on the field and
  clears, but **4.38 on its own chip tint** — and a danger chip is where the word most
  needs to be read.
- **`vitrine`'s `--shadow-1` had to be reordered.** Written colour-first the palette gate
  reads it as a colour it cannot compute; written length-first it is the same shadow and
  is checkable.
- **Three packs ship a derived `--danger`** — `daylight`, `notation` and `almanac`, whose
  references are marketing sites that paint no error state. Each is marked derived **at
  the declaration**, so a later reader cannot mistake it for a measurement.

### Two findings from the palette work, recorded in the packs' Gotchas

- **Six chart series will not fit and the arithmetic says so.** Six distinguishable steps
  need about 60 L* of range; the dark end is bounded by usefulness and the light end runs
  into the page, so the palest measured **1.38** against the field. Four is what clears, at
  3.31 light and 4.61 dark. **The number of series is a decision of the palette, not of the
  data.**
- **A monochrome chart palette is the weakest, not the safest** — it holds two series on
  white (3.22) and three on ink (4.25); a third ink step on white lands at 2.72, under the
  non-text floor.

### Changed

- Every counted claim moved from twenty-two to twenty-seven, in all nine sources the
  counted-claims check reads. **The remainder beside the total moved with it** — the stale
  remainder is precisely the failure that check was written for, and it fired once during
  this change, exactly as its own comment predicts.

## [1.38.0] - 2026-08-16

### The routing table stopped being a second copy of the packs

**6203 tokens against a 5000 budget → 4595**, under the 4750 working limit, and
the **description 1021 → 948 of 1024**, which was three characters from the cap
and therefore three characters from being unable to advertise the next routed
trigger at all.

Nothing was deleted. Four sections restated a file `docs/DOCMAP.md` names as
their single home and are now one pointer each — `AI_PRODUCT_PATTERNS.md`,
`FIGMA_BRIDGE.md`, `DESIGN_SYNC_BRIDGE.md`, and the real-world-references rule
that `DESIGN_SYNC_BRIDGE.md` §4 already owns. Two craft sections moved to the
files whose argument they are:

| Moved | To | Why there |
|---|---|---|
| *How they bind* — the calibration dials | `MOTION_DOCTRINE.md` | every rule in it is about what §1's frequency table already cut; the table and the dial belong in one file |
| *Three looks that are defaults, not decisions* | `SHELEG_DESIGN.md` | it is the same argument that file makes throughout — values come from a pack extracted off a live reference, never from taste at the keyboard |

And the style-pack table's **Look** column is one clause per row instead of
three. The table's own preamble says each pack file "opens with its own full
description — this table is for choosing, not for reading instead of the pack",
and the Look column was the part that read instead of the pack. All 22 packs are
still named, which is what `ENUMERATION_SITES` requires of this file.

**The description gave up the Figma prose sentence**, not a trigger: `figma
variables` and `фигма в код` already live in the `Triggers -` half, so the
sentence was the only place that fact had two homes. **All 32 routed triggers
still resolve** (`node test/advertised_check.js` → *advertises all 32*), which is
the invariant B-54 exists to protect.

The `.cursor/` mirror moved with all three files, and the gate compares it in both
directions.

### Fixed

- A pointer written during this change cited `docs/DOCMAP.md` — a **repository**
  path with no counterpart in the installed bundle. The gate caught it, which is
  what that guard is for: an instruction that dead-ends for every reader who did
  not clone the repo.

Found by the nine-repository audit of 2026-08-16 (umbrella `B-66`;
`F-sheleg-design-04`, `-05`).

## [1.37.5] - 2026-08-16

### Changed

**`сделай лендинг` reached no route, and neither did `build a landing page`.** A landing
page is the canonical two-craft surface — how it looks and how it sounds — and the
unqualified ask for one arrived at nothing at all.

Both phrases now reach **`sheleg-design` and `copywriting` together**, which is what the
family's composition order says a landing needs. Verb phrases rather than the bare noun,
and that choice was measured against the alternative rather than argued: with a bare
`лендинг` trigger, `напиши текст для лендинга` picked up a visual route it did not ask for
and `почини баг на лендинге` collected three. With the verb phrase, both stay exactly as
they were — copywriting alone and task-pipeline alone.

Room was made rather than found: `scrubbed sections` and one `implemented` came out of the
prose, which is 30 characters that were not carrying their weight beside a phrase an
operator actually types.

## [1.37.4] - 2026-08-16

### Fixed

**The description was not valid YAML, and every gate this family owns read it with a
regex.** B-56 blamed the launcher for two cycles. The launcher was fine: `description`
carried `style packs: dashboards` — a colon-space inside an unquoted scalar, which YAML
reads as a nested mapping. `claude plugin validate`, this pack's own 4636 checks, the
umbrella's trigger fixture and `claude plugin update` all stayed green, because all of
them match the field with a regular expression. The skills CLI uses a real parser: it
reported *No valid skills found*, the family launcher exited 1 on this member, and the hub
copy every non-Claude-Code agent reads sat on the previous version — refreshed by hand
after each of the last four releases.

Both colon-spaces are gone (`style packs — dashboards`, `the Figma border — tokens as
variables`) and the front matter parses. The regression was introduced by the 1.37.0
rewrite that gave this skill its plain vocabulary, so it shipped and broke installation in
the same release that fixed routing.

**The gate now exists in both places.** `test/validate.py` asks the umbrella's
`advertised_check.js`, which refuses an unquoted scalar containing `": "` — measured
across all 69 scalar lines the family ships, two hits, both this defect. The umbrella runs
the strict form with a real parser over every shipped `SKILL.md`. Watched failing in both.

## [1.37.3] - 2026-08-16

### Changed

**`сделай дизайн лендинга` reached no route at all**, and the word that would have fixed it
is the word that declines the route: bare `дизайн` sits inside «без дизайна», so a trigger
there would make the refusal unsayable. The two-word phrase clears that and is more precise
anyway — `дизайн лендинга` / `design a landing` route here, while `напиши текст для
лендинга` still goes to `copywriting` alone, which the bare noun `лендинг` would have broken.

It **replaces** `"cinematic landing" / "кинематографичный лендинг"` rather than joining it,
because this description had six characters of budget left. The loss was measured before it
was taken: nobody types «кинематографичный лендинг», and `make the hero more cinematic` —
the case that pair was really for — still reaches here through `hero`.

## [1.37.2] - 2026-08-16

### Added

**This gate can now see an invariant it breaks one repository away.** The family umbrella
routes work by matching a prompt against a table in `lib/triggers.js`, and every trigger
there must be a word this skill's own `description` advertises. Nothing here knew that
table existed. On 2026-08-16 `sheleg-design` 1.37.0 shipped green having dropped a phrase
that was still a live trigger, the umbrella found out minutes after the tag, and it cost a
patch release — because the member releases FIRST and the umbrella re-pins after.

`test/validate.py` now asks the umbrella's own checker (`test/advertised_check.js`), which
reads the module the hook itself calls. **No copy of the table lives here**, so there is
nothing to drift. With no umbrella above this checkout — a standalone clone, and CI — it
discloses rather than passing, because a check that cannot look must never read as one
that looked.

Watched refusing a real drop before shipping: every one of the seven members carrying
routed triggers had one of its own advertised phrases removed and every one of them failed
its own gate.

## [1.37.1] - 2026-08-16

### Fixed

- **The 1.37.0 rewrite dropped a phrase a router still fires on.** Rewording the
  description to advertise plain visual words also replaced
  `"figma variables / figma to code" / "переменные фигмы, фигма в код"` with the
  shorter pair — and `фигма в код` is a live trigger in the family umbrella's routing
  hook. A trigger whose skill no longer claims the words is a hook firing on a promise
  nobody made, so the phrase is restored.

  **This pack's own gate cannot see that failure, and that is the finding.** The
  trigger table lives in `sshlg-skills`, not here; `npm test` was green on 1.37.0 and
  the umbrella's `test/triggers_test.js` caught it minutes later. The invariant it
  holds — every trigger is a word the skill itself advertises — is enforced one
  repository away from the file that can break it.

## [1.37.0] - 2026-08-16

### Changed

- **The description now advertises the words an operator actually types.** Board row
  `B-49` in the family umbrella measured it: every one of the fifteen triggers was a
  compound noun phrase — `cinematic landing`, `design tokens`, `dashboard style` — so the
  router that owns the visual layer could not be reached by asking for visual work.
  `сделай paywall красивее` → `[]`. `поменяй палитру` → `[]`. `сделай дизайн лендинга` →
  `[]`. And **`make the hero more cinematic` → `[]`**, because the trigger was the phrase
  `cinematic landing` and not the word.

  A trigger may only be a word this description advertises — the family's own check
  enforces that, which is why the fix starts here. Seven plain pairs are added:
  `palette` / `палитра`, `colors` / `цвета`, `typography` / `типографика`, `font` /
  `шрифт`, `how it looks` / `выглядит`, `make it prettier` / `красивее`, and the
  description is reworded to open with what it is for — *deciding how something looks or
  moves* — rather than with the most cinematic thing it can do.

  **`landing` alone is deliberately not a trigger.** A landing page is copy as much as it
  is visual, and the bare noun would take the route from `copywriting`.

  Measured after, and the instrument matters: routing is a model reading a description,
  not a substring matcher, so the check is *does the description carry a stem the
  operator's phrase contains* — `палитр`, `красив`, `цвет`, `анимац`, `дизайн`, `hero`.
  All seven visual phrases reach one; all six controls — a payment bug, a text for a
  landing page, a production check, a test, a README, a refactor — reach none.

  The first instrument said otherwise and was wrong: it compared exact substrings in a
  language that declines, so `палитра` missed `палитру` and `красивее` missed `красиво`,
  and it tokenised the compound trigger `кинематографичный лендинг` into words and then
  reported the bare `лендинг` leaking onto the copy work it was written to avoid. Three
  false misses and one false leak, all of them the checker's.

## [1.36.1] - 2026-08-16

**1.36.0 added two traps and left the sentence above them saying six.** The Gotchas section
of `awning` opened with "Six traps" over a list of eight, because the edit that added them
matched on a guessed line wrap and the header replacement silently did not apply. Every gate
passed: the repository's counted-claims check counts **packs and kits**, not the things a
pack says about itself.

### Fixed

- The header now reads "Eight traps" and names which five are the reference's — and which
  **two of those five were found only by rendering**.

### Added

- **`validate.py` now checks a pack's stated trap count against its own list.** No other
  pack in the library disagreed, measured; the class was simply ungated.
- **And the check's first draft could not fail.** `NUMBER_WORDS` is keyed lowercase, the pack
  writes "Eight" capitalised, so the lookup returned `None` and every pack was skipped in
  silence — a gate that passes everything, which is precisely the defect it exists to catch.
  Caught by planting the defect and watching for a failure that never came. `.lower()` added,
  re-planted, and watched failing before being kept. 2653 → **2657** checks.

## [1.36.0] - 2026-08-16

**`awning` shipped as a specification and had never been rendered.** Asked whether the
design itself had been done, the answer was no: a pack, a token layer and a nine-component
kit that typechecks, and not one pixel looked at. A page was built in the kit and
photographed, and it produced three findings the token layer could not — two of them
defects in the reference that survived the 1.35.0 release precisely because that release
was read rather than seen.

### Fixed — in `awning`

- **A secondary control's border misses the contrast floor for a control boundary.**
  `--line-strong` `#d4d4d8` is **1.48:1** on white against WCAG's **3:1** for a UI component
  boundary — short by half. It matters more here than it would anywhere else, because a
  secondary button in this system is `transparent` at rest, hover, active *and* disabled: the
  border is not decoration around the control, it **is** the control. `--shade-40` does not
  reach the floor either (2.56:1). **New `--control-border`** `#71717a`, 4.83:1, the first
  step on the ramp that clears it. Found by looking at a "Talk to sales" button beside a
  black pill and seeing it nearly disappear.
- **The second field is declared and a page built from the pack will not use it.**
  `--bg-deep` existed from the first release and the first page rendered ran fifteen sections
  on pure white without touching it, because nothing forces the alternation and white is the
  default of everything. A front door in this register is long; a long page on one field
  reads as one endless scroll. Recorded as a trap with the instruction to alternate by
  section and to spend the change where the argument changes.
- **A `Stat`'s label and its sub were the same grey**, so the number read as sandwiched
  between two equal lines rather than as the thing the block is about. The sub drops to
  `--ink-faint`; the constraint that comes with it — 4.40:1 on `--bg-deep`, so a Stat on the
  second field moves its sub back to `--ink-soft` — is written beside it.
- **A `FeatureRow`'s mono index was top-aligned** against a title set larger, and floated
  free of the line it belongs to. It takes the title's leading now.

### Note

Gotchas went from six to eight, and the header now says which of them were found by
rendering rather than by reading. That distinction is the point of this release: the pack
passed three validators, both `--strict` runs and a typecheck at 1.35.0 with two
accessibility defects in it, and neither was reachable without building a page.

## [1.35.0] - 2026-08-15

> **The number was already in use.** A concurrent run had written a
> `## [1.35.0]` section for `ledger` before this one, and `v1.35.0` tags this
> commit — so the ledger notes moved to a heading of their own, directly
> below. Standing instruction 1 in `docs/evidence/retro.md` is about exactly
> this, and it caught the collision late rather than never.

**A twenty-second pack, and the reference it was asked for did not survive measurement.**
The request was "a pack in the style of taskip.net". Taskip turned out to be WordPress and
Elementor over a bought theme (Xilancer), carrying **three token systems that disagree** —
the theme's declared primary `#6074f6` appears nowhere on the rendered page, the visible
emerald lives in a second sheet, and a third set of values is Tailwind slate. Twelve radius
values, six shadows, seven weights, four font families, and `.3s` / `0.3s` / `300ms` written
as three different things. That is a page-builder output, not a vocabulary, and this library
exists on the premise that a pack is the reference's own vocabulary rather than a
reconstruction of one. It was declined as a source and the register was re-sourced instead.

### Added — `awning`, the twenty-second pack

Origin: <https://www.shopify.com>, read 2026-08-15 from the served HTML plus its six linked
stylesheets. Chosen after measuring five candidates on the same axes; it was the only one
that paired the register with a real system.

- **The accent is black, and it is a resolved chain rather than a stylistic absence.**
  `--color-component-button-primary-bg` → `--color-theme-bg-cta` → `#000`, with hover, active
  and disabled declared beside it. No hue reaches the chrome at all, which is what leaves
  every colour on the page belonging to the product screenshot inside it.
- **A three-tier token layer** — primitives, semantic roles, per-component states — so the
  pack ships the indirection rather than the resolved values. `--radius-component-button:
  var(--radius-theme-full)` is the only place the system says *why* a button is a pill.
- **420 and 550, and no 700 anywhere.** A variable grotesque used as one. Setting a heading
  in 700 here is not a small deviation; it is the one number the system was built to avoid.
- **Tracking crosses zero inside one family** — negative on the display ramp, positive on the
  body ramp, crossover around 1.375rem — where most packs in this library split tracking
  across two faces.
- **Leading ships paired with size in `rem`**, not as a ratio, and the ratio *changes* down
  the ramp: 1.08 at display, 1.12 at t2, 1.30 at t7.
- **One shadow, three layers** — ambient, contact, and a `0 0 2px` hairline edge that is what
  stops a card dissolving on pure white. That third layer is the one people drop when they
  copy a shadow by eye.
- Six Gotchas, three of them defects in the reference: `--ink-faint` at **4.40:1 on the
  system's own second field**; three eases named as tokens against **ten unnamed inline
  durations**; and `ease-in` shipped as a token while the doctrine bans it in UI.
- Routed through all seven surfaces the validator checks, mirrored to `.cursor`, added to
  `install.sh`, and shipped with `kits/awning` — the six-name spine on the canonical API plus
  `ProductFrame`, `PlanCard` and `FeatureRow`.

### Fixed

- `paperclip` and `showroom` now link **back** to `awning`. The validator caught the one-way
  fork: a neighbour reference that only points one direction is a dead end for anyone who
  reaches the other pack first.
- Nine stated counts moved from twenty-one to twenty-two across `SKILL.md`, `README.md`,
  `package.json`, both manifests, `bin/cli.js`, `MOBILE_SURFACES.md`, `SURFACE_COMPOSITION.md`
  and `DESIGN_SYNC_BRIDGE.md`, plus core-contract packs from six to seven. Every one was
  caught by the gate rather than remembered.

## [ledger — shipped inside 1.35.0] - 2026-08-15

> **Two runs took the number 1.35.0, and the tag went to the other one.**
> `v1.35.0` is `e9c0bf6`, the `awning` release below; this section's work is
> `48f24d9`, which carried `1.35.0` in every manifest and was never tagged —
> `git checkout v1.35.0` gets you both, because the ledger commit is an
> ancestor of the tag. Two identical `## [1.35.0]` headings sat here from
> 2026-08-15 until 1.45.0, the ledger one ABOVE the tagged one, so a release
> extractor reading the first match for `## [1.35.0]` would have shipped the
> wrong notes. The heading is no longer a version because the version was
> never this section's to hold, and `validate_release_register()` now refuses
> a duplicate.

**The twenty-first pack, and two counts that had been wrong for eight releases.**
`ledger` was extracted from `basedash.com` — a warm cream console for a product
that answers questions about data. Adding it walked the library past twenty for
the first time, which is where two gates turned out to have been counting with a
table that stopped at twenty and a regex that read one modifier word.

### Added

- **`ledger` — style pack 21 (widened contract, standalone product UI).** Warm
  cream field `#fcf9f5` under `#14100c` ink, elevation as a **1px hairline at 12%
  ink and no shadow on any card**, the reference's ×1.25 radius ramp nested
  concentrically (a 15px track with 4px of padding holds a 10px thumb), an **ink**
  primary button, and a terracotta `#c2410c` that **never fills a control** — of
  eleven accent-coloured elements on the reference, five are a 10px monospace
  uppercase kicker and none is a button. 32px data rows in the system monospace;
  the large figure on a stat tile is the UI face at 34px, not the mono, which is
  what the reference actually does. Light `:root` plus a `[data-theme="dark"]`
  twin whose alpha ramp is a different set of steps rather than the light one
  inverted.
  - **Signature element: the seal in a card's title row** — `Verified` /
    `Inferred` / `Unverified`, linking to the proof. It is
    `AI_PRODUCT_PATTERNS.md` §4's provenance tag applied to a card instead of a
    span, and it maps onto three tokens the pack already ships, so implementing
    it adds no hue.
  - **`--warn` is derived and says so at the declaration**, per the template's
    rule 3: the reference declares an amber in its theme layer and never paints a
    warning. The step differs per theme because at amber-500 the *dark* accent and
    the warning are 7.1 apart at full colour — one colour with two meanings, below
    the hard floor. amber-300 is 16.2 apart and clears every dichromacy.
  - **`--chart-1` … `--chart-5` are named for shadcn/ui**, so a Recharts series
    reads the pack's chart ramp through `ChartConfig` with no adapter.
- **`kits/ledger`** — twelve components: the six-name spine plus `Seal`,
  `Kicker`, `DataTable`, `SegmentedControl`, `StatusDot` and an `EmptyState` that
  carries the capability and two runnable example questions.

### Fixed

- **The counted-claims gate could not count past twenty.** `NUMBER_WORDS` stopped
  there, so every correct "twenty-one packs" was read as **"one packs"** and
  failed, in nine files at once. The table now runs to thirty, the alternation is
  longest-first, and a lookbehind refuses a match that starts mid-compound. Two
  planted-defect fixtures had the same hyphen blindness and one of them had
  stopped mutating anything — a plant that changes nothing reports BROKEN, which
  is how it was found.
- **A count with two modifier words was never read as a count at all.** The regex
  allowed one of `visual `/`style `, and both manifests say "pluggable **visual
  style** packs". Widening it to `*` immediately surfaced two stale numbers: the
  plugin description said **twenty** on the day twenty-one shipped, and
  `marketplace.json`'s own top-level description had said **thirteen** since the
  thirteenth pack — eight releases, in the two files an agent host reads first.
- **The core-contract paragraph's two regexes matched `\w+`**, so a hyphenated
  total failed to parse and the check reported the paragraph missing rather than
  wrong.

### Known limitation

- `validate_pack_enumerations` tests membership by **substring**, so `ledger`
  passed in four files that merely described `scoreboard` as carrying "a dark
  ledger". The four were filled in by hand and are now genuinely exhaustive; the
  check that would have caught it — a name in a context that routes to it — is
  not written.

## [1.34.0] - 2026-08-15

**The pack was applied correctly and the result still read as somebody else's typography.**
Everything measured green — zero radius, zero shadow, two hues, AA on every pair — and the
dashboard was flat. This release is what the flatness turned out to be, and most of it is a
correction to the `### On a product surface` section shipped two versions ago.

### Fixed — in `tenor`

- **"A dashboard has no display type" threw away the rule that makes this pack legible.** The
  section rhythm is a page value and stays out; the *tracking rule* is not, and it only acts on
  type large enough to show it. A screen title at 30px tracked `-0.02em` is the rule acting on
  nothing. The section now separates the **ramp** (out) from the **rule** (in) and gives the three
  steps a dashboard actually has — screen title, section head, metric — with sizes, tracking and
  line-height for each. All three at weight **400**: ranking by size is this pack's device and
  ranking by weight is the one it replaced. Measured against a ramp of 30 / 16 / 13, where the
  jump from title to section head was **3:1 with nothing between** — two sizes that far apart stop
  reading as a hierarchy.
- **A stat row built as four bordered boxes breaks the inversion.** `## Components` already said
  three equal blocks share one lattice and never read as three cards; what it did not say is that
  the construction is load-bearing on a product surface. Container draws top and left, each cell
  draws right and bottom, **gap zero**. Build it with boxes 12px apart and the hover inversion
  leaves a seam down every border it touches.
- **A colour earns its place where the column varies, and the chip rule only covered half of it.**
  1.32.0 dropped the box from a chip repeated down a table; the hue stayed. Measured across twenty
  routes: on the agent-connections screen, **82 rows all reading `ACTIVE` and 421 green marks**,
  none of which told the reader anything, because a value that never changes is not a status. Two
  screens away the audit log spends the same green across 200 rows against the warn value and it
  carries the whole distinction. Set the severity value only on rows that differ from the column's
  norm; leave the norm in `--ink`.

### Added — in `tenor`

- **The motion budget of a product surface, stated.** Every motion token in this pack is a page
  value — a 640ms fade, an 820ms travel, a 110ms stagger four steps deep — spent on a block a
  reader scrolls to once. `MOTION_DOCTRINE.md` §1 puts a dashboard's screens in the row where
  animation is cut to the floor, so **the entrance budget on a product surface is zero**: nothing
  plays on load, on client navigation or on a keystroke. What remains is the whole budget and it is
  enough — the cell inversion, the nav underline, the focus ring, the fill on a hovered control.
  Each is caused by the reader's own pointer, which is what makes it read as a response rather
  than as a delay.

## [1.33.0] - 2026-08-15

**Three things the pack asserts that a running page disproved.** Same dashboard as 1.32.0,
audited a second time — but by walking the **computed styles of every element** rather
than by re-reading the source. That is the difference this entry is about: all three
findings are invisible to a grep over the stylesheets, and two of them are invisible to
the stylesheets entirely.

### Fixed — in `tenor`

- **The second-hue ban was being broken by the pack's own token, on every render.** Bans
  said "the orange is the entire chromatic budget", flatly, while the Palette section
  three hundred lines above derived `--good` and explained why a product surface needs it.
  Measured on a live screen, hue 150 appeared **36 times on one page** — checklist marks
  and success chips. The ban now names its exception and states the real rule: no hue you
  did not find in this file, and the only two in it are the orange and `--good`.
- **Two bans the browser breaks for you, with no stylesheet involved.** `<strong>` renders
  at **700** against "no weight above 500" and `<em>` renders italic against "no italics".
  Neither appears in any CSS, so neither is greppable and neither surfaces in review;
  both were found by reading computed styles. `tokens/tenor.css` now ships the three-line
  base layer, and emphasis resolves the pack's own way — by **value**, not by weight or
  slant. **Every pack in this library that bans a weight or a slant owes the same block**,
  and none of the twenty ships one; filed as `B-044`.
- **The 25px orange rule conflated a measurement with a limit.** It is the size of the
  reference's investor lockup, not a threshold derived from anything, and a product's own
  lockup will not be 25px. The rule it stands for is *one small resting orange object per
  screen*; the entry now says which half is which.

### Added — in `tenor`

- **`--data-rest`**, a role over the value ramp the staircase already spends — `--stair-3`
  on the paper (3.37:1 on `--bg`, over the non-text floor) and `--ink-faint` on the band.
  It exists because this pack has **one border weight**: a design system carrying
  `--border` and `--border-strong` as two steps collapses both onto `--line` here, and a
  chart that reached for the stronger of the two paints its resting bars in the exact
  colour of the rule between its own rows. Measured on a dashboard's account table — the
  two resolved identically and the bars matched the row separator to the byte. Nothing
  errors, because both names resolve; that is the failure mode.
- The `### On a product surface` section gains the chart rule, and repeats the standing
  instruction that charts in any pack go through `dataviz` first.

### Note

Two contrast claims in this diff named `--line`, which is declared with alpha and is
therefore dropped from the validator's solids — so no claim naming it can ever be checked.
`validate_stated_ratios` caught the one that sat on a checkable line and stayed silent on
the one that did not, which is the hole `B-003` already describes. Both are now written as
arguments with their resolved hex rather than as measurements.

## [1.32.0] - 2026-08-15

**The pack met a product surface, and three of its own measurements did not survive
the meeting.** `tenor` was mounted on a populated twenty-route dashboard behind a
`?pack=` switch — the "mount them, don't imagine them" procedure `SKILL.md` prescribes
— and every finding below came from a screen with real data on it rather than from a
re-read. Each is reproduced by a number the token layer now carries and
`validate_stated_ratios` now checks.

### Fixed — in `tenor`

- **The reference puts the wrong label on its own accent, and the pack copied the
  workaround instead of the fix.** Gotcha 3 measured `--paper` on the orange at 3.02:1,
  correctly, and concluded that a control whose label is its only statement must keep
  its ink fill and move its *border* to the accent. It never measured the other
  direction: `--coal` on the same orange is **5.84:1**. `--accent-ink` is the coal now,
  declared once and deliberately not overridden on the dark band — the orange does not
  change between fields, so neither does the only label readable on it. The hover fill,
  which is this pack's most recognisable interaction, is legal after all.
- **Gotcha 1's remedy was short on the pack's own second field.** It said to darken
  `--ink-soft` "to at least `#6f6f6b`", which clears 4.67:1 on `--bg` and only **4.27:1**
  on `--bg-deep` — a field the pack spends on a whole section. A remedy nobody
  re-measures is a defect with a citation attached. **New `--ink-soft-aa` `#6b6b67`**:
  4.95:1 and 4.53:1, the smallest step that holds on both. `--ink-soft` keeps the
  reference's value and is now marked for the tracked mono labels, not for prose.
- **`--warn` is the accent, and a product surface sets warn as a word.** At 3.02:1 the
  orange cannot carry one. **New `--warn-ink` `#94400f`** — the same hue on the value
  axis, 6.47:1 on `--bg` and 5.93:1 on `--bg-deep`. `--warn` stays the mark (the dot,
  the edge rule, the fill); the two are one severity in two roles, which is the split
  `--sev-ask`/`--sev-limit`/`--sev-never` already models. On the dark band the orange
  clears AA unaided, so `--warn-ink` remaps back to the accent there.
- **The dark band's `--bg-deep` resolved to the field it sits on.** Correct for a band,
  which has no hover and no resting chip; a rule that silently does nothing on a product
  surface, which has both. Derived to `#222221` — paper at 8% over the coal, 1.20:1
  against `--bg`, and `--ink` 14.73:1 / `--ink-soft` 6.31:1 / `--good` 7.07:1 on it.

### Added — in `tenor`

- **`--coal`**, beside `--paper`. The pack has two materials and named only one, which is
  why the dark band restated `#f7f6f2` as a literal that then had to agree with the light
  block by hand. `--ink` is `var(--coal)` on the paper and `var(--paper)` on the band.
- **`### On a product surface`**, inside `## Components`. Five things a marketing page
  never exercises, each derived and each found on the dashboard: no dark theme exists and
  a product with a toggle has to pick one of three answers; ranking by value costs the
  link its affordance, and the pack's own flipped-origin rule is the fix (static
  underline in a table — fifty animated rules is the marquee ban in another costume); a
  rail's selected row is the lattice cell's inversion held open; **a column of chips is
  where the single hairline stops separating**, which makes the Register's "not for dense
  operator chrome" specific rather than a blanket refusal; and prose sits on two fields
  at once. What does not change: the spacing scale and the type ramp, which are page
  values.

### Note

`--bg-deep` on the dark band was written into this changelog's draft as 1.41:1 against
`--bg` and is **1.20:1**. The number was asserted rather than computed, and
`validate_stated_ratios` caught it before the commit — the check earning its keep on the
run that extended it.

## [1.31.0] - 2026-08-14

**T29 ran, and the pack it was written for did not survive it intact.** Both branches
green — the routing worked — and the pair returned forty-one findings, twenty-six of them
against `paperclip`, a pack that had passed all three gates three times. Every one was
reproduced before an edit; every one is fixed here.

### Fixed — in `paperclip`, found by T29a

- **`--cream` was prescribed and never declared.** The dark primary button's hover was
  specified to keep its label and border at `--cream`, a token this pack does not ship. It
  means `--accent`, and now says so.
- **The dark card hover was a no-op.** A card rests at `--surface` and the hover was
  written as `--surface`. A card and a grid cell are now separated: the cell rests at
  `--bg` and hovers one step toward the card's fill; the card does not hover at all.
- **`--terminal-dim` at 2.92:1 was the label of a tab a reader has to click.** Repaired to
  `--terminal-mid` (5.64:1). `--terminal-dim` survives for the prompt glyph, which is
  `aria-hidden` punctuation, and now carries an `@role non-text:` note saying so.
- **`--shadow-alert` was a second resting shadow in a pack that claimed one** — and it
  hardcoded the reference's **light**-theme amber into a value only ever painted on the
  dark field. Derived from `--warn` with `color-mix()`, and the Texture section now names
  both shadows.
- **All three stagger formulas hardcoded `.14s`.** Zeroing `--stagger` under reduced
  motion would have left every one of them running. They spend `var(--stagger)` now, and
  the pack says why in the sentence that used to say "change it in one place".
- **The reduced-motion blanket had no mechanism for half of what it promised.** The
  marquee and the two 1.5s trace loops are literals inside `animation` shorthands, which no
  token can zero. The pack now ships the rule block beside the token list.
- **The signature element's generation rule did not reproduce its own artwork.** The
  bottom stop was stated at −10.3°/step and does not land on the last capsule; the value
  implied by the anchors is **−10.45°**. "Near-constant saturation and lightness" was true
  of the top ramp (S 96→84, L 56→48) and false of the bottom (S 96→69, L 56→33) — the
  bottom stop darkens as it turns, which is what keeps the curtain's lower edge off the
  field. Both ramps are now stated separately, and "forty-five gradients" no longer sits
  two sentences from "every capsule is filled with its own": a column carries twelve and
  the eight columns reuse the ramps, four of them in reverse.
- **The concentric-radius rule was arithmetically wrong about a nest that does not exist.**
  `8 − 2 ≈ 4.8` is 6, and the reference's tab group sits inside a header with no radius.
  The rule is now declared as the pack's own decision, with a worked example that computes,
  and the reference's actual behaviour — pick by element size, no arithmetic — recorded.
- **`--radius-lg` was called "never spent" and is spent five times**, on the three large
  mock panels. `--radius-md` is the rung that is never spent.
- Smaller, and all reproduced: the artwork called 1200px *tall* where 1200 is its frame's
  width (it is a 560 × 630 curtain in a 1200 × 675 frame); "nothing in this pack overlaps"
  in a pack whose hero is an overlap; a 1.5 line-height floor claimed against a display
  ramp that runs 0.98; `--font-serif` and `--font-sans` named as if the layer declared
  them; an icon range of 14–16px that excluded the pack's own 11px nav glyph; a mono ramp
  called width-invariant beside an axis mark that steps at 768px; a Gotchas count of seven
  where eight are defects; the grain's 512-unit filter in a 256px tile, which is the
  reference's own arrangement and doubles the effective frequency to ~5.9 — now stated with
  its consequence rather than repaired; weight 450 prescribed in a pack that documents 450
  as unrenderable; and an invented "roughly 22 characters per line", replaced by the two
  lines the reference actually sets.

### Fixed — in neighbours, found by the same run

- **`ora`'s merge-time fork clause called this pack "three grotesques and a monospace".**
  It is two grotesques and a monospace; the pack's own Bans cap it at three families.
- **`SKILL.md` marked three packs `(standalone)` and its ceiling paragraph named four.**
  `ora`, `tenor` and `paperclip` all declare standalone in their own Registers and all
  three pin a ceiling — 4, 4 and 5 — that the paragraph never mentioned. An agent choosing
  any of them off the table alone would have taken `MOTION_INTENSITY` 7 from the marketing
  row. All three are marked and all three ceilings enumerated.

### Added

- **`--terminal-dot`, `--mark-rest`, `--scrim`** — three colours the pack spent as literals
  in its Components section. `--scrim` is `#0a0a0a8c` in **both** themes, because the
  reference veils a light modal in coal too, and it stays a literal because the palette gate
  cannot compute a `color-mix()` into `transparent` — and an unparseable token is a failure
  there, not a skip.
- **`--t-hero-art` and `--t-hero-copy` in the Motion tokens table**, which shipped in the
  token layer and appeared only as prose. The table is now the whole set.
- **B-038 … B-043** — fifteen findings against `instrument-console` from T29b, filed rather
  than fixed because they belong to a shipped pack this run does not own. Four reproduced
  first: zero `--danger`/`--info` tokens against Bans that legislate for four statuses; a
  pressed primary label at **3.06:1**; one of only two token layers with no
  `prefers-reduced-motion` branch, in the pack that mandates a particle field; and a Bans
  line that forbids coloured shadows "besides `--accent-glow`", which is a colour.

## [1.30.0] - 2026-08-14

> **Never released on its own.** There is no `v1.30.0` tag and no `1.30.0` on npm,
> so `npm install sheleg-design-skill@1.30.0` and `git checkout v1.30.0` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

A twentieth pack, **`paperclip`**, extracted from a live reference rather than composed:
<https://paperclip.ing>, read from the two shipped stylesheets
(`/_next/static/chunks/0sw-z-v7xc9dd.css`, 622 rules; `/_next/static/chunks/19xj4kovk13jy.css`,
712 rules), the hero's inline SVG and the `@font-face` block. It is the first pack whose
thesis is that **colour is ornament**: there is no functional colour anywhere in the
interface, and the whole chromatic budget is spent on two things a reader cannot click.

Authored on `feat/paperclip-pack` in a dedicated worktree while another run held the
`PACK-TENOR` lease on the shared checkout, per `docs/DOCMAP.md`. That run landed `ora` and
`tenor` as 1.29.0 while this branch was open — including the version this branch had
already taken — so the merge moved it to 1.30.0 and recounted every site from eighteen to
twenty. Nothing was lost in either direction; the counted-claims gate named all eleven
sites that needed moving.

### Added

- **`styles/paperclip.md` + `styles/tokens/paperclip.css` — widened contract, all thirteen
  headings.** A neutral coal field (`#0a0a0a`) with `#fafafa` ink at 18.97:1, and a light
  twin on pure white at 19.80:1 that has **no elevation step at all**: the reference sets
  `--background` and `--card` to the same white and separates a card from the page with a
  1px rule and nothing else.
- **The accent is the inverted field, and colour is ornament.** Every control is
  monochrome — `.navbar-cta`, `.hero-btn-primary`, `.sim-submit` and `.cta-btn` are one
  component wearing four names — and the pack's central rule is one sentence: a gradient
  that can be clicked, hovered or focused has left the pack. The corollary is what makes
  the four status hues land: because colour is spent entirely on things that do nothing,
  anything coloured reads as scenery.
- **The capsule curtain as the signature element.** 96 capsules in 8 columns on a 70px
  pitch, each 70 × 170 at `rx: 35`, stepped 34.5px so every capsule covers all but a
  34.5px band of the one above it. The 45 gradients filling them are **generated, not
  chosen**: the top stop rotates forward around the hue wheel by ~12.4° per capsule and
  the bottom stop backward by ~10.3°, at near-constant saturation and lightness — so the
  stops stay near-complementary and each column inverts its own gradient between its first
  capsule and its last. Measured across all 45 gradients and 89 distinct stops.
- **One noise recipe, on every saturated surface and nowhere else.** `fractalNoise`,
  `baseFrequency 2.95`, 5 octaves, seed 9, tiled at 256px under `isolation: isolate` with
  `mix-blend-mode: overlay` — 12% on a section badge, 86% over the artwork through an
  alpha mask of the capsules themselves. The same seed on both, which is why a
  twelve-gradient page does not band.
- **Twelve section-badge gradients, each with its own hand-picked label ink** — white on
  six, and `#2a1530` / `#3d3010` / `#1a2a40` / `#2a2340` / `#1a3a38` on the five light
  ramps, because a 90° gradient has two ends and one label has to clear both.
- **`kits/paperclip/` — the React reference kit**, the six-name spine plus seven signature
  components: `CapsuleCurtain`, `SectionBadge`, `HairlineGrid`, `OrgNode`, `LedgerRow`,
  `ScheduleLane`, `Terminal`. `src/styles.css` opens with the token layer byte for byte,
  and four of the seven carry `container-type: inline-size`, so no component in the kit is
  sized by the screen.
- **`T29` in `test/scenarios.md`** — the operator register and its fork against the
  console, with the negative branch, and a second rejected pack because `ora` now sits
  inside the same silhouette. **Written and not yet run**, and the scenario says so in its
  own Result line rather than in a footnote.

### Fixed — in the pack, against its own reference

- **`--info` is derived and marked derived.** The reference's dark block overrides five
  status *icon* colours and leaves the four base status colours at their light values, so
  `--status-task-in_progress` renders at **3.83:1** on the coal field and is set as text
  (`● 1 live`). The pack ships `#60a5fa`, the 400 step of the same ramp, at 7.79:1.
- **The focus ring is kept.** The reference's one text input sets `outline: none` on focus
  and replaces the ring with a 1px border colour change.
- **Two 1.5s infinite loops are stopped under `prefers-reduced-motion`.** `dotPulse` and
  `statusBlink` survive the reference's own reduced-motion blocks, which do calm the hero,
  the parallax, the marquee tracks and the modal.
- **The budget bar animates `transform: scaleX()`**, not `width` for 1.2s per bar with six
  bars in view.

### Changed

- **Four reciprocal fork clauses.** `instrument-console`, `workbench` and `orchard` each
  gain one against `paperclip`; `ora` and `paperclip` gain the pair in both directions,
  which is the one edge no gate could have asked for — neither pack existed in the other's
  tree, so `validate_fork_reciprocity()` had nothing to check. The two are the closest in
  the library: both dark by default, both refusing a brand hue, both spending the accent as
  the inverted field. Three tests separate them, and both packs now carry all three.
- Counts moved from nineteen to twenty in the README, `bin/cli.js`, the three manifests,
  `SURFACE_COMPOSITION.md`, `MOBILE_SURFACES.md` and `DESIGN_SYNC_BRIDGE.md`; the
  `@role non-text:` tally is recomputed (fourteen of twenty, from thirteen of nineteen) and
  the accent tally with it (eighteen, from seventeen).
- `/sheleg-design`'s by-name fast path said "the fourteen are" over a list of nineteen —
  a count no gate reads, because it has no counted noun after it. It now says twenty and
  lists them.
- `SKILL.md`'s core-contract paragraph: six of the twenty, the other fourteen.

## [1.29.0] - 2026-08-14

A nineteenth pack, **`tenor`**, and the first one in the library extracted from a
**hand-authored stylesheet** rather than a compiled bundle: <https://heytenor.com> ships
33,822 bytes of CSS somebody wrote, so the token names, the ratios between them and the
reasons they exist were all legible in the source instead of having to be reconstructed.

### Added

- **`styles/tenor.md` + `styles/tokens/tenor.css` — widened contract, all thirteen
  headings.** Warm paper `#f7f6f2` under near-black ink at 17.61:1, **zero `border-radius`
  and zero `box-shadow` in the entire reference**, and one border weight for the whole
  system. The colour argument is the pack: at rest the page carries a single 25px orange
  square, and every other appearance of the accent is a hover fill or the focus ring — a
  page in this pack screenshots with no colour in it at all.
- **Severity as value rather than hue.** The reference's guardrail chips settle it in one
  row: ALWAYS ASK is the orange, LIMIT is a grey, NEVER is the ink, and the *word* carries
  the meaning in all three. The pack ships `--sev-ask` / `--sev-limit` / `--sev-never` as
  the primary system; `--warn` is the accent and `--danger` is the ink, so `--good`
  `#296b46` is the only value in the pack the reference does not contain, and it is marked
  DERIVED at its declaration.
- **Type: two families, two weights, and tracking that runs both ways.** The sans is held
  at weight 400 and tracks negative, tightening to `-0.065em` on the hero; the mono is 500
  and tracks positive, opening to `0.12em` on the smallest label. Display line-height goes
  **below one** — 0.91 at a `12ch` measure — which is what turns every heading into a
  three- or four-line stack.
- **`kits/tenor/` — the React reference kit**, the six-name spine plus seven signature
  components: `Staircase` (the signature element, typed as a **four-tuple** so the value
  ramp cannot grow a fifth rung), `SplitHeadline`, `Lattice` + `LatticeCell`, `FilmFrame`,
  `Guardrail` and `Eyebrow`. Every breakpoint in `src/styles.css` is a `@container` query;
  `FilmFrame` deliberately does not call `play()`, because the page owns the motion policy
  and a kit is the static half of a pack.

### Changed

- **The library is nineteen packs**, and every counted claim moved with it: `SKILL.md`
  (the routing table, the core-contract split — six of the nineteen, the other thirteen —
  and the token-vocabulary note), `README.md`, `bin/cli.js`, `install.sh`, the three
  manifests, the Cursor rule, the slash command, `MOBILE_SURFACES.md`,
  `SURFACE_COMPOSITION.md` (`--accent` in seventeen packs, `@role non-text:` in thirteen of
  the nineteen) and `DESIGN_SYNC_BRIDGE.md` (nineteen kits).
- **`blueprint` and `roster` fork against it, reciprocally.** `blueprint` also refuses
  radius outright and also builds from hairlines — the tell is the marks, since it draws
  registration marks over a visible grid and `tenor` has neither. `roster` also spends one
  orange on a light field and also forbids it from carrying a word — it argues *who
  already uses you*, where `tenor` argues *how the work is organised*.
- **`bin/cli.js` now names `ora` as well.** The enumeration gate had passed it since
  1.28.0 because `ora` is a substring of `cyclorama` — the under-reporting the machine's
  own notes warn about, found by the same check failing honestly on `tenor`.
- **Ratchet floors raised** to 2294 / 1156 / 478, purely additive; all three self-tests
  still catch every planted defect.

### Six defects in the reference, recorded in the pack rather than copied

- **`--ink-soft` is 4.16:1** on the paper and carries every lead paragraph at 16px, which
  is not large text — short of AA by a margin no one notices and every audit finds.
- **`--ink-faint` is 2.36:1** and carries the grey half of the hero headline at 40.8px to
  74.4px, below even the 3:1 that large text is allowed.
- **The accent clears its non-text floor by 0.02**, and contrast is symmetric — so a paper
  label on an orange fill is the same 3.02:1. Both of the reference's orange-filled
  elements put a label below the large-text threshold on it, including **every CTA at the
  moment it is hovered**, where the label falls from 17.61:1 to 3.02:1.
- **A variable font is loaded across two axes and used at one point**: Instrument Sans is
  requested as `wdth,wght@75..100,400..600` against zero `font-stretch` declarations, zero
  `font-variation-settings` and exactly one weight in 33,822 bytes.
- **The mobile panel ships the pre-`dvh` viewport unit as its base** with a `@supports`
  upgrade, so it jumps on every browser that lacks the upgrade.
- **Seven display selectors carry hand-written `<br>` tags** whose visibility is then
  managed at 620px, and one of them appears in both the hide rule and the re-show rule.

## [1.28.0] - 2026-08-14

> **Never released on its own.** There is no `v1.28.0` tag and no `1.28.0` on npm,
> so `npm install sheleg-design-skill@1.28.0` and `git checkout v1.28.0` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

> Authored and gated on its own, **released inside `v1.29.0`**: the `tenor` pack followed
> it in the same session before a tag was cut, and splitting the two after the fact would
> have produced an intermediate commit whose ratchet floors no longer matched its own
> tree. There is no `v1.28.0` tag; this section is the record of what it added.

An eighteenth pack, **`ora`**, extracted from a live reference rather than composed:
<https://ora.ai> and <https://journey.ora.ai>, read from the shipped stylesheet
`/_next/static/chunks/feb8eaf5618096ba.css` and the route bundles beside it. It is the
first pack in the library whose **default theme is dark** — because that is the
reference's own arrangement, which paints its dark values on
`:root:not([data-theme=light])`, so an unattributed root is dark.

### Added

- **`styles/ora.md` + `styles/tokens/ora.css` — widened contract, all thirteen
  headings.** A warm coal field, cream ink, and **no third hue**: the accent is the
  inverted field, which the reference names out loud as
  `--accent-signature` / `--accent-signature-foreground` and spends as
  `bg-foreground text-background` on its one primary action. Both themes ship: coal
  `#141210` with cream `#f7f2e5` at 16.72:1, paper `#f9f7f2` with `#1a1a1a` at 16.26:1.
- **Two families and one of them is a serif doing the sans job.** `--font-sans`,
  `--font-serif` and `--default-font-family` all resolve to Lora, so there is no sans
  anywhere in the system; Space Mono carries every machine fact. The rule the pair
  encodes — a serif means a person said it, mono means a machine reported it — is what
  the whole page is read through, and the pack bans adding a sans for that reason.
- **`kits/ora/` — the React reference kit**, the six-name spine plus six signature
  components: `Verdict` (the signature element), `LayerBar`, `Terminal`, `StepLog`,
  `SectionRule`, `StatusDot`. `src/styles.css` opens with the token layer byte for byte;
  every breakpoint in it is a `@container` query, so no component is sized by the screen.
- **The verdict numeral as the signature element.** One number in the display serif in
  its grade colour, a hairline `/ 100` at half its size, and the letter plus the word
  beneath. `grade` and `label` are **required props** on the component, which is the
  palette rule made into an API: under deuteranopia `--good` and `--danger` separate by
  6.5 in dark and 7.4 in light, below the 8.0 CVD floor, so the letter and the word are
  what make the verdict legible.

### Changed

- **The library is eighteen packs**, and every counted claim moved with it: `SKILL.md`
  (the routing table, the core-contract split — six of the eighteen, the other twelve —
  and the token-vocabulary note), `README.md`, `bin/cli.js`, `install.sh`, the three
  manifests, the Cursor rule, the slash command, `MOBILE_SURFACES.md`,
  `SURFACE_COMPOSITION.md` (`--accent` in sixteen packs, `@role non-text:` in twelve of
  the eighteen) and `DESIGN_SYNC_BRIDGE.md` (eighteen kits).
- **`datasheet` and `manpage` fork against it, reciprocally.** Both are verdict-shaped
  and both refuse a second family, so an agent reaching either first now learns the
  distinction: `datasheet` when the artefact is a row of cells, `manpage` when the page
  is documentation, `ora` when the artefact is a number with a grade and the reader must
  be shown the raw response a machine received.
- **Ratchet floors raised** to 2179 / 1095 / 464, purely additive; all three self-tests
  still catch every planted defect.

### Six defects in the reference, recorded in the pack rather than copied

Named in `## Gotchas` because a pack extracted from a live site inherits its accidents
unless someone reads them:

- `--border-strong` is declared once in the light `:root` and never re-declared for
  dark, so the reference paints a paper-coloured hairline at **12.02:1** on the coal
  field. This pack ships a dark value of its own and marks it derived at the declaration.
- `--shadow-pop` is a complete shadow in the app scope and a bare **colour** in the
  journey scope. Copying the wrong one produces an invalid declaration, so the shadow
  disappears silently rather than erroring.
- The shadcn `--accent` is a raised **surface**, not an accent — an agent reading token
  names alone concludes the pack has none.
- Two dark greys in one product: warm coal `#141210` against neutral `#151515`, each
  with its own ladder and its own accent.
- Two radius systems: the proportional ladder off `--radius: .5rem`, and
  `rounded-[7px]` / `rounded-[9px]` literals that sit on no ladder.
- Four webfont families are loaded on `<html>` and two are referenced in the stylesheet;
  the progress fill is animated with `transition-all`, which animates `width` and lays
  out every frame.

## [1.27.1] - 2026-08-13

This project's own pipeline paperwork moved from `docs/superpowers/` to
`docs/evidence/`, following `task-pipeline` v1.53.0, which renamed the default and made
the root resolvable. **A patch, deliberately: nothing a consumer of this skill can see
changed.** The directory, this repository's own validator paths and its CI plants moved
together; the records inside the directory were NOT rewritten — a brief describes where
things were when it was written.

## [1.27.0] - 2026-08-13

A ban that said "no side-stripe accent borders" was measured against a real consumer for
the first time, and it turned out to forbid the wrong thing. Narrowed to what it always
meant.

### Changed

- **`editorial-luxury` — the side-stripe ban now says which stripe.** The bare wording
  banned every `border-left` accent, and a production app on this pack has **42** of them.
  Reading them one at a time is what settled it: four are 1px hairlines on code blocks and
  TOC drawers, so not accents at all; three are `transparent`, reserving the gutter for a
  **selected-state** marker; the remaining thirty-five are 2–3px rules on TEXT BLOCKS —
  blockquotes, callouts, toasts, notices, log entries. That is the oldest editorial device
  there is, and a pack whose display face is Fraunces and whose field is cream paper has no
  business banning it. What the list actually collects is **ornament** — its neighbours are
  gradient text, glassmorphism, outer glow and purple — so the ban now names the ornament:
  the full-height accent rule down the side of a card, carrying no state and no semantic
  role, put there to make the card look designed. The line to hold is stated with it: a
  stripe must mean something, and must never be drawn in a colour nobody chose.

  Why it matters beyond wording: a guard written to the literal reading fails on all 42
  sites at once, and a gate nobody can satisfy is a gate that gets bypassed — so the
  over-broad ban was buying zero enforcement while looking like doctrine.

## [1.26.0] - 2026-08-13

The palette gate computed one contrast per theme — ink against field — and never once
asked whether a status colour could be read on the surface it sits on. Twenty-eight
findings in eleven of seventeen packs were waiting behind that.

### Added

- **`validate_status_on_field()`** — every semantic colour is checked against the field
  of **its own theme**, in three tiers, which is what the packs already argued and
  nothing enforced:
  - **≥ 4.5:1** — text, no declaration needed.
  - **≥ 3.0:1** — declared `@role non-text:`, a mark that can be understood on its own.
  - **< 3.0:1** — declared **and** the pack states status is never by colour alone,
    because below the non-text floor the colour is reinforcement and the word is the
    message.
- **`@role non-text:`, a second canonical role marker**, beside the `@role accent:` this
  library already had. It is the whole point of the release: eleven packs *did* say their
  status colours were not text — in five different phrasings ("never text on the field",
  "a FILL and large-text colour", "a fill, not a text colour", "No coral word under
  24px", "category marks") — and a class nobody can grep for is a class nobody checks.
  Documented in `SURFACE_COMPOSITION.md` beside the accent marker.
- Two plants, one per tier, and the check's core was split out so a plant can be a token
  layer written as a string rather than an edit to a real file.

### Fixed

- **`scoreboard`'s dark band inherited the paper status set** (board B-034). Its
  `[data-surface="panel"]` block remapped eleven tokens — `--ink-soft` among them, for
  exactly this reason — and left the four statuses pointing at the paper values, so
  `var(--good)` painted **3.69:1** on that band while `--good-on-dark` had **10.21:1**
  waiting three lines away in the same file. The pack has always said to use the on-dark
  set there; now the token layer does it.
- **`showroom`'s status chip painted its label in its own status colour** (board B-021).
  Measured against the fills the kit actually uses: `--good` **2.03:1**, `--warning`
  **1.54:1**, `--danger` **2.65:1**, at the 12px the same row specifies. The label is
  `--ink` now (14.65–14.73:1) and the status colour is the chip's tint plus a 6px dot —
  which is the pack's own "never by colour alone" rule applied to the component that
  exists to serve it. Corrected in the pack, the kit and with the numbers.
- **`validate.py` counted its own worktree.** Both of its ROOT markdown walks read every
  `.md` under the repository, and this project's standing practice for a concurrent run is
  an isolated worktree at `.claude/worktrees/<name>` — a full second copy of the tree. So
  the gate reported **2361 checks** where the same commit measures **2067** clean, and the
  ratchet in `floors.json` was one commit away from enshrining the inflated number. A floor
  measured with a worktree present fails the next clean run for a regression that never
  happened, and the failure names a count, not a cause. Nested checkouts are now excluded
  by what they **are** — a directory carrying its own `.git` — not by name, because the name
  is a convention and the next one will differ. The plant is the only one in this suite
  whose pass condition is silence: a nested checkout must change neither the verdict nor the
  count, and with the guard removed it reports `MISSED`.
- **`blueprint` answered separation and never legibility.** Its four category marks clear
  every separation floor under all three dichromacies, which the pack said — and
  `--good` **2.40:1**, `--warning` **1.72:1** and `--info` **1.21:1** on the stock, which
  it did not. Its own advice, *"label them anyway, because a legend of four coloured
  squares is a legend nobody reads"*, is now the requirement it always was.

### Notes

- **Nothing else changed colour.** The other twenty-four findings are declarations: the
  packs were right about their own colours and unreadable about it to a machine.
- Gates on the merged tree: `validate.py` 2067, palette **1001**, sloplint 450 — palette
  958 base + 8 from 1.25.0's status set + 35 from this check, additive with nothing hidden
  in it. Floors raised with the reason.
- **This release is 1.26.0 because 1.25.0 was taken while it was being built.** Two runs
  worked the repository at once and both bumped to the same number; the other reached
  `origin/main`, its tag and npm first, so it keeps 1.25.0 and its entry above. Nothing was
  discarded and nothing was rewritten — the collision cost this release a version number and
  twenty-two version references in prose, each of which would otherwise have named a release
  it is not in.
- The two remaining `scoreboard` rows (B-033, B-035, B-036) are untouched — a retracted
  permission still live in its token layer, eight numbers that disagree with the values
  beside them, and a pixel-numeral rule with no working mechanism outside WebKit.

## [1.25.0] - 2026-08-13

**`editorial-luxury` gets the status set it told surfaces to ask for.**

The pack shipped one semantic colour, `--red`, and instructed any surface needing
a full set to close the gap *in the pack, deliberately, not at the keyboard*. The
instruction was right and nobody followed it: a production admin console built on
this pack had invented amber-as-warning and cyan-as-info on top of an amber that
was also its entire chrome — so the hue meaning "a provider is backing up" was
the hue of every button on the page. Seven of that surface's colour pairs sat
below AA and three under 1.1:1.

`--status-{ok,warn,info,danger}` and their `-weak` tints close it. Three of the
four are values the pack already owned: `--status-ok` is `--accent-deep`,
`--status-danger` is `--red`. Only `warn` and `info` are new, each the existing
amber and cyan family deepened until it clears the AA floor for normal text on
**all three** cream grounds — `--paper`, `--paper-2` and `--paper-3` — because
two grounds would have been the same enumerated-list hole one level down. Status
is still never carried by colour alone: the tint carries the colour, the word
carries the meaning in `--ink`.

Also: `--dur-hover` and `--dur-state`. The pack said the product register stays
in the fast range and never named the values, so every product surface built on
it typed `0.15s` literals — there was nothing to reference.

## [1.24.0] - 2026-08-13

A seventeenth style pack, whose whole argument is other people's names — and a reference
whose `h1` is one pixel wide.

### Added

- **`roster`** — the seventeenth pack, extracted from `babylovegrowth.ai` off the
  server-rendered HTML of `/en` (1,415,414 bytes), its two shipped stylesheets (466,577
  bytes, 410 custom properties) and then off **computed styles on the live page** at
  1440×900, 768×1168 and 390×790 — **5,936 rendered elements** at the widest. A white
  field in a faint grid of squares, hairlines instead of shadows, the pill as the most
  frequent shape, and one orange that may never carry a word. For products whose argument
  is *who already carries them*: AI-search and GEO visibility, SEO and content platforms,
  agencies, marketplaces. Widened contract, a light-only token layer, a full reference kit,
  and reciprocal forks written into `scoreboard`, `showroom`, `pigeonhole` and `manpage`.
- **The fork against `scoreboard` is the pack's reason to exist.** Both serve growth, ads
  and SEO products, so the category cannot decide it — the **kind of proof** can. One is
  built around a figure that ticks up; the other around a name that appears. Ask what the
  page loses if you delete its proof, and the giveaway is that `roster` sets its largest
  figure (*4,000+*) in the same 16px eyebrow as everything else.
- **`RESOLVED`, a fourth provenance family.** The reference computes its neutrals in
  `lab()`, which the palette gate refuses on purpose, so each was resolved to the sRGB the
  browser actually paints — **34 distinct values**, each painted into a 1×1 canvas and read
  back as bytes. They turn out to be Tailwind v4's defaults: 7,234 borders at
  `lab(91.6229 …)` = `#e5e7eb`. The bespoke layer beside them is four near-blacks and two
  oranges wide, and the pack ships one of each with the criterion written at the
  declaration.
- **`IndustryColumn`, the signature element** — a pill-labelled column of other companies'
  marks, hairline-divided, six across at 1440 — plus `LogoTile`, `Eyebrow` and `StepCard`.
  Both container breakpoints are **derived from the component's own geometry** (220px for
  the column's two-up mark grid, 640px for the step card's split) rather than carried over
  from the viewport, which is what B-032 exists to prevent.

### Fixed

- **The pack refuses the reference's heading structure.** Its `h1` is `.sr-only` — 1×1px,
  white, `clip-path: inset(50%)` — and the visible 68px line is a `<span>`, while all
  sixteen `h2`s are small orange eyebrows. So the document outline says *eyebrow* where the
  page says *section head*, and the largest text on the page is not a heading at all. This
  pack teaches the opposite and `manpage` now carries the fork from the other end.
- **The accent may not carry a word.** `#fa5c12` is 3.18:1 on white; white on `#f25533` at
  the nav pill's 16px/600 is **3.43:1**. The pack ships `--accent-ink` at 4.52:1 for
  anything read, keeps the accent for fills and large text, and makes the primary button
  black — 19.66:1, which is what the reference itself does for its hero.
- **The dominant secondary ink fails on its own band**: `#6a7282` is 4.84:1 on white and
  **4.35:1** on the `#f0f3f8` band it is painted on. `--ink-soft` is the darkened form and
  clears both.
- **No `--warn` is shipped.** The reference paints no amber anywhere, so one here would be
  invented rather than selected. Stated in the Palette instead of filled in.

### Notes

- **Reduced motion covers six of the reference's animations out of roughly twenty.** Its
  branch names classes one by one, leaving `arrow-nudge`, `skeleton-blink`, both spinners,
  `settings-ripple`, `meta-preview-float` and the accordions running — the opposite failure
  to `pigeonhole`'s reference, which collapsed everything with one `*` rule and strobed its
  marquee by doing so. This pack collapses unconditionally and pauses its two floats in the
  component layer.
- **A claim the measurement refused.** The hero sets a third party's wordmark inline after
  the word *from*; it was sampled seven times across 5.4 seconds with no change, so the
  pack specifies **one mark chosen per page** and makes no claim that it rotates.
- Gates: validate 1938 → 2066, palette 906 → 956, sloplint 436 → 450, floors raised with
  the reason.

## [1.23.1] - 2026-08-13

Two of the seven answers 1.23.0 shipped told an implementer to do something the same
release had just described as impossible.

### Fixed

- **`pigeonhole` contradicted the SELF category it shipped beside.** Its new Responsive
  answer said the labelled row and the FAQ "take `container-type: inline-size` on their
  wrapper" — but the row's axis and the list's columns are properties of the row and the
  `<dl>` **themselves**, so neither can query its own width. That is exactly the SELF case
  the skeleton now defines. The corrected answer is the useful one: both live inside a
  list the consumer already owns, so **the consumer's list is the container** — a
  component library may ask for `container-type` on it and may not wrap someone's markup
  to get it. Descendants inside them (the preview's truncation, the date's visibility)
  are ordinary CONTAINER cases and need nothing from the consumer.
- **`showroom` named a wrapper its kit does not ship.** "container-type on the table
  wrapper" became the **specimen frame**, which is the component that actually holds the
  table (`Specimen`), so the data row and the column header query something that exists.

### Notes

Found by checking every component named in the seven new answers against the components
its kit actually ships — a check worth running whenever pack prose starts naming parts.
Five of the seven were already right; `maquette`'s "agent prompt" is named by the pack and
absent from the kit, which is a pre-existing pack/kit gap rather than this release's.

## [1.23.0] - 2026-08-13

A component library that sized itself by the screen, and a contract bullet nobody had
answered since it was written.

### Added

- **`validate_pack_container_answer()`** — a widened pack's `## Responsive` section has
  to say which of its components size against their container. The skeleton has carried
  that bullet since the contract was widened in **1.5.0**, and **seven of the ten
  widened packs left it blank**: the contract asked and nothing checked, which is the
  same dead zone the all-or-nothing heading rule closed. "None, and here is why" is a
  valid answer — `field-notes` and `cyclorama` were already giving it.
- **`validate_kit_breakpoints()`** — every width media query in the sixteen kits must
  either target `:root` alone or carry a declared reason, because a kit ships components
  a consumer drops into an arbitrary box. It found **seven queries across six kits, and
  zero `container-type` anywhere**.
- **Three kinds of breakpoint, in the skeleton**, because only one of them has a
  container answer: **CONTAINER** (a property on a descendant of a component root),
  **PAGE** (a value the page owns — a hero's padding, a root token switch), and **SELF**
  — a property on the element that *establishes* the container, which cannot query
  itself and has no container answer at all. Five of the seven queries turned out to be
  SELF or PAGE, which is why "0 of 16 kits use container queries" was a worse
  description of the problem than it looked.
- **The distinction the library was missing:** the pack documents a page measured off a
  reference, so its breakpoints are viewport-shaped; the kit ships components this
  project authors, so theirs are container-shaped. `field-notes` was right that
  container queries are "not for the page" and incomplete about the component library
  shipped beside it.
- **All seven silent packs now answer**, each from its own component list — the
  instrument's cell grid, the code frame and the endpoint row, the CLI line and the
  agent prompt, the labelled row and the FAQ's columns, the install line and the
  benchmark row, the data row and the column header, the panel and the figure well.

### Fixed

- **`scoreboard`'s ledger now does what its own pack has always specified.** The pack
  says *"Container queries for the report surface and the ledger: `container-type:
  inline-size`, because both appear inside columns of different widths on the same page
  and neither should size against the viewport"* — and the kit was switching on the
  viewport, so a ledger in a 320px sidebar on a 1440px screen kept its wide columns and
  crushed its leader. This was not a missing modern feature; it was a kit ignoring its
  pack.
- **The breakpoint is derived rather than carried over.** 767px was a statement about
  phones. The row's own geometry: label 95 + gap 12 + numeral column 80 + gap 12 = 199px
  of fixed content, plus a minimum leader of `--space-8` so the dotted line still reads
  as a leader — **231px**, with the 32px named as the one decision it contains.

### Notes

- **Two conversions are held, with the reason at the block.** `blueprint`'s tick and
  column rule and `datasheet`'s cell grid are genuine CONTAINER cases marked
  `TODO-CONTAINER B-032`; each needs its breakpoint derived from its own geometry, and
  carrying 768 or 640 into `@container` would be the same mistake in a newer syntax.
- The new check's own first draft looked back a fixed 400 characters for its marker and
  missed a five-line reason whose marker sat at 425 — a check that fails on a longer
  explanation teaches authors to write shorter ones. It reads the whole comment now.

## [1.22.0] - 2026-08-13

The palette gate learns two colour forms it had been refusing, and the refusal turns
out to have been the reason eight token layers restate a token's channels by hand.

### Added

- **`color-mix()` and relative colour are computable, so they are no longer banned.**
  The gate parses `color-mix(in srgb | srgb-linear | oklab | oklch, A p%, B q%)` —
  premultiplied, shorter hue arc — and `rgb(from <colour> r g b / a)`, with `var()`
  now resolved **inside** a value rather than only as a whole value. Verified against
  Chrome 151's own computed values across eleven cases at a **worst ΔE of 0.004**,
  which is the browser's six-digit serialisation rather than a disagreement.
- **Four self-test plants, two of which prove the new paths are checked rather than
  tolerated.** A `color-mix()` and a relative colour whose ink misses AA must fail on
  the *ratio* — only possible if the parser really computed them. The other two prove
  the refusals still refuse: an unimplemented mix space, and a `calc()` inside a
  channel. Half-implemented CSS maths is worse than an honest refusal.
- **Rule 5 in the pack skeleton** replaces the ban with the limits and one migration
  rule: relative colour is Baseline 2024, so where a token feeds an
  accessibility-critical property — a focus ring above all — the literal ships first
  and the derived value second, because a dropped declaration on a focus ring is an
  invisible focus indicator.
- **`docs/audit/2026-08-13-modern-css-audit.md`** — the whole measurement: what the
  library is ahead on (OKLab dichromacy checks, `color-scheme` in 16/16,
  `text-wrap: balance` in 13/16 kits, `tabular-nums` in 10/16), what is a deliberate
  position rather than a gap, and ten findings with counts.

### Fixed

- **`showroom`'s focus ring now tracks its accent.** `rgba(38, 109, 240, 0.35)` was
  the accent's channels written out by hand; it is now
  `rgb(from var(--accent) r g b / 0.35)`, measured **ΔE 0.00** from the literal, with
  the literal kept as the preceding declaration. Re-tinting `--accent` used to leave
  the ring on the old blue silently — the live mechanism behind B-023/B-024.
- **A blind spot closed in the same commit that opened its cause.** `themes()` decided
  whether a block was a theme by testing for a `#` or an `oklch(` prefix, so a dark
  theme written in `color-mix()` would have been read as "overrides no colour" and
  skipped entirely. It asks `COLOR_SHAPED` now.

### Notes

- **The migration itself is not in this release.** 42 declarations across eight token
  layers are ΔE 0.00 from a token in their own file and could migrate with no visible
  change; 13 more sit within ΔE 2 without equalling one, and *near is not drift* — a
  white at 80% beside an off-white field may be deliberately white. The first set is
  B-027 and needs a per-property support decision; the second is B-028 and needs its
  author, not a script.
- Also filed: B-029 (container queries in the kits — 0 of 16, against 7 viewport
  blocks), B-030 (`text-box-trim`, measure in `ch`, metric-matched fallbacks,
  `@property`, fluid spacing), B-031 (a DTCG export for the Figma seam).

## [1.21.0] - 2026-08-12

A sixteenth style pack, whose eleven pastel hues are a filing scheme rather than a
mood — and a taxonomy that fails its own contrast floor eight times out of nine.

### Added

- **`pigeonhole`** — the sixteenth pack, extracted from `getinboxzero.com` off the
  server-rendered HTML of `/` (399,558 bytes), its two shipped stylesheets
  (599,990 bytes, 152 custom properties) and then off **computed styles on the
  live page** at 1440×900, 768×1024 and 390×844 — 912 rendered elements. A white
  field ruled by hairlines, one blue that only ever appears as a two-stop
  gradient, a display face that never passes weight 400, one italic word in the
  headline, and nine categories in which a hue *is* the category, drawn from an
  eleven-ramp pastel system. For products
  whose job is to sort the reader's incoming mess into named categories — email
  triage, ticket routing, digests, organisers, CRM inboxes. Widened contract, a
  light-only token layer, a full reference kit, and reciprocal forks written into
  `cyclorama`, `showroom`, `orchard`, `workbench` and `manpage`.
- **The signature element is a chip with two layers.** The outer carries the
  deeper tint pair at radius 8px, the inner the paler pair at 7px with one pixel
  between them — the one place in the reference where radius-by-subtraction
  happens to hold exactly. `CategoryChip`'s label word is a **required** prop, not
  an optional one, and the reason is measured: see below.
- **Nine category inks, eight of them derived.** The reference paints its chip
  inks on tints of their own hue and eight of nine fail WCAG AA against those very
  tints — `#49d1fa` at 1.53:1, `#d8a40c` at 1.65:1, `#e65707` at 2.71:1, `#17a34a`
  at 2.72:1, `#c942b2` at 2.79:1, `#c94244` at 3.09:1, `#124dff` at 3.89:1,
  `#6410ff` at 4.28:1. Only the neutral `#525252` clears it. Each is re-derived
  along OKLab lightness with hue and chroma held, and each derivation is marked at
  its declaration.
- **The label word is mandatory, and the number says why.** Darkening those inks
  to clear 4.5:1 compresses them: the worst deuteranopic pair (Marketing against
  Notification) falls from ΔE 4.42 to **1.24**, far under the palette gate's hard
  floor of 10. Eleven hues cannot be simultaneously AA-compliant and mutually
  distinguishable to a dichromatic reader, so the hue is declared a *redundant*
  channel and the category tokens sit deliberately outside the gate's semantic
  peer set — with the reason written at the declaration, so a future widening
  reads it rather than assuming an oversight.
- **`LabelledRow`, `WashCard` and `FaqList`** join the six-component spine. A
  wash card's shadow is mixed toward its own hue rather than toward black, which
  is why the page reads coloured while the field stays white.

### Fixed

- **The primary button's ramp is reversed against the reference.** White on its
  upper gradient stop measures 5.04:1 and on its lower stop 3.29:1 — the label
  passes at the top of the button and fails at the bottom of the same button. The
  pack and the kit run the gradient light-to-dark so the worst case is the passing
  colour.
- **The focused CTA gets a ring.** The reference computes `outline-style: none` on
  its focused primary button with no compensating shadow. The kit ships 2px of
  `--accent-strong` at 2px offset.
- **The lede ink.** `#848484` at 3.74:1, painted at 18px regular, replaced by the
  reference's own `#6b7280` at 4.83:1.
- **Two counts that reached no check** are corrected in passing:
  `SURFACE_COMPOSITION.md`'s accent-role tally (thirteen → fourteen, recounted
  from the token layers rather than incremented) and the kit-count claims in
  `README.md`. The class stays open on the board as B-016.
- **B-015 is closed.** `.tmp-fp-hero.png` leaves the tree and `.gitignore` gains
  the `.tmp*` rule that would have stopped it entering.

### Notes

- **Two claims from the screenshots were refuted by the DOM and are recorded
  rather than dropped.** There is no rotation anywhere on the page — zero
  elements carry a rotation term in `transform` or the individual `rotate`
  property, at three viewports — so a scattered, tilted pile is explicitly not
  this pack. And the before/after diptych is not built from DOM rows: the words
  `Before` and `After` appear zero times in the served HTML and zero times in the
  live DOM after a full scroll pass. The section is raster art, and the pack
  specifies it as art direction with an aspect ratio rather than as a component.
- **No dark theme.** The reference's stylesheet carries a `.dark` block, but it
  belongs to the application's stock shadcn slate theme and nothing on the
  marketing page consumes it. Shipping an undocumented dark twin is a defect this
  library already carries once (board B-018), so the pack is light only and says
  so.

## [1.20.0] - 2026-08-12

A fifteenth style pack, whose display typeface costs zero bytes — and three
WCAG failures in the reference, one of them on the very element the design is
remembered by.

### Added

- **`manpage`** — the fifteenth pack, extracted from `zernio.com` off the
  server-rendered HTML of three pages and its two shipped stylesheets, which
  declare 398 custom properties: the Tailwind v4 default ramps plus twelve
  bespoke brand names (coral, cream, ink, charcoal, burgundy, each with a
  `-muted` partner). Cream paper, a 48px display that never grows louder, a
  576px argument column narrower than most prose, coral label chips that are
  real `<h2>`s, `└` tree glyphs in their own grid column, and one dark code
  frame as the focal point. For developer products whose buyer reads code —
  APIs, SDKs, CLIs, MCP servers. Widened contract, a two-theme token layer, a
  full reference kit, and reciprocal forks written into `blueprint`,
  `datasheet`, `field-notes`, `instrument-console`, `scoreboard`, `showroom`
  and `workbench`.
- **The display face is the system monospace, and that is the whole identity.**
  The reference loads exactly one webfont — a single variable Geist Sans — and
  sets its headline, body, chips, code frames and FAQ in
  `Menlo, Consolas, Monaco, "Liberation Mono", "Courier New", monospace`, which
  is already on the reader's machine. No render-blocking request for the face
  that carries the page, and no swap window on the headline. Substituting a
  webfont mono is banned in the pack: it costs a request to look less native.
- **The section heading is a chip and the chip is a real heading.** `LabelChip`
  wraps its span in an `<h2>`, which is why the reference keeps a clean outline
  — one `h1`, one `h2` per section — while reading as a printed specification.
- **`FaqList` is a `<dl>` that never collapses.** The reference ships zero
  `<details>` and zero `<summary>` on its FAQ: every answer is flat text in the
  DOM, paired with its question, extractable without running JavaScript. The
  component has no `collapsed` prop and will not get one.

### Fixed

Four corrections to the reference, every replacement a colour it already ships:

- **The white button label fails AA.** `Start for Free` is white on coral at
  **4.16:1**, on both the hero and the closing CTA. The fill is kept — the coral
  button *is* the identity — and the label darkens to `--on-action` (ink) at
  **4.55:1**. `--action-strong` is the reference's burgundy, carrying white at
  13.34:1.
- **The signature element is the least readable thing on the page.** The section
  chip paints 12px coral on a coral/8 wash: **3.24:1**, worse than coral on bare
  cream because the wash lifts the field. The wash and edge are kept so the chip
  looks identical; the label becomes `--accent-ink` at **10.40:1**.
- **The live-status green fails AA at 2.82:1.** `green-600` carries the credit
  balance, the `online` badge and both weekly counters. Its own ramp cannot be
  stepped into a legal set — `green-700` still misses at 4.35:1 and `green-800`
  clears AA but separates by only 3.9 under dichromacy — so success takes
  emerald-800, a ramp the reference also ships in full.
- **One reduced-motion gate out of eight animations.** The reference gates its
  40s logo marquee behind `motion-safe:` and leaves the hero blur-in, every
  section rise, `fadeInScale`, `slideInRight`, `pulse`, `ping` and a **1.1s
  infinite `waveform`** running for a reader who asked for stillness. The pack
  collapses the whole surface, and infinite motion **stops** rather than
  shortens.

### Changed

- `test/floors.json` raised: `validate.py` 1647 → 1788, `validate_palette.py`
  716 → 791, `sloplint.py` 366 → 422.
- **The stated-ratio checker earned its keep twice on this pack**, catching
  `--ink-strong` claimed at 18.98:1 against a computed 19.44 and
  `--on-action-strong` at 6.71:1 against 7.76 — both authored by hand, both
  wrong, neither visible on inspection.
- `SURFACE_COMPOSITION.md`: three counts corrected by measurement — the accent
  resolves as `--accent` in **thirteen** packs, `--brand` in `field-notes` and
  `--cta` in `orchard`. **B-016 stays open**: none of the three reaches a check,
  because `in thirteen,` is not followed by a counted noun. This is the third
  release in which they were fixed by hand.
- `plugins/sheleg-design/.claude-plugin/plugin.json` said **thirteen** style
  packs while fourteen shipped. `validate_counted_claims()` did not catch it:
  its pattern wants `<number> [pluggable|locked] style packs` and the manifest
  wrote `pluggable visual style packs`, so the intervening adjective hid a stale
  count from the gate that exists to find them. Corrected to fifteen; the
  pattern gap is the same class as B-016.

## [1.19.0] - 2026-08-12

A fourteenth style pack, and the Refero style card it started from was wrong in
four measurable places.

### Added

- **`datasheet`** — the fourteenth pack, extracted from `fingerprint.com` off its
  live computed styles and its shipped stylesheet, which declares 140 custom
  properties including ten-step ramps for nine hues. An off-white spec sheet, one
  vivid orange, Inter over JetBrains Mono, a concentric radius family from 16 down
  to 2 — and a **live instrument ruled out of hairlines at radius 0 which re-skins
  itself dark when it detects the reader is hiding**. For B2B SaaS whose product is
  a verdict about the visitor, the request or the device: fraud and bot detection,
  device intelligence, identity, API products sold on their payload. Widened
  contract, a two-theme token layer, a full reference kit, and reciprocal forks
  written into `field-notes`, `instrument-console`, `showroom`, `blueprint` and
  `scoreboard`.
- **The dark half is a state, not a theme.** `[data-state="alarm"]` — the token
  `--dash-dark` appears in 97 rules on the reference and every one of them is an
  incognito selector; 134 rules in total re-skin the instrument when it detects
  evasion. Wiring that surface to a user preference is banned in the pack, because
  it destroys the only idea the pack has.

### Fixed

- **`validate_counted_claims()` did not read the three manifests, and both carried
  a stale count.** `.claude-plugin/marketplace.json` said *"twelve pluggable style
  packs"* above a list of thirteen for two releases, and `package.json` said
  *"thirteen"* on the day the fourteenth landed. Names in those files were already
  checked; the number beside the names was not, because the source list was
  all-markdown plus two scripts. The list now includes both plugin manifests and
  `package.json`, watched saying no against a planted `eleven` in the real file and
  again as a permanent self-test plant that derives its wrong number from whatever
  the manifest currently claims.
- **Four corrections to the reference, recorded rather than applied silently.** Its
  primary button sets white on `--orange-7` at **3.32:1**, so the pack's resting
  fill moves one ramp step to `--orange-8` (5.34:1) and hovers to `--orange-9`
  (9.02:1) — no colour invented, and the darkening direction kept. Its 8px mono
  badge is set in `--gray-6` at **2.51:1** and the pack refuses that ink. Its `h1`
  is pure black while its `body` is `#141415`, and the pack ships one ink. Its
  `prefers-reduced-motion` block covers one group of hero animations out of roughly
  twenty keyframe sets, and the token layer collapses the whole surface.
- **Eleven defects in the new pack, found by its own routing scenario and fixed
  before the tag.** T24 ran both branches in fresh contexts — the positive branch
  chose `datasheet`, the negative stayed on `field-notes` — and each was asked to
  read its chosen pack and report defects. The sharpest: in the alarm state
  `--danger` on its own tint measured **4.44:1**, in the one cell that state exists
  to render (the tint moves to `--pink-10`, 6.24:1); and the focus ring at
  `--accent` measured **2.85:1** on `--accent-wash`, the surface the pack itself
  mandates for a selected cell (a new `--focus-color` is `--accent-deep` on paper).
  Also fixed: an accent job list that contradicted the pack's own ban, a button
  border rule with no token behind it, 54 of 118 token declarations carrying
  neither MEASURED nor SELECTED, a "hard floor" argument that sat exactly on the
  floor, a duration measured against the wrong ceiling, an empty state using an ink
  the palette table forbids for content, and two type values outside the ramp. Full
  table in `test/scenarios.md` under T24.
- **`SKILL.md` said "Six of the fourteen … The other seven answer all four."** Six
  plus seven is thirteen against a fourteen-row table, and the pack left out of the
  sentence was the one this release adds. It was this release's own count edit that
  did it — **and the identical defect was found by a scenario agent in the previous
  pack release**, fixed then as an instance. `validate_contract_split()` now derives
  all three numbers from the table, watched saying no against a planted remainder
  and shipped with a permanent self-test plant that reads whatever the paragraph
  currently claims.
- **`SURFACE_COMPOSITION.md` said the accent role resolves to `--accent` in ten
  packs.** True at twelve, silently wrong at thirteen, twelve at fourteen. Fixed by
  hand and filed as **B-016**, because the phrase reaches no check: `in ten,` is
  not followed by a counted noun.

### Changed

- Ratchet floors raised to **1647 / 716 / 366** from 1507 / 603 / 352.

## [1.18.0] - 2026-08-12

### Changed

- **The installer now offers the family's routing block** (closing B-06 in the
  umbrella). Until now only `super-ux` delegated: install this skill on its own
  and no router was written at all, so an agent had the skill and no rule saying
  when to reach for it. The bundle installer wrote all eight, which is why
  nothing looked broken — the gap only opened for someone installing one member.

  Delegated to `npx sshlg-skills routers --member sheleg-design` rather than
  reimplemented, for three reasons:

  - The block describes what the machine actually has. A lone member rendering
    the whole thing would print a table for routers nobody installed.
  - `--member` scopes the write to this skill's own section. Verified by damaging
    two sections of a real block and running this installer: its own was
    repaired, the other left exactly as it was.
  - The launcher is the only writer that copies the operator's global instruction
    file before touching it. That file has no version control behind it.

  `--no-install` keeps it from silently downloading a package nobody asked for.
  When the launcher is absent the command is printed instead of failing: ending
  an install in an error over an optional follow-up reads as a failed install.
  Both paths were exercised.

## [1.17.0] - 2026-08-12

The scenario harness reaches zero unrun, and the last five runs found something
the three gates could not see about themselves.

### Changed

- **Every scenario in `test/scenarios.md` now carries a verdict and a date.** T4,
  T8, T10, T11 and T12 were run **blind** — against the installed bundle, which
  has no `test/` directory, so no agent could reach its own pass condition. Five
  of five green: style-by-name, the Figma border in both directions, the deck
  register, consumer health, and the friendly-half disambiguation.
- **`RATIO_CLAIM` no longer reads `--space-4: 1rem` as a `4:1` claim.** A real
  latent defect that had never fired, because the branch that would have hit it
  skipped every claim whose partner it could not name — the same blind spot, one
  layer down. Floors and bounds (*"must clear"*, *"no better than"*) join the skip
  list, because they are arguments about a measurement rather than one.

### Fixed

- **1.16.0 fixed an instance and called it a class.** It gave
  `instrument-console` a declared ratio base and swept nothing else. Measured now,
  across the library: **121 stated contrast ratios, 71 of them — 59% — reach no
  check.** Six packs declare no table base, and packs that do still leak, because
  a Gotchas paragraph is not a table row.
- **All 71 were recomputed by hand and all 71 are correct**, so nothing shipped
  wrong; what is missing is a guard against the next edit. Two guards were written
  and both discarded, and that is the part worth keeping: pooling every token pair
  **cannot fail** (a planted `9.99:1` passed — thirty tokens are ~435 pairs
  spanning the whole range), and pooling the token named on the line fails on nine
  lines of which eight are correct writing — floors, bounds, gradient positions,
  and candidate colours a pack measures in order to reject them. A guard has to
  tell a measurement from an argument about one. Filed as **B-013**, with the
  honest interim state written into `validate_palette.py` at the point where the
  skip happens, rather than a check that reports coverage it does not have.

## [1.16.1] - 2026-08-12

### Changed

- **The body is back inside the token budget** — ~5478 → ~4988 of 5000. Four places
  were restating what a file beside them already carries in full: the style-pack table
  described each pack in a sentence when every pack file opens with its own
  description, so the table is now for *choosing*; the reference-sweep, When-to-Use and
  Overview sections lost their second telling. Nothing was deleted — the core-contract
  asymmetry, the sweep boundary and the pack-wins rule all stay inline, because those
  are traps an agent cannot know to look up.
- The Cursor mirror was updated in the same change; its drift guard is what caught the
  omission.

## [1.16.0] - 2026-08-12

The five findings T5 and T6 left on the board, actioned.

### Fixed

- **`instrument-console`'s palette table declared no base, so none of its ratios
  were checked.** `validate_stated_ratios` reads the comparison base out of a
  table header; with none, the library's default dark infrastructure pack was its
  **least-covered**, and the one automated fact about it was `--ink` on `--bg`. The
  table now declares `| On \`--base\` |` and every number in it is recomputed on
  each run — the palette gate goes 596 → **603 checks**, which is the size of the
  hole.
- **`--accent-ink` was stated at 6.0:1 in two places and computes 6.17.** From the
  unrounded colour rather than the shipped hex, the same way four `scoreboard`
  ratios were wrong in 1.13.0. Conservative in direction, wrong in kind.
- **`workbench`'s reference kit had no selected row.** The pack mandates
  `--accent-weak` plus a 2px accent inset for selected; `Chip` implemented it and
  `DataTable` did not — the one atom on an admin dashboard that most needs
  selection was the one that lacked it. `DataTableRow` gains `selected`, with
  `aria-selected` on the row.
- **`workbench` stated its type scale and its 4px grid in prose and shipped
  neither as tokens**, which made the craft bar's *"no ad-hoc font size anywhere
  in the diff"* unachievable in this pack specifically — and its own kit wrote
  **twenty** raw `font-size` declarations because there was nothing to reference.
  `--t-chip` … `--t-page` and `--space-1` … `--space-6` now ship; every value was
  lifted from the pack's own Type section, none was chosen. The kit is down to
  zero raw sizes.

### Changed

- **`test/scenarios.md` says out loud that it cannot be blind.** Every scenario
  states its pass condition a paragraph from its brief, so an agent with
  repository access can find its own exam — T5's run reported exactly that, after
  selecting the right pack anyway. Runs are now pointed at an **installed** bundle,
  which carries no `test/` directory. A run against the checkout still yields
  findings; its verdict is not blind and must not be recorded as if it were.

## [1.15.0] - 2026-08-12

Two of the eight unrun scenarios were run. Both passed, and between them they
found four things three green gates could not.

### Added

- **A core pack's missing half has an authored answer, and the bundle now says
  where.** `npx sheleg-design-skill --kit <pack>` materializes `src/styles.css`,
  whose component half is real CSS for `:hover`, `:focus-visible`, `:disabled` and
  selected — the exact per-component states a **core** pack declines to specify.
  `SKILL.md` said kits are not installed and stopped there, so an agent reading the
  bundle invented those states from scratch while an authored version sat one
  command away. Neither file pointed at the other.
- **A precedence rule for the dial table.** "A quiet internal admin dashboard"
  fires both *quiet like Linear* (DENSITY 2–3) and *product UI* (6–8) — a factor of
  three, with nothing to break the tie. **The row that names the surface wins over
  the row that names a mood**, and you say which fired.
- **Two cases the reference-sweep pairing assumed away**, both common: only the
  image server present (you are reading structure off screenshots — a weaker read,
  say so) and a sweep that returns nothing (a null result is a result; "I swept"
  with no findings and no statement of emptiness cannot be told apart from not
  sweeping).

### Fixed

- **`workbench`'s accent gotcha named two surfaces of three.** It forbids accent
  text on `--panel-2` and `--accent-weak` at 4.30:1 — but in light mode `--bg` **is**
  `--panel-2` (`#F7F8FA`), so a plain accent link on the app ground fails identically
  and read as covered for four releases. The most ordinary element in an admin panel.

## [1.14.1] - 2026-08-12

### Fixed

- **1.14.0 said Refero was "alone among the three" in returning flows. Mobbin
  returns them too.** `mcp__mobbin__search_flows` has always existed; it was
  invisible because Mobbin was registered and unauthenticated, so the sentence
  shipped as a claim nobody in that session could check — in a file whose own
  rule, two paragraphs away, is **gate on the tools present in the session, not
  on the config**. The rule was right and was not applied to its own author.
  Corrected the hour Mobbin was signed in, against its live tool surface.
- **The distinction that replaces it is the useful one: they answer in different
  media.** Mobbin returns each step as an evenly-spaced *preview image* — its own
  tool description says to look at those rather than trust the metadata — and
  also searches web **sections** (hero, pricing, footer). Refero returns each step
  as *structure*: a goal, an action, a system response. Drawing a diagram with
  decision points and recovery paths reads Refero; judging whether a step works on
  a phone looks at Mobbin.

## [1.14.0] - 2026-08-12

### Added

- **Refero joins the reference-sweep slot** (`mcp__refero__*`), beside Lazyweb
  and Mobbin. It searches real UI screens, returns visually and functionally
  *similar* screens for one you already have, and — alone among the three —
  returns **flows**: connected steps carrying a goal, an action and a system
  response each. `DESIGN_SYNC_BRIDGE.md` §4 now says what each of the three is
  for, since they are not interchangeable, and the section heading names all
  three: a heading is a discovery surface, which is the lesson 1.12.1 shipped.

### Changed

- **The sweep boundary is now stated against a tool that argues with it.**
  Refero ships a *style* search whose own description offers "typography,
  palette, layout/composition, spacing, elevation… the overall design language"
  — by that description a source of identity, which is the half a pack owns. The
  rule is unchanged and now explicit: a style found there is a **candidate
  source**, not a decision. One that should set identity goes through §5
  live-site extraction into a pack, with measured values and an addressable
  `Origin:`; applied straight to a page it is a second identity source and the
  page ends up in two design systems. The one-line test: **a sweep may change
  what is on the screen and where; only a pack may change what it looks like.**
- The gate pins the full §4 heading, so a fourth server is a check failure
  rather than a silent omission.

## [1.13.1] - 2026-08-12

`scoreboard`'s routing scenario was run the day it shipped, and it found nine
things three green gates had not.

### Fixed

- **The focus ring was invisible.** 1.13.0 promoted the reference's decorative
  `focus-within` glow — a 20% accent halo with a 40% border — to the pack's focus
  treatment without measuring it. Composited the way a browser does it, the halo
  is **1.29:1** against the paper and the border **1.67:1**, against a WCAG floor
  of 3:1 for a non-text indicator. `--ring-focus` is a solid 2px accent ring now,
  and `--ring-focus-sand` carries `--surface-sand`, the one field where the accent
  falls under the floor at 2.97:1.
- **No orange in the pack can carry a link, and 1.13.0 said one could.**
  `--accent-hover` was called "the one orange that may carry a link" at 4.12:1 —
  below the same AA threshold the pack cites two paragraphs earlier to ban the
  accent from text. A link is `--ink` with an `--accent` underline.
- **Four status ratios were stated 0.02–0.08 optimistic**, computed from the
  OKLCH the colours were selected from rather than from the 8-bit hex the token
  layer ships: `--good` 5.09, `--warn` 4.78, `--danger` 7.93, `--info` 6.49. They
  passed the repository's own gate only because its tolerance is 0.1, which is
  how a wrong number survives a green check.
- **The status chip carried a 10% tint that put an 11px `--warn` label at
  4.38:1.** The chip has no fill now — the word carries the colour. This also
  removes a disagreement between the pack doc and the kit, which had never
  rendered a tint.
- **`--bp-md` and `--bp-lg` were referenced in three token comments and defined
  nowhere.** Replaced with the pixel values they meant.
- **`SKILL.md` miscounted its own library**: "Six of the thirteen are on the core
  contract … the other **six** answer all four." Six plus seven. Introduced by
  1.13.0's own count edit and found independently by both scenario branches.
- **`SURFACE_COMPOSITION.md` said only `field-notes` ships a validated
  `--chart-1…N` set.** `scoreboard` ships one too.
- **The numeral column is a glyph budget, and the pack only warned about it.**
  Press Start 2P advances a full em per glyph, so at 15px the 80px column holds
  five glyphs and the 70px mobile column four: `3.4x` fits, `$9,840` does not.
  Stated as a ceiling with the only two legal answers — shorten the figure, or
  widen the column for the whole ledger.

### Changed

- **T23 has a result.** Both branches run in fresh contexts: `scoreboard` chosen
  for the tally brief with the fork quoted from both sides, `field-notes` held for
  the provenance brief. Recorded with every finding's disposition — including one
  **refuted** (`--on-accent` is not a dead token; its consumer is the selected chip
  at 4.92:1), because a refuted claim nobody writes down comes back as folklore.
- `validate_palette.py`'s floor drops 597 → 596, with the reason in
  `test/floors.json`: a token was deleted rather than a check weakened.

## [1.13.0] - 2026-08-12

A thirteenth style pack, and it is the first one in the library whose accent is
forbidden from carrying a word.

### Added

- **`scoreboard`** — the thirteenth pack, extracted from
  <https://www.get-ryze.ai/> on 2026-08-12 off its shipped stylesheet and the
  markup of three pages. Warm paper (`#FAF9F5`), a warm near-black ink
  (`#221D16`, 15.88:1), radii of two and three pixels, an **ink** primary button,
  one hot orange (`#FF4801`) used only as a mark, and a dark ledger of
  dotted-leader rows whose numbers are set in an aliased pixel face. Widened
  contract — all thirteen headings — with `styles/tokens/scoreboard.css` and a
  full reference kit in `kits/scoreboard/`.
- **The accent measures 3.23:1 and the pack says so at the top.** Above the 3:1
  floor for a non-text mark, below the one for a word. The reference obeys this
  without ever stating it: across three pages its orange is a 3×18px tick, a
  `::marker`, a focus ring, a selection colour, a link underline and one
  oversized chevron — and its primary button is ink. The pack turns that
  observation into a ban, which is the only reason a page in it can carry a
  colour that loud.
- **Two status sets rather than one filtered set.** The reference paints status
  only on its dark panels; those values measure 1.6–2.6:1 against warm paper. The
  paper set is selected from deeper steps of the Tailwind ramp the reference's own
  stylesheet ships, and the measured on-dark set is kept beside it under
  `--*-on-dark`. Every declaration says which of the two kinds of claim it is.
- **`TickHeading`, `Ledger`, `LedgerRow` and `StatusChip`** in the kit, on the
  same six-component spine as every other kit. `StatusChip` takes `label` as a
  **required** prop: the paper statuses cluster (the accent and `--warn` separate
  by 6.3 under protanopia), so status in this pack is a chip with its word in it.

### Fixed

- **Three corrections to the reference, recorded rather than silently applied.**
  Its positive-delta colour `#00D492` is set at 11px on white — 1.84:1, an
  invisible success state — and is confined here to the dark panel where it
  measures 10.21:1. Its primary button transitions over 500ms, past the 300ms
  ceiling in `MOTION_DOCTRINE.md` §3, and the pack pins `--dur-fast` at .16s. Its
  scan line animates `top`; the pack rebuilds it on `transform`.
- **`validate.py --self-test` printed FAILED and exited 0.** `main()` returned
  the self-test's status and `__main__` called it bare, so the code was dropped
  on the floor and `npm run selftest` stayed green through a self-test that had
  failed — found because this release's count change broke a plant fixture and
  the suite passed anyway. The argv handling directly above it exists to close
  this exact class one layer up and never reached the exit code. Verified by
  breaking a fixture in a copy of the tree: 0 before, 1 after.
- **A plant fixture pinned to a literal that changes every release.** The
  stale-count plant searched for `**twelve locked style packs**`; the first time
  the library grew it mutated nothing and stopped testing the check it exists
  for. It now reads whatever number the README claims and makes that wrong.
- **Reciprocal forks with `field-notes` and `workbench`.** From a distance
  `field-notes` *is* this pack — warm paper, one orange-red accent, hairline
  rules — and the distinction is what the small type does: mono numerals make
  evidence auditable, pixel numerals make results countable. Both neighbours now
  carry the fork back, so an agent arriving at either one first still learns it
  exists.

## [1.12.1] - 2026-08-11

- **The reference-sweep heading named one server for a section about two.** It
  read `Optional — real-world references (Lazyweb MCP)` after Mobbin joined it,
  so an agent skimming headings would conclude Mobbin was not there. Headings are
  a discovery surface, not decoration.

## [1.12.0] - 2026-08-11

Mobile becomes a register the skill can name, and a second reference sweep joins
the one slot that already existed rather than opening a competing one.

### Added

- **`MOBILE_SURFACES.md`** — loaded when the brief is a native app screen or a
  mobile-web view. It collects the five mobile rules the packs each state on
  their own (`svh` over a banned bare `100vh`, the 16px input floor that exists
  to stop iOS zoom-on-focus, a desktop flourish that must not survive into a
  touch target, the `pointer: coarse` depth collapse, and why reduced motion and
  a coarse pointer are two signals rather than one). Until now a reader looking
  for *mobile* had to find them inside `field-notes`, `cyclorama` and the
  template.
- **The half a pack does not decide on a phone: platform convention.** Where
  primary navigation lives, sheet versus push, gesture affordances, the notch and
  the home indicator — no pack in the library states any of it and none should.
  Said out loud, in the same shape as a `Contract: core` declaration, so the
  silence is not read as permission to invent.
- **Mobbin joins the reference-sweep slot** (`mcp__mobbin__*`) beside Lazyweb.
  Strongest on native iOS and Android, and it carries web products too, so it is
  swept on a website as well — **use whichever server is present, on web and
  mobile alike; with both, sweep both.** `DESIGN_SYNC_BRIDGE.md` §4 is
  unchanged and now governs two sources: **a sweep informs structure, hierarchy,
  content order and platform convention; identity stays the pack's.** Stylistic
  observations are allowed *as observations* — "three of five finance apps use a
  full-bleed dark sheet for the confirm step" is a structural fact worth telling
  a designer; "use their blue" is a second identity source, and a reference that
  genuinely should set identity goes through §5 live-site extraction into a pack
  instead.

- **A sixth mobile rule that no pack answers.** Every pack's type scale is a
  `vw`-keyed `clamp()`, which responds to viewport width and **not** to iOS
  Dynamic Type or Android's font scale — a user at the largest text size gets
  the same type as a user at the smallest. Zero mentions of it existed anywhere
  in the bundle. Two independent test agents raised it as the largest
  unaddressed gap for a native surface, and it is now stated as a gap with the
  decision handed to the reader rather than answered with an invented value.

### Changed

- **The sweep gate reads the tools, not the config.** A registered MCP server
  nobody has signed into exposes nothing, and Mobbin needs both a browser
  sign-in and a paid plan — so "is it configured" was never the right question.
  Its tool surface is unpublished, so the skill says to discover what the session
  exposes rather than naming a tool it cannot verify.
- **The description carries a mobile trigger** (`"mobile screen" / "мобильный
  экран"`) and `mobile app screens` in the product-UI clause. It was restructured
  rather than extended to make room: the two overlapping Figma triggers merged
  into one pair and `"particle landing"` came out, since the prose already
  carries `particle/WebGL background`. Net 964 → **961**, under the 970 working
  limit the house rule reserves for a future "not for" clause — the first draft
  reached 1017 and the gate refused it.
- **One trigger removal was a regression, caught by running T1 rather than by
  reasoning about it.** Dropping `scrubbed sections` from the prose cost the
  scroll-narrative storyboard task: a fresh agent answered `none` where the old
  description loaded the skill. A control run against the previous description
  proved the edit caused it rather than the task being borderline. The phrase is
  back, paid for by shortening `marketing site, or hero experience`, and the
  re-run is **14/14 — 0 misses, 0 false loads** across the full set including
  both new mobile tasks. A description edit obliges the whole trigger set for
  exactly this reason.

## [1.11.0] - 2026-08-10

The bundle now stands on its own. A repeat audit ran the skill the way an agent
actually uses it — six application scenarios in fresh contexts, not routing
questions — and found the same defect class three times: **a rule inside the
shipped bundle instructing the reader to use something only the repository has.**
1.10.0 had fixed one instance of this and swept the literal form (a repo path in
backticks, now zero) without sweeping the class.

### Fixed — the class, in its three shipped shapes

- **The bundle carries its own version.** `SKILL.md` front-matter gains
  `metadata.version`, making version sync ×5. `DESIGN_SYNC_BRIDGE.md` §7 has told
  readers since 1.6.0 to record the pack version in the synced project; there was
  no version anywhere in the bundle to read, only historical mentions in two packs
  ("until 1.10.0 the header rule read…"). A rule whose input does not ship is not
  a rule.
- **The spine is named.** §1 built its "names are the interface" argument on "the
  same six component names" and named none of them. They are now stated —
  `Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — so a delivered kit can be
  checked against the claim. A test agent refused to guess them and said asserting
  them would be "inventing a value and believing I read it".
- **Pack-authoring rules ship with the template.** *Never ship on the nine*, *no
  addressable reference, no pack*, *a derived value is marked derived where it is
  declared*, and *the three gates are what done means* lived in `CONTRIBUTING.md`,
  which no install contains. They are now in `styles/STYLE_PACK_TEMPLATE.md`,
  which does.
- **`validate_bundle_self_sufficiency()`** gates all three shapes, each watched
  failing on a planted defect *and* discriminated by its own message. It checks
  the three forms that have actually shipped and says so — it is not a general
  proof, so a fourth instance has to be a new shape.

### Fixed — two files that disagreed, and two constants with no value

- **The scrub recipe now obeys the doctrine it contradicted.** `SHELEG_DESIGN.md`
  §9 shipped `useLayoutEffect` with hand-rolled teardown; `MOTION_DOCTRINE.md` §6
  names that exact pattern as where leaked triggers and doubled animations come
  from. Neither file acknowledged the other, and an agent reading only the
  reference copied the banned shape into a junior-ready plan.
- **`arcAmp` and `drop` are declared tuning constants.** Both appeared inside
  formulas with no value anywhere in the skill, which reads as an omission rather
  than a decision. Neither is invented here; the rule is to tune, then record the
  value beside the formation rather than inline.

### Changed

- **The entry point is back under its disclosure budget** — 6157 → 4856 tokens.
  Scene depth and the `dataviz` handoff moved to `SURFACE_COMPOSITION.md` with
  stated load triggers; the quick-reference table moved next to the mechanisms it
  summarises in `SHELEG_DESIGN.md`. No doctrine was deleted.
- **The front-matter budget was measuring the wrong thing, and fixing it raises
  the total ceiling from 1024 to 1280.** That is a loosening, named as one. The
  single 1024 cap over the whole block conflated the spec's limit on
  `description` with the bookkeeping keys beside it, leaving the check stricter
  than the standard it claimed to implement — so a 24-character version key
  consumed the description's headroom and would have blocked the widening board
  row B-006 asks for. Now two budgets: `description` ≤ 1024 (the spec),
  everything else ≤ 256, against 74 characters used today.
- **Six scenario results recorded** with their commit, closing most of board row
  B-005. The harness had 20 scenarios and 7 recorded results, so the repository
  could not answer "do the usage scenarios work" from its own records.

## [1.10.0] - 2026-08-10

A fresh-eyes audit of the whole skill, and the finding is the green: at 1.9.0 all
three gates passed — 1270 / 412 / 224 — while the skill told a reading agent
there were six style packs, handed the chart layer a token ramp no pack defines,
and stated thirteen contrast ratios that are wrong.

Full report with every `file:line`, and the reproductions:
[`docs/audit/2026-08-10-skill-audit.md`](./docs/audit/2026-08-10-skill-audit.md).

### Fixed — what an agent was told that was not true

- **The `dataviz` handoff named tokens no pack defines.** `SKILL.md` promised a
  ramp `--accent-tint … --accent-deep`: `--accent-tint` exists in **one** pack of
  twelve, `--accent-deep` in three, and **no pack has both**. It promised a
  status set of `--good` / `--warning` / `--danger` that seven packs lack and
  two have no version of at all. An undefined custom property does not error —
  the declaration goes invalid at computed-value time and the property silently
  inherits — so the agent follows the instruction exactly and the page is wrong.
  The table is now written by role, and the non-uniform mappings are named.
- **Thirteen stated contrast ratios, recomputed and corrected.** `blueprint`'s
  ratio column is headed ``On `--bg` `` and every number in it was computed
  against pure white (`--ink` 17.74 → **17.15**, `--accent` 7.53 → **7.28**,
  pure black 21 → **20.31**). `prism` claimed ink "≥18:1 over all four stops"
  three times; it is **15.85–16.82** — 18.95 is ink on plain white, carried onto
  the wash. Also `showroom` 15.9 → **15.35** and 7.7 → **7.08**, `maquette` 5.0 →
  **5.62** and 13.9 → **13.57**, `editorial-luxury` 6.1 → **6.93**, `workbench`
  5.0 → **4.57**. None crossed a floor; all were presented as measured.
- **Two packs justified one accent by a "symmetry" that is a mathematical
  identity.** WCAG contrast is symmetric for every pair by definition. In
  `showroom`, whose field is white, the sentence stated one measurement twice; in
  `blueprint`, whose field is not, the two directions genuinely differ and the
  pack asserted one number for both.
- **`atrium` prescribed `transition: padding-top .2s` on a sticky header** — a
  layout property, transitioned, on scroll: the exact form `MOTION_DOCTRINE.md`
  forbids, shipped inside the bundle that ships the ban.
- **`field-notes`' radius rule, its worked example and its token layer were three
  different systems.** "Subtract the padding … `12 - 12 ≈ 7.2`" — subtraction
  gives 0; the token layer uses `calc(var(--radius) * 0.6)`.
- **`blueprint`'s Components and Hero instructed the violation its own Signature
  element section names** (registration marks on both CTAs). `test/scenarios.md`
  recorded this as "fixed in the same run"; only half of it had landed.
- **`atrium` said three shadows exist**; its token layer defines four.
- **The colour-blindness ban was copy-pasted into six packs**, asserting a
  measurement across "several pairs" in packs owning one status colour or none —
  and naming four states as if the pack supplied them, which is an invitation to
  invent a hue. Rewritten for `orchard`, `editorial-luxury` and `briefing-room`.
- **`MOTION_DOCTRINE.md` §5 over-banned**, forbidding everything outside four
  properties while §2 prescribes an ease for colour changes. The ban is on
  layout, which is what its own rationale says.
- **ADR-0001 named a pack that never existed** (`lecture-hall`; the pack that
  shipped from graphify.com is `field-notes`). The decision stands; the example
  was written on a branch that never merged.

### Added — the half-library nobody declared

Six of twelve packs carry `## Components`, `## Hero`, `## Responsive` and
`## Signature element`; six do not, and nothing said which. Every pack now
declares **`Contract: core` or `Contract: widened`** above its Register, a core
pack states what it leaves the reader to decide, the `SKILL.md` routing table
marks it, and a check enforces the declaration against the headings present.

### Added — six checks, each watched failing on a planted defect

Counted claims (whitespace-normalised: the README's "six locked style packs" was
split across a line break) · exhaustive pack enumerations in both manifests, the
slash command, the CLI, the README and the Cursor rule · one name for the pack
contract · the `Contract:` declaration · the core role vocabulary (`--bg`,
`--ink`, and an accent role every pack resolves) · and **every stated contrast
ratio, recomputed from the token layer**.

The ratio check is scoped to claims whose base the document declares — a column
headed ``On `--bg` ``, an `on/over --token` phrase, or an `--on-X` name. A first
draft that inferred the partner produced 22 false positives out of 40.

### Fixed — three gates that could not fail

- **Deleting requirements made two gates quieter, and green.** Stripping a pack's
  four widened headings took `validate.py` 1270 → 1269 and `sloplint.py` 224 →
  223, both exit 0. **Ratchet floors** now live in `test/floors.json` and are
  enforced by all three.
- **One decoy comment disabled a slop-lint ban for a whole file, permanently.**
  The check took the first match only and `continue`d past a nearby negation
  word, so the counter fell and later occurrences went unexamined. Suppression is
  now per occurrence, and ban-quoting sections are exempted by heading.
- **`validate.py --self-test` printed OK for a self-test that did not exist** —
  the same defect the 2026-08-05 retrospective recorded in `validate_palette.py`.
  All three scripts now exit 2 on an unknown argument, and `validate.py` has a
  real self-test: six planted defects, run against a copy of the tree.
- **The slop lint read only fenced code blocks**, and no style pack contains one —
  so all twelve packs, `SKILL.md`, both bridges and the AI patterns were never
  linted. It now reads the inline CSS the packs prescribe in prose.
- **`npm test` and both workflows now run every gate and every self-test.** The
  release path was gated on one of three.

### Fixed — stale counts and reach

"six locked style packs" and "all six kits" (twelve), "T1–T7" (T1–T19), "Three
packs extracted" (eight), the pack contract called nine / ten / thirteen in five
places at once — one of which told an author to ship nine headings, which the
gate then passed. `plugin.json`, `marketplace.json` and the `/sheleg-design`
command named three packs of twelve, so nine could not be asked for by name.
`MOTION_DOCTRINE.md`, marked REQUIRED, appeared on no install surface: it is now
in the README table, the CLI help and banner, the slash command, and the Cursor
rule — which gains the whole doctrine in condensed form.

Gates: **1364 / 469 / 320**, from 1270 / 412 / 224.

## [1.9.0] - 2026-08-09

Four style packs, taking the library from eight to twelve — and a fix to the
thing that would have made twelve worse than eight.

Extracted from four live references on 2026-08-09. Three of them sell vector
databases and none of them collapse into each other; two are the same company's
project page and product page, and they share a type stack and nothing else.

### Added

- **`showroom`** — from [attio.com](https://attio.com/). A white gallery where
  one real product surface is the exhibit, under a **seven-layer shadow**. The
  reference declares its palette in **CIE Lab**, which this repo's palette gate
  cannot parse; every value was converted by painting it into a canvas and
  reading the sRGB bytes back — the browser's conversion, not ours.
- **`blueprint`** — from [pinecone.io](https://www.pinecone.io/). A drawing
  sheet: a 32px grid, ruled column boundaries, corner registration marks, one
  electric blue that works as ink *and* as fill at 7.53:1 both ways, and **no
  radius anywhere**.
- **`prism`** — from [milvus.io](https://milvus.io/). One static iridescent wash
  with a hard bottom edge, a heavy grotesque display over **mono body copy** —
  the inversion that makes a page read as a project rather than a company.
- **`maquette`** — from [zilliz.com](https://zilliz.com/). A near-black table
  with a cream axonometric model on it, mono block labels, and the only accent in
  this library's four new packs that works as text (15.49:1).
- Four reference kits, each with the six-component spine plus four signature
  parts, and four routing scenario pairs (**T16–T19**), every one with its
  negative branch.

### Fixed — the routing table, which was a list

**Five of the eight shipped packs named no other pack at all.** Forks existed
only in `field-notes`, `cyclorama` and `atrium`, and every one pointed backwards
at packs that never pointed back — so an agent entering at `instrument-console`,
which is where any infrastructure brief lands first, never learned that a
distinction existed. Four more one-way forks would have made twelve packs with
eight dead ends.

- `instrument-console`, `workbench`, `field-notes` and `cyclorama` each gain the
  mirror clause for the new pack that forks against them.
- **A new `validate.py` check enforces it:** a markdown link from one pack to
  another must be reciprocated. Watched failing against a planted defect before
  it landed.

### Fixed — in the packs, not in the references

- **`blueprint`'s reference sets pure black as body ink**, on 316 elements, which
  the doctrine bans. The pack ships the reference's *own* second ink `#111827`
  (136 elements) and does not pretend it is the same colour: the two sit **21.2
  apart** in OKLab.
- **`showroom`'s reference names `#A4ADBA` "caption-foreground"** and it measures
  **2.27:1** on its own white field. Kept, renamed `--disabled`, and captions
  routed to an ink that passes.
- **`prism`'s reference sets 72px display type in `#00B3FF`** — **2.36:1**, which
  fails even the relaxed large-text floor. The cyan is a fill in this pack.
- **Neither `blueprint` nor `prism` ships a `prefers-reduced-motion` branch** —
  zero blocks each, against live marquee, ping, pulse and scroll. Both packs
  require the branch their references omit.
- **`maquette`'s status palette is derived, not extracted**, and the token layer
  says so at the declaration. The reference exposes none; the first set this run
  reached for was a framework default, and the palette gate caught it colliding.

## [1.8.0] - 2026-08-08

An eighth style pack, and the first one whose reference already implements this
skill's own core pattern.

`cyclorama` is extracted from [codos.ai](https://www.codos.ai/): a pale field
that breathes through **six pastel stops on a 32-second loop** under near-black
ink that never moves with it, a **monospaced typewriter serif** over a
monospaced sans, one orange used only as a fill, and no shadows anywhere. Its
reference ships GSAP ScrollTrigger with real pinning and two WebGL canvases
whose formation holds and then redeploys — principle 3 in production rather than
in a doc.

### Added

- **`styles/cyclorama.md`** on the thirteen-heading widened contract plus
  `## Motion flavor`, with an addressable origin and every ratio computed by
  importing `test/validate_palette.py` rather than by a second implementation.
- **`styles/tokens/cyclorama.css`** — the six cycle stops as named tokens, one
  ease, three durations plus the 32s loop, a five-step radius ramp whose nesting
  is arithmetic, and an inline accent-dot cursor.
- **`kits/cyclorama/`** — the six-component spine plus four signature parts:
  `FieldStop` (the six stops as six static surfaces — the cycle itself does not
  cross the border), `AppWindow` (a hairline frame with **no fill**, so the
  field shows through it), `StatusPill` and `ComparePanel`.
- **`docs/adr/0001-style-pack-naming.md`** — restored to `main`. It was written
  on a branch that held at its stage-0 gate and never merged, so the decision
  register began at `0002` for four days while the rule it records was already
  binding. It is why this pack is `cyclorama` and not `codos`.
- **T15** in `test/scenarios.md` — a routing pair with its negative branch, so
  "is `cyclorama` distinguishable from `field-notes`?" can fail in the
  interesting direction.

### Fixed — in the pack, not in the reference

- The reference paints its section eyebrows in the accent on the field, which
  measures **1.71–1.97:1** across the six stops. This pack does not propagate
  it: the accent is a fill, eyebrows take `--ink-soft` at 8.36:1. The three
  darkened-orange candidates are recorded in `## Gotchas` **with their numbers**,
  because each one trades a WCAG failure for a colour-blindness collision with
  `--danger` or `--warning` — there is no text-safe orange in this palette, and
  the next reader should not have to rediscover that.
- The pack states that `--accent` and `--signal` sit 6.8 apart under protanopia
  and that **the palette gate cannot see it**, because `--signal` is not one of
  the names it treats as semantic. Written down rather than renamed around: a
  token renamed to satisfy a checker is worse than an unchecked token that says
  so out loud.
- The reference's own display fallback is `Fraunces`, which is **proportional**,
  while the face it replaces is monospaced — so a reader without the licensed
  font gets a hero that reflows rather than merely restyles. The pack ships
  measured substitutes instead (Courier Prime 0.600, Cutive Mono 0.605 against
  the original's 0.590).

## [1.7.0] - 2026-08-05

The Claude Design border, and the first code this skill has ever shipped.

`DESIGN_SYNC_BRIDGE.md` is the contract for pushing a pack to claude.ai/design
through Claude Code's bundled `/design-sync`, so the design agent builds screens
out of a pack's real components instead of generic ones. Like the Figma bridge,
it spends as much space on what does **not** cross: motion stays in code, and a
kit is the static half of a pack.

### Added

- `DESIGN_SYNC_BRIDGE.md` — seven sections, each a reference type or a border:
  what crosses and in what shape, style packs as the source of truth, the
  Figma/pack/Claude Design triangle taken one direction at a time, Lazyweb
  sweeps (layout crosses, identity does not), live-site extraction (the pack
  first, the sync second), what cannot cross, and round-trip discipline.
- A tool-presence-gated `## Optional — Claude Design (design-sync)` section in
  `SKILL.md`, gated exactly like the Lazyweb one. Cursor is unaffected.
- **Seven React reference kits** under `kits/<pack>/` — a six-component spine
  with identical names, props and types in every kit, plus each pack's signature
  components, built by `tsc` to `dist/` with a `.d.ts` tree, because the
  converter reads the built entry and the design agent codes against those types.
- `npx sheleg-design-skill --kit <pack> --out <dir>` materializes one kit and
  drops the pack document into `guidelines/` on the way.
- `--accent-ink` in `workbench`, `editorial-luxury` and `instrument-console`,
  additively. Text on the accent had no token in those three; `atrium` and
  `briefing-room` already had exactly this name. In `workbench` it flips with
  the theme, because white on the dark-mode accent is 3.2:1 and fails AA.
- `docs/DOCMAP.md` and `docs/adr/` — the repo's doc map and its decision home.
- Scenario `T14`, run green by a fresh agent holding only the installed bundle.

### Changed

- The validator gained eleven kit checks, including a prop-parity diff of the
  spine across every kit package. Each was watched failing against a planted
  defect before it landed.
- CI builds every kit in a matrix and asserts the build emitted something —
  `tsc` exits 0 when it compiles nothing.
- README's dependency-free promise gains its one honest caveat: the kits are
  code, they are not installed, and they appear only when asked for by name.

### Notes

- **The kits are not installed with the skill.** They ship in the npm package
  and are copied out on demand (`ADR-0002`), which is how the installed skill
  stays documentation while still having real components to hand.
- The live `/design-sync` push is a human step: the skill carries
  `disable-model-invocation`, so only a person typing the command can start it.
  Structure, build and materialization are proven; the upload is not yet proven
  in anger.

## [1.6.0] - 2026-08-05

The harvest of a 41-skill audit of the design skills installed on this machine.
The finding was narrow and repeated everywhere: the skill specified *what a
thing looks like* with real rigour and left *how much, how fast, and whether at
all* to whoever happened to be typing. Three of those four are now numeric, and
two of them are checked by a script.

Landed on top of 1.5.0, which shipped the `field-notes` pack from a concurrent
run in the same working copy. That pack was already written against the widened
contract below, so the two runs converged rather than collided — it is the first
and so far only pack on the thirteen-heading contract.

### Added

- **`MOTION_DOCTRINE.md`** — the missing half of the motion story.
  `SHELEG_DESIGN.md` says how motion is built; this says whether to build it.
  Frequency decides first, and it overrules taste: anything a user meets a
  hundred times a day does not animate, ever. Then the easing tree with
  `ease-in` banned in UI and the reason stated, three named curves, a duration
  table with a 300 ms ceiling, springs in Apple's notation, and interruptibility
  as the actual argument for reaching for one. Then the forms that are defects
  rather than preferences — scroll listeners, continuous input held in component
  state, blur and grain on scrolling containers, easing under `scrub`,
  `useEffect` where `useGSAP` belongs, and layout transforms silently erased by
  animated ones. Closes on anti-drift: the tokens are right and the built page is
  generic anyway, which happens at application time and so is named there.

- **Three calibration dials** — `DESIGN_VARIANCE`, `MOTION_INTENSITY`,
  `VISUAL_DENSITY`, baseline `7 / 5 / 4`, read off the brief from a table. A
  pack answers *which register*; it never answered *how far*, which is how a
  regulated insurer and a design studio came out of one pack looking alike. The
  dials are deliberately weak where the pack is strong: no dial invents a
  colour, a face or a radius, and `MOTION_INTENSITY` sits **under** the
  frequency table rather than over it.

- **A widened pack contract — nine headings to thirteen.** `Components`,
  `Hero`, `Responsive` and `Signature element`. The packs were precise about
  colour and motion and then went quiet exactly where implementations drift:
  per-component states, the opening viewport, collapse behaviour, and the one
  element a page is remembered by. The skeleton also now teaches concentric
  radius arithmetic, a `Not for` line in `Register`, and that an origin nobody
  can re-read is decorative.

- **`test/validate_palette.py`** — the colour part is computable, so it is
  computed. Claimed contrast ratios are re-derived from the hex and compared,
  WCAG floors are enforced, and semantic colours are checked for separation in
  OKLab under protanopia, deuteranopia and tritanopia. A pack may sit under the
  floor only if it states out loud that colour is never the only carrier.

- **`test/sloplint.py`** — the skill is held to its own bans. The token layers
  and every fenced example are read for `100vh`, scroll listeners, bare
  `ease-in`, transitions on layout properties and pure black fields; and the
  tables the docs promise are asserted by string, so a rule cannot be deleted
  without failing the build. Both scripts ship a `--self-test` that watches every
  check fail against a planted defect — a green from a check nobody has seen say
  no is not evidence.

- **A six-layer scene depth model**, a **parameter handoff to the built-in
  `dataviz` skill** instead of duplicating it, and a **`?variant=` procedure**
  for choosing between packs by mounting them on a populated page rather than
  arguing about them.

- **The three generated looks that are defaults rather than decisions** —
  recorded so a page that lands on one has to say whether that was a measurement
  or the default talking.

### Changed

- **The pack section gate is all-or-nothing.** The nine original headings stay
  required; adopt one of the widened four and all four are owed. The six packs
  that shipped before the widening stay valid on nine — backfilling them
  honestly needs re-reading each live reference, and three record a product name
  where an address belongs, so they cannot be re-read at all. Filling those
  sections from the token layer instead would be inventing values with a
  citation attached, which is the failure the pack layer exists to prevent. The
  rule closes the gap either way: no pack can be half-widened, so a new pack
  cannot copy the thirteen-heading skeleton, keep the cheap nine and pass.
- `npm test` now runs three gates, not one. `npm run selftest` runs the planted
  defects.
- `package.json` described "three locked style packs" while six shipped.

### Not shipped, deliberately

- **An eighth `industrial-brutalist` pack.** The register is real and the set
  lacks it, but the only description available carries a synthesised palette,
  not one measured off a production site. Held rather than authored.
- **A backfill of the six existing packs onto the widened contract.** Same
  reason, from the other direction: three of them cannot be re-read.

## [1.5.0] - 2026-08-04

> **Never released on its own.** There is no `v1.5.0` tag and no `1.5.0` on npm,
> so `npm install sheleg-design-skill@1.5.0` and `git checkout v1.5.0` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

The register the skill was missing for its own audience: a developer tool that
does not live on a dark console. Six packs could dress a landing page, a
dashboard, a deck and two kinds of consumer health, and none of them had an
answer for open-source software sold on *being checkable* — which is most of
the software the people using this skill actually build.

### Added

- **Seventh style pack: `field-notes`** — extracted from **graphify.com**
  (2026) by reading its live computed styles: 92 declared custom properties,
  the served `@font-face` set, every authored rule pulled out of the CSSOM, and
  a contrast pass over all 38 colour pairs in the system. Warm off-white paper
  with a green cast (`#F8F7F0`), near-black green-cast ink (`#16211B`, 15.4:1),
  one rust accent (`#9A3F28`), and a complete dark twin.

  Its defining composition is what separates it from every warm pack already
  here: **the page is one continuous sheet ruled by a `1px` hairline.** Ten of
  the reference's sixteen sections are divided by nothing but that line; three
  add a 40% wash. Where `orchard` stacks discrete slabs and `atrium` runs a
  continuous field that changes layout, this one draws a rule and keeps going.

  The hero is the other half of the idea: not a dark band but a **dawn** —
  eight stops from `#062A22` to the exact paper colour, so the dark has no
  edge. Over it, an inline `feTurbulence` grain at `baseFrequency 0.82`, a
  radial vignette, and an ambient layer that is **notation rather than
  particles**: mathematical glyphs at 14% opacity, one at a time flipping to
  the verified hue.

  It also carries the two devices most worth stealing. **The numbered eyebrow**
  — `〉 HOW IT WORKS [03/09]`, built from `::before`/`::after` on a `data-n`
  attribute — makes a marketing page into a document with a table of contents.
  And **printer's crop marks** at the four corners: eight 1px gradient arms,
  `inset: 14px`, ink at 30%, desktop only. Both cost nothing and both state the
  thesis that the page is a printed record.

  Elevation is a **ring** (`0 0 0 1px var(--line)`), not a shadow; radii are a
  proportional ramp off one `--radius`, so a hardcoded `12px` is banned; and
  motion is two eases doing two jobs — `.15s` `cubic-bezier(.4,0,.2,1)` for
  control state, `.5s` `cubic-bezier(.22,1,.36,1)` for scroll entry — with one
  rule on top: **only the verified hue ever animates colour.** The rust never
  moves, because a brand that animates stops reading as an identity and starts
  reading as a status.

  Four corrections to the reference ship with it, each measured. Its hero
  accent phrase — the single most prominent piece of text on the site — runs
  the light brand over the gradient at **2.29:1** at the top and **1.41:1** in
  the middle; the pack adds `--brand-on-dark` `#CF7A52` (**4.82:1**) and bans
  the other. Its `--verify` green is 3.2:1 on paper and its own
  `--verify-foreground: #fff` is 3.4:1 on the green, so both are fills and the
  labels take `-ink`. It sets `color-scheme` nowhere despite a complete dark
  theme — the same trap that bit `workbench`. And it paints three unrelated
  dark palettes (warm-brown theme, forest bands, navy terminal) plus an app
  layer whose neutrals drift browner than its page layer and whose ring is a
  violet used nowhere else; the pack reconciles all of it to the forest family
  and the page's own neutrals.

  The pack ships that app layer deliberately, with a routing rule rather than a
  turf war: `workbench` stays the default for neutral product UI, which should
  disappear; `field-notes` is for a product whose console must read as the same
  paper as its site.

- **`AI_PRODUCT_PATTERNS.md` gains the provenance pattern** (§4), promoted out
  of the pack because it is the reference's one genuinely transferable
  invention and a direct extension of the file's existing *honest state* rule:
  **label the part, not the whole.** A single confidence number on a mixed
  answer hides exactly the clause the reader needed to check, so the pattern
  attaches a small set of named states — `[EXTRACTED]` · `[INFERRED]` ·
  `[AMBIGUOUS]` — inline to the span each one qualifies, with three tests for
  whether it is honest: every state must be reachable, every label must derive
  from something real, and if you cannot say which words a state covers you do
  not know it well enough to show it. Any pack can implement it on three hues.

- **Test scenario T13** — the developer register **and** the fork against
  `instrument-console`, run as two prompts in separate contexts. The pack is
  only worth its row if an agent can tell "this product has a source" from
  "this product has a dial", so a pass requires both branches: one that must
  select `field-notes`, one that must stay on the dark console.

### Changed

- `SKILL.md`, `README.md`, `bin/cli.js`, `install.sh` and the Cursor rule all
  learn the seventh pack; the CLI's help and the README's file table stop
  saying "six".

## [1.4.0] - 2026-08-03

> **Never released on its own.** There is no `v1.4.0` tag and no `1.4.0` on npm,
> so `npm install sheleg-design-skill@1.4.0` and `git checkout v1.4.0` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

Two packs for the warm consumer register, extracted from two production sites
that solve the same brief in opposite ways — one premium and editorial, one
friendly and modular. Between them they replace the reflex a generated wellness
page falls into (a gradient, three cards, a stock photo of someone stretching).

### Added

- **Fifth style pack: `atrium`** — the warm consumer register, extracted from
  **functionhealth.com** (2026) by reading its live token layer and computed
  styles. The skill could already do dark-technical, editorial, product UI and
  decks; it had no answer for *premium consumer health* — the page that has to
  land a serious clinical claim without a sterile surface anywhere on it.

  What it encodes: **one continuous cream field with no dark bands** (sections
  are separated by a 48→99px rhythm and a change of layout, never by flipping
  the background — the reflex that makes generated pages read as a stack of
  slabs); a single terracotta accent `#B05A36`; a serif that ships **one
  weight, 300**, set at `line-height: 0.9`, whose entire emphasis vocabulary is
  *one italic accent phrase* per heading; a sans with only 300 and 600 in it;
  mono reserved for exactly one component; a fully fluid `clamp()` scale keyed
  to a single 23.5rem→90rem band, so the page resizes as one object; hairline
  and cream-on-cream steps instead of shadows, with three shadows that each
  have one job; and `999px` on everything clickable.

  Its signature motif is the **fluted-glass hero**: a WebGL shader refracting
  photography through reeded-glass ribs, shipped with the real numbers (82.8
  ribs at `0.36rad`, amplitude `0.0255`, feather `0.63`, a 7.2s reveal cycle,
  the ink scrim at 70%) over a still-image fallback. Its lifecycle is the pack's
  most useful lesson: context-lost, tab-hidden, reduced-motion and no-WebGL are
  four branches that ship in the same commit as the effect.

  It also promotes something the reference does that most sites do not: **every
  autonomous motion carries a visible `PAUSE MOTION` control**, and the pack
  bans shipping one without it — `prefers-reduced-motion` alone does not
  discharge the obligation.

  Three measured contrast traps are carried as Gotchas rather than left for an
  audit: the accent is AA on the field (4.6:1) but **fails on the cream surface**
  (4.2:1); `--good`/`--info` are fills at 2.1:1 and 3.4:1 and may never be text;
  and the hairline is 1.6:1 — decorative strength, not affordance strength, so
  controls need `--line-strong`, `--line-ink` or `--accent` instead.
- **Sixth style pack: `orchard`** — the same buyer, the opposite voice,
  extracted from **gutgutgoose.com** (2026). Where `atrium` is one continuous
  field, `orchard` is **a stack of rounded slabs**: every section is a card with
  its own fill (oat, sage, cacao), no two adjacent slabs repeat, and the field
  shows around all of them. Its whole layout rhythm is four numbers — `64px 24px`
  slab padding, `44px` between blocks, `55px` between slabs, `36px` card padding.

  Three colours with fixed jobs — oat is the paper, sage is the brand, candy
  orange is the verb — and the pack's most useful rule is that **two of them are
  not text colours**. A rounded geometric display at Medium carries all
  hierarchy, so body weight never goes above 500; the price is deliberately set
  in the body face, because a rounded display numeral reads as branding and a
  price has to read as a fact.

  Its signature material is **light, not shadow**: the "candy pill" is a flat
  fill wearing two inset white hairlines (`.8` top, `.35` bottom) plus an
  ambient glow **in the button's own hue** — the only real drop shadow in the
  system. Its one cinematic move is a **word-by-word scrubbed headline** (opacity
  only, ~12% of hero scroll per word) beside a sticky visual column, and that is
  the entire motion budget.

  The reference is strong on composition and weak on contrast, so the pack
  carries the three measured failures with fixes from inside its own palette:
  the CTA label is **2.8:1** (white on orange) and must use the cacao ink for
  **5.6:1**; body copy on the sage slab is **3.4:1** — and oat on sage is
  **2.96:1**, under even the large-text floor — so small text moves to
  `--primary-deep` at **4.9:1**; and the 60% ink is **4.1:1** on oat, a caption
  colour only. It also ships the `prefers-reduced-motion` branch the reference
  has nowhere on the site.
- `scenarios.md` gains T11 and T12 for the two consumer registers.

### Changed

- README, `SKILL.md`, `bin/cli.js`, `install.sh` and the standalone Cursor rule
  route and ship both new packs; the stale "three style packs" counts in the
  README are corrected to six, and the Cursor rule — which had listed only three
  packs and never gained `briefing-room` — now names all six.

## [1.3.4] - 2026-07-30

### Added

- **`displayName`** ("SHELEG Design") in both manifests — the `/plugin` picker
  falls back to `name`, which is kebab-case for namespacing reasons.

## [1.3.3] - 2026-07-30

### Fixed
- **`argument-hint` in the slash command was unquoted.** In YAML a bare
  `[a | b]` is a flow sequence, not a string, so the hint parsed as a *list*.
  Found by `claude plugin validate --strict`, the upstream schema checker, which
  now runs in CI on both this plugin and its marketplace manifest.
- **`homepage` and `repository` sat at the top level of `marketplace.json`,
  where Claude Code does not recognize them.** They are plugin-entry fields;
  moved there, so the values reach the plugin listing instead of being ignored.

## [1.3.2] - 2026-07-30

### Changed

- **The licence is declared in both manifests** — SPDX `license: MIT` in the
  `marketplace.json` plugin entry and in the skill's front matter (mirrored into
  the `.cursor` copy, which the validator holds byte-identical). The `LICENSE`
  file was always present and visible on neither surface a user actually reads.

## [1.3.1] - 2026-07-30

### Changed

- **README** — the family list gained `agent-sync`, and the install block now
  carries all three family commands (`install`, `update`, `list`) with the
  restart note; skills and hooks load at session start, so the session that
  updates is not the session that gets the new ones. The registry copy of the
  README is what most people read, and it only moves on a release.
- `CONTRIBUTING.md` — how to run `test/validate.py` and what a PR is checked
  against.

## [1.3.0] - 2026-07-29

### Added

- **Fourth style pack: `briefing-room`** — a register the skill had no answer
  for. Decks are among the most-requested things people ask an agent to build,
  and the default output is bullet lists on a gradient. Extracted from a
  production investor-deck site (2026) by reading its live token layer; the
  source is **anonymized at the owner's request**, so the `Origin:` line says
  what it is without naming it — the values are still extracted rather than
  invented, which is the point of the rule.

  What it encodes: a fixed **1280×720 canvas with `overflow: hidden`** (content
  that does not fit becomes a second slide — never a smaller type ramp); the
  first **OKLCH** token layer in the skill, where every neutral is the accent
  hue `254` starved of chroma, so the palette cannot drift into two designs;
  Inter at tight optical tracking against JetBrains Mono furniture at `+0.14em`
  to `+0.18em`; a two-part veil that protects text over artwork **without**
  fading the artwork; 1-bit dithered art as the only imagery; mono numbered
  section headers; **the slide title is a claim, not a label**; one bespoke
  diagram per slide instead of bullets; exactly one highlighted phrase per
  deck; and every number carrying its source.

  Its motion position is a deliberate inversion of the rest of the skill:
  **slides never animate**, because the presenter's voice is the timeline.
  `prefers-reduced-motion` is a no-op by construction rather than by neglect.

  Two honest notes carried as Gotchas: a fixed canvas fails *silently* (clipped
  content is invisible in review and obvious in the room), and the reference
  shipped no print or reduced-motion branch — the pack requires both.
- `scenarios.md` gains T10 for the deck register. Gate: 194 → 220 checks.

## [1.2.0] - 2026-07-29

Worked through Figma's *State of the Designer 2026* (NewtonX, 906 digital
designers across five regions, surveyed September–October 2025). It is a survey
of the profession — AI adoption, what designers mean by craft, satisfaction,
regional outlook — **not** a visual-trends report, so nothing here is a "trend"
invented from it. Two findings were actionable, and one was a gap in this skill.

### Added

- **`AI_PRODUCT_PATTERNS.md`** — the surfaces a model drives, which the skill
  had nothing to say about while the survey ranks *designing AI-driven
  products* the **third most in-demand skill (37%)**, ahead of motion design
  (29%) and information architecture (19%). Organizing rule: **honest state**.

  Contents: the five states of a model call (idle · working · complete ·
  refused/needs-a-human · failed — a refusal is not an error and a rate limit
  is not a crash); streaming instead of spinners, with a stop control from the
  first frame, a reserved container and no fake typing delay; latency as two
  numbers (time-to-first-token is the one users feel); provenance and
  uncertainty (cite or don't claim, no confidence theater, show the context the
  model actually used); agent actions where the confirmation *is* the design —
  the diff/recipient/query shown before it runs, explicit consent for anything
  irreversible or outward-facing, undo for what's cheap; empty states that
  carry the capability; chat as a shape rather than the shape; cost and scope
  as visible state; and a ban list. Pairs with `workbench` and reuses its
  status tokens.
- **The craft bar** in `SKILL.md` — a definition of done ordered by what
  designers actually mean by craft in that survey: visual polish (58%),
  thoughtful problem solving (47%), clear intuitive UX (36%), emotion and
  delight (35%), consistency (15%). Item 3 is explicitly *not* this skill's
  half — if flows and states aren't decided, the honest move is to stop.
- Discovery, the Cursor rule, the README and both installers cover the AI-UI
  direction; `scenarios.md` gains T9.

### Fixed

- **The validator enforced five of the nine required pack headings** while the
  0.9.0 entry, `CONTRIBUTING.md`, the README and the wiki all claimed the full
  contract was gated. Exactly the promise-without-a-check defect this repo
  keeps hunting, living inside the checker itself. All nine are now enforced
  (`Motion flavor` stays conditional — `workbench` is standalone and has no
  motion layer to flavor), which is also why the check count jumps to 194.

## [1.1.1] - 2026-07-29

### Fixed

- `FIGMA_BRIDGE.md` described the mapping without mentioning that the official
  Figma MCP **gates its main tools behind guidance skills** (`/figma-use`
  before `use_figma`, `/figma-create-new-file` before `create_new_file`,
  `/figma-design-to-code` before `get_design_context`) — the server names
  skipping them the cause of hard-to-debug failures. An agent following the
  bridge alone would have called them bare. The doc now says to load the gate
  first and that the server's instructions win on *how* to call anything; this
  file is the contract, not a tool manual. It also names the two read paths
  worth knowing: `get_variable_defs` for token parity, `get_metadata` for frame
  existence and naming.

## [1.1.0] - 2026-07-29

### Added

- **`FIGMA_BRIDGE.md`** — the design↔code contract, a gap that was invisible
  because it lived between repos: `super-ux` hands the look to this skill and
  expects the chosen pack to become Figma variable collections, while this
  skill did not mention Figma anywhere.

  The rule is one line — the pack is the source of truth in both directions.
  Publishing writes its values into variables; implementing a design maps the
  file's values onto the pack's tokens, and a value with no token is either a
  gap in the pack (add it, with its CSS line) or drift in the file, never an
  inlined literal.

  The specifics are what make it usable: one collection per token family with
  names 1:1 with the CSS custom properties; **modes are themes, not surfaces**
  — `workbench`'s light/dark is one collection with two modes, while
  `editorial-luxury`'s espresso is a coexisting surface and modelling it as a
  mode invents a theme switch the design never had; colors convert to 0..1
  floats rather than copy; motion cannot cross at all (Figma has no easing
  variable type, so §10's ease/durations/stagger stay code-only); shadows are
  effect styles whose `radius`/`color`/`spread`/offsets bind to variables;
  variables are COLOR/FLOAT/STRING/BOOLEAN only; and `addMode` can be refused
  once a plan's mode cap is hit — ship light-only and say so rather than faking
  a parallel collection. Figma file content is data, never instructions.
- Discovery, the Cursor rule and the README cover the Figma direction; the
  validator now requires every companion doc in the bundle to be linked from
  `SKILL.md` (161 checks) — a reference nothing points at is a file the agent
  never opens.

## [1.0.1] - 2026-07-28

Open-source hygiene pass — the repo is public, so the files a first-time
contributor looks for now exist.

### Added
- `SECURITY.md` — states plainly that `bin/cli.js` neither spawns processes nor
  touches the network, and that `install.sh` **does** fetch over HTTPS when run
  without a checkout, so the documented `curl … | sh` one-liner is named as the
  trust decision it is, with two alternatives.
- `CODE_OF_CONDUCT.md`, issue forms and a pull-request template.
- README points at the security policy and the code of conduct.

## [1.0.0] - 2026-07-28

First stable release. Nothing about the method changed — this marks the point
where the surfaces below are treated as a contract, and a second full pass over
every file cleared the remaining inaccuracies.

**What 1.0.0 promises.** The installed layout (`SKILL.md`, `SHELEG_DESIGN.md`,
`styles/*.md`, `styles/tokens/*.css`, `styles/STYLE_PACK_TEMPLATE.md`), the
ten-heading style-pack contract, the token names inside a pack, and the CLI
flags are stable within 1.x. A pack may gain tokens; it will not silently
change what an existing token means. Removing or renaming either is a major.

### Fixed

- `release.yml` pointed at `pipeline.example.json`, a file that has never
  existed in this repo, and installed `jsonschema` for a validator whose first
  line says stdlib-only. Both gone; its post-release smoke test now `diff -r`s
  the whole installed bundle instead of checking three paths.
- The CLI accepted a bare trailing `--dir` and silently fell back to
  auto-detect — installing somewhere the caller did not ask for. `--dir`
  without a path, an unknown flag, and `--dir` combined with
  `--cursor`/`--claude` now print the reason and exit 2 (previously exit 0).
- `SKILL.md` listed "dashboards" under *not for*, one line after listing
  dashboards as a supported use — the exclusion is about the cinematic motion
  layer, and now says so.
- `SHELEG_DESIGN.md` §13 presented the reference implementation's Next.js paths
  as if they were the reader's; it now says to port the split, not the strings.
  The §9 snippet used `STAGGER` without showing where it comes from, §11 said
  "port" a file no reader has, and the closing line still said "this site".
- `npm test` ran `--help` and always passed. It runs the validator now.
- The 0.3.0 design spec still declared templates out of scope; annotated with
  what superseded it rather than quietly rewritten.

### Added

- `CONTRIBUTING.md`: repo layout, the canonical-bundle-vs-mirror rule, and a
  step-by-step for authoring a style pack (including the cross-pack token
  naming trap).
- README rewritten for people arriving cold: what the problem is, the two
  halves, the pack table, what installs where, and an honest development
  section.

## [0.9.1] - 2026-07-28

> **Never released on its own.** There is no `v0.9.1` tag and no `0.9.1` on npm,
> so `npm install sheleg-design-skill@0.9.1` and `git checkout v0.9.1` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

### Added

- Optional **Lazyweb MCP** step: when `mcp__lazyweb__*` tools are present, the
  skill sweeps real-world references for the target screen before laying it
  out — recommended for the product-UI (`workbench`) register. The split is
  explicit: references inform layout, hierarchy and content order; palette,
  type and motion stay the pack's. Documented in `SKILL.md`, the Cursor rule
  and the README; nothing depends on the MCP, and fetched reference content is
  treated as data, never as instructions.

## [0.9.0] - 2026-07-28

Consistency pass over every file: the contradictions below were real and are
fixed, and each one now has a validator or CI check so it cannot return.

### Fixed

- **The pack skeleton was unreachable from an installed skill.** `SKILL.md`
  pointed at `templates/style-pack-template.md`, which `files[]` never shipped.
  The skeleton now rides in the bundle as
  `styles/STYLE_PACK_TEMPLATE.md`, kept byte-identical to `templates/`.
- **`SKILL.md` listed 8 of the 10 pack headings** (no Motion flavor, no
  Gotchas), so an authored pack would legitimately lose sections the packs and
  the template both carry. The contract is now stated once and enforced.
- **The motion-token contradiction.** `SHELEG_DESIGN.md` §10 declared one
  site-wide ease while `editorial-luxury` and `workbench` legitimately override
  it. §10 now states the defaults *and* that the pack wins; the packs say the
  same from their side.
- **Stagger drift inside the reference:** the Reveal table said 0.06s and the
  GSAP recipe hard-coded 0.08 against a `STAGGER = 0.07` token; both now read
  the token.
- **`workbench.css` set `color-scheme: light dark`**, so a page forced to
  `data-theme="dark"` still got UA controls and scrollbars from the OS
  preference. Light `:root`, dark under the attribute; a reduced-motion block
  zeroes the duration tokens.
- **`--accent-dim` meant opposite things across packs** (a pressed darker blue
  in `instrument-console`, a 12% tint in `editorial-luxury`). The tint is now
  `--accent-weak`, matching `workbench`'s naming.
- **`workbench.md` shipped prose where tokens belong** ("amber", "red",
  "`#1a7f37`-family") — the table now carries the exact light/dark pairs from
  the CSS, and `--info` is documented as deliberately the accent hue.
- **CLI help still advertised two style packs** (the success message had been
  fixed, the help text had not), and the bundle blurb omitted the token CSS.
- **The Cursor rule promised product-UI guidance it never gave** — it now
  carries a self-contained workbench contract for agents without the skill
  installed.
- README, `marketplace.json`, and the `/sheleg-design` command all described a
  landing-page-only skill; all three now state the product-UI half.
- Reference cleanups: ASCII architecture diagram re-aligned (the fan-out
  connector was one column off the store box), `bias` added to the store
  fields it lists, the `936 = 24 × 13 × 3` factorization disambiguated from
  scene indices, and a product-specific closing-line example genericized.

### Added

- Validator (146 checks, was 101): the **whole** `.cursor/` mirror is compared
  against the plugin bundle file-by-file in both directions (previously only
  `SKILL.md`), the full ten-heading pack contract is enforced on every pack and
  on the template, the shipped template must match `templates/`, and every pack
  must be routed from the `SKILL.md` table and named in the CLI output.
- CI installs through both channels and `diff -r`s the result against the
  bundle, so a file that reaches one installer and not the other fails the run.
- `test/scenarios.md` gains T7 (authoring a new pack against the contract).

## [0.8.0] - 2026-07-28

### Fixed
- The Cursor channel copy of `SKILL.md` could drift from the plugin copy without
  anything noticing. The validator now compares them and fails on drift.

### Changed
- `RU triggers - …` replaced with English-first pairs
  (`"design tokens" / "дизайн-токены"`), so the description reads as English
  with localized aliases.
- README is English-only, with a plain statement of what the skill gives you and
  an author/links block.

### Added
- Validator enforces the description canon: `Use when` opening, Russian trigger
  aliases present, front-matter under 1024 characters.

## [0.7.0] - 2026-07-25

Review pass.

- **FIX: `SHELEG_DESIGN.md` pointed at a non-existent `DESIGN.md`** and hard-coded
  the instrument-console palette in the build recipe, contradicting the
  style-agnostic method — §11 now says to implement the chosen style pack's tokens.
- **Toggleable release automation** (`.github/workflows/release.yml`, off unless
  `RELEASE_ENABLED` is set): the repo shipped 0.2.0–0.6.0 with no tags and no
  GitHub releases.
- README gains a Russian section; `package.json` `files[]` ships `CHANGELOG.md`;
  a stray untracked `.claude/skills/sheleg-design` plain copy was removed and
  `.claude/` gitignored (it shadowed the plugin).

## [0.6.0] - 2026-07-20

> **Published, never tagged.** `0.6.0` is installable from npm but there is no
> `v0.6.0` tag, so the artifact exists and the commit it was cut from cannot be
> checked out. A bug report against this version has no source tree to read
> (2026-08-17, umbrella `B-71`).

### Added

- Ready-made token layers `styles/tokens/<pack>.css` for all three packs
  (copy verbatim instead of transcribing tables; workbench ships light +
  `data-theme="dark"` twins). Validator requires a tokens file per pack.
- Motion-flavor sections in the cinematic packs (particle tint/energy,
  Reveal set, instrument styling per style).
- Versioned release test scenarios (`test/scenarios.md`, T1–T6) encoding
  the RED/GREEN history.
- Validator installer-sync check (every bundle file shipped by install.sh;
  npx CLI now walks the bundle at runtime — adding a pack no longer
  touches installers) and a CI negative self-test (validator must FAIL on
  a corrupted version).
- Style-pack authoring skeleton `templates/style-pack-template.md`;
  `/sheleg-design` accepts a pack name argument.

### Fixed

- Discovery gap: skill description (and Cursor rule) now trigger on
  product-UI tasks — dashboards, admin tools, design tokens, light/dark
  themes (EN + RU) — previously such tasks never loaded the skill.
- Stale manifests: package.json / marketplace / plugin descriptions and
  the Cursor rule now mention style packs incl. workbench.

## [0.5.0] - 2026-07-20

> **Never released on its own.** There is no `v0.5.0` tag and no `0.5.0` on npm,
> so `npm install sheleg-design-skill@0.5.0` and `git checkout v0.5.0` both fail. This section
> describes work that shipped inside a later version. The note is here because
> the section reads as a release (2026-08-17, umbrella `B-71`).

### Added

- **`workbench` style pack** — quiet light+dark utilitarian product UI for
  dashboards, admin panels, and internal/dev tools: neutral grays, borders
  as elevation, one functional blue accent, system + mono type, canonical
  atoms (status dot, chip, stat tile, sparkline), honest-state and
  glanceability rules. Blended from the Builder Pro AI production design
  system and GitHub-style border discipline. Usable standalone — SKILL.md
  now routes dashboard/tool requests to this pack instead of excluding
  them outright.

## [0.4.0] - 2026-07-19

> **Published, never tagged.** `0.4.0` is installable from npm but there is no
> `v0.4.0` tag, so the artifact exists and the commit it was cut from cannot be
> checked out. A bug report against this version has no source tree to read
> (2026-08-17, umbrella `B-71`).

### Added

- **Style packs** (`styles/`): the motion methodology is now style-agnostic
  and pairs with a chosen visual identity pack. Two packs ship:
  `instrument-console` (near-black aerospace console, electric-blue signal
  — the original reference style) and `editorial-luxury` (warm cream +
  espresso + sage, Fraunces/Newsreader/JetBrains Mono, dossier motifs —
  extracted from the prowl.chat production design system). Each pack locks
  palette/type/texture/motion tokens, signature motifs, and bans; SKILL.md
  documents the pack contract for authoring new styles.
- Installers (npx CLI, install.sh) ship the `styles/` directory; validator
  enforces >=2 packs with required sections.

## [0.3.0] - 2026-07-19

> **Published, never tagged.** `0.3.0` is installable from npm but there is no
> `v0.3.0` tag, so the artifact exists and the commit it was cut from cannot be
> checked out. A bug report against this version has no source tree to read
> (2026-08-17, umbrella `B-71`).

### Added

- Claude Code marketplace layout: `.claude-plugin/marketplace.json` +
  `plugins/sheleg-design/` (plugin.json, `/sheleg-design` command, skill).
  Installable via `/plugin marketplace add ssheleg/sheleg-design-skill` and
  discoverable by the vercel-labs `skills` CLI.
- Cursor rule `cursor/rules/sheleg-design.mdc` (self-contained, no relative
  links).
- Repo consistency validator `test/validate.py` + GitHub Actions CI
  (`validate.yml`: validator, `node --check`, CLI smoke test).
- POSIX fallback installer `install.sh` (local checkout / curl / wget).
- Russian trigger phrases in the skill description.

### Changed

- Skill bundle moved from `skill/` to
  `plugins/sheleg-design/skills/sheleg-design/`; the npx installer copies
  from the new location (installed layout unchanged).

## [0.2.0] - 2026-07-19

> **Published, never tagged.** `0.2.0` is installable from npm but there is no
> `v0.2.0` tag, so the artifact exists and the commit it was cut from cannot be
> checked out. A bug report against this version has no source tree to read
> (2026-08-17, umbrella `B-71`).

### Changed

- SKILL.md reworked to skill-authoring canon: trigger-only description
  (no workflow summary), canonical sections (Overview / When to Use / Core
  Pattern / How to Apply / Quick Reference / Common Mistakes), ~590 words,
  explicit REQUIRED REFERENCE pointer to SHELEG_DESIGN.md.
- Reference doc genericized (removed source-repo-specific `v2` paths).
- Verified with subagent scenarios (trigger, application, retrieval) before
  and after the rewrite.

## [0.1.0] - 2026-06-11

### Added

- Initial release: SKILL.md + SHELEG_DESIGN.md bundle and the zero-dependency
  `npx sheleg-design-skill` installer (auto-detect `.cursor`/`.claude`,
  `--cursor`, `--claude`, `--dir`, `--force`).
