# Datasheet — the contract this design system ships under

**Register.** Choose Datasheet for **B2B SaaS whose product is a verdict about
the visitor, the request or the device**: fraud and bot detection, device
intelligence, identity and verification, anti-abuse, payment risk, API products
sold on the payload they return. The page is a spec sheet, and the specimen is the
reader — the instrument shows *their* visitor id, *their* city, *their* IP, and a
verdict reached seconds ago. The fork people get wrong is against `field-notes`,
which shares the off-white paper, the hairlines and the one warm accent: there the
small mono type annotates a **source** so a claim can be checked (*how do you
know?*); here it carries a **reading** about the reader (*what did you get?*).
Build every screen against `var(--…)` and never a literal.

**The accent is a mark and a fill, not a voice.** `--accent` measures 3.17:1 on
the field: enough for a non-text mark and for large text at 24px and above, not
enough for anything at body size. Its jobs are one word of a display headline, the
mono visitor id, a 2px focus ring, a tick, and a wash on a selected cell. Where an
orange must carry a word at body size, use `--accent-deep` at 5.11:1. The primary
button fills with `--action` — one ramp step deeper than the brand orange, because
white on the brand step measures 3.32:1 and fails AA — and darkens to
`--action-hover` on press.

**The instrument is not a card, and its cells never round.** A card is
`--surface` at `--r-card` with the inset elevation pair. The instrument is a grid
whose walls are 1px `--rule` at `--r-cell`, which is **0**. Rounding those cells is
the single edit that turns this system into a generic SaaS page. Padding is
`--pad-cell`; every cell is a 9px uppercase label over an 11px value, and machine
output — ids, IPs, hashes, timestamps — takes the mono face.

**Radii are concentric and the arithmetic is real.** 16 outside, 8 inside, 12 on
cards, 6 on buttons, 4 on controls, 2 on a chip, 0 on the instrument. An inner
radius is the outer radius minus the padding between them: the frame carries
`--grid` of padding, so its shell resolves to `--r-inner`. Never the same radius
twice in a nest.

**Elevation is inset, never dropped.** Cards and the frame carry the measured
two-line inset — a pale top edge, a darker bottom one. Nothing casts a downward
shadow, nothing lifts on hover, nothing scales.

**Status is never by colour alone.** Every status cell tints its whole background
with the matching `--*-weak` and **writes the verdict out**. The four statuses do
not separate under dichromacy — success and warning are 3.7 apart under
deuteranopia against a floor of 8 — so the tint is emphasis and the word is the
meaning. No bare dots, no traffic lights, and never a hue swap to signal disabled:
a disabled cell that changes colour reads as a different verdict. Disabled is 0.7
opacity with pointer events off.

**The dark surface is a state, not a theme.** `[data-state="alarm"]` exists
because the instrument **detected** something — on the reference, that the reader
is in incognito. Never wire it to a user preference, a toggle or
`prefers-color-scheme`; that destroys the one idea this system has. In the alarm
state the accent steps lighter, text on the accent flips to ink, and the status set
is selected rather than measured, danger from the pink ramp because a red cannot
sit beside an orange accent on a dark field.

**Type.** Two families only: Inter and JetBrains Mono. No serif anywhere. The
display weight is **500, not 600** — at 48px with -0.0625em tracking, 500 reads as
engineered and 600 reads as an advertisement. Tracking runs both ways: negative
and steep above 36px, positive and wide below 12px. A 9px label at neutral tracking
is the fastest way to make this system look like a generic admin theme.

**Motion.** One curve, one measured base duration (`--dur-base`, the reference's
own single duration token), and one measured stagger of `--stagger` between the
words of a display headline. Nothing exceeds 300ms. Colour and opacity only —
never a layout property, and never `ease-in`. Under
`prefers-reduced-motion: reduce` every duration and the stagger go to zero and the
headline arrives already in place.

**Never fabricate a reading.** If the instrument cannot show live data, it shows a
labelled last-known one — the reference's own badge reads *this is a demo,
production accuracy will be higher*. A screen in this system that invents an IP
address has told its only lie in its loudest element.
