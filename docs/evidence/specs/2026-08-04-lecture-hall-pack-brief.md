# Task brief — `lecture-hall` style pack (from graphify.com)

> Stage-0 intake artifact (task-pipeline 1.10.1). **Status: HELD at the stage-0
> gate** by operator decision — see *Concurrency* below. Stages 1→10 have not run.

- **Date:** 2026-08-04
- **Branch:** `feat/lecture-hall-pack` (created so `main` stays untouched while
  other sessions hold this repo)
- **Task (one line):** add a seventh style pack to the SHELEG Design skill,
  extracted from the live computed styles of <https://graphify.com/>, named for
  its register (`lecture-hall`) rather than its source brand.
- **UI verdict:** **no** — the deliverable is documentation plus a CSS token
  layer. No screen, no flow, no component. super-ux is **not** armed for this run.
- **Model:** Opus 5 (top tier available at preflight; recorded, not re-asked).

## Knowledge sources (the phase-1 harvest — written BEFORE the first question)

| Source | What it says about this task | Fresh? | Authority | Stale after this run? |
|---|---|---|---|---|
| `test/validate.py:40-50, 261-295` | **The binding contract.** 9 required `## ` headings; every pack needs `styles/tokens/<stem>.css`; `SKILL.md` must link `styles/<name>.md`; `bin/cli.js` must name the stem; `install.sh`'s `for f in …` list is checked **both ways**; `.cursor/` mirror byte-identical with **no extra files**; every relative markdown link must resolve | current (272 checks) | **contract** | yes — gains rows for the new pack |
| `styles/STYLE_PACK_TEMPLATE.md` | The skeleton. "Origin: … never invented ad hoc". ≤3 type families. `## Motion flavor` is optional (cinematic packs only) | current | contract | no |
| `templates/style-pack-template.md` | Must stay byte-identical to the bundled copy (validator compares them) | current | contract | no |
| The six existing packs | **Naming convention: the register, never the source brand** — deck.sparkl.ing→`briefing-room`, functionhealth.com→`atrium`, gutgutgoose.com→`orchard` | current | convention | no |
| `styles/orchard.md` | The quality bar: measured WCAG audits, explicit positioning against sibling packs, gotchas naming the reference's **real** failures | current | exemplar | no |
| `styles/tokens/workbench.css` | The dual-register pattern: `:root` light default + `:root[data-theme="dark"]` twin + `@media (prefers-reduced-motion)` zeroing durations; `color-scheme` set explicitly | current | pattern | no |
| `styles/tokens/orchard.css` | **Tokens are unprefixed** (`--bg`, `--ink`, `--primary`), grouped by comment banner, contrast ratios written inline as comments | current | pattern | no |
| `SKILL.md` | The pack table every pack must join; "Never apply the cinematic motion layer to: product UI, docs sites, static content sites" | current (v1.4.0) | contract | yes — gains a row |
| `docs/superpowers/specs/2026-07-19-canon-sync-design.md` | Repo layout, the version sync and the distribution channels | 2026-07-19 | decision | no (this run does not touch it) |
| `docs/superpowers/retro.md` | **Absent** — no standing instructions bind this run | — | — | seeded at stage 10 |
| `graphify-out/graph.json` | **Not built** in this repo. Offered once, declined: 32 markdown files, low reach value | — | — | no |
| Obsidian wiki | Installed → `sshlg-projects-vault`. Stage-9 target: `projects/sheleg-design-skill/` | current | context | yes — stage 9 |
| Global `~/.claude/CLAUDE.md` | Production-grade bar; pipeline routing; post-release refresh via `npx --yes sshlg-skills@latest update`; **never** bare `npx skills update <name>` (creates a shadowing plain-copy) | current | house rule | no |
| **`docs/superpowers/specs/2026-08-04-design-sync-bridge-brief.md`** | **A concurrent run's stage-0 brief**, found mid-grill. Inherited findings: the wiki records **npm 2FA as the one human step where versions strand**; CI runs both installers and `diff -r`s them; the pack contract is "ten headings" (9 enforced + `Motion flavor` optional — consistent, not a conflict) | 2026-08-04, live | peer run | — |
| **graphify.com (live DOM + computed styles)** | Full extraction — see the appendix. Read via browser, not recalled | fetched 2026-08-04 | **source of truth for the pack** | no |

Precedence for *what is*: code > host docs/ADRs > wiki > memory. The operator
outranks every document — **but only out loud**.

## Scope

**In.** One new style pack: `styles/lecture-hall.md` + `styles/tokens/lecture-hall.css`,
wired into every place the validator and the four distribution channels require,
plus a behavioural test scenario, a CHANGELOG entry and a synchronized version bump.

**Out.** The design-sync bridge and React reference kits (a separate concurrent
run — see *Concurrency*). No change to the motion methodology, `SHELEG_DESIGN.md`,
`AI_PRODUCT_PATTERNS.md` or `FIGMA_BRIDGE.md`.

## Requirements (the REQ spine)

| ID | Requirement | How it's verified | Status |
|---|---|---|---|
| REQ-001 | `styles/lecture-hall.md` carries all 9 required headings; `Origin:` names graphify.com and the extraction date; every hex traceable to the appendix | `python3 test/validate.py` (9 heading checks) + diff each hex against *Appendix A* | open |
| REQ-002 | `styles/tokens/lecture-hall.css` exists: unprefixed tokens, `:root` light + `:root[data-theme="dark"]` twin, reduced-motion block | validator token-layer check + `grep -c 'data-theme="dark"\|prefers-reduced-motion'` = 2 | open |
| REQ-003 | Pack routed where the validator enforces it: `SKILL.md` pack table, `bin/cli.js` installer output, `install.sh` file list (both directions) | `python3 test/validate.py` — the three named checks at `validate.py:288,292,314` | open |
| REQ-004 | Pack named on the human-facing surfaces: `README.md`, `cursor/rules/*.mdc`, `package.json` description | `grep -l lecture-hall README.md cursor/rules/*.mdc package.json` → 3 hits | open |
| REQ-005 | `.cursor/skills/sheleg-design/` mirror byte-identical, no extra files | validator mirror check (`validate.py:240,246`) | open |
| REQ-006 | Version **1.5.0** identical in `package.json`, `.claude-plugin/marketplace.json`, `plugins/sheleg-design/.claude-plugin/plugin.json` | validator manifest check + `grep -h '"version"' <all three> \| sort -u \| wc -l` = 1 | open |
| REQ-007 | CHANGELOG 1.5.0 entry describing the pack | `grep -A5 '## \[1.5.0\]' CHANGELOG.md` non-empty | open |
| REQ-008 | New behavioural scenario (T12) in `test/scenarios.md` for the pack | `grep 'T12' test/scenarios.md` | open |
| REQ-009 | Every local gate green | `python3 test/validate.py` · `node --check bin/cli.js` · `sh -n install.sh` · npx + posix installer bundle-diff · each exit 0 | open |
| REQ-010 | Upstream validators green | `claude plugin validate --strict` on **both** the plugin and the marketplace entry | open |
| REQ-011 | Released: main pushed, GitHub Actions green, `v1.5.0` tagged, npm publish workflow succeeded | `gh run list --limit 1` success + `npm view sheleg-design-skill version` = 1.5.0 | open |
| REQ-012 | Local installs refreshed; **no shadowing plain-copies** | `npx --yes sshlg-skills@latest update`, then the shadow-check loop prints nothing | open |
| REQ-013 | ADR recording the pack-naming convention | `docs/adr/0001-style-pack-naming.md` exists and is linked from the brief | **done** |
| REQ-014 | Wiki synced: `projects/sheleg-design-skill/` records the seventh pack | vault page names `lecture-hall` | open |

**Frozen.** Adding a row is free; removing or narrowing one needs the operator's
explicit agreement, recorded in the carry-over ledger.

## Decisions locked (the grill's output)

| # | Decision | Chosen | Rationale |
|---|---|---|---|
| D1 | Pack name | **`lecture-hall`** | The brief asked for `graphify`, which breaks the established register-not-brand convention and collides with the `/graphify` skill and `graphify-out/` dirs. `lecture-hall` joins the place-name family (atrium, orchard, briefing-room, workbench) and names the whole register — the green board, the chalk derivations, and the warm paper the gradient resolves into. **→ [ADR-0001](../../adr/0001-style-pack-naming.md)** |
| D2 | Token naming | **Unprefixed** (`--bg`, `--ink`, `--brand`, `--verify`, `--witness`) | Read off `orchard.css`/`workbench.css`; every existing pack is unprefixed. Supersedes the `--lh-*` sketch shown during the grill. |
| D3 | Release path | branch → `main` (ff-only) → push → **CI green** → `git tag v1.5.0` → npm publish workflow | Publish is authorized **in advance but only on that precondition**; red CI stops and asks. Tagging is irreversible and reaches every installed copy. |
| D4 | Concurrency | **HOLD at the stage-0 gate** | Three other live sessions share this repo, one a duplicate graphify analysis. Operator will decide ownership and restart against a clean tree. |
| D5 | Register positioning | *deferred to the stage-2 gate* | Proposal: the first pack covering a developer product **end-to-end** — cinematic marketing hero *and* standalone product UI — with provenance encoded as colour. Overlaps `instrument-console` (technical, cold) and `workbench` (product UI); the brainstorm gate is where that overlap gets accepted or the pack gets killed. |

## Autonomy (the sweep)

| Stage | Settled |
|---|---|
| run-wide | Opus 5. Decide alone while reversible and inside the repo; escalate anything outward. |
| 0 Harvest | Wiki yes; code graph declined (low value here); doc sources = this repo + wiki. |
| 1 Docs | No external library APIs. Ground: font licensing (Bricolage Grotesque, Geist — both OFL), and the `claude plugin validate --strict` contract. |
| 2 Decompose | Single module, not a platform. |
| 2–3 Spec | UI verdict **no** → super-ux not armed, no scenario tracing. |
| 3 Design surface | n/a — no Figma in this task. |
| 4–5 Dev | Branch `feat/lecture-hall-pack`; conventional commits (repo history: `feat:`, `fix:`, `ci(release):`); tracker = the pipeline TaskList. |
| 5 Integration | ff-only merge into `main`. |
| 6 Tests | `python3 test/validate.py && node --check bin/cli.js`, `sh -n install.sh`, both installer smoke tests. "Green" = validator OK + CI success. No known-red baseline. |
| 7 Lint+deploy | `claude plugin validate --strict` ×2. Deploy authorization **granted** under D3's precondition. |
| 8 Post-deploy | `gh run list`; `npm view sheleg-design-skill version`; then `npx --yes sshlg-skills@latest update`. |
| 9 Docs+wiki | Wiki yes. Graph refresh n/a. |
| 10 Acceptance | Operator signs off. `docs/superpowers/retro.md` absent → seeded this run. |

## Done-criteria

Every REQ row closed with evidence from a check **seen failing at least once**
against a planted defect; carry-over ledger empty or explicitly deferred;
retrospective written.

## Open assumptions / risks

- **R1 — Concurrency (active).** Three other live sessions in this repo; one
  duplicates this task. Nothing may touch shared files until ownership is settled.
- **R2 — npm 2FA.** The wiki records 2FA as the one human step where releases
  strand (0.6.0 sat behind). The workflow is now token-armed via `PUBLISH_NPMJS`
  — **verify the secret is armed before tagging**, not after.
- **R3 — Pack sprawl.** Seven packs with two adjacent technical registers. D5.
- **R4 — Font licensing.** Both faces are OFL, but the pack must name substitutes
  the way `orchard.md` does rather than assume availability.
- **A1 — Assumption.** The green hero field is marketing-only; the product UI
  register is the light/dark pair. Taken from the DOM (`.hero-scope` is one
  section; `body` is `#f8f7f0`). Revisit if the extraction is extended past the
  landing page.

---

## Appendix A — the extraction (real computed values, read from the live DOM)

Read from <https://graphify.com/> on 2026-08-04 via browser computed styles.
**This appendix is the expensive artifact of this run** — it is what a restart
must not have to redo.

### Field & gradient

The hero is a single `.hero-scope` section carrying an 8-stop vertical gradient
that **resolves exactly into the body background** — the page dissolves from
blackboard to paper:

```
linear-gradient(
  #062a22   0%,   #0a3f31  35%,  #124f3c  60%,  #1e6149  74%,
  #4f8a68  85%,   #a8c9ad  93%,  #e9ecdf  98%,  #f8f7f0 100%)
```

### Semantic tokens (light `:root` — the product default)

| Token | Value | Token | Value |
|---|---|---|---|
| `--background` | `#f8f7f0` | `--foreground` | `#16211b` |
| `--card` | `#fdfcf6` | `--border` | `#e0e2d3` |
| `--muted` | `#edeee2` | `--muted-foreground` | `#626b60` |
| `--secondary` | `#edeee2` | `--input` | `#dcdecd` |
| `--brand` | `#9a3f28` | `--brand-ink` | `#8f3f1f` |
| `--brand-soft` | `#e8cbb8` | `--brand-foreground` | `#f8f4ef` |
| `--verify` | `#0e9e76` | `--verify-ink` | `#0a7558` |
| `--verify-soft` | `#d6f1e7` | `--witness` | `#b3402a` |
| `--witness-ink` | `#9a3016` | `--witness-soft` | `#f4ded4` |
| `--destructive` | `#c0442e` | `--ring` | `#9a3f28` |
| `--radius` | `.75rem` | | |

**The signature:** `brand` / `verify` / `witness` — provenance encoded as colour,
each with an `-ink` (text-safe), `-soft` (wash) and `-foreground` (on-fill) member.
No other pack in this skill has this.

### Dark twin (`.dark`) — warm black, *not* green

`--background #14110e` · `--foreground #f7f3ec` · `--card #1c1815` ·
`--muted #262019` · `--muted-foreground #a89e8f` · `--border #ffffff1a` ·
`--input #ffffff24` · `--brand #cf7a52` · `--verify #2bc0a8` ·
`--witness #e06a4f` · `--destructive #e5654c`

### Type — exactly three families

| Role | Family | Observed |
|---|---|---|
| Display | **Bricolage Grotesque** | 600, `-0.025em` tracking, `1.02` line-height, clamped to `2.6rem` at the hero |
| Body | **Geist** | 400, 16px / 24px |
| Data | **Geist Mono** | 12px, used for labels and the `>_` affordance |

### Texture & surface

- **Elevation is borders, never shadow.** The only `box-shadow` on the page is
  Tailwind's all-transparent reset. Every section separator is
  `border-t border-border` / `border-b border-border`.
- **Grain** (copyable recipe): SVG `feTurbulence type="fractalNoise"`,
  `baseFrequency 0.82`, `numOctaves 3`, `stitchTiles="stitch"`, 150×150 tile,
  `opacity .5`, `mix-blend-mode: soft-light`, `position:absolute; inset:0`.
- **Radii:** base `--radius: .75rem` on the shadcn sm/md/lg/xl ladder, plus
  `rounded-full` for the nav pill and primary CTA (33 occurrences — the most
  common radius on the page).

### Motion

- Transitions: **150ms `cubic-bezier(.4, 0, .2, 1)`**, scoped to named properties
  (`transform`, `background-color`, `border-color`) — never `all`.
- Product keyframe vocabulary: `sym-verify`, `sym-recall`, `verify-pulse`,
  `gf-copy-node`, `gf-copy-ring`, `gf-copy-label`, `gf-marquee`, `gf-tab-in`,
  `glitch-fx`.
- A full-bleed `<canvas>` in the hero renders the drifting chalk-mathematics
  field (∀ ∃ ∫ λ ⊂ ≈ θ π √ Σ ∆x dx ƒ″ ∮ ⊗). This is the pack's particle-field
  analogue.

### Controls

| Control | Observed |
|---|---|
| Primary CTA | `#fff` fill, ink `#07281f`, `rounded-full`, `8px 16px`, 14px/500 |
| Secondary | `#f8f7f0` fill, `12px` radius, `12px 20px`, 14px/600 |
| Ghost on dark | `rgba(255,255,255,.06)` fill, `1px` `rgba(255,255,255,.2)` border, ink `rgba(255,255,255,.9)` |

### Not yet extracted (a restart should finish these)

- Sections below the fold — one inverted section observed (`text-[#eef6f1]`).
- Focus-visible ring treatment.
- Spacing ramp (only `max-w-6xl` / `px-6` container observed).
- Measured WCAG ratios for every pair — **`orchard.md` sets the bar that these
  are computed, not asserted.**
