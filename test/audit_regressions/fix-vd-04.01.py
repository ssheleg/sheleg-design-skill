#!/usr/bin/env python3
"""FIX-VD-04.01 — shadcn is styled, not unstyled; token color is not the whole
adapter (sherlock audit, VD-04).

The finding: SKILL.md called shadcn/ui "unstyled primitives", but its official
docs ship "Beautiful Defaults" — editable STYLED components on HEADLESS
primitives. And the adapter was described as a color remap, when a token color
map alone leaves shadcn's default radius/padding/shadow/type in place.

The fix under test: shadcn is described as editable styled components on
headless primitives (docs cited, date pinned); the adapter contract is
color + geometry + density + typography + elevation + state/anatomy; after a
token remap the RENDERED component matrix (computed sizes/padding/radius/
shadow/fonts/states) is compared against the chosen direction with kept
defaults listed; and a custom component edit is not automatically a redesign.
Documented in SKILL.md, and the sufficiency rule is run as behaviour.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")
SKILL = os.path.join(SKILL_DIR, "SKILL.md")


def bundle_text():
    """SKILL.md plus every document it LINKS TO — what the agent actually loads.

    The needles below assert that a doctrine sentence REACHES the agent. They read
    SKILL.md alone until 2026-09-10, when the body breached the house 5000-token
    budget and the house rule's own remedy — a split into a bundled reference —
    would have deleted them. The address a doctrine claim has is the bundle, not
    one file inside it, so the links are RESOLVED here rather than listed: a
    sentence parked in a document SKILL.md does not point at is still gone, which
    is the same reachability the house auditor enforces (BUNDLE_UNREACHABLE).
    """
    import re
    text = open(SKILL, encoding="utf-8").read()
    parts = [text]
    for rel in sorted(set(re.findall(r"\]\(\./([A-Za-z0-9_./-]+\.md)\)", text))):
        path = os.path.join(SKILL_DIR, rel)
        if os.path.isfile(path):
            parts.append(open(path, encoding="utf-8").read())
    return " ".join(" ".join(parts).split())

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def t_doctrine_corrects_shadcn():
    flat = bundle_text()
    for needle in ("it is\nNOT unstyled either".replace("\n", " "),
                   'ship "Beautiful Defaults"',
                   "built on HEADLESS\nprimitives (Radix/Base)".replace("\n", " "),
                   "https://ui.shadcn.com/docs,\nchecked 2026-09-09".replace("\n", " "),
                   "a custom component edit is a normal adaptation, NOT automatically a redesign",
                   "color + geometry + density + typography + elevation + state/anatomy**",
                   "compare the RENDERED\ncomponent matrix".replace("\n", " "),
                   "list the defaults you deliberately kept"):
        assert needle in flat, f"the skill bundle no longer states {needle!r}"
    assert "It is\nunstyled primitives plus Tailwind".replace("\n", " ") not in flat, \
        "the 'unstyled primitives' claim survived somewhere in the bundle"


# ---------------- the adapter-sufficiency rule, executed


ADAPTER_AXES = ("color", "geometry", "density", "typography", "elevation", "state")


def adapter_complete(remapped_axes):
    """A pack's shadcn adapter is complete only when every axis is addressed;
    color alone is not sufficient."""
    return set(ADAPTER_AXES) <= set(remapped_axes)


def compare_matrix(before, after):
    """After a token remap, a component differs on the pack's direction only if
    the RENDERED properties move — not just the color variables."""
    return {k: (before.get(k), after.get(k)) for k in set(before) | set(after)
            if before.get(k) != after.get(k)}


def t_color_only_adapter_is_incomplete():
    assert not adapter_complete({"color"}), \
        "a color-only remap was accepted as a complete adapter — the finding itself"
    assert adapter_complete(ADAPTER_AXES)


def t_render_matrix_catches_default_geometry():
    # only color remapped: radius/padding stay at shadcn defaults
    before = {"color": "brand", "radius": "0.5rem", "padding": "8px 16px"}
    after = {"color": "packed", "radius": "0.5rem", "padding": "8px 16px"}
    diff = compare_matrix(before, after)
    assert "radius" not in diff and "padding" not in diff, \
        "the default geometry did not survive a color-only remap"
    assert "color" in diff
    # a real adaptation moves the geometry too
    after2 = {"color": "packed", "radius": "2px", "padding": "6px 12px"}
    diff2 = compare_matrix(before, after2)
    assert "radius" in diff2 and "padding" in diff2, \
        "the render matrix did not surface the geometry change"


def t_custom_edit_is_not_a_redesign():
    def classify_edit(kind):
        # editing a copied-in component is a normal adaptation; a redesign is a
        # change of direction, not any component tweak
        return "adaptation" if kind == "component-edit" else "redesign"
    assert classify_edit("component-edit") == "adaptation", \
        "a custom component edit was classed as a redesign"
    assert classify_edit("direction-change") == "redesign"


def main():
    case("the doctrine corrects the shadcn description and adapter contract",
         t_doctrine_corrects_shadcn)
    case("a color-only adapter is incomplete", t_color_only_adapter_is_incomplete)
    case("the render matrix catches default geometry a color remap left",
         t_render_matrix_catches_default_geometry)
    case("a custom component edit is not a redesign", t_custom_edit_is_not_a_redesign)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
