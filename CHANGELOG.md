# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow [SemVer](https://semver.org/spec/v2.0.0.html).

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
