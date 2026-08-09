# Design record — four style packs, v1.9.0

**Stage 3 · manual gate.** Settles C5 and fixes the shape of all four packs.
Every value was read off its live reference on 2026-08-09; every ratio was
computed by importing `test/validate_palette.py`.

---

## 1. `showroom` — the product is the hero

**Origin:** <https://attio.com/>

**Register.** Choose `showroom` for a **product-led company whose best argument
is the product on screen**: CRMs, project tools, analytics, anything where a
dense real surface — a table with real rows, real chips, real column headers —
persuades faster than a sentence about it. The first viewport carries the claim
and then *the application itself*, at full fidelity and legible size, not a
blurred mock.

**Not for:** a product with no screenshot worth showing (that is `cyclorama`);
an open-source project whose front door is a command, not a UI (`prism`); the
dashboard itself, which is `workbench` — this pack is the marketing page that
*displays* such a dashboard.

**The fork people will get wrong — against `workbench`.** Both render dense
product UI with borders as elevation and a single blue accent. `workbench` **is**
the tool: it is meant to disappear, it caps its motion at 150–200ms, and it bans
scroll-driven motion. `showroom` is the page **arguing for** the tool: it rides
the cinematic layer, and its product surface is a specimen under glass, lit and
framed. Route by which surface you are building — the thing operated, or the page
that sells it.

**Palette.** Converted from `lab()` through the browser's own canvas.

| Token | Value | Role | Measured |
|---|---|---|---|
| `--bg` | `#FFFFFF` | the page | — |
| `--surface` / `--surface-2` | `#FAFAFB` / `#EDEFF3` | card · sunken well | — |
| `--ink` | `#1C1D1F` | body and display | **16.87:1** |
| `--ink-2` | `#232529` | secondary | 15.9:1 |
| `--ink-soft` | `#505967` | captions that must be read | 7.7:1 |
| `--disabled` | `#A4ADBA` | **disabled and placeholder only** | 2.27:1 ✗ — see Gotchas |
| `--line` / `-strong` | `#D3D8DF` / `#CAD0D9` | hairline · emphasised | — |
| `--accent` | `#266DF0` | link, primary fill | **4.64:1** both directions |
| `--good` / `--danger` / `--warning` | `#0FC27B` / `#FF5B59` / `#F5B900` | status | needs the declaration |

**Type.** Four families ship on the reference; the pack takes **three** and names
the fourth vestigial (settles C5): **InterDisplay 600** for display,
**Inter 400/500** for body and UI, **JetBrains Mono** for data and IDs.
**Tiempos** appears on one editorial surface only and is *not* part of this pack —
a serif in a showroom page is a different register wearing this one's clothes.
The ramp is the reference's own `--text-*` set, where **every step carries its
own weight, line-height and tracking** as one token — that coupling is the thing
to copy.

**Texture.** The signature is the **seven-layer shadow**: a 1px inner ring plus
six stacked offsets from `0 1px 2px` to `0 32px 64px -8px`, all at 3–15% alpha.
It is what makes the product screenshot read as a physical specimen rather than
an image pasted on a page. Radii `2/4/6/8/12/16/20`.

**Signature element — the specimen.** One product surface, in the first viewport,
at real size, under the seven-layer shadow, cropped by the viewport rather than
scaled down. Everything else on the page is quiet so that this reads as evidence.

**Kit:** spine + `Specimen` (the shadowed product frame), `DataRow`,
`StatusChip`, `ColumnHeader`.

---

## 2. `blueprint` — the drawing, not the render

**Origin:** <https://www.pinecone.io/>

**Register.** Choose `blueprint` for **infrastructure sold on precision**: vector
databases, search and retrieval, storage engines, anything whose buyer wants to
see the mechanism drawn to scale. Its whole vocabulary is technical drafting —
a white sheet, a grid, ruled column edges, registration marks at the corners of
things, and one saturated blue used the way a draftsman uses ink.

**Not for:** a page whose subject is a *running* system (`instrument-console`); a
warm, humane document (`field-notes`); anything that needs a rounded corner —
this pack has **no radius at all**, and adding one breaks it more than changing
its blue would.

**The fork — against `field-notes`.** Both draw rules on a light field and both
serve technical readers. `field-notes` is **warm paper**: green-cast off-white,
rust ink, crop marks that say *this was printed*. `blueprint` is **cold stock**:
pure white, electric blue, registration marks that say *this was drawn to
tolerance*. Route by whether the argument is provenance (*how do you know*) or
precision (*how exactly is it built*).

**Palette.**

| Token | Value | Role | Measured |
|---|---|---|---|
| `--bg` / `--surface` | `#FBFBFC` / `#FFFFFF` | sheet · panel | — |
| `--ink` | `#111827` | body and display | **17.74:1** |
| `--ink-soft` | `#4B5563` | secondary | 7.5:1 |
| `--line` / `-2` / `-3` | `#E7E5E4` / `#E2E8F0` / `#CBD5E1` | the grid, the rules | — |
| `--accent` | `#002BFF` | ink **and** fill — rare | **7.53:1** both ways |
| `--good` / `--info` / `--danger` | `#86AF80` / `#8BF6FF` / `#A440CE` | category marks | all pairs clear both floors |

**The ink conflict, stated plainly.** The reference sets **pure black** on 316
elements. The doctrine bans pure black as ink and `sloplint.py` enforces it. This
pack ships `#111827` — the reference's **own second ink**, on 136 elements — and
does not pretend that is the same colour: the two sit **21.2 apart** in OKLab.
It is a substitution, it is visible, and it is recorded in Gotchas.

**Type.** GT Planar (licensed) + JetBrains Mono. Substitutes measured at stage 4.
The ramp is small and letterspaced at the bottom: `10px/1px` and `11px/600/0.5px`
labels, `12px` JetBrains Mono for data, `13/15/16px` body, `32/44px/700` display.

**Texture.** **Zero radius everywhere.** Elevation is a hairline; there is one
soft shadow and one `0 0 0 1px` accent ring, and nothing else. Transitions
`0.15s ease-out`.

**Signature element — the registration marks.** Small L-shaped brackets at the
corners of the primary action and of framed figures. They cost nothing, they are
the one ornament the pack allows, and they are why the page reads as a drawing
rather than a website. *(Observed on the rendered page; not reachable from any
stylesheet rule — see the ledger, C3.)*

**Correction required:** the reference ships **no** `prefers-reduced-motion`
branch against live marquee, ping, pulse and scroll. The pack requires one.

**Kit:** spine + `RegistrationMarks`, `GridField`, `RuledColumn`, `CodeLine`.

---

## 3. `prism` — white split into a spectrum

**Origin:** <https://milvus.io/>

**Register.** Choose `prism` for an **open-source infrastructure project's front
door**: the page a developer lands on from GitHub, where the first action is a
command and the second is a benchmark. Its field is white passed through an
iridescent wash — pink to lilac to mint to cyan — and its body copy is **mono**,
which is what makes it read as a project rather than a company.

**Not for:** the commercial product built on that project — that is `maquette`,
and the two are the same company's two faces; a page selling auditability
(`field-notes`); a page whose field must hold still (`workbench`).

**The fork — against `cyclorama`.** Both are pale, mono-voiced light fields.
`cyclorama`'s field **moves** — six stops on a 32-second loop — and its display
face is a typewriter serif. `prism`'s field **holds**: one static iridescent
wash, with a heavy grotesque display. Route by whether the page's subject is a
change of state (`cyclorama`) or a piece of software you can install right now
(`prism`).

**Palette.**

| Token | Value | Role | Measured |
|---|---|---|---|
| `--bg` / `--surface` | `#FFFFFF` / `#F9F9F9` | field · card | — |
| `--ink` | `#00131A` | near-black, cyan-cast | **18.95:1** |
| `--ink-soft` | `#667176` | body-safe secondary | **5.01:1** |
| `--line` | `#E9E9ED` | card border | — |
| `--accent` | `#00B3FF` | **fill and large display only** | 2.36:1 as body text ✗ |
| `--on-accent` | `#00131A` | label on the accent | **8.02:1** |
| `--good` / `--warning` / `--danger` | `#65F8C3` / `#F25C05` / `#D51F00` | status | warning/danger 11.3 → declaration |

**Correction required:** no `prefers-reduced-motion` branch on the reference. The
pack requires one, and it must stop the iridescence from animating.

**Signature element — the wash.** The prism itself: one static gradient across
the top of the page, pink → lilac → mint → cyan, under type that never picks up
its hue. It is spent once, at the top; below it the page is white.

**Kit:** spine + `Wash` (the gradient as a static surface), `InstallLine`,
`BenchmarkRow`, `RepoBadge`.

---

## 4. `maquette` — the built object on a dark table

**Origin:** <https://zilliz.com/>

**Register.** Choose `maquette` for **enterprise data infrastructure sold to an
architecture buyer**, where the reader must understand a structure before they
can evaluate it. The subject is a *built object*: an axonometric model in cream,
labelled block by block in mono, lit from the upper left on a near-black table.

**Not for:** a product with a value that changes while you watch. That is
`instrument-console`, and this fork was **tested before the pack was built** —
see the brief.

**The fork — against `instrument-console`, and it is reciprocal.** A cockpit
answers *what is happening now*; a maquette answers *what is this made of*. The
test: **does the page have to render a number that changes while the reader
watches?** Yes → `instrument-console`. No, but the reader must decompose a system
→ `maquette`. `instrument-console` gains the mirror clause in this run (REQ-012).

**Palette.**

| Token | Value | Role | Measured |
|---|---|---|---|
| `--bg` | `#151515` | the table | — |
| `--surface` / `-2` / `-3` | `#1B1B1B` / `#1D1D1D` / `#131313` | a tight dark family | ink 16.49–17.79:1 |
| `--ink` | `#FFF9F4` | **cream**, not white — the model's own colour | **17.49:1** |
| `--ink-soft` | `#B3B5C1` | secondary | **8.95:1** |
| `--line` | `#2B2B2B` | hairline | — |
| `--accent` | `#97FDFF` | pale aqua — works as **text**, unusually | **15.49:1** |
| `--on-accent` | `#000000` | label on the aqua CTA | **17.81:1** |
| `--model-face` | `#FFF3D6` | the lit face of a model block | 16.56:1 |

**Status is a pack decision, and the pack says so.** The reference exposes no
status palette; its surface is cream, aqua and greys. `--good` `#3FCF7F`,
`--warning` `#FFB020` and `--danger` `#FF5C5C` are derived to sit in the pack's
own world, not extracted. The first set this run reached for was a framework
default and the palette gate caught it colliding — recorded in the brief, and the
token layer now marks the whole set as derived. `never by colour alone` is
declared: green and red sit 6.4 apart under deuteranopia in every candidate,
because that pair is not separable by hex for a deuteranope.

**Texture — the offset shadow.** `12px 24px 24px rgba(0,0,0,.25)`: displaced on
**both** axes, which is what makes a block read as sitting on a surface under a
raking light rather than floating. It is the pack's one shadow and its direction
is not adjustable — every block is lit from the same upper-left source or the
model falls apart. Radii `8`, with `36px` pills for actions.

**Signature element — the axonometric model.** One per page, cream on the dark
field, blocks labelled in mono, dotted leader lines to their captions. No
perspective, no vanishing point: axonometric, so every block keeps its true
proportion and the drawing stays measurable.

**Kit:** spine + `ModelBlock`, `LeaderLabel`, `AquaPill`, `CliLine`.

---

## 5. The reciprocity fix (REQ-012)

Where a new pack forks against an existing one, the existing one gains a
one-paragraph mirror clause:

| Existing pack | Gains a fork against | Because |
|---|---|---|
| `instrument-console` | `maquette` | the dial/model test — and it currently names **no** pack at all |
| `workbench` | `showroom` | the operated surface vs the page selling it |
| `field-notes` | `blueprint` | provenance vs precision |
| `cyclorama` | `prism` | a field that moves vs a field that holds |

And a new `validate.py` check: **if pack A's text names pack B inside a fork,
pack B must name pack A.** Shipped with a planted defect, per standing
instruction 6.

## 6. What this run will not do

- No change to any existing pack's **values** — only added fork paragraphs.
- No dark themes for `showroom`, `blueprint` or `prism`; their references have
  none, and inventing one is inventing a dozen colours.
- No new gate beyond the reciprocity check.
