# Sample outputs — a harness check, not a model run

These four directories are hand-written stand-ins for what a model run leaves
behind, one per brief in `../briefs.json`. They exist so the runner can be
watched working in CI: each carries known contents, and
`test/render_eval_test.js` asserts the counts the runner reports for them.

| Directory | Planted on purpose |
|---|---|
| `landing-hero-motion` | nothing: tokens only, a reduced-motion branch, a valid flagship record |
| `mobile-onboarding` | a violet gradient, an emoji icon, motion with no reduced-motion branch, no record |
| `product-dashboard` | a raw hex and a raw palette class outside the tokens (R8), a valid product record |
| `paywall` | a record whose taste profile is only "modern, clean" |

No number from this directory measures a model. A model's outputs go in a
directory of their own, with the run's method (`../README.md`).
