# Evaluations for sheleg-design

These files describe behavior to measure with the pack installed. They are not
unit tests and CI does not pretend that schema validity is model quality.

| File | Holds |
|---|---|
| `triggers.json` | positive requests and close negative cases, split before tuning |
| `scenarios.json` | three end-to-end behaviors scored line by line |
| `RESULTS.md` | dated model runs, or an explicit statement that none exist |

Validate the data and the validator's planted defect:

```bash
python3 test/evals_validate.py
python3 test/evals_validate.py --self-test
```

To measure triggers, ask each query in a fresh session three times and record
whether the intended skill loaded. To measure scenarios, record each expected
line as pass or fail. Always record the model, pack version and other installed
skills; coexistence changes routing.

## Outcome corpus — the arm that judges artifacts

`scenarios.json` and `triggers.json` test that the right skill NAME is
picked, which proves nothing about whether running it helped. The outcome
corpus at `evals/cases/sheleg-design.json` (contract: `outcome-case/1` in
`ssheleg/sshlg-skills` — `schemas/outcome-case.schema.json` +
`test/outcome_harness.py`) judges ARTIFACTS instead, with with/without-skill
arms; probe-gated cases (a browser for computed styles) go NOT_RUN where the
tool is unavailable — measured degradation, never PASS.
`test/audit_regressions/fix-ev-01.14.py` keeps the corpus honest.
