#!/usr/bin/env python3
"""FIX-EV-01.14 — the outcome corpus for sheleg-design (sherlock audit,
parent FIX-EV-01; depends on the family harness of FIX-EV-01.01).

The corpus (evals/cases/sheleg-design.json) holds a positive (adapter
audit), a negative (routing), a single-verdict motion case (DS-04), an
exact-Figma no-op case (VD-01: no composition exploration) and a
browser-gated computed-style case (DS-06) — judged on ARTIFACTS through the
family's outcome-case contract, so sheleg-design can no longer pass an eval
by its name being picked.

Checked here, stdlib only: structural validity with prompt-pinned digests;
the negative forbids loading; the motion verdict is singular with a rule id;
the no-op pins "variations: none"; the browser case is probe-gated (NOT_RUN,
never a silent skip); the family harness validates each case where present.
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
CASES = os.path.join(ROOT, "evals", "cases", "sheleg-design.json")
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


def t_cases_are_structurally_valid():
    m = manifest()
    ids = [c["id"] for c in m["cases"]]
    assert len(ids) == len(set(ids)) and len(ids) >= 5
    for c in m["cases"]:
        assert c["schema_version"] == "outcome-case/1"
        assert c["skill"] == "sheleg-design"
        assert c["environment"]["case_digest"] == \
            hashlib.sha256(c["prompt"]["text"].encode()).hexdigest(), \
            f"{c['id']}: case_digest does not pin the frozen prompt"
        assert c["checks"]["outcome"], \
            f"{c['id']}: no outcome checks — the name-picking eval again"


def t_negative_forbids_loading():
    neg = next(c for c in manifest()["cases"] if "negative" in c["id"])
    assert "sheleg-design" in neg["checks"]["load_trace"]["expect_not_loaded"]
    assert not neg["checks"]["load_trace"]["expect_loaded"]


def t_motion_verdict_is_singular_with_rule_id():
    c = next(x for x in manifest()["cases"] if "one-verdict" in x["id"])
    kinds = {o["kind"] for o in c["checks"]["outcome"]}
    assert "artifact-contains" in kinds and "command-exit-0" in kinds
    single = next(o for o in c["checks"]["outcome"] if o["kind"] == "command-exit-0")
    assert "grep -c 'verdict:'" in single["target"] and "= 1" in single["target"], \
        "the singularity oracle does not count verdicts"


def t_noop_pins_no_exploration():
    c = next(x for x in manifest()["cases"] if "noop-exact-figma" in x["id"])
    assert any(o.get("expect") == "variations: none" for o in c["checks"]["outcome"]), \
        "the exact-Figma case does not pin that no variations were created"


def t_browser_case_is_probe_gated():
    c = next(x for x in manifest()["cases"] if "computed-style" in x["id"])
    probe = c["checks"]["tool"][0]["command"]
    assert "command -v" in probe, "the browser case has no probe — it cannot NOT_RUN"
    flat = " ".join(json.dumps(manifest(), ensure_ascii=False).split())
    for needle in ("actual output oracle", "raw result", "with/without-skill",
                   "NOT_RUN", "measured degradation", "grader convenience"):
        assert needle in flat, f"the manifest no longer records {needle!r}"


def t_family_harness_validates_each_case_where_present():
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
    case("every case is structurally valid, none is name-picking",
         t_cases_are_structurally_valid)
    case("the negative case forbids the skill from loading", t_negative_forbids_loading)
    case("the motion verdict is singular and names its rule",
         t_motion_verdict_is_singular_with_rule_id)
    case("the exact-Figma no-op pins 'variations: none'", t_noop_pins_no_exploration)
    case("the browser case is probe-gated and the manifest records the rules",
         t_browser_case_is_probe_gated)
    case("the family harness validates each case (where present)",
         t_family_harness_validates_each_case_where_present)
    for n in not_run:
        print(f"  NOT_RUN  {n}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
