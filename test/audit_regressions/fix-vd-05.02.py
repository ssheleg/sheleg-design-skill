#!/usr/bin/env python3
"""FIX-VD-05.02 — Heading: the semantic level and the visual size are two
props, not one (sherlock, VD-05).

The finding: `level` decided BOTH the tag (h1/h2/h3 — the document outline)
and the visual class, so an h2 could not wear the display size and any visual
re-skin moved the outline under screen readers and the crawler alike.

The fix under test, across all 39 kits (the spine is byte-identical):
* the TAG derives from `level` only; the CLASS from `size ?? level` — an h2
  may wear the display size, and a visual variant never moves the outline;
* backwards compatible: `size` defaults to the level;
* the spine passthrough of FIX-VD-05.01 extends to Heading (host attributes,
  forwardRef, rest spread);
* the bridge states the contract. Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
KITS = os.path.join(ROOT, "kits")
WB = os.path.join(KITS, "workbench", "src", "Heading.tsx")
BRIDGE = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                      "DESIGN_SYNC_BRIDGE.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def t_tag_from_level_class_from_size():
    s = read(WB)
    assert "const Tag = `h${level}`" in s, "the tag no longer derives from the semantic level"
    assert "${size ?? level}" in s, \
        "the class does not follow size ?? level — level still decides the look"
    assert re.search(r"size\?\:\s*1\s*\|\s*2\s*\|\s*3", s), "the size prop is gone"


def t_passthrough_extends_to_heading():
    s = read(WB)
    assert "extends Omit<HTMLAttributes<HTMLHeadingElement>" in s
    assert "forwardRef<HTMLHeadingElement, HeadingProps>" in s
    assert "{...rest}" in s


def t_every_kit_carries_the_same_contract():
    props_re = re.compile(r"export\s+interface\s+(\w+Props)\s*(?:extends[^{]*)?\{(.*?)^\}",
                          re.S | re.M)

    def body(text):
        for m in props_re.finditer(text):
            if m.group(1) == "HeadingProps":
                b = re.sub(r"/\*.*?\*/", "", m.group(2), flags=re.S)
                b = re.sub(r"//[^\n]*", "", b)
                return "".join(b.split())

    bodies = set()
    n = 0
    for kit in sorted(os.listdir(KITS)):
        f = os.path.join(KITS, kit, "src", "Heading.tsx")
        if not os.path.isfile(f):
            continue
        n += 1
        s = read(f)
        bodies.add(body(s))
        assert "${size ?? level}" in s, f"{kit}: the visual size does not default to the level"
        assert "const Tag = `h${level}`" in s, f"{kit}: the tag moved off the semantic level"
    assert n >= 39, f"only {n} kits found"
    assert len(bodies) == 1, f"{len(bodies)} distinct HeadingProps bodies — the spine split"


# ---------------- the resolution, run as a pure model


def rendered(level=2, size=None):
    return {"tag": f"h{level}", "size_class": f"--{size if size is not None else level}"}


def t_h2_wears_display_size_outline_unmoved():
    display_h2 = rendered(level=2, size=1)
    assert display_h2["tag"] == "h2", "asking for the display size moved the outline"
    assert display_h2["size_class"] == "--1"
    plain = rendered(level=2)
    assert plain["tag"] == "h2" and plain["size_class"] == "--2", \
        "the backwards-compatible default broke — size no longer defaults to level"
    assert rendered(level=3, size=3)["tag"] == "h3"


def t_bridge_states_the_contract():
    flat = " ".join(read(BRIDGE).split())
    for needle in ("`size` defaults to the level",
                   "an `h2` may wear the display size",
                   "the DOM outline never moves with a visual variant"):
        assert needle in flat, f"the bridge no longer states {needle!r}"


def main():
    case("the tag derives from level, the class from size ?? level",
         t_tag_from_level_class_from_size)
    case("the spine passthrough extends to Heading", t_passthrough_extends_to_heading)
    case("all 39 kits carry one identical contract", t_every_kit_carries_the_same_contract)
    case("an h2 wears the display size with the outline unmoved",
         t_h2_wears_display_size_outline_unmoved)
    case("the bridge states the contract", t_bridge_states_the_contract)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
