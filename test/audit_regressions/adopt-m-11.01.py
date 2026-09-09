#!/usr/bin/env python3
"""ADOPT-M-11.01 — standards-vs-heuristics accessibility reference (sherlock audit).

The adoption: an evidence contract for accessibility claims. A WCAG criterion
(number, version, level, units, exceptions) is not a design heuristic; a
browser screenshot does not prove DOM/assistive-technology behaviour; a check
whose tool is absent reports NOT_RUN, never PASS; and nothing auto-installs
axe to convert a NOT_RUN into a verdict.

The acceptance, run as behaviour: the decision rules exactly as the shipped
doctrine states them — pt-vs-px conversion, the large-text boundary, the AA/AAA
target-size split — driven over the audit's counterexample cases:

* 18px normal at 3:1 FAILS (13.5pt is not large text);
* 24px normal at 3:1 passes — the 18pt boundary exactly;
* a 24px target passes AA (2.5.8) and fails AAA (2.5.5) — two different claims;
* a DOM/AT check with no tool available is NOT_RUN, and NOT_RUN is not PASS;
* no shipped text or script auto-installs axe.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")
DOC = os.path.join(SKILL_DIR, "ACCESSIBILITY_EVIDENCE.md")

checks = 0
failures = []


def case(name, fn):
    global checks
    try:
        fn()
        checks += 1
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


# ------------------------------------------------------- the doctrine, as shipped


def t_doctrine_ships_and_is_linked():
    assert os.path.isfile(DOC), "ACCESSIBILITY_EVIDENCE.md is missing"
    text = open(DOC, encoding="utf-8").read()
    for needle in ("1.4.3", "1.4.6", "1.4.11", "2.5.8", "2.5.5",
                   "4.5:1", "3:1", "24×24 CSS px", "44×44 CSS px",
                   "pt, not px", "NOT_RUN, never PASS", "Never auto-install axe",
                   "proves **nothing** about the DOM"):
        assert needle in text, f"the doctrine no longer states {needle!r}"
    skill = open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8").read()
    assert "ACCESSIBILITY_EVIDENCE.md" in skill, "SKILL.md never links the doctrine"


# ------------------- the decision rules exactly as the doctrine states them


PX_PER_PT = 4.0 / 3.0  # 1pt = 4/3 px at 96dpi — the conversion the doctrine names


def is_large_text(px, bold=False):
    pt = px / PX_PER_PT
    return pt >= 18 or (bold and pt >= 14)


def contrast_verdict(ratio, px, bold=False, level="AA"):
    if level == "AA":
        need = 3.0 if is_large_text(px, bold) else 4.5
    else:  # AAA, 1.4.6
        need = 4.5 if is_large_text(px, bold) else 7.0
    return "PASS" if ratio >= need else "FAIL"


def target_verdict(size_px, level="AA"):
    need = 24 if level == "AA" else 44
    return "PASS" if size_px >= need else "FAIL"


def at_check(tool_available):
    """A DOM/assistive-technology claim: only a tool that reads the tree testifies."""
    return "PASS" if tool_available else "NOT_RUN"


def t_18px_normal_at_3_to_1_fails():
    assert not is_large_text(18), "18px (13.5pt) was classed as large text"
    assert contrast_verdict(3.0, 18) == "FAIL", \
        "18px normal at 3:1 passed AA — the px-as-pt trap the doctrine names"
    assert contrast_verdict(4.5, 18) == "PASS"


def t_24px_normal_is_the_boundary():
    assert is_large_text(24), "24px (18pt exactly) was not classed as large"
    assert contrast_verdict(3.0, 24) == "PASS", "the 18pt boundary case failed at 3:1"
    assert contrast_verdict(3.0, 23.9) == "FAIL", "23.9px slipped over the boundary"
    # bold moves the threshold: 14pt bold ≈ 18.67px
    assert contrast_verdict(3.0, 18.7, bold=True) == "PASS"
    assert contrast_verdict(3.0, 18.7, bold=False) == "FAIL"


def t_aa_target_is_not_the_enhanced_target():
    aa, aaa = target_verdict(24, "AA"), target_verdict(24, "AAA")
    assert (aa, aaa) == ("PASS", "FAIL"), \
        f"a 24px target must pass AA (2.5.8) and fail AAA (2.5.5): got {(aa, aaa)}"
    assert target_verdict(44, "AAA") == "PASS"
    assert target_verdict(23, "AA") == "FAIL"


def t_absent_tool_is_not_run_never_pass():
    assert at_check(tool_available=False) == "NOT_RUN"
    assert at_check(tool_available=False) != "PASS", "an absent tool testified"
    assert at_check(tool_available=True) == "PASS"


def t_nothing_auto_installs_axe():
    """No shipped script or doctrine line INSTALLS axe; naming the ban is allowed."""
    install_re = re.compile(r"(npm\s+(?:install|i)\s+[^\n]*axe|pip\s+install\s+[^\n]*axe)", re.I)
    hits = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "plugins")):
        dirnames[:] = [d for d in dirnames if d not in ("node_modules", "__pycache__")]
        for name in filenames:
            if not name.endswith((".md", ".py", ".js", ".sh", ".json")):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8", errors="ignore") as fh:
                for i, line in enumerate(fh, 1):
                    if install_re.search(line):
                        hits.append(f"{os.path.relpath(path, ROOT)}:{i}")
    assert not hits, f"a shipped file installs axe: {hits}"


def main():
    case("the doctrine ships with its exact bars and is linked", t_doctrine_ships_and_is_linked)
    case("18px normal at 3:1 fails AA", t_18px_normal_at_3_to_1_fails)
    case("24px normal is the large-text boundary", t_24px_normal_is_the_boundary)
    case("a 24px target: AA pass, AAA fail — different claims", t_aa_target_is_not_the_enhanced_target)
    case("an absent tool is NOT_RUN, never PASS", t_absent_tool_is_not_run_never_pass)
    case("nothing shipped auto-installs axe", t_nothing_auto_installs_axe)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
