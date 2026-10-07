---
surface_class: internal
---

## Brief

Surface: internal admin — the job queue
Job: find a stuck job and retry it
Constraint: the existing admin shell
Falsifier: a stuck job is not distinguishable from a running one without opening it

## Mode

audit — a11y, verify, visual-qa, speed

## Markers

npx sheleg-design-skill --lint admin @ 0c1d2e3 — 0 S1, 1 S2, 0 S3, 0 waived

## Open

Nothing on visuals; the retry policy is a backend decision.
