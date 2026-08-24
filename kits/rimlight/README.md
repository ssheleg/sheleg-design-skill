# @sheleg-design/rimlight

The React reference kit for the SHELEG **Rimlight** style pack — a white field, one
near-black act, a monospace carrying every piece of chrome, and an elevation made of
coloured light rather than shadow.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/rimlight.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and types
in every SHELEG kit, so switching packs swaps identity rather than API.

## This pack's own

`LitButton` (the sixteen-layer rig, one per viewport), `Tile` (the 80px icon square
that opens a section, and one of only two objects allowed an ordinary shadow), `Label`
(the monospace chrome — untracked, always) and `Act` (a full-bleed section, including
the dark one, which is a surface variant and never a document theme).

## The three rules that carry the kit

1. **One lit control per viewport.** The rig is the only chromatic event on a page
   otherwise made of ink, one blue and two greys — so the most saturated thing on the
   screen is also the thing you are meant to click. Two of them and that stops working.
2. **The light does not move.** It is deliberately absent from `.rl-lit`'s transition
   list. A static light reads as craft; an animated one reads as a toy.
3. **The monospace is chrome and the grotesque is prose.** Never mix the two roles, and
   never track the monospace.

**Motion does not cross into a design tool.** A kit is the static half of a pack: this
one is unusually literal about that, because the pack's whole motion budget is a 0.3s
colour transition.
