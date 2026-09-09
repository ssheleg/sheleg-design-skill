#!/usr/bin/env python3
"""FIX-VD-06.01 — dials become preference hints; the contract is observable
anchors (sherlock audit, VD-06/XD-07).

The finding: numeric dials rode through several stages as a ritual — density 5
was never tied to any reproducible visual quality, and identity-preserving
redesigns auto-raised motion.

The fix under test (SKILL.md + SHELEG_DESIGN.md):
* the primary contract is observable targets (reading width, CTA
  reachability, visible alternatives, keyboard state, empty-space purpose);
* dials are optional shorthand / preference hints; a number without anchors
  is not evidence; each value carries an example/counterexample or derives
  from the accepted direction;
* the same digit does not equalise a quiet dashboard, a consumer chat and an
  accessibility-large-text surface;
* identity-preserving redesign no longer auto-raises MOTION;
* the explicit user requirement beats the baseline/style floor; the token
  contract stays invariant while composition stays open;
* the anchors rule run as behaviour.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                     "SKILL.md")
SD = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                  "SHELEG_DESIGN.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def flat(path):
    with open(path, encoding="utf-8") as fh:
        return " ".join(fh.read().split())


def t_anchors_are_the_contract():
    d = flat(SKILL)
    assert "The primary contract is a set of OBSERVABLE TARGETS" in d
    for anchor in ("reading width", "CTA", "alternatives", "keyboard state",
                   "empty space"):
        assert anchor in d, f"the {anchor} anchor is missing"
    assert "a number without its anchors is not evidence" in d


def t_dials_are_hints_with_examples():
    d = flat(SKILL)
    assert "optional shorthand" in d and "preference hints, not measurements of quality" in d
    assert "an example or a counterexample" in d
    assert "a digit pinned before anything exists binds nothing" in d


def t_same_digit_different_tasks():
    d = flat(SKILL)
    assert "The same digit does not equalise different platform tasks" in d
    for surface in ("quiet dashboard", "consumer chat", "accessibility-large-text"):
        assert surface in d, f"the {surface} example is missing"


def t_identity_redesign_no_motion_raise():
    d = flat(SKILL)
    assert "| redesign, preserve the existing identity | match | match | match |" in d, \
        "the identity-preserving row still auto-raises motion"
    assert "match +1" not in d.split("redesign, preserve")[1].split("|", 8)[0] + "", \
        "a +1 survived in the identity row"


def t_user_beats_floor_and_tokens_invariant():
    d = flat(SKILL)
    assert "an explicit user requirement beats the baseline and any style floor" in d
    assert "The token contract stays invariant" in d
    assert "composition within it is an open choice" in d


def t_sheleg_design_enriched():
    d = flat(SD)
    assert "Calibrating by anchors, not by digits" in d
    assert "A digit with no example/counterexample beside it is a ritual" in d


# ---- behaviour: is a calibration claim evidence?


def is_evidence(claim):
    if claim.get("anchors"):
        return True
    if claim.get("derived_from_direction"):
        return True
    return False


def t_bare_number_is_not_evidence():
    assert not is_evidence({"density": 5}), "a bare digit counted as evidence"
    assert is_evidence({"density": 5, "anchors": ["reading width 68ch",
                                                    "3 alternatives visible"]})
    assert is_evidence({"density": 5, "derived_from_direction": "accepted render v2"})


def main():
    case("observable targets are the primary contract", t_anchors_are_the_contract)
    case("dials are hints with example/counterexample", t_dials_are_hints_with_examples)
    case("the same digit does not equalise three platform tasks",
         t_same_digit_different_tasks)
    case("identity-preserving redesign no longer auto-raises motion",
         t_identity_redesign_no_motion_raise)
    case("user requirement beats the floor; tokens invariant, composition open",
         t_user_beats_floor_and_tokens_invariant)
    case("SHELEG_DESIGN.md carries the external-method section",
         t_sheleg_design_enriched)
    case("fixture: a bare number is not evidence; anchored or derived is",
         t_bare_number_is_not_evidence)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
