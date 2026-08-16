# Almanac — the contract this design system ships under

**Register.** Choose Almanac for **pages that assert a category**: a manifesto page, a
company saying what this kind of thing is, a product whose argument is editorial. The
field is **oatmeal `#f0efe3`, not white**, and it is the whole first impression. Light
is the default register and dark is a first-class twin; both come from the same
tokens, so build every screen against `var(--…)` and never a literal.

**Seams are 2px and there is no 1px anywhere.** Structure is read by mass rather than
by contrast, which is why the seam values sit far under a hairline pack's and are not
a defect. Neither seam carries meaning alone: every panel edge in this pack has an
uppercase mono tag notched through it.

**One object floats per page**, on four stacked shadow stops whose deepest is 162px
of blur. A second floating object is the fastest way to lose the effect.

**`--warn` is two different colours and swapping them is silent.** `#993f0e` on the
light register and `#fa6838` on the dark are the same orange at two steps, because
the bright one measures 2.32 on oatmeal. Using the bright value on the light field
ships a warning nobody can read and nothing on screen looks broken.

**Status is never by colour alone.** Every state is a mono tag or a dot **plus a
word**. `--danger` is **derived** and is a crimson on purpose: an orange-red beside
this pack's burnt-orange warn fails the palette gate's hard floor.

**Bans** (verbatim from the pack):

- No 1px anywhere; no second floating object; no drawn box without its tag.
- No sentence in the mono — it is the label voice.
- No weight 700 as the default emphasis; 500 is the pack's weight.
- No white field. The oatmeal is the identity.
- No status by colour alone.
