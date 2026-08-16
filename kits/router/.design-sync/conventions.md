# Router — the contract this design system ships under

**Register.** Choose Router for **product consoles and the marketing pages that
have to look like them**: dashboards, admin surfaces, developer platforms, billing
and usage screens, and a landing page whose argument is *here is everything the
thing holds, and its state*. Light is the default register and dark is a
first-class twin; both come from the same tokens, so build every screen against
`var(--…)` and never a literal. Body is **14px at weight 450** — the half step
above normal is measured off the reference and is the density of the whole
interface; nothing here scales the body at any width.

**Elevation is the seam, not a shadow.** A 1px `--border` at 7.8% of the ink,
everywhere a lesser pack would reach for a shadow. The single `--shadow-1` token
exists for a menu and for nothing else. A card is `--panel` on `--bg` with that
seam and radius 8, and that is the entire model.

**The accent rule.** There is exactly one accent (`--accent`), and at most one
accent fill per view — the single action the screen exists to make easy.
`--info` deliberately *is* the accent value, which is the reference's own
decision: its `--color-info` and its `--or-royal` are the same hex. A second
accent hue is a design defect.

**The triplet.** Every status holds three tokens rather than one: `--ok-mark` is
painted, `--ok` is written, `--ok-weak` is laid under. The colour you paint with
is not the colour you write with, and the `-mark` values are identical in both
registers because only the words have to be read.

**Status is never by colour alone.** Every state is a dot **plus a word**. Under
deuteranopia `--danger` and `--warn` separate by 1.2 — the green/amber/red triple
is the classic confusion set and no palette solves it, so the word carries the
meaning and the colour reinforces it. `StatusDot` requires its `label` in the
type for this reason.

**The control edge is not the seam.** `--edge` is a separate token at 3.05:1,
because WCAG 1.4.11 wants 3:1 for the visual boundary of a control and the seam
is 1.35. Reusing the seam as a button's border ships controls whose edges fail.

**Bans** (verbatim from the pack):

- No shadow as elevation; one lift exists and it is a menu.
- No second accent; no accent inside a chart — a bar wearing the button's colour
  tells the reader the bar is clickable.
- No status by colour alone; no body text below 14px and no scaling of the body.
- No uppercase in a table header — the reference does not do it, and its absence
  is what makes those tables read as software rather than as a report.
- No entrance motion, no shimmer, no spinner. Nothing animates on arrival.
- No search field that searches nothing, and no window chrome, title bar or
  traffic lights. This pack's reference is a real console and drawing a fake one
  is its specific occupational hazard.
