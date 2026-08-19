# Style pack — Maquette

Origin: <https://zilliz.com/> (2026), the marketing site of an enterprise vector
lakebase. Every value below was read off its live computed styles on 2026-08-09,
and every ratio was computed by importing this repository's own palette gate. A
near-black table, cream ink that is the same cream the models are built from, one
pale aqua that works as text, mono block labels, and a single offset shadow that
puts every object under one raking light.

The identity in one sentence: **a built object on a dark table.** The subject is
not a screenshot and not a diagram-as-decoration — it is an axonometric model of
the system, labelled block by block, that the reader is meant to take apart with
their eyes before they evaluate what it costs.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **enterprise data infrastructure sold to an architecture
buyer**: lakebases, warehouses, serving layers, platforms whose pitch is a
separation of concerns. It suits a product whose argument is *here is how this is
put together* — where the reader must hold a structure in their head before any
number about it means anything.

It rides the SHELEG cinematic layer at a restrained setting. The model is a
drawing and drawings do not perform; the motion budget goes to section entry and
to controls.

**Not for:** a product with a value that changes while you watch — that is
`instrument-console`, and the fork is below. The open-source project the platform
is built on — `prism`, and in the real world these two are frequently the same
company's two faces. A page whose centre is a product screenshot — `showroom`.

### The fork against [`instrument-console`](./instrument-console.md), which is the one people get wrong

Both are near-black with one pale accent, mono labels and an
enterprise-infrastructure buyer. On surface signals they are nearly identical,
and on product *category* they overlap completely. The test is not the category
— it is what the page has to render.

**Does the page have to show a number that changes while the reader watches?**

Yes — a dial, a stream, request rates, an error budget, saturation → 
`instrument-console`. Its single electric signal, its scrubbed telemetry and its
progress rail exist to make a moving value readable.

No, but the reader must decompose a system before they can judge it → 
`maquette`. Nothing on this page moves on its own; the model is static because a
measurable object has to hold still.

**A cockpit answers *what is happening now*; a maquette answers *what is this
made of*.** This fork was tested before the pack shipped: two agents in separate
fresh contexts, one given an architecture brief and one a live-telemetry brief,
each chose correctly and each derived this test unprompted.

### Against [`blueprint`](./blueprint.md)

Both were extracted from vector-database companies, so category matching sends
briefs to either with equal force. The split is **structural versus
quantitative**: this pack's centre is one complete labelled model, and it bans a
second drawing on the page; `blueprint` gives figures, ruled data cells and mono
columns for arguments made in numbers. A page whose hook is a separation of
concerns lands here. A page with two numeric arguments and an architecture
section is a sheet of figures, and that is `blueprint`.

### Against [`prism`](./prism.md)

The same company will often have both. `prism` is the light project page and its
centre is a **command** you can run in thirty seconds. `maquette` is the dark
product page and its centre is a **model** you have to study. If the next action
is `pip install`, that pack; if the next action is a demo call, this one.

## Palette

Ready-made token layer: [`tokens/maquette.css`](./tokens/maquette.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#151515` | the table | — |
| `--surface` / `--surface-2` / `--surface-sunken` | `#1B1B1B` / `#1D1D1D` / `#131313` | panel · raised panel · a well cut into the table | ink 16.5–17.8:1 |
| `--ink` | `#FFF9F4` | **cream, not white** | **17.49:1** |
| `--ink-soft` | `#B3B5C1` | secondary copy | **8.95:1** |
| `--ink-faint` | `#8A8F98` | captions, leader lines | 5.62:1 |
| `--line` / `--line-strong` | `#2B2B2B` / `#3A3A3A` | the hairline · emphasis | — |
| `--accent` | `#97FDFF` | pale aqua — **works as text** | **15.49:1** |
| `--on-accent` | `#000000` | the label on an aqua fill | **17.81:1** |
| `--model-top` / `--model-face` / `--model-side` | `#FFF9F4` / `#FFF3D6` / `#E8DDC8` | the three faces of one cream solid | 17.5 / 16.6 / 13.6 :1 |
| `--leader` | `#8A8F98` | the dotted line from a block to its label | — |
| `--good` / `--warning` / `--danger` | `#3FCF7F` / `#FFB020` / `#FF5C5C` | status — **a pack decision, see below** | — |

Four rules carry this palette.

- **The ink is cream, and this is the pack's least obvious rule.** `#FFF9F4` is
  the same cream the model is built from, so type and object read as one material
  under one lamp. Substitute `#FFFFFF` — which every framework default will do
  for you — and the page splits into a warm object sitting on a cold document.
- **The accent works as text**, at 15.49:1, which is unusual in this library:
  most packs here have a fill-only accent. The aqua may set a display word, a
  link or a label with no second token. Under it, **black** at 17.81:1 — never
  the cream, which falls to 1.1:1 and vanishes.
- **The three model faces are flat fills, not shading.** An axonometric drawing
  has no light model; the relationship between `--model-top`, `--model-face` and
  `--model-side` *is* the lighting. Do not add a gradient to a face.
- **Status is never by colour alone.** These four are **derived for this pack,
  not extracted** — the reference exposes no status palette at all, and the token
  layer says so at the declaration. They are separated as far as the hue wheel
  allows, and `--good` and `--danger` still sit 6.4 apart under deuteranopia,
  because green and red are the one pair no hex separates for a deuteranope.
  Every status therefore carries its word.

## Type

Two families, split strictly by what is speaking.

- **Geist, 700 / 400** for the argument: display, headings, lede, prose.
- **Geist Mono, 400** for anything the *model* says: block labels, leader
  captions, dimensions, CLI lines, table cells.

That split is the pack's typographic rule, and it is easy to state and easy to
break: **prose is the grotesque, and the drawing speaks in mono.** A block label
set in Geist stops reading as part of the object.

Both faces are SIL OFL, so there is no substitution trap here.

| Token | Size / line-height | Tracking | Weight |
|---|---|---|---|
| `--t-display` | 66 / 1.06 | −0.02em | 700 |
| `--t-h2` / `--t-h3` | 40 / 1.2 · 28 / 1.25 | −0.02em | 700 |
| `--t-lede` | 22 / 1.273 | 0 | 400 |
| `--t-body` / `--t-sm` | 16 / 1.6 · 14 / 1.5 | 0 | 400 |
| `--t-label` | 13 / 1.4 — **Geist Mono** | 0.02em | 400 |

## Texture & surface

- **One shadow direction, two sizes, and the direction is not adjustable.**
  `--shadow-block-sm` is the same cast at half the offsets, for a small block; a
  model never mixes the two on one plane. `--shadow-block` is
  `12px 24px 24px rgba(0,0,0,.25)` — displaced on **both** axes, which is what
  makes a block sit on the table under a raking light instead of floating above a
  page. Every block in a model is lit from the same upper-left source. Change the
  offsets on one and the model comes apart; change the direction and it stops
  reading as one scene.
- **The model's outline is the field colour.** `--model-line` is `#151515` — the
  table itself — so the cream solids are separated by the dark showing between
  them rather than by a drawn stroke. This is why the model reads as cut paper
  rather than as an SVG.
- **Radii `6 / 8 / 12 / 20`, and every action is a `36px` pill.** The mix is
  deliberate: panels are rectangles with a small radius, actions are pills, and
  nothing in between.
- **Surfaces are a tight family.** `#1B1B1B`, `#1D1D1D` and `#131313` are within
  a few percent of the field; the page is nearly one value, and the model is the
  only bright thing on it. Widening that family is how the page turns into a
  generic dark SaaS site.
- Spacing is a 4px ramp; the page column is 80rem.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary CTA** | `--accent` fill, `--on-accent` label, `--radius-pill`, `8px 18px`, 13px Geist | fill → `--accent-deep` over `--dur-fast` | `translateY(1px)` | `opacity: .45`, `cursor: not-allowed` |
| **Secondary CTA** | `--surface-2` fill, `--ink` label, `--radius-pill`, `6px 18px` | fill → `--surface` | as above | as above |
| **Model block** | a cream solid: `--model-top`, `--model-face`, `--model-side`, separated by `--model-line`, `--shadow-block` | none — it is a drawing | — | — |
| **Leader label** | mono `--t-label` in `--ink`, on `--model-top` fill, `--radius-sm`, `4px 10px`, with a 1px dotted `--leader` running to its block | none | — | — |
| **Panel** | `--surface`, `1px --line`, `--radius`, 20px padding | border → `--line-strong` | — | — |
| **CLI line** | `--surface-sunken`, `1px --line`, `--radius`, `12px 16px`, mono 14px, a label in `--ink-soft` then the command in `--ink` | copy button tints | copied: the **label changes**, not only a colour | — |
| **Status mark** | an 8px dot in its status colour **with its word beside it**, mono `--t-label` | none | — | — |
| **Nav item** | Geist 15px, `--ink-soft` | colour → `--ink` | colour → `--accent` | — |
| **Input** | `--surface-sunken`, `1px --line-strong`, `--radius`, `10px 14px`, **16px** | border → `--ink-faint` | focus: `--accent` border plus a 3px aqua halo at 20% | `opacity: .5` |
| **Agent prompt** | `--surface` fill, `--radius-xl`, a mono caret that blinks, a submit key at the right | border → `--line-strong` | — | — |
| **Loader** | **pack decision:** a skeleton in `--surface-2` with the geometry of the block it replaces, no shimmer | — | — | — |
| **Empty state** | **pack decision:** one `--ink` line, one `--ink-soft` line, one pill. No illustration — the model is the only drawing this pack allows | — | — | — |

## Hero

- **Height** `--hero-min-h: 100dvh`. Never `100vh`.
- **Two columns: the argument left, the model right.** The display headline with
  **one phrase in `--accent`**, a four-line lede in `--ink-soft`, two pills, then
  the CLI line beneath them. The model occupies the right half at roughly 45% of
  the viewport width.
- **Line ceiling: three**, at 66px and 1.06 leading. The model needs the vertical
  room and a fourth line takes it.
- **The model is in the first viewport, complete.** Not a teaser, not a crop, not
  a "scroll to reveal". The whole argument of this pack is that the reader can
  see the structure immediately — a model that has to be assembled by scrolling
  is a story, and stories belong to the cinematic packs.
- **Every block in the model is labelled.** An unlabelled axonometric is
  decoration; the labels are what make it an argument. If a block has no name you
  can defend, remove the block.
- The first viewport does not carry a logo wall, a metric row or a screenshot.

## Responsive

- **The two columns stack, and the model goes first.** Below 1024px the model
  moves *above* the headline rather than below it — the object is the hook, and
  putting it after four lines of lede buries it.
- **Type steps at breakpoints:** the display drops 66 → 44 → 34.
- **The model scales, and its labels do not.** Mono block labels stay at 13px at
  every width; scaling them with the drawing makes them illegible at exactly the
  size where the drawing is hardest to read. Below 640px, labels move outside the
  model's bounding box with longer leaders.
- **The offset shadow shortens** below 768px (12px 24px → 6px 12px), because a
  24px displacement on a 320px-wide drawing reads as a printing error.
- Full-height sections use `dvh`; bare `100vh` is banned.

- **Container queries.** The **CLI line** and the **agent prompt** wrap by their own
  width, so they answer to their container. The **model block's** drop-shadow is
  **SELF**: the shadow is a property of the block that would establish the container,
  and a container cannot query itself — so that one breakpoint stays a viewport query,
  by limitation rather than by preference.

## Motion tokens

- **One curve, `cubic-bezier(0.4, 0, 0.2, 1)`.** Durations `--dur-fast .15s`,
  `--dur-base .28s`, `--dur-slow .32s`.
- **The model never moves.** No parallax, no rotation, no exploded-view on
  scroll, no block that slides into place. A measurable object that drifts stops
  being measurable, and an exploded view on scroll is the single most tempting
  and most damaging thing you can do to this pack.
- The only motion in the hero is the agent prompt's caret, which blinks. That is
  the reference's own behaviour and it is the exception that proves the rule: one
  living pixel on a page of still ones.
- `prefers-reduced-motion` zeroes every duration and stops the caret. The
  reference ships four such blocks — unusually good for this category — and this
  pack requires the same posture.

## Signature motifs

- **The axonometric model** in cream on the dark table, blocks separated by the
  field colour.
- **Mono block labels on cream chips** with dotted leaders.
- **The offset shadow** at a fixed upper-left light.
- **Pill actions** — every action, at 36px radius, on a page otherwise made of
  rectangles.
- **The CLI line** under the buttons: the enterprise page that still shows you a
  command.
- **One aqua phrase** in the headline.
- **A near-single-value dark field** — three surfaces within a few percent of
  each other, so the model is the only bright object.

## Signature element

**The axonometric model.** One per page, in the first viewport, complete and
labelled.

It carries the identity because it is the only pack in this library whose subject
is a *drawing of a thing* rather than the thing itself or a story about it. A
screenshot shows what the product looks like; a photograph shows what it is; an
axonometric model shows how it is **assembled** — and that is exactly the
question an architecture buyer is asking before they will listen to a price.

Axonometric, specifically, and not perspective: there is no vanishing point, so
every block keeps its true proportion and the drawing stays measurable. That is
not a stylistic preference. A perspective render says *look at this*; an
axonometric drawing says *check this*.

Everything else is quiet to pay for it: one accent, one shadow, a field that is
nearly one value, and no second drawing anywhere on the page.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack: keep the scroll clock, run the Reveal set
at `--dur-slow` on the one curve — opacity and an 8px translate, nothing larger.

**The model is exempt from all of it.** It enters with the section and then it is
static for the rest of the page's life. There is no particle field in this pack,
no mesh gradient, no WebGL: the ambient layer, if you want one, is the table
itself — a very slight vignette toward the edges, and nothing that moves.

If a section needs to show change over time, that section is telling you the page
belongs in `instrument-console`.

## Micro-interactions

- **Pills** transition fill over `--dur-fast` and press to `translateY(1px)`.
  Nothing scales; a scaling pill on a page of static rectangles reads as the only
  soft thing in the room.
- **The CLI copy button changes its label**, not only its colour — the same rule
  as the status marks, and for the same people.
- **Focus-visible** is an `--accent` border plus a 3px aqua halo at 20% alpha,
  following the element's own radius. On an aqua fill the ring is `--ink`
  instead, because aqua on aqua is nothing.
- **Nav** changes colour only; the current item is `--accent`.
- Model blocks, leaders and labels have **no states at all.** They are printed on
  the page.

## Bans

- **Moving the model.** Parallax, rotation, exploded views, scroll-linked
  assembly, hover-to-highlight-a-block. It is a drawing.
- **Perspective.** No vanishing point, ever. Axonometric or it is a different
  pack.
- **`#FFFFFF` as ink.** The ink is cream and it matches the model.
- The cream as a label on an aqua fill — 1.1:1. Black, or nothing.
- A gradient on a model face; a drawn stroke around a block where the field
  colour belongs.
- A second drawing on the page; an unlabelled block.
- Widening the dark family — a `#0A0A0A` or a `#252525` panel breaks the
  single-value field.
- A status mark without its word.
- A rectangle where a pill belongs, or a pill where a panel belongs.
- `transition: all`; `100vh`; a scroll listener; fluid `clamp()` type.

## Gotchas

- **The reference exposes no status palette, and this pack's statuses are
  therefore derived, not extracted.** The token layer says so at the
  declaration. The first set this run reached for was a framework default and the
  palette gate caught it colliding — 7.9 under deuteranopia, 7.8 under
  protanopia. The replacement is separated as far as the hue wheel allows and
  green still sits 6.4 from red under deuteranopia, which is why the pack
  declares its secondary encoding rather than claiming to have solved it.
- **The ink is cream and every tool will try to make it white.** Framework
  defaults, "improve contrast" linters and designers copying from a screenshot
  all converge on `#FFFFFF`. It measures better (18.4:1 vs 17.49:1) and it is
  wrong: the page's whole coherence is that the type and the model are the same
  material.
- **The shadow is displaced on both axes and that is not a mistake.**
  `12px 24px 24px` looks wrong in a spec and correct on the page. A centred
  shadow (`0 24px 24px`) turns the model from an object on a table into a card in
  a stack.
- **Aqua on aqua disappears.** `--accent` as a focus ring on an aqua-filled
  button is invisible; use `--ink` there. This is the one place the pack needs a
  conditional and it is easy to miss because it only shows up on the primary CTA.
- **The reference's `--topbar-secondary-text-color` `#B3B5C1` is the only colour
  token it exposes at all** — seven root variables in total. Everything else in
  this pack was read off painted elements rather than from a declaration, so
  treat the surface family in particular as a faithful reading rather than a
  published palette.
- **Values are a snapshot** taken 2026-08-09 from a live production site. Treat
  them as extracted, not eternal.
