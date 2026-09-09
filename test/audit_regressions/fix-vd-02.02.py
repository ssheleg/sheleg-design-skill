#!/usr/bin/env python3
"""FIX-VD-02.02 — bounded rerender comparison (sherlock audit, VD-02 leaf 2,
on FIX-VD-02.01's actionable critique).

The rules under test: the second (fixed) render is judged on the SAME
before/after matrix — same content, same viewport — scored
resolved/partial/unresolved; a fixed budget bounds it and its exhaustion
leaves an open observation UNRESOLVED, never renamed ship; a mechanical
result (a PNG, tokens passing) is not a craft PASS; an already-chosen
direction gets a single critique pass without a mandatory fork.

Documented in CREATIVE_DIRECTOR.md and SKILL.md, and the matrix/budget rules
are run as behaviour.

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


def t_doctrine_states_the_bounded_rerender():
    cd = " ".join(read("CREATIVE_DIRECTOR.md").split())
    for needle in ("The bounded rerender comparison",
                   "before/after on the SAME content and viewport",
                   "resolved / partial / unresolved per observation",
                   "its exhaustion\nleaves UNRESOLVED as unresolved".replace("\n", " "),
                   "Budget exhaustion is a state, not a pass",
                   "Mechanical result is not craft result",
                   "no mandatory fork",
                   "a sequential independent pass is a valid substitute for a fresh subagent"):
        assert needle in cd, f"CREATIVE_DIRECTOR.md no longer states {needle!r}"
    sk = " ".join(read("SKILL.md").split())
    assert "judged on the SAME before/after matrix inside a" in sk, \
        "SKILL.md does not reference the bounded rerender"


# ---------------- the matrix + budget rules, executed


def compare(before, after):
    """Same content/viewport or the pair is invalid; per-observation verdict."""
    if before["content"] != after["content"] or before["viewport"] != after["viewport"]:
        return {"valid": False, "reason": "content or viewport moved"}
    verdicts = {}
    for obs, fixed in after["observations"].items():
        was = before["observations"].get(obs)
        if fixed == "fixed":
            verdicts[obs] = "resolved"
        elif fixed == "improved":
            verdicts[obs] = "partial"
        else:
            verdicts[obs] = "unresolved"
    return {"valid": True, "verdicts": verdicts}


def settle(verdicts, budget_spent, budget):
    """Budget exhaustion never renames unresolved as ship."""
    out = dict(verdicts)
    if budget_spent >= budget:
        # stop; whatever is unresolved STAYS unresolved
        return {"status": ("all-resolved" if all(v == "resolved" for v in out.values())
                           else "budget-exhausted"), "verdicts": out}
    return {"status": "in-progress", "verdicts": out}


def craft_pass(mechanical_ok, craft_reviewed_ok):
    """A mechanical pass alone is never a craft pass."""
    return bool(mechanical_ok and craft_reviewed_ok)


def t_same_matrix_or_invalid():
    b = {"content": "c1", "viewport": "1280", "observations": {"o1": "defect"}}
    a_ok = {"content": "c1", "viewport": "1280", "observations": {"o1": "fixed"}}
    assert compare(b, a_ok)["verdicts"]["o1"] == "resolved"
    a_bad = {"content": "c2", "viewport": "1280", "observations": {"o1": "fixed"}}
    assert compare(b, a_bad)["valid"] is False, \
        "a content change was compared as a valid before/after"


def t_budget_exhaustion_leaves_unresolved():
    verdicts = {"o1": "resolved", "o2": "unresolved"}
    r = settle(verdicts, budget_spent=10, budget=10)
    assert r["status"] == "budget-exhausted", "an open observation was renamed ship"
    assert r["verdicts"]["o2"] == "unresolved", "the unresolved observation was renamed"
    r2 = settle({"o1": "resolved"}, budget_spent=10, budget=10)
    assert r2["status"] == "all-resolved"


def t_mechanical_is_not_craft():
    assert craft_pass(mechanical_ok=True, craft_reviewed_ok=False) is False, \
        "a PNG + passing tokens was accepted as a craft PASS — the finding itself"
    assert craft_pass(mechanical_ok=True, craft_reviewed_ok=True) is True


def t_already_chosen_gets_one_pass_no_fork():
    cd = " ".join(read("CREATIVE_DIRECTOR.md").split())
    assert "An already-chosen direction gets a\nsingle critique pass here".replace("\n", " ") in cd \
        or "already-chosen direction gets a single critique pass here" in cd, \
        "the single-pass-no-fork allowance is missing"


def main():
    case("the doctrine states the bounded rerender", t_doctrine_states_the_bounded_rerender)
    case("the second render is judged on the same matrix or invalid",
         t_same_matrix_or_invalid)
    case("budget exhaustion leaves unresolved as unresolved",
         t_budget_exhaustion_leaves_unresolved)
    case("a mechanical result is not a craft pass", t_mechanical_is_not_craft)
    case("an already-chosen direction gets one pass, no fork",
         t_already_chosen_gets_one_pass_no_fork)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
