#!/usr/bin/env python3
"""FIX-DS-01.02 — the rendered pack comparison (sherlock audit, DS-01 leaf 2).

On FIX-DS-01.01's adapter contract. The rules under test, run as the
documented behaviour: a comparison pins one component, one content, one
viewport and attributes differences to the PACK; a content/viewport mismatch
invalidates the pair rather than counting as a difference; geometry and
state differences are PRESERVED in the receipt, not collapsed to a boolean;
identical renders across packs flag a dead adapter, not equivalence; and a
candidate without a complete adapter makes the whole comparison NOT READY —
never "ready with the packs that had adapters".

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                     "SKILL.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def t_doctrine_states_the_protocol():
    flat = " ".join(open(SKILL, encoding="utf-8").read().split())
    for needle in ("one component, one content, one viewport",
                   "INVALIDATES the pair",
                   "identical geometry and states across a compared pair is a "
                   "signal the adapter never reached the component",
                   "not ready",
                   "struck from the candidate list explicitly",
                   '"compared what had adapters" silently is a comparison of a '
                   "different question"):
        assert needle in flat, f"SKILL.md no longer states {needle!r}"


# ------------- the documented receipt and rules, executed


def render_record(pack, adapter_complete, component, content, viewport,
                  geometry, states):
    return {"pack": pack, "adapter_complete": adapter_complete,
            "component": component, "content": content, "viewport": viewport,
            "geometry": geometry, "states": states}


def comparison_ready(candidates):
    """NOT READY unless every named candidate has a complete adapter."""
    missing = [c["pack"] for c in candidates if not c["adapter_complete"]]
    if missing:
        return False, [f"NOT READY: {p} has no complete adapter — adapt it or "
                       "strike it from the candidate list explicitly"
                       for p in missing]
    return True, []


def compare(a, b):
    """Differences attributable to the pack, or an invalid pair."""
    for pin in ("component", "content", "viewport"):
        if a[pin] != b[pin]:
            return {"valid": False,
                    "reason": f"{pin} differs — the pair compares nothing"}
    geo = {k: (a["geometry"].get(k), b["geometry"].get(k))
           for k in set(a["geometry"]) | set(b["geometry"])
           if a["geometry"].get(k) != b["geometry"].get(k)}
    states = {k: (a["states"].get(k), b["states"].get(k))
              for k in set(a["states"]) | set(b["states"])
              if a["states"].get(k) != b["states"].get(k)}
    out = {"valid": True, "geometry_diff": geo, "state_diff": states}
    if not geo and not states:
        out["warning"] = ("identical render across packs — the adapter never "
                          "reached the component; not a finding of equivalence")
    return out


def rec(pack, **kw):
    base = dict(adapter_complete=True, component="card", content="sha:abc",
                viewport="1280x800",
                geometry={"card": (0, 0, 320, 180), "cta": (24, 120, 120, 40)},
                states={"cta:hover": "raised", "cta:disabled": "dimmed"})
    base.update(kw)
    return render_record(pack, base.pop("adapter_complete"), base.pop("component"),
                         base.pop("content"), base.pop("viewport"),
                         base.pop("geometry"), base.pop("states"))


def t_missing_adapter_blocks_the_whole_comparison():
    cands = [rec("workbench"), rec("orchard"), rec("gallery", adapter_complete=False)]
    ready, problems = comparison_ready(cands)
    assert not ready, "a comparison declared ready with an adapterless candidate"
    assert any("gallery" in p and "NOT READY" in p for p in problems), \
        f"the missing adapter is not named: {problems}"
    ready2, _ = comparison_ready([rec("workbench"), rec("orchard")])
    assert ready2, "a fully adapted candidate list was refused"


def t_pack_differences_are_preserved_not_boolean():
    a = rec("workbench")
    b = rec("orchard",
            geometry={"card": (0, 0, 320, 200), "cta": (24, 140, 120, 44)},
            states={"cta:hover": "underlined", "cta:disabled": "dimmed"})
    d = compare(a, b)
    assert d["valid"]
    assert d["geometry_diff"]["card"] == ((0, 0, 320, 180), (0, 0, 320, 200)), \
        "the geometry difference was not preserved per element"
    assert d["state_diff"]["cta:hover"] == ("raised", "underlined"), \
        "the state difference was collapsed"
    assert "cta:disabled" not in d["state_diff"], "an equal state was reported"


def t_content_or_viewport_mismatch_invalidates():
    a = rec("workbench")
    for pin, val in (("content", "sha:other"), ("viewport", "375x812"),
                     ("component", "table")):
        b = rec("orchard", **{pin: val})
        d = compare(a, b)
        assert not d["valid"] and pin in d["reason"], \
            f"a {pin} mismatch was counted as a pack difference"


def t_identical_render_flags_dead_adapter():
    d = compare(rec("workbench"), rec("orchard"))
    assert d["valid"] and not d["geometry_diff"] and not d["state_diff"]
    assert "never reached the component" in d.get("warning", ""), \
        "an identical render passed as equivalence — a dead adapter went unseen"


def main():
    case("the doctrine states the protocol", t_doctrine_states_the_protocol)
    case("a missing adapter blocks the WHOLE comparison, by name",
         t_missing_adapter_blocks_the_whole_comparison)
    case("pack differences are preserved per element, never a boolean",
         t_pack_differences_are_preserved_not_boolean)
    case("a content/viewport/component mismatch invalidates the pair",
         t_content_or_viewport_mismatch_invalidates)
    case("an identical render flags a dead adapter, not equivalence",
         t_identical_render_flags_dead_adapter)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
