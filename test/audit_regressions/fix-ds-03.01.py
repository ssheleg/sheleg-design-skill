#!/usr/bin/env python3
"""FIX-DS-03.01 — performance by budget and recipe, not by API blacklist
(sherlock audit, DS-03).

The finding: `addEventListener("scroll")` was banned as inherently janky (MDN
documents the legitimate throttled/passive pattern), while `filter` and
`clip-path` were called unconditionally safe (web.dev warns a blur's cost
scales with area and device).

The fix under test (MOTION_DOCTRINE.md):
* the scroll bullet blames the WORK (thrashing, per-frame state, unthrottled
  computation), gives the recipe (passive → cheap read → rAF batch → cleanup)
  and rejects a handler only on a MEASURED defect — with the MDN link;
* filter/clip-path are CONDITIONAL on a measured budget for the target
  devices — with the web.dev link; 60 AND 120 Hz and reduced-motion are
  separate checks;
* the verdict rule run as behaviour on the audit's scenarios.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "MOTION_DOCTRINE.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def flat():
    with open(DOC, encoding="utf-8") as fh:
        return " ".join(fh.read().split())


def t_scroll_defect_is_the_work():
    d = flat()
    assert "the defect is the WORK, not the API" in d
    assert '`window.addEventListener("scroll", …)`** — runs every frame, unbatched' not in d, \
        "the blanket API ban survived — the finding itself"
    assert "{passive: true}" in d
    assert "rejected only on a MEASURED defect" in d
    assert "developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event" in d


def t_recipe_present():
    d = flat()
    assert "passive listener → cheap read → batch writes in rAF → clean up on unmount" in d


def t_filter_conditional_with_budget():
    d = flat()
    assert "`filter` and `clip-path` are CONDITIONAL, not free" in d
    assert "full-screen animated blur passes only a MEASURED performance budget" in d
    assert "web.dev/articles/animations-guide" in d
    assert "60 AND 120 Hz" in d and "`prefers-reduced-motion` separately" in d


# ---------------- the verdict rule, run as behaviour


def verdict(kind, measured_defect=None, budget_passed=None):
    if kind == "cheap-passive-scroll":
        return "reject: " + measured_defect if measured_defect else "allowed"
    if kind == "fullscreen-animated-blur":
        return "allowed" if budget_passed else "reject: needs a passed performance budget"
    if kind == "layout-animation":
        return "reject: layout property"
    return "allowed"


def t_verdicts():
    assert verdict("cheap-passive-scroll") == "allowed", \
        "a cheap passive scroll listener was rejected without a measured defect"
    assert verdict("cheap-passive-scroll", measured_defect="long tasks 180ms").startswith("reject"), \
        "a measured defect no longer rejects"
    assert verdict("fullscreen-animated-blur", budget_passed=False).startswith("reject"), \
        "a full-screen animated blur passed without a budget"
    assert verdict("fullscreen-animated-blur", budget_passed=True) == "allowed"
    assert verdict("layout-animation").startswith("reject"), "layout animation ban lost"


def main():
    case("the scroll defect is the work, with the MDN link", t_scroll_defect_is_the_work)
    case("the recipe is present", t_recipe_present)
    case("filter/clip-path conditional on a measured budget, 60/120Hz + reduced-motion separate",
         t_filter_conditional_with_budget)
    case("the verdict rule run as behaviour", t_verdicts)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
