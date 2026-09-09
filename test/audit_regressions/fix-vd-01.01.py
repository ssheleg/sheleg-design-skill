#!/usr/bin/env python3
"""FIX-VD-01.01 — the invariant/open-axis split (sherlock audit, VD-01).

The finding: a preserve-the-brand brief collapsed into one direction — the
brand lock was read as locking composition too, and an existing token file
closed the exploration it has no authority over.

The fix under test: VISUAL_EXPLORATION.md separates locked invariants from
open axes and a per-direction hypothesis; direction count is proportional
(2-3 for exploration, 1 for an explicit decision, 0 variations for
exact-Figma); an existing token file forbids nothing; neither packs, dials
nor font counts are craft evidence; everything runs offline. The documented
proportionality and axis rules are run as behaviour.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def read(name):
    return open(os.path.join(SKILL_DIR, name), encoding="utf-8").read()


def t_doctrine_states_the_split():
    flat = " ".join(read("VISUAL_EXPLORATION.md").split())
    for needle in ("Locked invariants", "Open axes",
                   "brand colors, logo, accessibility floors",
                   "composition, type hierarchy, control anatomy, motion purpose",
                   "differing visibly on at least two open axes",
                   "exact-Figma reproduction generates NO variations",
                   "an EXISTING token file closes nothing by itself",
                   "neither a style pack, nor dial numbers, nor the count of "
                   "fonts is evidence of craft",
                   "no concept roll, no imagegen"):
        assert needle in flat, f"VISUAL_EXPLORATION.md no longer states {needle!r}"
    sk = " ".join(read("SKILL.md").split())
    assert "VISUAL_EXPLORATION.md" in sk, "SKILL.md does not route the exploration"
    cd = " ".join(read("CREATIVE_DIRECTOR.md").split())
    assert "a locked BRAND is not a locked composition" in cd, \
        "Act 3 still reads the brand lock as a composition lock"


# ---------- the documented proportionality and axis rules, executed


OPEN_AXES = ("composition", "type-hierarchy", "control-anatomy", "motion-purpose")
INVARIANTS = ("brand-colors", "logo", "accessibility")


def directions_for(brief_kind, has_token_file=False):
    if brief_kind == "exact-figma":
        return 0
    if brief_kind == "explicit-decision":
        return 1
    return 2                          # under-determined: two, at most three


def valid_direction_pair(a, b):
    problems = []
    for inv in INVARIANTS:
        if a["invariants"].get(inv) != b["invariants"].get(inv):
            problems.append(f"{inv}: directions disagree on a locked invariant")
    differing = [ax for ax in OPEN_AXES if a["axes"].get(ax) != b["axes"].get(ax)]
    if len(differing) < 2:
        problems.append(f"only {len(differing)} open axes differ — two renders "
                        "of one direction, not two directions")
    for d in (a, b):
        if not d.get("hypothesis"):
            problems.append("a direction without a hypothesis is a mood, not a claim")
    return problems


def t_proportionality():
    assert directions_for("under-determined") == 2, \
        "an under-determined brief did not open the exploration"
    assert directions_for("under-determined", has_token_file=True) == 2, \
        "an existing token file closed the exploration — the finding itself"
    assert directions_for("explicit-decision") == 1
    assert directions_for("exact-figma") == 0, \
        "exact-Figma reproduction generated variations"


def t_two_directions_must_differ_on_open_axes():
    base = {"invariants": {"brand-colors": "#0af,#111", "logo": "v3",
                           "accessibility": "AA"},
            "axes": {"composition": "chat-first", "type-hierarchy": "system",
                     "control-anatomy": "pill", "motion-purpose": "feedback"},
            "hypothesis": "the chat IS the product"}
    twin = {**base, "axes": dict(base["axes"]),
            "hypothesis": "services frame the chat"}
    problems = valid_direction_pair(base, twin)
    assert any("open axes differ" in p for p in problems), \
        "two identical compositions passed as two directions"
    other = {**base, "axes": {**base["axes"], "composition": "services-grid",
                              "type-hierarchy": "display-serif"},
             "hypothesis": "services frame the chat"}
    assert valid_direction_pair(base, other) == [], \
        f"a genuine second direction was refused: {valid_direction_pair(base, other)}"


def t_invariants_hold_across_directions():
    a = {"invariants": {"brand-colors": "#0af", "logo": "v3", "accessibility": "AA"},
         "axes": {"composition": "x", "type-hierarchy": "y",
                  "control-anatomy": "z", "motion-purpose": "w"},
         "hypothesis": "h1"}
    b = {"invariants": {"brand-colors": "#f60", "logo": "v3", "accessibility": "AA"},
         "axes": {"composition": "q", "type-hierarchy": "r",
                  "control-anatomy": "z", "motion-purpose": "w"},
         "hypothesis": "h2"}
    problems = valid_direction_pair(a, b)
    assert any("brand-colors" in p for p in problems), \
        "a direction broke a locked invariant and passed"


def main():
    case("the doctrine states the split across all three files",
         t_doctrine_states_the_split)
    case("direction count is proportional; tokens close nothing",
         t_proportionality)
    case("two directions must differ on >=2 open axes, each with a hypothesis",
         t_two_directions_must_differ_on_open_axes)
    case("locked invariants hold across directions", t_invariants_hold_across_directions)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
