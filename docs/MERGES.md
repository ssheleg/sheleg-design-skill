<!-- agent-sync:merge-log -->

# Merge log

Written by `agent_sync.py merge`. Entries newer than 7 days keep their detail; older ones are compacted to one line each on the next write. Read it before starting work: it is the shortest answer to *what landed while I was on my branch*.

### 2026-08-30T16:33:31Z · `SHD-W3-yaml-frontmatter` · fix/yaml-front-matter-v1.58.1 → main · landed via PR #17 (squash)
- run: r-a3532a2fe
- files: 12 (12 files changed, 149 insertions(+), 11 deletions(-))
- conflicts: none
- summary: v1.58.1: the front-matter description made valid YAML again — `Triggers: "…"` from the 1.57.0 rewrite became `Triggers - "…"` (the siblings' shape, all 35 routed triggers surviving per `advertised_check.js`), mirror byte-identical; `validate_front_matter_is_yaml()` parses every shipped front-matter block with `yaml.safe_load` in THIS repo's gate (the 1.37.4 fix's strict gate lived in the umbrella, which CI never has above it), fails closed without PyYAML, permanent self-test plant; three workflows install PyYAML; floor 5598 → 5621

### 2026-08-30T15:03:22Z · `SHD-W2` · feat/shd-wave2-v1.57.0 → main · landed via PR #14 (squash)
- run: r-a3532a2fe
- files: 111 (111 files changed, 2050 insertions(+), 43 deletions(-))
- conflicts: none (rebased over v1.55.0 and v1.56.0 mid-run; both concurrent releases from the same directory's other run)
- summary: v1.57.0: sibling skills declared optional with in-text fallbacks (SHD-05); `## Contents` derived from each file's headings via gen_contents.py + gate (SHD-01); manifest descriptions derived from STYLE_PACK_INDEX.md via gen_manifest_descriptions.py + gate (SHD-03); deck trigger narrowed to the web register (SHD-09); layout deviation recorded (SHD-11)

### 2026-08-29T21:11:44Z · `SHD-07-installer-shadow-refusal` · fix/installer-shadow-refusal-v1.54.1 → main · landed via PR (squash)
- run: r-a3532a2fe
- files: 12 (12 files changed, 566 insertions(+), 10 deletions(-))
- conflicts: none
- summary: v1.54.1: both installers refuse the plugin-channel shadow (exit 3, remedy from installed_plugins.json, --force override); 13-case installer suite in npm test and CI; CONTRIBUTING requires annotated release tags

## Compacted

_nothing older than the window yet_
