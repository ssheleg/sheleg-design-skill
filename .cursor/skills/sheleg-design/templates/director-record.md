---
surface: <name of the surface, e.g. pricing-page>
surface_class: <flagship | product | internal | ad>
revision: <commit or date this record describes>
---

# Director record — <surface>

<!--
HOW TO USE THIS TEMPLATE
Copy it to the product repository as docs/design/<surface>/director-record.md
and fill it BEFORE the first render: the record is where the decisions live, and
the generator reads it as context. Everything inside an HTML comment is guidance
and counts as empty, so a copied template fails the validator until it is filled:

  npx sheleg-design-skill --check-record docs/design/<surface>/director-record.md

Exit 0 valid, 1 with the list of missing or empty fields, 2 usage error.

Which fields a class owes (the validator enforces this):
  flagship  every field below; ADA scored on the flagship profile (ADA_RUBRIC.md)
  product   Brief, Mode, References, Markers, Open
  internal  Brief, Mode, Markers, Open
  ad        Brief, Mode, Taste, References, Markers, Signature, ADA (ad profile), Open
A field a class does not owe may stay empty; once filled, its rule applies.

Declining design work ("no design") is a record too: write `declined` and the
reason under Mode, and nothing else is required.
-->

## Brief

<!--
Four labelled lines, each filled. The falsifier is what would prove the design
failed, stated so that it could actually happen.
  Surface: landing / hero, product UI, mobile screen, agent interface, deck-as-page
  Job: what the person who lands here must be able to do, in their words
  Constraint: the thing that is not negotiable
  Falsifier: e.g. "a first-time visitor cannot say what this does after five seconds"
  Scenario: <id from docs/ux/scenarios.md, where a scenario base exists>
A brief that explicitly asks for a marked pattern (SLOP_MARKERS.md) names the
marker id here or under Open.
-->

## Mode

<!--
One word first: new | redesign | update | audit | declined
then where you entered, e.g. "redesign — entered at verify + visual-qa".
Declined: "declined — <the reason, in a sentence>".
-->

## Taste

<!--
The taste profile for THIS surface: what we take and what we ban, in words a
second reader can check against the render. "modern", "clean", "minimal" and
"sleek" on their own are read as empty: every product claims them, so they
decide nothing. Name materials, references, type, rhythm, the subject's own
vernacular.
  Take: e.g. "ledger-paper rhythm from the subject; tabular figures; one warm accent"
  Ban: e.g. "violet gradients; three equal feature cards; stock 3D blobs"
  Anti-patterns: optional — SLOP_MARKERS ids this surface is most at risk of
  Dials: optional — VARIANCE / MOTION / DENSITY with one anchor each (SKILL.md, Calibration)
  Profile: optional — the standing taste profile this was read from, if any
-->

## References

<!--
At least five real products, each with its URL and what we take from it — the
structural trait, not its palette. One line each:
  - <Product> — https://… — take: <the trait>
Or, when the sweep came back empty, say so and say where you looked:
  none found
  Searched: <the reference servers and queries, e.g. Refero "pricing table", Lazyweb "usage-based pricing">
Mandatory for new design and redesign of a brand or flagship surface.
-->

## Cast

<!--
Each skill or tool, what it is for, and the lane it serves — one line each.
Say whether the roster was measured (`npx sshlg-skills pack design`) or read
from the harness list.
-->

## Fork

<!--
Start with yes or no.
  no — <why: the brief already determines the answer, a locked system, a fix>
  yes — rubric below written before either direction; then
    A: <cast / direction>
    B: <cast / direction>
    Winner: <A or B> — grafted from the other: <the trait>
-->

## Rubric

<!--
Three to five criteria, written before any direction exists and not touched
afterwards. Each one checkable by someone who built neither variation, with its
anchor:
  - the primary action is reachable without scrolling at 1280×800
  - the type scale renders at most five distinct sizes
-->

## Critique

<!--
Render critique as triples, one per line: region → defect → change.
  - hero headline, top-left 0–480px → wraps to four lines at 375px → shorten to the job, set the measure
A clean render is a valid result: write "clean render" and stop. No defect quota.
-->

## Markers

<!--
The `--lint` run this record stands on: the command, the revision it ran at and
the counts by severity, copied from its summary line.
  npx sheleg-design-skill --lint src @ 3f2a9c1 — 0 S1, 2 S2, 1 S3, 1 waived
Each waived marker: its id and the Brief or Open line that earned it. An S1
finding blocks — fix it, or waive it in source with `sheleg-lint-allow: V0NN <reason>`.
-->

## Alignment

<!--
The falsifier, checked out loud, and the result. Where scenarios exist, the
/ux-audit result that checked the surface against them.
-->

## Quality

<!--
The measurable table from CREATIVE_DIRECTOR.md Act 5, with numbers: contrast
ratios, type sizes counted, durations measured, NOT_APPLICABLE with its reason.
-->

## Signature

<!--
Exactly one signature moment for the flow — what it is, where it happens, and
why it comes from the subject rather than from a catalogue.
  What: <the moment>
  Where: <screen / state / transition>
  Why: <how the subject produces it>
-->

## Surfaces

<!--
Where the job also lives outside the app or page — widget, Live Activity, App
Intent, Watch, PWA install, share card — or why none is needed.
-->

## Haptics

<!--
Native only: a table of event → pattern, each pattern used for its documented
meaning and switchable off. Otherwise "n/a — <reason, e.g. web surface>".
-->

## ADA

<!--
Scored on ADA_RUBRIC.md. flagship: profile, target categories and the verdict
by type; every G item PASS, at most two J FAIL with the reason recorded; J items
are NOT_ASSESSED until a labelled set exists.
  Profile: flagship
  Targets: Interaction, Inclusivity
  G: 15 PASS / 0 FAIL / 2 N/A
  J: NOT_ASSESSED — no labelled set yet
  H: contact sheet reviewed by <who>, <date>
  FAIL triples: region → defect → change
ad: the same lines on the ad profile, plus "Safe zones: <placement and result>".
Any other class: "n/a — <reason>".
-->

## Open

<!--
What a person still has to decide. Not an admission of failure: every real
design job has something left to decide.
-->
