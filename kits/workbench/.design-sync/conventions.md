# Workbench — the contract this design system ships under

**Register.** Choose Workbench for **product surfaces**: dashboards, admin panels,
internal tools, dev tools, analytics, settings. Calm, dense, utilitarian — neutral
grays, borders as elevation, mono for data. Design serves the product and never
performs. Light is the default register and dark is a first-class twin; both come
from the same tokens, so build every screen against `var(--…)` and never a literal.
Elevation is a 1px `--border` plus a `--panel` / `--panel-2` step, not a shadow;
the one shadow token exists for true overlays only.

**The accent rule.** There is exactly one accent (`--accent`), and at most one accent
fill per view — the single action the screen exists to make easy. Semantic colour
(`--ok`, `--warn`, `--danger`, `--info`) is **state only**, never decoration, and each
has a `-weak` tint for badge and banner fills. Amber is reserved for "a human is
needed". `--info` deliberately *is* the accent hue: "running / working" is the
product's own signal, not a new colour. A second accent hue is a design defect, and
sequential data scales are tints of `--accent` rather than a new hue.

**Bans** (verbatim from the pack):

- No gradients, no shadows-as-decoration, no glassmorphism, no
  illustrations/mascots, no icon noise, no emojis in product UI.
- No second accent hue; no semantic color used decoratively; no amber
  outside "needs a human".
- No display/serif fonts — this is a workbench, not a brand page.
- No spinners where live state exists; no badge without an action.
- No cinematic/scroll-driven motion — that belongs to the other packs'
  register.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack.
