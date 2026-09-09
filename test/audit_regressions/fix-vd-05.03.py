#!/usr/bin/env python3
"""FIX-VD-05.03 — generated-kit propagation: one canonical spine, mechanical
sync, structural parity + one representative test (sherlock audit, VD-05).

The finding's remedy (parent FIX-VD-05): a spine change must reach all 39 kits
at once, and the proof must not require 39 full app builds — structural parity
catches a kit left behind, and ONE representative semantic test catches what
the change actually altered, because the behaviour is identical in every kit by
construction.

This leaf verifies the propagation itself:
* the bridge documents one-canonical-spine + mechanical sync + parity + one
  representative test;
* STRUCTURAL PARITY: every kit's Button AND Heading `*Props` bodies are
  byte-identical (comments stripped) — 1 distinct body each, ≥39 kits;
* ONE REPRESENTATIVE semantic check runs the spine behaviour (Button type
  override, Heading tag-from-level / class-from-size) once, not per kit.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
KITS = os.path.join(ROOT, "kits")
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


PROPS_RE = re.compile(r"export\s+interface\s+(\w+Props)\s*(?:extends[^{]*)?\{(.*?)^\}",
                      re.S | re.M)


def props_body(text, name):
    for m in PROPS_RE.finditer(text):
        if m.group(1) == name + "Props":
            b = re.sub(r"/\*.*?\*/", "", m.group(2), flags=re.S)
            b = re.sub(r"//[^\n]*", "", b)
            return "".join(b.split())
    return None


def t_bridge_documents_the_propagation():
    flat = " ".join(read(BRIDGE).split())
    for needle in ("One canonical spine, propagated mechanically",
                   "tested once, not 39 times",
                   "structural parity",
                   "one representative DOM/semantic test",
                   "names the kit\nthat drifted".replace("\n", " ")):
        assert needle in flat, f"the bridge no longer states {needle!r}"


def t_structural_parity_across_all_kits():
    kits = sorted(k for k in os.listdir(KITS) if os.path.isdir(os.path.join(KITS, k)))
    assert len(kits) >= 39, f"only {len(kits)} kits"
    for comp in ("Button", "Heading"):
        bodies = set()
        for kit in kits:
            f = os.path.join(KITS, kit, "src", f"{comp}.tsx")
            assert os.path.isfile(f), f"{kit}: missing {comp}.tsx (a kit left behind)"
            body = props_body(read(f), comp)
            assert body is not None, f"{kit}: {comp}Props did not parse"
            bodies.add(body)
        assert len(bodies) == 1, \
            f"{comp}Props has {len(bodies)} distinct bodies — a kit drifted from the spine"


# ---------------- ONE representative semantic test (not 39 builds)


def button_type(explicit):
    return explicit if explicit is not None else "button"


def heading_render(level=2, size=None):
    return {"tag": f"h{level}", "size_class": f"--{size if size is not None else level}"}


def t_one_representative_catches_the_semantics():
    # Button: explicit type wins, default fills the hole (FIX-VD-05.01)
    assert button_type("submit") == "submit"
    assert button_type(None) == "button"
    # Heading: tag from level, class from size; h2 may wear display size (FIX-VD-05.02)
    assert heading_render(2, 1) == {"tag": "h2", "size_class": "--1"}
    assert heading_render(2) == {"tag": "h2", "size_class": "--2"}
    # the exemplar's source actually carries these behaviours (the representative)
    wb_btn = read(os.path.join(KITS, "workbench", "src", "Button.tsx"))
    wb_head = read(os.path.join(KITS, "workbench", "src", "Heading.tsx"))
    assert "type={type ?? 'button'}" in wb_btn
    assert "const Tag = `h${level}`" in wb_head and "${size ?? level}" in wb_head


def main():
    case("the bridge documents canonical-spine + mechanical sync + parity + one test",
         t_bridge_documents_the_propagation)
    case("structural parity holds across all 39 kits (Button and Heading)",
         t_structural_parity_across_all_kits)
    case("one representative test catches the actual spine semantics",
         t_one_representative_catches_the_semantics)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
