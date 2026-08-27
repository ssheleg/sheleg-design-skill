# Surface composition — depth, and the handoff to `dataviz`

Two things a surface needs that the pack layer does not decide: how many planes
it has, and what a chart drawn on it is allowed to use.

**Load this when** you are about to write CSS for a cinematic page (the depth
half) or about to draw a chart in any pack (the dataviz half). Neither half is
needed to choose a pack, so neither belongs in the entry point.

Both sections moved here from `SKILL.md` in 1.11.0, unchanged. Two paragraphs
are **new** and marked *(added 1.11.0)* where they appear: what a `core` contract
implies for layer 1, and the fact that `--border-strong` is a role rather than a
name. Neither existed before; saying which is which is the difference between a
move and a rewrite.

## Contents

- Scene depth — six layers
- Charts and data — hand the pack to `dataviz`

## Scene depth — six layers

A cinematic page is not flat content with motion on top; it is a scene, and a
scene has depth. Assign every element a layer before writing any CSS. The
common failure is not "too little animation" — it is everything sitting on one
plane, which no amount of easing repairs.

| Layer | What lives there | Treatment |
|---|---|---|
| 0 | field, background imagery | slight blur, lowest contrast, slowest parallax |
| 1 | ambient texture: grain, gradient wash, mesh | fixed, `pointer-events: none`, never on a scroller |
| 2 | structural furniture: rules, grid marks, section labels | no parallax; they anchor the grid |
| 3 | the subject: product, hero artwork, the thing being sold | sharpest, largest, leads the motion |
| 4 | content: type, cards, controls | full contrast; readability outranks depth |
| 5 | overlays: nav, modals, cursor effects, scrims | above everything, documented z-index |

Rules that hold in every pack:

- **Three layers minimum per section.** Two is a flat page with a shadow.
- **Depth comes from treatment, not just `z-index`** — blur, scale, contrast and
  parallax rate together, or the layering reads as stacking.
- **Layer 4 never trades contrast for atmosphere.** If the text needs the scrim,
  the scrim is layer 3's problem.
- **Decorative layers are `aria-hidden="true"`.** Depth is visual; it never
  reaches a screen reader.
- **Below `pointer: coarse`, collapse 0–2 toward the field.** Parallax on a
  phone costs frames and buys nothing.

*(added 1.11.0)* A pack on the **core** contract does not specify layer 1: whether it has an
ambient texture at all is part of `Texture & surface`, which every pack states.
A pack that bans grain and blur leaves the slot empty rather than filling it —
"the darkness itself is the texture" is a decision, not a gap.

## Charts and data — hand the pack to `dataviz`

Do not restyle charts from the pack by hand, and do not let a chart library pick
its own colours. The `dataviz` skill already owns chart form, colour roles and
the runnable palette validation; a pack is the *parameter set* it consumes.

**Read the chosen pack's own token names before you write a single `var()`.**
This table is by *role*, not by token, because the names are not uniform across
the thirty-six packs: only `--bg` and `--ink` resolve in every pack. The accent is
`--accent` in twenty-nine of the thirty-six packs, `--brand` in `field-notes` and `--cta` in `orchard` (each
declares `@role accent:` in its token layer). **A second marker joins it in 1.26.0:**
a semantic colour that sits below WCAG AA on its own field declares
`@role non-text:` with the reason and the ratio, because nineteen of the token layers
carry such a colour and each said so in a different phrasing — "never text on the field",
"a FILL and large-text colour", "a fill, not a text colour", "No coral word under 24px",
"category marks" — which is exactly why nothing could check it.

Status colours are the least uniform thing in the library, so the full map is here
rather than summarised — and it is a **table** so that
`validate_status_vocabulary()` can compare every row against the token layers.
The prose version of this map was wrong in three places at the twenty-ninth
pack, because a sentence enumerating packs is not something a gate can read.

| Status set (non-variant tokens, root block) | Packs |
|---|---|
| `--danger` / `--info` / `--ok` / `--warn` | almanac, daylight, instrument-console, ledger, notation, patchbay, proscenium, router, vitrine, workbench |
| `--danger` / `--good` / `--info` / `--warning` | blueprint, cyclorama, maquette, prism, showroom |
| `--danger` / `--good` / `--info` / `--warn` | bulletin, deskmate, nameplate, onionskin, ora, paperclip, pigeonhole, rimlight, scoreboard |
| `--danger` / `--info` / `--success` / `--warning` | datasheet, manpage |
| `--danger` / `--good` / `--warn` | awning, tenor |
| `--danger` / `--info` / `--success` / `--warning` | outrank |
| `--good` / `--warn` | babylove |
| `--danger` / `--good` / `--info` | atrium |
| `--danger` / `--good` | roster |
| `--danger` | field-notes |
| `--good` | briefing-room |
| *(none)* | editorial-luxury, orchard |

Writing `var(--warning)` in `atrium` is the trap this table
exists to prevent — it is the shape of a token this pack does not have — a pack with no status palette does not
get one invented for it; the chart uses categorical hues and a label.

An undefined custom property does not error. `color: var(--good)` where
`--good` is undefined makes the declaration invalid at computed-value time, so
the property silently falls back to its inherited or initial value — which is
why guessing a token name is the quietest way to ship a wrong chart.

| `dataviz` parameter | What the pack supplies | Where to find it |
|---|---|---|
| Ramps | the pack's tint/step scale, where it has one | its Palette table; not every pack ships a ramp |
| Categorical order | a fixed hue order drawn from the pack, assigned once, never cycled | Palette + Signature motifs. Most packs carry **one** accent and ban a second hue, so a multi-series chart usually means small multiples, or one accent series against `--border-strong` — or a validated `--chart-1…N` set added to the **token layer** in the same change. `field-notes` and `scoreboard` each ship one today |
| Sequential hue | the pack's single accent hue | `--accent`, or the token its `@role accent:` names |
| Diverging pair | two poles from the pack, with a neutral grey midpoint | Palette. A one-accent pack has no sanctioned second pole; status colours are state-only and may not stand in. If the pack has no pair, that is a gap to close in the pack |
| Status palette | the pack's status set, **if it has one**, distinct from categorical | Palette; `editorial-luxury` and `orchard` have none |
| Surfaces | `--bg` for light, the pack's dark field for dark | resolves in all twenty-one |
| Texture fill | the pack's grain or hatch, for the print and forced-colours case | Texture & surface — several packs ship none, in which case the forced-colours fallback is shape and label, not fill |

Two rules survive the handoff unchanged: **never a dual-axis chart**, and
**colour follows the entity, never its rank** — a filter that changes the series
count must not repaint the survivors.

*(added 1.11.0)* `--border-strong` is itself a role rather than a name:
`instrument-console` spells it `--hairline-strong`. Check the token layer before
reaching for it, the same way you would for the accent. A test agent building a
chart in that pack hit this and corrected the table itself.
