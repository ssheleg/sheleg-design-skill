# sheleg-design-skill — canon sync (0.3.0)

Date: 2026-07-19. Status: implemented, partly superseded — kept as the record
of why the repo is laid out this way.

**Superseded since:** the "no templates" decision below (0.5.0 → 0.9.0). The
skill now ships one template, `styles/STYLE_PACK_TEMPLATE.md` — an authoring
skeleton for style packs, not a project scaffold. It seeds nothing into a
consuming project; the original intent (this skill is not a generator) holds.

## Goal

Bring the repo to the ssheleg skill-pipeline canon (reference:
`ssheleg/super-ux`) without changing the skill's content contract.

## Decisions

- Marketplace layout: `.claude-plugin/marketplace.json` with one plugin
  `sheleg-design` sourced from `plugins/sheleg-design/`.
- Skill bundle moves to `plugins/sheleg-design/skills/sheleg-design/`
  (dir name == front-matter `name`). The npx installer copies from there;
  installed layout (`.cursor/.claude` `skills/sheleg-design/`) unchanged.
- One thin command `/sheleg-design` wrapping the skill.
- Cursor rule `cursor/rules/sheleg-design.mdc` is self-contained (no
  relative links — .mdc files get copied into foreign projects).
- Validator `test/validate.py` (stdlib only, `from __future__ import
  annotations` for py3.9) + CI running validator, `node --check`, and a CLI
  smoke test.
- Version sync across marketplace.json / plugin.json / package.json /
  CHANGELOG top entry, enforced by the validator.
- Distribution: npm (`npx sheleg-design-skill`), Claude plugin, vercel-labs
  `skills` CLI (free via marketplace manifest), `install.sh` POSIX fallback.

## Out of scope

- Project templates — the skill seeds no application code. (The pack-authoring
  skeleton added later is documentation, not a scaffold; see the note above.)
- Multiple skills/commands — one job, one skill.
