#!/usr/bin/env python3
"""XD-06.01 — composition examples instead of uncalibrated axes
(sherlock audit, XD-06).

LAYOUT_CRAFT.md replaces dial values with observable composition. The test
holds it to the acceptance:

* squint/focal-order, proximity-before-container and the density≠rhythm
  distinction each carry a concrete OBSERVABLE sign;
* container/zoom/locale/keyboard adaptation and DOM/focus-order agreement are
  described, and optical correction is proven on the RENDER — source alignment
  alone is not proof;
* three independent decision pairs (dense operator / editorial read / mobile
  action) exist and are NOT declared styles or packs;
* a fix names the lost priority, never an arbitrary dial; card/table/grid are
  admissible when they do the task's job; density derives from the task, not
  the brand category.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "LAYOUT_CRAFT.md")

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


def t_observable_signs_not_dials():
    d = flat()
    assert "The squint test and focal order" in d
    assert "Proximity before container" in d
    assert "Density is not rhythm" in d
    assert d.count("Observable") >= 3, "the axes lost their observable signs"
    assert "never an\narbitrary dial value".replace("\n", " ") in d or \
           "never an arbitrary dial value" in d, "fixes may still be dial numbers"
    assert "the primary action is not first in\nfocal order".replace("\n", " ") in d or \
           "the primary action is not first in focal order" in d, \
        "the lost-priority fix example is gone"


def t_task_decides_not_brand():
    d = flat()
    assert "never\nassigned by brand category".replace("\n", " ") in d or \
           "never assigned by brand category" in d, "density is assigned by brand again"
    assert "Card, table and grid are all admissible when they do the task's job" in d, \
        "card/table/grid admissibility is missing"


def t_adaptation_and_focus_agreement():
    d = flat()
    for axis in ("Container", "Zoom", "Locale", "Keyboard"):
        assert f"**{axis}**" in d, f"the {axis} adaptation is missing"
    assert "DOM order and focal\norder are the same walk".replace("\n", " ") in d or \
           "DOM order and focal order are the same walk" in d, \
        "the DOM/focus-order agreement is missing"


def t_three_pairs_not_packaged():
    raw = open(DOC, encoding="utf-8").read()
    for pair in ("dense operator", "editorial read", "mobile action"):
        assert pair in raw, f"the {pair!r} pair is missing"
    d = flat()
    assert "not styles and not packs" in d, "the pairs may be promoted into presets"
    rows = [l for l in raw.splitlines()
            if l.startswith("|") and "What decides" not in l and not set(l) <= set("|- ")]
    assert len(rows) >= 3, "fewer than three decision pairs"
    for r in rows:
        assert "when" in r.lower(), f"a pair does not say what decides: {r[:60]}"


def t_optical_correction_on_render():
    d = flat()
    assert "proven\non the RENDER".replace("\n", " ") in d or "proven on the RENDER" in d, \
        "optical correction is not proven on a render"
    assert '"The values align in\nCSS" is the claim the correction exists to overrule'.replace("\n", " ") in d \
        or '"The values align in CSS" is the claim the correction exists to overrule' in d, \
        "source alignment still counts as proof"


def main():
    case("axes carry observable signs, fixes name the lost priority",
         t_observable_signs_not_dials)
    case("the task decides; card/table/grid admissible; not the brand",
         t_task_decides_not_brand)
    case("container/zoom/locale/keyboard adaptation + DOM/focus agreement",
         t_adaptation_and_focus_agreement)
    case("three decision pairs, explicitly not styles/packs", t_three_pairs_not_packaged)
    case("optical correction is proven on the render", t_optical_correction_on_render)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
