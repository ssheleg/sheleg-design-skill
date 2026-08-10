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
   a value it cannot parse, so keep `color-mix()` and `lab()` out of the token
   layer; and a markdown link from your pack to another must be reciprocated, so
   do not fork against a pack you are not also editing.

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
  (`container-type: inline-size`) rather than the viewport.
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
