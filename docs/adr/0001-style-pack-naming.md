# ADR-0001 — Style packs are named for the register, never the source brand

- **Status:** accepted
- **Date:** 2026-08-04
- **Context of record:** the SHELEG Design skill's `styles/` directory
- **Landed on `main`:** 2026-08-08, by the `cyclorama` run. It was written on
  `feat/lecture-hall-pack`, which held at its stage-0 gate and never merged, so
  the decision register began at `0002` for four days while the rule it records
  was already binding. Restored here unchanged — the decision is not this run's
  to rewrite, only to obey.
- **Applied a second time:** 2026-08-08. The eighth pack was extracted from
  `codos.ai` and is named **`cyclorama`** for the register it encodes (a
  seamless backdrop that changes colour behind a fixed subject), not `codos`.
- **Applied four more times:** 2026-08-09, for the 1.9.0 batch —
  `attio.com` → **`showroom`**, `pinecone.io` → **`blueprint`**,
  `milvus.io` → **`prism`**, `zilliz.com` → **`maquette`**. Twelve packs, twelve
  registers, no source brand used as a name.
- **Corrected:** 2026-08-10. The Decision section named the seventh pack
  `lecture-hall`. That was the name on the branch this ADR was written on, and
  that branch never merged; the pack that shipped from graphify.com is
  **`field-notes`**. The rule is unchanged and was obeyed — only the example was
  stale. See the note at the Decision.

## Context

Every style pack in this skill is extracted from a real production site — the
`STYLE_PACK_TEMPLATE.md` requires it ("Origin: … never invented ad hoc"). That
makes the source brand the most *available* name for a new pack, and the
seventh pack arrived with exactly that request: extract graphify.com, call it
`graphify`.

Three prior packs had already resolved this the other way, without the rule
being written down anywhere:

| Source site | Pack name |
|---|---|
| deck.sparkl.ing | `briefing-room` |
| functionhealth.com | `atrium` |
| gutgutgoose.com | `orchard` |

The convention existed only as a pattern in the file listing. A pattern nobody
has written down is one that the next request overrides by accident — which is
precisely what happened.

## Decision

**A style pack is named for the design register it encodes, never for the site
it was extracted from.** The source is recorded in the pack's `Origin:` line,
which is where attribution belongs.

The seventh pack is therefore named for its register, not `graphify`.

> **Record corrected 2026-08-10.** This line originally read "*The seventh pack
> is therefore `lecture-hall`, not `graphify`*". `lecture-hall` was the register
> name chosen on `feat/lecture-hall-pack`, the branch this ADR was written on and
> which never merged. The pack that actually shipped from graphify.com is
> **`field-notes`** (`CHANGELOG.md`, 1.5.0). No `lecture-hall` pack, token layer
> or kit has ever existed. The decision itself is untouched: the shipped name is
> a register, not the source brand, which is what this ADR requires. A decision
> register that names an artifact nobody can find teaches the reader to distrust
> the register, so the fact is corrected here rather than left to be rediscovered.

## Consequences

**Why this is hard to reverse.** A pack name is a public API across four
distribution channels: the npm package, the Claude Code plugin marketplace, the
`.cursor` skills mirror, and the `install.sh`/POSIX bundle. It is also the
filename an agent is told to read (`styles/<name>.md`), the token-layer filename
(`styles/tokens/<name>.css`), a string the validator asserts on in `bin/cli.js`,
and a wiki link. After a release, renaming means a breaking change for every
installed copy — which is what makes this an ADR rather than a preference.

**What the rule buys.**

- *Longevity.* A register outlives a company. `briefing-room` still describes
  what it is if deck.sparkl.ing rebrands or disappears; `sparkling` would not.
- *Selection by intent.* `SKILL.md`'s pack table is read by an agent choosing a
  look for a product it is building. "Choose `atrium` for consumer health" is
  actionable; "choose `functionhealth`" requires already knowing the site.
- *No trademark surface.* The packs document a visual register and cite their
  origin. Naming the artifact after someone else's brand invites a reading —
  endorsement, affiliation — that the docs do not intend and cannot support.
- *Namespace hygiene.* `graphify` specifically collides with the user's
  `/graphify` skill and the `graphify-out/` directories in sibling projects,
  making future greps and wiki links ambiguous.

**What it costs.** The link back to the source is one indirection weaker: a
reader who knows the site must open the pack to discover the connection. The
`Origin:` line is the mitigation, and it is mandatory.

**Applies to.** Every future pack. A request naming a pack after its source
brand is a request to override this ADR, and should be answered by pointing at
it rather than by complying silently.

## Alternatives considered

- **`graphify`** — as literally requested. Rejected: breaks the established
  convention, collides with an installed skill's namespace, and couples a
  long-lived artifact to a third party's branding.
- **`chalkboard`** — object-name family, like `workbench`. Genuinely close, and
  more literal about the dominant visual. Rejected because it names only the
  dark half of a system whose defining move is the gradient *resolving into warm
  paper*, and whose product UI is light by default.
