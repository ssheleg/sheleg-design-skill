# Babylove — seven tokens, and the other end of the same question

Origin: <https://www.babylovegrowth.ai/en> and its `/dashboard/overview`, read
2026-08-21 in a logged-in Chrome session. Every value below was measured off the
served pages with `getComputedStyle`.

Contract: widened
Themes: light only — the reference ships one field and no dark block, and this pack does not invent one.
Rank: none — `--brand`'s six steps are a ramp of one hue, not a severity ladder.

**Read this pack against `outrank`, because the pair is the argument.** Both are
2026 SEO-and-AI-visibility products with a landing and a dashboard. `outrank`
answers *"how much system do you need"* with **536 custom properties across two
borrowed design systems** — daisyUI on the marketing site, Semrush's Intergalactic
in the product. This one answers it with **seven**: `--brand` and six steps of it,
with every grey taken from Tailwind v4's defaults and nothing else declared at all.

Neither is wrong. The pair exists so a team can see the two ends of the choice
priced, and the price is legible in both directions: `outrank` gets a semantic
vocabulary and inherits somebody else's upgrade path; this gets a system a person
holds in their head and no answer at all for a second theme.

## Register

Plain, warm, unhurried. The product is patient with itself — it ships a *What to
expect* block that says results arrive over months 1–3, 3–6 and 6–12 — and the
visual language matches: one hue, no shadows, no gradients, nothing that hurries.

Motion ceiling: **2**. Measured — the entire site's budget is a 0.15s colour
transition. No scroll clock, no parallax, no scrub, no reveal.

## Palette

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--ink` | `#171717` | the headline and body | 17.93:1 |
| `--ink-data` | `#101828` | every number | 17.75:1 |
| `--ink-soft` | `#4A5565` | card titles, captions | 7.56:1 |
| `--ink-faint` | `#6A7282` | the rail's section labels — **corrected** | 4.84:1 |
| `--brand` | `#FA5C12` | fills, bars, rings, the accent word at display size | 3.18:1 |
| `--brand-ink` | `#B73F06` | the brand when it carries a word | 5.63:1 |
| `--action` | `#0F0A0A` | every primary button | 19.66:1 |
| `--good` / `--warn` | `#027A48` / `#B54708` | the status chip's ink | 5.41:1 / 5.43:1 |

- **The brand orange may not carry a word, in either direction.** `--brand` is
  3.18:1 on the page and white on it is 3.18:1 — it clears the 3:1 floor for a
  graphical object and clears nothing for text. The reference knows this and its
  hero CTA is **near-black at 19.66:1**; the one place it breaks its own rule is
  the nav button, white on `#F25533` at **3.43:1**. Use `--brand-ink` for a word.
- **One correction, and the value came from the framework rather than from me.**
  The rail's section labels are set in Tailwind's gray-400 `#99A1AF` at 11px —
  **2.60:1 on `--bg` and 2.49:1 on the inner card**. `#6A7282` is gray-500, the
  next step down the same ramp and the nearest that clears 4.5 on both.
- `--brand-dark` `#D8410A` is **4.49:1** — one hundredth short of AA. It is kept
  because the reference declares it, and it is not the token to set text in.
- **Status is never by colour alone, and `--live` is why the rule is written here
  rather than assumed.** At 2.62:1 it is under even the 3:1 floor for a graphical
  object — it is the dot inside a `● Live` pill whose **word** carries the state.
  The same holds for `--good` and `--warn`: they are the chip's ink beside a
  label, never the label's replacement.

## Type

Two families, split by how long a thing is read: **Raleway** for the marketing
display, **Plus Jakarta Sans** for everything else including the product.

- Hero — Plus Jakarta Sans **600, 76px / 76px leading**, tracking normal, centred.
  **The leading equals the size** — on a headline, not only on a metric — which is
  what makes the hero read as a block rather than as lines.
- Lede — **20px / 28px at weight 300**. The light weight is the pack's, and it is
  what keeps a 20px lede from competing with a 76px headline.
- Page title — 24px / 32px, weight 600.
- Metric — 30px / 30px, weight **700**, `--ink-data`. Leading equals size again.
- Card title — 14px / 20px, weight 500, `--ink-soft`.
- Rail label — 11px, weight 700, **0.55px tracking**, uppercase, `--ink-faint`.

## Texture & surface

- **Two card levels, and their radii differ on purpose.** The section card is
  `--r-outer` 16px on `--surface` with a 1px `--hairline-soft`; the card inside it
  is `--r-inner` 8px on `--surface-2` with a 1px `--hairline`. The nesting is the
  layout: a section owns a subject and each inner card owns one figure of it.
- **No shadows.** Measured across the dashboard: one `0 1px 6px rgba(0,0,0,.06)`
  in the entire surface, and nothing else. Separation is a border and a tint.
- **The rail has no border at all.** 272px of whitespace does the separating,
  which is the one place this pack is quieter than every other in the library.
- The landing field carries a **faint pixel-grid with scattered small glyphs** —
  a page texture at very low contrast, never a component's.

## Components

| Component | Resting | Hover | Active | Disabled |
|---|---|---|---|---|
| **Primary button** | `--action` fill with `--on-action` on it, `--r-control`, `12px 32px`, 16px/600 — the pair's ratio is in the Palette, where its two tokens sit on one line | fill lightens one step | `scale(0.98)` | `--surface-3` fill, and `--ink-faint` on `--surface-3` is 4.39:1 |
| **Section card** | `--surface`, 1px `--hairline-soft`, `--r-outer`, `16px` padding, no shadow, an ⓘ beside the title and an ↗ at the right | unchanged | n/a | n/a |
| **Inner card** | `--surface-2`, 1px `--hairline`, `--r-inner`, `12px` padding | unchanged | n/a | n/a |
| **Status chip** | tinted `--r-pill`, 12px/600, `0 4px`, ink in `--good` or `--warn` | n/a | n/a | n/a |
| **Nav row** | `--ink` label, icon left | `--surface-2` fill | `--surface-3` fill **plus a 3px `--brand` bar on the left edge** | `--ink-faint`, no fill |
| **Score ring** | a donut in `--good` with the figure centred, beside its sub-scores | n/a | n/a | renders `—` and the reason |
| **Empty states** | two kinds, and the pack distinguishes them. A **disconnected** source renders at full size with an icon, one sentence naming what connecting buys, and a button — the signature element below. A genuinely **empty** collection renders `--surface-2` at `--r-inner` with one line naming what is not there, and no illustration | unchanged | n/a | n/a |
| **Loader** | **none.** The reference shows a `Running analysis` chip on the card that is working and leaves every other surface drawn. There is no skeleton anywhere | | | |
| **Input** | **not specified.** The reference's forms were not read in this pass, and a pack that invented them would be inventing values with a citation attached | | | |

## Hero

A centred marketing hero: floating nav, a 76px headline in two lines where the
**second line carries the accent phrase in `--brand`**, a two-line lede at weight
300, one black CTA, a refund guarantee in one line under it, and a Trustpilot chip.

- **Line ceiling: two**, at 76px and leading 1.0 — measured off the served page.
- **One CTA, and it is black.** Unlike `outrank`'s two-door hero this page offers a
  single action. The guarantee sentence under the button — *"if organic traffic
  doesn't grow within 90 days, we refund you in full"* — is doing the work the
  second door does elsewhere: it removes the risk instead of removing a password.

## Responsive

- **Breakpoints** 640 / 768 / 1024 / 1280px — Tailwind's own, unchanged.
- **Container queries** for the inner cards: `container-type: inline-size`, because
  an inner card's width depends on how many siblings its section card holds, not on
  the viewport.
- The rail collapses below 1024; the two-level card nesting flattens to one level
  below 768, because two borders and two tints inside 375px is noise.

## Motion tokens

- Ease `cubic-bezier(0.4, 0, 0.2, 1)` — Tailwind's default, and the one curve.
- `--dur-press` 0.15s, `--dur-fast` 0.15s, `--dur-base` 0.2s. All three inside
  `MOTION_DOCTRINE.md` §3's bands, and all three collapse under reduce.
- **Nothing else moves.** Measured over a 13 089px landing and the dashboard.

## Signature motifs

1. **Leading equal to size**, on the headline and on the metric alike.
2. **The card inside the card**, at 16px and 8px, tinted one step apart.
3. **The left brand bar** on the active nav row — 3px, and the only place the
   orange touches navigation.
4. **The composite score decomposed in place** — a donut beside three sub-scores,
   each with its own `/100` and a bar.
5. **The metric priced in money** — *80K potential reach* answered by *$641 to buy
   this visibility via Ads*.

## Signature element

**The disconnected state, treated as a first-class surface.** Where a data source
is not connected the card renders at full size with an illustration, one sentence
naming what connecting buys, and a button — *"Connect Google Search Console to
track your search performance and rankings"*. It occupies exactly the space the
data would, so the dashboard's shape does not change when a source is added, and a
new account reads as unfinished rather than as broken.

## Motion flavor

Not applicable — this pack has no cinematic layer, and the ceiling of 2 is the
whole story. The one animated thing in the product is a `Running analysis` chip.

## Micro-interactions

- Button press: `scale(0.98)` over `--dur-press`.
- Nav row: `--surface-2` on hover, `--surface-3` plus the 3px brand bar when active.
- **The working card says so on itself.** A card whose data is being computed wears
  a `Running analysis` chip; the rest of the screen stays drawn. The status is on
  the thing that is working, not over the page.
- `focus-visible`: 2px `--action` ring at 2px offset. Not the brand orange, which
  is 3.18:1 and cannot carry an affordance on white.

## Bans

- **No shadow.** Separation is a border and a tint. One 6px shadow exists in the
  whole product and it is not yours to add to.
- **No word in `--brand`.** 3.18:1 in both directions. `--brand-ink` carries text.
- **No second hue.** One orange, six steps, and Tailwind's greys.
- **No skeleton.** A card that is working says so on itself; the rest stays drawn.
- **No dark theme.** The reference ships one field. Inventing a twin here would be
  inventing thirty values with a citation attached.
- **No scroll-driven motion.** Ceiling 2, budget one colour transition.

## Gotchas

- **[CORRECTION] The reference has no `prefers-reduced-motion` branch.** Its budget
  is a 0.15s transition, so the omission costs a reader little — this pack requires
  the branch anyway, and collapsing three durations costs the design nothing.
- **The nav CTA fails AA and the hero CTA does not.** White on `#F25533` is
  **3.43:1**; the hero's near-black is 19.66:1. The site made the right call once
  and the wrong one once, in the same viewport. Use `--action`.
- **The rail's section labels are 2.60:1 as shipped.** Corrected to `#6A7282`,
  which is the framework's own next step rather than a value from me.
- **`--brand-dark` is 4.49:1 — one hundredth under AA.** Kept because the reference
  declares it; not the token to set a word in. `--brand-ink` is.
- **Two oranges are painted, not one.** `--brand` is `#FA5C12` in the declared
  token and the nav button paints `#F25533`. Neither is wrong on its own; a pack
  that copied only the painted one would ship a brand hue the site does not declare.
- **The landing is 13 089px** — about two thirds of `outrank`'s. Same category,
  same job, and a page a third shorter, which is worth knowing before treating
  either length as a target.
