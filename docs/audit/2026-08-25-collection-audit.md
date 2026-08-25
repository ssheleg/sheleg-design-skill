# Collection audit — all 34 references against the collection rule (2026-08-25)

Run with `python3 tools/audit_packs.py`, which reports the half the three gates cannot
see: **how** each pack was measured. `validate.py` checks that a pack is structurally
whole and routed; `validate_palette.py` recomputes every ratio it states. Neither can
tell you whether the values came off a rendered page or off a stylesheet, whether a
narrow width was ever measured, or whether the pack's kit was ever put in a browser.

## What was verified

**Every cited source is still reachable.** 31 of 34 packs cite an address; probed on
2026-08-25, **30 answered 200 and one answered 302** (a redirect, still resolving).
Zero link rot across the library. The remaining three carry a written exception rather
than a silent gap: `briefing-room` is anonymised **at the owner's request**, and
`instrument-console` and `workbench` name a product rather than an address — each states
so in its own `Origin:`, stays on the `core` contract and is never widened by invention.

**Six packs sit on the core contract by design**, leaving components, hero, responsive
and the signature element undecided and saying so. That is the recorded asymmetry, not a
gap.

## The queue, and it is a queue rather than a defect list

| | count | why it is not simply a bug |
|---|---|---|
| read off the render | 21 / 34 | Rule 7 — *read the render, not the stylesheet* — was only written on 2026-08-24. Thirteen packs predate it. |
| narrow width on record | 14 / 34 | A pack's `## Responsive` is answerable against a measurement; twenty state collapse rules without one on record. |
| kit render on record | 6 / 34 | Step 8 — render the kit and check its computed values — was written on 2026-08-24. Twenty-eight predate it. |
| names which stylesheets it counted | 15 / 34 | Only meaningful where the reference also loads vendor CSS. Reported, never scored. |

Re-measuring thirteen references from the render is hours per pack, not a pass. It is
recorded here so the gap is visible and prioritised rather than rediscovered.

## What this audit found and closed in the same change

**Four of the 34 kits shipped an invisible status dot.** `almanac`, `daylight`, `notation` and
`vitrine` painted it with `var(--ok-mark)` / `--warn-mark` / `--danger-mark` — tokens
none of them declares. An undefined custom property does not error; it drops to the
initial value, so the dot computed `rgba(0, 0, 0, 0)` and every gate stayed green.
Measured before the fix and after: `vitrine`'s three dots went from
`rgba(0, 0, 0, 0)` to `rgb(7, 90, 57)`, `rgb(112, 85, 0)` and `rgb(119, 35, 34)` at 6px.
All four packs state *"status is never by colour alone — a dot plus a word"*, and the dot
was half of that contract. `tools/check_kit_vars.py` now gates it in CI.

Two regex traps are recorded in that script because both were met while writing it: a
declaration is **not** line-anchored (`--a: x; --b: y;` on one line declares two, and
anchoring to `^` reported 24 false defects in `paperclip` alone), and comments must be
stripped first or a token named in prose counts as a use.

**`ADR-0001` was under-counting its own exceptions.** Its closing paragraph said *two*
packs shipped carrying their source brand as the pack name. There are **three**:
`outrank`, `babylove` and — found here — `paperclip`, whose source is `paperclip.ing`
and whose own text says *"the product is named after office supply"*. It was found by
the leak guard in `tools/site.py`, written to keep source addresses off the published
site: two of the names it refused to publish were pack names. None is being renamed —
the ADR is explicit that a pack name is a public API across four distribution channels —
but a register claiming an unbroken chain of applications while under-counting its own
exceptions makes a claim the library does not support, which is the failure that
paragraph exists to prevent.

## The table, as measured

```
pack                added       contract  render  narrow  which css  kit rendered  origin    live
-------------------------------------------------------------------------------------------------
almanac             2026-08-17  widened   —       yes     —          —             address   
atrium              2026-08-03  widened   yes     —       —          —             address   
awning              2026-08-15  core      —       —       yes        yes           address   
babylove            2026-08-21  widened   yes     —       yes        —             address   
blueprint           2026-08-09  widened   yes     —       —          —             address   
briefing-room       2026-07-29  core      —       —       —          —             recorded  
bulletin            2026-08-17  widened   —       yes     yes        —             address   
cyclorama           2026-08-08  widened   yes     yes     —          —             address   
datasheet           2026-08-12  widened   yes     —       yes        —             address   
daylight            2026-08-17  widened   yes     yes     yes        —             address   
editorial-luxury    2026-07-19  core      —       —       yes        —             address   
field-notes         2026-08-04  widened   yes     yes     —          yes           address   
instrument-console  2026-07-19  core      —       —       —          —             recorded  
ledger              2026-08-15  widened   yes     —       yes        —             address   
manpage             2026-08-12  widened   —       —       yes        —             address   
maquette            2026-08-09  widened   yes     —       —          —             address   
nameplate           2026-08-24  widened   yes     yes     yes        —             address   
notation            2026-08-17  widened   yes     yes     yes        —             address   
ora                 2026-08-14  widened   —       —       yes        yes           address   
orchard             2026-08-03  core      yes     —       —          —             address   
outrank             2026-08-21  widened   yes     —       yes        —             address   
paperclip           2026-08-14  widened   —       —       —          —             address   
patchbay            2026-08-22  widened   yes     —       —          —             address   
pigeonhole          2026-08-12  widened   yes     yes     yes        —             address   
prism               2026-08-09  widened   yes     —       —          —             address   
proscenium          2026-08-17  widened   yes     yes     yes        —             address   
rimlight            2026-08-24  widened   yes     yes     —          —             address   
roster              2026-08-13  widened   yes     yes     yes        —             address   
router              2026-08-17  widened   yes     yes     —          yes           address   
scoreboard          2026-08-12  widened   —       —       yes        yes           address   
showroom            2026-08-09  widened   yes     yes     —          —             address   
tenor               2026-08-14  widened   —       —       yes        yes           address   
vitrine             2026-08-17  widened   —       yes     —          —             address   
workbench           2026-07-20  core      —       —       —          —             recorded  

34 packs · 21 read off the render · 14 measured narrow · 6 kit renders on record · 31 addressable origins (3 recorded exceptions)
```

Reproduce: `python3 tools/audit_packs.py --check-live` (adds the network probe).
Tree at `d04f725`.
