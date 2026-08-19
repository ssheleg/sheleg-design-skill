#!/usr/bin/env python3
"""Consistency validator for the sheleg-design-skill repo (stdlib only).

The repo's defect class is contradiction *between* files, so every promise one
file makes is checked against the file that has to keep it:

  1. Manifests parse, required fields present, four-way version sync
     (marketplace.json / plugin.json / package.json / CHANGELOG top entry).
  2. Every skill has front-matter: name (matching its directory) + description,
     and the description canon: opens with "Use when", carries Russian trigger
     aliases, front-matter under 1024 characters.
  3. The reference doc SHELEG_DESIGN.md ships next to SKILL.md, and the whole
     .cursor/ mirror matches the plugin bundle file-by-file, both directions.
  4. Every style pack carries the full section contract and a ready-made
     tokens/<pack>.css, is routed from the SKILL.md table and named in the CLI
     output; the shipped pack skeleton matches templates/.
  5. Every command has front-matter: description.
  6. Every cursor rule (.mdc) has front-matter: alwaysApply, and description
     unless alwaysApply is true; no relative links (rules travel alone).
  7. install.sh ships exactly the bundle, and bin/cli.js walks it at runtime.
  8. Relative markdown links inside the repo resolve.

Exit code 0 with "OK (<n> checks)" when clean; 1 with FAIL: lines otherwise.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# The self-test plants a defect in a COPY of the tree and re-runs this file
# against it, so every check is exercised exactly as CI runs it rather than by a
# re-implementation that can drift from the thing it is testing.
ROOT = Path(os.environ.get("SHELEG_ROOT") or Path(__file__).resolve().parent.parent)
PLUGIN = "sheleg-design"
PLUGIN_DIR = f"plugins/{PLUGIN}"
# The pack contract is THIRTEEN headings, plus "## Motion flavor" for a
# cinematic pack. These nine are the always-required floor; the four in
# PACK_SECTIONS_WIDENED_ONLY are the rest, enforced all-or-nothing below.
#
# One name, one number, everywhere. Say "the thirteen-heading contract" and
# nothing else: this repo shipped "nine", "ten" and "thirteen" simultaneously
# across DOCMAP, DESIGN_SYNC_BRIDGE, scenarios.md, CONTRIBUTING and this
# docstring, and one of those sites actively instructed an author to ship a
# nine-heading pack -- which the gate then passed, because nine is the floor.
# validate_contract_terminology() now fails on the stale spellings.
PACK_SECTIONS = (
    "## Register",
    "## Palette",
    "## Type",
    "## Texture & surface",
    "## Motion tokens",
    "## Signature motifs",
    "## Micro-interactions",
    "## Bans",
    "## Gotchas",
)

# The widened contract (1.5.0). Four sections were added after an audit found the
# packs specified colour and motion precisely and then went quiet exactly where
# implementations drift: per-component states, the opening viewport, collapse
# behaviour, and the one element the page is remembered by.
#
# The skeleton carries all thirteen from the moment it is widened -- a template
# that teaches nine while the contract wants thirteen is worse than no template.
#
# The packs that shipped before the widening stay on the nine -- there were six of
# them when this paragraph was written on 2026-08-04 and the number has moved
# since, so it is computed and printed rather than repeated here. Backfilling them
# honestly needs re-reading each pack's live reference, and three of them record
# a product name where an address belongs, so three cannot be re-read at all.
# Filling those sections from the token layer instead would be inventing values
# with a citation attached -- the exact failure the pack layer exists to prevent.
# Held rather than faked (operator, 2026-08-04).
#
# So the gate is all-or-nothing rather than staged. Nine are always required.
# Touch one of the four widened sections and you owe all four -- which closes the
# dead zone where a new pack copies the thirteen-heading skeleton, keeps the easy
# nine, and still passes. There is no version of a pack that is half-widened.
PACK_SECTIONS_WIDENED_ONLY = (
    "## Components",
    "## Hero",
    "## Responsive",
    "## Signature element",
)
PACK_SECTIONS_WIDE = PACK_SECTIONS + PACK_SECTIONS_WIDENED_ONLY

# The Claude Design bridge covers four reference types plus the border; each is a
# heading, so "we documented design-sync" stops being a claim and becomes a check.
BRIDGE_SECTIONS = (
    "## 1. What crosses, and in what shape",
    "## 2. Style packs — the pack is the source of truth",
    "## 3. Figma — one border at a time",
    # The heading names every server in the slot on purpose: 1.12.1 shipped it
    # reading "(Lazyweb MCP)" after Mobbin had joined, and a heading is a
    # discovery surface -- an agent skimming them concluded Mobbin was not there.
    # Pinning the whole string here is what makes a third server a gate failure
    # rather than a silent omission.
    "## 4. Reference sweeps (Lazyweb, Mobbin, Refero) — layout crosses, identity does not",
    "## 5. Live-site extraction — the pack first, the sync second",
    "## 6. What cannot cross",
    "## 7. Round-trip discipline",
)

SPINE = ("Button", "Card", "Chip", "Stat", "Heading", "Rule")
CARD_GROUPS = ("Foundations", "Actions", "Surfaces", "Data", "Signature")
COLOR_LITERAL = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|oklch\(")
PROPS_RE = re.compile(
    r"export\s+interface\s+(\w+Props)\s*\{(.*?)^\}", re.S | re.M
)
CATEGORY_RE = re.compile(r"^category:\s*(\S+)\s*$", re.M)

failures = []
checks = 0
# Figures this run measured. A number that appears here is never also written into
# a comment or a document: the comments below say what was measured and WHEN, and
# the current value prints. Three stale tallies in this file were the argument for
# it -- "the six packs shipped before the widening" (seven, since `awning`) and
# "seven of the ten widened packs" (twenty-two widened now), both true once.
report: list[str] = []


def check(ok, msg):
    global checks
    checks += 1
    if not ok:
        failures.append(msg)
    return ok


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None



def raw_front_matter(path) -> str:
    """The front-matter block verbatim -- what an agent host actually loads."""
    text = read(path) or ""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return "" if end == -1 else text[4:end]


def check_description_canon(rel, path, desc: str) -> None:
    """The three canon rules every skill description must satisfy."""
    check(
        desc.startswith("Use when"),
        f"{rel}/SKILL.md: description must start with 'Use when' (canon)",
    )
    check(
        bool(re.search(r"[а-яё]", desc, re.I)),
        f"{rel}/SKILL.md: description must carry Russian trigger aliases beside the English ones (canon)",
    )
    # Two budgets, not one -- and this RAISES the total ceiling from 1024 to
    # 1280, which is a loosening and is recorded as one rather than as a tidy-up.
    #
    # The old check capped the WHOLE front-matter at 1024 and called it canon.
    # 1024 is the Agent Skills limit on `description` alone, so the old check was
    # stricter than the standard it claimed to implement, and it conflated the
    # number that governs discovery with the bookkeeping keys beside it. The
    # conflation had a cost the moment it was tested: a 24-character
    # `metadata.version` consumed the description's remaining headroom, and board
    # row B-006 -- widen the description, which today has no trigger for decks,
    # the motion doctrine or design-sync -- would have been blocked by a ceiling
    # that does not exist upstream.
    #
    # The 256 is a budget, not a measurement: `name` + `license` + `metadata`
    # is 74 characters today, so it is roughly three times the current need and
    # will fail long before front-matter becomes a place to write prose.
    check(
        len(desc) <= 1024,
        f"{rel}/SKILL.md: description is {len(desc)} chars, the spec limit is 1024",
    )
    raw = raw_front_matter(path)
    overhead = len(raw) - len(desc)
    check(
        overhead <= 256,
        f"{rel}/SKILL.md: front-matter carries {overhead} chars besides the "
        "description, budget is 256 -- everything here is read every session, so "
        "keys other than the description stay bookkeeping-sized",
    )


def front_matter(path):
    """Parse a leading ----delimited front-matter block into a flat dict."""
    text = read(path)
    if text is None or not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    data = {}
    for line in text[3:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip().strip('"').strip("'")
        if value.lower() in ("true", "false"):
            data[key.strip()] = value.lower() == "true"
        else:
            data[key.strip()] = value
    return data


def load_json(rel, required):
    path = ROOT / rel
    text = read(path)
    if not check(text is not None, f"{rel}: missing"):
        return None
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        check(False, f"{rel}: invalid JSON ({exc})")
        return None
    for field in required:
        check(field in data, f"{rel}: missing required field '{field}'")
    return data


def changelog_version():
    text = read(ROOT / "CHANGELOG.md")
    if not check(text is not None, "CHANGELOG.md: missing"):
        return None
    match = re.search(r"^## \[?(\d+\.\d+\.\d+)\]?", text, re.MULTILINE)
    check(match is not None, "CHANGELOG.md: no '## [x.y.z]' release heading")
    return match.group(1) if match else None


def skill_metadata_version():
    """The version the SHIPPED bundle carries, read from `metadata.version`.

    Parsed with an explicit nested pattern rather than through front_matter():
    that parser is flat, so it would also accept a bare top-level `version:`
    key -- which is not a legal Agent Skills front-matter key and would pass
    here while failing an install-time validator.

    The bundle exists without the repo. `DESIGN_SYNC_BRIDGE.md` §7 tells the
    reader to record the pack version in the synced project so staleness can be
    answered without guessing, and until 1.11.0 there was no version anywhere in
    the bundle to read: the only version strings were historical ("until 1.10.0
    the header rule read ..."). A rule whose input does not ship is not a rule.
    """
    rel = f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md"
    text = read(ROOT / rel) or ""
    head = text.split("\n---", 1)[0] if text.startswith("---") else ""
    match = re.search(
        r"^metadata:[ \t]*\n(?:[ \t]+[^\n]*\n)*?[ \t]+version:[ \t]*(\d+\.\d+\.\d+)[ \t]*$",
        head,
        re.MULTILINE,
    )
    check(
        match is not None,
        f"{rel}: front-matter must carry a nested 'metadata.version' -- the "
        "bundle ships without the repo, so a rule that says to record the pack "
        "version has nothing to read",
    )
    return match.group(1) if match else None


def validate_manifests():
    marketplace = load_json(
        ".claude-plugin/marketplace.json",
        ["name", "owner", "description", "plugins"],
    )
    plugin = load_json(
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        ["name", "description", "version", "license"],
    )
    package = load_json("package.json", ["name", "version", "bin", "files", "license"])
    if package:
        check(
            package.get("name") == "sheleg-design-skill",
            "package.json: name != sheleg-design-skill",
        )
        bin_rel = (package.get("bin") or {}).get("sheleg-design-skill", "")
        bin_path = ROOT / bin_rel
        if check(bin_path.is_file(), f"package.json: bin '{bin_rel}' missing"):
            first_line = (read(bin_path) or "").splitlines()[:1]
            check(
                first_line == ["#!/usr/bin/env node"],
                f"{bin_rel}: missing '#!/usr/bin/env node' shebang",
            )
        for entry in ("bin/", "plugins/", "cursor/"):
            check(
                entry in package.get("files", []),
                f"package.json: files[] must include '{entry}'",
            )
    changelog = changelog_version()
    if marketplace:
        entries = marketplace.get("plugins", [])
        check(len(entries) == 1, "marketplace.json: expected exactly one plugin entry")
        if entries:
            entry = entries[0]
            check(
                entry.get("name") == PLUGIN,
                f"marketplace.json: plugin name != {PLUGIN}",
            )
            source = entry.get("source", "")
            check(
                (ROOT / source).is_dir(),
                f"marketplace.json: plugin source '{source}' is not a directory",
            )
            skill_version = skill_metadata_version()
            if plugin and package and changelog and skill_version:
                # Five homes since 1.11.0. The fifth is the only one that ships
                # inside the bundle, which is the whole reason it exists.
                versions = {
                    entry.get("version"),
                    plugin.get("version"),
                    package.get("version"),
                    changelog,
                    skill_version,
                }
                check(
                    len(versions) == 1,
                    "version mismatch: marketplace=%s plugin=%s package=%s "
                    "changelog=%s SKILL.md=%s"
                    % (
                        entry.get("version"),
                        plugin.get("version"),
                        package.get("version"),
                        changelog,
                        skill_version,
                    ),
                )


def validate_skills():
    skills_dir = ROOT / PLUGIN_DIR / "skills"
    skill_dirs = (
        [
            p
            for p in sorted(skills_dir.iterdir())
            if p.is_dir() and p.name != "references"
        ]
        if skills_dir.is_dir()
        else []
    )
    check(bool(skill_dirs), f"{PLUGIN_DIR}/skills: no skill directories found")
    for skill in skill_dirs:
        rel = skill.relative_to(ROOT)
        fm = front_matter(skill / "SKILL.md")
        if not check(fm is not None, f"{rel}/SKILL.md: missing or has no front-matter"):
            continue
        check(
            fm.get("name") == skill.name,
            f"{rel}/SKILL.md: front-matter name != '{skill.name}'",
        )
        check(bool(fm.get("description")), f"{rel}/SKILL.md: missing description")
        desc = fm.get("description") or ""
        check_description_canon(rel, skill / "SKILL.md", desc)
    # The Cursor channel ships its own copy of the WHOLE bundle -- any file in
    # it may drift (a stale pack or token layer there is otherwise invisible).
    canonical_dir = skills_dir / PLUGIN
    mirror_dir = ROOT / ".cursor" / "skills" / PLUGIN
    if check(mirror_dir.is_dir(), f".cursor/skills/{PLUGIN}: missing"):
        for src in sorted(p for p in canonical_dir.rglob("*") if p.is_file()):
            rel_path = src.relative_to(canonical_dir)
            mirror = mirror_dir / rel_path
            if check(mirror.is_file(), f".cursor/skills/{PLUGIN}/{rel_path}: missing"):
                check(
                    read(mirror) == read(src),
                    f".cursor/skills/{PLUGIN}/{rel_path}: drifted from {PLUGIN_DIR}/skills/{PLUGIN}/{rel_path}",
                )
        for extra in sorted(p for p in mirror_dir.rglob("*") if p.is_file()):
            rel_path = extra.relative_to(mirror_dir)
            check(
                (canonical_dir / rel_path).is_file(),
                f".cursor/skills/{PLUGIN}/{rel_path}: not in the plugin bundle",
            )
    # Companion docs ship with the bundle AND are reachable from SKILL.md --
    # a reference nothing links to is a file the agent never opens.
    skill_body = read(skills_dir / PLUGIN / "SKILL.md") or ""
    for companion in (
        "SHELEG_DESIGN.md",
        "FIGMA_BRIDGE.md",
        "AI_PRODUCT_PATTERNS.md",
        "MOTION_DOCTRINE.md",
        "DESIGN_SYNC_BRIDGE.md",
    ):
        if check(
            (skills_dir / PLUGIN / companion).is_file(),
            f"{PLUGIN_DIR}/skills/{PLUGIN}/{companion}: missing",
        ):
            check(
                companion in skill_body,
                f"SKILL.md: {companion} ships in the bundle but is not linked from SKILL.md",
            )
    # The bridge doc's headings are a contract, not a suggestion: each one is a
    # reference type someone has to be told about, and a missing heading is a
    # reference type the agent will handle by improvising.
    bridge = skills_dir / PLUGIN / "DESIGN_SYNC_BRIDGE.md"
    brel = f"{PLUGIN_DIR}/skills/{PLUGIN}/DESIGN_SYNC_BRIDGE.md"
    if bridge.is_file():
        btext = read(bridge) or ""
        for section in BRIDGE_SECTIONS:
            check(section in btext, f"{brel}: missing required section '{section}'")
    styles_dir = skills_dir / PLUGIN / "styles"
    template = styles_dir / "STYLE_PACK_TEMPLATE.md"
    packs = sorted(p for p in styles_dir.glob("*.md") if p != template) if styles_dir.is_dir() else []
    check(len(packs) >= 2, f"{PLUGIN_DIR}/skills/{PLUGIN}/styles: expected >=2 style packs")
    # SKILL.md tells authors to copy this skeleton, so it has to exist and carry
    # every heading a real pack is held to -- otherwise the instruction dead-ends.
    trel = f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/STYLE_PACK_TEMPLATE.md"
    if check(template.is_file(), f"{trel}: missing"):
        ttext = read(template) or ""
        for section in PACK_SECTIONS_WIDE:
            check(section in ttext, f"{trel}: missing required section '{section}'")
        check(
            read(ROOT / "templates/style-pack-template.md") == ttext,
            f"{trel}: drifted from templates/style-pack-template.md",
        )
    skill_text = read(skills_dir / PLUGIN / "SKILL.md") or ""
    cli_text = read(ROOT / "bin/cli.js") or ""
    # The agent-facing surfaces are covered above; these two are read by humans
    # deciding whether to install, and they drift silently because nothing
    # imports them. A pack the README doesn't list is a pack nobody chooses.
    readme_text = read(ROOT / "README.md") or ""
    rules_text = "".join(
        read(p) or "" for p in sorted((ROOT / "cursor/rules").glob("*.mdc"))
    )
    for pack in packs:
        rel = pack.relative_to(ROOT)
        text = read(pack) or ""
        for section in PACK_SECTIONS:
            check(has_heading(text, section), f"{rel}: missing required section '{section}'")
        # All-or-nothing on the widened four. A pack that copied the current
        # skeleton and kept only the cheap headings would otherwise pass while
        # teaching the next author that the four are optional.
        # A pack that opens its Gotchas with "Six traps" and then lists eight is
        # asserting a number nobody recomputed. Shipped exactly that in `awning`
        # 1.36.0: the two traps found by rendering the pack were added correctly
        # and the header above them was not, and every other gate passed --
        # because the generic count check below counts packs and kits, not the
        # things a pack says about itself. A count is checkable, so it is checked.
        gotchas = text.split("## Gotchas", 1)
        if len(gotchas) == 2:
            listed = len(re.findall(r"^\d+\. \*\*", gotchas[1], re.M))
            m = re.match(r"\s*(\w+) traps\b", gotchas[1])
            # `.lower()` is load-bearing: NUMBER_WORDS is keyed lowercase and the
            # pack writes "Eight traps" capitalised, so the first draft of this
            # check looked up "Eight", got None, and skipped every pack in silence
            # — a gate that cannot fail, which is the defect it was written for.
            said = WORD_NUMBERS.get(m.group(1).lower()) if m else None
            if said is not None and listed:
                check(
                    said == listed,
                    f"{rel}: the Gotchas open with '{m.group(1)} traps' and the section "
                    f"lists {listed} -- a count is checkable, so it is checked",
                )

        adopted = [s for s in PACK_SECTIONS_WIDENED_ONLY if has_heading(text, s)]
        if adopted:
            missing = [s for s in PACK_SECTIONS_WIDENED_ONLY if not has_heading(text, s)]
            check(
                not missing,
                f"{rel}: half-widened pack -- carries {', '.join(adopted)} but not "
                f"{', '.join(missing)}. The widened four ship together or not at all",
            )
        check(
            (styles_dir / "tokens" / f"{pack.stem}.css").is_file(),
            f"{rel}: missing ready-made token layer styles/tokens/{pack.stem}.css",
        )
        # A pack nobody is routed to is a pack that does not exist.
        check(
            f"styles/{pack.name}" in skill_text,
            f"SKILL.md: style pack '{pack.stem}' is not linked from the pack table",
        )
        check(
            pack.stem in cli_text,
            f"bin/cli.js: style pack '{pack.stem}' is not named in the installer output",
        )
        check(
            pack.stem in readme_text,
            f"README.md: style pack '{pack.stem}' is not listed in the pack table",
        )
        check(
            pack.stem in rules_text,
            f"cursor/rules: style pack '{pack.stem}' is not named in any .mdc rule",
        )


def validate_installer_sync():
    """Every file in the skill bundle must be shipped by install.sh; the npx
    CLI walks the tree at runtime (check the walker exists)."""
    skill_dir = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    bundle = sorted(
        str(p.relative_to(skill_dir)) for p in skill_dir.rglob("*") if p.is_file()
    )
    cli = read(ROOT / "bin/cli.js") or ""
    check(
        "listBundleFiles" in cli,
        "bin/cli.js: runtime bundle walker (listBundleFiles) missing",
    )
    sh = read(ROOT / "install.sh") or ""
    match = re.search(r"^for f in (.+); do$", sh, re.MULTILINE)
    if check(match is not None, "install.sh: 'for f in …' file list not found"):
        listed = set(match.group(1).split())
        for f in bundle:
            check(f in listed, f"install.sh: bundle file '{f}' not in its file list")
        for f in listed:
            check(
                (skill_dir / f).is_file(),
                f"install.sh: lists '{f}' which does not exist in the bundle",
            )


def validate_commands():
    commands_dir = ROOT / PLUGIN_DIR / "commands"
    expected = {"sheleg-design.md"}
    found = (
        {p.name for p in commands_dir.glob("*.md")} if commands_dir.is_dir() else set()
    )
    check(expected <= found, f"commands: missing {sorted(expected - found)}")
    for name in sorted(found):
        fm = front_matter(commands_dir / name)
        ok = check(fm is not None, f"commands/{name}: missing front-matter")
        if ok:
            check(bool(fm.get("description")), f"commands/{name}: missing description")


def validate_cursor_rules():
    rules_dir = ROOT / "cursor/rules"
    rules = sorted(rules_dir.glob("*.mdc")) if rules_dir.is_dir() else []
    check(bool(rules), "cursor/rules: no .mdc rules found")
    for rule in rules:
        rel = rule.relative_to(ROOT)
        fm = front_matter(rule)
        if not check(fm is not None, f"{rel}: missing front-matter"):
            continue
        check("alwaysApply" in fm, f"{rel}: missing alwaysApply")
        if not fm.get("alwaysApply"):
            check(
                bool(fm.get("description")),
                f"{rel}: agent-requested rule needs a description",
            )
        text = read(rule) or ""
        check(
            "](./" not in text and "](../" not in text,
            f"{rel}: relative links are banned in .mdc (files get copied standalone)",
        )


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")

# ------------------------------------------------- what counts as this tree
#
# A nested checkout is not content. This project's standing practice is one
# isolated worktree per concurrent run, at `.claude/worktrees/<name>` -- and that
# is a FULL second copy of the tree, so a walk from ROOT reads every pack, doc and
# link twice. Measured 2026-08-13 on one commit: 2361 checks with a worktree
# present, 2067 on the same commit clean.
#
# A count that moves with whether a worktree happens to exist is the one thing the
# ratchet in floors.json cannot survive. Enshrine the inflated number and the next
# clean run fails for a regression that never happened; enshrine the clean one and
# a run with a worktree passes a floor it never had to clear. Either way the
# failure names a count and not a cause, which is the expensive kind.
#
# Excluded by what it IS -- a directory carrying its own `.git` -- rather than by
# name: the name is a convention, and the next convention will have another.
PRUNE_DIRS = {".git", "node_modules", "graphify-out", "dist", "build"}
# The self-test's copytree needs the same list plus nothing: a plant copied a
# nested worktree into every fixture before this, five times per run.
COPY_IGNORE = (".git", "node_modules", "graphify-out", "dist", ".claude")


def walk_md(root: Path):
    """Every markdown file that IS this tree's content."""
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        if here != root and (here / ".git").exists():
            dirnames[:] = []  # its own tree, with its own gates
            continue
        dirnames[:] = sorted(d for d in dirnames if d not in PRUNE_DIRS)
        for name in filenames:
            if name.endswith(".md"):
                yield here / name


def validate_links():
    for md in sorted(walk_md(ROOT)):
        text = read(md) or ""
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(SKIP_PREFIXES):
                continue
            target = target.split("#")[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            check(
                resolved.exists(),
                f"{md.relative_to(ROOT)}: broken relative link '{match.group(1)}'",
            )


def _props_body(text, name):
    """The prop block, stripped of comments and whitespace, for cross-kit
    comparison. Two kits may format differently and still agree."""
    for match in PROPS_RE.finditer(text):
        if match.group(1) != f"{name}Props":
            continue
        body = re.sub(r"/\*.*?\*/", "", match.group(2), flags=re.S)
        body = re.sub(r"//[^\n]*", "", body)
        return "".join(body.split())
    return None


def validate_fork_reciprocity():
    """A fork is an edge, and an edge that points one way is not a router.

    Five of eight packs named no other pack at all until 1.9.0, and every fork
    that did exist pointed backwards -- at packs that never pointed back. An
    agent entering the table at `instrument-console` therefore never learned any
    distinction existed, which makes the pack table a list rather than something
    that routes.

    The marker is a markdown link to another pack (`](./other.md)`), not a bare
    mention: a pack may name a neighbour in passing without owing it a section,
    but linking to it is a claim that the two are confusable -- and that claim is
    only useful if the neighbour makes it too.
    """
    styles_dir = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    template = styles_dir / "STYLE_PACK_TEMPLATE.md"
    packs = {p.stem: read(p) or "" for p in styles_dir.glob("*.md") if p != template}
    link = re.compile(r"\]\(\./([a-z0-9-]+)\.md\)")
    for name, text in sorted(packs.items()):
        for target in sorted(set(link.findall(text))):
            if target not in packs or target == name:
                continue
            check(
                f"](./{name}.md)" in packs[target],
                f"styles/{name}.md forks against '{target}' but styles/{target}.md "
                f"does not link back -- a one-way fork is a dead end for anyone "
                f"who reaches '{target}' first",
            )


def validate_kits():
    """The reference kits: one per pack, a spine that is identical everywhere,
    tokens copied rather than transcribed, and nothing that would push a kit
    into the installed bundle (ADR-0002)."""
    kits_dir = ROOT / "kits"
    styles_dir = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    template = styles_dir / "STYLE_PACK_TEMPLATE.md"
    packs = sorted(
        p.stem for p in styles_dir.glob("*.md") if p != template
    ) if styles_dir.is_dir() else []
    kits = sorted(
        p.name for p in kits_dir.iterdir() if p.is_dir()
    ) if kits_dir.is_dir() else []

    # 3. every pack has a kit, and every kit has a pack
    for pack in packs:
        check(pack in kits, f"kits/{pack}: no kit for style pack '{pack}'")
    for kit in kits:
        check(kit in packs, f"kits/{kit}: no style pack named '{kit}'")

    # The exemplar is the reference for the spine's shape.
    reference = {}
    ref_dir = kits_dir / "workbench" / "src"
    for name in SPINE:
        text = read(ref_dir / f"{name}.tsx") or ""
        reference[name] = _props_body(text, name)

    for kit in kits:
        src = kits_dir / kit / "src"
        ds = kits_dir / kit / ".design-sync"

        # 4. the spine is present and its props match the exemplar's
        for name in SPINE:
            comp = src / f"{name}.tsx"
            if not check(
                comp.is_file(),
                f"kits/{kit}: spine component '{name}' missing (the spine is identical in every kit)",
            ):
                continue
            if kit == "workbench" or reference.get(name) is None:
                continue
            check(
                _props_body(read(comp) or "", name) == reference[name],
                f"kits/{kit}/src/{name}.tsx: {name}Props differs from kits/workbench — "
                "switching packs must swap identity, not API",
            )

        # 5. every component carries a doc with a category from the taxonomy
        for comp in sorted(src.glob("*.tsx")) if src.is_dir() else []:
            doc = src / f"{comp.stem}.md"
            if not check(
                doc.is_file(),
                f"kits/{kit}/src/{comp.stem}.md: missing — a component with no doc gets no card group",
            ):
                continue
            match = CATEGORY_RE.search(read(doc) or "")
            if not check(
                match is not None,
                f"kits/{kit}/src/{comp.stem}.md: missing 'category:' frontmatter",
            ):
                continue
            check(
                match.group(1) in CARD_GROUPS,
                f"kits/{kit}/src/{comp.stem}.md: category '{match.group(1)}' is not one of "
                + "/".join(CARD_GROUPS),
            )

        # 6. the token block is the pack's token layer, byte for byte
        styles = src / "styles.css"
        tokens = styles_dir / "tokens" / f"{kit}.css"
        if check(styles.is_file(), f"kits/{kit}/src/styles.css: missing") and tokens.is_file():
            token_text = read(tokens) or ""
            check(
                (read(styles) or "").startswith(token_text),
                f"kits/{kit}/src/styles.css: token block drifted from "
                f"styles/tokens/{kit}.css — copy it, never transcribe it",
            )

            # 7. no colour literal below the component marker
            body = read(styles) or ""
            marker = "/* ── components ── */"
            if check(
                marker in body,
                f"kits/{kit}/src/styles.css: missing the '{marker}' marker",
            ):
                after = body.split(marker, 1)[1]
                offset = body[: body.index(marker)].count("\n") + 1
                for i, line in enumerate(after.splitlines(), start=offset + 1):
                    hit = COLOR_LITERAL.search(line)
                    if hit:
                        check(
                            False,
                            f"kits/{kit}/src/styles.css:{i}: raw colour literal "
                            f"'{hit.group(0)}' — use a token",
                        )

        # 9/10. the sync config, and the conventions header it must point at
        config_path = ds / "config.json"
        conventions = ds / "conventions.md"
        raw = read(config_path)
        if check(raw is not None, f"kits/{kit}/.design-sync/config.json: missing"):
            try:
                cfg = json.loads(raw)
            except json.JSONDecodeError as exc:
                cfg = None
                check(False, f"kits/{kit}/.design-sync/config.json: invalid JSON ({exc})")
            if cfg is not None:
                for field in ("pkg", "globalName", "shape", "cssEntry", "readmeHeader"):
                    check(
                        field in cfg,
                        f"kits/{kit}/.design-sync/config.json: missing required field '{field}'",
                    )
                check(
                    "projectId" not in cfg,
                    f"kits/{kit}/.design-sync/config.json: committed projectId would point "
                    "every user at one project — the target is chosen per sync, by a human",
                )
                check(
                    cfg.get("shape") == "package",
                    f"kits/{kit}/.design-sync/config.json: shape must be 'package'",
                )
                if "readmeHeader" in cfg:
                    check(
                        (kits_dir / kit / cfg["readmeHeader"]).is_file(),
                        f"kits/{kit}: readmeHeader points at '{cfg['readmeHeader']}', which does not exist",
                    )
        check(
            conventions.is_file() and len(read(conventions) or "") > 200,
            f"kits/{kit}/.design-sync/conventions.md: missing — the pack's bans never "
            "reach the design agent without it",
        )

        # 11. guidelines/ is materialized by --kit, never committed
        check(
            not (kits_dir / kit / "guidelines").exists(),
            f"kits/{kit}/guidelines/: committed — the pack doc has one home, "
            f"styles/{kit}.md; --kit materializes the copy",
        )

    # 8. nothing kit-shaped reached the bundle, and install.sh lists no kit path
    bundle = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    strays = sorted(
        str(p.relative_to(ROOT))
        for p in bundle.rglob("*")
        if p.is_file() and (p.suffix in (".tsx", ".ts") or p.name == "package.json")
    )
    for stray in strays:
        check(False, f"{stray}: kit-shaped file inside the bundle — kits ship in the package (ADR-0002)")
    sh = read(ROOT / "install.sh") or ""
    check(
        "kits/" not in sh,
        "install.sh: names a kits/ path — kits ship in the package, not the bundle (ADR-0002)",
    )

    # 9 (continued). the package must actually carry them
    package = ROOT / "package.json"
    try:
        files = json.loads(read(package) or "{}").get("files", [])
    except json.JSONDecodeError:
        files = []
    check("kits/" in files, "package.json: files[] must include 'kits/'")


# --------------------------------------------------------- counted claims
#
# The class this repo could never see. `validate.py` checked that each pack's
# NAME appears in the README, the CLI and the rules -- so twelve names were
# present and the sentence above them still read "six locked style packs" for
# four releases. A count is the one kind of claim a machine can settle outright,
# and it was the only kind nothing checked.
#
# Normalisation matters more than the regex: the README's "six locked style /
# packs" is split across a line break, so a line-based grep cannot see it. Every
# source is whitespace-collapsed first.
NUMBER_WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four",
    25: "twenty-five", 26: "twenty-six", 27: "twenty-seven",
    28: "twenty-eight", 29: "twenty-nine", 30: "thirty",
}
WORD_NUMBERS = {w: n for n, w in NUMBER_WORDS.items()}
# Longest first, so "twenty-one" wins over "one"; and a lookbehind that refuses
# a match starting mid-compound. The twenty-first pack is what surfaced this:
# the table stopped at twenty, so every correct "twenty-one packs" was read as
# "one packs" and failed, and the hyphenated form of a count nobody had needed
# yet was the only thing missing.
_COUNT_WORDS = "|".join(sorted(WORD_NUMBERS, key=len, reverse=True))
# THE SEPARATOR IS A SPACE **OR** A HYPHEN, and it is captured and
# back-referenced so a compound is read in one alphabet or the other and never
# half in each: "twenty locked style packs" and "twenty-nine-style-packs" both
# parse, "twenty-nine style-packs" is not silently accepted as either.
#
# The hyphenated form is the hole this closes. `COUNTED` required a SPACE, so
# "a fourteen-kit build matrix" in `docs/DOCMAP.md` -- the document whose own
# subject is that every fact has one home -- stayed wrong through every kit
# release after it, with the counted-claims check green on the line above. The stale
# fact is the smaller half. The larger half is that a contributor had ALREADY
# measured the hole and routed around it: the 2026-08-19 reduced-motion run
# deleted a hyphenated "twenty-nine releases" from its own prose rather than
# plant a number this regex could not police. A guard people write around has
# stopped being a guard, so the coverage is worth more than either fact.
COUNTED = re.compile(
    r"(?<![-\w])(?P<num>" + _COUNT_WORDS + r"|\d{1,2})(?P<sep>[ -])"
    r"(?:(?:locked|named|shipped|pluggable|real|React|reference)(?P=sep))*"
    # `*`, not `?`: plugin.json says "twenty pluggable VISUAL STYLE packs", and a
    # single optional modifier meant that count was never read as one. It sat
    # stale at twenty while twenty-one shipped, in the file an agent host reads.
    r"(?:(?:visual|style)(?P=sep))*"
    # `s?`, and the plural is required back at the call site for the SPACE form
    # only. A hyphenated count is a modifier and singular by grammar ("a
    # fourteen-kit matrix"); a spaced one is a tally and plural ("fourteen kits").
    # Accepting a spaced singular everywhere would read "one kit per pack" -- a
    # ratio, not a tally -- as a claim that the library holds one kit.
    r"(?P<noun>pack|kit|scenario|heading)(?P<plural>s?)\b",
    re.I,
)
# "A fork between two packs" counts a relationship, not the library.
COUNT_NOT_A_TALLY = re.compile(r"(?i)\b(?:between|either|each|any|both|per|same)\s+$")
# A hyphen used to mean "not a count" outright, which is what hid `fourteen-kit`.
# Now that it can carry one, the compounds that are NOT tallies have to be named,
# because a widened pattern that flags correct prose is its own defect. Measured
# old-pattern-against-new on one tree at the commit that widened it: **+2** spans
# inside the source list below, both in `docs/DOCMAP.md`, zero of them false; and
# **+51** across all 1025 text files, of which 3 are exempted here. The tree figure
# moves whenever prose is edited, so the source-list figure is the one the floor
# pins. Two classes in the widening are not claims about the library, and only the
# first can be settled by a pattern.
#
#   1. A count glued into a longer identifier -- `feat/four-packs-v1.9.0`, a
#      branch name recorded in a spec brief. Prose never puts a tally directly
#      after a slash or directly before another hyphen, so this is exempted:
#      a hyphen-form match has to stand alone as a modifier.
#   2. A hyphenated compound counting something that is NOT the library: "a
#      six-pack backfill" (retro.md) counts one run's work, and "the nine-heading
#      contract" (this file, CHANGELOG, two briefs) narrates a contract that has
#      since widened. No pattern separates those from a stale claim -- only the
#      SOURCE LIST does, and none of them is in it. That list stays deliberately
#      short for this reason; widening it means adjudicating each of those spans,
#      not adding a regex escape.
COUNT_IS_AN_IDENTIFIER = re.compile(r"^(?:[-/]|\.\w)")


def _packs() -> list[str]:
    d = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    return sorted(p.stem for p in d.glob("*.md") if p.name != "STYLE_PACK_TEMPLATE.md")


def validate_counted_claims():
    """Every 'N packs' / 'N kits' / 'N scenarios' / 'N headings' is true."""
    packs = _packs()
    kits = sorted(p.name for p in (ROOT / "kits").iterdir() if p.is_dir()) if (ROOT / "kits").is_dir() else []
    scen = read(ROOT / "test/scenarios.md") or ""
    truth = {
        "pack": len(packs),
        "kit": len(kits),
        "scenario": max((int(n) for n in re.findall(r"^##+ T(\d+)", scen, re.M)), default=0),
        "heading": len(PACK_SECTIONS_WIDE),
    }
    # The three manifests were missing from this list until 1.19.0, and the cost
    # was exactly what this check exists to prevent: marketplace.json said
    # "twelve pluggable style packs" while thirteen shipped, for two releases,
    # and package.json said "thirteen" on the day the fourteenth landed. Names in
    # these files were already checked (validate_pack_enumerations); the NUMBER
    # beside the names was not, because the source list was all-markdown plus two
    # scripts. A count is checkable wherever it is written, including in JSON.
    sources = [
        "README.md", "CONTRIBUTING.md", "bin/cli.js", "docs/DOCMAP.md",
        "cursor/rules/sheleg-design.mdc",
        ".claude-plugin/marketplace.json",
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        "package.json",
        f"{PLUGIN_DIR}/commands/{PLUGIN}.md",
    ] + [
        str(p.relative_to(ROOT))
        for p in sorted((ROOT / PLUGIN_DIR / "skills" / PLUGIN).rglob("*.md"))
    ]
    for rel in sources:
        text = read(ROOT / rel)
        if text is None:
            continue
        flat = " ".join(text.split())
        for m in COUNTED.finditer(flat):
            raw, noun = m.group("num").lower(), m.group("noun").lower()
            hyphenated = m.group("sep") == "-"
            # See `s?` above: a spaced count is a tally and must be plural.
            if not hyphenated and not m.group("plural"):
                continue
            glued_left = m.start() > 0 and flat[m.start() - 1] == "/"
            glued_right = COUNT_IS_AN_IDENTIFIER.match(flat[m.end():]) is not None
            if hyphenated and (glued_left or glued_right):
                continue
            said = WORD_NUMBERS.get(raw, int(raw) if raw.isdigit() else None)
            if said is None or truth[noun] == 0:
                continue
            if COUNT_NOT_A_TALLY.search(flat[max(0, m.start() - 24): m.start()]):
                continue
            check(
                said == truth[noun],
                f"{rel}: says {m.group(0)!r} but there are {truth[noun]} {noun}s "
                f"-- a count is checkable, so it is checked",
            )


# ------------------------------------------------- exhaustive enumerations
#
# These surfaces are where a host or a human decides whether this skill answers
# their request. plugin.json named three packs of twelve, and the /sheleg-design
# command's fast path listed the same three -- so nine packs could not be asked
# for by name through the command that exists to ask for them.
#
# Scoped to sites whose list is contractually exhaustive. FIGMA_BRIDGE.md names
# three packs on purpose (they are the ones with a mode trap) and is not here.
ENUMERATION_SITES = (
    (".claude-plugin/marketplace.json", "the marketplace card an agent host reads"),
    # package.json was missing until 1.45.0, and it is the surface an npm reader
    # chooses from -- npmjs.com renders this description and nothing else. Its
    # COUNT was already checked (validate_counted_claims reads the same file), so
    # it said "twenty-nine locked style packs" over a list of twenty-seven for two
    # pack releases: the number was policed and the names beside it were not.
    ("package.json", "the description npmjs.com renders"),
    (f"{PLUGIN_DIR}/.claude-plugin/plugin.json", "the plugin description an agent host reads"),
    (f"{PLUGIN_DIR}/commands/{PLUGIN}.md", "the slash command's by-name fast path"),
    ("bin/cli.js", "the installer's help and banner"),
    ("README.md", "the pack table"),
    ("cursor/rules/sheleg-design.mdc", "the standalone Cursor rule"),
    (f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md", "the routing table"),
)


def validate_pack_enumerations():
    packs = _packs()
    for rel, why in ENUMERATION_SITES:
        text = read(ROOT / rel)
        if not check(text is not None, f"{rel}: missing"):
            continue
        missing = [p for p in packs if p not in text]
        check(
            not missing,
            f"{rel}: {why} names {len(packs) - len(missing)} of {len(packs)} packs "
            f"-- missing {', '.join(missing)}. A pack absent here cannot be chosen here",
        )


# ------------------------------------------------------ contract terminology
#
# The pack contract was called "nine", "ten" and "thirteen" simultaneously
# across DOCMAP, DESIGN_SYNC_BRIDGE, scenarios.md, CONTRIBUTING and validate.py's
# own docstring -- and DESIGN_SYNC_BRIDGE told an author to ship "all nine
# headings", which this gate then passed, because nine is the floor. One name,
# one number, or the author ships the smaller thing.
STALE_CONTRACT = re.compile(
    r"\b(nine|ten|eleven|twelve|fourteen|9|10|11|12|14)[- ]heading\b", re.I
)


def validate_contract_terminology():
    want = NUMBER_WORDS[len(PACK_SECTIONS_WIDE)]
    # Documentation only. The gates' own source has to be able to name the stale
    # spellings -- in the comment explaining why this check exists, and in the
    # self-test fixture that plants one -- and a checker that fails on its own
    # explanation teaches people to delete the explanation.
    for md in sorted(walk_md(ROOT)):
        parts = set(md.parts)
        if parts & {"test", "audit", "evidence"} or md.name == "CHANGELOG.md":
            # A dated record states the contract of its own day, and an audit
            # report has to be able to quote the stale spelling it found.
            continue
        text = read(md) or ""
        for m in STALE_CONTRACT.finditer(text):
            check(
                False,
                f"{md.relative_to(ROOT)}: says {m.group(0)!r}; the pack contract is "
                f"{want} ({len(PACK_SECTIONS_WIDE)}) plus '## Motion flavor' for a "
                f"cinematic pack. One name, one number",
            )


# ------------------------------------------------ what a pack does NOT specify
#
# Six packs carry the four widened sections and six do not, and nothing said so.
# SKILL.md tells the agent a pack "supplies the palette, type, texture,
# motion-token values, signature motifs, and bans" -- a list that quietly omits
# the four. An agent on a core-contract pack finds no component states, no hero
# ceiling and no breakpoints, and invents them; the precision of what IS
# specified reads as completeness.
CONTRACT_MARKER = re.compile(r"^Contract:\s*(core|widened)\b", re.M)


def _section(text: str, heading: str) -> str:
    """The body of one `## Heading`, up to the next one. Empty when absent."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    except StopIteration:
        return ""
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    return "\n".join(lines[start + 1:end])


def has_heading(text: str, heading: str) -> bool:
    """A heading is a line, not a substring.

    `"## Hero" in text` is true of any prose that mentions `## Hero` -- including
    the core-contract note that lists the four sections a pack omits, which made
    six packs look widened the moment they declared they were not. Structure is
    checked structurally.
    """
    return re.search(rf"^{re.escape(heading)}\s*$", text, re.M) is not None


def validate_contract_split():
    """The core-contract paragraph states three numbers; the table decides them.

    "Six of the fourteen are on the core contract ... The other eight answer all
    four" is three claims about one table, and they have now been wrong in TWO
    CONSECUTIVE pack releases -- each time introduced by the release's own count
    edit, which changed the total and left the remainder behind. 1.13.0 shipped
    "Six of the thirteen ... the other six" (found by a T23 scenario agent);
    1.19.0's draft shipped "Six of the fourteen ... the other seven" (found by a
    T24 scenario agent). Both were fixed as instances. This is the class fix, and
    it is arithmetic rather than judgement: the paragraph is the one place the
    library explains that a core pack leaves four sections to the reader, so a
    wrong remainder there is precisely the "invent a value and believe you read
    it" failure the paragraph itself warns about.

    validate_counted_claims() cannot see these: "Six of the fourteen" has no
    counted noun after the number, and "the other eight" has none either.
    """
    skill_path = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "SKILL.md"
    skill = read(skill_path) or ""
    rows = re.findall(r"^\| \[`[a-z0-9-]+`\].*$", skill, re.M)
    total = len(rows)
    core = sum(1 for r in rows if "core contract" in r)
    if not check(total > 0, "SKILL.md: no pack table rows found -- the contract split "
                            "cannot be checked against anything"):
        return
    m = re.search(r"\*\*([\w-]+) of the ([\w-]+) are on the core contract", skill)
    if check(m is not None, "SKILL.md: the core-contract paragraph does not state "
                            "'<N> of the <M> are on the core contract'"):
        said_core, said_total = (WORD_NUMBERS.get(g.lower()) for g in m.groups())
        check(said_core == core,
              f"SKILL.md: says {m.group(1)!r} packs are on the core contract; the table "
              f"marks {core}")
        check(said_total == total,
              f"SKILL.md: says the library holds {m.group(2)!r} packs; the table has {total}")
    m = re.search(r"The other ([\w-]+) answer all four", skill)
    if check(m is not None, "SKILL.md: the core-contract paragraph does not state "
                            "'The other <N> answer all four'"):
        check(
            WORD_NUMBERS.get(m.group(1).lower()) == total - core,
            f"SKILL.md: says {m.group(1)!r} packs answer all four widened sections; the "
            f"table leaves {total - core} that are not marked 'core contract' -- this "
            f"remainder has been stale in two consecutive releases, each time because a "
            f"count edit moved the total and not the remainder",
        )


def validate_contract_declaration():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    skill = read(styles.parent / "SKILL.md") or ""
    core: list[str] = []
    for name in _packs():
        text = read(styles / f"{name}.md") or ""
        rel = f"styles/{name}.md"
        widened = all(has_heading(text, s) for s in PACK_SECTIONS_WIDENED_ONLY)
        m = CONTRACT_MARKER.search(text)
        if not check(m is not None, f"{rel}: no 'Contract: core|widened' line -- a reader "
                                    "cannot tell what this pack leaves them to decide"):
            continue
        check(
            (m.group(1) == "widened") == widened,
            f"{rel}: declares 'Contract: {m.group(1)}' but "
            f"{'carries' if widened else 'does not carry'} the four widened sections",
        )
        if not widened:
            core.append(name)
            check(
                f"styles/{name}.md" in skill and "core contract" in skill,
                f"SKILL.md: '{name}' is on the core contract and the pack table does not "
                "say so -- the table is where the pack is chosen",
            )
    report.append(
        f"contract split: {len(core)} core / {len(_packs()) - len(core)} widened "
        f"of {len(_packs())} packs (core: {', '.join(core)})"
    )


CONTAINER_ANSWER = re.compile(r"container-type|container quer|@container", re.I)
# A width-based viewport query, which is what a component must not be sized by.
KIT_MEDIA = re.compile(r"@media[^{]*\((?:min|max)-width[^{]*\{", re.I)
# The three kinds a breakpoint can be. Only CONTAINER has a container answer; the
# other two are declared, with a reason, at the block.
KIT_MEDIA_MARK = re.compile(r"\b(PAGE|SELF|TODO-CONTAINER)\b")


def validate_pack_container_answer():
    """A widened pack has to say which components size against their container.

    The bullet has been in the skeleton's `## Responsive` section since the contract
    was widened in 1.5.0, and when this check was written (2026-08-13, ten widened
    packs) seven of the ten left it blank -- so the contract asked and nothing
    checked, which is the same shape as the nine-heading dead zone the
    all-or-nothing rule closed. The split moves with every release and is printed by
    this run rather than restated here. "None, and here is why" is a valid answer;
    `field-notes` and `cyclorama` were already giving it.

    Core packs are exempt because they carry no `## Responsive` section at all.
    """
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    for name in _packs():
        text = read(styles / f"{name}.md") or ""
        if not all(has_heading(text, s) for s in PACK_SECTIONS_WIDENED_ONLY):
            continue  # core contract: no Responsive section to answer in
        section = _section(text, "## Responsive")
        check(
            bool(CONTAINER_ANSWER.search(section)),
            f"styles/{name}.md: '## Responsive' does not say which components size "
            "against their container -- the skeleton has asked since 1.5.0, and "
            "'none, and why' is a valid answer",
        )


def validate_kit_breakpoints():
    """A component's breakpoint belongs to its container, not to the viewport.

    A kit ships components a consumer drops into an arbitrary box, so a viewport
    query inside one is a bug the moment the component is not full-width: a
    scoreboard row in a 320px sidebar on a 1440px screen keeps its wide columns and
    overflows. Measured 2026-08-13: seven width queries across six kits, and zero
    `container-type` anywhere.

    Two blocks legitimately stay on the viewport and both are declared rather than
    tolerated: a `:root` token switch (`:root` is inside nobody's container) and a
    property on the element that would *establish* the container, which cannot query
    itself. Anything else says TODO-CONTAINER with a board id.
    """
    kits_dir = ROOT / "kits"
    if not kits_dir.is_dir():
        return
    for css in sorted(kits_dir.glob("*/src/styles.css")):
        text = read(css) or ""
        rel = css.relative_to(ROOT)
        for m in KIT_MEDIA.finditer(text):
            start = m.end()
            depth, i = 1, start
            while i < len(text) and depth:
                depth += text[i] == "{"
                depth -= text[i] == "}"
                i += 1
            body = text[start:i - 1]
            selectors = [s.strip() for s in re.findall(r"([^{}]+)\{", body)]
            root_only = selectors and all(s == ":root" for s in selectors)
            # The marker lives in the comment immediately above the block, and the
            # comment is read whole rather than through a fixed window: the first
            # version looked back 400 characters and missed a five-line reason whose
            # marker sat at character 425 -- a check that fails on a longer
            # explanation teaches authors to write shorter ones.
            before = text[:m.start()].rstrip()
            marked = False
            if before.endswith("*/"):
                opened = before.rfind("/*")
                marked = opened != -1 and bool(KIT_MEDIA_MARK.search(before[opened:]))
            check(
                root_only or marked,
                f"{rel}:{text[:m.start()].count(chr(10)) + 1}: a viewport width query in a "
                f"kit sizes a component by the screen instead of by its box "
                f"({', '.join(selectors[:3]) or 'no selector'}) -- use container-type on the "
                f"root and @container on the descendant, or mark the block PAGE / SELF / "
                f"TODO-CONTAINER with the reason",
            )


# ------------------------------------------------------------ the ratchet
#
# "Each may rise, never fall" was a sentence in DOCMAP.md and nothing else.
# Measured: stripping the four widened headings from one pack made BOTH gates
# quieter -- validate.py 1270 -> 1269, sloplint.py 224 -> 223 -- and both still
# exited 0. A gate whose count can fall silently cannot detect a deleted
# requirement, which is the one failure a consistency validator exists to catch.
FLOORS = Path(__file__).resolve().parent / "floors.json"


def check_floor(script: str, count: int) -> None:
    try:
        floors = json.loads(FLOORS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"FAIL: {FLOORS.name} is missing or unreadable -- the ratchet cannot be enforced",
              file=sys.stderr)
        sys.exit(1)
    floor = floors.get(script)
    if floor is None:
        print(f"FAIL: {FLOORS.name} has no floor for {script}", file=sys.stderr)
        sys.exit(1)
    if count < floor:
        print(
            f"FAIL: {script} ran {count} checks, below its floor of {floor}. "
            f"Checks do not disappear on their own -- something that used to be "
            f"required is not being required any more. If the drop is intended, "
            f"lower the floor in {FLOORS.name} in the same commit, with the reason.",
            file=sys.stderr,
        )
        sys.exit(1)


# ------------------------------------------------------------- self-test
#
# Each planted defect is one this repo actually shipped. The tree is copied, one
# defect is planted, and THIS file is re-run against the copy -- so what is
# tested is the validator CI runs, not a re-implementation of it.
#
# An entry is (label, path, mutate) or (label, path, mutate, expect). Without
# `expect` the pass condition is only "the validator went red", which is weaker
# than it looks the moment a file is read by more than one check: every token
# layer is also copied into its kit byte for byte, so ANY edit to
# styles/tokens/<pack>.css also trips the kit-drift check -- and a plant caught by
# a neighbouring check proves nothing about the check it was written for. The two
# reduced-motion plants below name the message they must provoke.
PLANTS = (
    (
        # A widened pack that stops answering the container bullet. Derived from
        # whatever the pack currently says rather than pinned to a phrase, so it
        # keeps mutating something as the answers get rewritten.
        "a widened pack whose Responsive section stops answering the container question",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/scoreboard.md",
        lambda t: t.replace("**Container queries** for the report surface", "**Breakpoints** for the report surface", 1),
    ),
    (
        # A kit component sized by the screen instead of by its box: the defect
        # this release exists to close, planted back in.
        "a kit breakpoint that goes back to the viewport with no reason given",
        "kits/scoreboard/src/styles.css",
        lambda t: t.replace("@container (max-width: 231px)", "@media (max-width: 767px)", 1),
    ),
    (
        # The literal count word travels with every release, so pinning it here
        # made the fixture stop mutating anything the first time the library
        # grew -- a plant that changes nothing reports BROKEN rather than
        # missing, but it stops testing the check either way. Read whatever
        # number the README currently claims and make it wrong.
        "a count that is true of an older release",
        "README.md",
        lambda t: re.sub(
            r"\*\*[a-z-]+ locked style\npacks\*\*", "**six locked style\npacks**", t, count=1
        ),
    ),
    (
        "a manifest naming three packs of twelve",
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        lambda t: t.replace("briefing-room (dark 16:9 deck), ", ""),
    ),
    (
        # The remainder that has now been stale in two consecutive pack releases:
        # 1.13.0 shipped "the other six" of thirteen, and 1.19.0's draft shipped
        # "the other seven" of fourteen. Derived from whatever the paragraph
        # currently says, so it cannot pin itself to a number the next release
        # edits -- the failure mode of the plant this one sits beside.
        "the core-contract remainder left behind by a count edit",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md",
        # `[\w-]+`, not `\w+`: at the twenty-eighth pack the remainder crossed twenty
        # and became "twenty-one", which a bare `\w+` cannot match -- so the plant
        # changed nothing and the self-test reported a check that had quietly stopped
        # being exercised. A fixture that cannot find its own target is a hole in the
        # gate, and it opens on exactly the release this plant exists to catch.
        lambda t: re.sub(r"The other [\w-]+ answer all four", "The other five answer all four", t, count=1),
    ),
    (
        # The same class as the first plant, in a file the source list did not
        # read until 1.19.0 -- which is how "twelve pluggable style packs" sat
        # above a list of thirteen for two releases. Derived from whatever the
        # manifest currently claims, for the reason given at the first plant.
        "a count that is true of an older release, in a manifest",
        ".claude-plugin/marketplace.json",
        lambda t: re.sub(r"[a-z-]+ (pluggable style packs)", r"six \1", t, count=1),
    ),
    (
        "the contract called by a stale number",
        "CONTRIBUTING.md",
        lambda t: t.replace("The contract is **thirteen**", "The contract is **nine-heading**"),
    ),
    (
        "a pack that does not declare what it leaves undecided",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/workbench.md",
        lambda t: re.sub(r"^Contract: .*\n", "", t, count=1, flags=re.M),
    ),
    (
        "a version out of five-way sync",
        "package.json",
        lambda t: t.replace('"version": "', '"version": "9.', 1),
    ),
    (
        "the bundle's own version removed, leaving §7's rule with nothing to read",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md",
        lambda t: re.sub(r"^metadata:\n  version: .*\n", "", t, count=1, flags=re.M),
    ),
    (
        "a repo-only path offered to a reader who has no repo",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/DESIGN_SYNC_BRIDGE.md",
        lambda t: t.replace(
            "## 7. Round-trip discipline",
            "## 7. Round-trip discipline\n\nSee `docs/evidence/backlog.md` for the open rows.",
            1,
        ),
    ),
    (
        "a counted claim whose members stopped travelling with the count",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/DESIGN_SYNC_BRIDGE.md",
        lambda t: t.replace("The six are `Button`, `Card`, `Chip`,", "The six are `Card`, `Chip`,", 1),
    ),
    (
        "a style pack the SKILL.md table does not route to",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md",
        lambda t: t.replace("styles/maquette.md", "styles/nowhere.md"),
    ),
    (
        # B-040, planted back in. `instrument-console` shipped with no branch at
        # all while mandating a WebGL particle field, and both gates stayed green
        # because the only thing reading the promise was a string assertion over
        # MOTION_DOCTRINE.md. The at-rule is removed and the `:root` body left
        # behind, so what the plant removes is exactly the query -- a plant that
        # deleted the whole tail would also be a syntax error and could be caught
        # for the wrong reason.
        "a token layer that ships motion tokens and no reduced-motion branch",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/instrument-console.css",
        lambda t: t.replace("@media (prefers-reduced-motion: reduce) {\n  :root {", "  :root {", 1),
        "ships no '@media (prefers-reduced-motion: reduce)' branch",
    ),
    (
        # The defect the CHECK would have had if it were a grep, which is the
        # defect B-040 was really about: sloplint asserts the STRING
        # `prefers-reduced-motion` occurs in the doctrine, so a branch that
        # mentions the query and collapses nothing satisfied every gate. §9 says
        # motion collapses to static or instant, "not to 'slower'" -- 0.4s is
        # slower, and this plant is the whole reason the check reads values.
        "a reduced-motion branch that mentions the query and collapses nothing",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/editorial-luxury.css",
        lambda t: re.sub(r"(--dur-[a-z]+|--stagger): 0s;", r"\1: 0.4s;", t),
        "collapses no duration to an instant value",
    ),
    (
        # SG-03, and the exact string that shipped. `COUNTED` matched a number
        # only when a SPACE followed it, so this claim stayed wrong in DOCMAP
        # through every kit release after it while the counted-claims gate ran
        # green over the same file. The plant is the defect restored verbatim.
        "a stale count hyphenated onto its noun",
        "docs/DOCMAP.md",
        lambda t: t.replace("twenty-nine-kit", "fourteen-kit", 1),
        "says 'fourteen-kit' but there are 29 kits",
    ),
    (
        # The same hole in digits. Worth its own plant because the number and the
        # word reach the pattern by different branches of the same alternation,
        # and a widening that fixed only the spelled form would pass the plant
        # above while leaving `14-kit` invisible.
        "a stale count hyphenated onto its noun, in digits",
        "docs/DOCMAP.md",
        lambda t: t.replace("twenty-nine-kit", "14-kit", 1),
        "says '14-kit' but there are 29 kits",
    ),
    (
        # The status map's live instance: `workbench` had grown a quartet while the
        # map still said `--ok` / `--warn`. Planted as the smallest possible drift.
        "the cross-pack status map disagreeing with a token layer",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SURFACE_COMPOSITION.md",
        lambda t: t.replace(
            "| `--danger` / `--good` | roster |", "| `--danger` | roster |", 1),
        "the status table says 'roster'",
    ),
    (
        # `datasheet.css` explains the reference's rem base with `html { font-size:
        # 8px }` INSIDE a comment, so a brace scan over the raw text sliced a
        # nine-character root block and excluded the pack from two sweeps. This
        # plants a shadow into that pack: it can only be caught if the block scanner
        # skips comments.
        "a pack whose root block starts after a comment containing a brace",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/datasheet.css",
        lambda t: t.replace(":root {\n", ":root {\n  --shadow-planted: 0 1px 2px rgba(0,0,0,.1);\n", 1),
        "ships '--shadow-planted'",
    ),
    (
        # Two runs took the number 1.35.0 and the tag went to the second, with the
        # first one's notes sitting above it -- so a release extractor reading the
        # first match would have shipped the wrong section.
        "two CHANGELOG sections under one version",
        "CHANGELOG.md",
        lambda t: t.replace(
            "## [1.43.0] - 2026-08-17",
            "## [1.44.0] - 2026-08-19\n\n### Changed\n\n- a second section under a "
            "number that already has one.\n\n## [1.43.0] - 2026-08-17", 1),
        "appears more than once",
    ),
    (
        # The Run stamps table sat at v1.26.0 while 1.44.0 shipped, and the
        # retirement trigger in the same file counts rows in it.
        "a release with no row in the Run stamps table",
        "docs/evidence/retro.md",
        lambda t: t.replace("**`v1.44.0` shipped**", "**shipped**", 1),
        "has no row for 1.44.0",
    ),
    (
        # 1.45.0's four sweeps, one plant each. All four defects are ones the tree
        # was shipping when the sweeps were written, planted back in.
        #
        # A shadow token no prose names. `scoreboard` shipped four shadows under a
        # comment counting three; sixteen tokens across eleven packs were unnamed.
        "a shadow token the pack ships and its prose never names",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/scoreboard.md",
        lambda t: t.replace("`--shadow-panel` (one layer, 4%) seats", "A single wash seats", 1),
        "ships '--shadow-panel'",
    ),
    (
        # A component given two radii. `showroom` said --radius-2xl in Texture and
        # --radius-3xl in Components, and its nesting rule subtracts from the outer
        # value, so every inner radius inherited the 4px error.
        "one component given two different radii",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/showroom.md",
        lambda t: t.replace(
            "| **Specimen frame** | `--surface` fill, `--radius-3xl`",
            "| **Specimen frame** | `--surface` fill, `--radius-2xl`", 1),
        "different radii",
    ),
    (
        # A press outside the doctrine's band for a press. `prism` put its CTA press
        # on --dur-fast at 200ms, 40ms past the top of the band, with nothing faster
        # in the layer -- and the band is read out of MOTION_DOCTRINE.md, so this
        # plant also proves the parse works.
        "a press prescribed over a duration outside the doctrine's band",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/prism.md",
        lambda t: t.replace(
            "- **The press** is `translateY(1px)` over `--dur-press` —",
            "- **The press** is `translateY(1px)` over `--dur-fast` —", 1),
        "press band",
    ),
    (
        # The same class one layer down: a duration written as a literal where the
        # pack's own token holds that exact value. `showroom` wrote `0.3s` into two
        # prose sites while --dur-base was 0.3s in the layer beside them.
        "a duration literal in prose where a token holds that value",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/showroom.md",
        lambda t: t.replace(
            "colour → `--ink` over `--dur-base`", "colour → `--ink` over `0.3s`", 1),
        "a duration written twice",
    ),
    (
        # And a literal past the ceiling that no token accounts for, on a line that
        # does not claim to be an entrance.
        "a control duration past the doctrine's UI ceiling",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/showroom.md",
        lambda t: t.replace(
            "colour → `--ink` over `--dur-base`", "colour → `--ink` over `0.42s`", 1),
        "UI ceiling",
    ),
    (
        # A banned weight with no base layer. `<strong>` renders 700 with no
        # stylesheet involved, so the ban lived only in prose -- twenty-seven of
        # twenty-nine packs were in this state. Editing a token layer also trips the
        # kit-drift and mirror checks, which is why `expect` is not optional here.
        "a banned weight with no base rule in the token layer",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/tenor.css",
        lambda t: t.replace("strong, b {\n  font-weight: var(--weight-mono);",
                            "strong, b {\n  letter-spacing: 0;", 1),
        "ships no base rule",
    ),
    (
        # The other half of SG-03: the same class of defect in a wiring fact
        # rather than a count. DOCMAP opened its "Shared state" section with this
        # sentence while `.claude/agent-sync.json` carried `"gated": true` and
        # leases sat on disk. `expect` matters here -- the mutation removes a
        # bolded lead-in, which several link and prose checks also read.
        "DOCMAP re-asserting that this repo is ungated",
        "docs/DOCMAP.md",
        lambda t: t.replace(
            "**Gated — and the wiring is not restated here.**",
            "ungated — no lease mechanism is in force in this repo.",
            1,
        ),
        "'Shared state' re-asserts",
    ),
)


def self_test() -> int:
    src = Path(__file__).resolve().parent.parent
    ok = True
    for plant in PLANTS:
        label, rel, mutate = plant[:3]
        expect = plant[3] if len(plant) > 3 else None
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "repo"
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*COPY_IGNORE))
            target = dst / rel
            before = target.read_text(encoding="utf-8")
            after = mutate(before)
            if before == after:
                print(f"  BROKEN  {label}: the fixture changed nothing in {rel}")
                ok = False
                continue
            target.write_text(after, encoding="utf-8")
            env = {**os.environ, "SHELEG_ROOT": str(dst)}
            run = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), ],
                capture_output=True, text=True, env=env,
            )
            if run.returncode == 0:
                print(f"  MISSED  {label}  ({rel}) -- validator stayed green")
                ok = False
            elif expect is not None and expect not in run.stdout + run.stderr:
                # Red for some other reason is not proof. A token layer is also
                # copied into its kit, so an edit here trips the kit-drift check
                # too, and without this branch the plant would report "caught"
                # with the check it was written for never having run.
                print(f"  MISSED  {label}  ({rel}) -- went red without saying {expect!r}")
                ok = False
            else:
                print(f"  caught  {label}")

    # Two checks read `git`, which the copied tree above does not have -- `.git` is
    # in COPY_IGNORE, and a shallow CI checkout has no tags either. Their plants are
    # therefore calls rather than file copies, against the real core.
    for label, args, expect in (
        (
            "a CHANGELOG release with no tag and no declared reason",
            ("## [9.9.9] - 2026-08-20\n", "## Run stamps\n| x | y | 9.9.9 | z |\n## Log\n",
             ["1.0.0"]),
            "there is no tag for it",
        ),
        (
            "a declared untagged release whose tag now exists",
            ("## [1.28.0] - 2026-08-14\n", "## Run stamps\n| x | y | 1.28.0 | z |\n## Log\n",
             ["1.28.0"]),
            "the tag exists",
        ),
    ):
        del failures[:]
        _release_register(*args)
        fired = [f for f in failures if expect in f]
        if fired:
            print(f"  caught  {label}")
        else:
            print(f"  MISSED  {label} -- no failure said {expect!r}")
            ok = False
    del failures[:]

    # The one plant whose pass condition is silence. Every other fixture proves the
    # validator says no; this one proves a nested checkout changes neither the
    # verdict nor the count -- because the failure it guards against is a floor
    # measured against a tree that had a second copy of itself inside it.
    with tempfile.TemporaryDirectory() as tmp:
        dst = Path(tmp) / "repo"
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*COPY_IGNORE))
        argv = [sys.executable, str(Path(__file__).resolve())]
        env = {**os.environ, "SHELEG_ROOT": str(dst)}
        clean = subprocess.run(argv, capture_output=True, text=True, env=env)
        nest = dst / ".claude" / "worktrees" / "concurrent-run"
        (nest / "docs").mkdir(parents=True)
        (nest / ".git").write_text("gitdir: /nowhere\n", encoding="utf-8")
        # Both things the two ROOT walks look for, so a regression at either site shows.
        (nest / "docs" / "STOWAWAY.md").write_text(
            "# a file in a worktree\n\n[gone](./no-such-file.md)\n\nthirteen headings\n",
            encoding="utf-8",
        )
        dirty = subprocess.run(argv, capture_output=True, text=True, env=env)
        if dirty.returncode != 0:
            print("  MISSED  a nested checkout FAILED the gate -- it walked a worktree")
            ok = False
        elif dirty.stdout != clean.stdout:
            print(f"  MISSED  a nested checkout moved the count: "
                  f"{clean.stdout.strip()} -> {dirty.stdout.strip()}")
            ok = False
        else:
            print("  caught  a nested checkout changes neither verdict nor count")

    if not ok:
        print("\nself-test FAILED: a planted defect went undetected", file=sys.stderr)
        return 1
    print("\nself-test OK — every planted defect was caught")
    return 0


# ------------------------------------------------- the core role vocabulary
#
# CONTRIBUTING.md has always said "token naming is an interface across packs".
# Nothing enforced it, so twelve packs spoke twelve dialects: `--accent` was
# absent from two (`field-notes` calls it `--brand`, `orchard` `--cta`) and
# `--bg` from two more (`--paper`, `--base`). Every cross-pack document then
# named tokens some packs do not define -- SKILL.md's dataviz handoff promised
# `--accent-tint … --accent-deep`, a ramp NO pack defines in full.
#
# That is the quietest way this skill produces wrong output: an undefined custom
# property makes the declaration invalid at computed-value time, so the property
# falls back to its inherited or initial value with no error anywhere. The agent
# followed the instruction exactly and the page is wrong.
#
# Three roles, resolvable in every pack. A pack whose own name for the role
# differs adds an alias; it never renames or invents a colour.
CORE_VOCABULARY = ("--bg", "--ink")
# The accent is the same contract, declared rather than aliased: two packs name
# it something else AND could not take the alias -- `field-notes` measures its
# rust 5.5 from `--danger` (hard floor 10), so calling it `--accent` would make
# it a status peer and fail the palette gate. A pack either defines `--accent`
# or declares `/* @role accent: --X */`, and either way a cross-pack document
# can resolve it.
ROLE_ACCENT = re.compile(r"@role accent:\s*(--[a-z0-9-]+)")


def validate_core_vocabulary():
    tokens = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles" / "tokens"
    for name in _packs():
        css = read(tokens / f"{name}.css") or ""
        for tok in CORE_VOCABULARY:
            check(
                re.search(rf"^\s*{re.escape(tok)}\s*:", css, re.M) is not None,
                f"styles/tokens/{name}.css: no '{tok}'. The core role vocabulary is "
                f"{', '.join(CORE_VOCABULARY)} in every pack -- add an alias to whatever "
                f"this pack calls it, so a cross-pack document can name it truthfully",
            )
        m = ROLE_ACCENT.search(css)
        declared = m.group(1) if m else "--accent"
        check(
            re.search(rf"^\s*{re.escape(declared)}\s*:", css, re.M) is not None,
            f"styles/tokens/{name}.css: the accent role resolves to '{declared}', which "
            f"is not defined here. Define --accent, or declare '@role accent: --X' "
            f"pointing at a token that exists",
        )


# ------------------------------------------------- degrade to calm, observed
#
# "Degrade to calm" is one of this pack's five stated principles
# (SHELEG_DESIGN.md:53) and MOTION_DOCTRINE.md §9 spends a section on it:
# *"Shipping an animation without a reduced-motion path is a bug, not a polish
# item."* Until now the only thing that read that promise was sloplint's
# doctrine table, which asserts the STRING `prefers-reduced-motion` occurs
# somewhere in MOTION_DOCTRINE.md -- i.e. it checks that the doctrine mentions
# the rule, never that a shipped artifact obeys it. Measured 2026-08-19 with
# both gates green: 2 of 29 token layers shipped no branch at all --
# `instrument-console.css`, the pack that mandates a WebGL particle field, and
# `editorial-luxury.css` (B-040).
#
# Two decisions about how much this check may demand, both taken against what
# the doctrine WRITES rather than what would be tidy:
#
#  1. Mere existence of the at-rule is not enough. An empty
#     `@media (prefers-reduced-motion: reduce) {}` would satisfy a grep and
#     change nothing at runtime, and a check a defect can satisfy is the defect
#     this one exists to remove -- so the block must actually collapse a
#     duration to an instant value. §9: motion "collapse[s] to static or
#     instant -- not to 'slower'".
#  2. It does NOT demand that every declared duration collapse. `roster` keeps
#     `--dur-float-a/b` at 5.5s/6.5s on purpose, with the reason written at the
#     declaration: they drive infinite animations, a duration cannot stop one,
#     and at 0.01ms it strobes at exactly the reader the query protects. The
#     component layer pauses those with `animation-play-state`, which no custom
#     property can express. A per-token rule would have to break that or grow an
#     escape hatch; both are a different rule from the one §9 states. Logged as
#     B-045 instead of smuggled in here.
#
# Durations are detected by VALUE, not by name. `paperclip` spells its
# durations `--t-micro … --t-hero-copy` and `instrument-console` spells its
# curve `--motion-ease`, so a check keyed only on `--dur-*` would have read
# paperclip's branch as empty and passed a layer it never inspected.
MOTION_NAME = re.compile(r"^[ \t]*(--(?:dur|ease)-[a-z0-9-]+)\s*:", re.M | re.I)
CSS_TIME = re.compile(r"^[ \t]*(--[a-z0-9-]+)\s*:\s*(-?[0-9.]+)(ms|s)\s*(?:;|$)", re.M | re.I)
REDUCE_AT = re.compile(r"@media[^{]*prefers-reduced-motion\s*:\s*reduce[^{]*\{", re.I)
# 1ms. Every layer that ships a branch collapses to `0s` or to `0.01ms` (the
# value pigeonhole measured off its reference); nothing legitimate sits between
# 1ms and a duration a reader can see.
INSTANT_SECONDS = 0.001


def _reduce_blocks(text: str) -> list[str]:
    """Bodies of every `prefers-reduced-motion: reduce` at-rule, brace-balanced.

    Counted rather than sliced to a fixed window for the reason given at
    validate_kit_breakpoints: `blueprint` and `prism` ship two blocks, and a
    reader who adds a third must not silently stop being checked.
    """
    bodies = []
    for m in REDUCE_AT.finditer(text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            depth += text[i] == "{"
            depth -= text[i] == "}"
            i += 1
        bodies.append(text[m.end():i - 1])
    return bodies


def validate_reduced_motion():
    tokens = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles" / "tokens"
    for name in _packs():
        css = read(tokens / f"{name}.css") or ""
        if not MOTION_NAME.search(css):
            continue  # a layer that declares no motion owes no degradation
        bodies = _reduce_blocks(css)
        if not check(
            bool(bodies),
            f"styles/tokens/{name}.css: declares motion tokens and ships no "
            f"'@media (prefers-reduced-motion: reduce)' branch. MOTION_DOCTRINE.md §9: "
            f"shipping an animation without a reduced-motion path is a bug, not a polish "
            f"item -- collapse the durations here, in the layer an implementer copies",
        ):
            continue
        collapsed = []
        for body in bodies:
            for prop, num, unit in CSS_TIME.findall(body):
                seconds = float(num) / (1000.0 if unit.lower() == "ms" else 1.0)
                if seconds <= INSTANT_SECONDS:
                    collapsed.append(prop)
        check(
            bool(collapsed),
            f"styles/tokens/{name}.css: the reduced-motion branch collapses no duration to "
            f"an instant value. §9 says motion collapses to static or instant, not to "
            f"'slower' -- a branch that sets no duration to 0s (or below "
            f"{INSTANT_SECONDS * 1000:g}ms) satisfies a grep and changes nothing a reader "
            f"can feel",
        )


# ------------------------------------------------- the bundle stands alone
#
# The installed bundle is `plugins/<p>/skills/<s>/` and nothing above it: 32
# files, every one .md or .css. Three times now a rule inside it has instructed
# the reader to use something only the repository has, and each time the rule
# read as authoritative right up to the moment someone tried to follow it:
#
#   1.10.0  the `Contract: core` note cited `docs/evidence/backlog.md`
#   1.11.0  §7 said to record the pack version, in a bundle carrying none
#   1.11.0  §1 built an argument on "the same six component names" and named none
#
# The 1.10.0 run fixed the instance and not the class -- it swept the literal
# form (a repo path in backticks, now zero) and left the two forms that are not
# paths. This check covers the three NAMED forms above. It is not a proof that
# the bundle is self-sufficient in general; no check is. It is the three shapes
# that have actually shipped, so a fourth has to be a new shape.
REPO_ONLY_DIRS = ("docs/", "test/", "kits/", ".github/", "scripts/", "cursor/")


# ------------------------------------------------- the coordination claim
#
# The second half of the same defect as a stale count, in the same file. DOCMAP's
# "Shared state" section opened with `ungated` -- "no lease mechanism is in force
# in this repo" -- while `.claude/agent-sync.json` carried `"gated": true` and a
# nine-entry `guardedFiles`, and expired lease files sat in `.agent-sync/leases/`.
# A count and a wiring fact fail identically: restated in a second place, they
# drift from their home and nothing notices.
#
# So DOCMAP stops describing the wiring and points at the generated page instead,
# and this check holds the derivation together from both ends: the page must be
# generated (not hand-written) and must agree with the config, and DOCMAP must not
# reinstate a contradiction of it.
COORDINATION_DENIED = (
    "ungated",
    "no lease mechanism",
    "does not use it",
    "concurrent agents are not arbitrated",
)


def validate_coordination_claim():
    """`docs/AGENT_SYNC.md` is derived from the config, and DOCMAP defers to it."""
    page = read(ROOT / "docs" / "AGENT_SYNC.md")
    if page is None:
        # No coordination page at all is a legitimate state for a consumer
        # checkout, but it is not this repository's. Assert it and stop, rather
        # than returning early and quietly dropping three checks from the count.
        check(False, "docs/AGENT_SYNC.md is missing -- DOCMAP defers the whole of "
                     "'Shared state' to it, so its absence leaves that fact homeless")
        return
    check(
        page.lstrip().startswith("<!-- agent-sync:generated"),
        "docs/AGENT_SYNC.md: no 'agent-sync:generated' marker on the first line. "
        "DOCMAP points here instead of restating the wiring, which only holds "
        "while this page is regenerated from the config rather than edited",
    )
    # The page's own rendering of the fact, not a second opinion about it. If this
    # repo is ever genuinely ungated the page will say so, and then DOCMAP saying
    # the same thing is correct rather than stale -- which is the difference
    # between checking a claim and hard-coding today's answer.
    rendered = re.search(r"runs recorded \*\*(\w+)\*\*", page)
    gated = rendered is not None and rendered.group(1) == "gated"
    docmap = read(ROOT / "docs" / "DOCMAP.md") or ""
    shared = docmap.partition("## Shared state")[2]
    stale = [
        phrase for phrase in COORDINATION_DENIED
        # Narrating the old claim is allowed; re-asserting it is not. The
        # difference is the backtick-or-quote form this file uses to quote
        # itself -- so only a bare, unquoted phrase counts as an assertion.
        if re.search(rf'(?<![`"]){re.escape(phrase)}(?![`"])', shared)
    ]
    check(
        not (gated and stale),
        f"docs/DOCMAP.md: 'Shared state' re-asserts {stale} while "
        f"docs/AGENT_SYNC.md records this repo as gated. That sentence was wrong "
        f"for the whole of the coordination era; quote it to narrate it",
    )
    # The config lives under `.claude/`, which COPY_IGNORE strips from the
    # self-test's copy of the tree -- so this arm cannot be conditional on the
    # file existing without making the check COUNT depend on which copy is
    # running, and a floor that moves between the two turns every planted defect
    # red for the wrong reason. The check is emitted either way.
    raw = read(ROOT / ".claude" / "agent-sync.json")
    if raw is None:
        ok, msg = True, ""
    else:
        try:
            guarded = json.loads(raw).get("guardedFiles", [])
        except json.JSONDecodeError:
            guarded = None
        listed = re.findall(r"^- `(.+)`$", page.partition(
            "### Guarded files")[2].partition("###")[0], re.M)
        ok = guarded is not None and listed == guarded
        msg = (
            f"docs/AGENT_SYNC.md: its guarded-file list {listed} is not "
            f"`.claude/agent-sync.json`'s {guarded} -- the page is generated from "
            f"the config, so a difference means it is stale. Regenerate it with "
            f"`agent_sync.py setup`"
        )
    check(ok, msg)


# --------------------------------------------- the release register
#
# Three registers describe the same releases and none of them checked the others.
# Measured 2026-08-20: `CHANGELOG.md` carried TWO `## [1.35.0] - 2026-08-15`
# sections -- two different runs took the same number and the tag went to the
# second, with the first one's notes sitting ABOVE it, so a release extractor
# reading the first match for that heading would have shipped the wrong notes.
# `docs/evidence/retro.md`'s Run stamps table stopped at `v1.26.0` while `1.44.0`
# shipped, eighteen versions later -- and the retirement trigger in that file's
# standing instructions counts run stamps, so a short table makes every
# instruction look dormant. And four CHANGELOG sections record releases that have
# no tag at all.
#
# What is GATED and what is REPORTED, deliberately:
#   - a duplicate version heading FAILS. One number, one release.
#   - a release with no run stamp FAILS, from the version the table starts at.
#   - a missing TAG is REPORTED against a declared list. A tag nobody has is not
#     this run's to invent, and creating one to satisfy a gate would publish a
#     release that never happened. A missing tag NOT on the list fails, so the
#     next forgotten tag is caught while the four historical ones stay declared.
#   - tags are read with `git`, which is absent from the self-test's copied tree
#     and from a shallow CI checkout. No tags visible means the tag half cannot
#     run, and it says so rather than passing silently -- the count stays fixed
#     either way, so the ratchet does not move with whether git is available.
CHANGELOG_VERSION = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})", re.M)
# The version this project began stamping runs at: the first row of the Run stamps
# table. Everything before it predates task-pipeline in this repo.
STAMPS_FROM = (1, 5, 0)
# Releases with a CHANGELOG section and no tag, each already carrying a "Never
# released on its own" note in that section. Declared, not tolerated: an entry
# added here has to be argued for in the same commit.
UNTAGGED_RELEASES = {
    "1.4.0": "built and held; the release went out as 1.6.0",
    "1.5.0": "built and held; the release went out as 1.6.0",
    "1.28.0": "shipped inside a later version, see its CHANGELOG note",
    "1.30.0": "shipped inside a later version, see its CHANGELOG note",
}


def _git_tags() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "tag", "-l", "v*"],
            capture_output=True, text=True, timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    return [] if out.returncode else [l.strip()[1:] for l in out.stdout.split() if l.strip()]


def _release_register(changelog: str, retro: str, tags: list[str]) -> None:
    found = CHANGELOG_VERSION.findall(changelog)
    versions = [v for v, _ in found]
    if not check(bool(versions), "CHANGELOG.md: no '## [x.y.z] - date' sections found"):
        return
    dupes = sorted({v for v in versions if versions.count(v) > 1},
                   key=lambda s: tuple(map(int, s.split("."))))
    check(
        not dupes,
        f"CHANGELOG.md: {', '.join(dupes)} appears more than once -- one number, one "
        f"release. A tag points at one commit, so a second section under the same "
        f"heading is notes that will never be published or notes that will be "
        f"published in place of the right ones",
    )

    key = lambda s: tuple(map(int, s.split(".")))
    releases = [v for v in versions if key(v) >= STAMPS_FROM]

    # The Run stamps table, read as a table rather than as the whole file: the Log
    # below it narrates versions too, and a version mentioned in a story is not a
    # stamp.
    start = retro.find("## Run stamps")
    stop = retro.find("## Log", start + 1) if start != -1 else -1
    if not check(start != -1 and stop != -1,
                 "docs/evidence/retro.md: no '## Run stamps' table between '## Run stamps' "
                 "and '## Log' -- the retirement trigger in the standing instructions "
                 "counts rows in it"):
        return
    # ROWS only, not the section. The section's own header paragraph names the
    # range it was reconstructed over ("from `v1.27.0` to `v1.44.0`"), and reading
    # the prose let that sentence stand in for twenty-six rows -- the self-test
    # planted a deleted row and the check stayed green because the header still
    # mentioned the version.
    table = "\n".join(l for l in retro[start:stop].splitlines() if l.startswith("|"))
    # `\b` before the digits does not work: the rows write `` `v1.27.0` ``, and
    # between `v` and `1` there is no word boundary, so every backticked version in
    # the table read as absent and forty-six correct rows were reported missing.
    stamped = set(re.findall(r"(?<![\w.])v?(\d+\.\d+\.\d+)(?![\w.])", table))
    missing = [v for v in sorted(set(releases), key=key) if v not in stamped]
    check(
        not missing,
        f"docs/evidence/retro.md: '## Run stamps' has no row for "
        f"{', '.join(missing)} -- a release with no stamp is a release the "
        f"retirement trigger cannot count, and that trigger retires standing "
        f"instructions on a count of five",
    )

    # BOTH branches emit exactly two checks. An early return when git is absent
    # moved the count by one between a checkout with tags and one without, and the
    # ratchet caught it inside the hour: the self-test's copied tree has no `.git`,
    # so the floor measured here failed there. A gate whose count depends on the
    # environment cannot have a floor.
    visible = bool(tags)
    untagged = [v for v in sorted(set(releases), key=key) if v not in set(tags)] if visible else []
    undeclared = [v for v in untagged if v not in UNTAGGED_RELEASES]
    # The release BEING PREPARED is the one exception, and it has to be, or the bump
    # commit is uncommittable: the tag cannot exist before the commit that bumps to it.
    # It is exactly one version -- the newest CHANGELOG entry, and only while it equals
    # what `package.json` declares. Every OLDER untagged release still fails, which is
    # the defect this check was written for (four of them, 1.4.0 through 1.30.0).
    preparing = None
    if undeclared:
        # `Path`, not `pathlib.Path` — this module imports the class, not the package,
        # and a bare `except Exception` swallowed the NameError so the exemption
        # silently never applied. Narrowed, so the next mistake here is visible.
        try:
            declared = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))["version"]
        except (OSError, ValueError, KeyError):
            declared = None
        newest = sorted(set(releases), key=key)[-1] if releases else None
        if declared and newest == declared and declared in undeclared:
            preparing = declared
            undeclared = [v for v in undeclared if v != declared]
    check(
        not undeclared,
        f"CHANGELOG.md records {', '.join(undeclared)} and there is no tag for it. "
        f"A tag nobody has is not a gate's to invent, so this is reported and not "
        f"created: either tag the commit that shipped it, or add it to "
        f"UNTAGGED_RELEASES with the reason and put a note in its section",
    )
    if preparing:
        report.append(f"release {preparing} is in the CHANGELOG with no tag yet -- a "
                      f"release in preparation, and the tag is cut after the commit that "
                      f"bumps to it")
    stale = sorted(v for v in UNTAGGED_RELEASES if v in set(tags)) if visible else []
    check(
        not stale,
        f"UNTAGGED_RELEASES declares {', '.join(stale)} as untagged and the "
        f"tag exists -- a declared exception nobody removed is an exception that "
        f"stops describing the tree",
    )
    report.append(
        f"release register: {len(set(versions))} versions, {len(tags)} tags, "
        f"{len(untagged)} declared untagged ({', '.join(untagged) or 'none'})"
        if visible else
        "release register: tags are not visible in this checkout (no .git, or a "
        "shallow clone) -- the duplicate-version and run-stamp halves ran, the "
        "missing-tag audit did not"
    )


def validate_release_register():
    _release_register(
        read(ROOT / "CHANGELOG.md") or "",
        read(ROOT / "docs/evidence/retro.md") or "",
        _git_tags(),
    )


# ------------------------------------- the cross-pack status vocabulary
#
# `SURFACE_COMPOSITION.md` carries the library's only per-pack map of which status
# tokens exist where, and an agent handing a pack to `dataviz` reads it to decide
# whether `var(--warning)` resolves. It was PROSE -- "the pair `--ok` / `--warn` in
# `workbench` and `instrument-console`; the pair `--good` / `--warning` in
# blueprint, cyclorama…" -- so nothing could read it, and at twenty-nine packs it
# was wrong for three of them: `workbench` had grown a full quartet, `atrium` had
# `--info` and `--danger` the map did not mention, and `instrument-console` was
# about to. The same class as B-016's accent count, which was fixed by hand twice
# before `@role accent:` made it derivable.
#
# So the map is a table and this reads it. An undefined custom property does not
# error -- `color: var(--good)` where --good is undefined is invalid at
# computed-value time and falls back silently -- which is why a wrong entry here is
# a wrong chart nobody sees fail.
STATUS_ROLES = ("good", "ok", "success", "warn", "warning", "danger", "error", "info")
STATUS_VARIANTS = ("-soft", "-weak", "-tint", "-dim", "-deep", "-bright", "-light",
                   "-on-dark", "-mark", "-ink")
# The table is found by its header and read to the first non-row line. A bare
# two-column row pattern over the whole file matched four other tables in it and
# reported "the status table lists 'lowest contrast', which is not a pack".
STATUS_TABLE_HEAD = "| Status set (non-variant tokens, root block) | Packs |"
STATUS_ROW = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def _status_set(css: str) -> set[str]:
    """The pack's own status tokens: root block, non-variant, not `--on-*`."""
    out = set()
    for m in re.finditer(r"^\s*(--[a-z0-9-]+)\s*:", _root_block(css), re.M):
        name = m.group(1)
        if name.startswith("--on-") or name.endswith(STATUS_VARIANTS):
            continue
        if name.lstrip("-").split("-")[0] in STATUS_ROLES:
            out.add(name)
    return out


def validate_status_vocabulary():
    skill = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    doc = read(skill / "SURFACE_COMPOSITION.md") or ""
    tokens = skill / "styles" / "tokens"
    claimed: dict[str, set[str]] = {}
    lines = doc.splitlines()
    try:
        head = next(i for i, l in enumerate(lines) if l.strip() == STATUS_TABLE_HEAD)
    except StopIteration:
        head = -1
    for line in lines[head + 2:] if head != -1 else []:
        row = STATUS_ROW.match(line)
        if not row:
            break
        cell, packs = row.group(1), row.group(2)
        want = set(re.findall(r"--[a-z0-9-]+", cell))
        for name in re.split(r",\s*", packs.strip()):
            if name:
                claimed[name] = want
    if not check(bool(claimed), "SURFACE_COMPOSITION.md: no status-vocabulary table found -- "
                                "the per-pack status map has to be readable, or it goes stale "
                                "silently and a chart resolves an undefined property"):
        return
    for name in _packs():
        css = read(tokens / f"{name}.css")
        if css is None:
            continue
        got = _status_set(css)
        if not check(name in claimed,
                     f"SURFACE_COMPOSITION.md: the status table does not list '{name}' "
                     f"-- every pack is in the map or the map is not a map"):
            continue
        check(
            got == claimed[name],
            f"SURFACE_COMPOSITION.md: the status table says '{name}' has "
            f"{', '.join(sorted(claimed[name])) or 'no status tokens'} and its token layer "
            f"declares {', '.join(sorted(got)) or 'none'} -- var() on a token a pack does "
            f"not define is invalid at computed-value time and fails silently",
        )
    for name in sorted(set(claimed) - set(_packs())):
        check(False, f"SURFACE_COMPOSITION.md: the status table lists '{name}', "
                     f"which is not a pack in this library")


# ------------------------------------------------- the pack contradicts itself
#
# Four sweeps over one class of defect: a pack's TOKEN LAYER and its PROSE stating
# different rules. A reader copies the token layer verbatim -- every pack says so
# in its own Palette -- so when the two disagree the layer wins and the prose lies.
# Every one of these was found by reading two files side by side, which is not a
# method that scales to twenty-nine packs times two files.
#
# All four are scoped to what a machine can settle without guessing intent: a token
# nobody named, a colour that cannot be seen where it is drawn, a component with two
# radii, a duration outside a band the doctrine states in a table.

# A shadow or a glow is the one token class a component cannot approximate: an
# author who cannot find it in the prose invents one, and the pack's whole
# elevation argument goes with it. `scoreboard` shipped four shadows under a
# comment that counted "two soft stacks and a hairline" and named three in its
# Texture section; `instrument-console` mandated `--signal-glow` in three places
# and never wrote the token's name once, while its Bans permitted only the other
# glow -- so the pack banned its own signature motif.
ELEVATION_TOKEN = re.compile(r"^\s*(--(?:shadow|elev)[a-z0-9-]*|--[a-z0-9-]*glow):", re.M)


CSS_COMMENT = re.compile(r"/\*.*?\*/", re.S)


def _root_block(css: str) -> str:
    """The first declaration block, which is the pack's own token layer.

    Theme and reduced-motion blocks re-declare the same names; reading the whole
    file would report a token twice and pin the count to how many themes a pack
    happens to ship.

    Comments are stripped FIRST. `datasheet.css` carries `html { font-size: 8px }`
    inside a header comment explaining the reference's rem base, so a brace scan
    over the raw text found that one, returned nine characters, and silently
    excluded the whole pack from both sweeps that read this. A block scanner that
    reads a comment as code skips exactly the packs whose authors explained
    themselves most.
    """
    css = CSS_COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), css)
    start = css.find("{")
    if start == -1:
        return css
    depth, i = 1, start + 1
    while i < len(css) and depth:
        depth += css[i] == "{"
        depth -= css[i] == "}"
        i += 1
    return css[start + 1:i - 1]


def validate_elevation_tokens_named():
    """Every shadow and glow a pack ships is named in the pack's prose."""
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    for name in _packs():
        css = read(styles / "tokens" / f"{name}.css")
        prose = read(styles / f"{name}.md")
        if css is None or prose is None:
            continue
        for tok in sorted(set(ELEVATION_TOKEN.findall(_root_block(css)))):
            check(
                tok in prose,
                f"styles/tokens/{name}.css: ships '{tok}' and styles/{name}.md never "
                f"names it -- a shadow a reader cannot find in the prose is a shadow "
                f"they will invent, and the pack's elevation argument goes with it",
            )


# A component with two radii. `showroom` specified its specimen frame as
# `--radius-2xl` in Texture and `--radius-3xl` in Components -- 16px against 20px --
# and its nesting rule subtracts the padding from the OUTER value, so every inner
# radius derived from the wrong one was wrong too. The kit shipped 20px, which is
# how the defect was settled: the implementation is the tiebreak, and the prose is
# what two readers disagree about.
#
# SCOPE. A component is a bolded row label in the pack's `## Components` table --
# the pack's own list of the things it specifies. A radius is attributed to a
# component only where the token stands within four words of the component's name,
# or where it appears in that component's own table row. Anything looser reads the
# nesting example ("a --radius-sm chip inside a --radius-lg row") as three
# contradictions instead of one sentence.
RADIUS_TOKEN = re.compile(r"--(?:radius|r)-[a-z0-9-]+")
COMPONENT_ROW = re.compile(r"^\|\s*\*\*([^*|]+)\*\*\s*\|", re.M)


def _radius_claims(prose: str, component: str) -> dict[str, list[int]]:
    """{radius token: [line numbers]} for one component name, in one pack."""
    stem = component.strip().lower().rstrip("s")
    found: dict[str, list[int]] = {}
    for lineno, line in enumerate(prose.splitlines(), 1):
        low = line.lower()
        if stem not in low:
            continue
        if line.startswith("|"):
            row = COMPONENT_ROW.match(line)
            if not row or row.group(1).strip().lower().rstrip("s") != stem:
                continue
            hits = RADIUS_TOKEN.findall(line)
        else:
            # A radius token modifies the noun that FOLLOWS it, so the span read is
            # from the token to the next radius token or the end of the line. The
            # first draft read 60 characters either side, and the nesting sentence
            # every pack writes -- "a --radius-sm chip inside a --radius-lg row
            # inside a --radius-3xl specimen frame" -- then reported three
            # contradictions where the sentence states one rule per noun.
            hits = []
            spans = [m.start() for m in RADIUS_TOKEN.finditer(line)] + [len(line)]
            for i, m in enumerate(RADIUS_TOKEN.finditer(line)):
                if stem in low[m.end():spans[i + 1]]:
                    hits.append(m.group(0))
        for h in hits:
            found.setdefault(h, []).append(lineno)
    return found


def validate_radius_single_valued():
    """A component's radius is stated once, or the pack states two rules."""
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    for name in _packs():
        prose = read(styles / f"{name}.md")
        if prose is None:
            continue
        table = _section(prose, "## Components")
        for component in sorted({m.group(1).strip() for m in COMPONENT_ROW.finditer(table)}):
            claims = _radius_claims(prose, component)
            if len(claims) < 2:
                continue
            where = "; ".join(
                f"{tok} at {', '.join(str(n) for n in lines)}"
                for tok, lines in sorted(claims.items())
            )
            check(
                False,
                f"styles/{name}.md: '{component}' is given {len(claims)} different radii "
                f"({where}) -- one of them is what the kit ships and the rest are what a "
                f"reader will copy; and a nesting rule keyed to the outer value carries "
                f"the error inward",
            )


# A duration outside the band the doctrine states for it. Both numbers are parsed
# out of MOTION_DOCTRINE.md rather than repeated here, because a gate that hard-codes
# the doctrine's numbers stops agreeing with the doctrine the first time it is edited
# -- and the doctrine is the document this library asks packs to obey.
#
# `prism` put its CTA press on `--dur-fast` at 200 ms, 40 ms past the top of the
# press band, with nothing faster in the layer to reach for. `showroom` wrote `0.3s`
# into two prose sites instead of naming `--dur-base`, which is the same number and
# is what the layer ships.
PRESS_ROW = re.compile(r"^\|\s*Button press[^|]*\|\s*(\d+)\s*[–—-]\s*(\d+)\s*ms", re.M | re.I)
UI_CEILING = re.compile(r"UI motion stays at or under\s+(\d+)\s*ms", re.I)
DUR_DECL = re.compile(r"^\s*(--dur[a-z0-9-]*)\s*:\s*([0-9.]+)(m?s)\s*;", re.M)
PRESS_WORD = re.compile(r"\bpress(?:ed|es)?\b", re.I)
# An entrance is not UI motion and the doctrine says so; a pack claiming the
# exemption has to use the word, which is also what makes the claim reviewable.
ENTRANCE_WORD = re.compile(r"\bentrance|\breveal|\bscroll-linked|\bscrub", re.I)
# "instant on purpose" is a real answer to a press band and `cyclorama` gives it.
INSTANT = re.compile(r"\b0s\b|instant", re.I)


def _ms(value: str, unit: str) -> float:
    return float(value) * (1.0 if unit == "ms" else 1000.0)


def validate_motion_bands():
    """A press sits inside the doctrine's press band; UI motion sits under its ceiling."""
    skill_dir = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    doctrine = read(skill_dir / "MOTION_DOCTRINE.md") or ""
    band = PRESS_ROW.search(doctrine)
    ceiling = UI_CEILING.search(doctrine)
    if not check(band is not None, "MOTION_DOCTRINE.md: no 'Button press feedback' row with a "
                                   "ms band -- the packs' press durations cannot be checked "
                                   "against a table that does not state one"):
        return
    if not check(ceiling is not None, "MOTION_DOCTRINE.md: no 'UI motion stays at or under N ms' "
                                      "ceiling -- the boundary has to be a number a gate can apply"):
        return
    lo, hi = float(band.group(1)), float(band.group(2))
    top = float(ceiling.group(1))

    styles = skill_dir / "styles"
    for name in _packs():
        css = read(styles / "tokens" / f"{name}.css")
        prose = read(styles / f"{name}.md")
        if css is None or prose is None:
            continue
        durations = {m.group(1): _ms(m.group(2), m.group(3))
                     for m in DUR_DECL.finditer(_root_block(css))}
        # `## Motion flavor` is in scope because that is where a pack prescribes
        # its entrance set, and an entrance is the one case the ceiling exempts --
        # so it is also the section where an exemption gets claimed for a control.
        for heading in ("## Components", "## Micro-interactions", "## Motion flavor"):
            body = _section(prose, heading)
            for line in body.splitlines():
                if not PRESS_WORD.search(line) or INSTANT.search(line):
                    continue
                # The token nearest the word `press`, so a line that also prescribes
                # a hover duration is not read as putting the hover on the press.
                pos = PRESS_WORD.search(line).start()
                near = sorted(
                    ((abs(m.start() - pos), m.group(1)) for m in
                     re.finditer(r"(--dur[a-z0-9-]*)", line)),
                )
                if not near or near[0][1] not in durations:
                    continue
                tok = near[0][1]
                got = durations[tok]
                check(
                    lo <= got <= hi,
                    f"styles/{name}.md: the press is prescribed over {tok} at {got:g}ms, "
                    f"outside the doctrine's {lo:g}-{hi:g}ms press band -- add a duration "
                    f"inside the band rather than reaching for the nearest one",
                )
            # A raw duration in prose is a value the token layer does not govern.
            for m in re.finditer(r"`(\d+(?:\.\d+)?)(ms|s)`", body):
                got = _ms(m.group(1), m.group(2))
                lineno = body[:m.start()].count("\n") + 1
                named = [k for k, v in durations.items() if v == got]
                check(
                    not named,
                    f"styles/{name}.md: '{heading}' writes the literal {m.group(0)} where "
                    f"{'/'.join(named)} is that exact value -- a duration written twice is a "
                    f"duration that drifts (line {lineno} of the section)",
                )
                if named:
                    continue
                check(
                    got <= top or ENTRANCE_WORD.search(body.splitlines()[lineno - 1]) is not None,
                    f"styles/{name}.md: '{heading}' prescribes {m.group(0)} for a control, past "
                    f"the doctrine's {top:g}ms UI ceiling, and the line does not say it is an "
                    f"entrance -- an entrance may run longer, a control may not",
                )


# A pack that bans a weight or a slant and ships no base layer has banned nothing.
# `<strong>` renders at 700 and `<em>` renders italic with no stylesheet involved, so
# a ban that lives only in prose is invisible to every grep over CSS and to every
# browser. Two of twenty-nine shipped the block; `tenor`'s own comment states the
# rule this check enforces -- "any pack in this library that bans a weight or a slant
# owes the same block" -- which is a doctrine nothing was reading.
WEIGHT_BAN = re.compile(
    r"no\s+(?:bold|700|800|900)\b|there\s+is\s+no\s+bold\b|no\s+weight\s+(?:above|over)\b",
    re.I,
)
SLANT_BAN = re.compile(r"no\s+italics?\b|has\s+no\s+italic\b|never\s+italic\b", re.I)
# The selector has to be the bare elements. `\b[^{]*\{` accepted
# `strong, b.disabled {` -- a rule for one class, which leaves every other
# `<strong>` on the UA default. The self-test found this by planting exactly that.
WEIGHT_BASE = re.compile(
    r"^\s*(?:strong|b)\s*,\s*(?:strong|b)\s*(?:,[^{.\[:]*)?\{[^}]*font-weight", re.M | re.S)
SLANT_BASE = re.compile(
    r"^\s*(?:em|i)\s*,\s*(?:em|i)\s*(?:,[^{.\[:]*)?\{[^}]*font-style", re.M | re.S)


def validate_emphasis_base_layer():
    """A banned weight or slant is banned in CSS, not only in prose."""
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    for name in _packs():
        prose = read(styles / f"{name}.md")
        css = read(styles / "tokens" / f"{name}.css")
        if prose is None or css is None:
            continue
        for label, ban, base, elements, prop in (
            ("weight", WEIGHT_BAN, WEIGHT_BASE, "strong, b", "font-weight"),
            ("slant", SLANT_BAN, SLANT_BASE, "em, i", "font-style"),
        ):
            hit = ban.search(prose)
            if not hit:
                continue
            check(
                base.search(css) is not None,
                f"styles/tokens/{name}.css: styles/{name}.md bans a {label} "
                f"({hit.group(0).strip()!r}) and the token layer ships no base rule for it "
                f"-- add '{elements} {{ {prop}: … }}', because the UA supplies one whether "
                f"the pack does or not and the ban is invisible to a grep over CSS",
            )


def validate_bundle_self_sufficiency():
    bundle = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    if not bundle.is_dir():
        return
    # Form 1 -- a repo-only path offered to a reader who does not have the repo.
    path_ref = re.compile(
        r"`(" + "|".join(re.escape(d) for d in REPO_ONLY_DIRS) + r")[A-Za-z0-9_./-]+`"
    )
    for doc in sorted(bundle.rglob("*.md")):
        rel = doc.relative_to(ROOT)
        for match in path_ref.finditer(read(doc) or ""):
            check(
                False,
                f"{rel}: cites '{match.group(0)}', which is a repository path -- "
                "the installed bundle has no such directory, so this instruction "
                "dead-ends for every reader who did not clone the repo",
            )
    # Form 2 -- a rule whose input is a version the bundle does not carry.
    # Unconditional on purpose. A first draft gated this on the substring "pack
    # version" appearing in the bridge, which made the check evadable by
    # rephrasing the very sentence it protects -- the check would go quiet and
    # the count would fall by one, which is the shape `test/floors.json` exists
    # to catch and not a shape worth shipping. The bundle carries its version or
    # it does not; no wording anywhere changes that.
    check(
        skill_metadata_version() is not None,
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md: the bundle must carry its own "
        "version -- DESIGN_SYNC_BRIDGE.md §7 tells the reader to record the pack "
        "version in the synced project, and an installed reader has nothing else "
        "to read it from",
    )
    # Form 3 -- a counted claim about a set the bundle never enumerates. The
    # count and the members have to travel together, or the reader has to guess
    # which six, and guessing is how a value gets invented and believed.
    for doc in sorted(bundle.rglob("*.md")):
        text = read(doc) or ""
        rel = doc.relative_to(ROOT)
        if "six component names" not in text:
            continue
        missing = [name for name in SPINE if f"`{name}`" not in text]
        check(
            not missing,
            f"{rel}: claims 'the same six component names' but does not name "
            f"{', '.join(missing)} -- a counted claim ships with its members or "
            "the reader guesses them",
        )


def _disclose_routing(msg):
    """A check that could not run, said out loud rather than counted as a pass."""
    print(f"  unlooked: {msg}")


def check_routed_triggers_still_advertised():
    """The family's routing hook fires on words this description has to keep.

    B-54, 2026-08-16: `sheleg-design` 1.37.0 shipped green on its own gate having dropped
    a phrase from its description that was a live trigger in the umbrella's
    `lib/triggers.js`. This repository has no way to know that table exists, and it
    releases BEFORE the umbrella re-pins, so the umbrella found out minutes after the tag.
    A hook firing on a promise nobody made is the defect; a patch release was the cost.

    **The table is not copied here.** The umbrella's own checker is asked, reading the
    module the hook itself calls, so there is no duplicate to drift. When no umbrella sits
    above this checkout — the ordinary state of a standalone clone, and of CI — this
    discloses instead of passing, because a check that cannot look must never read as one
    that looked.
    """
    script = os.path.join(str(ROOT), "..", "..", "test", "advertised_check.js")
    if not os.path.isfile(script):
        _disclose_routing("routed triggers — no sshlg-skills umbrella above this checkout")
        return
    try:
        proc = subprocess.run(["node", script, "--member", "sheleg-design", "--root", str(ROOT)],
                              capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        _disclose_routing(f"routed triggers — could not run the umbrella's checker ({exc})")
        return
    if proc.returncode == 1:
        check(False, (proc.stdout + proc.stderr).strip())
    elif proc.returncode != 0:
        _disclose_routing(f"routed triggers — {(proc.stderr or 'the checker could not look').strip()}")


def main():
    if sys.argv[1:]:
        # An unknown flag silently running the normal pass is how a suite reports
        # green for a self-test it never ran. This script had no argv handling at
        # all: `validate.py --self-test` printed OK and exited 0.
        if sys.argv[1:] == ["--self-test"]:
            return self_test()
        print(
            f"FAIL: unknown argument {sys.argv[1]!r} (expected --self-test or none)",
            file=sys.stderr,
        )
        sys.exit(2)
    validate_manifests()
    validate_skills()
    validate_commands()
    validate_cursor_rules()
    validate_fork_reciprocity()
    validate_installer_sync()
    validate_kits()
    validate_links()
    validate_counted_claims()
    validate_pack_enumerations()
    validate_contract_terminology()
    validate_contract_split()
    validate_contract_declaration()
    validate_core_vocabulary()
    validate_reduced_motion()
    validate_pack_container_answer()
    validate_kit_breakpoints()
    validate_release_register()
    validate_status_vocabulary()
    validate_elevation_tokens_named()
    validate_radius_single_valued()
    validate_motion_bands()
    validate_emphasis_base_layer()
    validate_bundle_self_sufficiency()
    validate_coordination_claim()
    check_routed_triggers_still_advertised()

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        sys.exit(1)
    check_floor("validate.py", checks)
    for line in report:
        print(f"  {line}")
    print(f"OK ({checks} checks)")


if __name__ == "__main__":
    # `main()` bare dropped the self-test's return code on the floor: with
    # --self-test it printed "self-test FAILED" and exited 0, so `npm run
    # selftest` stayed green through a self-test that had failed. The argv
    # handling above was added to close exactly this class one layer up and did
    # not reach the exit code. The normal pass exits through sys.exit() inside
    # main(), so SystemExit(None) is the success path.
    raise SystemExit(main())
