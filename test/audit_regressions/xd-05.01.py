#!/usr/bin/env python3
"""XD-05.01 — the portable typography craft reference (sherlock audit, XD-05).

TYPE_CRAFT.md carries the pack-agnostic half of typography. The test holds it
to the acceptance:

* semantic roles, relative hierarchy, line length / line height / weight /
  width and numeric alignment are described;
* real font loading, fallback, missing glyphs, long strings and native text
  scaling are CHECKS, not assumptions;
* scoped before→after fixes exist, with NO banned-font list and NO fetch;
* one family or the system face is a complete answer; long Cyrillic/RTL/
  numeric content is never shortened for a demo; neither a CDN nor a new font
  package is required.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "TYPE_CRAFT.md")

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


def t_doc_exists_with_core_topics():
    assert os.path.isfile(DOC), "TYPE_CRAFT.md was not created"
    d = flat()
    for topic in ("Semantic text roles", "Relative hierarchy", "Line length",
                  "Line height", "tabular-nums", "Numeric alignment"):
        assert topic in d, f"the {topic!r} section is missing"


def t_reality_checks_are_checks():
    d = flat()
    for chk in ("Real font loading", "Fallback parity", "Missing glyphs",
                "Long strings", "Native text scaling"):
        assert chk in d, f"the {chk!r} check is missing"
    assert "run, not assumed" in d, "the checks are assumptions again"


def t_one_family_and_system_face_suffice():
    d = flat()
    assert "One font family — or the system face — is a complete answer" in d, \
        "one family / system face is not accepted as complete"
    assert "there is no banned-font list here" in d, "a banned-font list crept back"


def t_content_never_shortened_for_a_demo():
    d = flat()
    assert "Content is never shortened to keep a demo pretty" in d, \
        "content can still be trimmed for the demo"
    for tongue in ("Cyrillic", "RTL", "long numbers"):
        assert tongue in d, f"{tongue} content is not in the long-strings check"


def t_no_cdn_or_package_required():
    d = flat()
    assert "no font is fetched to follow this reference" in d, "the reference fetches a font"
    assert "none requires a new font, a CDN, or a fetch" in d, \
        "a fix requires a CDN or a new package"
    assert "per-brief decisions, outside this baseline" in d, \
        "licensing/new-font is not scoped to the brief"


def t_scoped_fixes_table():
    raw = open(DOC, encoding="utf-8").read()
    rows = [l for l in raw.splitlines() if l.startswith("|") and "Scope" not in l
            and not re.match(r"^\|[-\s|]+\|$", l)]
    assert len(rows) >= 5, f"only {len(rows)} before→after fixes"
    for r in rows:
        assert r.count("|") >= 4, f"a fix row lacks a scope column: {r}"


def main():
    case("the doc exists with roles/hierarchy/measure/numeric topics",
         t_doc_exists_with_core_topics)
    case("loading/fallback/glyphs/long-strings/native-scaling are checks",
         t_reality_checks_are_checks)
    case("one family or the system face is a complete answer",
         t_one_family_and_system_face_suffice)
    case("content is never shortened for a demo (Cyrillic/RTL/numeric)",
         t_content_never_shortened_for_a_demo)
    case("no CDN, no new package, no fetch required", t_no_cdn_or_package_required)
    case("the scoped before→after fixes table stands", t_scoped_fixes_table)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
