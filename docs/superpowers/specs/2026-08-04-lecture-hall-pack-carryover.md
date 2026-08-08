# Carry-over ledger — `lecture-hall` style pack

> Append-only. Every stage writes here the moment something is deferred, dropped
> or left half-done. Read in full at stage 10. **Deferred out loud is forgotten.**

| # | Stage | Item | Why deferred | Owner / resolution |
|---|---|---|---|---|
| C1 | 0 | **The whole run, stages 1→10** | Three other live sessions share this repo (`local_63e3d6e0` duplicate graphify analysis, `local_f0f9de42` design-sync bridge, `local_5192bd2b` skills UX audit). Operator chose *hold everything* rather than race them to v1.5.0 across 8 shared files. | **Operator** — settle repo ownership, then restart against a clean tree on `feat/lecture-hall-pack`. |
| C2 | 0 | D5 — register positioning vs `instrument-console` and `workbench` | Genuinely a design call, and the stage-2 gate is manual by design. A proposal is recorded in the brief; it is not settled. | Stage 2 brainstorm gate. |
| C3 | 0 | Extraction incomplete below the fold | The grill needed enough to ground the pack, not the whole site. Missing: sections below the hero, focus-visible treatment, the spacing ramp, and **measured WCAG ratios for every colour pair**. | Stage 1, before the spec locks any contrast claim. `orchard.md` sets the bar: computed, never asserted. |
| C4 | 0 | Folding the design-sync bridge into one v1.5.0 | Operator selected it, then superseded it with *hold everything* once the third and fourth sessions surfaced. The bridge brief remains untracked on `main`. | Superseded by C1. Re-decide at restart. |
| C5 | 0 | `PUBLISH_NPMJS` secret not yet verified as armed | Stage 7 concern; the wiki records npm 2FA as the one step where releases strand (0.6.0 sat behind). Checking it at tag time is too late. | Stage 7, **before** `git tag`. |
| C6 | 0 | `docs/DOCMAP.md` not written | The pipeline's doc-inventory phase was not reached — the run held at the stage-0 gate first. | Stage 0 on restart. |
| C7 | 0 | Entry audit (`references/setup.md`) never offered | Offered-once row; the run held before it came up. | Stage 0 on restart — ask once, record a refusal. |
