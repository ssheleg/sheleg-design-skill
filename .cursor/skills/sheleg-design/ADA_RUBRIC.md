# ADA rubric — 25 binary checks for a surface that has to be award-grade

**This rubric is derived. Apple does not publish one.** Apple publishes six
Apple Design Awards categories, one sentence of criteria for each, and the
reasons it gave its winners. The 25 items below are this pack's reading of those
criteria and of what the 2024–2026 winners were named for, turned into binary
properties a second reader can check. Passing them does not mean Apple would
agree, and nothing here speaks for Apple. The pages it was read from, with the
date of the reading, are under [Sources](#sources).

Load it when the director record's `surface_class` is `flagship` or `ad`
([`templates/director-record.md`](./templates/director-record.md)), and from
Act 5 of [`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md), where the measurable
half of a review is decided. A product surface takes only its gate items.

## Contents

- How to read an item
- The 25 items
- Profiles and thresholds
- The judge — how a J item gets a verdict anyone can trust
- Every FAIL is a triple
- What the rubric cannot do
- Sources

## How to read an item

Each item is binary: **PASS**, **FAIL**, or **N/A** with the reason it does not
apply. Two more verdicts exist and are never a PASS in disguise: **NOT_RUN** (the
check needs a tool that was not available — a simulator, a browser) and
**NOT_ASSESSED** (a judged item before the judge has been calibrated, below).

| Type | Who decides | Can anything outvote it? |
|---|---|---|
| **G** | a deterministic check: a test, a linter, an audit, a count | no — a G-FAIL blocks, whatever the judge or the reviewer thinks of the render |
| **J** | a multimodal judge working from a per-task checklist | the human on the contact sheet |
| **H** | the human, once, on the contact sheet | — |

An item typed **G+J** or **G+H** has two halves: the deterministic half gates on
its own, the other half is judged or reviewed. A profile that takes "only G items"
takes the G half of a mixed item and leaves the rest.

**Applies to:** **i** iOS, **a** Android, **w** web, **ad** an ad or static
creative. "all" is all four.

## The 25 items

| # | Category | Item (binary) | How to verify (tool → artifact) | Type | Applies |
|---|---|---|---|---|---|
| R1 | Interaction | The scenario's main task completes with no dead end, and every error has a way out | an end-to-end run of the scenario (Playwright, XCUITest, a Compose test) → the run log | G | i a w |
| R2 | Interaction | At most one onboarding screen before the first value, or the director record says why | screens counted in the flow → the contact sheet's first-run row | G+H | i a w |
| R3 | Interaction | Navigation and controls are the platform's own: tab bar, stack, sheet; edge-swipe back works; no floating action button on iOS | an XCUITest swipe-back; a search for custom tab bars; a comparison with 2–3 shipped references from the sweep | G+J | i a |
| R4 | Interaction | An action answers within 100 ms, and animations can be interrupted | web: INP under 200 ms in a performance trace; iOS: Instruments hitches; Android: a Macrobenchmark frame-timing metric | G | i a w |
| R5 | Interaction | The keyboard never covers the primary action; keyboard type and autofill are right | the `keyboard-up` cell of the axes matrix ([`MOBILE_SURFACES.md`](./MOBILE_SURFACES.md)) | G | i a |
| R6 | Interaction | Every haptic event in the record's event → pattern table uses the pattern for its documented meaning, and haptics can be switched off | a search for the haptic calls against the record's `Haptics` table | G+J | i a |
| R7 | Visuals | One theme, drawn from the subject, written down before generation; the screen is recognisable without its logo | the record's `Taste` and `Brief` → a judge working from the brief; `--lint` clean of S1 | J+H | all |
| R8 | Visuals | No raw hex or px outside the token layer | `npx sheleg-design-skill --lint <dir> --ratchet <budget>` (the `raw-color` rule), a strict-value stylelint, Tailwind's no-arbitrary-value rule, Figma `get_variable_defs` | G | all |
| R9 | Visuals | The type scale renders at most six or seven sizes; system text styles or Dynamic Type; tabular figures for data | a histogram of computed `font-size` in the browser, or a search for fixed system sizes in Swift | G | all |
| R10 | Visuals | The custom motion carries meaning (a state change, data arriving), and its durations sit in the doctrine's bands | the frame strip and run video from the motion review ([`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md) §12) → a judge; the `DUR-*` table | J | i a w ad |
| R11 | Visuals | Images, illustrations and charts were made for this product, not taken from stock | each asset's provenance record (where, how and under what licence it was made) → a judge | G+J | all |
| R12 | Visuals | Dark mode and Increased Contrast are designed views, not an inversion | the theme axis of the matrix; contrast measured in every theme | G | i a w |
| R13 | Visuals | Optical finish: concentric radii, safe areas respected, nothing clipped or overlapped | a clipped-text accessibility audit; an occlusion check; the render critique's triples | G+J | all |
| R14 | Inclusivity | Contrast at least 4.5:1, large text at least 3:1, in every theme | axe `color-contrast`; an XCUITest contrast audit; Android's accessibility checks | G | all |
| R15 | Inclusivity | The largest text size (iOS AX5, web 200% and a 320px reflow) clips nothing and loses no function | the simulator's content size at its accessibility maximum with a Dynamic Type and clipping audit; Compose `fontScale`; browser zoom | G | i a w |
| R16 | Inclusivity | Every element has a meaningful label and trait, reading order is logical, and one manual VoiceOver or TalkBack pass is recorded | the element-description, trait and element-detection audits; axe; the recorded pass | G+H | i a w |
| R17 | Inclusivity | Touch targets: 44pt on iOS, 48dp on Android, 24px on the web | a hit-region audit; Android's touch-target check; axe `target-size` | G | i a w |
| R18 | Inclusivity | Colour is never the only signal (Differentiate Without Color) | a grayscale capture → a judge; the setting turned on in the matrix | J | all |
| R19 | Inclusivity | A double-length pseudolocale and RTL break nothing; at least two real locales if the product promises them | the platform pseudolocales (Xcode double-length and RTL, Android `en-XA` and `ar-XB`, a web pseudolocale) → the locale columns of the matrix | G | i a w |
| R20 | Inclusivity | Reduce Motion and Reduce Transparency are honoured | captures and video with the setting on; `prefers-reduced-motion` turned on, not read from the CSS | G | i a w |
| R21 | Delight | Exactly one signature moment per flow, named in the record and visible on the contact sheet | the record's `Signature` field → a judge: "the moment is there / there is more than one" | J+H | all |
| R22 | Delight | The text is in the brand's voice, with no AI tells | the family's `copywriting` skill and its brand linter where installed; NOT_RUN where absent | G | all |
| R23 | Delight | The empty state and the first run are designed: a next step, never a bare "No data" | the `empty` row of the matrix → a judge | G+J | i a w |
| R24 | Innovation | The job is taken where it lives — widget, Live Activity, App Intent, Watch — or the record says why not | the record's `Surfaces` field; captures of the widget families | G | i a |
| R25 | Social impact | Every element traces to the person's job; no dark pattern; errors and offline are honest | the alignment check of Act 5 ([`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md)) and the `error` and `offline` rows of the matrix | J+H | all |

**R3, R6, R15 and R24 name Apple's platform.** On Android and the web they mean
their equivalents — Material navigation, WCAG reflow and zoom, an installable PWA
and the system share target. The rubric never makes an Android screen look like
iOS: dressing one platform in the other's uniform is itself a defect
([`SLOP_MARKERS.md`](./SLOP_MARKERS.md), Platform).

## Profiles and thresholds

The record's `surface_class` picks the profile. The validator
(`npx sheleg-design-skill --check-record`) holds the `ADA` field to it.

| Profile | Items | Threshold |
|---|---|---|
| **flagship** — landing, onboarding, paywall, a product's main screen, store creatives | all 25 | every G item PASS; at most **two** J items FAIL, each with its reason written in the record; every H item reviewed on the contact sheet |
| **product** — the other screens of a product | the G items only: R1, R3–R5, R8, R9, R12–R17, R19, R20, R22 (the G half of R3, R13 and R16) | every one PASS |
| **ad** — a story, a feed creative, a banner | R7, R8, R10, R11, R14, R18, R21, R22, plus the placement's safe zones | every G item PASS and the safe zones clear; J items as for flagship |
| **internal** | none — the linter and a functional look | — |

**A J item is NOT_ASSESSED until the judge is calibrated** (next section). Until
then the flagship threshold reads "every G item PASS, J NOT_ASSESSED", and the
record says so rather than reporting a PASS nobody measured.

In the director record the verdict is four lines:

```
Profile: flagship
Targets: Interaction, Inclusivity
G: 15 PASS / 0 FAIL / 2 N/A
J: NOT_ASSESSED — no labelled set yet
```

plus `H:` (who reviewed the contact sheet, when), `Labelled set:` once J items
are scored, `Safe zones:` on the ad profile, and a triple for every FAIL.

## The judge — how a J item gets a verdict anyone can trust

A judge is useful only as far as its agreement with people has been measured.
These rules come from the papers and practice listed under Sources; each one is
there because the alternative was measured to be worse.

1. **A checklist written for this task, not a score.** The judge answers the J
   items as yes/no questions about this surface, anchored to the brief and the
   record. A 1–10 "quality" score is not a verdict.
2. **Pairwise only against an approved reference, and in both orders.** The
   judge compares the candidate with an approved baseline or reference, once as
   A/B and once as B/A. Only a verdict that survives the swap counts.
3. **Three samples.** Each J item is asked three times, independently.
   Disagreement between the samples is **`uncertain`** — neither PASS nor FAIL —
   and goes to the human as its own row on the contact sheet.
4. **NOT_ASSESSED until a labelled set exists.** Before a judge's J verdicts
   count, 20–30 screens carry a human verdict and the judge's agreement with them
   is measured; the agreement threshold is the owner's decision. The family's
   `agent-evals` skill covers the measuring. No labelled set, no J PASS.
5. **The judge looks at what runs.** It gets the axes matrix and a run video,
   not one frame.
6. **The judge sits below the floor.** It never turns a G-FAIL into a PASS, and
   never outvotes an S1 finding of `--lint`. The strict constraints gate before
   the soft winner ([`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md), render
   critique).
7. **The generator is not the judge.** The agent that rendered the surface does
   not score it: self-review was measured to praise its own output and to talk
   itself out of real issues. A separate agent, or a separate pass with no
   access to the generator's reasoning, judges.

## Every FAIL is a triple

A FAIL without a place to look is an opinion. Each one is written as
**region → defect → change**, the same triple as the render critique:

```
paywall, plan cards 0–390px → the selected plan is marked by colour alone (R18) → add a check glyph and a "Selected" label
```

A clean render is a valid result. The rubric has no quota: an item that passes
passes, and the judge does not invent a third finding to fill a slot.

## What the rubric cannot do

- **It does not make a surface good.** It removes the reasons a surface could
  not be good — the same limit Act 5 states about the quality table. Taste is
  still the person's call on the contact sheet.
- **Platform evidence stays native.** A web render dressed as a phone proves
  nothing about Dynamic Type, VoiceOver or a sheet's detents
  ([`VISUAL_REVIEW.md`](./VISUAL_REVIEW.md)); a native item without a simulator or
  a device is NOT_RUN.
- **The rubric can steer toward its own slop.** Every item is a property to
  check, never an adjective to aim at; R7 and R21 are tied to the brief so that
  "distinctive" cannot be met by decoration.

## Sources

Read on 2026-10-07. The category criteria are quoted from Apple's pages; the
items are this pack's derivation and are not Apple's.

- Apple Developer, *Apple Design Awards* — the six categories and their
  one-sentence criteria (Delight and Fun, Inclusivity, Innovation, Interaction,
  Social Impact, Visuals and Graphics):
  https://developer.apple.com/design/awards/ (read 2026-10-07)
- Apple Developer, *2025 winners and finalists*:
  https://developer.apple.com/design/awards/2025/ (read 2026-10-07)
- Apple Developer, *2024 winners and finalists*, which also carried a Spatial
  Computing category: https://developer.apple.com/design/awards/2024/ (read 2026-10-07)
- Apple Newsroom, *Apple reveals winners of the 2026 Apple Design Awards*:
  https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/ (read 2026-10-07)
- The judge rules: ArtifactsBench, per-task checklists and temporal screenshots,
  https://arxiv.org/abs/2507.04952; MLLM-as-a-Judge, pair comparison against
  scoring, https://arxiv.org/abs/2402.04788; Anthropic, *Harness design for
  long-running application development*, on separate skeptical evaluators and
  self-praise, https://www.anthropic.com/engineering/harness-design-long-running-apps
  (all read 2026-10-07).

The derivation, the date and what it informed are recorded in
[`KNOWLEDGE_PROVENANCE.md`](./KNOWLEDGE_PROVENANCE.md).
