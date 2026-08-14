# Brief — `paperclip`, the eighteenth style pack

- **Run:** `feat/paperclip-pack`, opened 2026-08-14 from `main` at `cc3b471`, **in its own
  worktree** at `/Users/sshlg/DATA/sshlg-skills-wt-paperclip`
- **Reference:** <https://paperclip.ing> — the marketing site of a product for hiring,
  organising and budgeting a team of AI agents
- **Opening request:** *"Давай ещё проработаем дизайн этого пейперклипа, тоже максимально
  глубоко, все стили, как сделан, и сохраним к себе в коллекцию"* — an address, twelve
  screenshots, and "save it to the collection", which is the fifth time in this repository
  an address has arrived as the whole request. ADR-0001 answers it: the pack is named for
  the register it encodes and the address lives in its `Origin:`. Here the reference's own
  name *is* the register — the shape language, the token names and the product are one
  joke about office supply — so `paperclip` is the register name and not a shortcut.

## The concurrency finding, recorded first because it decided the route

At the moment this run started, **another run held the `PACK-TENOR` lease on the same
checkout** (`.agent-sync/leases/PACK-TENOR.lock`, run `r-fe09aa614`, renewed 18:23:19,
last seen 18:26:40 — seconds before the check) and had already written `ora` and was
mid-flight on `tenor`: `styles/tenor.md` appeared between two directory listings four
minutes apart. Its uncommitted tree touched `README.md`, `SKILL.md`, `install.sh`,
`bin/cli.js`, `package.json` and all three manifests — every file this pack also has to
edit — and had claimed **1.28.0**.

`docs/DOCMAP.md` is unambiguous about this case: *"every concurrent run must take its own
`git worktree`."* This run did. Two consequences are carried rather than hidden:

1. The worktree branches from `main`, which holds **seventeen** packs. Every count this
   run writes is true of eighteen and will be wrong the moment `ora` and `tenor` land. The
   merge owes a recount, not a re-read.
2. **1.29.0 was taken to leave 1.28.0 alone.** The number is provisional and the CHANGELOG
   entry says so at the top. A version another run had already taken is a defect this
   repository shipped once already (`a9c497e`).

`agent-sync`'s own status could not have prevented this: its `fs` backend keys the run id
off the repository's shared `.agent-sync/run-id`, so it reported *this* session as
`r-fe09aa614` — the other run's id — and would have let it acquire anything. The lease
file's mtime, the `tenor.md` that appeared mid-session, and `git status` were the evidence.

## What was measured, and with what

| Instrument | What it produced |
|---|---|
| `curl` | `/` at 486,017 bytes; two stylesheets at 73,813 + 83,685 bytes, 622 + 712 rules |
| a CSS rule-splitter over both bundles | every `:root` and `[data-theme=dark]` block, resolved by role rather than by name |
| the hero's inline SVG, parsed | 45 `linearGradient`s, 89 distinct stops, 97 `rect`s in 8 `<g class="hero-bg-column">` groups |
| `colorsys`, over the 24 ramp endpoints | the generation rule: +12.4°/step on the top stop, −10.3°/step on the bottom, at near-constant S and L |
| a WCAG ratio script over 35 pairs | every ratio this brief and the pack state |
| `test/validate_palette.py` | the ratios recomputed from the token layer, plus OKLab separation under three dichromacies |
| the twelve screenshots supplied with the request | the sections in scroll order, and the two themes as shipped |

## The register, in one sentence

A neutral coal field on which **nothing functional is coloured**, and one loud chromatic
object that cannot be clicked. Every control is the inverted field; every container is a
hairline; every status is a word with a mark beside it. Colour arrives twice — the hero's
curtain of gradient capsules, and twelve gradient section badges — and both are labels or
scenery.

The identity in one sentence: **delete every colour from this page and it loses its
poster, not its meaning.** That is also the test the T27 pair is built around.

## Why the library has room for it, at eighteen packs

The pairwise question, asked against all seventeen (standing instruction 10). Three forks
are sharp enough to matter, and two of them are written into the packs on both sides:

- **`instrument-console`** — the near-twin on first impression: near-black, mono, machines
  at work. The distinction is what colour is *for*. There, one electric blue marks the
  value the reader must follow; here, colour cannot be interacted with at all. Reciprocal
  clause added to `instrument-console.md`.
- **`workbench`** — the same elevation model exactly (borders, never shadows), the same
  mono data, both themes. `workbench` **is** the application; `paperclip` is the page that
  sells one. The mocks inside a `paperclip` page should be the `workbench` build.
  Reciprocal clause added.
- **`orchard`** — both round generously and both put colour where the reader looks first.
  Warm oat invites a consumer to touch; neutral coal tells an operator the interface will
  stay out of the way. Reciprocal clause added.

Nothing in the library holds the "colour is ornament" thesis. `prism` has an iridescent
wash but spends it as identity; `briefing-room` and `maquette` are dark with a functional
hue; `roster` and `scoreboard` are white pages about proof. The gap is real.

## What the reference gets wrong, and the pack does not inherit

Recorded here because a pack extracted from a live site inherits its defects by default:

1. `--status-task-in_progress` stays at its light value on the dark field — **3.83:1** —
   and is rendered as text (`● 1 live`). The pack derives `#60a5fa` (7.79:1) and marks it.
2. The one text input sets `outline: none` on focus, leaving a 1px border colour change as
   the only focus indicator.
3. `dotPulse` and `statusBlink` — two 1.5s `infinite` loops — survive
   `prefers-reduced-motion`, which the reference otherwise honours in four places.
4. The budget bar transitions `width` for 1.2s, per bar, with six bars in view.
5. No `@media (hover: hover)` anywhere, so every hover fires on first touch — including
   the marquee's pause, which on touch stops the row and does not restart it.
6. `font-weight: 450` is asked for and only 400 and 500 ship, as static instances.
7. `--radius-md` and `--radius-lg` are declared and never spent; the alias row the
   components use skips both. Kept as shipped and documented, because a pack that silently
   repairs its reference stops being a measurement.
