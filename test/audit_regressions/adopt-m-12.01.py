#!/usr/bin/env python3
"""ADOPT-M-12.01 — a11y evidence wired from the design entry (sherlock audit;
depends on ADOPT-M-11.01's ACCESSIBILITY_EVIDENCE.md).

The adoption: the design entry connects the accessibility-evidence contract at
the scopes where a claim is made (the craft gate's contrast row, the render
critique) through EXISTING capability — no new global router, no new entry
point — and visual judgment is never passed off as WCAG conformance: a
conformance row needs a computed, scoped check naming its criterion.

Acceptance, run both ways: the link resolves; a receipt where a glance
produced a conformance row is refused, while a computed check passes and an
absent tool stays NOT_RUN.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")
SKILL = os.path.join(SKILL_DIR, "SKILL.md")

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


# ------------------------------------------------------------------ the doctrine


def t_link_resolves_and_the_scope_is_stated():
    text = open(SKILL, encoding="utf-8").read()
    m = re.search(r"\[`ACCESSIBILITY_EVIDENCE\.md`\]\(\./(ACCESSIBILITY_EVIDENCE\.md)\)", text)
    assert m, "the entry no longer links the evidence contract"
    assert os.path.isfile(os.path.join(SKILL_DIR, m.group(1))), "the link does not resolve"
    flat = " ".join(text.split())
    for needle in ("The connection is **scoped, not routed**",
                   "an existing capability, no new router, no new entry point",
                   "A glance cannot produce a conformance row"):
        assert needle in flat, f"the entry no longer states {needle!r}"


def t_no_new_global_router():
    """The description (the routing surface) gained no a11y trigger — the
    connection rides the existing design entry, it does not compete with it."""
    text = open(SKILL, encoding="utf-8").read()
    front = text.split("---")[1]
    desc = next(l for l in front.splitlines() if l.startswith("description:"))
    for trigger in ("accessibility", "a11y", "wcag", "доступность"):
        assert trigger not in desc.lower(), \
            f"the description grew an {trigger!r} trigger — that is a new router"


# --------------------- the receipt rule, run as documented behaviour


BASES = {"glance", "computed-ratio", "dom-tool", "absent-tool"}


def receipt_row(kind, basis, criterion=None):
    """Exactly the documented rule: what a row is allowed to claim, given how
    it was produced."""
    assert kind in ("visual-judgment", "wcag-conformance") and basis in BASES
    if kind == "visual-judgment":
        return {"kind": kind, "verdict": "recorded"}
    # wcag-conformance:
    if basis == "glance":
        return {"kind": kind, "verdict": "REFUSED",
                "why": "a glance cannot produce a conformance row"}
    if basis == "absent-tool":
        return {"kind": kind, "verdict": "NOT_RUN"}
    if not criterion:
        return {"kind": kind, "verdict": "REFUSED", "why": "no criterion named"}
    return {"kind": kind, "verdict": "PASS", "criterion": criterion}


def t_glance_cannot_produce_conformance():
    row = receipt_row("wcag-conformance", "glance")
    assert row["verdict"] == "REFUSED", f"a glance produced a conformance row: {row}"
    ok = receipt_row("wcag-conformance", "computed-ratio", criterion="1.4.3 AA")
    assert ok["verdict"] == "PASS" and ok["criterion"] == "1.4.3 AA"


def t_conformance_needs_its_criterion():
    row = receipt_row("wcag-conformance", "computed-ratio")
    assert row["verdict"] == "REFUSED" and "criterion" in row["why"], \
        f"a conformance row without a criterion passed: {row}"


def t_absent_tool_stays_not_run():
    row = receipt_row("wcag-conformance", "absent-tool")
    assert row["verdict"] == "NOT_RUN" and row["verdict"] != "PASS"


def t_visual_judgment_still_welcome():
    """The split is not a ban: how the render reads is recorded — as itself."""
    row = receipt_row("visual-judgment", "glance")
    assert row["verdict"] == "recorded", f"visual judgment was refused: {row}"


def main():
    case("the link resolves and the scoped connection is stated",
         t_link_resolves_and_the_scope_is_stated)
    case("no new global router on the description surface", t_no_new_global_router)
    case("a glance cannot produce a conformance row", t_glance_cannot_produce_conformance)
    case("a conformance row names its criterion", t_conformance_needs_its_criterion)
    case("an absent tool stays NOT_RUN", t_absent_tool_stays_not_run)
    case("visual judgment is recorded as itself", t_visual_judgment_still_welcome)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
