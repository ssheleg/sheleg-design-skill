#!/usr/bin/env python3
"""Every var() a kit consumes is declared, or carries a fallback.

An undefined custom property does not error — it drops to the initial value, so a
status dot painted with `var(--ok-mark)` when only `--ok` exists renders **transparent**
and every gate stays green. Measured 2026-08-25: four kits shipped exactly that, and the
dot is half of what those packs mean by "status is never by colour alone".

    python3 tools/check_kit_vars.py        # exit 1 on any undeclared use

Two regex traps this file exists to remember, both met while writing it:
  * a declaration is not line-anchored — `--a: x; --b: y;` on one line declares TWO,
    and anchoring to `^` reported 24 false defects in one kit;
  * comments must be stripped first, or a token named in prose counts as a use.
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
USE = re.compile(r"var\(\s*(--[a-z0-9-]+)\s*(?:,([^()]*(?:\([^()]*\)[^()]*)*))?\)")
DECL = re.compile(r"(?:^|[{;])\s*(--[a-z0-9-]+)\s*:", re.M)


def undeclared(css: str) -> collections.Counter:
    body = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    declared = set(DECL.findall(body))
    out = collections.Counter()
    for m in USE.finditer(body):
        if m.group(1) not in declared and m.group(2) is None:
            out[m.group(1)] += 1
    return out


def main() -> int:
    kits = sorted(p for p in (ROOT / "kits").iterdir() if p.is_dir())
    bad, checked = {}, 0
    for kit in kits:
        css = kit / "src" / "styles.css"
        if not css.exists():
            continue
        checked += 1
        miss = undeclared(css.read_text())
        if miss:
            bad[kit.name] = miss
    if not bad:
        print(f"OK ({checked} kits, every var() declared or defaulted)")
        return 0
    total = sum(sum(v.values()) for v in bad.values())
    print(f"FAIL: {total} undeclared var() use(s) with no fallback, across {len(bad)} of {checked} kits")
    for name, miss in bad.items():
        for tok, n in sorted(miss.items()):
            print(f"  kits/{name}/src/styles.css: {tok} used {n}x, never declared "
                  f"— renders as the initial value, silently")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
