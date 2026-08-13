# Acceptance — 2026-08-10 bundle self-sufficiency (v1.11.0)

Closed at `89a8798`, tagged `v1.11.0`, released and published.
Audit that produced it: a repeat pass over the skill, run as **application**
scenarios in fresh contexts rather than routing questions.

## What the run was for

The v1.10.0 acceptance ended with an instruction for its successor:

> The pattern to check next time is not a file — it is whether the last run's
> findings were swept across siblings, or fixed only where they surfaced.

Checked, and the answer is **both**. The literal form was swept clean: zero
repo-only paths remain in the bundle, measured. The *class* was not — the same
defect had two more shapes that are not paths, and both were live in production.

## Ladder walk

Each REQ walked bottom-up — decision → spec → contract and its failure behaviour
→ task → change → executed test → surface/docs. **Every absence became a row
before this table was written.** Three did, all created by this change, and none
of them visible to any gate:

| Found on the ladder | Seam | Became |
|---|---|---|
| `README.md` said "four-way version sync" after the version gained a fifth home | change → surface | fixed in `89a8798`+1; the count now names the fifth and why it exists |
| `CONTRIBUTING.md`'s release step named three files to bump, not four plus the bundle | change → surface | fixed; and the four authoring rules now say the shipped template is their home, so one rule does not live in two places |
| `README.md`'s bundled-reference table did not list `SURFACE_COMPOSITION.md` | change → docs | fixed; a file that ships and is not listed is a file no reader knows to open |

The seam these three share is worth naming: **`validate_counted_claims()` derives
counts from directories, so it sees "twelve packs" and cannot see "four-way
version sync".** A count of a *concept* has no directory to count. That is the
gap the ladder walk exists to cover, and it covered it three times in one run.

## Coverage

Carry-over counts printed beside every verdict: **8 of 21 scenarios still carry
no recorded result** (down from 13 of 19), **3 REQ rows at `never`** in the
verification ledger, **9 board rows open** — B-001…B-006 carried in, plus B-007
and B-008 filed by this run's own scenario agents and B-009 by its refused graph
refresh.

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 the bundle carries its own version | **green** · 0 carried | `metadata.version` in front-matter; version sync ×5; planted removal caught with its own message |
| REQ-02 the spine is named, not just counted | **green** · 0 | `DESIGN_SYNC_BRIDGE.md` §1 names all six; planted removal of one caught |
| REQ-03 pack-authoring rules reach an installed author | **green** · 0 | four rules in `styles/STYLE_PACK_TEMPLATE.md`, which ships; `CONTRIBUTING.md` demoted to a pointer |
| REQ-04 the class is gated | **green** · 0 | `validate_bundle_self_sufficiency()`, three forms, each watched failing **and discriminated by its own message** |
| REQ-05 the hook contradiction is resolved | **green** · 0 | `SHELEG_DESIGN.md` §9 uses `useGSAP`; the two remaining `useLayoutEffect` mentions are the ban and its history |
| REQ-06 unmeasured constants declared | **green** · 0 | `arcAmp` and `drop` named as tuning constants with the record-your-value rule; nothing invented |
| REQ-07 entry point under budget | **green** · 0 | `make-skill-audit --house`: **0 GAP, 11 PASS**; 6157 → **4856** tokens |
| REQ-08 today's scenario results recorded | **carried** · → B-005 | 6 recorded with the tree they ran against; 8 of 21 still unrecorded |
| REQ-09 gates green, floors raised | **green** · 0 | 1385 / 469 / 332; `floors.json` names the branch that measured them |
| REQ-10 CI runs every gate | **green** · 0 | scripts diffed against `validate.yml`; every gate present, no workflow change needed — noted rather than assumed |
| REQ-11 released and verified by artifact | **green** · 0 | npm serves 1.11.0; **tarball unpacked**: 388 files, 32 in the bundle, version present, spine named, 0 repo-only paths |
| REQ-12 local installs refreshed | **green** · 0 | plugin and hub both at 1.11.0; one-channel invariant prints nothing |
| REQ-13 docs and wiki | **green** · 0 | doc map, README, CONTRIBUTING, wiki all updated in this run |
| REQ-14 board and ledger closed | **green** · 0 | 9 open rows, priorities re-derived; B-007, B-008 and B-009 filed by this run |

| REQ-15 the code graph | **carried** · → B-009 | **the refresh was refused and the refusal was right.** The incremental re-extraction produced 1652 nodes against 1703 on disk, and the shrink-guard declined to overwrite. Investigated rather than forced: only 52 of the 168 lost nodes were `.cursor`-mirror duplicates; the rest were real content the new pass modelled more coarsely — a node per historical release in `CHANGELOG.md` among them. Forcing would have deleted the record of four releases to gain one. `graph.json` stays at 1703 nodes, `built_at_commit` `9312a85`, two commits behind HEAD, and says so |
## Gates

| Gate | Before | After |
|---|---|---|
| `validate.py` | 1368 | **1385** |
| `validate_palette.py` | 469 | **469** |
| `sloplint.py` | 320 | **332** |

The palette gate is unchanged because this run touched no colour. Recorded as a
flat number rather than quietly omitted: a gate that did not move is evidence
about scope, not an oversight.

## The one loosening, named

The front-matter budget split raises the total ceiling from 1024 to 1280. It is
a loosening. The reasoning — 1024 is the spec's limit on `description` alone, so
one cap over the whole block was stricter than the standard it claimed to
implement — is in the code, the CHANGELOG and here, because a gate that gets
more permissive during the run that needed it to is exactly the move that
deserves three witnesses.

## What a re-run should look at first

The three shipped forms are now gated. **A fourth instance of the class has to be
a new shape**, so the question for the next run is not "are there repo paths in
the bundle" — that is answered by a machine now — but: *what else does the bundle
tell a reader to do with something it does not contain?* The two found this time
were a version and a list. The next one will not look like either.
