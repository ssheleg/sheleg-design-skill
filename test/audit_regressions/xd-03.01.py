#!/usr/bin/env python3
"""XD-03.01 — the visual-evidence-fitness contract (sherlock audit, XD-03).

A screenshot is evidence only of the right thing, freshly, and rendered. This
leaf creates VISUAL_REVIEW.md; the test holds it to the acceptance:

* a capture record pins revision/route/scenario/state/viewport/locale/theme/
  motion/captured-at/source;
* a blank / stale / wrong-route (or wrong viewport / unrendered-font) frame
  cannot be promoted to a visual-pass, and no runtime => `unverified`;
* capture is tool-agnostic — any browser capability qualifies, Playwright is
  not required;
* visual evidence is separated from DOM/source reading, functional trace and
  native device evidence, and a native mockup is not a verified native
  interface.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "VISUAL_REVIEW.md")

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


def t_doc_exists():
    assert os.path.isfile(DOC), "VISUAL_REVIEW.md was not created"


def t_capture_record_fields():
    d = flat()
    for field in ("revision", "route", "scenario", "state", "viewport",
                  "locale", "theme", "motion", "captured-at", "source"):
        assert f"`{field}`" in d, f"the capture record does not pin {field!r}"


def t_disqualifiers_cannot_be_promoted():
    d = flat()
    assert "may not be promoted to one" in d, "the no-promotion rule is missing"
    for bad in ("it is blank", "it is stale", "the wrong route", "the wrong viewport",
                "the fonts had not rendered"):
        assert bad in d, f"the disqualifier {bad!r} is not listed"


def t_no_runtime_is_unverified_not_pass():
    d = flat()
    assert "recorded as **`unverified`**, not as a pass" in d, \
        "no-runtime is not recorded as unverified"
    assert "never demands a mandatory tool install" in d, \
        "the contract still demands a mandatory tool install"


def t_capture_is_tool_agnostic():
    d = flat()
    assert "any working\nbrowser capability qualifies".replace("\n", " ") in d \
        or "any working browser capability qualifies" in d, "capture is not tool-agnostic"
    assert "Playwright is not required" in d, "Playwright is still required"


def t_evidence_classes_separated():
    d = flat()
    for cls in ("visual evidence", "DOM / source reading", "functional trace",
                "native device evidence"):
        assert cls in d, f"the evidence class {cls!r} is not named"
    assert "A native mockup is not a verified native interface" in d, \
        "a native mockup can still be called a verified native interface"


# ---------------- the promotion rule, run as behaviour


def can_promote(capture):
    """The doc's rule: a frame becomes a visual-pass only if it is fit."""
    if not capture.get("runtime"):
        return "unverified"
    if capture.get("blank"):
        return False
    if capture.get("revision") != capture.get("under_review"):
        return False          # stale
    if capture.get("route") != capture.get("claimed_route"):
        return False          # wrong route
    if capture.get("fonts_unrendered"):
        return False
    return True


def t_promotion_rule_behaviour():
    ok = {"runtime": True, "blank": False, "revision": "r2", "under_review": "r2",
          "route": "/pricing", "claimed_route": "/pricing", "fonts_unrendered": False}
    assert can_promote(ok) is True, "a fit capture was not promoted"
    assert can_promote({**ok, "blank": True}) is False, "a blank frame was promoted"
    assert can_promote({**ok, "revision": "r1"}) is False, "a stale frame was promoted"
    assert can_promote({**ok, "route": "/"}) is False, "a wrong-route frame was promoted"
    assert can_promote({**ok, "fonts_unrendered": True}) is False, "an unrendered-font frame passed"
    assert can_promote({**ok, "runtime": False}) == "unverified", "no runtime was promoted to a pass"


def main():
    case("VISUAL_REVIEW.md exists", t_doc_exists)
    case("the capture record pins every field", t_capture_record_fields)
    case("blank/stale/wrong-route/viewport/font frames cannot be promoted",
         t_disqualifiers_cannot_be_promoted)
    case("no runtime is unverified, not a pass, and no mandatory install",
         t_no_runtime_is_unverified_not_pass)
    case("capture is tool-agnostic; Playwright not required", t_capture_is_tool_agnostic)
    case("evidence classes separated; native mockup is not a verified native interface",
         t_evidence_classes_separated)
    case("the promotion rule, run as behaviour", t_promotion_rule_behaviour)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
