#!/usr/bin/env python3
"""Regenerate both host-facing manifest descriptions from the pack index.

The family audit (SHD-03, 2026-08-29) found the two descriptions an agent host
reads — `plugin.json`'s and the plugin entry inside `marketplace.json` —
append-scarred: `patchbay` and `nameplate` glossed twice, `deskmate` never
glossed at all, and `chorus`'s entry carrying `deskmate`'s orphaned parenthesis.
That is what a description grown by hand-appending "and <pack> (…)" at every
release converges to. So neither description is authored any more: both are
DERIVED from `STYLE_PACK_INDEX.md`'s catalogue table — the register and good-fit
columns the packs are already chosen by — and `test/validate.py` refuses a
manifest whose description differs from the derivation.

    python3 scripts/gen_manifest_descriptions.py            # check; exit 1 on drift
    python3 scripts/gen_manifest_descriptions.py --write    # rewrite both manifests

Adding a pack: add its catalogue row (the enumeration gate already requires
that), then run `--write` here — `npm run gen-descriptions` is the same thing.
`package.json`'s description stays authored: npmjs.com is a human surface, and
the name-list and count checks already police it.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "sheleg-design"
BUNDLE = Path("plugins") / PLUGIN / "skills" / PLUGIN
INDEX = BUNDLE / "STYLE_PACK_INDEX.md"
PLUGIN_JSON = Path("plugins") / PLUGIN / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = Path(".claude-plugin") / "marketplace.json"

ROW = re.compile(
    r"^\|\s*\[`(?P<name>[a-z0-9-]+)`\]\([^)]*\)\s*\|"
    r"\s*(?P<register>[^|]+?)\s*\|"
    r"\s*(?P<fit>[^|]+?)\s*\|\s*$",
    re.M,
)

_ONES = (
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
).split()
_TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty"}

PREAMBLE = (
    "SHELEG Design methodology: cinematic scroll-driven landing pages (single "
    "scroll clock, layered degrade-to-calm motion, WebGL particle formations), "
    "a motion doctrine that decides whether to animate before it decides how, "
    "and {word} pluggable visual style packs, each with a ready-made token "
    "layer — "
)
TAIL = (
    ". Ships the sheleg-design skill, the architecture reference, the motion "
    "doctrine, the Figma and Claude Design bridges, AI-surface patterns, the "
    "packs' token CSS, and the /sheleg-design command."
)


def number_word(n: int) -> str:
    if 0 <= n < 20:
        return _ONES[n]
    if n in _TENS:
        return _TENS[n]
    tens, ones = divmod(n, 10)
    if tens * 10 in _TENS:
        return f"{_TENS[tens * 10]}-{_ONES[ones]}"
    raise ValueError(f"no number word for {n} -- extend the map")


def _clean(cell: str) -> str:
    """A catalogue cell as plain prose: markers off, markdown off."""
    # ' · **core contract**' / ' · (standalone)' are routing marks, not prose.
    cell = cell.split("·")[0]
    cell = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", cell)
    return cell.replace("**", "").replace("`", "").strip()


def catalogue(root: Path) -> list[tuple[str, str, str]]:
    text = (root / INDEX).read_text(encoding="utf-8")
    table = text.split("## Catalogue", 1)[1].split("## ", 1)[0]
    rows = [
        (m.group("name"), _clean(m.group("register")), _clean(m.group("fit")))
        for m in ROW.finditer(table)
    ]
    packs = sorted(
        p.stem
        for p in (root / BUNDLE / "styles").glob("*.md")
        if p.name != "STYLE_PACK_TEMPLATE.md"
    )
    if sorted(n for n, _, _ in rows) != packs:
        missing = set(packs) - {n for n, _, _ in rows}
        extra = {n for n, _, _ in rows} - set(packs)
        raise SystemExit(
            f"FAIL: STYLE_PACK_INDEX.md catalogue disagrees with styles/ -- "
            f"missing {sorted(missing)}, extra {sorted(extra)}. Fix the index first"
        )
    return rows


def description(root: Path) -> str:
    rows = catalogue(root)
    entries = ", ".join(f"{name} ({register}; {fit})" for name, register, fit in rows)
    return PREAMBLE.format(word=number_word(len(rows))) + entries + TAIL


def _rewrite(path: Path, mutate) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = mutate(data)
    if changed:
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    return changed


def main() -> int:
    write = sys.argv[1:] == ["--write"]
    if sys.argv[1:] and not write:
        print(f"unknown argument {sys.argv[1]!r} (expected --write or none)", file=sys.stderr)
        return 2
    want = description(ROOT)
    drifted = []

    plugin_path = ROOT / PLUGIN_JSON
    plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    if plugin.get("description") != want:
        drifted.append(PLUGIN_JSON)

    market_path = ROOT / MARKETPLACE_JSON
    market = json.loads(market_path.read_text(encoding="utf-8"))
    entry = (market.get("plugins") or [{}])[0]
    if entry.get("description") != want:
        drifted.append(MARKETPLACE_JSON)

    if not drifted:
        print("OK -- both manifest descriptions match the derivation from STYLE_PACK_INDEX.md")
        return 0
    if not write:
        for rel in drifted:
            print(f"STALE  {rel}: description differs from the STYLE_PACK_INDEX.md derivation")
        print("\nrun `python3 scripts/gen_manifest_descriptions.py --write` (npm run gen-descriptions)")
        return 1

    def set_plugin(data):
        if data.get("description") == want:
            return False
        data["description"] = want
        return True

    def set_market(data):
        e = (data.get("plugins") or [{}])[0]
        if e.get("description") == want:
            return False
        e["description"] = want
        return True

    if _rewrite(plugin_path, set_plugin):
        print(f"wrote  {PLUGIN_JSON}")
    if _rewrite(market_path, set_market):
        print(f"wrote  {MARKETPLACE_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
