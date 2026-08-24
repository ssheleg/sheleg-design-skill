# Rimlight — the contract this design system ships under

**Register.** Choose Rimlight for **a studio's own front door and the pages that sell
what it makes**: design and engineering agencies, product studios, service and
case-study pages, B2B surfaces whose argument is craft rather than a feature list. A
white field, a cool grey act separator, one near-black act, and coloured light where
other systems put a shadow. Build every screen against `var(--…)` and never a literal.

**Elevation is a light, and it belongs to one control.** `--glow-rig` is sixteen
layers — six lit and ten held at alpha 0, thrown from below and to the left. Exactly
one control per viewport wears it. Two lit controls and the light stops meaning *this
one*.

**The rig is static.** It does not change on hover, press or focus: the fill moves one
step and the light stays. Pulsing, rotating or hover-growing it is the first ban here,
and it is the single change that turns this pack into a novelty.

**The only other shadows are the tile's.** `--shadow-tile` on the 80px icon tile and
`--shadow-tile-inner` on its 68px image. Nothing else carries one — 483 of the
reference's 487 visible elements compute `box-shadow: none`. A card has no shadow and
no border; it is separated by the field it sits on.

**The monospace is the chrome.** Every nav item, button and label is Source Code Pro;
every sentence is Archivo. That split is how a reader tells a control from a statement
without reading either, and it is not decorative.

**Do not track the monospace.** `letter-spacing` computes to `normal` on every label
in the reference — the openness is the face's own advance width. Adding tracking is
the trap this pack sets for anyone matching it from a screenshot.

**No bold anywhere.** 500 is the heaviest weight and it belongs to the mono label; the
display runs at 400 and the lede at 300. The display is loud because it is 86px.

**Tracking is negative at every size and tightens as the display shrinks** —
`--track-display` (−0.02em) at 86px, `--track-display-narrow` (−0.04em) at the 40px
narrow headline.

**The blue is two tokens because it does two jobs.** `--accent` is 3.03:1 on `--bg`:
legal on a word only at WCAG large text, which at weight 400 means ≥ 24px. Anything
smaller takes `--accent-ink`. A 16px link in `--accent` is a word below the floor and
is the commonest way to break this pack while believing you matched it.

**The colours live in the dark act.** Every one of the reference's five secondary hues
is 6.5–10.5:1 on `#1b1b1b` and 1.65–2.65:1 on white. They were designed for the dark;
on a light field they are not text.

**`[data-surface="dark"]` is a section, never the document.** There is no toggle and
no second palette for the page — one band is dark and the rest stays light. Putting it
on `:root` inverts a page that was never designed to invert, and the light field's four
statuses measure 1.1–1.5:1 if they arrive unremapped.

**Status is never by colour alone** — every state takes a glyph or a label beside its
colour. The four roles are derived rather than adopted: the reference's own secondary
set is a palette, not a scheme, with eight of its twenty-one pairs too close to
separate under dichromacy.

**Every control clears `--tap-min` (44px).** A correction: 26 of the reference's 37
visible interactive elements at 390px are shorter than that.

**Nothing travels in space.** No parallax, no scrub, no `animation-timeline`, no press
translation. `MOTION_INTENSITY` above 2 has nothing legal to buy, and reduced motion
collapses every duration to zero.
