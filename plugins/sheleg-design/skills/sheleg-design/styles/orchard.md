# Style pack — Orchard

Origin: **gutgutgoose.com** (2026), a production consumer-biotech site built in
Framer. Every value below was read off its live computed styles. A warm oat
field carrying a stack of **rounded slabs**, a sage-green brand, one candy
orange reserved entirely for the action, a rounded geometric display face, and
buttons made of light rather than of shadow. It reads the way good packaging
does: friendly enough to pick up, precise enough to trust.

Contract: core — this pack does **not** specify `## Components`, `## Hero`,
`## Responsive` or `## Signature element`. Per-component states (hover,
active, disabled), the opening viewport and its line ceiling, the collapse
rules, and the single element the page is remembered by are **yours to
decide** here, and you must say so out loud when you do. Everything the pack
*does* state is measured; the precision of that half is not evidence about
this half. The backfill is held rather than written from the token layer,
because filling these sections from tokens would be inventing values with a
citation attached — which is the one thing this pack layer exists to prevent.

## Register

Choose this pack for **approachable consumer biotech and DTC wellness**:
testing kits, supplements and personalized formulations, subscription health,
early-stage consumer science that has to feel warm and credible at the same
time. It suits a product whose buyer is being asked to trust a lab result *and*
a brand voice — where a clinical-white surface would kill the conversion and a
lifestyle-brand surface would kill the credibility.

Set against the skill's other warm pack: **`atrium` is premium and restrained**
(one continuous field, a light serif, terracotta, editorial pacing);
**`orchard` is friendly and modular** (every section is a card, a rounded
geometric sans, sage and orange, packaging pacing). If the product is sold on
prestige, use `atrium`. If it is sold on *this is for you and it is not
frightening*, use this one.

A third warm pack now sits in the same thumbnail and the separation is
mechanical rather than tonal: [`bulletin`](./bulletin.md) draws every object
with a 1px outline over a hard zero-blur offset, so its surfaces are separated
by a **line**. Here they are separated by a **gap** — a slab is inset from the
field and carries no border at all. If the brief wants edges, it wants that pack.

It **rides the SHELEG cinematic layer at one point only**: the hero headline is
scrubbed to the scroll clock, word by word. Below the fold, motion is a sticky
visual column beside scrolling copy and nothing else. Do not add a particle
field to this pack — the register is tactile, not atmospheric.

The defining constraint is composition: **the page is a stack of rounded slabs,
not a continuous surface**. Rhythm comes from alternating slab fills (oat,
sage, cacao) with a `55px` gap between them, and every slab is inset from the
field so the field is always visible around it.

**The fork against [`pigeonhole`](./pigeonhole.md).** Both are friendly, both are
tinted, both round generously. This pack works on **warm oat slabs** with soft-3D
pills and its tint is decoration in service of approachability; that one works on
**white** with hairlines and its tint carries meaning — nine hues, each bound to a
category, each label word mandatory. A warm field says *this is pleasant*; a white
field with nine labelled hues says *this is sorted*.

**The fork against [`paperclip`](./paperclip.md)** is warmth against neutrality.
Both round generously — this pack's soft-3D pills and that pack's capsules are
the same instinct — and both put colour where the reader looks first. The
difference is the field underneath and who colour is *for*. Warm oat with tinted
slabs invites a consumer to touch something; neutral coal with one loud
ornament on it tells an operator the interface will stay out of the way. A
friendly register belongs here; a page that must look like it will not spend
your money belongs there.

## Palette

Ready-made token layer: [`tokens/orchard.css`](./tokens/orchard.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#FFFEF4` | the field the slabs sit on |
| `--surface` / `-2` | `#F6ECDC` / `#FBF7EA` | oat slab & card / the lighter floating pill |
| `--surface-ink` | `#3A1B13` | the cacao slab — inverted sections, selected chips |
| `--line` | `#E3D7C8` | hairline on oat |
| `--ink` | `#3A1B13` | cacao, not black — 15.4:1 on `--bg`, 13.3:1 on oat |
| `--ink-soft` | `rgba(58,27,19,.6)` | 4.1:1 on oat — captions only, **not** body |
| `--primary` | `#78934A` | sage — the brand. A **fill**, 3.4:1 |
| `--primary-deep` | `#61783B` | the text-safe green — 4.9:1 under `--on-primary` |
| `--primary-light` / `-tint` | `#AACA73` / `sage 10%` | the mark & illustration / quiet wash |
| `--cta` | `#FA7241` | candy orange — the ONE action colour, a fill, 2.8:1 |
| `--cta-ink` | `#3A1B13` | the label **on** the CTA — white here fails AA |

Two rules carry this palette, and the reference breaks both — which is exactly
why they are written down:

- **Sage and orange are fills, never text.** `--primary` is 3.4:1 on the field
  (large text and UI marks only) and `--cta` is 2.8:1 (nothing, ever). Body
  copy on a sage slab must sit on `--primary-deep`, and the CTA label must be
  `--cta-ink`.
- **The ink is brown.** `#3A1B13` is the black of this system; a true `#000` or
  a cool `#18181B` beside it reads instantly as a component from another kit.
  Framer/Tailwind defaults leaking into this palette is the most common way it
  degrades.

Three colours and nothing else: oat is the paper, sage is the brand, orange is
the verb. A fourth hue means one of them stopped meaning something.

## Type

Two families, each with a single weight in practice:

- **Display — a rounded geometric sans at Medium (500)**, tracked `-0.023em` at
  28px and above and `normal` below. The roundness *is* the friendliness; a
  grotesque here turns the whole page corporate. The reference uses Pogonia;
  substitutes with the same voice: Poppins, Gilroy, Objektiv Mk1, Nunito Sans
  at 600.
- **Body — Figtree at 400** (500 for emphasis). Nothing bolder: the display
  face carries hierarchy, so body weight never has to.

Scale, fixed px (this pack does **not** fluidly scale its type — it changes the
slab layout at breakpoints instead):

| Token | px / line-height | Used for |
|---|---|---|
| `--t-hero` | 46 / 1.245 | the scrubbed hero claim |
| `--t-h1` | 44 / 1.2 | every section heading |
| `--t-h2` / `-h3` | 32 / 28 · 1.2 | slab headings, sub-claims |
| `--t-h4` / `-h5` / `-h6` | 24 / 22 / 20 · 1.2 | card titles, list heads |
| `--t-price` | 34 | the price — set in the **body** face, not the display face |
| `--t-lg` / `--t-body` / `--t-sm` | 18 / 16 / 14 | lede · body · captions |

Line height is flat `1.2` across every display size, `1.3` on 16–18px body and
`1.5` at 14px and below. The price being set in the body face is deliberate and
worth keeping: a rounded display numeral reads as *branding*, and a price needs
to read as a fact.

## Texture & surface

- **Elevation is light, not shadow.** The signature material is two inset white
  hairlines — `inset 0 1px 0 rgba(255,255,255,.8)` on top and
  `inset 0 -1px 0 rgba(255,255,255,.35)` on the bottom — which make a flat fill
  read as a soft extruded pill. The only real drop shadow in the system is
  `0 9px 14px rgba(250,114,65,.25)`: an ambient glow **in the button's own
  hue**, not a grey shadow. Cards carry `0 1.4px 1.4px rgba(0,0,0,.02)`, which
  is almost nothing and should stay that way.
- **Nothing has a sharp corner.** `12px` is the default (cards, panels, most
  slabs), `20px` for media cards and chips, `24px` for a full-bleed section
  slab, `6px` for small marks, and a pill radius on every control.
- Spacing is an 8-based ramp with two named rhythms doing almost all the work:
  **`64px 24px` slab padding**, **`44px` between blocks inside a section**, and
  **`55px` between full-bleed slabs**. Cards take `36px`. Learn those four
  numbers and the layout builds itself.
- The field shows around the top slab as an `8px` inset — a small detail that
  makes the whole page read as content *placed on* a surface rather than
  printed into it. Keep it.
- Imagery is photography inside `20px` wells and flat vector illustration in
  `--primary-light`. No gradients as decoration: the only gradient in the
  system is the CTA's own radial sheen.

## Motion tokens

- `--dur-quick .15s` · `--dur-base .25s` · `--dur-slow .4s` on
  `cubic-bezier(0.4, 0, 0.2, 1)`. Buttons transition `background, box-shadow` —
  scoped, not `all`.
- **The one scrubbed instrument is the hero headline**: each word is its own
  span whose opacity is driven from the scroll clock, roughly one word per 12%
  of the hero's scroll range, from `0.001` to `1`. Opacity only — nothing
  translates, nothing scales, no blur. It is the pack's entire cinematic
  budget.
- The second scroll behaviour is a **sticky visual column** (a `24px`-radius
  panel pinned at `top: 0`) beside a scrolling explanation. Sticky, not
  scrubbed: the panel does not animate, it simply stays.
- `prefers-reduced-motion` resolves the headline to fully opaque immediately
  and releases the sticky column to normal flow. The reference ships **no**
  reduced-motion branch at all — see Gotchas; this pack requires one.

## Signature motifs

- **The candy pill.** A two-layer button: a flat `--cta` fill under a radial
  sheen, wearing `--shadow-cta` (both inset white hairlines plus the orange
  ambient glow) at pill radius, `16px 24px 14px` padding — the extra top pad is
  what makes the label sit optically centred. Exactly one of these per view.
  It is the only orange object on the page, which is what makes it unmissable
  without being loud.
- **Slabs as sections.** Each section is a rounded rectangle with its own fill:
  oat for explanation, sage for invitation, cacao for emphasis. Adjacent slabs
  never repeat a fill; the field between them is the separator.
- **The word-by-word headline.** The hero claim resolves as you scroll, one
  word at a time, which turns a long sentence into a paced read instead of a
  wall. It only works on a claim short enough to finish inside the hero — write
  the sentence to the mechanism, not the mechanism to the sentence.
- **Chips as a filter rail.** Symptom/topic chips at `20px` radius, `8px 16px`
  padding, `11px` gaps, selected state filled `--surface-ink` with `--on-ink`.
  They double as navigation and as a plain-language list of what the product is
  for.
- **The claim/evidence pair.** Every marketing assertion is followed by a
  quieter citation line in `--ink-soft` naming the study or source. On a health
  page this is not decoration — it is the reason the page is allowed to make
  the claim at all.
- **Objection sections written as objections.** Headings that state the reader's
  suspicion in their own words rather than the brand's benefit. The layout
  device is a plain stack of oat slabs; the craft is in the copy, and the pack
  should not decorate it.
- **The glass nav pill.** A `--surface-2` pill at `50px` radius with
  `backdrop-filter: blur(20px)`, sticky at `top: 0`, floating over whatever
  slab is passing beneath it.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack with this pack: keep the scroll clock, use
the Reveal set at ≤`--dur-slow`, and let the *only* scrubbed consumer be the
headline. A particle field is the wrong instrument here — if the page needs an
ambient layer, use a slow parallax on the illustration inside one slab and
nothing more. Anything generative stays in `--primary-light` on `--surface`;
the orange never moves, because the moment it moves it stops reading as the
button.

## Micro-interactions

- Buttons transition `background, box-shadow` over `--dur-base`; hover deepens
  the fill (`--primary` → `--primary-deep`) and the CTA's ambient glow grows.
  Nothing scales — a soft-3D pill that also grows reads as a toy.
- Chips toggle fill and ink; the selected chip is the cacao one, and there is
  always exactly one selected.
- Focus-visible is a `2px` `--ink` ring at `2px` offset, pill-shaped like its
  target. On the orange CTA the ring is `--ink`, not white.
- The nav pill is sticky and never changes size on scroll; its `blur(20px)` is
  the only thing separating it from the slab underneath.
- Accordions and disclosure rows animate height over `--dur-base` and nothing
  else; the row does not lift, tint, or shift.

## Bans

- **A status palette this pack does not have.** `orchard` ships **no**
  `--good` / `--warn` / `--danger` / `--info` at all: its colour vocabulary is
  the sage brand and the one candy-orange action, and *"a fourth hue means one
  of them stopped meaning something"* (below) is why. If a screen needs status,
  that is a **gap to close in this pack, deliberately** — not four hues invented
  at the keyboard. Until then, carry state with a word, an icon or a border, and **never by colour
  alone**.
  *(Corrected 2026-08-10: this bullet was copy-pasted into six of the twelve and told
  the reader that "several of these pairs sit inside a dichromat's confusion
  line", a measurement that needs at least two status colours to exist.)*
- Orange or sage as **text**; white text on the orange CTA; white text on
  `--primary` at body size (use `--primary-deep`).
- A true black, a cool grey, or any Framer/Tailwind default neutral
  (`#18181B`, `#1A1A1A`, `#F2F3F4`) beside the warm palette.
- A fourth hue; a second orange object in the same view; the CTA colour used
  for a non-action (a badge, a chart series, a heading).
- Sharp corners anywhere; a grotesque or a serif as the display face; a bold
  (700+) body weight.
- `transition: all`; hover states that scale or lift; a drop shadow in grey
  where the bevel belongs.
- Two adjacent slabs with the same fill; a section that bleeds edge-to-edge
  without the field showing around it.
- A claim without its citation line; a benefit heading where the reference
  would have written the reader's objection.

## Gotchas

The reference is strong on composition and weak on contrast. All three failures
below are real, measured, and fixable from inside the palette — treat them as
the first thing to correct when porting this look:

- **The CTA label fails AA.** White on `#FA7241` is **2.8:1**. Use `--cta-ink`
  (`#3A1B13` on orange = **5.6:1**). Darkening the orange to reach 4.5:1 with
  white would take it to roughly `#C4491A` and cost the candy quality — the ink
  label is the better trade.
- **Body copy on the sage slab fails AA.** `--on-primary` on `--primary` is
  **3.4:1** (and oat on sage is **2.96:1**, below even the large-text floor).
  A 44px display heading is fine; 14–18px copy is not. Put small text on
  `--primary-deep` (**4.9:1**) or on an oat card inside the sage slab.
- **`--ink-soft` is 4.1:1 on oat**, under AA. It is a caption and citation
  colour. Long-form secondary copy takes full `--ink`.
- **The reference ships no `prefers-reduced-motion` rule anywhere**, so the
  scrubbed headline runs for everyone. Ship the branch in the same commit as
  the reveal: at reduced motion the words start at full opacity and the sticky
  column is released.
- **A scroll-scrubbed headline is a legibility hazard on short viewports.** If
  the hero is shorter than the scroll range the reveal needs, the last words
  never resolve. Cap the sentence length, and give the effect a floor so the
  headline is fully readable by the time the hero leaves the viewport.
- **The soft-3D bevel is invisible on dark fills.** `rgba(255,255,255,.8)`
  inset reads as a highlight on orange and sage but as a scratch on the cacao
  slab. Buttons on `--surface-ink` take a flat fill, no bevel.
- Substituting the display face changes this pack more than substituting a
  colour: the rounded terminals are the entire personality. If no rounded
  geometric with a real Medium is available, prefer a different pack.
