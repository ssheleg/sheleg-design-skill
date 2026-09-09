#!/usr/bin/env python3
"""FIX-DS-01.01 — the semantic token adapter (sherlock audit, finding DS-01).

The finding: pack comparison "by swapping the CSS" had no shared token API —
only --bg and --ink resolve in every pack, and an undefined custom property
does not error, it silently falls back, so the comparison compared fallbacks.

The fix under test: each compared pack's token file ends with an @adapter
block mapping the ten semantic roles onto its own tokens, or declaring a role
@absent; a role neither mapped nor declared is a MISSING token caught BEFORE
comparison. Workbench and orchard carry complete adapters; every mapped
target resolves to a token the pack actually defines.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")
TOKENS = os.path.join(SKILL_DIR, "styles", "tokens")

CONTRACT = ["--sem-surface", "--sem-surface-raised", "--sem-text", "--sem-text-muted",
            "--sem-line", "--sem-primary", "--sem-on-primary",
            "--sem-positive", "--sem-caution", "--sem-negative"]

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def audit_pack(css_text):
    """The pre-comparison check, exactly as documented: every contract role is
    mapped (to a token the pack defines) or declared @absent; anything else is
    MISSING and blocks."""
    defined = set(re.findall(r"^\s*(--[a-z0-9-]+)\s*:", css_text, re.M))
    mapped = dict(re.findall(r"^\s*(--sem-[a-z0-9-]+)\s*:\s*var\((--[a-z0-9-]+)\)", css_text, re.M))
    absent = set(re.findall(r"(--sem-[a-z0-9-]+)", " ".join(re.findall(r"@absent([^*]*)", css_text))))
    problems = []
    for role in CONTRACT:
        if role in mapped:
            if mapped[role] not in defined:
                problems.append(f"{role} maps to {mapped[role]}, which the pack never defines")
        elif role in absent:
            pass
        else:
            problems.append(f"{role} is neither mapped nor declared absent — MISSING")
    return problems


def t_skill_md_names_the_contract():
    text = " ".join(open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8").read().split())
    for needle in ("The mounting rides the semantic token contract",
                   "or declaring a role `@absent`",
                   "blocks the comparison BEFORE any render",
                   "a comparison built on silent fallbacks compares the fallbacks",
                   "No CSS-swap promise follows"):
        assert needle in text, f"SKILL.md no longer states {needle!r}"
    for role in CONTRACT:
        assert f"`{role}`" in text, f"SKILL.md does not name {role}"


def t_workbench_maps_everything():
    css = open(os.path.join(TOKENS, "workbench.css"), encoding="utf-8").read()
    v = audit_pack(css)
    assert v == [], f"workbench adapter incomplete: {v}"
    import re as _re
    assert not _re.search(r"@absent\s+--sem-", css), \
        "workbench declared a role absent that it can map"


def t_orchard_maps_core_and_declares_status_absent():
    css = open(os.path.join(TOKENS, "orchard.css"), encoding="utf-8").read()
    v = audit_pack(css)
    assert v == [], f"orchard adapter incomplete: {v}"
    for role in ("--sem-positive", "--sem-caution", "--sem-negative"):
        assert role in css and "@absent" in css, f"orchard's missing {role} is not DECLARED"
        assert not re.search(rf"^\s*{role}\s*:", css, re.M), \
            f"orchard both maps and declares {role} absent"


def t_missing_token_is_caught_before_comparison():
    broken = "\n".join([":root {", "  --bg:#fff;", "  --ink:#000;",
                        "  --sem-surface: var(--bg);", "  --sem-text: var(--ink);", "}"])
    v = audit_pack(broken)
    assert any("MISSING" in x for x in v), f"an undeclared role slipped through: {v}"
    dangling = broken.replace("var(--bg)", "var(--ghost)")
    v2 = audit_pack(dangling)
    assert any("never defines" in x for x in v2), f"a dangling mapping slipped through: {v2}"


def t_kits_carry_the_adapter():
    for pack in ("workbench", "orchard"):
        kit = os.path.join(ROOT, "kits", pack, "src", "styles.css")
        assert "@adapter" in open(kit, encoding="utf-8").read(), \
            f"the {pack} kit's token block lost the adapter (run npm run sync-kits)"


def main():
    case("SKILL.md names the contract and its rules", t_skill_md_names_the_contract)
    case("workbench maps all ten roles", t_workbench_maps_everything)
    case("orchard maps the core and declares status absent", t_orchard_maps_core_and_declares_status_absent)
    case("a missing or dangling role is caught before comparison", t_missing_token_is_caught_before_comparison)
    case("the materialized kits carry the adapter", t_kits_carry_the_adapter)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
