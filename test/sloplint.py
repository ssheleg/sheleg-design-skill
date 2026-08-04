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

Pack hygiene rides along, and ratchets: a pack authored under the widened
contract must carry an addressable origin. Packs still on the nine-heading
contract are not held to it -- they are held to it the moment they are
backfilled, which is the point.

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
        re.compile(r"transition\s*:[^;{}]*\b(?:width|height|top|left|margin)\b"),
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


def lint_sources():
    targets: list[tuple[str, str]] = []
    for css in sorted(TOKENS.glob("*.css")):
        targets.append((str(css.relative_to(ROOT)), read(css)))
    for md in sorted(SKILL_DIR.rglob("*.md")):
        body = read(md)
        for i, block in enumerate(FENCE.findall(body)):
            targets.append((f"{md.relative_to(ROOT)} (example {i + 1})", block))
    check(bool(targets), "no bundle sources found to lint")
    for rel, text in targets:
        for label, pattern, why in BANNED:
            hit = pattern.search(text)
            # A doc may quote a banned form in order to ban it. The quote lives
            # in prose, not in an example, so only fenced blocks are scanned --
            # but a doctrine example may still show the wrong way beside the
            # right way, marked as such.
            if hit and re.search(r"(?i)\b(?:never|not|wrong|banned|instead of)\b", text[max(0, hit.start() - 120) : hit.start()]):
                continue
            check(hit is None, f"{rel}: {label} -- {why}")


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

URL = re.compile(r"https?://[^\s)>\]]+")


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
        if "## Signature element" in text:
            origin = re.search(r"^Origin:(.*?)(?=\n\n)", text, re.S | re.M)
            check(
                origin is not None and URL.search(origin.group(1)) is not None,
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
    if problems:
        print("\nself-test FAILED: " + "; ".join(problems))
        return 1
    print("\nself-test OK — every ban was watched firing against a planted defect")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    lint_sources()
    lint_doctrine()
    lint_packs()
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"\n{len(failures)} failure(s) out of {checks} checks")
        return 1
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
