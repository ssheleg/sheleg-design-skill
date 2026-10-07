# Skill Card — sheleg-design

## Identity

| Field | Value |
|---|---|
| Pack and skill | `sheleg-design` |
| Version | `1.62.0` |
| License | MIT |
| Source | https://github.com/ssheleg/sheleg-design-skill |

## Job and boundary

Decide visual language and motion: style packs, tokens, typography, themes,
cinematic scroll and the Figma boundary. It does not decide product structure,
write copy, implement backend behavior or replace an accessibility audit.

## Inputs and outputs

Inputs are a brief, existing visual system and target surfaces. Outputs are a
recorded pack choice, calibration dials, token mapping, visual implementation
and verification captures. Component kits are materialized only when requested.

## Runtime and trust

The pack is Markdown, CSS token layers and a zero-dependency Node installer.
Optional work may operate on a user-authorized Figma file or connected reference
service. Drawing inside a shared Figma frame is treated as publishing.

## Distribution

Install from npm/GitHub, through the Agent Skills CLI, or as the
`sheleg-design` Claude Code plugin. `npx sheleg-design-skill --kit <pack>`
materializes a component token kit. `npx sheleg-design-skill --lint <dir>`
checks a project against the visual floor in `SLOP_MARKERS.md` (exit 1 on an
S1 marker; `--json`, `--ratchet <budget.json>`, `--include-tests`).

## Verification

- Repository validator: `python3 test/validate.py`
- Project linter: `node test/lint_test.js` and `npx sheleg-design-skill --self-test`
- Token/style checks: repository test suite
- House audit: pinned `make-skill` auditor in `validate.yml`
- Behavioral data: `test/evals/`
- Evaluation status: authored and schema-validated; no model result claimed

## Known limits

A pack fixes values and rules, not product behavior. Core packs intentionally
leave some component and responsive decisions open; the generated kit supplies
component states, but the user still owns product-specific decisions.

