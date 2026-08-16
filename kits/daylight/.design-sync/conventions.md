# Daylight — the contract this design system ships under

**Register.** Choose Daylight for **client-facing portals and the pages that sell
them**: onboarding, workspaces a customer logs into, service dashboards, scheduling
and billing. Light is the default register and dark is a first-class twin; both come
from the same tokens, so build every screen against `var(--…)` and never a literal.

**Elevation is one shadow, and it is a budget.** `--shadow-lift` is 90px of blur at a
−30px spread and it belongs to **one object per view** — the thing the page is about.
`--shadow-1` is the quiet card shadow for everything else, and most things get
neither. A card component that ships the lift as its default gives every card the
hero object's weight and the page loses its focal point without any single change
looking wrong.

**The accent rule.** There is exactly one accent, and at most one accent fill per
view. `--info` deliberately *is* the accent: a second blue would separate from `--ok`
by less than the palette gate's hard floor. `--danger` is **derived, not measured** —
the reference paints no error state — and the token layer marks it at the
declaration.

**Status is never by colour alone.** Every state is a dot or an icon **plus a word**.
Under deuteranopia `--danger` and `--warn` separate by 1.6; no palette solves the
green/amber/red triple, so the word carries the meaning.

**Bans** (verbatim from the pack):

- No second lift; no shadow on a button or an input.
- No third family — display, body, and a mono for figures only.
- No compressing the section rhythm to fit more above the fold; the space is the
  argument.
- No accent on a large surface; no testimonial in the first viewport.
- No status by colour alone.
