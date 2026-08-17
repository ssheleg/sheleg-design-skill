# Proscenium — the contract this design system ships under

**Register.** Choose Proscenium for **product-led marketing front doors whose
argument is a demonstration**: SaaS home pages, launch and tour pages, any page with
six or more acts that needs a repeated beat. Light is the default register and dark
is a first-class twin; both come from the same tokens, so build every screen against
`var(--…)` and never a literal.

**The page is a sequence of acts on a fixed beat.** Two acts, then the same call to
action, again. The reader is never more than two acts from the next one, and the
cadence — not a divider or a colour — is what keeps a long page legible.

**One dark act, at the middle.** `--stage` is a measured gradient and the pack allows
exactly one block of it per page. A second makes the page read as a section list, and
it is the most likely drift because the block is the easiest thing on the page to
like.

**The control stays nearly square.** Radius 4 on buttons against 16 on cards, both
measured. Closing that gap is the single fastest way to make a page in this pack look
like every other generated landing page.

**The product is on screen before any claim is made**, inside a frame the fold cuts
off. `Frame cropped` is the signature: the panel runs off the viewport rather than
sitting complete inside it.

**Three shadows, three jobs.** `--shadow-card` (94px of blur, violet-tinted) carries
an argument card; `--shadow-hair` (a hard 1px 2px, no blur) carries a container card;
`--shadow-control` belongs to the primary button. A control never takes the card's
shadow and a card never takes the control's. Inside the dark act there is no shadow
at all — at 9% on a gradient it reads as dirt.

**Status is never by colour alone.** Every state is a dot or an icon **plus a word**,
and `StatusDot` makes the label a required prop so the rule cannot be skipped by
omission.

**Two status colours and the whole dark register are pack decisions, not
measurements.** The reference paints no success and no error state and has no dark
mode; the token layer marks each substitution at its declaration. Read them as
decisions, and re-check them if the reference ever ships the real thing.

**Bans** (verbatim from the pack):

- No second dark act; no scroll clock, no scrub, no parallax.
- No status by colour alone.
- No card shadow on a control, and no control shadow on a card.
- No closing the 4/16 radius gap.
- No second family, and no swapping Inter for a system stack "for now".
- No logo wall and no invented counter — a page with no real logos builds its proof
  rail from product facts and leaves no hole where one would go.
- No bloom under running text; no fixed CTA bar on a phone.
