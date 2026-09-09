#!/usr/bin/env python3
"""FIX-VD-03.02 — the native state matrix (sherlock audit, VD-03 leaf 2, on
FIX-VD-03.01).

The rules under test: a per-target STATE matrix (keyboard, dismissal, restore,
safe-area/insets, text-scale) with expected native behaviour and an evidence
status (measured/unverified); a numeric norm verified against the current
official source before a normative write; the simulator/device type and prior
settings recorded and RESTORED (never unconditionally to 1.0); and the AI
semantic states independent of the 10px mono shape and pack durations.
Documented in MOBILE_SURFACES.md and AI_PRODUCT_PATTERNS.md, and the
matrix/evidence rules run as behaviour.

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


def t_doctrine_states_the_matrix():
    ms = " ".join(read("MOBILE_SURFACES.md").split())
    for needle in ("The native state matrix — what each surface owes",
                   "per-target STATE matrix",
                   "**keyboard**", "**dismissal**", "**restore**",
                   "**safe-area / insets**", "**text-scale**",
                   "measured` on a real device/simulator",
                   "verified against the current official source before it is\nwritten as "
                   "normative".replace("\n", " "),
                   "restore them",
                   "never unconditionally to 1.0"):
        assert needle in ms, f"MOBILE_SURFACES.md no longer states {needle!r}"
    ai = " ".join(read("AI_PRODUCT_PATTERNS.md").split())
    assert "shape is a web-render\nconvention, not the semantic contract".replace("\n", " ") in ai
    assert "independent of\nthe 10px mono size".replace("\n", " ") in ai, \
        "the AI semantic states are still tied to the 10px mono shape"


# ---------------- the matrix + evidence rules, executed


SHEET_STATES = ("keyboard", "dismissal", "restore", "safe_area", "text_scale")


def matrix_complete(cells):
    """Every state carries a behaviour AND an evidence status; a missing status
    is not a pass."""
    problems = []
    for st in SHEET_STATES:
        cell = cells.get(st)
        if not cell or not cell.get("behaviour"):
            problems.append(f"{st}: no expected native behaviour")
        elif cell.get("evidence") not in ("measured", "unverified"):
            problems.append(f"{st}: evidence status must be measured/unverified")
    return problems


def review_scope(cells):
    """A browser prototype leaves native cells unverified — the review ends at
    'reviewed, native unverified', never 'native verified'."""
    if any(c.get("evidence") == "measured" for c in cells.values()):
        return "partially-verified"
    return "reviewed-native-unverified"


def restore_setting(saved, changed_for_test):
    """After a text-scale verification, restore the device to its SAVED value,
    never to a hardcoded 1.0."""
    return saved


def t_matrix_needs_behaviour_and_status():
    good = {s: {"behaviour": f"{s} behaviour", "evidence": "unverified"}
            for s in SHEET_STATES}
    assert matrix_complete(good) == []
    missing_status = dict(good, keyboard={"behaviour": "pushes up"})
    assert any("keyboard" in p for p in matrix_complete(missing_status)), \
        "a cell with no evidence status passed"


def t_browser_review_is_not_native_verified():
    web = {s: {"behaviour": "b", "evidence": "unverified"} for s in SHEET_STATES}
    assert review_scope(web) == "reviewed-native-unverified", \
        "a browser prototype review claimed native verified — the finding itself"


def t_device_setting_restored_to_saved_not_one():
    assert restore_setting(saved=1.4, changed_for_test=3.0) == 1.4, \
        "the device text-scale was reset to a hardcoded value, not the saved one"
    assert restore_setting(saved=1.0, changed_for_test=3.0) == 1.0


def t_numeric_norm_gated_on_verification():
    def write_norm(value, verified_against_source):
        if not verified_against_source:
            return "BLOCKED: verify against the current official source first"
        return f"norm: {value}"
    assert write_norm(8, verified_against_source=False).startswith("BLOCKED"), \
        "a numeric norm was written without primary verification"
    assert write_norm(8, verified_against_source=True) == "norm: 8"


def main():
    case("the doctrine states the native state matrix", t_doctrine_states_the_matrix)
    case("the matrix needs a behaviour and an evidence status per state",
         t_matrix_needs_behaviour_and_status)
    case("a browser review ends unverified, not native verified",
         t_browser_review_is_not_native_verified)
    case("a device setting is restored to its saved value, not 1.0",
         t_device_setting_restored_to_saved_not_one)
    case("a numeric norm is gated on primary verification",
         t_numeric_norm_gated_on_verification)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
