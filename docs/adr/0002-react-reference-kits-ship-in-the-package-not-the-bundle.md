# React reference kits ship in the package, not in the skill bundle

- **Status:** Accepted
- **Consequences / affects:** `README.md`, `package.json` (`files[]`), `bin/cli.js`,
  `install.sh`, `test/validate.py`, `plugins/sheleg-design/skills/sheleg-design/DESIGN_SYNC_BRIDGE.md`
- **Source:** run `2026-08-04-design-sync-bridge` · brief
  `docs/superpowers/specs/2026-08-04-design-sync-bridge-brief.md`
- **Partially supersedes:** `docs/superpowers/specs/2026-07-19-canon-sync-design.md`
  → *Out of scope* → "Project templates — the skill seeds no application code"

Claude Code's bundled `/design-sync` skill pushes a **React** design system to
claude.ai/design, so a SHELEG style pack — markdown plus a CSS token layer — cannot
be pushed at all without React components existing somewhere on disk. The
2026-07-19 canon spec recorded that this skill seeds no application code and "is not
a generator", and the README promises the installed skill is "documentation an agent
reads"; a style pack's worth of components inside the bundle, once per pack, would
break both, and would put React into every Cursor install that never asked for it.
*(Written when there were six packs; there are twelve as of 1.9.0, which only makes
the argument larger — the count is deliberately not restated here, because a number
in a decision record goes stale while the decision does not.)*

So the kits live in `kits/<pack>/` — committed to the repo, shipped in the npm
package (`files[]`), and **never copied into a consuming project by any installer**.
An agent materializes one deliberately with `npx sheleg-design-skill --kit <pack>
--out <dir>` and then runs `/design-sync` on it. The original intent survives intact:
nothing is seeded into a project without an explicit command. The bridge doc
therefore points at **that command**, never at a relative path — which is the fix for
the failure class the project already paid for once, when `STYLE_PACK_TEMPLATE.md`
had to move into the bundle because `SKILL.md` pointed at a path only the repo had.
