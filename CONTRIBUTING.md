# Contributing

This repo ships prose an agent reads, not a library — so the review question is
always *"would an agent, with only these files, do the right thing?"* Two rules
follow from that: **no invented values**, and **every promise a file makes must
have a check that fails when it stops being true**.

## Setup

No dependencies. You need Node ≥ 16 (installer) and Python 3 (validator).

```bash
npm test        # all four gates — run this one
```

Run it before and after every change. It is four gates, not one:

| Gate | What it decides |
|---|---|
| `python3 test/validate.py` | the consistency contract — manifests, version sync, the pack contract, routing, mirrors, links |
| `python3 test/validate_palette.py` | colour: contrast floors and separation between semantics, per theme, including colour-vision deficiency |
| `python3 test/sloplint.py` | bundle compliance and doctrine completeness |
| `node --check bin/cli.js` | the installer parses |

`npm run selftest` runs the planted-defect self-tests for the palette gate and
the slop lint — the proof each check has been watched saying no. CI runs all of
it on every push and PR; a green from `validate.py` alone covers one gate of
four.

## Repo layout

| Path | What it is |
|---|---|
| `plugins/sheleg-design/skills/sheleg-design/` | **The canonical bundle** — SKILL.md, the reference, the packs, the token CSS, the pack template |
| `.cursor/skills/sheleg-design/` | Byte-identical mirror for the Cursor channel; never edit it by hand |
| `plugins/sheleg-design/commands/` | The `/sheleg-design` slash command |
| `cursor/rules/sheleg-design.mdc` | Self-contained condensed rule — **no relative links** (it gets copied into foreign projects alone) |
| `bin/cli.js`, `install.sh` | The two installers; both must ship the whole bundle |
| `test/validate.py` | Structural gate |
| `test/scenarios.md` | Behavioral harness (T1–T19) |
| `templates/style-pack-template.md` | Source of the shipped pack skeleton |

Edit the canonical bundle, then copy the changed file into the `.cursor/`
mirror. The validator compares the whole tree in both directions and fails on
drift.

## Adding a style pack

1. Copy `templates/style-pack-template.md` to
   `plugins/sheleg-design/skills/sheleg-design/styles/<name>.md`.
2. Fill **every** heading. The contract is **thirteen**, plus `## Motion flavor`
   for a cinematic pack: Register / Palette / Type / Texture & surface /
   **Components** / **Hero** / **Responsive** / Motion tokens / Signature
   motifs / **Signature element** / *Motion flavor (cinematic packs only)* /
   Micro-interactions / Bans / Gotchas. The four in bold were added in 1.5.0 and
   are the ones that decide whether an implementation drifts; the validator
   enforces the other nine always and the four all-or-nothing, so a pack cannot
   be half-widened. **Do not ship a pack on the nine**: the gate will pass it and
   the agent that reads it will invent the rest. This rule and the three
   beside it now live in `styles/STYLE_PACK_TEMPLATE.md`, which ships — an
   author holding only the installed bundle never sees this file. Edit them
   there; this paragraph is the pointer, not the home.
3. Author `styles/tokens/<name>.css` in the **same change**. Values come from a
   real production system or a reference you can name in the pack's `Origin:`
   line — a pack whose tokens were invented defeats the point of the repo.
4. Route it: add a row to the `SKILL.md` pack table and name the pack in
   `bin/cli.js`. The validator requires both — a pack nobody routes to does not
   exist.
5. Mirror the new files into `.cursor/skills/sheleg-design/`, add them to the
   `install.sh` file list, and re-run the validator.
6. Add its React reference kit under `kits/<pack>/` — the six-name spine copied
   from an existing kit (identical names, props and types) plus this pack's
   signature components, `src/styles.css` opening with `styles/tokens/<pack>.css`
   copied **byte for byte**, and `.design-sync/{config.json,conventions.md}`. The
   validator refuses a pack without one. See
   `docs/evidence/specs/2026-08-04-design-sync-bridge-design.md`.
7. Add or update a scenario in `test/scenarios.md` if the pack changes routing
   behavior.
8. **Render the kit in a browser and compare the computed values against what the
   pack claims.** Not a screenshot for the eye — mount the kit on a page with real
   content at 1440, 768 and an emulated 390, then read `getComputedStyle` back and
   check it against the pack's own numbers: control heights, body weight, radii,
   gutters, the tap-target floor, no horizontal overflow.

   This step exists because the three gates cannot do it. **A gate reads
   structure, not layout**, and two releases in a row shipped defects that every
   gate passed: `bulletin` (1.43.0) collapsed a platform rail to a column because
   `container-type` was set on a shrink-to-fit box, and `nameplate` (1.48.0)
   rendered its signature plate 78px against a stated 50 — the kit declared no
   `box-sizing`, and Chrome gives a `button` `border-box` while giving an anchor
   `content-box`, so the button beside it kept its promise and the plate silently
   grew by its own padding. The same render caught body copy at weight 400 against
   the pack's central claim of 500, because `--weight-body` existed and no
   component consumed it — a token that was decorative rather than binding.

   Until 1.48.1 this was not a step. It lived as a sentence in the `bulletin`
   CHANGELOG entry, so whether it happened depended on the next author reading
   that paragraph — which is not a procedure, it is luck.

**Auditing the collection.** `python3 tools/audit_packs.py` reports what the gates
cannot see — how each pack was measured, whether its source is still reachable, whether
its kit was ever rendered. `--check-live` adds the network probe. It is a report and
always exits 0: several gaps are recorded exceptions in the packs themselves, and two
rules postdate most of the library. The standing result lives in `docs/audit/`.

**Every var() a kit consumes must be declared.** `python3 tools/check_kit_vars.py` gates
it, and CI runs it. An undefined custom property drops to the initial value instead of
erroring, so four of the 35 kits shipped a status dot that painted nothing while every other
gate stayed green.

**Publishing the catalogue.** `python3 tools/site.py --out _site` builds the public site
— index, gallery, audit — and **refuses to emit a page that names any source address**,
computing the forbidden set from the packs rather than from a list somebody maintains.
The `pages` workflow builds it on every push to `main`; nothing generated is committed,
because a generated page in git drifts from the tokens it claims to show.

**Looking at the library.** `python3 tools/gallery.py` renders every pack as one
browsable page from the packs' **own token layers** — swatches, radius, accent and type
stack read out of `styles/tokens/<pack>.css` rather than described, so a card that looks
wrong is a pack that is wrong. It writes `gallery.html` (gitignored) and needs no network.
Two `var()`-inside-`calc()`-and-font-stack cases were invisible until it existed.

Token naming is an interface across packs: `--accent-weak` is a tint,
`--accent-dim`/`-deep` is a darker accent. Reusing a name for the opposite
meaning silently inverts anyone who switches packs.

## Changing the skill or the reference

- `SKILL.md`'s front-matter `description` is discovery. It states **trigger
  conditions**, opens with "Use when", carries Russian aliases beside the
  English triggers, and stays under 1024 characters. All three are validated.
- Any behavioral claim in `SKILL.md` or `SHELEG_DESIGN.md` must match the
  packs and the CSS. Contradictions between files are the defect class this
  repo cares about most — see the 0.9.0 entry in the CHANGELOG for a full pass
  of them.
- After editing the skill, a pack or the reference, re-run the affected
  scenarios from `test/scenarios.md` with fresh subagents.

## Releasing

Semver. Bump `.claude-plugin/marketplace.json`, `plugins/sheleg-design/.claude-plugin/plugin.json`,
`package.json`, the `CHANGELOG.md` top entry **and** `SKILL.md`'s
`metadata.version` **together** — five homes since 1.11.0, and the validator
fails on a mismatch. The fifth is the only one that ships inside the bundle,
which is why it exists: an installed reader has nothing else to read a
version from. Tag `vX.Y.Z`; the release workflow (armed by the
`RELEASE_ENABLED` repo variable) validates, cuts a GitHub release from the
matching CHANGELOG section and smoke-tests the tag through `npx`. **It also
publishes to npm**, with provenance, gated on the `PUBLISH_NPMJS` repo variable.

`npm publish` used to be the one human step here, because 2FA blocks a token
that is not automation-scoped; the workflow's `publish` job replaced it and this
paragraph did not move with it. Corrected on 2026-08-17, after the stale
sentence sent a release's operator looking for a manual step that no longer
exists. **The tag is the whole release**: push `vX.Y.Z` and GitHub cuts the
release and publishes the package.


### The family catalogue moves with the release

`sshlg-skills` — the launcher that installs and updates the whole ssheleg family — pins every
member's version in its own `skills.json`. **A release that does not bump that pin is invisible.**
`npx sshlg-skills list` keeps reporting the previous version, `update` keeps installing it, and
anyone comparing their install against `list` is told the wrong number with nothing to reveal it.

So a release is not finished when this package hits npm:

```bash
# in ssheleg/sshlg-skills
#   1. bump this member's "version" in skills.json
#   2. move the submodule pointer: git -C skills/sheleg-design checkout vX.Y.Z
#   3. carry the same number into the README row — the validator compares all three
#   4. bump the launcher's own version and changelog, then tag
git push origin main --follow-tags        # the tag publishes the launcher too
npx --yes sshlg-skills@latest list        # the new number must appear here
```

**Steps 2 and 3 are the ones that get forgotten**, and the launcher's validator
fails on both: a pin that names a version the submodule is not checked out at,
and a README row that disagrees with `skills.json`.

## Coordinating with other agents

`docs/AGENT_SYNC.md` describes how coordination is wired in this repository and
what it does **not** guarantee. It is generated from `.claude/agent-sync.json`:
read it before editing a file that config guards, and regenerate it with
`agent_sync.py setup` in the same change that alters the config.

## Reporting

Issues and PRs: <https://github.com/ssheleg/sheleg-design-skill/issues>. For a
bug in what an agent *did*, include the prompt and which files it read — that's
the reproduction.
