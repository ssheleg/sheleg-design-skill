# Notation — the contract this design system ships under

**Register.** Choose Notation for **developer and technical products sold on
restraint**: open source front pages, workspaces aimed at people who dislike being
sold to, documentation homes. Light is the default register and dark is a
first-class twin; both come from the same tokens, so build every screen against
`var(--…)` and never a literal.

**Structure is drawn, not filled.** A group is a hairline box or a hairline above and
below. `--panel` is 2% off the field and is for grouping the eye already believes in,
never for creating it. There is one shadow token, at 4%, and it exists so a dropdown
does not merge with the page.

**The primary control is the INK.** The accent marks what can be **read**; the ink
marks what can be **pressed**. Swapping them is the single change that destroys this
pack, and it looks like an improvement in isolation — the button gets "brand colour"
and every link on the page loses its only signal.

**There is no bold.** `--w-semi` and `--w-bold` are both 500, deliberately. Emphasis
is the serif, the mono, or a rule.

**Status is never by colour alone.** Every state is a dot or an icon **plus a word**.
`--danger` is **derived, not measured**, and the token layer marks it at the
declaration.

**Bans** (verbatim from the pack):

- No accent fill on a control; no bold; no second chamfer on a page.
- No card fill where a hairline will do; no shadow used as elevation.
- No skeleton blocks — a grey rectangle on a page with no fills reads as broken
  layout rather than as pending data.
- No illustration, photograph or logo wall in the first viewport.
- No status by colour alone.
