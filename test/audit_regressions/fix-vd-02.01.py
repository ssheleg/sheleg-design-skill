#!/usr/bin/env python3
"""FIX-VD-02.01 — actionable render critique (sherlock audit, VD-02).

The finding: the review had screenshots and quality gates but no mandatory
critique of the specific render — so "premium"/"generic" with no region
passed as acceptance, a clean render could be handed a fabricated defect, and
a soft winner could be picked over a render that failed a hard gate.

The fix under test: the critique is a triple (image region, observable
defect, intended change) with a second render; a clean render stops the loop
(no quota); missing brand is NOT_ASSESSED; the strict gate runs before the
soft winner. Documented in CREATIVE_DIRECTOR.md, and the critique/gate rules
are run as behaviour.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "CREATIVE_DIRECTOR.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def t_doctrine_states_the_critique():
    flat = " ".join(open(DOC, encoding="utf-8").read().split())
    for needle in ("Render critique — the soft half, made actionable",
                   "a phrase with no region attached is not acceptance",
                   "an image region", "observable defect", "intended change",
                   "there is no defect quota",
                   "Missing brand context is `NOT_ASSESSED`, not a P1",
                   "The strict constraints gate BEFORE the soft winner"):
        assert needle in flat, f"CREATIVE_DIRECTOR.md no longer states {needle!r}"


# ---------------- the critique + gate rules, executed


def is_actionable(observation):
    """A finding counts only as the full triple; a bare adjective does not."""
    return all(observation.get(k) for k in ("region", "defect", "change"))


def critique(observations):
    """A clean render (no observations) stops the loop; fabricating one to fill
    a quota is refused by construction — there is no minimum count."""
    actionable = [o for o in observations if is_actionable(o)]
    dropped = [o for o in observations if not is_actionable(o)]
    return {"findings": actionable, "rejected_as_vague": dropped,
            "stop": len(actionable) == 0}


def choose(renders):
    """Strict gate first: a render failing contrast/keyboard is out regardless
    of soft read. Among gate-passers, an equal soft read is a person's call."""
    passing = [r for r in renders if r["contrast_ok"] and r["keyboard_ok"]]
    if not passing:
        return {"winner": None, "reason": "no render passed the hard gate"}
    top = max(r["soft"] for r in passing)
    leaders = [r for r in passing if r["soft"] == top]
    if len(leaders) > 1:
        return {"winner": None, "reason": "equal after the gate — a person decides"}
    return {"winner": leaders[0]["id"], "reason": "passed the gate and read best"}


def brand_fit(has_brand_pack):
    return "NOT_ASSESSED" if not has_brand_pack else "assessed"


def t_vague_phrase_is_not_acceptance():
    r = critique([{"region": "", "defect": "feels generic", "change": ""},
                  {"region": "top 120px", "defect": "empty band dominates",
                   "change": "raise the composer into the fold"}])
    assert len(r["findings"]) == 1, "a region-less phrase counted as a finding"
    assert r["rejected_as_vague"], "the vague phrase was not flagged"


def t_clean_render_stops_the_loop():
    r = critique([])
    assert r["stop"] is True and r["findings"] == [], \
        "a clean render did not stop the loop — a quota would fabricate a defect"


def t_missing_brand_is_not_assessed():
    assert brand_fit(False) == "NOT_ASSESSED", \
        "absent brand context became an assessed (P1) defect"
    assert brand_fit(True) == "assessed"


def t_hard_gate_precedes_the_soft_winner():
    renders = [
        {"id": "A", "contrast_ok": False, "keyboard_ok": True, "soft": 9},  # prettiest
        {"id": "B", "contrast_ok": True, "keyboard_ok": True, "soft": 6},
    ]
    r = choose(renders)
    assert r["winner"] == "B", \
        "a render that failed contrast won on its soft read — the gate did not gate"


def t_equal_after_gate_is_a_persons_call():
    renders = [
        {"id": "A", "contrast_ok": True, "keyboard_ok": True, "soft": 8},
        {"id": "B", "contrast_ok": True, "keyboard_ok": True, "soft": 8},
    ]
    assert choose(renders)["winner"] is None, \
        "a manufactured preference broke a genuine tie"


def main():
    case("the doctrine states the actionable critique", t_doctrine_states_the_critique)
    case("a region-less phrase is not acceptance", t_vague_phrase_is_not_acceptance)
    case("a clean render stops the loop, no quota", t_clean_render_stops_the_loop)
    case("missing brand is NOT_ASSESSED, not a P1", t_missing_brand_is_not_assessed)
    case("the hard gate precedes the soft winner", t_hard_gate_precedes_the_soft_winner)
    case("equal after the gate is a person's call", t_equal_after_gate_is_a_persons_call)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
