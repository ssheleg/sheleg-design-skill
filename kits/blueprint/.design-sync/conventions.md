# Blueprint — the contract this design system ships under

**Register.** Choose Blueprint for **infrastructure sold on precision**: vector
databases, search and retrieval, storage and query engines. Its vocabulary is
technical drafting — a white sheet, a 32px grid, ruled column edges, registration
marks, one saturated blue used the way a draftsman uses ink. The fork people get
wrong is against `field-notes`: that pack is **warm paper** arguing from
provenance (*how do you know*), this one is **cold stock** arguing from precision
(*how is it built*). Against `instrument-console`: that pack's subject is a
running system with a changing value; this one's is a mechanism drawn to scale.
Build every screen against `var(--…)` and never a literal.

**There is no radius.** `--radius: 0`, everywhere, and the token exists so the
ban is greppable. The single exception is `--radius-round: 50%` for a dot or an
avatar. Most component libraries ship a default radius — zero it globally rather
than per component, or the page ends up with three rounded inputs nobody notices
until it looks cheap and nobody can say why.

**One blue does everything.** `--accent` `#002BFF` measures 7.53:1 as text on the
stock *and* 7.53:1 under white. It sets a heading word, draws a 1.5px rule, fills
a button and rings a focused input, with no second token. It is unusually
saturated and vibrates against `--ink` at small sizes — never set body copy in
it.

**The ink is not the reference's ink, and the pack says so.** The reference sets
pure black on 316 elements; the doctrine bans pure black as ink. This system
ships `#111827` — the reference's own second ink, on 136 of its elements. The two
sit 21.2 apart in OKLab: it is a visible substitution, not a rounding.

**Category marks are squares, not circles.** A circle is a status; a square is a
kind. Every pair clears both separation floors under all three dichromacies —
label them anyway, because a legend of four coloured squares is a legend nobody
reads.

**Bans** (verbatim from the pack):

- A radius. Any radius, on anything, except `50%` for a dot or an avatar.
- A shadow used for elevation.
- `--ink-faint` as text; `--accent` as a large field fill.
- A circle used as a category mark; a category colour used to mean health.
- The annotation size without its tracking; caps annotations set at 0.
- A geometric or humanist substitute for the display face.
- Fluid `clamp()` type; `transition: all`; `100vh`; a scroll listener.
- Animating the grid, or parallaxing it.
- A screenshot as the hero's figure. Draw it, or use `showroom`.

**The reference ships no `prefers-reduced-motion` branch at all**, against live
marquee, ping, pulse and scroll animations. This system requires the branch its
reference omits.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack.
