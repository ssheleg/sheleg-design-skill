#!/usr/bin/env python3
"""FIX-DS-05.01 — quality checks carry applicability predicates (sherlock
audit, DS-05).

The finding: the Creative Director covers product/agent/native surfaces, yet
the mandatory Quality table demanded "content in served HTML" with no
public/web condition — while the SEO router itself excludes logged-in internal
tools, and a native screen has no served HTML at all.

The fix under test (CREATIVE_DIRECTOR.md):
* every check names its surface class (all / web / public-web / native
  semantics);
* a check outside its class is NOT_APPLICABLE with a reason, never PASS
  without running;
* the predicate rule run as behaviour on the packet's three fixtures: public
  pricing gets the no-JS check, an authenticated admin SPA gets N/A for
  crawler HTML (and loading/error instead), a SwiftUI screen gets no SSR
  demand; contrast/colour checks stay universal.

Proven by PARSING the doctrine's own table. Standard library only.
"""
import os
import re
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


def read():
    with open(DOC, encoding="utf-8") as fh:
        return fh.read()


def parse_table():
    """{check: applies_to} from the doctrine's quality table."""
    rows = {}
    in_table = False
    for line in read().splitlines():
        if line.startswith("| Check | Applies to |"):
            in_table = True
            continue
        if in_table:
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if not m or m.group(1).startswith("---"):
                if not line.startswith("|"):
                    break
                continue
            rows[m.group(1)] = m.group(2)
    return rows


SURFACE_CLASSES = {
    "public-pricing": {"all", "web", "public-web"},
    "admin-spa": {"all", "web"},
    "swiftui-screen": {"all", "native"},
}


def applicable(check_class, surface):
    return check_class in SURFACE_CLASSES[surface]


def t_predicates_parse():
    table = parse_table()
    assert table, "the Applies-to column did not parse"
    assert table.get("Renders without JS") == "public-web"
    assert table.get("Contrast") == "all"
    assert table.get("Loading / error states") == "web"


def t_public_pricing_gets_no_js():
    table = parse_table()
    assert applicable(table["Renders without JS"], "public-pricing"), \
        "public pricing escaped the no-JS check"


def t_admin_spa_is_na_for_crawler_html():
    table = parse_table()
    assert not applicable(table["Renders without JS"], "admin-spa"), \
        "the authenticated admin SPA still gets the crawler-HTML check"
    assert applicable(table["Loading / error states"], "admin-spa"), \
        "the internal surface lost its loading/error check"
    d = " ".join(read().split())
    assert "N/A here (with that reason), not quietly PASSed" in d


def t_native_screen_gets_no_ssr():
    table = parse_table()
    assert not applicable(table["Renders without JS"], "swiftui-screen"), \
        "the SwiftUI screen was handed an SSR requirement"
    d = " ".join(read().split())
    assert "a native screen has no served HTML at all" in d
    assert "VoiceOver order, not DOM order" in d


def t_universal_checks_stay():
    table = parse_table()
    for check in ("Contrast", "Colour is not the only signal"):
        for surface in SURFACE_CLASSES:
            assert applicable(table[check], surface), \
                f"{check} no longer applies to {surface}"


def t_na_never_silent_pass():
    d = " ".join(read().split())
    assert "NOT_APPLICABLE with the reason" in d
    assert "never PASS without running" in d


def main():
    case("the Applies-to predicates parse from the table", t_predicates_parse)
    case("public pricing gets the no-JS check", t_public_pricing_gets_no_js)
    case("the admin SPA is N/A for crawler HTML, gets loading/error instead",
         t_admin_spa_is_na_for_crawler_html)
    case("the SwiftUI screen gets no SSR demand", t_native_screen_gets_no_ssr)
    case("contrast and colour checks stay universal", t_universal_checks_stay)
    case("N/A carries a reason, never a silent PASS", t_na_never_silent_pass)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
