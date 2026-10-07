# Render eval — what a surface built under the skill contains

The trigger and scenario evals in `test/evals/` measure whether `sheleg-design`
is picked and what plan it produces. This one measures the artifact: four fixed
briefs, rendered, then counted against the visual floor, the director record and
the source-decidable G items of `ADA_RUBRIC.md`.

| File | Holds |
|---|---|
| `briefs.json` | the four briefs — landing hero with motion, mobile onboarding screen, product dashboard, paywall — with surface class, prompt, falsifier and states |
| `run.js` | the runner: linter + record validator + G items per brief; `--write` appends one dated row to `test/evals/RESULTS.md` |
| `sample/` | hand-written stand-ins with known contents, so CI can watch the runner work |

## A model run, by hand

The generation step is **not run in CI** — it needs a model session and is made
by hand, the same way the trigger probes were:

1. For each brief, open a **fresh** session in an empty directory with the skill
   installed (record which other skills are installed: they change routing).
2. Send the brief's `prompt` verbatim. Let it write into
   `<outputs-dir>/<brief id>/`, including `director-record.md`.
3. Run `node evals/render/run.js <outputs-dir> --model <model id> --note "<what else was installed>" --write`.
4. Keep the outputs out of the repository; the row and its method carry the result.

```bash
node evals/render/run.js evals/render/sample          # the harness on the sample
node test/render_eval_test.js                         # the counts it must report
```

A row is comparable with an earlier one only while `briefs.json` is
byte-identical. A changed brief starts a new series.
