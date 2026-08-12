# Style pack — <Name>

> **This is the skeleton, not a pack.** Copy it to `styles/<name>.md`, fill
> every heading, and author `styles/tokens/<name>.css` in the same change.
> Never load this file as a style.

Origin: <an addressable production reference — a URL, or a named system with
the URL beside it; never invented ad hoc, never a product name alone. If the
next person cannot re-read the reference, the provenance is decorative.>
One-paragraph identity: field, ink, THE one accent, type voice, signature
texture.

Contract: <`widened` for all thirteen headings, or `core` if this pack
omits Components / Hero / Responsive / Signature element — in which case
say, here, what the reader must decide themselves. A pack that is silent
about its own silence is read as complete.>

## Before you fill anything — four rules that decide whether this pack is real

Until 1.11.0 these were spread across three places a reader of the installed
bundle cannot reach — the repository's `CONTRIBUTING.md` (rules 1 and 4), a
standing instruction in its retrospective (rule 2), and the prose of one pack
that had solved it once (rule 3). Being scattered is why they are restated here
rather than moved: the agent most likely to author a pack holds this directory
and no clone.

1. **Do not ship on the nine.** The consistency gate enforces the nine original
   headings always and the four widened ones all-or-nothing, so a pack cannot be
   *half* widened — but a pack that omits all four still passes. It passes and
   the agent that reads it invents the rest. Ship `widened`, or ship `core` and
   say in the `Contract:` line exactly what you are leaving to the reader.
2. **No addressable reference, no pack.** `Origin:` needs something the next
   person can open — a URL or a bare host, never a product name alone. This is
   not politeness about attribution: the contract forbids invented values, and a
   synthesised palette with a citation attached is an invented value wearing the
   costume of a measured one. A planned pack and a backfill were both held rather
   than shipped on this rule. Finding the reference is usually the most expensive
   part of authoring a pack, and nothing here can do it for you — a marketing
   site with a published stylesheet is the cheapest kind to measure.
3. **A value the reference does not have is a pack decision, and says so where
   it is declared.** Marketing sites do not paint error states, so a pack
   extracted from one usually has no status set while the palette gate still
   demands one that separates under dichromacy. Derive it, and mark it derived
   **at the declaration** — `maquette`'s token layer is the worked example. The
   failure this prevents is a derived value read later as a measured one.
4. **The gates are what "done" means.** Three of them run on every change:
   consistency (structure, routing, mirrors, kit parity), palette (every ratio
   you state recomputed from your token layer, plus OKLab separation under
   protanopia / deuteranopia / tritanopia), and slop lint (the skill obeying its
   own bans). Two consequences while authoring: the palette gate cannot compute
   a value it cannot parse, so a colour it cannot read is a **failure** rather
   than a skip (see rule 5 for what it can read now); and a markdown link from
   your pack to another must be reciprocated, so do not fork against a pack you
   are not also editing.
5. **Derive a colour from a token instead of restating its channels.** Until
   1.22.0 this rule was the opposite one — `color-mix()` was banned from the token
   layer — and the reason was never a design position, it was the gate's parser.
   It parses both now, verified against Chrome's own computed values across eleven
   cases at a worst ΔE of 0.004:

   - `color-mix(in srgb | srgb-linear | oklab | oklch, A p%, B q%)` — premultiplied,
     shorter hue arc in the polar space. **Any other space still fails**, because
     mixing in `srgb` and mixing in `oklab` give visibly different midpoints and a
     gate that guessed would certify a colour nobody rendered.
   - `rgb(from <colour> r g b / a)` — the alpha-variant form. `oklch(from …)` and a
     `calc()` inside a channel still fail: half-implemented CSS maths is worse than
     an honest refusal.
   - `var()` now resolves **inside** a value, so `rgb(from var(--accent) r g b / .35)`
     is readable by the gate.

   Why it matters: 42 declarations across eight shipped token layers restate a
   token's channels by hand, and a hand-derived literal stops tracking its source
   the moment either one moves — which is the live defect behind board B-023/B-024.
   `showroom`'s focus ring is the worked example.

   **One rule when you migrate.** Relative colour is Baseline 2024, so a browser
   that cannot parse it drops the declaration. Where the token feeds an
   accessibility-critical property — a focus ring above all — ship the literal
   first and the derived value second, so the old browser keeps the literal. For
   an ordinary decorative tint the derived value alone is fine.

## Register

Choose this pack for <product kinds / registers>. State whether it rides
the SHELEG cinematic motion layer or is used standalone.

**Not for:** <the registers this pack actively fails at>. A pack that claims
everything routes nowhere.

## Palette

Ready-made token layer: `tokens/<name>.css` (link it here once authored) —
copied verbatim instead of transcribing this table. Author that file in
the same change; the validator enforces it.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#……` | page field |
| `--ink` | `#……` | primary text |
| `--accent` | `#……` | THE single functional accent |

State contrast rules (WCAG floors) and what each semantic color may mean.

## Type

Display / body / data faces (≤3 families), weights, scale, measures.

## Texture & surface

Elevation model (border vs shadow vs surface steps), radii set, grain/
texture, spacing grid.

State the **radius arithmetic** when containers nest: an inner radius is the
outer radius minus the padding between them (`calc(2rem - 0.375rem)` inside
`p-1.5`), never the same value twice. Concentric curves are what separates
machined from stuck-together.

## Components

The per-component spec. Values measured off the reference, never inferred.
Each entry states resting state, hover, active and disabled — a component
described only at rest is half a component.

- **Buttons** — fill/outline hierarchy, radius, padding, press feedback.
- **Cards / containers** — fill, border, shadow, internal padding, when a card
  is used at all versus a divider or plain negative space.
- **Inputs / forms** — label position, focus ring, error placement.
- **Navigation** — resting shape, scrolled shape, mobile shape.
- **Loaders** — the pack's loading idiom (skeleton geometry matching the real
  layout, or a spinner, or nothing).
- **Empty states** — what fills a screen with no data.

## Hero

The pack's opening architecture: composition, type scale at the top of the
page, what the first viewport must contain and what it must not. State the
line ceiling for the display headline and the container width that keeps it
there — a headline that wraps to five lines is a broken hero, not a long one.

## Responsive

How the pack collapses. Not "it is responsive" — the actual rules.

- **Fluid type** — the `clamp()` values, with the slope shown, not guessed.
- **Container queries** — which components size against their container
  (`container-type: inline-size`) rather than the viewport. **This bullet is not
  optional and "none" is a valid answer**: it was added with the widened contract
  and seven of the ten widened packs left it blank until 1.23.0, which is why
  `validate_pack_container_answer()` now asks for it. Sort every breakpoint the
  pack owns into three kinds, because only the first has a container answer:

  | Kind | What it is | Where it goes |
  |---|---|---|
  | **CONTAINER** | a property on a *descendant* of a component root — a row's column widths, a grid's track count, a decorative tick | `container-type: inline-size` on the root, `@container` on the descendant |
  | **PAGE** | a value the page owns — a hero's padding, a nav's shape, a root token switch | a viewport `@media`, and it stays there |
  | **SELF** | a property on the element that *establishes* the container — a block's own shadow, a background-size on the grid element itself | **no container answer exists.** A container cannot query itself, and adding a wrapper to a consumer's markup is not the kit's business. Keep the viewport query and mark it `SELF` with the reason |

  The distinction the library was missing: **the pack documents a page measured off
  a reference, so its breakpoints are viewport-shaped; the kit ships components this
  project authors, so theirs are container-shaped.** `field-notes` was right that
  container queries are "not for the page" and incomplete about the component
  library shipped beside it.
- **Collapse** — what happens to asymmetry, overlap, rotation and negative
  margins below the pack's breakpoint. Overlapping elements that survive to
  mobile become touch-target conflicts.
- **Viewport** — `min-h-[100dvh]`, never `100vh`, for full-height sections.

## Motion tokens

The one site-wide ease, durations, stagger; what overrides the SHELEG
defaults; reduced-motion behavior.

## Signature motifs

The 3–6 recurring devices that make this style recognizable.

## Signature element

The **single** thing a page in this pack is remembered by — distinct from the
motifs above, which recur. One element, named, with the reason it carries the
pack's identity. If boldness is spent everywhere it is spent nowhere: this is
where it goes, and everything around it stays quiet.

## Motion flavor (optional — cinematic packs only)

How the pack rides the SHELEG layers: particle tint/energy, Reveal set,
instrument styling.

## Micro-interactions

Buttons, hover/selected states, focus-visible, keyboard rules.

## Bans

The slop guard: what this style never does. Be specific.

## Gotchas

Migration/usage traps discovered in production.

Correct the record here, do not flatter it: if an earlier version of this pack
shipped wrong values, name them and the right ones beside them. A gotcha that
only warns is half a gotcha — say what breaks and what it looks like when it
does.
