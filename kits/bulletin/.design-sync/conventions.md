# Bulletin — the contract this design system ships under

**Register.** Choose Bulletin for **front doors whose argument is breadth**: a
tool that does many things across many channels for many clients, sold
cheerfully to a small team or an agency — social and content platforms,
scheduling and inbox products, all-in-one SMB SaaS, marketplaces of small
features. Warm cream paper, flat pastel bands, and every object drawn rather
than tinted. Build every screen against `var(--…)` and never a literal.

**Elevation is a hard offset and it never blurs.** A 1px `--line` outline plus a
zero-blur ink shadow — `--shadow-1` 2px for a chip, `--shadow-2` 3px for a
control, `--shadow-3` 4px for a card, `--shadow-4` for the one framed panel per
page. One soft shadow anywhere and the pack is gone. An offset without an
outline reads as a rendering fault.

**The press.** A control translates by `--press-travel` exactly as its offset
shrinks to `--shadow-press`, so the ink displaced stays constant; `:active`
travels one more pixel and the offset goes to nothing. Hover and
`:focus-visible` share the rule, so a keyboard user sees it. A **surface** does
the opposite: its offset grows to `--shadow-3-wide`. One move per kind of
object.

**The accent rule.** There is exactly one accent (`--accent`) and it is a fill
and a mark, never a word — at 2.77:1 on the paper it sits below the non-text
floor. The filled control uses `--action`, a derived value: the reference sets
white on the measured orange at 2.89:1, which is under AA and under the
large-text floor, so no type size rescues it. Links use `--link` with an
underline. At most one accent fill per view.

**Status is never by colour alone.** `--good` / `--warn` / `--danger` /
`--info` are state, never decoration, and every one of them ships beside a word.
Under deuteranopia `--danger` and `--warn` separate by 0.7; the word is the
message and the colour reinforces it. The `[data-surface="ink"]` block remaps
all four — a theme that remaps its ink and leaves its statuses behind paints
1.3–2.0:1.

**Type.** Two families: Bricolage Grotesque for display, DM Sans for body. The
control label is **heavier than the headline** — 800 against 700 — and that is
measured, not a flourish. **Tracking is zero at every size.**

**Bans** (verbatim from the pack):

- No blur on any elevation. No offset without an outline.
- No second orange fill in one viewport; no accent as a word.
- No tracking, anywhere.
- No gradient in a band — the bands are flat.
- No status by colour alone.
- No motion beyond the press and a fade: no parallax, no scrub, no sticky
  choreography, no marquee.
- No white page. White is a card; the field is `--bg`.

**Motion does not cross.** A kit is the static half of a pack. The press is
specified in `styles.css` and described here; nothing else in this package
animates, and `prefers-reduced-motion` collapses every duration and both travel
distances to zero at the token layer.
