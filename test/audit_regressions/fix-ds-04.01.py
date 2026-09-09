#!/usr/bin/env python3
"""FIX-DS-04.01 — one duration table, one verdict per value (sherlock audit,
DS-04).

The finding: the duration table's modal row allowed 200–500 ms while the very
next rule gated all UI motion at ≤300 ms — a 400 ms modal matched the table
and violated the gate at once, and nothing said which rule wins.

The fix under test (MOTION_DOCTRINE.md): one table keyed by
purpose+frequency+platform, each row carrying a canonical rule ID
(DUR-FEEDBACK … DUR-ENTRANCE); the 300 ms gate is the ceiling of the UI rows;
the only exceptions are explicit rows (DUR-SHEET-MOBILE, DUR-ENTRANCE); the
overlapping 200–500 modal row is gone.

Proven by PARSING the doctrine's own table and running fixtures through it —
the document is the single source a checker would read.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "MOTION_DOCTRINE.md")

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
    """The doctrine's duration table → {id: (lo, hi)} (hi=None: authored)."""
    rows = {}
    for line in read().splitlines():
        m = re.match(r"\|\s*(DUR-[A-Z-]+)\s*\|.*?\|\s*([^|]+?)\s*\|", line)
        if not m:
            continue
        rid, dur = m.group(1), m.group(2)
        rng = re.search(r"(\d+)\s*–\s*(\d+)\s*ms", dur)
        rows[rid] = (int(rng.group(1)), int(rng.group(2))) if rng else (None, None)
    return rows


def verdict(rule_id, ms, table):
    lo, hi = table[rule_id]
    if lo is None:
        return ("PASS", rule_id)          # authored entrance: no numeric ceiling
    return ("PASS" if lo <= ms <= hi else "FAIL", rule_id)


def t_table_has_canonical_ids():
    table = parse_table()
    for rid in ("DUR-FEEDBACK", "DUR-OVERLAY", "DUR-SELECT", "DUR-SPATIAL",
                "DUR-SHEET-MOBILE", "DUR-ENTRANCE"):
        assert rid in table, f"{rid} missing from the table"


def t_400ms_desktop_modal_is_one_unambiguous_fail():
    table = parse_table()
    v, rid = verdict("DUR-SPATIAL", 400, table)
    assert (v, rid) == ("FAIL", "DUR-SPATIAL"), \
        f"a 400 ms desktop modal got {v} under {rid}"
    # and no OTHER ui row would pass it either — the ambiguity is dead
    assert table["DUR-SPATIAL"][1] <= 300, \
        "the desktop spatial row still reaches past the 300 ms gate"


def t_button_and_marketing_entrance_are_distinguished():
    table = parse_table()
    assert verdict("DUR-FEEDBACK", 150, table)[0] == "PASS"
    assert verdict("DUR-ENTRANCE", 500, table)[0] == "PASS", \
        "a 500 ms authored marketing entrance failed"
    assert verdict("DUR-FEEDBACK", 500, table)[0] == "FAIL", \
        "500 ms on a button passed"


def t_mobile_sheet_exception_is_explicit():
    table = parse_table()
    assert table["DUR-SHEET-MOBILE"] == (200, 500)
    d = " ".join(read().split())
    assert "the one spatial exception, and it names its platform" in d
    assert "UI motion stays at or under 300 ms." in d
    assert "That gate is the ceiling of DUR-FEEDBACK through DUR-SPATIAL" in d


def t_overlapping_row_is_gone_and_verdicts_cite_ids():
    d = " ".join(read().split())
    assert "| Modals, drawers, sheets | 200–500 ms |" not in d, \
        "the overlapping modal row survived"
    assert "the verdict cites the row's ID" in d
    assert "FAIL under DUR-SPATIAL" in d


def main():
    case("the table carries the six canonical rule IDs", t_table_has_canonical_ids)
    case("a 400 ms desktop modal is ONE unambiguous FAIL with a rule ID",
         t_400ms_desktop_modal_is_one_unambiguous_fail)
    case("a 150 ms button and a 500 ms authored entrance are distinguished",
         t_button_and_marketing_entrance_are_distinguished)
    case("the mobile-sheet exception is explicit and platform-named",
         t_mobile_sheet_exception_is_explicit)
    case("the overlapping row is gone; verdicts cite IDs",
         t_overlapping_row_is_gone_and_verdicts_cite_ids)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
