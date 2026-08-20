# Style pack — Awning

Origin: <https://www.shopify.com>. Read 2026-08-15 from the served HTML and the
six stylesheets it links, 542 KB resolved. Unlike most sites of this size the
delivered CSS carries a **three-tier token system** — primitives
(`--color-shade-*`), semantic roles (`--color-theme-bg-cta`) and per-component
states (`--color-component-button-primary-bg-hover`) — so the names below, the
indirection between them and the four states on every control are the reference's
own vocabulary rather than a reconstruction of one.

A pure white forecourt under a single neutral ramp, where **the accent is black
and there is no hue anywhere in the control set**. What carries identity instead
is shape and weight: the button's radius is pinned to a declared full-round token,
so the pill is a statement about what a button *is*; and the type is one variable
grotesque tuned off the standard axis, with body at **420** and bold at **550** —
no 700 exists in the system. A page in this pack can be photographed in full
colour and contain no colour at all.

Contract: core — this pack does **not** specify `## Components`, `## Hero`,
`## Responsive` or `## Signature element`. Per-component states (hover, active,
disabled), the opening viewport and what it may claim, the collapse rules and the
single element the page is remembered by are **yours to decide** here — and you
say so out loud when you do, because a decision nobody recorded reads as a value
the pack forgot. Everything the pack does state is binding.

## Register

Choose this pack for a **commerce or platform front door** — the surface that
sells a system other businesses will run their own storefront, payroll,
logistics or billing on. It suits a product whose credibility comes from being
infrastructure rather than from being liked: the argument is competence, the
proof is the product on screen, and the page is long, sectioned and full of
numbers a buyer will compare.

The register underneath it is the confident utility voice — plain sentences,
concrete nouns, no adjectives doing structural work. It reads expensive by
refusing to spend anything on hue, which is also why it survives being localised
into thirty markets and co-branded with a partner's colour without breaking.

Standalone: it does **not** ride the SHELEG cinematic motion layer. Its curves are
declared and its durations are not (see Gotchas), so `MOTION_INTENSITY` above **4**
has nothing legal to buy.

**Not for:** a product whose identity IS a colour — a brand-led consumer surface,
anything sold on warmth, or a page where a hue has to do the ranking. Not for a
dense operator screen either: the shadow is real and the radius scale has four
steps, so nesting reads as softness rather than as structure, and that is
`workbench`'s half.

**Two neighbours it is genuinely confusable with.**
[`paperclip`](./paperclip.md) also refuses functional colour entirely and also
makes every control monochrome — take it when the field is **coal** and the
chromatic budget is spent on decoration that cannot be clicked. Take Awning when
the field is **white**, the budget is spent on nothing at all, and the shape of
the control is what the reader remembers.
[`showroom`](./showroom.md) also puts a product screenshot on a white gallery
wall — take it when the shot is the exhibit and the page is built to frame it.
Take Awning when the shot is one section among fifteen and the page is a
catalogue of capabilities a buyer scrolls to compare.

## Palette

Ready-made token layer: [`tokens/awning.css`](./tokens/awning.css) — copy that
file verbatim instead of transcribing this table.

**One ramp, eight steps, no hue.**

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#ffffff` | the forecourt, and the fill of most things on it | — |
| `--bg-deep` | `#f4f4f5` | the second field; a section is one or the other | 1.05:1 |
| `--ink` | `#18181b` | headings, body, every filled control | 17.72:1 |
| `--ink-soft` | `#52525b` | **prose** — the value that holds on both fields | 7.73:1 |
| `--ink-faint` | `#71717a` | meta and non-text marks — **not prose**, see Gotcha 1 | 4.83:1 |
| `--line` | `#e4e4e7` | between rows | 1.27:1 |
| `--line-strong` | `#d4d4d8` | a decorative edge | 1.48:1 |
| `--control-border` | `#71717a` | **derived** — the boundary of a pressable control | 4.83:1 |
| `--accent` | `#000000` | every primary action | 21.00:1 |
| `--accent-ink` | `#ffffff` | text ON the accent | — |
| `--good` | `#0b6b3a` | **derived** — success on a product surface | 6.61:1 |
| `--warn` | `#8a5300` | **derived** — attention | 6.33:1 |
| `--danger` | `#b3261e` | **derived** — failure and prohibition | 6.54:1 |

**The accent is black, and it is a resolved chain rather than a stylistic
absence.** `--color-component-button-primary-bg` → `--color-theme-bg-cta` →
`#000`, with hover `#3f3f46`, active `#71717a` and disabled `#d4d4d8` declared
beside it. Three consequences follow and they are the pack. First, **hue is
available for content and nothing else** — a partner logo, a product screenshot,
an illustration may be as colourful as they like, because the chrome around them
has ceded the whole budget. Second, **ranking is by value and by shape**, which is
why the radius scale below matters more here than in any other pack in this
library. Third, the page needs no dark theme to look considered, and adding one
is a separate design rather than an inversion.

**The one tint the system keeps is a wash and may not carry anything.**
`--wash-mint` `#c1fbd4` is the sole survivor of a green ramp otherwise absent from
the delivered CSS. At 1.17:1 on the field it is a section background and nothing
else — never a mark, never a border, never a word.

**Severity is derived, and status is never by colour alone.** The reference paints
no success, warning or error anywhere in its theme layer, because a front door has
no state to report. The three above are the smallest set that clears AA on *both*
fields — the floor `--ink-faint` misses. They are also a red and a green, which
collapse toward each other under deuteranopia at a measured separation of 5.2
against this library's floor of 8.0, and no choice of warn repairs that pair. So
the rule is not negotiable here: **every state carries its word**, and the colour
is the second encoding rather than the first.

## Type

One variable grotesque, used as a variable font, plus a display face the reference
declares and spends sparingly.

| Face | Where | Weight |
|---|---|---|
| Inter-Variable (`--sans`) | every sentence and every control | **420** body, **550** bold |
| NeueHaasGrotesk (`--display`) | the display line, where it is used at all | 400 |
| system mono (`--mono`) | code and figures | 400 |

**Nothing is 700, and that is the signature.** The system declares
`--font-weight-body: 420` and `--font-weight-bold: 550`. Both are off the
standard axis, both are reachable only because the face is variable, and the
result is a page that reads substantial without reading heavy. Setting a heading
in 700 here is not a small deviation — it is the one number the system was built
to avoid.

**Tracking runs both ways within one family, and the axis is size rather than
face.** The display ramp tracks negative and the body ramp tracks positive:
`-0.01em` at 3.5rem, `-0.005em` at 2.75rem, zero through the middle, then
`+0.015em` across body and `+0.04em` at 0.875rem. This is the opposite
arrangement to a pack that splits tracking across two faces — here one face does
both, and the crossover sits at about 1.375rem.

**Leading is declared in `rem`, not as a ratio.** `3.78rem` on `3.5rem`, `2.97rem`
on `2.75rem`, `1.3rem` on `1rem`. The display therefore sits at **1.08**, which is
tight for a grotesque at that size, and the ratio *changes* down the ramp rather
than holding — 1.08 at display, 1.12 at t2, 1.30 at t7. Copy the pairs rather than
a single ratio; a system that ships size and leading as one token cannot drift
apart, which is the point of writing them this way.

**The ramp is fixed, not fluid.** Nine title steps (`dsp`, `t1`–`t8`) and six body
steps (`b1`–`b6`), all in `rem`, with breakpoints doing the collapsing. There is
no `clamp()` anywhere in the type layer.

## Texture & surface

**Radius is a four-step scale, and the button is pinned outside it.**
`0.375rem` / `0.5` / `0.75` / `1rem` for surfaces, and
`--radius-button: var(--radius-full)` — the pill. Keep the indirection when you
copy this: writing `9999px` on the button flattens the only place the system says
*why* a button is that shape.

**One shadow, three layers**, and it ships as `--shadow-1`.
`0 8px 48px #06060814` is the ambient,
`0 4px 8px #18181b0a` is the contact, and `0 0 2px #18181b40` is a hairline edge
that keeps a card's boundary legible on pure white where the ambient alone
dissolves it. That third layer is the part people drop when they copy a shadow by
eye, and dropping it is why a copied card floats without sitting. There is no
second shadow and no elevation scale.

**Two border weights**, which is unusual in this library: `--line` between rows,
`--line-strong` around a control. A control's border is heavier than a table's
rule, and that difference is what makes an outlined secondary button read as a
control at all when its fill is transparent.

**Spacing doubles, then jumps.** `0.25 / 0.5 / 1 / 1.5 / 2 / 2.5rem` for
component-scale work, then `4 / 5 / 8rem` for section rhythm. Nothing sits between
2.5 and 4: the system has component space and page space and refuses the middle.

## Motion tokens

| Token | Value | Where |
|---|---|---|
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | anything entering or changing state |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | anything moving on screen |
| `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | **declared and banned in UI** — see Gotchas |
| `--dur-hover` | `150ms` | **derived** — fills and borders |
| `--dur-control` | `200ms` | **derived** — dropdowns and selects |
| `--dur-panel` | `300ms` | **derived** — modals and sheets |
| `--dur-reveal` | `450ms` | **derived** — entrance, and only on a page |

The three curves are the reference's. **The four durations are not** — the
reference names zero durations and writes ten distinct inline values from `.1s` to
`.45s`, so there is no duration rule to extract and `MOTION_DOCTRINE.md` §3 fills
the gap. Reduced motion collapses all four to zero and leaves the curves
declared, because a curve with no duration costs nothing and a missing token
costs a dropped declaration.

## Signature motifs

1. **The black pill** — a fully-round primary action on a white field, its radius
   inherited from a token that says *button*, not from a number.
2. **The colourless chrome** — a full-colour screenshot of the product sitting in
   a frame that contains no hue at all, so every colour on the page belongs to the
   thing being sold.
3. **550, never 700** — a variable face carrying emphasis at a weight the standard
   axis does not offer.
4. **The three-layer shadow** — ambient, contact and a hairline edge, on white,
   where the edge is what stops the card dissolving.
5. **Two rules of different weight** — the row rule and the control border, and
   the fact that they differ is what makes an outlined control legible.
6. **Tracking that crosses zero inside one family** — negative on the display,
   positive on the body, with the crossover around 1.375rem.

## Micro-interactions

- **A primary control changes two properties, not one.** The fill goes
  `#000` → `--accent-hover` `#3f3f46`, and the label goes white → `--accent-ink-hover`
  `#d4d4d8` (14.21:1 on the fill). Moving only the fill reads as a lightening;
  moving both reads as a press.
- **A secondary control is transparent and borrowed.** Its fill is `transparent`
  at rest, hover, active and disabled alike — every state is carried by the
  border and the label, which is why `--line-strong` exists.
- **Disabled is a value, not an opacity.** `--accent-disabled` `#d4d4d8` fill with
  `--accent-ink-disabled` `#71717a` content. Nothing in this system fades; a
  disabled control is drawn in the pale end of the same ramp, so it keeps its
  edges and stays measurable.
- **Focus is not specified by the reference at the token layer**, and this pack
  does not invent one beyond the obvious: a 2px `--ink` ring at 2px offset. With
  no accent hue there is nothing else it could be, and that is worth stating
  rather than leaving to the reader.

## Bans

- **No accent hue.** Not on a button, a link, a tab, a badge or a focus ring. The
  moment chrome takes a colour, the screenshot inside it stops being the only
  colourful thing on the page and the register is gone.
- **No weight of 700.** Body is 420 and bold is 550; a variable face is loaded
  precisely so those exist.
- **No second shadow, and no elevation scale.** One three-layer shadow, or a
  border.
- **No `clamp()` in the type layer.** The ramp is fixed and the breakpoints do the
  work; a fluid step would drift out of its declared leading, which is shipped as
  a paired `rem` value for exactly that reason.
- **No `--wash-mint` on anything but a section background.** At 1.17:1 it cannot
  carry a mark, a border or a word.
- **No `ease-in` on anything a reader triggers.** The reference declares it;
  `MOTION_DOCTRINE.md` §2 bans it in UI and this pack keeps that ban.
- **No dark theme by inversion.** There is no second ramp in the reference and
  inverting a white forecourt produces a different product, not a night mode. A
  dark surface here is a new design and should be measured as one.

## Gotchas

Eight traps, measured on 2026-08-15 and 2026-08-16. Five are defects in the
reference, which is why a copy inherits them — and **two of those five were
found only by rendering a page in this pack**, not by reading its token layer.

1. **`--ink-faint` does not clear AA on the system's own second field.** At
   `#71717a` it is **4.83:1** on `#ffffff` and **4.40:1** on `#f4f4f5`, and the
   reference spends it on meta lines that appear on both. It is short by a margin
   nobody notices and every audit finds. Reserve it for non-text marks and large
   text; **prose takes `--ink-soft`** at 7.73:1 and 7.03:1. The same shape has now
   been found in two independently-extracted packs in this library, which suggests
   it is a property of how design systems get built rather than a mistake one team
   made.
2. **The curves are tokens and the durations are not.** Three eases are declared
   as custom properties; every duration is written inline, and there are **ten
   distinct values** between `.1s` and `.45s` — `.1`, `.12`, `.15`, `.2`, `.25`,
   `.3`, `.33`, `.35`, `.4`, `.45`. A system that names its curves and not its
   durations cannot hold a duration rule, and nothing in it can tell you whether
   `.33s` was a decision or a typo for `.3s`. The four `--dur-*` tokens in this
   pack are derived from the doctrine, not measured.
3. **`ease-in` is declared and is banned in UI.** It starts slow, and the delay
   lands in the exact moment after a click when the reader is watching hardest.
   The reference ships it as a token, which makes reaching for it easy; keep it
   for something leaving the screen entirely, and prefer `ease-in-out` even then.
4. **A secondary control's border misses the floor for a control boundary.**
   `--line-strong` `#d4d4d8` is **1.48:1** on white, and WCAG's floor for a UI
   component boundary is **3:1** — so it fails by half. This matters more here
   than it would in most packs, because a secondary button in this system is
   `transparent` at rest, hover, active *and* disabled: the border is not
   decoration around the control, it **is** the control. `--shade-40` does not
   reach the floor either (2.56:1). `--control-border` `#71717a` is the first
   step on the ramp that clears it, at 4.83:1. Found by rendering a page in the
   pack and looking at a "Talk to sales" button beside a black pill, where it
   nearly disappeared — not by reading the token layer, which is why it survived
   the first release.
5. **The second field exists and a page built from this pack will not use it.**
   `--bg-deep` is declared, and the first page rendered in this pack ran fifteen
   sections on pure white without touching it — because nothing in the token
   layer forces the alternation and white is the default of everything. A front
   door in this register is long and sectioned, and a long page on one field
   reads as one endless scroll. **Alternate the field by section**, and use the
   change to mark where the argument changes, not decoratively.
6. **The shade ramp is Tailwind's `zinc`, renamed.** `#f4f4f5`, `#e4e4e7`,
   `#d4d4d8`, `#a1a1aa`, `#71717a`, `#52525b`, `#3f3f46`, `#18181b` are that
   palette exactly. This is not a criticism — a bought ramp used deliberately,
   with semantic roles layered over it, is a different thing from a bought theme
   used by default. But it matters when someone asks whether the greys are
   "yours": they are chosen, not authored, and a second product on the same ramp
   will look related whether or not you meant it.
7. **The token layer is three tiers deep and a copy usually flattens it.**
   `--color-component-button-primary-bg` → `--color-theme-bg-cta` → `#000` is
   three lookups to reach one colour, and it is worth every one of them: the theme
   tier is where a co-brand or a locale swaps in. Flatten the chain when copying
   and the system still renders, having lost the only seam it was built around.
8. **The delivered CSS is 542 KB and most of it is a utility bundle.** Counting
   `border-radius` across the whole payload returns nineteen values and counting
   transitions returns twenty-five, which reads as sprawl. It is not: the *system*
   is `--radius-*` (four values plus full), one shadow and three weights, and the
   rest is Tailwind's utilities shipped alongside. Measure the token layer, not
   the bundle — the first draft of this pack drew the opposite conclusion from the
   bundle and was wrong.
