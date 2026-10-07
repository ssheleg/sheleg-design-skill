# Slop markers — the visual floor

**Catalogue version: 2026-10-07.** Reviewed at every release, because the target
moves: the advice that cured last year's generated look is part of this year's
generated look (the "three default looks" below were themselves anti-slop advice
once). A marker is never edited into a different marker; a retired one keeps its
id and its row, marked `retired`, and ids are not reused.

## Contents

- What a marker is, and what it is not
- Who wins: the floor, the pack and the brief
- How a row is checked
- Color and surface
- Type
- Layout
- Icons and decoration
- Content
- Motion, the doctrine's forbidden forms included
- Mobile
- Platform
- Retired markers
- Sources

## What a marker is, and what it is not

A marker is a visual pattern that shows up whether or not the brief asked for
it, so a reader takes it as the model's default rather than the designer's
choice. Each row says what it looks like, **why** it reads that way, what a
designer does **instead**, how it is **checked**, and when it is **not** slop.
Markers are not style bans: every one has a stated exception, and the reason
column is what an argument about a marker has to answer.

**Severity** says how much one hit is worth:

| Severity | Meaning |
|---|---|
| **S1** | decides alone. One hit is a finding the surface ships with only under a recorded exception. The linter exits 1. |
| **S2** | a signal. Three S2 markers on one surface read as a default look and are a finding; one is a question. |
| **S3** | weak. It counts toward the S2 reading in sum and never decides alone. |

Copy has its own list. Generic hero lines, buzzwords and rhythm tells belong to
`copywriting`'s AI-tell pass; V034 only points there. This catalogue holds no
punctuation rule: in Russian the em dash is normative typography, not a tell.

## Who wins: the floor, the pack and the brief

- **The floor is always on**, `Style pack: none` included. Choosing no pack
  removes the pack's values, not this list.
- **A pack may tighten the floor, never loosen it.** A pack that bans glass
  outright is stricter than V003 and wins; a pack cannot declare V001 harmless.
  A pack's measured value that happens to sit on a marker (a cream field read
  off a live reference) is the marker's exception, and the pack document says
  where it was measured.
- **An explicit brief requirement beats a marker**, as it beats every baseline
  in [`SKILL.md`](./SKILL.md), but only once it is written down: the director
  record ([`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md), *The output the
  director owes*) carries it on its `Brief` or `Open` line, with the marker id.
  A requirement nobody recorded is the default talking.

## How a row is checked

The `check` column is `lint:<rule>` when the project linter has a rule for it,
and `review` when only an eye on a render can tell (the render critique in
[`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md) and
[`VISUAL_REVIEW.md`](./VISUAL_REVIEW.md)). Every `lint:` rule here has exactly
one implementation, and the repository's validator refuses a rule on one side
without the other.

```bash
npx sheleg-design-skill --lint <dir> [--json] [--ratchet <budget.json>] [--include-tests]
npx sheleg-design-skill --self-test
```

- It reads `html`, `css`, `scss`, `js`, `jsx`, `ts`, `tsx`, `vue`, `svelte` and
  `astro` files, skips `node_modules`, build output, hidden directories and
  minified bundles, and **skips tests** (`__tests__`, `test`, `tests`,
  `fixtures`, `*.test.*`, `*.spec.*`) unless `--include-tests` is given: a
  ratchet test that guards against a pattern has to contain it.
- Output is `file:line rule severity id snippet`; `--json` prints an array of
  `{id, rule, severity, file, line, snippet}`.
- **Exit 0** — no S1 finding and no ratchet overrun. **Exit 1** — an S1
  finding, or a file over its ratchet budget. **Exit 2** — a usage error. S2
  and S3 findings print and never change the exit code.
- **A recorded exception** is a comment on the line or the line above:
  `sheleg-lint-allow: V015 brand face, director record Brief line`. The id and
  a reason are both required; a bare id waives nothing. Waived findings are
  counted in the summary, not hidden.
- **Ratchet.** `budget.json` maps a file (relative to `<dir>`) to the number of
  findings it may carry; a file absent from it may carry none. A count above
  its budget exits 1, a count below it asks for the budget to be lowered, and
  the budget only ever falls. `lint:raw-color` runs only under `--ratchet`:
  without a budget, a legacy tree prints hundreds of S3 lines that tell nobody
  anything; with one, a file may only lose them. A missing budget file exits 2
  and prints today's counts to start from.
- **A copied pack token layer** (the file carries the pack's `SHELEG Design — …
  token layer` header) holds the pack's measured values. Its token definitions
  are not reported, and a face it names first is a declared choice for
  `lint:default-font`; what the project writes around them is still read.
- The rules are pattern matches, not a renderer. They read class strings, CSS
  declarations and JSX data; they do not compute what a cascade resolves to.
  `review` rows exist because of that limit, and three lint rules carry a known
  one: `lint:decorative-blur` sees a `fixed` or `sticky` ancestor only within two
  lines, `lint:reveal-everywhere` counts per file, and `lint:default-font` reads
  an email template's system stack like any other (waive it there).

## Color and surface

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V001 | color | S1 | A gradient through violet, purple, fuchsia or indigo, most often indigo into violet into pink. | It is the averaged palette of years of component kits, so it reads as nobody having chosen. | One accent taken from the product's world; a gradient only as a specific effect with a reason. | `lint:purple-gradient` | The brand's own recorded gradient. | [ap], [blog] |
| V002 | color | S1 | Gradient-filled text, usually on the hero heading or a metric. | An effect stands in for hierarchy, and contrast becomes unmeasurable along the gradient. | Emphasis from weight, size and contrast between faces, in a solid colour. | `lint:gradient-text` | A logotype drawn that way. | [ap], [cf] |
| V003 | color | S2 | Frosted glass and `backdrop-blur` on cards and panels that float over nothing in particular. | Blur without a layer beneath it to separate is decoration that costs contrast. | Glass only where it separates navigation or an overlay from scrolling content. | `lint:decorative-blur` | A sticky bar, sheet, dialog, menu or popover over moving content. | [cf], [lg] |
| V004 | color | S2 | A coloured glow with no offset around buttons or cards, typically on a dark page. | A halo has no light source, so it is ornament posing as depth. | Elevation from an offset shadow with a soft blur, or from a lighter surface on dark. | `lint:glow` | A focus ring or a glow that is the product's own signal (a live state). | [ap], [cf] |
| V005 | color | S1 | A thick coloured stripe down one side of a card, alert or list item (`border-l-4`). | It is the single most repeated card treatment in generated UI. | Carry the state in the surface, an icon or the text; a 1px rule if a rule at all. | `lint:side-stripe` | A blockquote rule; a 2px tree or timeline guide (not flagged). | [ap], [cf] |
| V006 | color | S2 | A hairline grid drawn with stacked `linear-gradient` layers behind a hero or a whole page. | Texture with nothing under it borrows the look of a drawing without the drawing. | A plain surface; a grid only where real content sits on it (a canvas, a plan, a chart). | `lint:grid-background` | A product whose subject is a grid or a sheet. | [ap], [ts] |
| V007 | color | S3 | Repeating diagonal or straight stripes as surface decoration. | Same as V006, in a coarser weave. | A plain surface or a texture taken from the subject. | `lint:stripes` | A hazard or an indeterminate-progress state that means something. | [ap] |
| V008 | color | S2 | Grey text sitting on a saturated coloured background. | Neutral grey on colour looks washed out and often fails contrast. | Tint the secondary text from the background hue, then measure it. | `lint:gray-on-color` | None for body text; check the ratio either way. | [cf] |
| V009 | color | S2 | Body copy in a light grey that fails 4.5:1. | Low-contrast grey is the generated idea of "subtle", and it is the most common failure on the web. | Muted text that still clears the ratio, measured on the real background. | `review` | None. | [cf], [ae] |
| V010 | color | S3 | One radius and one soft grey shadow on every container (`rounded-2xl shadow-lg` on everything). | A depth system with one value is not a system; nothing is above anything. | Declare elevation once, radius by hierarchy, a child radius no larger than its parent. | `lint:uniform-card-chrome` | A pack whose measured reference really does this. | [fd41], [ap] |
| V011 | color | S3 | Palette classes and hex literals written into components instead of tokens. | Every literal is a decision taken outside the system, and they drift. | Read the pack's tokens; a new colour becomes a token first. | `lint:raw-color` | Token definitions themselves. | [cl] |
| V012 | color | S2 | Default look one: a warm cream field near `#F4F1EA`, a high-contrast serif display and a terracotta accent. | It is where generated design lands when nothing pushes it elsewhere. | Values from a pack extracted off a live reference; if the result sits here, say so. | `review` | A pack measured off a reference that is this (several are). | [fd16] |
| V013 | color | S2 | Default look two: a near-black field with a single acid-green or vermilion accent. | Same reason as V012: it arrives regardless of subject. | As V012. | `review` | A pack measured off a reference that is this. | [fd16] |
| V014 | color | S3 | Pure `#000` as a field, or a reflex tinted near-black (`#0B0B0B`, `#111`) standing in for a choice. | Both are habits rather than a neutral chosen for the scene of use. | Neutrals derived from the palette's hue and from where the product is used. | `review` | A pack's measured field. | [fd41], [ap] |

## Type

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V015 | type | S2 | Inter, Roboto, Arial or the system stack as the face actually shown, with no declared reason. | The default face is the clearest sign that no type decision was made. | A face chosen for the subject; one family or two that differ clearly; a set scale. | `lint:default-font` | A brand face, a face a pack's token layer names, or a deliberate system stack for product UI, recorded. | [ap], [blog], [fd41] |
| V016 | type | S3 | A timid scale: 400 against 600, steps under 1.25x, hierarchy by size alone. | Without contrast between roles there is no hierarchy to read. | Fewer roles with stronger steps; weight and colour carry rank as well as size. | `review` | Dense product UI where the pack sets the steps. | [ap] |
| V017 | type | S3 | One word of the headline in another colour, italic or weight. | It is the commonest generated typographic flourish. | Let the heading carry its own weight. | `review` | A product name or a term the reader must find. | [fd41] |
| V018 | type | S3 | A small tracked ALL-CAPS label (eyebrow, kicker, chip) above every heading. | Repeated chrome that encodes nothing about the content. | Delete it; keep a label only where it carries information the heading does not. | `review` | A label that does carry information, used once. | [ap], [cf], [fd41] |
| V019 | type | S3 | Monospace for mood: small data labels and captions set in mono to look technical. | Mono as a costume rather than for code, data or measurement. | Mono only where characters must align or be copied exactly. | `review` | A pack whose measured reference sets UI in mono. | [cf], [fd41] |
| V020 | type | S3 | Body text running the full width of a wide screen. | An unmeasured line is hard to read and shows the layout was not set. | A measure in `ch`, roughly 45 to 80 characters for body text. | `review` | Tables and code. | [fd41] |

## Layout

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V021 | layout | S2 | A centred hero with one CTA over three equal cards, each an icon in a rounded square, a heading and two lines. | It is the canonical generated landing page, independent of the product. | Open with the most characteristic thing in the product's world; let the content decide the structure. | `review` | A brief that names this structure. | [ap], [cf], [fd41] |
| V022 | layout | S2 | The hero-metric template: a big number, a small label, supporting stats, a gradient accent. | It is the default answer to "show traction". | Use it only when that number is the best opening this product has. | `review` | A product whose job is the number. | [cf], [fd41] |
| V023 | layout | S2 | Cards nested inside cards. | Container inside container adds borders and depth with no new information. | Group with space, type and dividers; one container level. | `review` | A nested surface that is a real object (a message preview inside a thread). | [ap], [cf] |
| V024 | layout | S3 | A bento grid chosen before the content, with cells that do not differ. | A safe template that hides how much content there is. | As many cells as there are things to show, sized by what they hold. | `review` | Content that really is a set of unequal tiles. | [ts] |
| V025 | layout | S3 | Section numbers 01 / 02 / 03 on content that is not a sequence. | Numbering claims an order the reader cannot use. | Number only steps and timelines. | `review` | A real sequence. | [cf], [fd41], [ts] |
| V026 | layout | S2 | Default look three: broadsheet hairline rules, zero radius, dense newspaper columns. | Same reason as V012 and V013. | As V012. | `review` | A pack measured off a reference that is this. | [fd16] |

## Icons and decoration

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V027 | icon-decor | S1 | Emoji standing in for icons, in markup or in data (`icon: "📊"` in a list rendered as cards). | An emoji set has no common stroke, weight or alignment and renders differently per platform. | One icon library or drawn SVG with one stroke and weight; SF Symbols on iOS. | `lint:emoji-icon` | Emoji that are the content (a reaction picker, a chat message). | [cf] |
| V028 | icon-decor | S2 | ✨ or a sparkles icon marking the "AI" feature. | The whole category uses the same glyph, so it says "generated" rather than what the feature does. | Name what the feature does; an icon for that action. | `lint:sparkles` | A brand whose mark it is. | [cf] |
| V029 | icon-decor | S3 | Coloured or pulsing dots before nav items, rows and badges. | Simulated liveness with no live data behind it. | A dot only for a state that is real and changes. | `review` | Real status (a server, availability). | [ap], [ts] |
| V030 | icon-decor | S3 | Sparklines, progress rings and soft rectangles filling space where content should be. | Imitation data is decoration that pretends to be information. | Real data, or nothing. | `review` | None. | [cf] |
| V031 | icon-decor | S3 | A component kit in its starter look: default radius, default icon set, default face. | The kit's defaults are everybody's defaults. | Map the kit to the pack on every axis ([`COMPONENT_LAYER.md`](./COMPONENT_LAYER.md)). | `review` | None. | [cl] |
| V032 | icon-decor | S3 | Template chrome: meta strings joined by middle dots (A · B · C), an arrow appended to every link and button. | Chrome that appears on any subject is not part of this one. | Separators and arrows only where they help the reader. | `review` | A single meta line; an arrow that means "leaves the page". | [fd41], [ts] |

## Content

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V033 | content | S1 | Invented proof: stat rows, customer logos and testimonials nobody supplied. | A fabricated claim on a public surface is untrue, not just generic. | Numbers and names from supplied truth; illustrative values labelled as such. | `review` | A prototype where every such value is visibly marked as sample. | [ap], [ts] |
| V034 | content | S2 | Generic hero copy that describes the product to itself. | The words are as templated as the layout. | Hand it to `copywriting`; its AI-tell pass owns the word list. | `review` | None here; the copy pass decides. | [fd41] |
| V035 | content | S2 | A fake product screen in the hero, built from styled divs. | A drawing of a product is not evidence of one. | A real screenshot, a real component, or nothing. | `review` | A product that does not exist yet, labelled as a concept. | [ts] |
| V036 | content | S2 | Happy-path content: perfect lengths, lorem-like text, every table exactly full. | It hides the states the surface has to survive. | Real copy at every breakpoint; long, empty and error states designed. | `review` | None. | [cf] |

## Motion, the doctrine's forbidden forms included

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V037 | motion | S2 | The same fade-and-rise entrance on every section as it scrolls in. | Scattered identical effects are the generated default; nothing is authored. | One orchestrated moment; everything else already visible. | `lint:reveal-everywhere` | A deck or story whose sections are the steps. | [cf], [fd41] |
| V038 | motion | S1 | Bounce, elastic or overshoot curves: `cubic-bezier` control points outside 0 to 1, `back` and `elastic` eases, springs with heavy bounce. | Real objects decelerate; overshoot on a settings panel reads as dated and toy-like. | Ease-out curves and critically damped springs ([`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md)). | `lint:bounce-easing` | Bounce 0.1 to 0.3 after a flick or drag release only. | [an], [md] |
| V039 | motion | S1 | `transition: all`. | It animates whatever changes next, layout included, and nobody chose it. | Name the properties. | `lint:transition-all` | None. | [md], [ra] |
| V040 | motion | S1 | Animating a property that triggers layout: width, height, top, left, margin, padding, gap, font size. | Every frame re-lays the document out, and it stutters. | Transform and opacity; clip-path inside a measured budget. | `lint:layout-transition` | None. | [md], [ap] |
| V041 | motion | S1 | Entering from `scale(0)`. | Nothing real appears from a point. | Enter from about `scale(0.95)` with opacity. | `lint:scale-zero` | None. | [md], [ra] |
| V042 | motion | S1 | `ease-in` on UI, entrances and exits alike. | It starts slow at the exact moment the user is watching for a response. | Ease-out for anything entering or responding. | `lint:ease-in` | None in UI. | [md] |
| V043 | motion | S1 | Animation with no `prefers-reduced-motion` path anywhere in the project. | Motion that cannot be turned off is a defect for the people it harms. | Every animation beyond a colour change has a reduced branch. | `lint:no-reduced-motion` | A project whose only motion is a loading spinner. | [md], [cf] |
| V044 | motion | S3 | Perpetual decoration: a marquee of logos, a blinking cursor in a hero that takes no input. | Motion that asks for attention it has not earned. | Motion that answers a person or shows a change. | `review` | One marquee carrying content. | [ap], [md] |

## Mobile

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V045 | mobile | S2 | Glass and blur on the content layer of a native screen. | The platform reserves translucent material for controls and navigation above content. | Glass on the navigation layer only; content stays opaque. | `review` | None. | [lg], [ms] |
| V046 | mobile | S2 | A hand-built bottom bar that clips under the home indicator, or fields that sit under the keyboard. | Off-spec controls make a fluent user hesitate. | The platform's tab bar and safe areas; the primary action stays above the keyboard. | `review` | None. | [ms], [ios] |
| V047 | mobile | S2 | Fixed type sizes that ignore the user's text size. | It breaks the setting the user chose. | Dynamic Type on iOS, `sp` and font scale on Android, relative units on the web. | `review` | None. | [ms], [ios] |
| V048 | mobile | S2 | A web page squeezed onto a phone: hover affordances, web buttons, custom navigation. | It reads as a port, not an app. | The platform's navigation and controls ([`MOBILE_SURFACES.md`](./MOBILE_SURFACES.md)). | `review` | A mobile web view that is honestly a web view. | [ms], [ios] |

## Platform

| id | group | severity | tell | why | instead | check | exception | source |
|---|---|---|---|---|---|---|---|---|
| V049 | platform | S2 | One platform dressed in the other's uniform: a floating action button and ripple on iOS, iOS chrome on Android. | Users trust controls that behave like the rest of their phone. | Each platform's own components and conventions. | `review` | A cross-platform brand component the brief records. | [ms], [ios] |

## Retired markers

None yet. A retired marker keeps its row here with `retired` in the severity
column and the date it left.

## Sources

Paraphrased, not copied: no source text is carried into this file. Repository
sources are pinned to the commit read on 2026-10-07 and carry provenance rows
17–20 (with rows 2, 11, 15 and 16) in
[`KNOWLEDGE_PROVENANCE.md`](./KNOWLEDGE_PROVENANCE.md); impeccable is
Apache-2.0, taste-skill and emilkowalski/skills are MIT, anthropics/skills is
Apache-2.0.

[ap]: https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/crates/live/assets/antipatterns.json
[cf]: https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/craft-floor.md
[an]: https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/animate.md
[ios]: https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/ios.md
[ts]: https://github.com/Leonxlnx/taste-skill/blob/e3c92037548e3e49bea8e6b906c99a8549654e71/skills/taste-skill/SKILL.md
[ra]: https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/STANDARDS.md
[fd16]: https://github.com/anthropics/skills/blob/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design/SKILL.md
[fd41]: https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/frontend-design/SKILL.md
[blog]: https://claude.com/blog/improving-frontend-design-through-skills "read 2026-10-07"
[lg]: https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass "read 2026-10-07"
[md]: ./MOTION_DOCTRINE.md
[ms]: ./MOBILE_SURFACES.md
[cl]: ./COMPONENT_LAYER.md
[ae]: ./ACCESSIBILITY_EVIDENCE.md
