---
surface: paywall
surface_class: flagship
revision: sample
---

## Brief

Surface: landing / hero
Job: a freelance translator sees that the tool bills by segment and starts a project
Constraint: the paper-and-ink token layer
Falsifier: a first-time visitor cannot say what the product does after five seconds

## Mode

new — entered at references, then style

## Taste

Take: modern, clean, minimal
Ban: outdated

## References

- Toggl Track — https://toggl.com/track/ — take: the timer as the hero object
- Harvest — https://www.getharvest.com/ — take: the invoice shown beside the timer
- Clockify — https://clockify.me/ — take: one primary action above the fold
- Smartcat — https://www.smartcat.com/ — take: segments as the unit of work
- Phrase — https://phrase.com/ — take: the editor itself as the illustration

## Cast

- sheleg-design — direction, tokens, critique (style, critique)
Roster read from the harness list, not measured.

## Fork

no — the brief names one direction and the token layer is fixed

## Rubric

- the call to action is reachable without scrolling at 1280×800
- the type scale renders at most five sizes
- the counting motion stops under reduced motion

## Critique

clean render — no observable defect at 375 or 1280

## Markers

npx sheleg-design-skill --lint evals/render/sample/landing-hero-motion @ 0000000 — 0 S1, 0 S2, 0 S3, 0 waived

## Alignment

Falsifier checked at 1280×800: the segment list and the headline say "billed per segment" in the first screen.

## Quality

| Check | Result |
|---|---|
| Contrast | ink on paper 15.2:1 |
| Motion | one 200 ms transition, removed under reduced motion |

## Signature

What: the segment counter ticks as each line is translated
Where: the hero's segment list
Why: the product's unit of work is the segment

## Surfaces

none needed — a marketing page; the product's own surfaces are out of scope

## Haptics

n/a — web surface with no haptic engine

## ADA

Profile: flagship
Targets: Interaction, Visuals and Graphics
G: 3 PASS / 0 FAIL / 13 N/A
J: NOT_ASSESSED — no labelled set yet

## Open

Whether the counter runs on load or only on hover.
