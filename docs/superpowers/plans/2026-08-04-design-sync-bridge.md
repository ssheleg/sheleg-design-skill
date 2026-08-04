# Plan — design-sync bridge + six reference kits

Stage-4 plan for [`…-design.md`](../specs/2026-08-04-design-sync-bridge-design.md)
(the spec) and [`…-brief.md`](../specs/2026-08-04-design-sync-bridge-brief.md) (the
brief and its REQ spine). **The spec is normative**; this file says who builds what,
in what order, and how each task proves it is done.

**Workspace:** `/Users/sshlg/DATA/sheleg-design-skill-wt/design-sync-bridge`, branch
`feat/design-sync-bridge`. The primary checkout at
`/Users/sshlg/DATA/sheleg-design-skill` belongs to another live session and is **never
written** by this run.

**The suite, for every task:** `python3 test/validate.py` from the worktree root.
Green = exit 0 and `OK (n checks)` with n ≥ 274. **A task is not done until the whole
suite is green** — not just its own new check.

## Isolation: one worktree, disjoint directories

The six kit tasks own **disjoint directory trees** and share no file, so they run as
parallel subagents inside this one worktree rather than in six git worktrees of their
own. Six worktrees would buy nothing here and cost a six-way merge. Every other task
is sequential and edits shared files.

Ownership is the contract that makes that safe:

| Task | Owns, exclusively |
|---|---|
| T1 | `plugins/…/DESIGN_SYNC_BRIDGE.md`, `plugins/…/SKILL.md`, both `.cursor/` twins, `install.sh`, `test/validate.py` |
| T2 | `kits/workbench/**` |
| T3–T7 | `kits/<pack>/**`, one pack each |
| T8 | `test/validate.py`, `bin/cli.js`, `package.json`, `.github/workflows/validate.yml` |
| T9 | `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `cursor/rules/sheleg-design.mdc`, `test/scenarios.md` |

T1 and T8 both edit `test/validate.py` and are therefore **sequential, never
concurrent** — T1 lands first and is committed before T8 starts.

## Dependency graph

```
T1  (seq)  bridge doc + SKILL.md + install.sh + mirror + checks 1–2
 └── T2  (seq)  kits/workbench — the exemplar, built end to end
      ├── T3  (par)  kits/instrument-console
      ├── T4  (par)  kits/editorial-luxury
      ├── T5  (par)  kits/briefing-room
      ├── T6  (par)  kits/atrium
      └── T7  (par)  kits/orchard
           └── T8  (seq)  validator checks 3–11 + --kit + files[] + CI
                └── T9  (seq)  docs propagation + T12 scenario
```

Parallel group: **T3–T7** only. Everything else is a barrier.

**Why the checks come after the kits (T8, not T1).** Check 3 asserts one kit per
style pack. Written before the kits exist it fails on all six, which turns the suite
red for every task in between and destroys the one signal each task depends on. The
checks are still TDD — T8 plants a defect for each one and watches it fail — the red
just happens inside T8 rather than six tasks earlier.

---

## T1 — the bridge doc and its wiring (sequential)

**Scene.** The skill bundle has three companion docs; this adds a fourth. The repo's
validator asserts that a companion doc both ships in the bundle *and* is linked from
`SKILL.md`, that `install.sh` lists exactly the bundle files, and that the `.cursor/`
mirror matches the plugin copy byte-for-byte in both directions. All four obligations
are this one task's, because they fail as one.

**Steps.**

1. Write `plugins/sheleg-design/skills/sheleg-design/DESIGN_SYNC_BRIDGE.md` with the
   seven headings of spec §2, verbatim, and the content contract stated per section
   there. Match `FIGMA_BRIDGE.md`'s voice: a one-line rule up top, tables where the
   mapping is a mapping, and a "what cannot cross" section that says why the limit is
   a contract rather than a gap.
   - **No relative link into `kits/`.** The doc names the command
     `npx sheleg-design-skill --kit <pack> --out <dir>` (spec §1).
2. Add the `## Optional — Claude Design (design-sync)` section to
   `plugins/sheleg-design/skills/sheleg-design/SKILL.md` at the position and with the
   text of spec §3. **Do not touch the front-matter.**
3. Add `DESIGN_SYNC_BRIDGE.md` to `install.sh`'s `for f in …` list.
4. Copy both edited files to `.cursor/skills/sheleg-design/` — byte-identical.
5. In `test/validate.py`, add `DESIGN_SYNC_BRIDGE.md` to the companion tuple at the
   `for companion in (…)` loop, and add spec §11 check 2 (the seven headings) beside
   the existing pack-section check, using its message text verbatim.

**TDD.** After step 5 but before step 1 is finished, the suite must be **red** with
`…/DESIGN_SYNC_BRIDGE.md: missing`. Then green. Prove both by running the suite twice
and pasting both outputs into the commit body.

**DoD.** `python3 test/validate.py` green; `git diff --stat` touches only the six
files above; the bridge doc contains no `](./kits` or `](../` outside the bundle.

**Commit.** `feat(bridge): the pack as a design system, and the border it does not cross`

---

## T2 — `kits/workbench`, the exemplar (sequential)

**Scene.** This is the kit the other five are built against and the only one pushed
live this run, so it is built first and alone. Everything in spec §4–§9 applies; the
pack's own rules are in
`plugins/sheleg-design/skills/sheleg-design/styles/workbench.md` and its token values
in `styles/tokens/workbench.css`.

**Components** — spine (spec §5): `Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule`.
Signature (spec §6): `StatusDot`, `DataTable`, `ProgressBar`, `SegmentedControl`,
`EmptyState`. Eleven in total.

**Steps.**

1. `kits/workbench/package.json` and `tsconfig.json` — verbatim from spec §4, with
   `<pack>` = `workbench`.
2. `src/styles.css` — spec §8. Part 1 is `styles/tokens/workbench.css` copied with
   `cp`, **never retyped**. Then the `/* ── components ── */` marker, then the
   component CSS, `var(--token)` only, no colour literals.
3. One `src/<Name>.tsx` per component. Props exactly as spec §5 for the spine; the
   signature components take what the pack describes and nothing more. Every component
   also accepts `className?: string`, appended last.
   - `workbench` is the pack with a real light/dark twin: the kit renders under
     `:root` and `[data-theme="dark"]` exactly as the token layer defines them, and
     adds no third theme.
4. One `src/<Name>.md` per component — frontmatter `category:` from the spec §7
   taxonomy, then a paragraph on what it is for *in this pack* and a usage example.
5. `src/index.ts` — a barrel re-exporting all eleven.
6. `.design-sync/config.json` — spec §9, `globalName: "ShelegWorkbench"`, **no
   `projectId`**.
7. `.design-sync/conventions.md` — the pack's register, its accent rule, its **Bans
   verbatim** from `styles/workbench.md`, and the closing line that motion is not part
   of this design system.
8. `.design-sync/previews/<Name>.tsx` for all eleven — 2–6 named exports each, real
   JSX importing from `'@sheleg-design/workbench'`, realistic content (never
   `foo`/`test`: these cards are read by humans and imitated by the design agent).
9. `README.md` — five lines: what this is, that it is generated from a SHELEG pack,
   and the two commands.

**TDD.** `cd kits/workbench && npm install && npm run build` exits 0 and leaves
non-empty `dist/index.js` **and** `dist/index.d.ts`. Then plant a type error in one
component, re-run, watch it fail, revert. Paste both results into the commit body —
a build that has never been seen failing is not a build that has been tested.

**DoD.** The build proof above; `python3 test/validate.py` green; no colour literal
below the marker (`grep -nE '#[0-9a-fA-F]{3,8}|rgba?\(|hsla?\(|oklch\(' src/styles.css`
returns nothing after the marker line); the token block byte-identical to
`styles/tokens/workbench.css` (`diff <(head -n $(wc -l < …tokens/workbench.css) src/styles.css) …tokens/workbench.css`).

**Commit.** `feat(kits): workbench — the exemplar kit, spine and signature`

---

## T3–T7 — the other five kits (parallel, one subagent each)

**Scene for each.** `kits/workbench` is built and committed; it is the reference for
structure, and **only** for structure. The pack's identity comes from its own
`styles/<pack>.md` and `styles/tokens/<pack>.css`, which are the source of truth and
disagree with `workbench` on purpose.

| Task | Pack | Signature components (spec §6) |
|---|---|---|
| T3 | `instrument-console` | `ActBadge`, `ProgressRail`, `HudFrame`, `Telemetry` |
| T4 | `editorial-luxury` | `DossierCard`, `Eyebrow`, `Stamp`, `DataTable` |
| T5 | `briefing-room` | `SlideFrame`, `ClaimTitle`, `SourcedNumber`, `HighlightPhrase`, `ComparisonTable` |
| T6 | `atrium` | `ItalicAside`, `MotionToggle`, `ComparisonTable`, `SourcedFigure`, `AuthorityRow` |
| T7 | `orchard` | `Slab`, `ChipRail`, `ClaimEvidence`, `GlassNav`, `ObjectionSection` |

**Steps.** T2 steps 1–7 and 9, with this pack's name, tokens and signature set.
**Skip step 8** — only `workbench` gets authored previews this run (brief, stage-2
scope call); these five ship the converter's floor card, which is honest rather than
broken.

**Five traps, each already paid for once by this project.**

1. **The spine is identical.** Same six names, same props, same types as
   `kits/workbench`. A pack that wants more expresses it as a signature component.
   Renaming a spine prop is the `--accent-dim` mistake in a new costume.
2. **`atrium` and `orchard` have no separate pill component.** The pill triad and the
   candy pill *are* that pack's `Button`. Building both produces two buttons and a
   design agent that picks the wrong one.
3. **Motion does not cross.** No particle field, no fluted-glass shader, no
   word-by-word headline, no scroll-linked anything. If a motif only exists in motion,
   it is not in the kit — that is spec §2 §6, not an omission to fix.
4. **`briefing-room` never animates and has no hover state on static cards.** Its
   own pack says a card that lifts under a cursor during a live presentation is noise.
5. **`atrium`'s `MotionToggle` still ships**, statically, with `aria-pressed` and the
   label that swaps to `Play motion` — the pack calls it a component of the pack, not
   an accessibility afterthought.

**Subagent hard rules.** Each task writes **only** inside its own `kits/<pack>/`.
Nothing else — not `test/validate.py`, not another kit, not the pack markdown it is
reading. A needed change anywhere else is reported back, not made.

**TDD and DoD.** Identical to T2, with the pack substituted.

**Commit (each).** `feat(kits): <pack> — spine and signature over its own token layer`

---

## T8 — the gate (sequential)

**Scene.** Six kits exist. Now the repo learns to refuse a broken one.

**Steps.**

1. `test/validate.py` — checks 3 through 11 of spec §11, each with its message text
   verbatim. Put them in one `validate_kits()` function called from `main()` beside
   the existing validators.
2. `bin/cli.js` — the `--kit` / `--out` contract of spec §10, including the
   `guidelines/<pack>.md` materialization, all four refusals with their exact text,
   and both flags in `--help`. Do **not** reuse `listBundleFiles`.
3. `package.json` — `files[]` gains `kits/`.
4. `.github/workflows/validate.yml` — the `kits` matrix job of spec §12, plus the
   REQ-007 step: materialize `workbench` with `--kit` into a temp dir, `diff -r`
   against `kits/workbench/` **ignoring `guidelines/`**, then assert
   `guidelines/workbench.md` is byte-identical to `styles/workbench.md`.

**TDD — the part that is not optional.** Every one of the nine new checks is **watched
failing against a planted defect**, one at a time:

| Check | Planted defect |
|---|---|
| 3 | `mv kits/atrium kits/atrium-x` |
| 4 | rename `Chip` → `Tag` in one kit |
| 5 | delete a `category:` line; then set it to `Widgets` |
| 6 | change one hex in a kit's token block |
| 7 | add `color: #fff` below the marker |
| 8 | add a `kits/…` path to `install.sh` |
| 9 | drop `kits/` from `files[]`; then add `"projectId": "x"` to a config |
| 10 | delete a `conventions.md` |
| 11 | `mkdir kits/orchard/guidelines && touch kits/orchard/guidelines/x.md` |

For each: plant, run, **record the exact FAIL line**, revert, run, confirm green. The
nine FAIL lines go in the commit body. A check nobody has seen fail is not evidence,
and this table is the whole reason stage 6 can say the word "verified".

**DoD.** Suite green with n ≥ 283; the nine FAIL lines recorded; `node --check
bin/cli.js` clean; `npx . --kit workbench --out /tmp/k1` produces a directory that
builds.

**Commit.** `test(kits): nine checks, each watched failing first`

---

## T9 — docs propagation (sequential)

**Scene.** `DOCMAP.md`'s propagation matrix names what a new bundle file and a new
release owe. This task pays all of it.

**Steps.**

1. `README.md` — the installed-file table gains `DESIGN_SYNC_BRIDGE.md`; a new
   *Claude Design* section beside the Figma one; **and the dependency-free promise
   gains its honest caveat**: the skill you install is still documentation, and the
   kits live in the package behind an explicit command.
2. `CHANGELOG.md` — a `1.6.0` entry at the top.
3. `CONTRIBUTING.md` — adding a style pack now also means adding a kit.
4. `cursor/rules/sheleg-design.mdc` — one line about the bridge. **No relative
   links** — `.mdc` files get copied into foreign projects and the validator enforces
   it.
5. `test/scenarios.md` — `T12`: a fresh agent with `/design-sync` available and only
   the installed bundle must find the bridge, name the materialization command, and
   state the four reference-type rules and what cannot cross. Written in the shape
   T1–T11 already use.
6. Version bump to `1.6.0` in `package.json`, `plugin.json` and `marketplace.json` so
   the four-way sync holds against the new CHANGELOG entry.

**DoD.** Suite green; `grep -c "1.6.0"` finds it in all four manifests; the README no
longer claims anything the repo does not do.

**Commit.** `docs: the Claude Design bridge across every channel; v1.6.0`

---

## REQ → task map

| REQ | Task |
|---|---|
| 001, 002, 003 | T1 |
| 004, 005, 006 | T2–T7 (built), T8 (enforced) |
| 007 | T8 |
| 008 | T8 |
| 009 | stage 6, after T2 |
| 010 | T9 |
| 011 | T9 |
| 012 | T9 (version), stage 7 (release) |
| 013 | closed at stage 0 |
| 014 | every task — worktree only |
| 015 | T2–T7 (built), T8 check 10 (enforced) |
| 016 | T8 (CI job) |

Every REQ has a task; every task has a REQ. No placeholders, no "similar to T2"
without the substitutions named, no undefined component or prop.
