# Orchard — the contract this design system ships under

**Register.** Choose Orchard for **approachable consumer biotech and DTC
wellness**: testing kits, supplements and personalized formulations,
subscription health, early-stage consumer science that has to feel warm and
credible at the same time. It suits a product whose buyer is being asked to
trust a lab result *and* a brand voice. The defining constraint is composition:
the page is a **stack of rounded slabs, not a continuous surface** — rhythm comes
from alternating slab fills (oat, sage, cacao) with `55px` of field between
them, and every slab is inset so the field shows around it. Elevation is light,
not shadow: two inset white hairlines make a flat fill read as a soft extruded
pill, and the only real drop shadow in the system is the CTA's ambient glow in
its own hue.

**The accent rule.** Three colours and nothing else: **oat is the paper, sage is
the brand, orange is the verb.** Sage (`--primary`, 3.4:1) and candy orange
(`--cta`, 2.8:1) are **fills, never text** — body copy on a sage slab sits on
`--primary-deep` or on an oat card, and the CTA label is `--cta-ink`, because
white on orange fails AA. There is **exactly one candy pill per view**; it is the
only orange object on the page, which is what makes it unmissable without being
loud. This pack has **no `--accent-ink`** — the role is `--cta-ink` on the pill,
`--on-primary` on `--primary-deep`, and `--on-ink` on the cacao surface. Writing
`var(--accent-ink)` here is an undefined variable that renders transparent.
`--ink-soft` is 4.1:1 on oat: a caption and citation colour, never body copy.

**Bans** (verbatim from the pack):

- Orange or sage as **text**; white text on the orange CTA; white text on
  `--primary` at body size (use `--primary-deep`).
- A true black, a cool grey, or any Framer/Tailwind default neutral
  (`#18181B`, `#1A1A1A`, `#F2F3F4`) beside the warm palette.
- A fourth hue; a second orange object in the same view; the CTA colour used
  for a non-action (a badge, a chart series, a heading).
- Sharp corners anywhere; a grotesque or a serif as the display face; a bold
  (700+) body weight.
- `transition: all`; hover states that scale or lift; a drop shadow in grey
  where the bevel belongs.
- Two adjacent slabs with the same fill; a section that bleeds edge-to-edge
  without the field showing around it.
- A claim without its citation line; a benefit heading where the reference
  would have written the reader's objection.

Motion is not part of this design system and must not be invented: the
word-by-word headline and the sticky visual column stay behind in the pack, and
a kit is the static half of one.
