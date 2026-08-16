# Vitrine — the contract this design system ships under

**Register.** Choose Vitrine for **the page a serious product ships as its front
door**: B2B software sold on trust, security and compliance surfaces, specification
and comparison pages. Light is the default register and dark is a first-class twin;
both come from the same tokens, so build every screen against `var(--…)` and never a
literal.

**Structure is drawn entirely in hairlines.** No card fill doing elevation, no shadow
doing depth. `--panel` is a grey step that **groups without lifting** — it makes a
region read as held together, never as above, and the moment it also gets a shadow
the page acquires a depth order it was never designed to have.

**The primary control is the INK.** On a page whose whole language is a hairline, an
accent-filled button is the loudest object by a wide margin; the accent's job here is
to mark what can be **read**.

**One framed object per page.** The frame's 1px inset highlight is the whole
difference between a case and a bordered box with a drop shadow — remove it and the
signature becomes something every pack has.

**Three of the reference's own colour roles fail WCAG on its own canvas and are not
copied.** Every value is the reference's except where a measurement says it cannot
be, and the token layer marks each substitution. Restoring "the originals" restores
three failures.

**Status is never by colour alone.** Every state is a dot or an icon **plus a word**.

**Bans** (verbatim from the pack):

- No accent fill on a control; no second shadow; no serif paragraph.
- No card that is both bordered and filled — one or the other.
- No photograph and no illustration in the first viewport.
- No promise without its limit, and the limit is marked by a rule rather than set in
  the accent — a bound that looks like a link gets clicked.
- No status by colour alone.
