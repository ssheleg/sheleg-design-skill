#!/usr/bin/env python3
"""Slop lint for the sheleg-design-skill bundle (stdlib only).

`validate.py` checks that files agree with each other and `validate_palette.py`
checks that the colours are true. Neither catches the third defect class: the
skill shipping the very patterns it tells other people not to ship.

Two halves:

  1. **The bundle obeys its own bans.** Every CSS token layer and every fenced
     example in the shipped docs is read for the forms the doctrine forbids --
     `100vh` where `100dvh` is required, scroll listeners, bare `ease-in`,
     transitions on layout properties, pure black as a field or ink.
  2. **The doctrine is actually there.** A rule that exists only in a commit
     message is not a rule. The tables and named bans the docs promise are
     asserted by string, so deleting one fails the build instead of quietly
     shrinking the contract.

Pack hygiene rides along, and ratchets: a pack authored under the full
thirteen-heading contract must carry an addressable origin. Packs still on the
always-required nine are not held to it -- they are held to it the moment they are
backfilled, which is the point. (The contract is thirteen; "the nine" is only
ever the always-required subset, never a contract an author may ship against.)

Run `--self-test` to watch each check fail against a planted defect.

Exit 0 with "OK (<n> checks)" when clean; 1 with FAIL: lines otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "plugins/sheleg-design/skills/sheleg-design"
STYLES = SKILL_DIR / "styles"
TOKENS = STYLES / "tokens"

failures: list[str] = []
checks = 0


def check(ok, msg):
    global checks
    checks += 1
    if not ok:
        failures.append(msg)
    return ok


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return ""


# --------------------------------------------------------------- banned forms
# Each entry: (label, compiled pattern, why it is a defect).
BANNED = (
    (
        "100vh",
        re.compile(r"(?<![\w-])(?:min-)?height\s*:\s*100vh"),
        "100vh jumps when the mobile address bar moves -- use 100dvh",
    ),
    (
        "scroll listener",
        re.compile(r"addEventListener\(\s*['\"]scroll['\"]"),
        "a scroll listener runs unbatched every frame -- use IntersectionObserver, "
        "useScroll, ScrollTrigger or animation-timeline",
    ),
    (
        "bare ease-in",
        re.compile(r"(?<![\w-])ease-in(?!-out)(?![\w-])"),
        "ease-in delays movement in the moment the user is watching hardest -- "
        "the doctrine bans it in UI",
    ),
    (
        "layout transition",
        re.compile(r"transition\s*:[^;{}]*\b(?:width|height|top|left|margin|padding|gap|font-size)\b"),
        "transitioning a layout property lays out every frame -- animate transform "
        "and opacity",
    ),
    (
        "pure black field or ink",
        re.compile(r"--(?:bg|ink|field)[a-z0-9-]*\s*:\s*#(?:000|000000)\b", re.I),
        "pure black reads as an unfinished default -- packs use an off-black",
    ),
    (
        "scrub with easing",
        re.compile(r"scrub\s*:\s*(?:true|[\d.]+)(?![^}]*ease\s*:\s*['\"]none['\"])[^}]*\bease\s*:\s*['\"](?!none)"),
        "under scrub the scrollbar is already the clock -- ease must be 'none'",
    ),
)

# Fenced code blocks in the shipped docs are examples an agent will copy, so
# they are held to the same bans as the token layers.
FENCE = re.compile(r"```[a-z]*\n(.*?)```", re.S)

# So are inline code spans inside a pack. Twelve of nineteen bundle markdown
# files carry no fenced block at all -- the packs prescribe CSS in backticks,
# in prose -- so scanning fences alone left `styles/*.md` entirely unlinted.
# `atrium.md` prescribed `transition: padding-top .2s` on a sticky header for
# two releases: a layout property, transitioned, on scroll, which is the exact
# form MOTION_DOCTRINE bans, in the bundle that ships the ban.
INLINE = re.compile(r"`([^`\n]+)`")

# A doc may quote a banned form in order to ban it. Suppression is per
# OCCURRENCE and stays on the occurrence's own line (plus the line above, for a
# leading comment), because the old window was 120 characters of preceding text
# for the FIRST match only -- so one decoy "never write this" disabled a ban for
# a whole file, permanently, and every later occurrence went unexamined.
# Watched: an identical `.real { min-height: 100vh; }` in a token layer FAILS
# without the decoy comment and PASSED with it, while the check count dropped
# 224 -> 223.
NEGATION = re.compile(r"(?i)\b(?:never|not|no longer|wrong|banned|forbidden|instead of|avoid)\b")


# A section whose whole job is to enumerate forbidden forms will contain them.
# Scanning it is guaranteed noise, so the exemption is declared by heading --
# narrow, greppable, and impossible to trip by accident -- rather than by
# hoping a negation word happens to sit nearby.
QUOTE_SECTION = re.compile(
    r"(?im)^#{2,4}\s.*\b(?:forbidden|banned|bans|never does|anti-drift)\b.*$"
)


def _quote_zones(text: str) -> list[tuple[int, int]]:
    """Character ranges of sections that exist in order to quote what is banned."""
    zones = []
    for m in QUOTE_SECTION.finditer(text):
        level = len(m.group(0)) - len(m.group(0).lstrip("#"))
        nxt = re.compile(rf"(?m)^#{{1,{level}}}\s").search(text, m.end())
        zones.append((m.start(), nxt.start() if nxt else len(text)))
    return zones


def _suppressed(text: str, start: int, zones: list[tuple[int, int]]) -> bool:
    """True when this occurrence is the doc quoting the form in order to ban it."""
    if any(a <= start < b for a, b in zones):
        return True
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", start)
    line_end = len(text) if line_end == -1 else line_end
    prev_start = text.rfind("\n", 0, line_start - 1) + 1 if line_start else 0
    return bool(NEGATION.search(text[prev_start:line_end]))


def lint_sources():
    # (label, text, zones, allowed_ranges) -- allowed_ranges limits which offsets
    # count, so an inline scan keeps the surrounding prose for suppression
    # instead of being handed a synthetic file of joined spans.
    targets: list[tuple[str, str, list, list]] = []
    for css in sorted(TOKENS.glob("*.css")):
        targets.append((str(css.relative_to(ROOT)), read(css), [], []))
    for md in sorted(SKILL_DIR.rglob("*.md")):
        body = read(md)
        zones = _quote_zones(body)
        for i, block in enumerate(FENCE.findall(body)):
            targets.append((f"{md.relative_to(ROOT)} (example {i + 1})", block, [], []))
        # Inline spans that look like a CSS declaration -- a prescription an
        # implementer will copy verbatim.
        spans = [
            m.span(1) for m in INLINE.finditer(body)
            if ":" in m.group(1) or "addEventListener" in m.group(1)
        ]
        if spans:
            targets.append((f"{md.relative_to(ROOT)} (inline)", body, zones, spans))
    check(bool(targets), "no bundle sources found to lint")
    for rel, text, zones, allowed in targets:
        for label, pattern, why in BANNED:
            # One check per (target, ban), ALWAYS -- never `continue`. A gate
            # whose count falls when a defect is planted cannot be ratcheted,
            # and this one fell twice: once per suppressed ban, once per deleted
            # requirement.
            live = [
                m for m in pattern.finditer(text)
                if (not allowed or any(a <= m.start() < b for a, b in allowed))
                and not _suppressed(text, m.start(), zones)
            ]
            where = "" if not live else f":{text[: live[0].start()].count(chr(10)) + 1}"
            check(not live, f"{rel}{where}: {label} -- {why}")


# ------------------------------------------------------- doctrine completeness

DOCTRINE_REQUIRED = (
    ("frequency table", "100+ times a day"),
    ("keyboard exemption", "keyboard-initiated"),
    ("easing tree", "ease-out"),
    ("ease-in ban", "banned in UI"),
    ("named curves", "--ease-drawer"),
    ("duration table", "100–160 ms"),
    ("duration ceiling", "under 300 ms"),
    ("spring notation", "bounce"),
    ("interruptibility", "keeps its velocity"),
    ("banned scroll listener", 'addEventListener("scroll"'),
    ("banned rAF-to-state", "requestAnimationFrame"),
    ("scrub rule", 'easing must be `none`'),
    ("useGSAP rule", "useGSAP"),
    ("no fabricated motion", "Do not invent motion"),
    ("validate before repeating", "Validate one animation"),
    ("factor repeats", "Factor repeats out"),
    ("transform collision", "collide"),
    ("anti-drift", "Anti-drift"),
    ("reduced motion contract", "prefers-reduced-motion"),
)

SKILL_REQUIRED = (
    ("variance dial", "DESIGN_VARIANCE"),
    ("motion dial", "MOTION_INTENSITY"),
    ("density dial", "VISUAL_DENSITY"),
    ("dial baseline", "Baseline `7 / 5 / 4`"),
    ("dial inference table", "Reading them off the brief"),
    ("three defaults", "defaults, not decisions"),
    ("depth model", "Scene depth"),
    ("dataviz handoff", "dataviz"),
    ("variant harness", "?variant="),
    ("motion doctrine link", "MOTION_DOCTRINE.md"),
)


def lint_doctrine():
    doctrine = read(SKILL_DIR / "MOTION_DOCTRINE.md")
    check(bool(doctrine), "MOTION_DOCTRINE.md: missing or empty")
    for label, needle in DOCTRINE_REQUIRED:
        check(needle in doctrine, f"MOTION_DOCTRINE.md: {label} is gone (looked for {needle!r})")
    skill = read(SKILL_DIR / "SKILL.md")
    for label, needle in SKILL_REQUIRED:
        check(needle in skill, f"SKILL.md: {label} is gone (looked for {needle!r})")


# ------------------------------------------------------------------ pack rules

# "Addressable" means a reader can go and look, not that someone typed a scheme.
# Packs cite their reference the way a person says it -- `graphify.com`,
# `**prowl.chat**` -- so a bare host counts. The extension list keeps filenames
# from reading as hosts: `package.json` and `validate.py` are not references.
NOT_A_HOST = (
    "md", "css", "js", "mjs", "cjs", "json", "py", "sh", "html", "htm",
    "png", "jpg", "jpeg", "svg", "webp", "ts", "tsx", "jsx", "yml", "yaml",
    "toml", "lock", "txt", "log", "map", "cfg", "ini",
)
_HOST = re.compile(r"\b[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)*\.([a-z]{2,})\b", re.I)


def addressable_reference(text: str) -> bool:
    """True when the text names somewhere a reader could actually go."""
    if re.search(r"https?://[^\s)>\]]+", text):
        return True
    return any(m.group(1).lower() not in NOT_A_HOST for m in _HOST.finditer(text))


def lint_packs():
    packs = [p for p in sorted(STYLES.glob("*.md")) if p.name != "STYLE_PACK_TEMPLATE.md"]
    check(bool(packs), "no style packs found")
    for pack in packs:
        rel = pack.relative_to(ROOT)
        text = read(pack)
        # "## Bans" with nothing under it is a heading, not a guard.
        m = re.search(r"^## Bans\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        check(
            m is not None and len(m.group(1).strip()) > 40,
            f"{rel}: '## Bans' is empty or too thin to guard anything",
        )
        # The ratchet: only packs on the widened contract owe an addressable
        # origin. The rest owe it the moment they are backfilled.
        # A heading is a line, not a substring: the core-contract note NAMES the
        # four sections a pack omits, which made three core packs look widened
        # the moment they declared they were not.
        if re.search(r"^## Signature element\s*$", text, re.M):
            origin = re.search(r"^Origin:(.*?)(?=\n\n)", text, re.S | re.M)
            check(
                origin is not None and addressable_reference(origin.group(1)),
                f"{rel}: widened pack must name an addressable origin (a URL), "
                f"not a product name -- provenance nobody can re-read is decorative",
            )


# ----------------------------------------------------------------- self-test


def self_test() -> int:
    global failures, checks
    planted = [
        ("100vh in a token layer", "min-height: 100vh;", "100vh"),
        ("a scroll listener", "window.addEventListener('scroll', onScroll)", "scroll listener"),
        ("bare ease-in", "transition: opacity 200ms ease-in;", "bare ease-in"),
        ("a layout transition", "transition: width 300ms ease-out;", "layout transition"),
        ("pure black ink", "--ink: #000000;", "pure black"),
    ]
    problems = []
    for label, snippet, expected in planted:
        failures, checks = [], 0
        for name, pattern, why in BANNED:
            if pattern.search(snippet):
                check(False, f"planted: {name} -- {why}")
        fired = [f for f in failures if expected in f]
        print(f"  {'caught ' if fired else 'MISSED '} {label}")
        if not fired:
            problems.append(label)
    # Clean CSS must stay silent.
    failures, checks = [], 0
    clean = "--ink: #1a1a1a; min-height: 100dvh; transition: transform 200ms ease-out;"
    for name, pattern, why in BANNED:
        if pattern.search(clean):
            check(False, f"planted: {name}")
    print(f"  {'quiet  ' if not failures else 'NOISY  '} clean CSS")
    if failures:
        problems.append("false positive on clean CSS")

    # Origin addressability, both directions. A pack cites its reference the way
    # a person says it, so requiring a scheme rejects real provenance -- which is
    # exactly what this check did until a neighbouring run's pack tripped it.
    origin_cases = [
        ("a bare host is addressable", "**graphify.com** (2026), read off live computed styles", True),
        ("a full URL is addressable", "https://functionhealth.com — read 2026-08-03", True),
        ("a product name is not", "the Builder Pro AI production design system", False),
        ("a filename is not a host", "values taken from package.json and validate.py", False),
    ]
    for label, sample, expected in origin_cases:
        got = addressable_reference(sample)
        ok = got is expected
        print(f"  {'ok     ' if ok else 'WRONG  '} {label}")
        if not ok:
            problems.append(f"{label}: expected {expected}, got {got}")
    if problems:
        print("\nself-test FAILED: " + "; ".join(problems))
        return 1
    print("\nself-test OK — every ban was watched firing against a planted defect")
    return 0



FLOORS = Path(__file__).resolve().parent / "floors.json"


def check_floor(script: str, count: int) -> int:
    """The ratchet. See test/floors.json for why a falling count is a defect."""
    import json as _json
    try:
        floors = _json.loads(FLOORS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        print(f"FAIL: {FLOORS.name} is missing or unreadable", file=sys.stderr)
        return 1
    floor = floors.get(script)
    if floor is None:
        print(f"FAIL: {FLOORS.name} has no floor for {script}", file=sys.stderr)
        return 1
    if count < floor:
        print(
            f"FAIL: {script} ran {count} checks, below its floor of {floor}. "
            f"Checks do not disappear on their own. If the drop is intended, lower "
            f"the floor in {FLOORS.name} in the same commit, with the reason.",
            file=sys.stderr,
        )
        return 1
    return 0


def main() -> int:
    # argv[0] is a path; `"--self-test" in sys.argv` made any invocation path
    # containing that substring silently run the self-test instead of the lint.
    args = sys.argv[1:]
    if args == ["--self-test"]:
        return self_test()
    if args:
        print(f"FAIL: unknown argument {args[0]!r} (expected --self-test or none)",
              file=sys.stderr)
        return 2
    lint_sources()
    lint_doctrine()
    lint_packs()
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"\n{len(failures)} failure(s) out of {checks} checks")
        return 1
    rc = check_floor("sloplint.py", checks)
    if rc:
        return rc
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
