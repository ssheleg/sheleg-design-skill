# Style pack — Workbench

Origin: the Builder Pro AI production design system (light+dark token
layer) blended with GitHub-style border discipline and quiet stat-tile
surfaces. A calm, dense, utilitarian product UI: neutral grays, borders as
elevation, one functional blue accent, mono for data. Design serves the
product — never performs.

## Register

Choose this pack for **product surfaces**: dashboards, admin panels,
internal tools, dev tools, analytics, settings. This is the one pack meant
to be used **standalone** — the SHELEG cinematic motion layer is out of
scope here; motion is limited to meaningful 150–200ms state transitions.
Light is the default register; dark is a first-class twin, both from the
same tokens.

## Palette

Ready-made token layer: [`tokens/workbench.css`](./tokens/workbench.css)
(light `:root` + `data-theme="dark"` twin) — copy it verbatim instead of
transcribing this table.

| Token | Light | Dark | Role |
|---|---|---|---|
| `--bg` | `#f7f8fa` | `#0f1218` | app ground |
| `--panel` | `#ffffff` | `#161b24` | cards, bars, dialogs, inputs |
| `--panel-2` | `#f7f8fa` | `#1b212c` | inset / table headers / quiet stat tiles |
| `--ink` | `#1a1f2b` | `#e8ecf3` | primary text |
| `--muted` | `#5b6472` | `#8a93a6` | secondary text, labels, metadata |
| `--border` / `-strong` | `#e6e9ef` / `#d7dce4` | `#232a36` / `#2c3441` | 1px lines / stronger edges |
| `--accent` (`-weak`) | `#2f6feb` (`#eaf0fe`) | `#4b8bff` (`#1b2740`) | THE one accent + its tint |
| `--ok` | `#1a7f37`-family green | brightened | done / healthy / success |
| `--warn` | amber | brightened | needs a human / waiting (reserved) |
| `--danger` | red | brightened | failed / error / incident |
| `--info` | blue | brightened | running / working |

Semantic colors are STATE ONLY, never decoration; each has a `-weak` tint
for badge/banner fills. Amber is reserved for "a human is needed". A second
accent hue is a design defect. Sequential data scales (heatmaps, charts)
are tints of `--accent`, not a new hue.

## Type

- UI face: system stack (`-apple-system, "SF Pro", "Segoe UI", sans-serif`)
  — zero load cost. Weights 400 body / 600 emphasis / 700 headings only.
- Data face: `ui-monospace / SF Mono` for ALL data — ids, metrics,
  timestamps, counters, chips, logs; `font-variant-numeric: tabular-nums`
  wherever digits align.
- Compact scale: 11px chips/meta · 12px labels (uppercase, tracked .1em) ·
  13px body/dense UI · 15px card titles · 20px sections · 28px page title.
- Running text ≤65ch; headings `text-wrap: balance`.

## Texture & surface

- **Elevation = border, not shadow**: layers separate via 1px `--border` +
  `--panel`/`--panel-2` steps. One soft shadow token exists, for true
  overlays (dialogs, popovers, menus) only.
- Radii: 6px controls · 8–10px cards · 999px chips/pills. Nothing else.
- 4px base grid; spacing steps 4/8/12/16/24/32; chips 2×8, dense rows
  8×12, cards 12–16. Compact by default.
- Stat tiles: label 12px `--muted` + value 20–28px semibold tabular-nums
  on a quiet `--panel-2` fill or 1px-border card — no gradients, no fills
  with meaning-free color.
- No decorative containers, no icon noise: if an element doesn't inform
  or act, it doesn't exist.

## Motion tokens

- 150–200ms, ease-out, and only where it carries meaning (state
  transition, attention pull); nothing looping, nothing scroll-driven.
- Hover/press transitions 120ms on background/border/color only — no
  translate/bounce on controls.
- `prefers-reduced-motion` → transitions off; the UI is fully static-safe.

## Signature motifs

- **Glanceability**: every surface answers its question in one glance —
  state → status dot/chip, trend → axis-less sparkline, change → one
  delta line («+4 done · fix deployed»). Detail is one drill-down away.
- **Honest state**: no fake "connected", no optimistic spinners; degraded
  renders visibly degraded (dimmed pane, banner, chip).
- Canonical atoms, built once: status dot (7–8px), mono chip (11px, 1px
  border, radius 999), card (panel + border + title row + right chip),
  progress bar (4–5px, border track, accent fill), segmented pill
  controls, empty state = one dim sentence + one action (no
  illustrations).
- Data tables: 32–36px rows, `--panel-2` sticky header, hairline row
  dividers, right-aligned numeric columns.

## Micro-interactions

- Hover on rows/nav: `--panel-2` fill; selected/active: `--accent-weak`
  fill + 2px accent inset indicator.
- Buttons: primary = accent fill (max one per view); secondary =
  1px-border ghost; destructive = red-border ghost + confirm. Toggles,
  not checkboxes, for enable/disable.
- Focus-visible on everything: 2px accent outline, offset 2px; contrast
  ≥ WCAG AA on both themes.
- Keyboard-first: every primary action reachable via keyboard; ⌘K
  palette as the front door where the product has one.

## Bans

- No gradients, no shadows-as-decoration, no glassmorphism, no
  illustrations/mascots, no icon noise, no emojis in product UI.
- No second accent hue; no semantic color used decoratively; no amber
  outside "needs a human".
- No display/serif fonts — this is a workbench, not a brand page.
- No spinners where live state exists; no badge without an action.
- No cinematic/scroll-driven motion — that belongs to the other packs'
  register.

## Gotchas

- Ship light AND dark from day one via the token layer — retrofitting a
  theme later leaves inverted hardcodes (sweep raw hex; consume only
  `var(--…)`).
- Guard contrast with a test: muted-on-panel-2 combinations silently
  fail AA when tokens drift.
- One shared Chip/Badge/Button primitive — three inline copies of an
  atom is how a token layer rots.
