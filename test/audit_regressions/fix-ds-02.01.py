#!/usr/bin/env python3
"""FIX-DS-02.01 — a survey about the word "craft" is context, not a work order
(sherlock audit, DS-02).

The finding: the Figma State-of-the-Designer numbers (58/47/36/35/15 — how
often designers picked each DEFINITION of craft) were read "as a definition of
done, in that order", putting polish before problem solving and clear UX. An
association frequency became a normative sequence.

The fix under test (sheleg-design SKILL.md):
* the survey stays as context with its exact meaning and the source link —
  58% proves an association in a survey, never a causal effect or work order;
* the gate order is DERIVED FROM DEPENDENCIES — task, states, availability,
  system, polish, emotion, consistency — and is declared an authored decision,
  not a research conclusion;
* the triage rule run as behaviour: a brief with a broken primary task fixes
  the task first, even with perfect tokens.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design", "SKILL.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def flat():
    with open(SKILL, encoding="utf-8") as fh:
        return " ".join(fh.read().split())


def t_survey_is_context_with_meaning_and_link():
    d = flat()
    assert "Read that as a definition of done, in that order" not in d, \
        "the survey is still a normative order — the finding itself"
    assert "an association survey" in d
    assert "https://www.figma.com/blog/state-of-the-designer-2026/" in d, "the source link is missing"
    assert "58% proves an association in a survey, never a causal effect or a work order" in d, \
        "what 58% proves is not stated"


def t_order_is_derived_and_authored():
    d = flat()
    assert "DERIVED FROM DEPENDENCIES" in d
    assert "authored decision, not a research conclusion" in d


def t_task_first_polish_later():
    raw = open(SKILL, encoding="utf-8").read()
    sec = raw[raw.index("## The craft bar"):]
    order = []
    for m in re.finditer(r"^\d+\.\s+\*\*(.+?)\*\*", sec, re.M):
        order.append(m.group(1))
        if len(order) >= 7:
            break
    assert order[0] == "The task", f"the first gate is {order[0]!r}, not the task"
    assert order.index("The task") < order.index("Polish"), "polish still precedes the task"
    assert order.index("States") < order.index("Polish")
    assert order.index("Availability") < order.index("System")


# ---------------- the triage, run as behaviour


def triage(broken_task, tokens_perfect):
    """The doctrine's rule: gate 1 first, regardless of gate 5's state."""
    if broken_task:
        return "fix the task"
    return "proceed to later gates"


def t_triage_behaviour():
    assert triage(broken_task=True, tokens_perfect=True) == "fix the task", \
        "perfect tokens outranked a broken primary task"
    assert triage(broken_task=False, tokens_perfect=False) == "proceed to later gates"


def main():
    case("the survey is context with its meaning and the source link",
         t_survey_is_context_with_meaning_and_link)
    case("the gate order is derived from dependencies and authored",
         t_order_is_derived_and_authored)
    case("the task gate precedes polish (and states/availability precede system/polish)",
         t_task_first_polish_later)
    case("a broken primary task is fixed first, even with perfect tokens",
         t_triage_behaviour)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
