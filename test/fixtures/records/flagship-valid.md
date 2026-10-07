---
surface: invoice-onboarding
surface_class: flagship
revision: 3f2a9c1
---

# Director record — invoice-onboarding

## Brief

Surface: mobile screen — first run of an invoicing app
Job: send the first invoice to a real client within two minutes of install
Constraint: the brand teal, the gradient wordmark (V002, brand-owned) and the type pair already in the token layer
Falsifier: a first-time user cannot reach "send" without opening the settings screen
Scenario: SCN-014

## Mode

new — entered at references, then style

## Taste

Take: paper-ledger rhythm from the subject; tabular figures on every amount; one warm accent on the send action
Ban: violet gradients; three equal feature cards; stock 3D illustrations of coins
Anti-patterns: V001, V012, V035
Dials: VARIANCE 5 (like the pack's own form screens) / MOTION 3 / DENSITY 5

## References

- Stripe Invoicing — https://stripe.com/invoicing — take: the line-item table that totals as you type
- Wave — https://www.waveapps.com/invoicing — take: the client picker before any item is added
- Square Invoices — https://squareup.com/us/en/invoices — take: the preview that sits beside the form, not after it
- FreshBooks — https://www.freshbooks.com/invoice — take: one primary action per step
- Xero — https://www.xero.com/us/accounting-software/send-invoices/ — take: due date chosen from relative presets

## Cast

- sheleg-design — direction, tokens, critique (style, critique)
- frontend-design — concept hypotheses inside the fixed palette (style)
- webapp-testing — screenshots at 375 and 768 (visual-qa)
- a11y-debugging — contrast and label pass (a11y)
Roster measured with `npx sshlg-skills pack design`.

## Fork

yes — the rubric below was written before either direction existed.
A: workbench pack + MOTION_DOCTRINE (form-first, preview below)
B: frontend-design concept, preview beside the form
Winner: B — grafted from A: the tabular amount column and its quieter motion

## Rubric

- "send" is reachable without scrolling at 375×667
- the type scale renders at most five distinct sizes
- every amount uses tabular figures
- the preview updates within one frame of an edit

## Critique

- line-item table, rows 2–4 → amounts misalign by 2px between rows → set tabular-nums on the amount cell
- send button, bottom 64px → competes with the "save draft" link of equal weight → demote the link to text style

## Markers

npx sheleg-design-skill --lint src @ 3f2a9c1 — 0 S1, 2 S2, 1 S3, 1 waived
V002 waived: the brand wordmark gradient, named in Brief constraint.

## Alignment

Falsifier checked on the build at 375×667: "send" is reached in four taps, settings never opened — the falsifier is false.

## Quality

| Check | Result |
|---|---|
| Contrast | body 7.1:1, secondary 4.8:1 |
| Type scale | 5 sizes rendered |
| Motion | 2 transitions, 160 ms and 200 ms; reduced motion turned on and verified |

## Signature

What: the paper invoice folds into the envelope as it is sent
Where: send confirmation, the single transition after "send"
Why: an invoice is a paper document the subject still names as one

## Surfaces

Widget for "awaiting payment" totals; App Intent "send invoice to <client>". Live Activity not needed: payment is not a timed event.

## Haptics

| Event | Pattern |
|---|---|
| invoice sent | success notification |
| amount field error | error notification |

## ADA

Profile: flagship
Targets: Interaction, Inclusivity
G: 15 PASS / 0 FAIL / 2 N/A
J: NOT_ASSESSED — no labelled set yet
H: contact sheet reviewed by the product owner, 2026-10-07

## Open

Whether the envelope fold plays every time or only on the first invoice.
