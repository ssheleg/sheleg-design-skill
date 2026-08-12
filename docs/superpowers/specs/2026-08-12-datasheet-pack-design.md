# Design record — `datasheet`, the fourteenth style pack

Companion to `2026-08-12-datasheet-pack-brief.md`. What was measured, what was
decided, and which of the brief's premises the measurement refuted.

## The premise the measurement killed

The brief opened with the register *"the page is a spec sheet and the data lives in
a **dark instrument window** cut into it"*, taken from the Refero style card, which
describes the reference's product panels as *"often dark and terminal-like,
creating a high-contrast focal point against the airy background."*

**That is false of the page as it ships.** Measured at 1440x900: the hero's focal
element is a **light** frame on `#ffffff` containing a hairline-ruled grid of
label-over-value cells, a map, green-tinted status rows and a pink-tinted gauge.
There is no dark panel in the first viewport, and no element on the page has a dark
background at all.

The dark surface is real, but it is **not a window — it is a state.** The token
`--dash-dark: #2e2e2c` appears in 97 rules and every one is
`.Demo-module--incognitoStyle` or `.VisitsHistorySection--isIncognito`: 134 rules
in total re-skin the instrument dark **when it detects the visitor is in
incognito.** The product's argument completes itself without a sentence of copy.

That is the pack's identity, and it is sharper than the premise it replaced. It is
also the exact failure `DESIGN_SYNC_BRIDGE.md` §4 exists to prevent — a Refero
style is a *candidate source*, and the pack comes from the live site. Recorded here
rather than quietly fixed, because a false claim in a record is worse than the
defect it describes.

Refero was wrong or stale in four measurable places, all corrected from the live
site: the display weight (it says 600, the site computes **500**), the page
container (1232px against a measured **1248px**), the section rhythm (a 48px gap
against measured **full-bleed alternating bands with `margin: -1px`**), and the
focal panel being dark (it is light, with a dark alarm state).

## What the reference actually gave

Read off `/styles.6f4ca5130282f8853ea6.css` and live computed styles at 1440x900
and 500x844 on 2026-08-12:

- **140 custom properties**, including ten-step ramps for grey, red, orange,
  yellow, green, teal, blue, purple and pink. This is why almost nothing in the
  token layer had to be selected: a value for a role the reference does not paint
  is usually a different *step* of a ramp it already ships.
- **One duration token** — `--t-normal: 250ms` — spent across 119 transitions, and
  a measured **130ms** stagger between the three word-spans of the headline
  (delays 0.000215s, 0.130447s, 0.261s, each rising over 0.3s).
- **`html { font-size: 8px }`**, matching its own `--grid-base`, so every `rem` in
  that stylesheet means an eighth of what it means in a default host. The token
  layer therefore states lengths in px, and the reference's odd `7.21px` button
  padding is `0.9rem` at that base.
- **A radius family with real arithmetic**: 16 on the outer frame carrying 8px of
  padding, whose inner shell reads 8px. `16 − 8 = 8` — the template's concentric
  rule, proven on the reference rather than asserted.
- **Statuses already accessible on paper**: its clean cell is `--green-9` text on a
  `--green-2` tint, measured 8.12:1. The light status set follows that rule.
- **Focus taken seriously**: 80 rules, all `outline: .25rem solid var(--orange-7)`
  — 2px at that rem base.

## The four decisions the numbers forced

**1. The primary button moves one ramp step.** White on `--orange-7` measures
**3.32:1** at a 14px/500 label. Two repairs were computed rather than guessed: ink
on the reference's own fills clears at rest (5.55:1) but fails on hover (3.45:1);
the fill at `--orange-8` with white clears at rest (5.34:1) and hover at
`--orange-9` clears at 9.02:1, keeping the reference's darkening direction. The
second shipped. No colour was invented — both steps are the reference's own.

**2. One ink, not two.** The reference's `body` computes `#141415` and its `h1`
computes pure black. The pack ships one ink at 17.62:1, because two near-blacks in
one voice is an accident, and because a pure-black ink token is banned by this
repository's slop lint as an unfinished default.

**3. The 8px badge ink is refused.** `--gray-6` (`#a0a09d`) at 8px measures
**2.51:1** — under even the 3:1 non-text floor, at the smallest size on the page.
`--ink-faint` here is `--gray-7` (3.23:1) and is restricted to placeholder and
disabled; a badge meant to be read takes `--ink-muted` at 5.06:1.

**4. The alarm state's danger comes from the pink ramp, and that is arithmetic
rather than taste.** On the dark field the accent is the reference's measured
`--orange-dark` (`#fa7545`, 6.44:1). A red danger beside it fails the palette
gate's hard floor of 10 in OKLab: `--red-6` separates by **5.2**, and `--red-5`
separates from the accent by 14.3 but then collides with the warning at **9.1**.
A brute-force search over the reference's own ramps returned 2,057 "legal"
combinations whose top scorers were degenerate — `--red-1` (`#fef4f4`) passes every
delta because it has stopped being red. The chosen set is
accent/`--green-5`/`--pink-5`/`--yellow-4`/`--blue-5`, worst separation **12.7** at
full colour, minimum contrast 5.06:1 on the darkest panel. Marked `SELECTED` at
every declaration, per the template's rule 3.

Under dichromacy the set is still tight (worst 3.6), which is why the pack states
that status is **never by colour alone** — and the reference supports that
independently: every status cell on it carries its word.

## The fork map — five packs, each edited in this change

Instruction 10's pairwise question was asked against the existing thirteen, since
this run adds one artifact. Five neighbours were close enough to need a written
distinction, and the reciprocity gate enforces that each names this pack back.

| Neighbour | What a reader who confuses them loses | The test |
|---|---|---|
| [`field-notes`](../../../plugins/sheleg-design/skills/sheleg-design/styles/field-notes.md) | the nearest twin: off-white paper, hairlines, one warm accent, mono small type | what the small type does — a **source** (how do you know) against a **reading** (what did you get) |
| `instrument-console` | both centre an instrument | a **changing** value on a dark field against a **settled** verdict on paper |
| `showroom` | both show the product rather than describing it | a whole **application surface** at real size against a **payload** |
| `blueprint` | both light, technical, gridded | zero radius, a drawing of what will exist, against concentric radii and a reading of what just happened |
| `scoreboard` | both warm paper, near-black ink, one orange that mostly marks | an accumulating **tally** against a single live **record** about this reader |

`workbench` is named without a link: the dashboard-versus-marketing-page
distinction is already owned by `showroom`'s fork, and duplicating it would be two
statements of one idea.

## A gate gap found on the way, and closed

`validate_counted_claims()` read every markdown file, `bin/cli.js` and the `.mdc`
rule — and **none of the three manifests**. So `.claude-plugin/marketplace.json`
said *"twelve pluggable style packs"* above a list of thirteen for two releases,
and `package.json` said *"thirteen"* on the day the fourteenth landed. The names in
those files were checked; the number beside them was not.

The source list now includes both plugin manifests and `package.json`. The check
was watched saying no twice: once against the real file (a planted `eleven` in
`marketplace.json` produced its own message, and the corrected file is silent), and
once as a permanent self-test plant that derives the wrong number from whatever the
manifest currently claims, so it cannot go stale the way its predecessor did.

A related unguarded count was found and fixed by hand: `SURFACE_COMPOSITION.md`
said the accent role resolves to `--accent` in **ten** packs. That was true at
twelve packs and silently wrong at thirteen; it is twelve at fourteen. It reaches
no check, because `in ten,` is not followed by a counted noun — the same class as
B-013, and it stays a known hole rather than a claimed fix.

## Verification

Gates on this branch: **validate.py 1640, validate_palette.py 711, sloplint.py
366**, against floors of 1507 / 603 / 352 measured on the previous release. Every
ratio stated in the pack and the token layer is recomputed from the tokens by the
palette gate — including one this run got wrong: `--ink-faint` on the alarm field
was written as 2.15:1 from intuition and computes **3.32:1**. The gate named both
numbers it accepts and neither was mine.

The kit compiles: `npm install && npm run build` in `kits/datasheet` exits 0 and
emits 11 components with declarations into `dist/`, verified by listing the
directory rather than by the exit code.
