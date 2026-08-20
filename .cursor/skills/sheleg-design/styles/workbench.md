# Style pack — Workbench

Origin: the Builder Pro AI production design system (light+dark token
layer) blended with GitHub-style border discipline and quiet stat-tile
surfaces. A calm, dense, utilitarian product UI: neutral grays, borders as
elevation, one functional blue accent, mono for data. Design serves the
product — never performs.
This `Origin:` names a product rather than an address, so a reader cannot check the pack against its source. That is a recorded exception, not an oversight: this pack predates the library's *no reference, no pack* rule, it stays on the `core` contract, and it is **never widened by invention** — the four sections it declines would have to come from taste wearing the authority of a measurement. An addressable reference is what would change that, in one change, with this line rewritten to the address.

Contract: core — this pack does **not** specify `## Components`, `## Hero`,
`## Responsive` or `## Signature element`. Per-component states (hover,
active, disabled), the opening viewport and its line ceiling, the collapse
rules, and the single element the page is remembered by are **yours to
decide** here, and you must say so out loud when you do. Everything the pack
*does* state is measured; the precision of that half is not evidence about
this half. The backfill is held rather than written from the token layer,
because filling these sections from tokens would be inventing values with a
citation attached — which is the one thing this pack layer exists to prevent.

## Register

Choose this pack for **product surfaces**: dashboards, admin panels,
internal tools, dev tools, analytics, settings. This is the one pack meant
to be used **standalone** — the SHELEG cinematic motion layer is out of
scope here; motion is limited to meaningful 120–200ms state transitions (`--dur-hover` 0.12s, `--dur-state` 0.18s).
Light is the default register; dark is a first-class twin, both from the
same tokens.

**Not for:** the marketing page a developer lands on before they ever sign in —
that is [`manpage`](./manpage.md), or [`pigeonhole`](./pigeonhole.md) where the
product files the reader's incoming mess into named categories. This pack is the
console they reach afterwards — and with `pigeonhole` it forms a deliberate pair,
whose seam is the category chip: if the marketing page names a category in a hue,
the application must name it in the same one.

**The fork against [`showroom`](./showroom.md).** Both render dense product UI,
both use borders rather than shadows inside that UI, both carry one blue accent.
The test is *which surface you are building*. This pack **is** the tool — it is
meant to disappear, and a page built in it is an application. `showroom` is the
marketing page **arguing for** the tool: it frames one real product surface as a
specimen under a seven-layer shadow and wraps a hero and a CTA around it. A real
product usually needs both, and the specimen in a `showroom` page should be a
screenshot of the `workbench` build.

**The fork against [`scoreboard`](./scoreboard.md)** is the same test on a
different axis: whose numbers are on screen. This pack renders the user's own
working data, in a surface they operate — filter it, sort it, act on it.
`scoreboard` renders a claim *about* numbers, on a marketing page whose argument
is that they accumulate. A metric the reader can drill into belongs here; a
metric the reader is being shown belongs there.

**The fork against [`paperclip`](./paperclip.md)** is the *which surface* test
one more time, and these two are deliberately close: both build elevation out of
hairlines and never shadows, both set data in a monospace, both ship a light
theme and a dark one. This pack **is** the application — no hero, no ornament
layer, one blue accent doing functional work. `paperclip` is the marketing page
arguing for an application of exactly this kind, and it spends its whole colour
budget on a single chromatic object that cannot be clicked, leaving every
control monochrome. A company selling an agent console needs both, and the mocks
inside a `paperclip` page should be the `workbench` build.

**The fork against [`ledger`](./ledger.md)** is the closest call in the family,
because both are standalone product-UI packs, both build elevation out of
hairlines and never shadows, and both set data in a monospace. The test is what
the reader is doing with the numbers. This pack is the console you **operate** —
cool neutral greys, a blue accent that fills the primary button, a surface built
to disappear while you filter, sort and act. `ledger` is the console you
**audit**: warm cream paper, an accent forbidden from filling any control, and a
per-card seal stating how each number was obtained. A product whose numbers a
model produced needs that seal; a product whose numbers the system already knows
does not, and paying for it is how a tool starts apologising for itself.

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
| `--accent-ink` | `#ffffff` | `#0f1218` | text **on** the accent — it flips with the theme, because white on the dark-mode accent fails AA |
| `--ok` (`-weak`) | `#1a7f37` (`#e6f4ea`) | `#3fb960` (`#12281a`) | done / healthy / success |
| `--warn` (`-weak`) | `#9a6700` (`#fff3d6`) | `#d9a93f` (`#2b2210`) | needs a human / waiting (reserved) |
| `--danger` (`-weak`) | `#d1242f` (`#fde8e9`) | `#e5534b` (`#2d1517`) | failed / error / incident |
| `--info` (`-weak`) | `#2f6feb` (`#eaf0fe`) | `#4b8bff` (`#1b2740`) | running / working |

Semantic colors are STATE ONLY, never decoration; each has a `-weak` tint
for badge/banner fills. Amber is reserved for "a human is needed". A second
accent hue is a design defect — `--info` deliberately *is* the accent hue
("running / working" is the product's own signal, not a new color).
Sequential data scales (heatmaps, charts) are tints of `--accent`, not a new
hue.

## Type

- UI face: system stack (`-apple-system, "SF Pro", "Segoe UI", sans-serif`)
  — zero load cost. Weights 400 body / 600 emphasis / 700 headings only.
- Data face: `ui-monospace / SF Mono` for ALL data — ids, metrics,
  timestamps, counters, chips, logs; `font-variant-numeric: tabular-nums`
  wherever digits align.
- Compact scale, **and it ships as tokens** (`--t-chip` 11px chips/meta ·
  `--t-label` 12px labels, uppercase, tracked .1em · `--t-body` 13px body and
  dense UI · `--t-card` 15px card titles · `--t-section` 20px sections ·
  `--t-page` 28px page title). It was prose-only until 1.16.0, which made the
  craft bar's *"no ad-hoc font size anywhere in the diff"* unachievable in this
  pack — there was nothing to reference, and this pack's own reference kit wrote
  twenty raw declarations because of it. No value changed in the tokenising.
- The 4px grid likewise: `--space-1` … `--space-6` = 4 / 8 / 12 / 16 / 24 / 32.
- Running text ≤65ch; headings `text-wrap: balance`.

## Texture & surface

- **Elevation = border, not shadow**: layers separate via 1px `--border` +
  `--panel`/`--panel-2` steps. One soft shadow token exists — `--shadow-1`,
  `0 4px 16px -8px rgba(26,31,43,.18)` — for true overlays (dialogs, popovers,
  menus) only.
- Radii: `--r-control` 6px · `--r-card` 10px · `--r-pill` 999px. Nothing else.
- 4px base grid; spacing steps 4/8/12/16/24/32; chips 2×8, dense rows
  8×12, cards 12–16. Compact by default.
- Stat tiles: label 12px `--muted` + value 20–28px semibold tabular-nums
  on a quiet `--panel-2` fill or 1px-border card — no gradients, no fills
  with meaning-free color.
- No decorative containers, no icon noise: if an element doesn't inform
  or act, it doesn't exist.

## Motion tokens

- `--dur-state` 0.18s with `--motion-ease` (`cubic-bezier(0.2, 0, 0, 1)`,
  ease-out), and only where it carries meaning (state transition, attention
  pull); nothing looping, nothing scroll-driven. This pack overrides the
  SHELEG default ease/duration set — there is no `epic` tier here.
- `--dur-hover` 0.12s on background/border/color only — no translate/bounce
  on controls.
- `prefers-reduced-motion` → transitions off; the UI is fully static-safe.

## Signature motifs

- **Glanceability**: every surface answers its question in one glance —
  state → status dot/chip, trend → axis-less sparkline, change → one
  delta line («+4 done · fix deployed»). Detail is one drill-down away.
- **Honest state**: no fake "connected", no optimistic spinners; degraded
  renders visibly degraded (dimmed pane, banner, chip). For model-driven
  surfaces — streaming output, agent runs, generated content — the same rule
  expands into a full pattern set in
  [`AI_PRODUCT_PATTERNS.md`](../AI_PRODUCT_PATTERNS.md), which reuses these
  status tokens (`--info` running, `--ok` done, `--warn` needs a human,
  `--danger` failed).
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

- Status carried by hue alone. Success, warning, danger and info always
  ship with an icon or a word beside the fill — **status is never by
  colour alone**. Measured off a production reference, several of these
  pairs sit inside a dichromat's confusion line; re-stepping them would
  invent a colour this pack does not own, so the second signal carries
  the meaning instead.
- No gradients, no shadows-as-decoration, no glassmorphism, no
  illustrations/mascots, no icon noise, no emojis in product UI.
- No second accent hue; no semantic color used decoratively; no amber
  outside "needs a human".
- No display/serif fonts — this is a workbench, not a brand page.
- No spinners where live state exists; no badge without an action.
- No cinematic/scroll-driven motion — that belongs to the other packs'
  register.

## Gotchas

- **Five pairs in this palette miss AA in light mode, and the Gotcha below used
  to name a pair that passes.** Measured from `tokens/workbench.css` on
  2026-08-10: `--ok` on `--ok-weak` **4.47**, `--danger` on `--danger-weak`
  **4.47**, `--warn` on `--warn-weak` **4.41**, `--accent` on `--panel-2`
  **4.30**, `--accent` on `--accent-weak` **4.00**. All five are below the 4.5
  floor for normal text; `--muted` on `--panel-2` measures **5.63** and passes.
  The values are not changed, because a darker green invented here would be a
  colour this pack does not own. **The resolutions, which are rules rather than
  new tokens:** the status word inside a chip renders in `--ink` (14–15:1 on all
  three tints) with the status colour carried by the dot or the fill; and
  accent-coloured text never sits on `--panel-2`, on `--accent-weak`, **or on
  `--bg`** — in light mode `--bg` and `--panel-2` are the same `#F7F8FA`, so the app
  ground carries that same 4.30 and a plain accent link sitting directly on the
  dashboard background fails identically. This clause named only two of the three for
  four releases, which made the most ordinary element in an admin panel look covered.
  Inside a
  selected row or a sticky header, text is `--ink` or `--muted`.
- **`--bg` and `--panel-2` are the same colour in light mode** (`#f7f8fa`) and
  different in dark. So the mandated row hover — a `--panel-2` fill — is
  **invisible** if a table sits directly on `--bg`. Dense tables go on a
  `--panel` card, always. The same applies to a "quiet stat tile on `--panel-2`".

- Ship light AND dark from day one via the token layer — retrofitting a
  theme later leaves inverted hardcodes (sweep raw hex; consume only
  `var(--…)`).
- Guard contrast with a test: muted-on-panel-2 combinations silently
  fail AA when tokens drift.
- One shared Chip/Badge/Button primitive — three inline copies of an
  atom is how a token layer rots.
