# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow [SemVer](https://semver.org/spec/v2.0.0.html).

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
