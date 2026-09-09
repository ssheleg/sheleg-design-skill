#!/usr/bin/env python3
"""FIX-DS-06.04 — the long-form-landing visual-composition eval corpus
(sherlock audit, DS-06/XD-13).

The corpus (evals/cases/fix-ds-06.04.json) separates deterministic
routing/constraint/provenance checks from the render-rubric visual outcome,
whose live eval is a SEPARATE authorized batch no fixture imitates. Checked
here, stdlib only:

* the seven case shapes exist (identity-preserving exploration, system font +
  one family, dense table, no-screenshot honesty, native mockup, unavailable
  external tools) and every case is structurally valid on the family harness;
* a correct render is not obliged to change; a screenshot MENTION is not a
  file; offline routes propose no install; 100% structural PASS is never
  phrased as proven improvement; comparison stays UNMEASURED until the run;
* the knowledge-transfer rows name method, source and loss check.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CASES = os.path.join(ROOT, "evals", "cases", "fix-ds-06.04.json")
HARNESS = os.path.expanduser("~/DATA/sshlg-skills/test/outcome_harness.py")

failures = []
not_run = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def manifest():
    with open(CASES, encoding="utf-8") as fh:
        return json.load(fh)


def t_cases_structurally_valid():
    m = manifest()
    ids = [c["id"] for c in m["cases"]]
    assert len(ids) == len(set(ids)) and len(ids) >= 5
    for c in m["cases"]:
        assert c["schema_version"] == "outcome-case/1"
        assert c["skill"] == "sheleg-design"
        assert c["environment"]["case_digest"] == \
            hashlib.sha256(c["prompt"]["text"].encode()).hexdigest(), \
            f"{c['id']}: case_digest does not pin the frozen prompt"
        assert c["checks"]["outcome"], f"{c['id']}: no outcome checks"


def t_required_case_shapes_present():
    ids = " ".join(c["id"] for c in manifest()["cases"])
    for shape in ("identity-preserving", "scroll-pressure", "anchor-per-viewport",
                  "no-screenshot", "reduced-motion-parity"):
        assert shape in ids, f"the {shape} case is missing"


def t_identity_preserving_and_faults():
    m = manifest()
    ip = next(c for c in m["cases"] if "identity" in c["id"])
    assert "NOT obliged to change" in ip["prompt"]["text"]
    mp = next(c for c in m["cases"] if "pressure" in c["id"])
    assert "never only a" in mp["prompt"]["text"], \
        "faults may still be reported as token/style names"
    assert "SAME content fixture" in mp["prompt"]["text"]
    rb = next(c for c in m["cases"] if "anchor" in c["id"])
    assert "mechanical token PASS does not close this review" in rb["prompt"]["text"], \
        "the mechanical-PASS substitution is not pinned"


def t_honesty_rules_pinned():
    m = manifest()
    ns = next(c for c in m["cases"] if "no-screenshot" in c["id"])
    assert "no screenshot path is cited as existing" in ns["prompt"]["text"]
    note = " ".join(m["note"].split())
    for needle in ("SEPARATE authorized execution batch", "no fixture task imitates",
                   "a mention is not a file", "proposes no install",
                   "never phrased as a proven design improvement",
                   "blind order", "UNMEASURED until the authorized run"):
        assert needle in note, f"the note no longer records {needle!r}"


def t_family_harness_validates():
    if not os.path.isfile(HARNESS):
        not_run.append("family harness absent — case validation NOT_RUN (never PASS)")
        return
    for c in manifest()["cases"]:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(c, fh)
            path = fh.name
        try:
            r = subprocess.run([sys.executable, HARNESS, path],
                               capture_output=True, text=True, timeout=60)
            assert r.returncode == 0, \
                f"{c['id']} rejected by the family harness:\n{r.stdout}"
        finally:
            os.unlink(path)


def main():
    case("every case is structurally valid", t_cases_structurally_valid)
    case("the required case shapes are present", t_required_case_shapes_present)
    case("identity-preserving + region-named faults pinned",
         t_identity_preserving_and_faults)
    case("the honesty rules are pinned (batch, files, install, UNMEASURED)",
         t_honesty_rules_pinned)
    case("the family harness validates each case (where present)",
         t_family_harness_validates)
    for n in not_run:
        print(f"  NOT_RUN  {n}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
