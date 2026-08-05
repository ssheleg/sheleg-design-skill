# `field-notes` — the graphify.com teardown

Date of capture: **2026-08-04**. Method: live DOM + `getComputedStyle` at
1280×720 on `https://graphify.com/`, plus the served `@font-face` set and the
authored CSS rules read out of `document.styleSheets`. Font contracts checked
against the Google Fonts CSS API and the upstream repository.

**What is measured and what is seen.** Every number below came off the live
page through the CSSOM. One viewport — the hero — was also inspected visually;
the browser pane could not be scrolled, so the composition of the sections
below the fold is described from the measured section/container/border data
rather than from a picture. Nothing here is an impression dressed as a value.

---

## 1. What the page is

An open-source developer tool sold on **auditability** rather than power. The
argument is "the answer is a path you can check", and the design serves that
argument in one decision: **it is printed on paper, not lit on a console.** In
a cockpit you trust the instrument; on paper you read the evidence.

That single choice is what makes it worth a pack. The skill already had a dark
technical register (`instrument-console`) and a neutral product-UI register
(`workbench`). It had no answer for a developer product whose whole pitch is
*here is where this came from*.

---

## 2. The token layer, verbatim

92 declared custom properties: a light `:root` and a complete `.dark` twin.
Framework base is Tailwind v4 + shadcn conventions, but the values are
authored, not defaults.

### 2.1 Light (`:root`)

| Token | Value | Role |
|---|---|---|
| `--background` | `#f8f7f0` | the paper — warm off-white with a green cast |
| `--foreground` | `#16211b` | the ink — near-black, also green-cast |
| `--card` / `--popover` | `#fdfcf6` | a lighter paper for raised blocks |
| `--card-foreground` / `--popover-foreground` | `#16211b` | |
| `--secondary` | `#edeee2` | the section wash (used at 40% opacity) |
| `--secondary-foreground` | `#232a24` | |
| `--muted` | `#edeee2` | the same wash, used at 20% |
| `--muted-foreground` | `#626b60` | captions, eyebrows, secondary copy |
| `--accent` | `#e8ebdd` | the deepest paper step |
| `--accent-foreground` | `#16211b` | |
| `--border` | `#e0e2d3` | **the hairline that does all the section work** |
| `--input` | `#dcdecd` | one step darker than the border |
| `--primary` | `#16211b` | ink as a fill (the dark pill button) |
| `--primary-foreground` | `#f8f7f0` | |
| `--brand` | `#9a3f28` | rust — the accent, a fill and a large-text colour |
| `--brand-foreground` | `#f8f4ef` | |
| `--brand-ink` | `#8f3f1f` | the text-safe rust |
| `--brand-soft` | `#e8cbb8` | the rust wash (selected chip) |
| `--ring` | `#9a3f28` | focus ring = the brand |
| `--destructive` | `#c0442e` | |
| `--radius` | `.75rem` (12px) | the **one** radius everything derives from |

### 2.2 The provenance triad — the pack's reason to exist

| Token | Value | On paper | Role |
|---|---|---|---|
| `--verify` | `#0e9e76` | 3.17:1 | fill / large only |
| `--verify-ink` | `#0a7558` | **5.29:1** | the tag label |
| `--verify-soft` | `#d6f1e7` | — | the tag wash |
| `--verify-foreground` | `#fff` | 3.40:1 on `--verify` | **fails — see §8** |
| `--witness` | `#b3402a` | 5.31:1 | |
| `--witness-ink` | `#9a3016` | **6.96:1** | |
| `--witness-soft` | `#f4ded4` | — | |
| `--witness-foreground` | `#fff` | 5.70:1 on `--witness` | passes |

Three states, three hues, and the tag component reads them as text rather than
as a score: `[EXTRACTED]` in `--verify-ink`, `[INFERRED]` in `--brand-ink`,
`[AMBIGUOUS]` — not present on the page at capture time — completes the set on
`--witness-ink` by construction of the token names.

> That last sentence is itself an inference, and it is labelled as one. The
> pack inherits that discipline; it is the whole point of the register.

### 2.3 Charts

`--chart-1 #9a3f28` · `--chart-2 #0e9e76` · `--chart-3 #f0603c` ·
`--chart-4 #b0563a` · `--chart-5 #3b82f6`. Series 1/2 are the brand and verify
hues; 3/4 extend the rust family; 5 is an unrelated blue and is the one value
in the set that looks like a framework default nobody revisited.

### 2.4 App surfaces

`--sidebar #fffdf9` · `--sidebar-accent #f1ece3` · `--sidebar-border #e8e1d5` ·
`--sidebar-foreground #1b1714` · `--sidebar-primary #1b1714` ·
`--sidebar-ring #6d5ae6`.

The sidebar family is warmer and *browner* than the page family (`#1b1714`
against the page's green-cast `#16211b`), and `--sidebar-ring` is a violet
`#6d5ae6` that appears nowhere else in the light theme. Both read as an
unreconciled second system rather than a decision — recorded here, reconciled
in the pack (§7).

### 2.5 Dark (`.dark`)

| Token | Value |
|---|---|
| `--background` | `#14110e` |
| `--card` / `--popover` / `--sidebar` | `#1c1815` |
| `--foreground` | `#f7f3ec` |
| `--muted` / `--accent` / `--secondary` | `#262019` |
| `--muted-foreground` | `#a89e8f` |
| `--border` | `#ffffff1a` (10%) |
| `--input` | `#ffffff24` (14%) |
| `--brand` / `--brand-ink` / `--ring` | `#cf7a52` |
| `--brand-soft` | `#2e1c12` |
| `--verify` / `--verify-ink` | `#2bc0a8` · soft `#14312a` |
| `--witness` / `--witness-ink` | `#e06a4f` · soft `#341711` |
| `--sidebar-primary` / `--sidebar-ring` | `#8f80f0` |

The dark twin is **warm brown**, not green. It is also the strongest part of
the whole system on contrast (§8) — and it is unrelated to the dark surfaces
actually painted on the page (§4.2).

---

## 3. Type

### 3.1 The families

| Slot | Family | Loaded weights | Notes |
|---|---|---|---|
| `--font-display` | **Bricolage Grotesque** | 500, 600, 700 (static cuts) | variable upstream: `opsz 12..96`, `wdth 75..100`, `wght 200..800`. **No italic exists.** SIL OFL 1.1, Mathieu Triay / Atelier Triay, forked from Jérémy Landes' Mayenne Sans |
| `--font-sans` | **Geist** | variable `100 900` | SIL OFL, Vercel |
| `--font-mono` | **Geist Mono** | variable `100 900` | SIL OFL, Vercel |

The page uses **600** for essentially every display setting, with 400 for two
deliberately quieter headings ("The answer is a path, not a vibe", "Graph,
chunks, or grep."). The `opsz` and `wdth` axes are available and unused.

### 3.2 The scale, as measured at 1280px

| Role | Size | Line height | Tracking | Weight | Family |
|---|---|---|---|---|---|
| Hero `h1` | 67.2px | 68.544px (1.02) | −1.68px (−0.025em) | 600 | display |
| Section `h2` | 44px | 50.6px (1.15) | −1.1px (−0.025em) | 600 | display |
| `h2` small | 40px / 30px | 46px / 36px (1.15 / 1.2) | −1px / −0.75px | 600 or 400 | display |
| `h3` | 20px | 28px (1.4) | −0.5px (−0.025em) | 600 or 400 | display |
| Card `h3` | 15px | 20.625px (1.375) | −0.375px (−0.025em) | 600 | display |
| Hero lede | 18px | 28px (1.556) | — | 400 | sans |
| Body | 16px | 24px (1.5) | — | 400 | sans |
| Eyebrow | 11px | 16.5px — or **11px (1.0)** on the `.eyebrow` class | **1.76px = 0.16em** | 400 | mono |
| Eyebrow, wide | 11px | 16.5px | 1.98px = 0.18em | 400 | mono |
| Provenance tag | 10px | 16px | 0.8px = 0.08em | 400 | mono |
| Tab label | 10px | 15px | 0.5px = 0.05em | 400 | mono |
| Terminal | 13px | 21.125px (1.625) | — | 400 | mono |
| Inline code | 0.9em of parent | 1.4 | −0.5px | 600 | mono |
| Data counter | 10px | 15px | 0.25px | 400 | mono + `tabular-nums` |

**The one rule that holds across the whole display range: tracking is a
constant −0.025em.** 67.2, 44, 40, 30, 20 and 15px all resolve to exactly
−0.025 of their size. That is a single authored decision, not five.

### 3.3 The `.eyebrow` component, authored

```css
.eyebrow {
  font-family: var(--font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted-foreground);
  font-size: 0.6875rem;   /* 11px */
  line-height: 1;
}
.eyebrow[data-n]::before { content: "〉"; opacity: .55; margin-right: .6em; }
.eyebrow[data-n]::after  { content: "[" attr(data-n) "/09]"; opacity: .55; margin-left: .6em; }
```

The page **numbers its own sections** — `〉 HOW IT WORKS [03/09]`. This is the
single most transferable motif in the design: it turns a marketing page into a
document with a table of contents, which is exactly the claim the product makes
about a codebase.

---

## 4. Surface & composition

### 4.1 Sections are ruled, not flipped

Measured across 16 `<section>` elements:

- **10** carry `border-top: 1px solid #e0e2d3` and no background at all.
- **3** carry the same hairline plus `background: --secondary` at **40%**
  opacity (one at `--muted` 20%).
- **1** is the hero.
- Section rhythm: `py-16` → **64px** top and bottom at `md`, `py-4` (16px)
  below it.

So the page is **one continuous sheet with rules drawn on it**. This is the
axis on which the pack differs from every warm pack the skill already has:
`orchard` stacks discrete slabs with the field showing between them; `atrium`
runs a continuous field and changes layout instead; `field-notes` runs a
continuous field and draws a line.

### 4.2 The hero is a dawn, not a band

```css
background-image: linear-gradient(
  #062a22   0%,
  #0a3f31  35%,
  #124f3c  60%,
  #1e6149  74%,
  #4f8a68  85%,
  #a8c9ad  93%,
  #e9ecdf  98%,
  #f8f7f0 100%
);
min-height: 100svh;
```

Eight stops from near-black forest to the exact paper colour. **The dark has no
edge** — it resolves into the page rather than ending against it. Two layers
sit on top:

- **Grain** — an inline SVG `feTurbulence type="fractalNoise" baseFrequency="0.82"`
  at 150×150, tiled, at low opacity.
- **Vignette** — `radial-gradient(72% 58% at 32% 42%, rgba(4,30,23,.28), transparent 74%)`,
  pulling focus to the headline's left third.
- **A glyph field** — mathematical and logical symbols (λ ∑ ∩ ∀ ⊗ ∫ θ ε ⇉ √ ∏)
  scattered at `--sym-op: .14`, with individual glyphs flickering to `--verify`
  (§6). Not particles — *notation*.

Other dark surfaces actually painted on the page, none of which match the
`.dark` theme or each other:

| Surface | Value | Family |
|---|---|---|
| Marquee / hero band | `#072820` | forest |
| Terminal header | `#0b332a` | forest |
| Terminal body | `#0b101d` | navy |
| Terminal sub-bar | `#131a2b` | navy |
| `.dark` theme background | `#14110e` | warm brown |

Three unrelated dark families. Recorded as a defect; resolved in §7.

### 4.3 Radii — one root, a proportional ramp

`--radius: .75rem` = 12px. Every radius on the page is a multiple of it:

| Measured | Ratio | Use |
|---|---|---|
| 3px | ×0.25 | the 16px assistant-icon square |
| 4px | ×0.33 | smallest marks |
| 7.2px | ×0.6 | **chips, provenance tags** |
| 9.6px | ×0.8 | inner blocks |
| 12px | ×1.0 | **cards, panels, buttons** |
| 16.8px | ×1.4 | media wells |
| 21.6px | ×1.8 | the largest panel |
| pill | — | nav, primary CTA, badges |

Change `--radius` and the whole system moves together. This is a real feature
and it forbids hardcoding `12px` anywhere.

### 4.4 Elevation is a ring

The four most-used shadows are all `0 0 0 1px <colour>` — a **1px ring**, not a
drop shadow. A named utility exists: `.hairline { border: 1px solid var(--border); }`.

| Shadow | Value | Job |
|---|---|---|
| ring | `0 0 0 1px #e0e2d3` | every card and panel |
| ring, brand | `0 0 0 1px oklab(.486843 .104033 .0736925 / .5–.6)` | the selected/branded panel |
| ring, inset (dark) | `inset 0 0 0 1px rgba(255,255,255,.04)` | panels on dark |
| sm | `0 1px 3px rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1)` | a lifted control |
| lg | `0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px` | overlay |
| deep, warm | `0 32px 64px -28px rgba(26,22,12,.45)` | the one floating hero object — note the **warm** tint, not grey |

### 4.5 Containers

| Max width | Padding-x | Use |
|---|---|---|
| 1920px | 16px → 48px | the full-bleed shell (hero, nav) |
| 1400px | 28px | the graph viewer |
| **1152px** (`max-w-6xl`) | 24px | **the default content column** |
| 672px | — | prose blocks |
| 576px / 448px | — | lede and caption measures |

### 4.6 Crop marks

```css
.crop-marks {
  position: absolute; inset: 14px; pointer-events: none;
  --cm-len: .75rem;                 /* 12px arms */
  /* 8 × linear-gradient(foreground/30%, foreground/30%) */
  background-size:     1px 12px, 12px 1px, 1px 12px, 12px 1px,
                       1px 12px, 12px 1px, 1px 12px, 12px 1px;
  background-position: 0% 0%, 0% 0%, 100% 0%, 100% 0%,
                       0% 100%, 0% 100%, 100% 100%, 100% 100%;
  background-repeat: no-repeat;
}
```

Real printer's registration marks — two 1px arms at each of the four corners,
inset from the edge, at 30% ink. `hidden md:block`: desktop only. Costs nothing
and states the whole thesis: *this is a printed document, and here is where it
was trimmed*.

---

## 5. Components

| Component | Measured spec |
|---|---|
| **Primary CTA (on dark)** | white fill, ink `#07281f`, 14px/500 sans, `8px 16px`, **pill**, transition `opacity .15s cubic-bezier(.4,0,.2,1)`; carries a `>_` prompt glyph |
| **Secondary button** | fill `#f8f7f0`, 14px/600, `12px 20px`, radius 12px, transition `transform .15s, background-color .15s` |
| **Ghost (on dark)** | `rgba(255,255,255,.06)` fill, `1px rgba(255,255,255,.15–.2)` border, radius 12px, `8px 14px`, 14px/400 |
| **Chip, unselected** | fill `--card`, `1px --border`, `--muted-foreground`, radius 7.2px, `6px 14px`, 14px/400 |
| **Chip, selected** | fill `--brand-soft` `#e8cbb8`, `1px --brand` `#9a3f28`, text `--brand-ink` `#8f3f1f`, same geometry |
| **Provenance tag** | transparent fill, `1px` border = the ink hue at **25% alpha**, text = the ink hue, mono 10px/16px, `0.08em`, `1px 4px`, radius 7.2px, bracketed label |
| **Nav** | floating pill, hairline, over the hero |
| **Terminal** | navy body, forest header bar, mono 13px/1.625, uppercase mono tab labels at 10px/0.05em, a `$` prompt in `rgba(255,255,255,.6)` |
| **Announcement bar** | full-width on paper, mono 12px/18px, a `--brand` dot as the bullet |
| **Data counter** | mono 10px, `tabular-nums`, `--muted-foreground` |

---

## 6. Motion

Two eases, two jobs — measured, not assumed:

| Ease | Duration | Used for |
|---|---|---|
| `cubic-bezier(.4, 0, .2, 1)` | **0.15s** | every UI state change: colour, background, transform, opacity on controls |
| `cubic-bezier(.22, 1, .36, 1)` | **0.5s** | `.reveal` — `opacity` + `transform` on scroll entry |

Transitions are **scoped to named properties**, never `all`.

Authored keyframes:

| Name | What it does |
|---|---|
| `sym-verify` | a hero glyph sits at `opacity: var(--sym-op, .14)` in `currentColor`, then at 45–55% flips to `--verify` at 0.95 opacity |
| `sym-recall` | the same shape for the recall state |
| `verify-pulse` | `text-shadow: 0 → 0 0 20px var(--verify) → none` — a bloom, on the verify hue only |
| `glitch-fx` | chromatic split using **the two brand hues as the channels**: `text-shadow: ±2px 0 var(--verify), ∓2px 0 var(--brand)` with a ±2px translate |
| `gf-marquee` | `translateX(0 → -50%)` — the logo strip |
| `gf-copy-node` / `-ring` / `-label` | the copy-to-clipboard confirmation: a node flies to `var(--gf-dx)/var(--gf-dy)` and scales to 0.3 |
| `gf-tab-in` | the terminal tab swap |

**The reference's reduced-motion story is good** — every animated class has a
`@media (prefers-reduced-motion: reduce)` rule that sets
`animation: auto ease 0s 1 normal none running none`, and `.reveal` resolves to
`opacity: 1; transition: none; transform: none`. This is worth stating plainly:
unlike `orchard`'s reference, this one shipped the branch.

**The colour rule inside the motion:** the only hue that ever animates is
`--verify`. Nothing pulses in the brand rust; the rust is a static label. That
is what keeps "verified" reading as an event and "brand" reading as an identity.

---

## 7. What the pack keeps, changes, and drops

| Reference behaviour | Pack decision |
|---|---|
| Light paper + full dark twin | **keep both**, and set `color-scheme` per theme (the reference sets none) |
| Three unrelated dark families (brown `.dark`, forest bands, navy terminal) | **reconcile to one**: the forest family, because it is the hero's own gradient and the only one the page argues for. The terminal keeps a single darker step of that family, not a navy. |
| `--sidebar-*` warmer/browner than the page, `--sidebar-ring` violet | **drop the divergence**: the app layer inherits the page's green-cast neutrals and the brand ring |
| `--chart-5 #3b82f6` | **drop**: an unrelated blue in a five-series palette that otherwise runs rust→teal |
| Brand rust as the hero accent phrase | **change the value**: `#cf7a52` (the dark-mode brand), which passes AA on the gradient — see §8 |
| Proportional radius ramp from one `--radius` | keep, and ban hardcoded px |
| Ring-as-elevation, `.hairline` | keep, promote to a named token |
| `.eyebrow[data-n]` section numbering | keep — the signature motif |
| Crop marks | keep |
| Two eases | keep, name them |
| Reduced-motion coverage | keep and require |

---

## 8. Contrast — every pair, computed

WCAG 2.1 relative luminance, computed 2026-08-04.

### Light — the paper is safe

| Pair | Ratio | Verdict |
|---|---|---|
| `--foreground` on `--background` | **15.43:1** | AAA |
| `--foreground` on `--card` | 16.12:1 | AAA |
| `--foreground` on `--secondary` | 14.15:1 | AAA |
| `--foreground` on `--accent` | 13.70:1 | AAA |
| `--muted-foreground` on `--background` | **5.16:1** | AA |
| `--muted-foreground` on `--secondary` | 4.73:1 | AA |
| `--brand` on `--background` | 6.28:1 | AA |
| `--brand-ink` on `--background` | 6.75:1 | AA |
| `--brand-ink` on `--brand-soft` | 4.71:1 | AA |
| `--brand-foreground` on `--brand` | 6.16:1 | AA |
| `--verify-ink` on `--background` | 5.29:1 | AA |
| `--verify-ink` on `--verify-soft` | 4.76:1 | AA |
| `--witness` on `--background` | 5.31:1 | AA |
| `--witness-ink` on `--background` | 6.96:1 | AA |
| `--witness-ink` on `--witness-soft` | 5.78:1 | AA |
| `--witness-foreground` on `--witness` | 5.70:1 | AA |
| `--destructive` on `--background` | 4.76:1 | AA |
| **`--verify` on `--background`** | **3.17:1** | **fail** — large/fill only |
| **`--verify-foreground` (white) on `--verify`** | **3.40:1** | **fail** |
| `--border` on `--background` | 1.22:1 | n/a — a rule, not text |

### The hero — where it actually breaks

| Pair | Ratio | Verdict |
|---|---|---|
| white on `#062a22` (top) | 15.42:1 | AAA |
| white on `#124f3c` (60%) | 9.51:1 | AAA |
| white on `#4f8a68` (85%) | 4.06:1 | fail at body size |
| **`--brand` `#9a3f28` on `#062a22`** | **2.29:1** | **fail** |
| **`--brand` `#9a3f28` on `#124f3c`** | **1.41:1** | **fail badly** |
| `#cf7a52` (dark-mode brand) on `#062a22` | **4.82:1** | **AA — the fix** |

The most prominent text on the site — the accent phrase in the hero headline —
is the least legible thing on it. The fix costs one token and no design: use
the dark-mode brand on dark surfaces. The pack encodes this as
`--brand-on-dark`.

The 85% stop is the second trap: white body copy is fine at the top of the
gradient and fails by the time the gradient reaches `#4f8a68`. Content must end
before the dawn does.

### Dark — clean throughout

| Pair | Ratio | Verdict |
|---|---|---|
| `--foreground` on `--background` | 17.01:1 | AAA |
| `--foreground` on `--card` | 15.94:1 | AAA |
| `--muted-foreground` on `--background` | 7.12:1 | AAA |
| `--brand` on `--background` | 5.88:1 | AA |
| `--brand-foreground` on `--brand` | 5.88:1 | AA |
| `--verify` on `--background` | 8.25:1 | AAA |
| `--witness` on `--background` | 5.68:1 | AA |
| `--brand` on `--brand-soft` | 5.08:1 | AA |

---

## 9. Content architecture

Read off the rendered page, in order: hero → proof strip (stars · downloads ·
integrations, each tagged) → adopters → **how it works** (three numbered steps,
an assistant picker, a tabbed terminal) → the payoff (a rendered graph path) →
the graph viewer with numbered annotations → origin story → release list →
adopter quote + community-reported results → press list → CTA → the comparison
("graph, chunks, or grep") → what the report contains.

Three content rules the layout depends on, all of which belong in the pack
because a generated page will otherwise drop them:

1. **Every claim carries its source, inline.** Not a footnote — the number and
   the person are in the same block: *"71.5× fewer tokens — lucasrosati/claude-code-memory-setup"*.
2. **Section headings are claims, not labels.** "The answer is a path, not a
   vibe"; "Every edge says how it knows". (`briefing-room` already carries this
   rule for slides; here it applies to a scrolling page.)
3. **The page states what it does not have.** *"No press kit. Engineers found
   it, benchmarked it, and wrote it up themselves."* The absence is the proof.

---

## 9a. Responsive & remaining components (second capture, same day)

Measured after the pack contract widened to thirteen headings and demanded
`Components`, `Hero`, `Responsive` and `Signature element`.

### Breakpoints and fluid type

- Media queries in use: `max-width: 639px`, then `min-width` at `40rem`,
  `48rem`, `64rem`, `80rem`, `96rem`.
- **The page contains exactly one `clamp()`**:
  `clamp(0.8125rem, 0.2rem + 2vw, 2.125rem)` — 13px → 34px on a 2vw slope, used
  for a single figure caption. Everything else is fixed px stepping at the
  breakpoints. This pack is **not** fluid-scaled, and that separates it from
  `atrium`, whose whole scale is one `clamp()` band.

### Viewport units

- Hero: `min-height: 100svh`.
- Figures: `24svh`, `34svh`, `36svh`.
- `100dvh` appears only behind `@supports (height: 100dvh)`.
- `.h-screen` (`100vh`) exists in the generated utility layer but is not used on
  the page.

### Container queries

**None.** No `container-type` declaration and no `@container` rule anywhere in
the stylesheet set. Components size against the viewport and their own
`max-width`.

### Navigation

- Wrapper: `position: fixed; inset-x: 0; top: var(--bar-h); z-index: 50;`
  `height: 74px`, `pointer-events: none`, and
  `transition: top 300ms` — the nav **slides** when the announcement bar is
  dismissed.
- `--bar-h` measured at **38px** with the bar open.
- The pill: `pointer-events: auto`, `border-radius: 9999px`,
  `background: rgba(255,255,255,.05)`, `border: 1px rgba(255,255,255,.15)`,
  `height: 62px`, `padding: 8px 8px 8px 12px`, **`backdrop-filter: none`** —
  unlike `orchard`'s glass pill, this one is a plain translucent fill.

### Inputs

One form control on the page (the waitlist email, on the dawn):
`background: rgba(255,255,255,.05)`, `border: 1px rgba(255,255,255,.2)`,
`border-radius: 12px`, `padding: 0 12px`, `font-size: 16px` Geist, white text,
focus outline `1.5px` in the brand at 50% alpha. The 16px is the iOS
zoom-on-focus floor.

### What the reference does not answer

Recorded as gaps, not filled silently — the pack supplies a decision for each
and labels it as such:

| Gap | Evidence |
|---|---|
| **Loading idiom** | no skeleton, spinner or shimmer element on the page; `spin` and `pulse` keyframes exist in the generated utility layer and are unused |
| **Empty states** | none present — a marketing page has no empty state |
| **Disabled controls** | one `<button disabled>` found, rendering at `opacity: 1` with `cursor: default` — visually identical to an enabled control |
| **Authored state rules** | no `:hover` / `:active` / `:disabled` rules in the stylesheets; every state is a generated utility, so the transition values on the resting element are the only reliable source |

## 10. Open items

- `[AMBIGUOUS]` was not rendered at capture time; its mapping to
  `--witness-ink` is inferred from the token set, and the pack says so.
- The `opsz 12..96` and `wdth 75..100` axes of the display face are available
  and unused by the reference. The pack recommends `font-optical-sizing: auto`
  at hero sizes; that is a pack decision, not a measurement.
- The reference is a snapshot. Values are true as of 2026-08-04.
