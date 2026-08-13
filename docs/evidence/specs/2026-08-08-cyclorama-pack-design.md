# Design record — `cyclorama` style pack

**Stage 3 · manual gate.** Settles C1 and C2 from the carry-over ledger.
Every value here was read off <https://www.codos.ai/> on 2026-08-08; every ratio
was computed by importing `test/validate_palette.py`. Where this pack diverges
from the reference it says so and gives the measured reason.

## 1. Identity

A pale field that **breathes through six pastel stops on a 32-second loop**,
near-black ink that never moves with it, one orange used only as a fill, a
**monospaced typewriter serif** for display over a monospaced sans for
everything else, and a generative organ that holds a formation for most of a
section and then redeploys.

The name: a *cyclorama* is the seamless theatre backdrop that changes colour
behind a fixed subject. That is literally the composition — `ctaCycle` recolours
the whole page while the type, the rules and the ink stay put.

## 2. Register — settles C1

**Choose `cyclorama` for a company selling transformation to an executive
buyer**: founder-led enterprise AI, AI-transformation and applied-AI services,
technical consultancies whose argument is *we install this and your business
starts running differently*. It suits a product with no screenshot worth showing
— where the thing being sold is a change of state, and the page has to make that
change visible without a product tour.

It **rides the SHELEG cinematic layer** and is the first pack whose reference
already implements it: GSAP ScrollTrigger with real pinning
(`pin-spacer-problemPin`), two WebGL canvases, and a formation that holds then
redeploys rather than crossfading.

**Not for:** data-dense product UI (a field that recolours under you is a defect
on a screen held for an hour — that is `workbench`); regulated, clinical or
public-sector pages where a moving pastel field reads as unserious; decks
(`briefing-room` is fixed 16:9 and never animates); any brand whose identity
depends on one stable background colour, because this pack's background is not a
colour, it is a loop.

### The forks, in the order people get them wrong

**Against `field-notes`** — the sharp one. Both are warm, light and
monospace-voiced, and both serve technical companies. `field-notes` is a **ruled
document** selling *auditability*: hairlines compose the page, crop marks sit at
the corners, provenance tags qualify each claim, and nothing moves. `cyclorama`
is a **stage** selling *transformation*: the field itself is the motion, the
subject is generative, and there is no hairline composition at all. Route by what
the product's argument rests on — *how do you know?* takes `field-notes`; *watch
this change* takes `cyclorama`.

**Against `instrument-console`.** Both are technical. `instrument-console` is a
dark cockpit whose one electric signal exists to make a **changing value**
readable. `cyclorama` is pale and its subject is a **changing organism** — there
is no dial, no telemetry, no live number.

**Against `orchard` and `atrium`.** All three are warm and light with a single
warm accent. Those two are **static** fields for consumer health and biotech, and
their buyer is a person buying for themselves. This field cycles, and its buyer
is an executive spending a company's money.

**Against `briefing-room`.** Both address the boardroom. `briefing-room` is a
fixed canvas that never animates; here motion is the identity.

## 3. Palette — every value measured, none invented

The field is **not one colour**, so every contrast claim is stated against the
worst stop.

| Token | Value | Role | Worst-stop ratio |
|---|---|---|---|
| `--bg` | `#F9DEF3` | the cycle's rest stop — `0%`/`100%` | — |
| `--field-1 … --field-6` | `#F9DEF3` `#F3D9B8` `#F9E0E2` `#EAE3EE` `#E6EEE3` `#EEEAE3` | the six stops of `ctaCycle`, in order | — |
| `--ink` | `#1a1a1a` | body and display | **12.79:1** (on `--field-2`) |
| `--ink-soft` | `#3a3a3a` | eyebrows, captions, secondary copy | **8.36:1** — a real body colour |
| `--accent` | `#FF8C00` | **fill, dot, chart series — never text on the field** | 1.71:1 as text ✗ |
| `--accent-hover` | `#e69900` | the accent's hover fill | — |
| `--on-accent` | `#1a1a1a` | the label on an accent fill | **7.46:1** |
| `--on-ink` | `#EBE1F0` | the label on an ink fill — the field colour, not white | measured off the live button |
| `--line` | `rgba(26,26,26,.22)` | THE hairline: window frames, outline buttons | — |
| `--line-soft` / `--fill-soft` | `rgba(26,26,26,.12)` / `rgba(26,26,26,.06)` | dividers / chip fill | — |
| `--surface` | `#ffffff` | the card — the one opaque surface in the system | — |
| `--panel` | `#C8BFCC` | the mist panel (comparison tables) | — |
| `--panel-tab` | `#b9afbd` | the panel's selected tab | — |
| `--good` | `#2c5a44` | success | — |
| `--warning` | `#9a6a00` | warning | — |
| `--danger` | `#7a3a1c` | destructive | — |
| `--info` | `#1b6ec2` | informational | — |
| `--signal` | `#00c22d` | the live dot — **a fill**; ink on it is 7.26:1 | 1.76:1 as text ✗ |

**Two rules carry this palette.**

1. **The accent is a fill and only a fill.** As text it measures 1.71–1.97:1
   across the six stops, and the reference paints its eyebrows that way anyway.
   Darkening is *not* the fix, and this pack records why rather than leaving the
   next person to rediscover it: the warm-dark region is already occupied by two
   of the reference's own semantics, so every text-capable orange collides —
   `#903A00` sits **4.6** from `--danger` (hard floor 10), `#A14700` sits 9.0
   from it and 5.1 from `--warning` under deuteranopia, `#C56200` sits **1.4**
   from `--warning` under protanopia. Eyebrows take `--ink-soft` at 8.36:1.
2. **Status is never by colour alone.** `--good` and `--danger` separate by 14.0
   at full colour but **7.2 under protanopia and 5.9 under deuteranopia**;
   `--warning`/`--danger` sit at 14.8. All are above the hard floor, so the
   palette is legal *with* the declaration — and the declaration is a measurement
   of the reference, which renders `● Listening` with the word and pairs every
   comparison dot with a text phrase.

## 4. Type — two monospaced faces, and that is the thesis

Measured advance ratios at 100px, the same probe for every face:

| Face | Ratio | Monospaced | Role |
|---|---|---|---|
| GT Alpina Typewriter | **0.590** | yes | display |
| DM Mono | 0.600 | yes | body, UI, data |
| Urbanist | proportional | no | vestigial — set on `body`, almost nothing uses it |

**Display and body are both monospaced, two percent apart.** That is why the page
reads as one voice rather than two, and it is the first thing to preserve.

**Substitutes, measured rather than recommended from memory.** GT Alpina
Typewriter is licensed (Grilli Type), so the pack must name obtainable faces
that keep the ratio *and* the serif:

- **Courier Prime** (SIL OFL) — ratio **0.600**, monospaced typewriter serif. The
  primary substitute.
- **Cutive Mono** (SIL OFL) — ratio 0.605, same category.
- **Not** Zilla Slab (0.576) or Bitter (0.641): both are **proportional**, and the
  hero is laid out per character.
- **Not Fraunces**, which is the reference's own declared fallback and is
  proportional. Recorded in Gotchas.

Scale, resolved at 1440px from the reference's own clamps:

| Token | Value | Notes |
|---|---|---|
| `--t-display` | `clamp(2.25rem, .5rem + 6.7vw, 8.125rem)` → **104.48px** at 1440 | `line-height: 1`, tracking **−0.02em** |
| `--t-h1` … `--t-h4` | `clamp` 2→3.75rem · 1.6→2.5rem · 1.375→1.875rem · 1.125→1.3125rem | leading 1.05 / 1.1 / 1.15 / 1.3 |
| `--t-intro` / `--t-body` / `--t-sm` | 1.125→1.875rem · .9375→1.0625rem · .8125→.875rem | leading 1.35 / 1.6 / 1.55 |
| `--t-metric` | `clamp(2.75rem, .8rem + 6vw, 6.5rem)` | leading .95 |
| `--t-caption` | .75rem | leading 1.45 |

## 5. Texture, surface, and the radius arithmetic

- **Elevation is a hairline, never a shadow.** `box-shadow: none` everywhere on
  the reference. The app window is `1px solid rgba(26,26,26,.22)` with **no
  fill** — the field cycle shows through it, which is why it cannot have one.
- **Radii: 4 / 8 / 16 / 24 / 9999**, and the reference's nesting is arithmetically
  correct — a 16px window with 12px padding holds 4px chips (16 − 12 = 4). The
  pack states this as the rule, with the measurement as its proof.
- **Rhythm:** `--section-gap: 200px`, `--page-max: 90rem`,
  `--page-gutter: clamp(1.75rem, 5.6vw, 5.6rem)`, spacing ramp
  0 / .25 / .5 / .75 / 1 / 1.5 / 2 / 3 / 4 / 6 rem.
- **Cards** are the one opaque surface: `#ffffff`, 16px radius, 32px padding, no
  border, no shadow.

## 6. Motion tokens

- **One ease, `cubic-bezier(.22,1,.36,1)`**, with a spring
  `cubic-bezier(.34,1.56,.64,1)` reserved for entrance only. Durations
  `.15s` / `.25s` / `.5s`.
- **`ctaCycle`: 32s, `ease-in-out`, infinite, six stops** — the signature.
- `particle-breathe` 6s on hover; `heroUp` and `legal-rise` are 10–12px
  translate-plus-fade entrances.
- **Reduced motion kills all of it**, including hover transforms — the reference
  ships this branch for every animated class, and the pack requires the same.
- `transition: all` appears on the reference's `html` rule. The pack bans it and
  scopes transitions to named properties.

## 7. Signature element — the cycling field

Not the organ. The organ recurs section by section, and recurrence makes a motif.
**The field cycle happens once, continuously, everywhere**, and it is the only
place this pack spends anything.

Everything else is quiet *because* of it, and that is the price: one accent used
only as a fill, no shadows, no gradients, no second surface colour, black ink
that never shifts, hairline borders. A generative blob is common; a page that
recolours itself under fixed ink on a 32-second loop is not. Spend the boldness
here or the pack has no centre.

## 8. The kit — settles C2

Six spine components, whose `*Props` are byte-identical to `kits/workbench`
(`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule`), plus four signature ones:

| Component | Category | Why it earns a place |
|---|---|---|
| `FieldStop` | Foundations | Renders one named stop of the cycle as a static background. **The cycle itself does not cross the border** — `DESIGN_SYNC_BRIDGE.md` excludes motion — so the design agent gets the six stops as six swatches, not an animation. |
| `AppWindow` | Surfaces | The transparent 16px-radius hairline frame with traffic-light dots and a mono title. The pack's product-UI idiom. |
| `StatusPill` | Data | `● Listening` — the dot plus **the word**, which is the secondary encoding made structural rather than optional. |
| `ComparePanel` | Data | The mist panel with hairline rows and one dot per row. |

`Eyebrow` is deliberately **not** a component: it is `--ink-soft` mono with
tracking, and a component would invite someone to parameterise its colour, which
is the one thing this pack forbids.

## 9. What this run will NOT do

- No change to the motion doctrine, the dials, or any other pack.
- No new gate script. The three existing gates cover this pack; the one check
  they cannot make (`--accent-ink` against `--danger`) is closed by **not
  creating the token**, which is stronger than a check.
- No dark theme. The reference has none, and inventing one would be inventing
  eleven colours.
