# Nameplate — the contract this design system ships under

**Register.** Choose Nameplate for **pages whose argument is that named third
parties will vouch for you**: press and media placement, PR distribution, trust
marks and badges, certification and accreditation, review aggregation and
"as featured in" surfaces. A cool near-white slab, a page that is square almost
everywhere, and one round shape reserved for a plate carrying somebody else's
name. Build every screen against `var(--…)` and never a literal.

**The page is square, and that is the discipline.** 87% of the reference's
rendered elements sit at zero radius — 1,091 of 1,251 measured. `--r-xs` (4px)
is an inline tag, `--r-sm` (8px) an inner well, `--r-md` (16px) a card or the
framed panel. `--r-pill` belongs to the plate and to the two CTAs, and to
nothing else. Every radius you add spends the plate's meaning.

**The plate is drawn by its border.** White fill, 1px `--line`, `--r-pill`,
`--shadow-pill` at 4% and 2px blur, one borrowed name as 15px/500 type at
`--pill-h`. It carries **type, never a logo** — that is what lets thirty of them
sit together without becoming a ransom note of thirty typefaces. One name per
plate. Give it a fill and it stops being a nameplate.

**The lift is one gesture.** On hover a plate translates by `--lift` (2px) *and*
grows its shadow to `--shadow-pill-hover`, both over `--dur-base` (200ms) on
`--ease-out`. Animating one without the other is the fastest way to break the
pack. `:active` returns the lift to zero over `--dur-press` (140ms).

**Elevation is a hairline, with one exception per screen.** `--shadow-frame` —
25px offset, 70px blur, 7% — belongs to the framed panel holding the
demonstration, and to nothing else. Two of them in one viewport spends the only
depth the page has; one on a card or a control makes the pack look like a
template.

**The action is a ramp, and it does not change on hover.** `--action` is a
two-stop coral gradient; hover spends `--shadow-action-hover` plus the lift,
`:active` swaps to `--action-pressed`. Darkening a coral on hover reads as a
disabled state. At most one primary per view. The blue is **not** the action —
it is `--link` and `--focus-color`, and the reference's declared tokens make it
look primary while the render disagrees.

**Colour corrections you must not undo.** White on the reference's own coral is
2.90:1; `--action` holds the hue and moves lightness until white clears AA
along the whole ramp. The reference's body grey is 4.42:1 on `--field`, so
`--ink-body` is darker. Its focus ring is `rgba(…, 0.35)` at 1.34:1 against a
3:1 floor — the ring here keeps the measured hue and is **opaque**. Reverting any
of the three reintroduces a measured failure.

**Two fields, and white is the resting state.** `--bg` is the page, `--field` the
cool slab an act stands on. A card on the slab is white with no border; the same
card on white takes a 1px `--line-soft`. This pack never separates by going
darker — `--surface-2` is an inset well, not a card.

**Status is never by colour alone.** `--good` / `--warn` / `--danger` / `--info`
each take a glyph or a label beside the colour. The set was searched, not
picked: with a coral action in the palette a conventional red danger is
indistinguishable from it under every dichromacy, so `--danger` is deep, and
`--info` is a cyan because the blue is already `--accent`.

**Type: one family, body at medium.** Poppins at four weights. Body is 17px at
**weight 500** with a 1.6 line-height; display is 700 tracked `--track-display`
(−0.02em). Two uppercase registers exist and are not interchangeable —
`--track-caps-control` (0.06em) on a button label, `--track-caps-micro`
(0.175em) on a micro-link.

**Every control clears `--tap-min` (44px).** This is a correction: 87 of the
reference's 137 visible interactive elements at 390px are shorter than that.

**No texture, no dark variant, no scroll clock.** There is no grid, noise or
pattern — acts are separated by returning to white, by a 1px rule, and by the
`Wave`. The reference has no dark band anywhere, so a dark theme here would be
invented. `MOTION_INTENSITY` above 4 has nothing legal to buy: no parallax, no
scrub, no `animation-timeline`.

**Reduced motion collapses every duration and the lift to zero**, and content is
never gated behind a reveal that did not run.
