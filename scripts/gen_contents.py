#!/usr/bin/env python3
"""Derive and enforce the `## Contents` list every long bundle reference carries.

The Agent Skills authoring rule this serves: a reference file over 100 lines
carries a `## Contents` list, because that is what a partial read sees. The
family audit (SHD-01, 2026-08-29) found 42 of 44 qualifying files without one —
every style pack and five core references — which is the state a hand-maintained
list always returns to. So the list is DERIVED: the entries are exactly the
file's own `## ` headings, in order, and the gate refuses a file whose list has
drifted from its headings.

    python3 scripts/gen_contents.py            # check; exit 1 + a remedy on drift
    python3 scripts/gen_contents.py --write    # rewrite every stale or missing list

`--write` also propagates: each changed bundle file is copied into the
`.cursor/` mirror, and a changed `STYLE_PACK_TEMPLATE.md` into
`templates/style-pack-template.md`, because the validator holds those pairs
byte-identical and a script that leaves them apart hands the author a red gate.

`test/validate.py` imports `targets()` / `problem()` from here — one derivation,
two callers, no second copy to drift.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "sheleg-design"
BUNDLE_REL = Path("plugins") / PLUGIN / "skills" / PLUGIN
MIRROR_REL = Path(".cursor") / "skills" / PLUGIN

# The spec's threshold: over 100 lines, a partial read needs a map.
LINE_FLOOR = 100
# SKILL.md is the entry point, not a reference — it is read whole, first.
EXEMPT = {"SKILL.md"}

HEADING = re.compile(r"^## (.+?)[ \t]*$", re.M)


def _blank_fences(text: str) -> str:
    """The same text with fenced-code lines blanked, line count preserved.

    A CSS or JS block can hold a line starting `## `; blanking instead of
    deleting keeps line numbers valid for the insertion arithmetic below.
    """
    out, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
        else:
            out.append("" if fenced else line)
    return "\n".join(out)


def headings(text: str) -> list[str]:
    """Every `## ` heading outside a code fence, minus the Contents line itself."""
    return [
        m.group(1)
        for m in HEADING.finditer(_blank_fences(text))
        if m.group(1) != "Contents"
    ]


def expected_block(text: str) -> str:
    return "## Contents\n\n" + "\n".join(f"- {h}" for h in headings(text)) + "\n"


def _span(text: str):
    """(start, end) character span of the existing Contents section, or None.

    The section runs from its `## Contents` line to the next `## ` heading
    (exclusive) or end of file.
    """
    blanked = _blank_fences(text)
    m = re.search(r"^## Contents[ \t]*$", blanked, re.M)
    if not m:
        return None
    nxt = re.compile(r"^## ", re.M).search(blanked, m.end())
    return (m.start(), nxt.start() if nxt else len(text))


def problem(text: str) -> str | None:
    """None when the list is present and derived; otherwise what is wrong."""
    span = _span(text)
    if span is None:
        return "carries no `## Contents` list"
    entries = [
        m.group(1)
        for m in re.finditer(r"^- (.+?)[ \t]*$", text[span[0]:span[1]], re.M)
    ]
    if entries != headings(text):
        return "its `## Contents` list has drifted from the file's own headings"
    return None


def apply(text: str) -> str:
    """The text with its Contents section inserted or rewritten in place."""
    block = expected_block(text)
    span = _span(text)
    if span is not None:
        tail = text[span[1]:]
        return text[: span[0]] + block + ("\n" if tail else "") + tail
    blanked = _blank_fences(text)
    first = HEADING.search(blanked)
    if first is None:
        return text  # no headings at all: nothing to map
    return text[: first.start()] + block + "\n" + text[first.start():]


def targets(root: Path) -> list[Path]:
    bundle = root / BUNDLE_REL
    return sorted(
        p
        for p in bundle.rglob("*.md")
        if p.name not in EXEMPT
        and len((p.read_text(encoding="utf-8")).splitlines()) > LINE_FLOOR
    )


def main() -> int:
    write = sys.argv[1:] == ["--write"]
    if sys.argv[1:] and not write:
        print(f"unknown argument {sys.argv[1]!r} (expected --write or none)", file=sys.stderr)
        return 2
    bundle = ROOT / BUNDLE_REL
    stale = 0
    for path in targets(ROOT):
        text = path.read_text(encoding="utf-8")
        what = problem(text)
        if what is None:
            continue
        stale += 1
        rel = path.relative_to(ROOT)
        if not write:
            print(f"STALE  {rel}: {what}")
            continue
        new = apply(text)
        path.write_text(new, encoding="utf-8")
        mirror = ROOT / MIRROR_REL / path.relative_to(bundle)
        if mirror.parent.is_dir():
            shutil.copyfile(path, mirror)
        if path.name == "STYLE_PACK_TEMPLATE.md":
            template = ROOT / "templates" / "style-pack-template.md"
            if template.is_file():
                shutil.copyfile(path, template)
        print(f"wrote  {rel}")
    if stale and not write:
        print(
            f"\n{stale} file(s) out of contract -- run "
            "`python3 scripts/gen_contents.py --write`"
        )
        return 1
    if not stale:
        print(f"OK -- every >{LINE_FLOOR}-line bundle reference carries a derived Contents list")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
