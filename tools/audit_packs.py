#!/usr/bin/env python3
"""Audit every style pack against the collection rule — the half the gates cannot see.

`test/validate.py` checks that a pack is structurally whole and routed; the palette gate
recomputes its ratios. Neither can tell you HOW a pack was measured, whether its source
is still reachable, or whether its kit was ever rendered. This does, and it reports
per-pack rather than as a score.

    python3 tools/audit_packs.py                 # table to stdout
    python3 tools/audit_packs.py --json          # machine-readable
    python3 tools/audit_packs.py --check-live    # also probe each Origin (network)

Exit code is 0 always: this is a report, not a gate. A gap here is a decision to make,
not a build to fail — several are recorded exceptions in the packs themselves.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
STYLES = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles"

# Rule 7 — "read the render, not the stylesheet". These are the phrases a pack uses when
# it did; a pack measured only off a stylesheet cannot honestly write any of them.
READ_RENDER = re.compile(r"computed styles?|getComputedStyle|\bCDP\b|live computed|"
                         r"computed on the live page|off the render", re.I)
# A narrow-width measurement, however the pack spells it.
NARROW = re.compile(r"\b(390|375|360)\s*(?:[x×]\s*\d{3,4})?\b(?![\d.])")
# A pack that says which stylesheets it counted — the authored/vendor question. Only
# meaningful where the reference HAS vendor CSS, so this is reported, never scored.
COUNTED_WHICH = re.compile(r"authored|vendor|Bootstrap|Tailwind|purchased|shipped stylesheet|"
                           r"stylesheets? (?:it|they) resolve|distinct stylesheets", re.I)
# An Origin that a reader can open: a URL, or a bare host with a dot in it.
ADDRESSABLE = re.compile(r"https?://\S+|\b[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)+\b")
# The packs that say so themselves rather than pretending otherwise.
RECORDED_EXCEPTION = re.compile(r"names a product rather than an address", re.I)
ANONYMISED = re.compile(r"anonymi[sz]ed at the owner's request", re.I)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def head_paragraphs(text: str, n: int = 3) -> str:
    return "\n\n".join(text.split("\n\n")[:n])


def probe(url: str, timeout: float = 12.0) -> str:
    """A reachability label, never an exception: link rot is data, not a crash."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return f"{r.status}"
    except urllib.error.HTTPError as e:
        return f"{e.code}"
    except Exception as e:
        return type(e).__name__


def collect(check_live: bool = False) -> list[dict]:
    scenarios = (ROOT / "test/scenarios.md").read_text()
    changelog = (ROOT / "CHANGELOG.md").read_text()
    out = []
    for md in sorted(STYLES.glob("*.md")):
        if md.stem == "STYLE_PACK_TEMPLATE":
            continue
        name = md.stem
        text = md.read_text()
        css = STYLES / "tokens" / f"{name}.css"
        csst = css.read_text() if css.exists() else ""
        origin_block = ""
        m = re.search(r"^Origin:(.*?)(?=\n\nContract:|\n## )", text, re.S | re.M)
        if m:
            origin_block = m.group(1)
        provenance = head_paragraphs(text) + "\n" + csst[:6000]

        url = ""
        mu = re.search(r"https?://[^\s,)]+", origin_block)
        if mu:
            url = mu.group(0).rstrip(".,)>")
        elif ADDRESSABLE.search(re.sub(r"`[^`]*`", "", origin_block)):
            host = ADDRESSABLE.search(re.sub(r"`[^`]*`", "", origin_block)).group(0)
            url = f"https://{host}" if "." in host and not host.startswith("http") else ""

        out.append({
            "name": name,
            "added": git("log", "--diff-filter=A", "--format=%ad", "--date=short", "-1", "--", str(md)),
            "contract": (re.search(r"^Contract:\s*(\w+)", text, re.M) or [None, "?"])[1],
            "origin_url": url,
            "addressable": bool(url),
            "recorded_exception": bool(RECORDED_EXCEPTION.search(text)),
            "anonymised": bool(ANONYMISED.search(text)),
            "read_render": bool(READ_RENDER.search(provenance)),
            "narrow_measured": bool(NARROW.search(provenance)) or bool(NARROW.search(text)),
            "names_which_css": bool(COUNTED_WHICH.search(provenance)),
            # step 8 exists only from 1.48.1; evidence for a pack is a CHANGELOG sentence
            # putting this pack and a render in the same breath.
            "kit_render_on_record": bool(
                re.search(rf"`?{name}`?[^.]{{0,300}}render|render[^.]{{0,300}}`?{name}`?",
                          changelog, re.I | re.S)),
            "named_in_scenarios": name in scenarios,
            "live": probe(url) if (check_live and url) else "",
        })
    return out


def table(rows: list[dict]) -> str:
    def mark(b): return "yes" if b else "—"
    w = max(len(r["name"]) for r in rows) + 1
    head = (f'{"pack":<{w}} {"added":<11} {"contract":<9} {"render":<7} {"narrow":<7} '
            f'{"which css":<10} {"kit rendered":<13} {"origin":<9} live')
    lines = [head, "-" * len(head)]
    for r in rows:
        origin = "address" if r["addressable"] else ("recorded" if r["recorded_exception"] else "MISSING")
        lines.append(f'{r["name"]:<{w}} {r["added"]:<11} {r["contract"]:<9} '
                     f'{mark(r["read_render"]):<7} {mark(r["narrow_measured"]):<7} '
                     f'{mark(r["names_which_css"]):<10} {mark(r["kit_render_on_record"]):<13} '
                     f'{origin:<9} {r["live"]}')
    n = len(rows)
    lines += ["", f"{n} packs · "
              f'{sum(r["read_render"] for r in rows)} read off the render · '
              f'{sum(r["narrow_measured"] for r in rows)} measured narrow · '
              f'{sum(r["kit_render_on_record"] for r in rows)} kit renders on record · '
              f'{sum(r["addressable"] for r in rows)} addressable origins '
              f'({sum(r["recorded_exception"] for r in rows)} recorded exceptions)']
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check-live", action="store_true", help="probe each Origin over the network")
    a = ap.parse_args()
    rows = collect(a.check_live)
    print(json.dumps(rows, indent=1) if a.json else table(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
