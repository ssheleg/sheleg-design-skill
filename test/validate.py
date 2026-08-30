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
        "STYLE_PACK_INDEX.md",
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
    skill_text = (read(skills_dir / PLUGIN / "SKILL.md") or "") + "\n" + (
        read(skills_dir / PLUGIN / "STYLE_PACK_INDEX.md") or ""
    )
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
    # Extended past thirty on 2026-08-21, when the thirty-first pack landed and
    # every check reading this table went red at once. The failure is the right
    # one -- a vocabulary that stops silently would let `thirty-one` read as
    # unparseable and the count go unchecked -- but the cheap wrong fix is to
    # write the numeral in the prose instead, which degrades the sentence to
    # satisfy the parser. Carried to forty so the next few releases do not
    # rediscover this.
    31: "thirty-one", 32: "thirty-two", 33: "thirty-three", 34: "thirty-four",
    35: "thirty-five", 36: "thirty-six", 37: "thirty-seven", 38: "thirty-eight",
    39: "thirty-nine", 40: "forty",
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


def _counted_sources() -> list[str]:
    """The one corpus both count checks read.

    It was inline in `validate_counted_claims` until a second check needed the
    same list; two copies of a source list is two lists that drift, and this one
    already grew once (the three manifests, 1.19.0).
    """
    return [
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
    for rel in _counted_sources():
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
    (f"{PLUGIN_DIR}/skills/{PLUGIN}/STYLE_PACK_INDEX.md", "the routed pack index"),
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


# --------------------------------------------------------- derived surfaces
#
# Two surfaces stopped being authored on the family audit (2026-08-29) and are
# now derived by a script in scripts/, which this gate imports rather than
# re-implements -- one derivation, two callers, no second copy to drift. The
# import is ROOT-relative on purpose: the self-test re-runs this file against a
# copied tree, and the copy must be judged by its own scripts.
def _load_script(name: str):
    import importlib.util

    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_contents_lists():
    """Every >100-line bundle reference carries a `## Contents` list derived
    from its own headings.

    The authoring rule is the Agent Skills one -- a partial read of a long
    reference sees the map or sees nothing -- and the family audit (SHD-01)
    found 42 of 44 qualifying files without one, which is where a hand-kept
    list always ends up. So the list is derived: `scripts/gen_contents.py`
    owns the derivation, `--write` regenerates, and this check refuses a file
    whose list is missing or has drifted from the headings it maps.
    """
    gen = _load_script("gen_contents.py")
    files = gen.targets(ROOT)
    check(
        bool(files),
        "gen_contents.targets() found no qualifying reference -- the walk is broken",
    )
    for path in files:
        rel = path.relative_to(ROOT)
        what = gen.problem(read(path) or "")
        check(
            what is None,
            f"{rel}: {what} -- a reference over {gen.LINE_FLOOR} lines is read "
            "partially, and the map is derived, never authored. Run "
            "`python3 scripts/gen_contents.py --write`",
        )
    report.append(
        f"Contents lists: {len(files)} bundle references over {gen.LINE_FLOOR} "
        "lines, every list derived from its own headings"
    )


def validate_manifest_descriptions():
    """Both host-facing manifest descriptions equal the STYLE_PACK_INDEX.md
    derivation.

    The family audit (SHD-03) found them append-scarred -- `patchbay` and
    `nameplate` glossed twice, `deskmate` never, `chorus` carrying a
    neighbour's orphaned parenthesis -- which is what per-release hand-appends
    converge to. `scripts/gen_manifest_descriptions.py` owns the derivation;
    a description that differs from it was hand-edited and is refused.
    """
    gen = _load_script("gen_manifest_descriptions.py")
    try:
        want = gen.description(ROOT)
    except SystemExit as exc:
        check(False, f"manifest descriptions could not be derived -- {exc}")
        return
    plugin = load_json(f"{PLUGIN_DIR}/.claude-plugin/plugin.json", []) or {}
    market = load_json(".claude-plugin/marketplace.json", []) or {}
    entry = (market.get("plugins") or [{}])[0]
    for rel, got in (
        (f"{PLUGIN_DIR}/.claude-plugin/plugin.json", plugin.get("description")),
        (".claude-plugin/marketplace.json", entry.get("description")),
    ):
        check(
            got == want,
            f"{rel}: the description differs from the STYLE_PACK_INDEX.md "
            "derivation -- this surface is generated, never hand-appended. Run "
            "`npm run gen-descriptions`",
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
    skill_path = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "STYLE_PACK_INDEX.md"
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


# B-006. A pack can only be chosen by a request that reaches this skill, and the
# description's trigger list is what the runtime matches on. `briefing-room` ships for
# "investor & board decks, briefings, talks as a page" and the word `deck` appeared nowhere
# in the description (measured 2026-08-20, 955 of 1024 chars with 69 spare) — so a request
# for a presentation deck reached nothing, and the pack was undiscoverable by the only
# phrasing anybody would use for it.
#
# The list is enumerated rather than derived from the pack table, deliberately: that table's
# "used for" column is prose about an INDUSTRY (consumer biotech, enterprise data
# infrastructure) far more often than about a surface, and a check demanding every noun in it
# would fail on words no user ever types. What must be reachable is the SURFACE class — what
# the thing being designed IS — and there are few enough of those to name.
SURFACE_CLASSES = {
    "deck": "briefing-room — investor & board decks, 16:9, a deck rather than a page",
    "dashboard": "workbench, scoreboard, instrument-console — product UI",
    "landing": "the cinematic scroll-driven pages this skill opens with",
    "admin": "the internal-tool surfaces the packs are chosen for",
    "mobile": "the phone-sized screens several packs specify",
    "token": "the token layer every pack ships",
    "theme": "light/dark twins",
}


def validate_every_surface_class_is_discoverable():
    """Every surface this library designs for is reachable from the description."""
    text = read(ROOT / PLUGIN_DIR / "skills" / PLUGIN / "SKILL.md") or ""
    m = re.search(r"^description:\s*(.*?)(?=^[a-z-]+:|^---)", text, re.S | re.M)
    if not check(m is not None, "SKILL.md: no description to check for discoverability"):
        return
    desc = m.group(1).lower()
    for word, why in sorted(SURFACE_CLASSES.items()):
        check(
            word in desc,
            f"SKILL.md description never says '{word}' — {why}. A surface the description "
            "cannot be asked for is a pack nobody reaches, whatever the pack table says",
        )

def validate_contract_declaration():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    skill = read(styles.parent / "STYLE_PACK_INDEX.md") or ""
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
            # B-001. `core` must NAME what it declines, not merely be narrow. Six of the
            # seven core packs already did; `awning` shipped a bare `Contract: core`
            # (2026-08-20), which reads to an implementer as an unfinished pack rather
            # than as a decided one — and the difference is the whole value of the line.
            # An absence and a decision look identical until one of them is written down.
            declared = text[m.start():m.start() + 400]
            names = sum(1 for s in PACK_SECTIONS_WIDENED_ONLY if f"## {s}" in declared
                        or s in declared)
            check(
                "not" in declared.lower() and names >= 2,
                f"{rel}: 'Contract: core' names nothing it declines -- write which of "
                f"{', '.join(PACK_SECTIONS_WIDENED_ONLY)} this pack leaves to the "
                "implementer, so a narrow pack reads as decided rather than unfinished",
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
    # EVERY file a kit can carry a width query in, not just `styles.css`.
    # Measured 2026-08-20: zero width queries live outside `styles.css` today and
    # zero CSS files fall outside the old `*/src/styles.css` glob — so the guard's
    # coverage was complete and complete BY ACCIDENT. A `.tsx` with a
    # `@media (max-width: …)` in a template literal, or a second stylesheet beside
    # the first, would have been invisible.
    files = sorted(
        f for f in kits_dir.rglob("*")
        if f.is_file()
        and f.suffix in (".css", ".tsx", ".ts", ".jsx", ".js")
        and "node_modules" not in f.parts
    )
    if not check(len(files) >= 2,
                 "kits/ holds fewer than two source files — the breakpoint guard "
                 "was not exercised, and a check that could not look is not a pass"):
        return
    for css in files:
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

    # TODO-CONTAINER is a legitimate escape and it may only shrink. It stood at 2
    # on 2026-08-20 — `blueprint`'s tick and column rule, `datasheet`'s instrument
    # grid — and both were resolved by doing the arithmetic the marker deferred:
    # the grid already collapsed by `auto-fit`, so the query was deleted, and the
    # other two turned out to be ornament rather than fitting, so they are PAGE.
    # An escape with no ceiling becomes the habit it was meant to interrupt.
    todos = sum((read(f) or "").count("TODO-CONTAINER") for f in files)
    try:
        ceiling = json.loads(FLOORS.read_text(encoding="utf-8")).get("kit_todo_container_at_most")
    except (OSError, ValueError):
        ceiling = None
    if check(ceiling is not None,
             "test/floors.json has no `kit_todo_container_at_most` — a deferral with "
             "no ceiling is a deferral that multiplies"):
        check(
            todos <= ceiling,
            f"{todos} TODO-CONTAINER marker(s) across the kits, above the pinned "
            f"{ceiling}. Each one defers arithmetic; deferring more of it needs the "
            f"pin moved in the same commit, with the reason",
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
        # The hole the product tier of this node's certification proved with a plant:
        # `REDUCE_DUR_DECL` keyed on a token NAME, so `paperclip`'s six `--t-*`
        # durations, seven `--stagger*`, `--marquee-cycle` and `--scan-period` -- 13
        # time-valued tokens across 10 layers -- were outside the walk entirely. The
        # tier removed this exact line, watched the gate print `0 silent` and exit 0,
        # and reported it. Matching by value took the walk from 112 durations to 127.
        # Kept here so the name-keyed form cannot come back.
        "a time-valued token whose NAME carries no duration word, dropped from its branch",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/paperclip.css",
        lambda t: re.sub(r"^\s*--t-hero-art\s*:\s*0s;[^\n]*\n", "", t, count=1, flags=re.M),
        "says nothing about it",
    ),
    (
        # The v1.37.5 regression, planted back: the carrier removed while the edit
        # reads as additive. Derived from the phrase rather than its surroundings.
        "a description edit that drops the phrase a T1 task depends on",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md",
        lambda t: t.replace("scroll-linked or scrubbed motion", "scroll-linked motion", 1),
        "the phrase T1's",
    ),
    (
        # The preamble's count, restated wrongly -- which is the state it shipped in
        # until 2026-08-20, saying twenty-six against a table of thirty-four.
        # Derived: whatever word opens the sentence is replaced.
        "a run-stamp count the preamble restates instead of recomputing",
        "docs/evidence/retro.md",
        lambda t: re.sub(r"\*\*([A-Za-z-]+|\d+)(\s+rows below are marked)",
                         r"**Twenty-six\2", t, count=1),
        "and the table holds",
    ),
    (
        # A plant with no `expect`, planted into the plant table itself. Derived:
        # the fourth element of the FIRST entry is dropped, whatever it says.
        "a plant that does not name the check it exercises",
        "test/validate.py",
        lambda t: re.sub(r'(\n        "does not say which components size",)', "", t, count=1),
        "carry no `expect` string",
    ),
    (
        # B-049's instance, planted back: the value that made the naming matter.
        # Derived from the token rather than the comment, so it keeps landing
        # however the explanation is reworded.
        "a token whose comment names a dropdown at 150ms past the dropdown band",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/bulletin.css",
        lambda t: t.replace("--dur-panel: 0.4s; /* the nav sheet",
                            "--dur-panel: 0.4s; /* the nav dropdown", 1),
        "bands at 150–250 ms",
    ),
    (
        # scoreboard's ring table in the form it shipped: one header base for both
        # rows, and the sand-only ring reported at its --bg ratio. Derived from the
        # `Measured on` column rather than pinned to the numbers.
        "a table row confined to one surface and measured against another",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/scoreboard.md",
        # The header goes back with it. A 4-cell row under a 5-column header is
        # caught by the table-shape guard first, so a plant that changes only the
        # row proves that guard works and says nothing about this one -- the
        # defect as it actually shipped was internally consistent.
        lambda t: t.replace(
            "  | Ring | Value | Role | Measured on | Ratio |\n  |---|---|---|---|---|\n"
            "  | `--ring-focus` | `#FF4801` | solid 2px, every surface but one | `--bg` `#FAF9F5` | 3.23:1 |\n"
            "  | `--ring-focus-sand` | `#221D16` | `--surface-sand` only, where the accent misses the floor at 2.97:1 | `--surface-sand` `#F5EFE2` | 14.60:1 |",
            "  | Ring | Value | Role | On `--bg` |\n  |---|---|---|---|\n"
            "  | `--ring-focus` | `#FF4801` | solid 2px, every surface but one | 3.23:1 |\n"
            "  | `--ring-focus-sand` | `#221D16` | `--surface-sand` only, where the accent misses the floor at 2.97:1 | 15.88:1 |",
            1),
        "describes a pairing that never",
    ),
    (
        # prism's oversight, planted back: a duration declared and the branch
        # silent about it. Derived — the collapse line is dropped whatever its
        # value — and `expect` is mandatory, because a token-layer edit also
        # trips the kit-drift and mirror checks.
        "a duration the reduced-motion branch says nothing about",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/prism.css",
        lambda t: re.sub(r"^\s*--dur-press\s*:\s*0s;\s*\n", "", t, count=1, flags=re.M),
        "says nothing about it",
    ),
    (
        # A kept duration whose reason is deleted. atrium keeps four flute
        # durations under reduce because the canvas is REMOVED; strip the markers
        # and the file no longer says whether that is a decision or a bug.
        "a duration kept above an instant with its reason removed",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/atrium.css",
        lambda t: t.replace("KEPT — the canvas is removed, not slowed", "")
                   .replace("KEPT — as above", "")
                   .replace("ON PURPOSE", "by choice"),
        "names no reason",
    ),
    (
        # The promise, unkept. pigeonhole keeps --dur-marquee at 0.01ms on the
        # ground that the KIT pauses the animation, because no custom property
        # can. Remove the kit's rule and the exception is a sentence.
        "a component-layer stop promised by a token layer and missing from the kit",
        "kits/pigeonhole/src/styles.css",
        lambda t: t.replace(".pg-marquee { animation-play-state: paused; }",
                            ".pg-marquee { opacity: 1; }", 1),
        "has no such rule inside a reduced-motion branch",
    ),
    (
        # The defect this session made: a second module-level constant with a
        # name already taken. The later binding wins with no error.
        "a gate constant whose name is already bound at module level",
        "test/validate.py",
        lambda t: t.replace("\nPRESS_WORD = re.compile(",
                            "\nREDUCE_DUR_DECL = re.compile(r\"never\")\nPRESS_WORD = re.compile(", 1),
        "assigned more than once",
    ),
    (
        # The defect the commit closing B-042 introduced: the prose prescribes
        # `--dur-press` and the layer stops defining it. Derived -- the declaration
        # line is dropped whatever its value becomes -- and the `expect` string is
        # mandatory, because an edit to a token layer also trips the kit-drift and
        # `.cursor` mirror checks. Without it this plant proves those two work.
        "a token the prose prescribes and the layer stops defining",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/instrument-console.css",
        lambda t: re.sub(r"^\s*--dur-press\s*:[^;]*;[^\n]*\n", "", t, count=1, flags=re.M),
        "resolves to nothing, silently",
    ),
    (
        # The fifth subject, carved on 2026-08-20, with its carve taken back out.
        # Derived rather than pinned: every line matching the carve pattern is
        # dropped, so the plant keeps landing however the wording is rewritten --
        # and it must drop ALL of them, because this pack states the exception
        # twice (the doctrine quote and the token) and removing one leaves the
        # check green over a pack that no longer carves anything. A plant that
        # left a third occurrence standing is a defect this repo has already had.
        "a pack that mandates a scrub and takes its `ease: none` exception back out",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/instrument-console.md",
        lambda t: "\n".join(
            l for l in t.splitlines() if not SCRUB_CARVED.search(l)),
        # Required, and the reason is measured: with the pin lifted to 5 this plant
        # was STILL reported caught, because an edit to a pack trips the `.cursor`
        # mirror check too. Without this string the plant proved the mirror check
        # works and said nothing about the one it was written for.
        "carve no `ease: none` exception",
    ),
    (
        # The rule the check measures packs against, deleted. Without this case the
        # check would keep printing a count after the doctrine stopped saying
        # anything -- five packs measured against nothing, reported green.
        "the scrub easing rule removed from the doctrine the packs are measured against",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/MOTION_DOCTRINE.md",
        lambda t: t.replace("easing must be `none`", "easing should stay gentle", 1),
        "the rule this check enforces has to live somewhere first",
    ),
    (
        # A widened pack that stops answering the container bullet.
        #
        # This plant was BROKEN from the day it was written and reported `caught`
        # on every run until 2026-08-20. It replaced the bullet's LABEL --
        # "**Container queries**" -> "**Breakpoints**" -- and `scoreboard`'s
        # Responsive section answers twice: the label, and `container-type:
        # inline-size` on the line below it. `CONTAINER_ANSWER` still matched, the
        # check stayed correctly green, and the only failure was the `.cursor`
        # mirror drift. So the plant proved the mirror check worked for a week and
        # never once exercised the check it was written for. Found by running the
        # thirteen expect-less plants and reading what each actually made fail.
        #
        # Derived, and it removes EVERY answer in the section rather than one:
        # a label-only removal is exactly the defect above.
        "a widened pack whose Responsive section stops answering the container question",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/scoreboard.md",
        lambda t: t.replace(
            _section(t, "## Responsive"),
            CONTAINER_ANSWER.sub("(removed by the plant)", _section(t, "## Responsive")),
            1),
        "does not say which components size",
    ),
    (
        # A kit component sized by the screen instead of by its box: the defect
        # this release exists to close, planted back in.
        "a kit breakpoint that goes back to the viewport with no reason given",
        "kits/scoreboard/src/styles.css",
        lambda t: t.replace("@container (max-width: 231px)", "@media (max-width: 767px)", 1),
        "sizes a component by the screen instead of by its box",
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
        "a count is checkable, so it is checked",
    ),
    (
        # Derived since 1.57.0: the description is generated from the pack index,
        # so the pinned literal `briefing-room (dark 16:9 deck), ` stopped
        # existing and the fixture changed nothing. Whatever gloss the generator
        # currently writes for the pack, removing the whole entry is the defect.
        "a manifest naming three packs of twelve",
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        lambda t: re.sub(r"briefing-room \([^)]*\), ", "", t, count=1),
        "the plugin description an agent host reads names",
    ),
    (
        # The remainder that has now been stale in two consecutive pack releases:
        # 1.13.0 shipped "the other six" of thirteen, and 1.19.0's draft shipped
        # "the other seven" of fourteen. Derived from whatever the paragraph
        # currently says, so it cannot pin itself to a number the next release
        # edits -- the failure mode of the plant this one sits beside.
        "the core-contract remainder left behind by a count edit",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/STYLE_PACK_INDEX.md",
        # `[\w-]+`, not `\w+`: at the twenty-eighth pack the remainder crossed twenty
        # and became "twenty-one", which a bare `\w+` cannot match -- so the plant
        # changed nothing and the self-test reported a check that had quietly stopped
        # being exercised. A fixture that cannot find its own target is a hole in the
        # gate, and it opens on exactly the release this plant exists to catch.
        lambda t: re.sub(r"The other [\w-]+ answer all four", "The other five answer all four", t, count=1),
        "answer all four widened sections",
    ),
    (
        # The same class as the first plant, in a file the source list did not
        # read until 1.19.0 -- which is how "twelve pluggable style packs" sat
        # above a list of thirteen for two releases. Derived from whatever the
        # manifest currently claims, for the reason given at the first plant.
        # `visual` joined the modifier chain when the descriptions became
        # generated (1.57.0), and the fixture that required the bare form
        # changed nothing. Optional, so the plant survives either wording.
        "a count that is true of an older release, in a manifest",
        ".claude-plugin/marketplace.json",
        lambda t: re.sub(r"[a-z-]+ (pluggable (?:visual )?style packs)", r"six \1", t, count=1),
        "a count is checkable, so it is checked",
    ),
    (
        "the contract called by a stale number",
        "CONTRIBUTING.md",
        lambda t: t.replace("The contract is **thirteen**", "The contract is **nine-heading**"),
        "One name, one number",
    ),
    (
        "a pack that does not declare what it leaves undecided",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/workbench.md",
        lambda t: re.sub(r"^Contract: .*\n", "", t, count=1, flags=re.M),
        "a reader cannot tell what this pack leaves them to decide",
    ),
    (
        "a version out of five-way sync",
        "package.json",
        lambda t: t.replace('"version": "', '"version": "9.', 1),
        "version mismatch",
    ),
    (
        "the bundle's own version removed, leaving §7's rule with nothing to read",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SKILL.md",
        lambda t: re.sub(r"^metadata:\n  version: .*\n", "", t, count=1, flags=re.M),
        "must carry a nested 'metadata.version'",
    ),
    (
        "a repo-only path offered to a reader who has no repo",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/DESIGN_SYNC_BRIDGE.md",
        lambda t: t.replace(
            "## 7. Round-trip discipline",
            "## 7. Round-trip discipline\n\nSee `docs/evidence/backlog.md` for the open rows.",
            1,
        ),
        "which is a repository path",
    ),
    (
        "a counted claim whose members stopped travelling with the count",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/DESIGN_SYNC_BRIDGE.md",
        lambda t: t.replace("The six are `Button`, `Card`, `Chip`,", "The six are `Card`, `Chip`,", 1),
        "a counted claim",
    ),
    (
        "a style pack the style-pack index does not route to",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/STYLE_PACK_INDEX.md",
        lambda t: t.replace("./styles/maquette.md", "./styles/nowhere.md"),
        "is not linked from the pack table",
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
        lambda t: re.sub(r"[a-z]+(?:-[a-z]+)?-kit", "fourteen-kit", t, count=1),
        "says 'fourteen-kit' but there are",
    ),
    (
        # The same hole in digits. Worth its own plant because the number and the
        # word reach the pattern by different branches of the same alternation,
        # and a widening that fixed only the spelled form would pass the plant
        # above while leaving `14-kit` invisible.
        "a stale count hyphenated onto its noun, in digits",
        "docs/DOCMAP.md",
        lambda t: re.sub(r"[a-z]+(?:-[a-z]+)?-kit", "14-kit", t, count=1),
        "says '14-kit' but there are",
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
    (
        # The deferral put back, now that the ceiling is zero.
        "a TODO-CONTAINER marker added back to a kit",
        "kits/blueprint/src/styles.css",
        lambda t: t.replace("/* PAGE — and the arithmetic is why.",
                            "/* TODO-CONTAINER B-999 — deferred again.\n   PAGE — and the arithmetic is why.", 1),
        "above the pinned 0",
    ),
    (
        "an @font-face in a token layer",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/manpage.css",
        lambda t: t + "\n@font-face { font-family: X; src: url(x.woff2); }\n",
        "declares `@font-face`",
    ),
    (
        # A real declaration, not the comment three files already carry — the
        # check strips comments first, which is what makes the two distinguishable.
        "a font-display declaration outside any @font-face",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/manpage.css",
        lambda t: t + "\n:root { font-display: swap; }\n",
        "which is a descriptor and only means anything",
    ),
    (
        # A width query in a .tsx, which the guard could not see until 2026-08-20.
        "a kit width query outside styles.css",
        "kits/datasheet/src/Button.tsx",
        lambda t: t + (
            "\n/* a styled block with no marker */\n"
            "const responsive = `@media (max-width: 600px) { .x { display: none } }`;\n"),
        "sizes a component by the screen",
    ),
    (
        # showroom's focus ring, put back the way it shipped: a literal, then the
        # relative form outside @supports, reading as guarded and guarding nothing.
        "relative colour in a custom property outside @supports",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/showroom.css",
        lambda t: t.replace(
            "  --ring-focus: 0 0 0 3px rgba(38, 109, 240, 0.35);",
            "  --ring-focus: 0 0 0 3px rgba(38, 109, 240, 0.35);\n"
            "  --ring-focus: 0 0 0 3px rgb(from var(--accent) r g b / 0.35);", 1),
        "is not a fallback",
    ),
    (
        # The row's own scenario: a tenth hue added to the layer and nowhere else.
        "a category hue the token layer ships and the pack never names",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tokens/pigeonhole.css",
        lambda t: t.replace("  --cat-reply-ink:",
                            "  --cat-invoice-ink: #7a2e00; /* 4.5:1 */\n  --cat-reply-ink:", 1),
        "and the pack never names",
    ),
    (
        "an excluded set with no stated carrier",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/pigeonhole.md",
        # BOTH phrasings, because the check accepts either — breaking one leaves
        # the other standing and the plant proves nothing.
        lambda t: t.replace("The label word is\n**required**.",
                            "The label word is\noptional.", 1)
                   .replace("**What carries the category is the word, and it is required.**",
                            "**The hue carries the category.**", 1),
        "never states what carries the category instead",
    ),
    (
        # atrium's four gaps, put back — the state it shipped in for eleven
        # iterations of the loop that widened it.
        "a Components section that drops a class it used to answer",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/atrium.md",
        # The WHOLE bullet, not its label: the body names skeleton, shimmer and
        # spinner in the course of saying the reference has none, so removing the
        # heading alone leaves the class answered and the plant proves nothing.
        lambda t: re.sub(
            r"- \*\*Loaders\*\* — \*\*none, and that is measured.*?never had\.\n",
            "- **Texture** — flat colour, nothing further.\n", t, count=1, flags=re.S),
        "component class(es) unanswered",
    ),
    (
        # The sum `field-notes` shipped, put back into a live passage.
        "a worked radius sum that does not compute",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/ora.md",
        lambda t: t.replace("(12 − 12 = 0 leaves the", "(12 − 12 = 7.2 leaves the", 1),
        "does not compute",
    ),
    (
        # The state six packs were in before 2026-08-20: marked standalone in the
        # table, silent about the ceiling in their own file.
        "a standalone pack whose Register states no ceiling",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/router.md",
        lambda t: t.replace("**Motion ceiling:** no pack ceiling is pinned here",
                            "**Texture note:** nothing further is pinned here", 1),
        "states no motion ceiling and does not say it has none",
    ),
    (
        "a Register that says no ceiling is pinned and names one anyway",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/router.md",
        lambda t: t.replace("the dial turns up what is left after that table",
                            "the dial turns up what is left after that table, though "
                            "`MOTION_INTENSITY` above **6** buys nothing", 1),
        "cannot both be true",
    ),
    (
        # The disagreement the row was filed for, in the direction that matters:
        # the doctrine's summary drifting from the pack that owns the number.
        "a doctrine ceiling that disagrees with the pack's Register",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/tenor.md",
        lambda t: t.replace("so `MOTION_INTENSITY` above **4** has nothing legal to buy",
                            "so `MOTION_INTENSITY` above **7** has nothing legal to buy", 1),
        "The Register is the home",
    ),
    (
        # Exactly what `atrium` shipped for eight iterations: widened in its own
        # file, still marked core in the table nobody read against it.
        "a table mark left behind after a pack was widened",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/STYLE_PACK_INDEX.md",
        lambda t: t.replace("consumer health and high-trust DTC |",
                            "consumer health and high-trust DTC · **core contract** |", 1),
        "declares `Contract: widened`",
    ),
    (
        "a core pack the table does not mark",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/STYLE_PACK_INDEX.md",
        lambda t: t.replace("dashboards, admin, internal tools · (standalone) · **core contract** |",
                            "dashboards, admin, internal tools · (standalone) |", 1),
        "the table does not mark it",
    ),
    (
        # The exact number that shipped over this tree for four hours.
        "a theme split restated wrong in the skeleton",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/STYLE_PACK_TEMPLATE.md",
        lambda t: re.sub(r"\d+ of them, then \d+, then \d+\.", "10 of them, then 13, then 5.", t, count=1),
        "and the packs' own `Themes:` lines derive",
    ),
    (
        # Exactly the sentence that sat wrong in `tenor` at twenty-nine packs:
        # a definite article, a numeral, and no noun for a gate to check.
        "a count written as `the <numeral>` with no noun",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SURFACE_COMPOSITION.md",
        lambda t: re.sub(r"across\n(the [a-z-]+) packs:", r"across\n\1:", t, count=1),
        "names no noun, so nothing can check it",
    ),
    (
        "a pack with no `Themes:` declaration",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/atrium.md",
        lambda t: t.replace("\nThemes: ", "\nThemes-was: ", 1),
        "no `Themes:` line",
    ),
    (
        # atrium ships one block and nothing else, so claiming a twin is a claim
        # its own token layer contradicts.
        "a `Themes:` claiming a dark twin the token layer does not ship",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/atrium.md",
        lambda t: t.replace("Themes: light only — no second block of any kind ships here.",
                            "Themes: light + dark — a full theme twin.", 1),
        "and the token layer says the opposite",
    ),
    (
        "a pack with no `Rank:` declaration",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/workbench.md",
        lambda t: t.replace("\nRank: ", "\nRank-was: ", 1),
        "no `Rank:` line",
    ),
    (
        # workbench is the row's own case: four unordered statuses, no ramp.
        "a `Rank: ordered` where the token layer ships no ramp",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/workbench.md",
        lambda t: t.replace("Rank: unordered — 4 status role(s)",
                            "Rank: ordered — `--sev-1` → `--sev-2`. 4 status role(s)", 1),
        "ships 0 ordered token(s)",
    ),
    (
        # Exactly what `atrium` shipped the day before this check existed: a hero
        # full of measurements and no statement of how many lines the headline may
        # take. `maquette` is the fixture because its hero carries exactly ONE
        # phrase of each kind — measured, rather than picked — so removing one
        # leaves the other standing and each plant proves its own half.
        "a `## Hero` with no line ceiling",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/maquette.md",
        lambda t: t.replace("- **Line ceiling: three**, at 66px", "- **Sized** at 66px", 1),
        "states no line ceiling",
    ),
    (
        # And what `showroom` shipped: the ceiling stated, and nothing saying what
        # holds it.
        "a `## Hero` whose ceiling has nothing holding it",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/styles/maquette.md",
        lambda t: t.replace("- **Line ceiling: three**, at 66px and 1.06 leading.",
                            "- **Line ceiling: three.**", 1),
        "and not what holds it",
    ),
    (
        # What three rows in this very file looked like on 2026-08-20: a shell
        # pipe inside a code span, shifting every cell after it. The rows read
        # correctly to a human and returned prose where a script asked for the
        # status, which is how the queue that orders this repository's work
        # skipped both `high` rows for ten iterations.
        "an unescaped pipe inside a board row",
        "docs/evidence/backlog.md",
        lambda t: t.replace("| B-007 |", "| B-007 | `grep x | wc -l` —", 1),
        "cells and its header declares",
    ),
    (
        # SHD-01's shipped state, planted back: a long reference whose map is
        # gone. Renaming the heading rather than deleting the block keeps the
        # plant one line and still reads as "no `## Contents` list".
        "a >100-line reference whose Contents list was dropped",
        f"{PLUGIN_DIR}/skills/{PLUGIN}/MOTION_DOCTRINE.md",
        lambda t: t.replace("## Contents", "## Map", 1),
        "carries no `## Contents` list",
    ),
    (
        # SHD-03's shipped state, planted back: one more clause hand-appended to
        # a description that is now derived. The mutation lands inside the JSON
        # string, so the manifest still parses and only the derivation check can
        # say what is wrong with it.
        "a manifest description hand-appended past the derivation",
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        lambda t: t.replace(
            "pluggable visual style packs",
            "pluggable visual style packs, and one glossed twice", 1),
        "differs from the STYLE_PACK_INDEX.md derivation",
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
        (
            # What 1.45.0 actually shipped: the release summary written above the
            # accumulated section, which was then left in place.
            "an [Unreleased] section sitting below a released version",
            ("## [1.28.0] - 2026-08-14\nsummary\n\n## [Unreleased]\ndetail\n",
             "## Run stamps\n| x | y | 1.28.0 | z |\n## Log\n", ["1.28.0"]),
            "sits BELOW a released version",
        ),
        (
            "two [Unreleased] sections, so one set of notes publishes twice or never",
            ("## [Unreleased]\na\n\n## [Unreleased]\nb\n\n## [1.28.0] - 2026-08-14\nc\n",
             "## Run stamps\n| x | y | 1.28.0 | z |\n## Log\n", ["1.28.0"]),
            "sections -- one of them is",
        ),
    ):
        del failures[:]
        _release_register(*args, complete=True)
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


def _git(*args) -> str:
    """One git question, or the empty string when git cannot answer it."""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args],
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return ""
    return "" if out.returncode else out.stdout.strip()


def _git_tags() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "tag", "-l", "v*"],
            capture_output=True, text=True, timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    return [] if out.returncode else [l.strip()[1:] for l in out.stdout.split() if l.strip()]


def _release_register(changelog: str, retro: str, tags: list[str],
                      complete: bool | None = None) -> None:
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

    # `[Unreleased]` MUST be the first section, and there may be one. The 1.45.0
    # release wrote its summary above the accumulated section and left it in
    # place, so the shipped version's own detail sat under `[Unreleased]` and the
    # next entry would have been written on top of already-published notes. The
    # duplicate-version check above cannot see it: `Unreleased` is not a version.
    unrel = [m.start() for m in re.finditer(r"(?m)^## \[Unreleased\]", changelog)]
    check(
        len(unrel) <= 1,
        f"CHANGELOG.md: {len(unrel)} '## [Unreleased]' sections -- one of them is "
        f"notes that will be published twice or not at all",
    )
    if unrel and found:
        first_release = re.search(r"(?m)^## \[\d+\.\d+\.\d+\]", changelog)
        check(
            first_release is None or unrel[0] < first_release.start(),
            "CHANGELOG.md: '## [Unreleased]' sits BELOW a released version, so "
            "notes that have already shipped are labelled unreleased and the next "
            "entry lands on top of them. Fold them into the version that shipped "
            "them and open a fresh section at the top",
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
    # `bool(tags)` treated ONE tag as the whole tag set, and that made the v1.45.0
    # release red for a reason that had nothing to do with the release: a release
    # checkout (`actions/checkout` with `ref: v1.45.0`) fetches that ref and nothing
    # else, so 49 shipped releases looked untagged. The same run on `main` passed
    # because a shallow checkout fetches NO tags, the check switched itself off, and
    # the difference between "no view" and "a one-tag view" was invisible.
    #
    # So a partial view is now named as one. Two signals, both cheap: a shallow
    # repository cannot answer this question at all, and a single tag against a
    # CHANGELOG of dozens is a fetched ref rather than a tag set.
    # `complete` lets a FIXTURE state that its synthetic tag list is the whole set.
    # Without it the heuristic below switched the check off for the two plants, whose
    # lists are one tag each by design, and the self-test reported them MISSED — a
    # guard turned off by the very rule meant to stop it answering blind.
    if complete is None:
        shallow = _git("rev-parse", "--is-shallow-repository") == "true"
        complete = bool(tags) and not shallow and len(tags) > 1
    visible = bool(tags) and complete
    if tags and not visible:
        report.append(
            f"untagged releases — the tag view here is partial "
            f"({len(tags)} tag(s){', shallow clone' if shallow else ''}), so which "
            f"releases carry a tag could not be read. A check that cannot look must "
            f"not read as one that looked"
        )
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


# ------------------------------------- the board's own columns
#
# The board orders every remaining piece of work in this repository, and a
# reader of it -- human or script -- takes the priority and the status from the
# column the header names. An unescaped `|` inside a row shifts every cell after
# it, so the status column comes back holding a fragment of prose and the
# priority holds another.
#
# Measured on 2026-08-20: THREE rows here carried a shell pipe inside a code span
# (`sort -u`, `cut -d/ -f2`, `grep … | wc -l`). Their status cells read
# `sort -u`, `` `datasheet` run, stage 0 `` and `medium`, and the queue that
# orders this loop's work skipped both `high` rows in the file -- B-004 and
# B-014 -- for ten iterations. The rows were never wrong; the table was.
#
# The rule is the cheapest one that catches it: a data row has exactly the cells
# its own header declares.
BOARD_FILES = ("docs/evidence/backlog.md", "docs/evidence/verification.md")
BOARD_ROW = re.compile(r"^\**[A-Z]{1,3}-\d+")


def _table_cells(line: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def validate_board_columns():
    for rel in BOARD_FILES:
        text = read(ROOT / rel)
        if text is None:
            continue
        width = None
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.startswith("#"):
                width = None            # a heading ends the previous table
                continue
            if not line.startswith("|"):
                continue
            cells = _table_cells(line)
            if cells and cells[0].lower().strip("* ") == "id":
                width = len(cells)
                continue
            if width is None or not BOARD_ROW.match(cells[0]):
                continue
            if all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells):
                continue
            check(
                len(cells) == width,
                f"{rel}:{lineno}: row {cells[0]} has {len(cells)} cells and its "
                f"header declares {width}. An unescaped `|` inside the row shifts "
                f"every cell after it, so the status and priority columns come "
                f"back holding prose -- escape it as `\\|`",
            )



# ------------------------------------- the hero's own two obligations
#
# The skeleton has asked for both since 1.5.0 -- "state the line ceiling for the
# display headline AND the container width that keeps it there" -- and nothing
# read the answer. Measured 2026-08-20 across the 23 packs that carry a `## Hero`
# heading: one states no ceiling (`atrium`, widened the day before by the run that
# then wrote this check) and one states no measure (`showroom`, which gives the
# ceiling and not what holds it). One live subject each way, which is what makes
# it a check rather than an assertion.
#
# WHAT COUNTS AS A MEASURE is deliberately wide, because the answer is not always
# a max-width: `showroom`'s reference holds two lines with `text-wrap: balance` at
# `leading .95` inside a centred column with side padding and no max-width at all.
# A word budget is an answer too. What is NOT an answer is silence.
HERO_CEILING = re.compile(
    r"ceiling|(?:two|three|one|four)\s+lines?\b|max(?:imum)?\s+\S{0,12}\s*lines?"
    r"|never wraps|wraps to", re.I)
HERO_MEASURE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:rem|px|ch|em)\b|--container|--page-max|--content"
    r"|max-width|\bmeasure\b|\bcolumn\b|text-wrap:\s*balance|word budget|\bwords\b", re.I)


def validate_hero_states_its_obligations():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    if not styles.is_dir():
        return
    looked = 0
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        lines = (read(md) or "").split("\n")
        # the HEADING, never the string: a `core` pack names `## Hero` inside its
        # own contract line to say it declines it, and a substring search counted
        # six such packs as having a hero section.
        at = [i for i, l in enumerate(lines) if l.rstrip() == "## Hero"]
        if not at:
            continue
        looked += 1
        i = at[0]
        j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
        sec = "\n".join(lines[i:j])
        rel = f"styles/{md.name}"
        check(
            bool(HERO_CEILING.search(sec)),
            f"{rel}: '## Hero' states no line ceiling for the display headline. The "
            f"skeleton has asked since 1.5.0, and a headline that wraps to five lines "
            f"is a broken hero rather than a long one -- state the number",
        )
        check(
            bool(HERO_MEASURE.search(sec)),
            f"{rel}: '## Hero' states a ceiling and not what holds it. A measure, a "
            f"container token, `text-wrap: balance` or a word budget all count; "
            f"silence does not, because the next author picks one and it is not yours",
        )
    if looked < 2:
        _skips.append("fewer than two packs carry a '## Hero' heading — the hero "
                      "obligations were not checked")



# ------------------------------------- the silences a pack owes an answer to
#
# `Contract: core` names four sections and nothing else, so a pack's OTHER
# silences stayed undeclared. B-008's case: `workbench` ships four status roles
# and no severity ramp, and a fresh-context agent building an incident list
# inferred a rank scale from role descriptions and only found the gap by hitting
# it.
#
# The row offered two answers -- a free "also not specified here" list, or four
# is the boundary. Both were refused, and the measurement is why. A free list is
# unbounded and uncheckable: 29 packs would write 29 different ones and nothing
# could compare them. And four is NOT the boundary, because two silences are
# real and common. Counted 2026-08-20:
#
#   * THEMES -- 11 packs ship a dark twin, 13 ship one block, and 5 ship a second
#     block that is a SURFACE variant rather than a theme (`[data-surface="dark"]`,
#     `[data-state="alarm"]`). "Does this pack have a dark mode?" got three
#     different answers depending on how you looked.
#   * RANK -- exactly ONE pack of 29 ships an ordered ramp (`tenor`:
#     `--sev-ask` -> `--sev-limit` -> `--sev-never`). The other 28 were silent.
#
# So the answer is a fixed pair of questions whose answers are DERIVED from the
# token layer, which makes them comparable across packs and checkable against the
# thing they describe. This re-derives both and refuses a declaration that does
# not match its own tokens.
RANK_TOKEN = re.compile(r"--((?:sev|severity|rank|level|priority|tier)[a-z0-9-]*)\s*:", re.I)
DARK_BLOCK = re.compile(r'theme="dark"|\.dark\b|prefers-color-scheme', re.I)


def validate_pack_declares_its_silences():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    tokens = styles / "tokens"
    if not tokens.is_dir():
        return
    looked = 0
    for css in sorted(tokens.glob("*.css")):
        md = styles / f"{css.stem}.md"
        if not md.is_file():
            continue
        looked += 1
        text = read(md) or ""
        rel = f"styles/{md.name}"
        body = read(css) or ""

        themes = re.search(r"(?m)^Themes:\s*(.+)$", text)
        if not check(themes is not None,
                     f"{rel}: no `Themes:` line. 11 packs ship a dark twin, 13 ship one "
                     f"block and 5 ship a surface variant that is not a theme — a reader "
                     f"asking 'is there a dark mode' has to read the token layer to find out"):
            continue
        said = themes.group(1)
        # the token layer's own answer
        blocks = [m.group(1) for m in re.finditer(r"(?m)^([^{}\n]+)\{", body)]
        extra = [b.strip() for b in blocks
                 if b.strip() not in (":root",) and not b.strip().startswith("@")
                 and "--" not in b and len(b.strip()) < 60]
        has_dark = any(DARK_BLOCK.search(b) for b in extra)
        claims_twin = "theme twin" in said and "not a theme twin" not in said
        check(
            claims_twin == has_dark,
            f"{rel}: `Themes:` says {'a full theme twin' if claims_twin else 'no theme twin'} "
            f"and the token layer says the opposite. The declaration is derived from the "
            f"blocks the layer ships, so a mismatch means one of the two moved alone",
        )

        rank = re.search(r"(?m)^Rank:\s*(.+)$", text)
        if not check(rank is not None,
                     f"{rel}: no `Rank:` line. Exactly one pack in the library ships an "
                     f"ordered severity ramp; the other 28 are silent, and an agent building "
                     f"an incident list infers a scale from role descriptions and finds the "
                     f"gap by hitting it"):
            continue
        ramp = sorted(set(RANK_TOKEN.findall(body)))
        claims_ordered = rank.group(1).strip().lower().startswith("ordered")
        check(
            claims_ordered == bool(ramp),
            f"{rel}: `Rank:` says {'ordered' if claims_ordered else 'unordered'} and the "
            f"token layer ships {len(ramp)} ordered token(s). One of the two moved alone",
        )
    if looked < 2:
        _skips.append("fewer than two packs have a token layer — the silence "
                      "declarations were not checked")



# ------------------------------------- a count whose noun is only implied
#
# `validate_counted_claims` reads "N packs". It cannot read "the accent role
# resolves to `--accent` in twenty-seven," where the noun is implied by context —
# which is how that sentence sat wrong at ten, then thirteen, then fourteen, each
# corrected by hand and each unguarded again the moment it was.
#
# THREE PATTERNS WERE TRIED AND TWO THROWN AWAY, measured on this tree:
#
#   1. every numeral with no counted noun after it -> 2553 spans. Ordinary prose
#      ("three cards", "one motion methodology"). Useless.
#   2. a numeral CLOSING its clause -> 62 spans, and nearly all correct ellipsis:
#      "one gate of four", "wrong two times out of three". Still useless.
#   3. the same, restricted to sentences naming a library noun -> 69 spans, most
#      of them the word "one" in prose. Worse than 2.
#
# What IS precise is the definite article: `the <numeral>` closing a clause, which
# in English asserts a known set. SEVEN spans in the whole corpus, three of them
# library counts, and one of the three was WRONG — `tenor` said token names are
# "not uniform across the twenty" at twenty-nine packs.
#
# So the class is closed by making the form checkable rather than by guessing at
# it: name the noun, and `validate_counted_claims` covers it forever. This refuses
# the bare form. It is deliberately narrow -- a numeral without `the` is prose.
# BUILT FROM `NUMBER_WORDS` rather than spelled out a second time. The
# hand-written alternation stopped at `thirty`, so on the day the library reached
# its thirty-first pack this guard went quiet on exactly the sentence it exists
# for — and its own plant reported the validator going red for another reason,
# which is how the silence surfaced. Two lists of one vocabulary is one list that
# drifts, and the longest alternative has to come first or `twenty` shadows
# `twenty-one`.
COUNT_WITHOUT_ITS_NOUN = re.compile(
    r"\bthe\s+("
    + "|".join(NUMBER_WORDS[n] for n in sorted(NUMBER_WORDS, reverse=True) if n >= 2)
    + r")\b(?=\s*[,.;:)\]])", re.I)


def validate_a_count_names_its_noun():
    for rel in _counted_sources():
        text = read(ROOT / rel)
        if text is None:
            continue
        flat = " ".join(text.split())
        for m in COUNT_WITHOUT_ITS_NOUN.finditer(flat):
            check(
                False,
                f"{rel}: \"the {m.group(1)}\" names no noun, so nothing can check it. "
                f"`the twenty` sat in `tenor` at twenty-nine packs and no gate could see "
                f"it — write what is being counted. A SUBSET is written `N of the M "
                f"packs`, because a bare `N packs` is read as a claim about the total",
            )



# ------------------------------------- the theme split, derived not restated
#
# The split was published on 2026-08-20 as 11 twin / 13 single / 5 surface-variant
# and the tree said 10 / 13 / 6. TWO derivations of one number existed in the run
# that wrote it — a loose regex over the raw CSS, which counts a pack that merely
# mentions `dark` anywhere, and the strict one that generated the `Themes:`
# declarations — and the prose quoted the loose one. Both were mine and only one
# shipped into the pack skeleton.
#
# So the split is derived here from the declarations and compared with whatever a
# document says. One derivation, in one place, and the prose is held to it.
THEME_SPLIT_CLAIM = re.compile(
    r"(\d{1,2})\s+of them,\s+then\s+(\d{1,2}),\s+then\s+(\d{1,2})")


def validate_theme_split_is_derived():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    twin = single = surface = 0
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        m = re.search(r"(?m)^Themes:\s*(.+)$", read(md) or "")
        if not m:
            continue
        said = m.group(1)
        if "not a theme twin" in said:
            surface += 1
        elif "theme twin" in said:
            twin += 1
        else:
            single += 1
    truth = (twin, single, surface)
    looked = 0
    for rel in ("plugins/sheleg-design/skills/sheleg-design/styles/STYLE_PACK_TEMPLATE.md",
                "templates/style-pack-template.md"):
        text = read(ROOT / rel)
        if text is None:
            continue
        m = THEME_SPLIT_CLAIM.search(" ".join(text.split()))
        if not m:
            continue
        looked += 1
        said = tuple(int(g) for g in m.groups())
        check(
            said == truth,
            f"{rel}: states the theme split as {said[0]}/{said[1]}/{said[2]} and the "
            f"packs' own `Themes:` lines derive {truth[0]}/{truth[1]}/{truth[2]}. "
            f"A split restated in prose is a second derivation of one number, which "
            f"is how 11/13/5 shipped over a tree that says 10/13/6",
        )
    if not looked:
        _skips.append("no document states the theme split — nothing to hold to the tree")



# ------------------------------------- the table's marks against the contract
#
# A check already compares SKILL.md's PROSE count of core packs with the table's
# `**core contract**` marks. It fires only when somebody edits the prose — so
# widening `atrium` on 2026-08-20 and leaving its mark in the table went unseen
# until an unrelated edit to the sentence beside it. The table was the stale
# half and nothing read the table against the packs.
#
# This does: every pack the table marks `core contract` must declare
# `Contract: core`, and every pack that declares it must be marked. Two
# directions, because one alone is the hole this closes.
def validate_table_marks_match_the_contract():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    skill = read(ROOT / PLUGIN_DIR / "skills" / PLUGIN / "STYLE_PACK_INDEX.md")
    if skill is None or not styles.is_dir():
        return
    marked = set()
    for line in skill.split("\n"):
        if not line.startswith("| [`"):
            continue
        m = re.match(r"\| \[`([a-z0-9-]+)`\]", line)
        if m and "**core contract**" in line:
            marked.add(m.group(1))
    declared = set()
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        m = re.search(r"(?m)^Contract:\s*(\w+)", read(md) or "")
        if m and m.group(1).lower() == "core":
            declared.add(md.stem)
    for stem in sorted(marked - declared):
        check(False,
              f"SKILL.md: the table marks `{stem}` as **core contract** and "
              f"styles/{stem}.md declares `Contract: widened`. Widening a pack and "
              f"leaving its mark is how the table went stale for a release")
    for stem in sorted(declared - marked):
        check(False,
              f"SKILL.md: styles/{stem}.md declares `Contract: core` and the table "
              f"does not mark it, so a reader choosing off the table is not told "
              f"what the pack declines")
    if not marked and not declared:
        _skips.append("no pack declares a contract — the table marks were not checked")



# ------------------------------------- the motion ceiling has ONE home
#
# It had two, and they disagreed. Measured 2026-08-20 before the fix:
# `MOTION_DOCTRINE.md`'s standalone passage named ceilings for ten packs, four
# packs stated one in their own `## Register`, the overlap was two, `awning`
# stated a 4 the doctrine never mentioned, and six packs marked `(standalone)` in
# `SKILL.md` had a ceiling in neither place. A reader who chose off the table and
# stopped took a ceiling that might not exist.
#
# The Register is the home, because that is what a reader of one pack has. The
# doctrine's prose is a summary of it and is held to it here. Whitespace is
# flattened first: two of this run's own hand measurements misread a ceiling
# because `above\n**4**` wraps.
CEILING_IN_REGISTER = re.compile(r"above\s+\*{0,2}(\d)\*{0,2}")
CEILING_IS_NONE = re.compile(r"no hard ceiling|no pack ceiling is pinned", re.I)


def _register_of(md: Path) -> str:
    body = read(md) or ""
    if "## Register" not in body:
        return ""
    return " ".join(body.split("## Register", 1)[1].split("\n## ", 1)[0].split())


def validate_motion_ceiling_has_one_home():
    skill_dir = ROOT / PLUGIN_DIR / "skills" / PLUGIN
    styles = skill_dir / "styles"
    skill = read(skill_dir / "STYLE_PACK_INDEX.md")
    doctrine = read(skill_dir / "MOTION_DOCTRINE.md")
    if skill is None or doctrine is None or not styles.is_dir():
        return

    # 1. every pack SKILL.md marks `(standalone)` states a ceiling, or states it has none
    standalone = set(re.findall(r"^\| \[`([a-z0-9-]+)`\][^\n]*\(standalone\)", skill, re.M))
    if not check(len(standalone) >= 2,
                 "SKILL.md marks fewer than two packs `(standalone)` — the ceiling home "
                 "was not checked, and a check that could not look is not a pass"):
        return
    stated: dict[str, str] = {}
    for stem in sorted(standalone):
        md = styles / f"{stem}.md"
        if not md.is_file():
            continue
        reg = _register_of(md)
        # ORDER MATTERS. Reading the number first made a Register that says "no
        # ceiling is pinned" AND names one report the number and pass — the
        # contradiction the next block exists to catch, hidden by the block above
        # it. Watched: the plant for it went red for an unrelated reason.
        m = CEILING_IN_REGISTER.search(reg)
        if CEILING_IS_NONE.search(reg):
            stated[stem] = "none"
        elif m:
            stated[stem] = m.group(1)
        check(
            stem in stated,
            f"styles/{stem}.md: `SKILL.md` marks it `(standalone)` and its `## Register` "
            f"states no motion ceiling and does not say it has none. A reader who chooses "
            f"off the table and stops takes a ceiling that may not exist",
        )

    # 2. a pack does not state two different ceilings in one Register
    for stem, val in stated.items():
        reg = _register_of(styles / f"{stem}.md")
        found = set(CEILING_IN_REGISTER.findall(reg))
        if val != "none":
            check(len(found) <= 1,
                  f"styles/{stem}.md: its `## Register` states more than one ceiling "
                  f"({', '.join(sorted(found))}) — one home means one number")
        else:
            check(not found,
                  f"styles/{stem}.md: its `## Register` says no ceiling is pinned AND "
                  f"names {', '.join(sorted(found))} — the two cannot both be true")

    # 3. where the doctrine names a number for a pack, the Register agrees
    flat = " ".join(doctrine.split())
    if "A standalone pack pins its own ceiling" in flat:
        passage = flat.split("A standalone pack pins its own ceiling", 1)[1]
        passage = passage.split("Moved out of", 1)[0]
        # The doctrine writes a ceiling two ways -- "`pigeonhole` … above **4**" and
        # "`ora` at **4**, `tenor` at **4**" -- and reading only the first meant
        # four of the packs it names were never compared with their own Register.
        for m in re.finditer(
                r"`([a-z0-9-]+)`[^`]{0,180}?(?:above|at)\s+\*{0,2}(\d)\*{0,2}", passage):
            stem, num = m.group(1), m.group(2)
            if stem not in stated:
                continue
            check(
                stated[stem] == num,
                f"MOTION_DOCTRINE.md names {num} for `{stem}` and styles/{stem}.md's "
                f"`## Register` states {stated[stem]}. The Register is the home; the "
                f"doctrine's prose is a summary of it and has to agree",
            )



# ------------------------------------- a worked radius sum that does not work
#
# `field-notes` shipped "an inner radius is the outer radius minus the padding
# between them … `12 - 12 ~= 7.2`". Subtraction gives 0. The 7.2 came from the
# pack's proportional ramp, and the token layer used neither — the rule, its
# worked example and the implementation were three systems, and an agent applying
# the rule as written would have shipped square tags.
#
# Sixteen packs state radius arithmetic and every live example in them computes,
# so this ships with no live subject and a plant instead. That is deliberate: the
# defect it catches was found by hand once and cost a correction note.
#
# A sum inside a `*(Corrected …)*` note is a RECORD of the error, not a claim, and
# excluding it is what lets the record stay in the file it belongs to.
RADIUS_SUM = re.compile(r"(\d+(?:\.\d+)?)\s*[-−]\s*(\d+(?:\.\d+)?)\s*(?:=|≈|~=)\s*(\d+(?:\.\d+)?)")
RADIUS_CONTEXT = re.compile(r"radius arithmetic|inner radius|concentric", re.I)


def validate_worked_radius_sums_compute():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    if not styles.is_dir():
        return
    looked = 0
    for md in sorted(styles.glob("*.md")):
        text = read(md) or ""
        if not RADIUS_CONTEXT.search(text):
            continue
        looked += 1
        # paragraph by paragraph, so a sum is judged with the sentence around it
        for para in re.split(r"\n\s*\n", text):
            flat = " ".join(para.split())
            if not RADIUS_CONTEXT.search(flat):
                continue
            if "(Corrected" in flat or "*(Corrected" in flat:
                continue        # the record of a fixed error, not a live claim
            for a, b, c in RADIUS_SUM.findall(flat):
                got = float(a) - float(b)
                check(
                    abs(got - float(c)) <= 0.35,
                    f"styles/{md.name}: the worked sum {a} - {b} = {c} does not "
                    f"compute ({got:g}). A radius rule whose own example is wrong "
                    f"is three systems — the rule, the example and the token layer "
                    f"— and an agent applies the one it can read",
                )
    if looked < 2:
        _skips.append("fewer than two packs discuss radius arithmetic — the worked "
                      "sums were not checked")



# ------------------------------------- the Components contract, as a ratchet
#
# The skeleton lists six component classes and requires each entry to state rest,
# hover, active and disabled. Whether that list is a CONTRACT or a menu was open
# until 2026-08-20, and the library's own behaviour settled it: counted over the
# packs carrying the heading, buttons appear in all of them, cards in all but one,
# inputs and navigation in all but two, loaders and empty states in all but four.
# It is a contract that four packs do not meet — so calling it a menu would
# license the gaps rather than close them.
#
# It ships as a RATCHET rather than a hard failure, because each remaining gap
# needs its own reference read and inventing an answer is the one thing the pack
# layer forbids. `atrium`'s four were closed by reading `functionhealth.com`
# again, including a loader entry that says NONE with the measurement behind it —
# zero skeleton, shimmer or spinner rules in either stylesheet.
COMPONENT_CLASSES = {
    "buttons": r"\bbutton|\bcta\b",
    "cards": r"\bcard\b|\bcontainer\b|\bpanel\b|\btile\b",
    "inputs": r"\binput\b|\bform\b|\bfield\b|\bselect\b",
    "navigation": r"\bnav\b|navigation|\bheader\b|\bsidebar\b",
    "loaders": r"\bloader|\bloading|\bskeleton\b|\bspinner\b|shimmer",
    "empty states": r"empty state|\bempty\b",
}


def validate_component_classes_are_answered():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    if not styles.is_dir():
        return
    gaps: list[str] = []
    packs = 0
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        lines = (read(md) or "").split("\n")
        # the HEADING, never the string — a core pack names `## Components` in its
        # own contract line to decline it, and a substring search counted all six
        # such packs as carrying the section.
        at = [i for i, l in enumerate(lines) if l.rstrip() == "## Components"]
        if not at:
            continue
        packs += 1
        i = at[0]
        j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
        sec = "\n".join(lines[i:j])
        for name, pat in COMPONENT_CLASSES.items():
            if not re.search(pat, sec, re.I):
                gaps.append(f"{md.stem}/{name}")
    if packs < 2:
        _skips.append("fewer than two packs carry a '## Components' heading — the "
                      "component classes were not checked")
        return
    try:
        ceiling = json.loads(FLOORS.read_text(encoding="utf-8")).get(
            "components_unanswered_at_most")
    except (OSError, ValueError):
        ceiling = None
    if not check(ceiling is not None,
                 "test/floors.json has no `components_unanswered_at_most` — an "
                 "unanswered class that is not pinned is one that can multiply quietly"):
        return
    check(
        len(gaps) <= ceiling,
        f"{len(gaps)} component class(es) unanswered across {packs} packs, above the "
        f"pinned {ceiling}: {', '.join(sorted(gaps))}. Each is a pack that names "
        f"neither the component nor the reason it has none — and 'none, and why' is "
        f"a full answer. Lower the pin in the same commit as the fix",
    )
    print(f"  component classes: {len(gaps)} unanswered across {packs} packs "
          f"(pinned at most {ceiling})")



# ------------------------------------- counts the token layers can settle
#
# `validate_counted_claims` reads *"N packs"* and holds N against the tree. It cannot
# read *"the accent is `--accent` in twenty-nine of the thirty-six packs"*, because the
# noun being counted is not packs-in-the-library but packs-that-declare-a-token — a
# property only the token layers can answer, and one that moves with every pack added.
#
# Measured 2026-08-27, and both halves were wrong: the sentence said twenty-nine at a
# true thirty-three, and its list of the packs that name the accent something else gave
# two of the three, omitting `babylove` entirely. The count is the smaller half. The
# larger half is that an agent following that sentence would look for `--accent` in
# `babylove`, find nothing, and have no way to learn that the pack calls it `--brand` —
# which is the exact failure the `@role accent:` marker exists to prevent.
#
# So both figures are derived here rather than typed there. The prose keeps the number;
# this refuses it when the tree disagrees.
ACCENT_POPULATION = re.compile(
    r"`--accent` in ([a-z-]+) of the ([a-z-]+) packs", re.I)
NONTEXT_POPULATION = re.compile(
    r"because ([a-z-]+) of the token layers\s+carry such a colour", re.I)
ALT_ACCENT = re.compile(r"@role\s+accent\s*:\s*(--[a-z0-9-]+)")


def validate_token_population_counts():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    tokens = styles / "tokens"
    doc = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "SURFACE_COMPOSITION.md"
    text = read(doc)
    if text is None or not tokens.is_dir():
        return
    layers = sorted(tokens.glob("*.css"))
    if not check(len(layers) >= 2,
                 "styles/tokens/ holds fewer than two layers — the population counts "
                 "were not checked, and a check that could not look is not a pass"):
        return
    declares = re.compile(r"^\s*--accent\s*:", re.M)
    with_accent = [f.stem for f in layers if declares.search(read(f) or "")]
    without = [f.stem for f in layers if f.stem not in set(with_accent)]
    nontext = [f.stem for f in layers if ROLE_NON_TEXT_MARK.search(read(f) or "")]

    flat = " ".join(text.split())
    m = ACCENT_POPULATION.search(flat)
    if check(m is not None,
             "SURFACE_COMPOSITION.md: no '`--accent` in N of the M packs' sentence — "
             "the population claim this check settles has been reworded, so either "
             "restore the shape or retire the check with the reason"):
        said = WORD_NUMBERS.get(m.group(1).lower())
        check(
            said == len(with_accent),
            f"SURFACE_COMPOSITION.md says `--accent` is declared in {m.group(1)} of the "
            f"packs and {len(with_accent)} token layers declare it. The count moves with "
            f"every pack; derive it or do not state it",
        )
    # every pack that does NOT declare --accent must be named in that same paragraph,
    # because a reader who cannot find the token has nothing else to go on.
    for stem in without:
        check(
            f"`{stem}`" in flat,
            f"SURFACE_COMPOSITION.md: `{stem}` declares no `--accent` and the accent "
            f"paragraph does not name it — a reader following that sentence looks for a "
            f"token the pack does not have and learns nothing about what it calls it",
        )
        check(
            bool(ALT_ACCENT.search(read(tokens / f"{stem}.css") or "")),
            f"styles/tokens/{stem}.css: declares no `--accent` and carries no "
            f"'@role accent:' marker — the marker is the only thing that says which "
            f"token holds the role",
        )
    m = NONTEXT_POPULATION.search(flat)
    if check(m is not None,
             "SURFACE_COMPOSITION.md: no 'N of the token layers carry such a colour' "
             "sentence — the non-text population claim has been reworded"):
        said = WORD_NUMBERS.get(m.group(1).lower())
        check(
            said == len(nontext),
            f"SURFACE_COMPOSITION.md says {m.group(1)} token layers carry an "
            f"'@role non-text:' colour and {len(nontext)} do",
        )
    print(f"  token population: --accent in {len(with_accent)} of {len(layers)} layers "
          f"({', '.join(without) or 'none'} name it otherwise), "
          f"{len(nontext)} carry an @role non-text colour")

# ------------------------------------- a set excluded from the peer check
#
# `pigeonhole` carries nine `--cat-*-ink` tokens that are deliberately outside
# `validate_palette.py`'s semantic peer set. The exclusion is correct — measured
# with the gate's own metric, the closest pair is 4.92 ΔE at full colour and
# **1.24 under deuteranopia** against floors of 10 and 8, and no arrangement of
# nine hues clears those. What was wrong is that the exclusion held by ACCIDENT:
# `STATUS_TOKENS` matches by NAME, so an author who renamed a category token
# `--danger-ink` got a red gate for the right reason by luck, and one who added a
# tenth hue got nothing at all.
#
# So the set is declared, and the declaration is checked two ways: the prose
# enumeration equals the tokens that ship, and the pack states what carries the
# category instead of the hue. The second half is the load-bearing one — an
# exclusion with no stated carrier is just a gap with a paragraph in front of it.
ROLE_NON_TEXT_MARK = re.compile(r"@role\s+non-text\s*:", re.I)
CATEGORY_INK = re.compile(r"--cat-[a-z0-9-]+-ink")


def validate_excluded_sets_are_declared():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    tokens = styles / "tokens"
    if not tokens.is_dir():
        return
    looked = 0
    for css in sorted(tokens.glob("*.css")):
        body = read(css) or ""
        in_layer = {m.group(0) for m in CATEGORY_INK.finditer(body)
                    if re.search(rf"^\s*{re.escape(m.group(0))}\s*:", body, re.M)}
        if not in_layer:
            continue
        looked += 1
        md = styles / f"{css.stem}.md"
        prose = read(md) or ""
        in_prose = {m.group(0) for m in CATEGORY_INK.finditer(prose)}
        rel = f"styles/{md.name}"
        missing = sorted(in_layer - in_prose)
        extra = sorted(in_prose - in_layer)
        check(
            not missing,
            f"{rel}: the token layer ships {', '.join(missing)} and the pack never "
            f"names them. A hue added without a row is a category no reader knows "
            f"about and no gate can see — the peer check excludes this set by "
            f"declaration, so the declaration is the only place it is counted",
        )
        check(
            not extra,
            f"{rel}: it names {', '.join(extra)} and the token layer ships no such "
            f"token, so the enumeration describes a pack that does not exist",
        )
        # THE CARRIER, and it has to be stated in the SECTION that enumerates the
        # set. Searching the whole file let an unrelated chip rule three sections
        # away satisfy a declaration about the category hues — the plant for this
        # broke two of the phrase's three occurrences and the third kept the check
        # quiet. A declaration is where the reader of that set is standing.
        lines = prose.split("\n")
        first = next((i for i, l in enumerate(lines) if CATEGORY_INK.search(l)), None)
        section = ""
        if first is not None:
            start = max((i for i in range(first, -1, -1) if lines[i].startswith("## ")),
                        default=0)
            end = next((i for i in range(first + 1, len(lines))
                        if lines[i].startswith("## ")), len(lines))
            section = "\n".join(lines[start:end])
        check(
            re.search(r"carries the category is the word|the word, and it is required",
                      section, re.I) is not None,
            f"{rel}: it excludes {len(in_layer)} category hues from the semantic peer "
            f"check and the section that enumerates them never states what carries "
            f"the category instead. An exclusion with no stated carrier is a gap "
            f"with a paragraph in front of it",
        )
    if not looked:
        _skips.append("no pack ships a category-ink set — the exclusion declarations "
                      "were not checked")



# ------------------------------------- a fallback that is not one
#
# `--x: rgba(…)` followed by `--x: rgb(from var(--y) …)` READS as a guarded
# migration and is not one. A custom property accepts almost any token sequence,
# so the relative form PARSES everywhere: it wins the cascade, and the invalidity
# surfaces only where the property is substituted, as invalid-at-computed-value-
# time. By then the literal declaration is gone and every `var(--x)` resolves to
# `unset` — not to the line above it.
#
# Measured 2026-08-20: 23 custom properties across `ledger` and `showroom` shipped
# that pattern, and `showroom`'s was `--ring-focus`. Its own comment named the
# stake — *"an invisible focus indicator, which is the one degradation this
# library may not ship"* — and then relied on the mechanism that cannot deliver
# it. Both are inside `@supports (color: rgb(from red r g b))` now, which is where
# a literal fallback actually survives.
RELATIVE_CUSTOM_PROP = re.compile(r"^\s*(--[a-z0-9-]+)\s*:.*\brgb\(\s*from\s")


# ------------------------------------- the bands reach the token layer's own comments
#
# `validate_motion_bands` reads a pack's `## Components`, `## Micro-interactions`
# and `## Motion flavor` prose, because that is where a pack prescribes an
# interaction. It never read the token layer, and board B-049 named the hole with
# its instance: `bulletin`'s `--dur-panel: 0.4s; /* the nav dropdown */`, 150 ms
# past the doctrine's dropdown band, invisible to every check in the repository.
#
# What the sweep reads is a DECLARATION whose token name or trailing comment names
# an element §3 bands. All 30 durations mentioned *inside* comment prose were also
# extracted and deliberately left alone: every one of them describes the reference
# ("the reference declares --t-normal: 250ms"), quotes the doctrine's own band, or
# explains a reduced-motion collapse. A check reading those is a check that flags
# a pack for correctly reporting what it measured.
#
# Adjudicating the nine live subjects turned up something the row had not: the same
# token was called a *dropdown* in the CSS and a *nav sheet* in the pack's prose,
# and §3 bands the two differently — one word made 0.4s a violation and the other
# made it correct. The value did not move; the naming did, with the reason at the
# declaration. A pack whose two files disagree about what a token drives cannot be
# checked by any band gate, which is why this one reports the pairing it used.
# Plurals are matched, and the reason is measured: `awning`'s
# `--dur-control: 200ms /* DERIVED — dropdowns and selects */` escaped the first
# version of this table entirely, because `\bdropdown\b` does not match
# "dropdowns". That value is legal, so nothing was hidden — but the sweep silently
# judged eight subjects where nine exist, and the ninth would have been the one to
# hide an illegal value written in the plural.
BANDED_ELEMENTS = (
    ("button press", 100, 160, r"\bpress(?:es)?\b|\bactive states?\b"),
    ("tooltip or popover", 125, 200, r"\btooltips?\b|\bpopovers?\b"),
    ("dropdown or select", 150, 250,
     r"\bdropdowns?\b|\bselects?\b|\bcomboboxe?s?\b"),
    ("modal, drawer or sheet", 200, 500,
     r"\bmodals?\b|\bdrawers?\b|\bsheets?\b|\bdialogs?\b|\bpanels?\b"
     r"|\boverlays?\b"),
)
BANDED_DECL = re.compile(
    r"^[ \t]*(--[a-z0-9-]+)\s*:\s*([0-9.]+)(ms|s)\s*;([^\n]*)$", re.M)


def validate_token_comments_respect_the_bands():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    tokens = styles / "tokens"
    doctrine = read(styles.parent / "MOTION_DOCTRINE.md")
    if not tokens.is_dir() or doctrine is None:
        return
    # The bands must still be in the doctrine. Without this the sweep keeps
    # printing a count after §3 is rewritten, measuring nothing against nothing.
    for label, lo, hi, _ in BANDED_ELEMENTS:
        if not check(f"{lo}–{hi} ms" in doctrine or f"{lo}-{hi} ms" in doctrine,
                     f"MOTION_DOCTRINE.md no longer states a {lo}–{hi} ms band, and this "
                     f"sweep measures the {label} against it"):
            return
    judged = 0
    for f in sorted(tokens.glob("*.css")):
        css = read(f)
        if css is None:
            continue
        for m in BANDED_DECL.finditer(css):
            tok, num, unit, trailing = m.group(1), float(m.group(2)), m.group(3), m.group(4)
            ms = num * 1000 if unit == "s" else num
            if ms == 0:
                continue          # a reduced-motion collapse is not a band subject
            # The comment wins over the name: it says what the token drives. Where
            # both match, the first band in doctrine order is used, and the pairing
            # is reported so a wrong pairing is arguable rather than invisible.
            for label, lo, hi, pat in BANDED_ELEMENTS:
                if not (re.search(pat, trailing, re.I) or re.search(pat, tok, re.I)):
                    continue
                judged += 1
                line = css[:m.start()].count("\n") + 1
                check(
                    lo <= ms <= hi,
                    f"styles/tokens/{f.name}:{line}: `{tok}` is {ms:g} ms and its own "
                    f"comment or name calls it a {label}, which MOTION_DOCTRINE.md §3 "
                    f"bands at {lo}–{hi} ms. Either the value is wrong or the element "
                    f"is named wrong — and the second is the one that ships silently",
                )
                break
    if judged < 2:
        _skips.append("fewer than two token declarations name a banded element — the "
                      "token-layer band sweep did not run")
        return
    print(f"  token-layer bands: {judged} declaration(s) name a banded element, "
          f"all inside their band")


# ------------------------------------- a ratio measured against a surface it never meets
#
# A palette table declares its base in the header — "On `--bg`" — and every row is
# read against it. `scoreboard`'s ring table carried a row whose own text confined
# the token to `--surface-sand`, and reported it at 15.88:1, which is its ratio
# against `--bg`. The number was right and described a pairing that never renders;
# on sand the same token measures 14.60. The second ring exists *because* the first
# misses the floor on sand, so `--bg` was the one surface it could not be about.
#
# The broad form of this check was measured and rejected: 58 rows across 24 packs
# name a surface token other than their header's base, and nearly all of them are
# the ordinary case — the row's SUBJECT is a surface token, correctly measured on
# the declared base. Only a row that CONFINES its token to another surface is
# making the mistake, and after the scoreboard fix there are **zero** of those.
# It ships anyway, as a regression guard with a plant: the shape cost a wrong
# number in a shipped pack once, and a table gains rows every release.
TABLE_BASE = re.compile(
    r"^\s*\|[^|\n]*\|.*?[Oo]n\s+`(--[a-z0-9-]+)`[^|\n]*\|\s*$", re.M)
CONFINED_TO = re.compile(
    r"`(--[a-z0-9-]+)`\s+only|only\s+on\s+`(--[a-z0-9-]+)`|on\s+`(--[a-z0-9-]+)`\s+only",
    re.I)


def validate_confined_tokens_measured_where_used():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    if not styles.is_dir():
        return
    tables = 0
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        lines = (read(md) or "").split("\n")
        for i, line in enumerate(lines):
            m = TABLE_BASE.match(line)
            if not m:
                continue
            tables += 1
            base = m.group(1)
            for j in range(i + 2, len(lines)):
                row = lines[j]
                if not row.strip().startswith("|"):
                    break
                for cm in CONFINED_TO.finditer(row):
                    tok = next(g for g in cm.groups() if g)
                    check(
                        tok == base,
                        f"styles/{md.stem}.md:{j + 1}: the table's header measures every "
                        f"row against `{base}` and this row confines its token to "
                        f"`{tok}`. The ratio in it describes a pairing that never "
                        f"renders — give the row its own `Measured on` cell, as "
                        f"`scoreboard`'s ring table now does",
                    )
    if tables < 2:
        _skips.append("fewer than two base-declaring palette tables found — the "
                      "confinement check did not run")
        return
    print(f"  confined tokens: {tables} base-declaring table(s), 0 row measured "
          f"against a surface it is confined away from")


# ------------------------------------- a description edit must not drop a carrier
#
# `T1` in `test/scenarios.md` gives an agent five skill descriptions and fourteen
# tasks, and passes only at 0 misses and 0 false loads. Its own record says what
# this check is for: the 1.12.0 run scored 13/14 because *"scrubbed sections"* had
# been dropped to make room for a mobile trigger, and that phrase was the only
# thing in the description carrying **section by section**. It was restored, the
# set re-ran green, and the harness header gained the rule that a description edit
# obliges the full trigger set.
#
# **It happened again, by the same mechanism, and nothing noticed for seven
# releases.** `v1.37.5` (`de09f9e`, "an unqualified landing page reaches both
# crafts") removed `scrubbed sections` while the description GREW 1009 -> 1021, so
# the edit read as additive. T1 has not been re-run since 2026-08-11, so the
# regression sat in every release from v1.37.5 to v1.45.0. Found 2026-08-20 by
# walking the phrase across every tag rather than by reading the diff.
#
# What this check can and cannot do. It proves a phrase a T1 task depends on is
# still IN the description — which is the failure mode that has now occurred twice.
# It cannot prove the runtime routes that phrasing here rather than to `super-ux`
# or `copywriting`; that is a fresh-context measurement and no string test
# substitutes for it (board B-052).
#
# Each pair is (the T1 task, the phrase that carries it). A pair is added when a
# task is added to T1, and the list is enumerated rather than derived because the
# mapping from a task to its carrier is a judgement the run makes, not a pattern.
T1_CARRIERS = (
    ("particle-hero landing", "particle"),
    ("WebGL hero upgrade", "WebGL"),
    ("scroll-narrative storyboard", "scrubbed"),
    ("landing janky / layers out of sync", "drift"),
    ("Russian cinematic particle landing", "лендинг"),
    ("quiet-light dashboard styling", "dashboard"),
    ("admin design tokens light/dark", "admin"),
    ("admin design tokens light/dark", "light/dark"),
    ("Russian calm light UI for an internal tool", "internal tool"),
    ("iOS onboarding screens", "mobile screen"),
    ("Russian mobile payment screen", "мобильный экран"),
    ("investor deck (added by B-006)", "deck"),
)


def validate_t1_carriers_survive():
    skill = read(ROOT / PLUGIN_DIR / "skills" / PLUGIN / "SKILL.md")
    scenarios = read(ROOT / "test" / "scenarios.md")
    if skill is None:
        return
    m = re.search(r"^description:\s*(.*?)^[a-z_]+:", skill, re.M | re.S)
    if not check(m is not None,
                 "SKILL.md front matter has no readable `description:` — the T1 carrier "
                 "check could not look, and that is not a pass"):
        return
    description = " ".join(m.group(1).split())
    # The scenario file must still hold T1. Without this the carriers are measured
    # against a set that no longer exists.
    if scenarios is not None:
        check("## T1 " in scenarios or "## T1 —" in scenarios,
              "test/scenarios.md no longer holds a `## T1` section, and this check "
              "exists to protect its tasks")
    missing = [(task, phrase) for task, phrase in T1_CARRIERS
               if phrase.lower() not in description.lower()]
    check(
        not missing,
        "the description no longer carries "
        + "; ".join(f"`{p}` (the phrase T1's \"{t}\" task depends on)"
                    for t, p in missing)
        + ". A description edit that reads as additive can still remove the only "
          "phrase carrying a task — that is how `scrubbed sections` was lost twice, "
          "and the second time it shipped in seven releases",
    )
    print(f"  T1 carriers: {len(T1_CARRIERS)} phrase(s) present, description "
          f"{len(description)}/1024 chars")


# ------------------------------------- a stamp count nobody recounts
#
# The Run stamps preamble reports how many rows carry no `Diverged?` answer, and
# the number matters: the third retirement trigger reads a stamp COUNT, so a table
# of reconstructed rows retires instructions on absences of evidence. The paragraph
# said "twenty-six" while the table held thirty-four, which is the same class of
# defect as every restated number this gate refuses elsewhere — in the one document
# whose subject is what a run may conclude.
#
# Both checks below are named in `retro.md` itself, which is why they exist: this
# family refuses a document that cites a command it does not have.
# `[ \t]*$`, never `\s*$`. With `\s*$` under re.M the trailing whitespace class eats
# the newline, each match consumes into the next line, and `finditer` returns every
# OTHER row: 29 of 57 here, with the check printing a confident number over half a
# table. Matched per line for the same reason.
STAMP_ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|.*\|[ \t]*(.+?)[ \t]*\|[ \t]*$")
WRITTEN_NUMBERS = {
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "twenty-six": 26, "thirty": 30, "thirty-one": 31, "thirty-two": 32,
    "thirty-three": 33, "thirty-four": 34, "thirty-five": 35, "thirty-six": 36,
    "forty": 40,
}
RETIREMENT_WINDOW = 5


def _stamp_rows():
    retro = read(ROOT / "docs" / "evidence" / "retro.md")
    if retro is None or "## Run stamps" not in retro:
        return None, None
    section = retro.split("## Run stamps", 1)[1]
    rows = []
    for line in section.split("\n"):
        m = STAMP_ROW.match(line)
        if m:
            rows.append((m.group(1), m.group(2)))
    return retro, rows


def validate_reconstructed_stamp_count():
    retro, rows = _stamp_rows()
    if rows is None:
        _skips.append("docs/evidence/retro.md has no '## Run stamps' section — the "
                      "stamp count was not checked")
        return
    if not check(len(rows) >= 10,
                 f"docs/evidence/retro.md: only {len(rows)} run stamp row(s) parsed — "
                 f"the count check could not look, and that is not a pass"):
        return
    unrecorded = sum(1 for _, verdict in rows if "unrecorded" in verdict)
    preamble = retro.split("## Run stamps", 1)[1].split("| Date |", 1)[0]
    # Anchored on the reporting sentence, not on a loose substring. `"five rows"`
    # matched the preamble's OWN aside -- "a list that is short by five rows
    # retires whatever it likes" -- so the check read 5 against a table of 34 and
    # failed for the wrong reason.
    stated = None
    m = re.search(r"\*\*([A-Za-z-]+|\d+)\s+rows below are marked", preamble)
    if m:
        token = m.group(1)
        stated = int(token) if token.isdigit() else WRITTEN_NUMBERS.get(token.lower())
    if not check(stated is not None,
                 "docs/evidence/retro.md: the Run stamps preamble no longer opens with "
                 "'**N rows below are marked**', so the count it reports cannot be "
                 "compared with the table. Restore the sentence or this check is blind"):
        return
    check(
        stated == unrecorded,
        f"docs/evidence/retro.md: the Run stamps preamble reports {stated} rows with no "
        f"`Diverged?` answer and the table holds {unrecorded}. The third retirement "
        f"trigger reads a stamp count, so this number decides what may be retired on "
        f"absences of evidence — it is recomputed here rather than carried",
    )
    print(f"  run stamps: {len(rows)} rows, {unrecorded} unrecorded (preamble says "
          f"{stated})")


def validate_retirement_window():
    _, rows = _stamp_rows()
    if not rows:
        return
    if len(rows) < RETIREMENT_WINDOW:
        _skips.append(f"fewer than {RETIREMENT_WINDOW} run stamps — the retirement "
                      f"window was not evaluated")
        return
    window = rows[-RETIREMENT_WINDOW:]
    blind = [d for d, verdict in window if "unrecorded" in verdict]
    # NOT a failure. A closed window is a legitimate state -- it was closed for
    # eighteen releases -- and failing the gate on it would make the honest answer
    # (`unrecorded`) more expensive than a guess. What must never happen is an
    # instruction retired while it is closed, and that is a decision a run makes,
    # so this reports the state the run has to read.
    state = "OPEN" if not blind else f"CLOSED ({len(blind)} of {RETIREMENT_WINDOW} unrecorded)"
    print(f"  retirement window: {state} — the 'has not fired in five run stamps' "
          f"trigger is {'available' if not blind else 'UNAVAILABLE'}")
    if blind:
        print(f"    blind stamps: {', '.join(blind)}")


# ------------------------------------- a plant must name the check it exercises
#
# The self-test's fourth tuple element is the string the output must contain, and
# it is the only thing separating "the gate went red" from "the check I wrote went
# red". Without it a plant is caught by whatever fires first — and in this
# repository that is usually the `.cursor` mirror-drift check or the kit-drift
# check, because both trip on any edit to a pack.
#
# Made mandatory on 2026-08-20, after the thirteen plants that had no `expect`
# were run one at a time and their real failures read. **One of the thirteen was
# proving nothing at all**: the container plant replaced a bullet's LABEL while
# `scoreboard` answers the container question twice in the same section, so the
# check stayed correctly green and the mirror check supplied the red. It had
# reported `caught` on every run since it was written. Four more of the thirteen
# produced a mirror failure ahead of their own, which is the same defect one
# reordering away.
def validate_every_plant_names_its_check():
    import ast as _ast
    src = ROOT / "test" / "validate.py"
    text = read(src)
    if text is None:
        _skips.append("test/validate.py is unreadable here — the plant-shape check "
                      "did not run")
        return
    try:
        tree = _ast.parse(text)
    except SyntaxError as exc:
        check(False, f"test/validate.py could not be parsed ({exc})")
        return
    plants = None
    for node in tree.body:
        if isinstance(node, _ast.Assign) and any(
                getattr(t, "id", "") == "PLANTS" for t in node.targets):
            plants = node.value
    if not check(isinstance(plants, _ast.Tuple) and len(plants.elts) >= 2,
                 "test/validate.py: PLANTS is not a tuple of at least two entries — "
                 "the plant-shape check could not look, and that is not a pass"):
        return
    bare = []
    for el in plants.elts:
        if not isinstance(el, _ast.Tuple):
            continue
        label = el.elts[0].value if isinstance(el.elts[0], _ast.Constant) else "?"
        if len(el.elts) < 4:
            bare.append(str(label))
    check(
        not bare,
        f"{len(bare)} plant(s) carry no `expect` string: {'; '.join(bare)}. A plant "
        f"without one is reported `caught` by whichever check fires first — in this "
        f"tree usually the mirror-drift or kit-drift check, both of which trip on any "
        f"edit to a pack — so it proves that check works and says nothing about the "
        f"one it was written for",
    )
    print(f"  plant shape: {len(plants.elts)} plant(s), every one names the check "
          f"it exercises")


# ------------------------------------- two constants, one name, and no error
#
# Python raises nothing when a module-level name is assigned twice: the later
# binding wins and every function written against the earlier one silently uses
# the wrong value. In a 3990-line gate that is not hypothetical — it happened
# while B-045 was being closed. A new `DUR_DECL` was added near line 3120 and an
# existing one at 3716 overwrote it, so the new check parsed durations with a
# regex whose groups mean something else and reported `0 kept` against a tree
# where six were measured by hand. It printed a number and passed.
#
# The check walks the gate's own files with `ast`, which is why it cannot be
# fooled by a name inside a function or a conditional re-binding: only top-level
# assignments and definitions count, and those are exactly the ones that shadow.
def validate_gate_has_no_shadowed_names():
    import ast as _ast
    from collections import Counter as _Counter
    # ROOT, not `Path(__file__).parent`: the self-test runs this module from its
    # real location against a COPIED tree, so reading its own directory reads the
    # one place a plant cannot land. The plant for this check stayed green until
    # the path came from the tree under test.
    here = ROOT / "test"
    files = sorted(here.glob("*.py")) if here.is_dir() else []
    if not check(len(files) >= 2,
                 "fewer than two gate modules found — the shadowed-name check could "
                 "not look, and a check that could not look is not a pass"):
        return
    for f in files:
        try:
            tree = _ast.parse(f.read_text(encoding="utf-8"))
        except (OSError, SyntaxError) as exc:
            check(False, f"test/{f.name}: could not be parsed ({exc})")
            continue
        seen: _Counter = _Counter()
        for node in tree.body:
            if isinstance(node, _ast.Assign):
                for t in node.targets:
                    if isinstance(t, _ast.Name):
                        seen[t.id] += 1
            elif isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef,
                                   _ast.ClassDef)):
                seen[node.name] += 1
        dupes = sorted(n for n, c in seen.items() if c > 1)
        check(
            not dupes,
            f"test/{f.name}: {len(dupes)} top-level name(s) assigned more than once "
            f"({', '.join(dupes)}). The later binding wins with no error, so every "
            f"check written against the earlier one runs on a value it did not mean "
            f"— and reports a number rather than failing",
        )
    print(f"  gate hygiene: {len(files)} module(s), no shadowed top-level name")


# ------------------------------------- the strict half of the reduced-motion gate
#
# `validate_reduced_motion` above is a floor: a layer must HAVE a branch and the
# branch must collapse SOMETHING. A layer collapsing one of nine durations passes
# it, which is board B-045. The strict form asks the question that matters —
# **every** declared duration is accounted for under reduce — and it has to allow
# the exceptions, because two of them are real and reasoned:
#
#   * `roster` keeps `--dur-float-a/b` at 5.5s/6.5s: they drive INFINITE
#     animations, a duration cannot stop one, and 0.01ms strobes at exactly the
#     reader the query protects. The kit pauses them with `animation-play-state`,
#     which no custom property can express.
#   * `atrium` keeps its four `--flute-dur-*`: under reduce the canvas is REMOVED
#     and the still underneath is the hero. A duration nothing spends is not a
#     defect, and collapsing it would state the opposite of what happens.
#
# So the rule is: a duration declared outside the branch must APPEAR inside it.
# Collapsed to an instant, or re-declared at its own value with a reason — the
# form `roster` and now `atrium` use. Silence is what is refused, because silence
# and a decision look identical to every reader and every gate.
#
# 0.01ms is a collapse, not an exception: it is the standard idiom for "instant
# but still fires `animationend`", and eight of the eleven re-declarations in the
# library are exactly that.
#
# The third part is the one the row asked for by name. Where the reason promises a
# stop in the COMPONENT layer, that stop is checked in the kit. `pigeonhole`'s
# `--dur-marquee` says the marquee is paused with `animation-play-state` and points
# at `.pg-marquee`; the rule is really there (kits/pigeonhole/src/styles.css:859)
# and the check now proves it rather than trusting the sentence.
# Matched by VALUE, not by name. The first version keyed on a name containing
# `dur|duration|speed|time`, and the product tier of this node's certification
# planted the proof: it removed `--t-hero-art: 0s;` from `paperclip`'s reduce branch
# in all three copies, left `--t-hero-art: 1.1s` in `:root`, and the gate still
# printed `0 silent duration(s)` and exited 0. Thirteen time-valued tokens across
# ten layers were outside the walk — `paperclip`'s six `--t-*`, seven `--stagger*`,
# `--marquee-cycle`, `--scan-period` — every one of them answered today by the
# authors' habit rather than by this check, which is a guard complete by accident.
# `docs/evidence/verification.md` already recorded the lesson for the floor check
# above: a name-keyed walk reads paperclip's branch as empty.
REDUCE_DUR_DECL = re.compile(
    r"^[ \t]*(--[a-z0-9-]+)\s*:\s*(\d+(?:\.\d+)?\s*m?s)\s*;(.*)$",
    re.M | re.I)
TIME_VALUE = re.compile(r"^([\d.]+)\s*(ms|s)$", re.I)
# A reason marker on the declaration itself or in the comment block above it.
KEPT_MARKER = re.compile(r"KEPT|ON PURPOSE|insufficient on its own|deliberate", re.I)
# A promise the token layer cannot keep by itself.
COMPONENT_STOP = re.compile(r"animation-play-state", re.I)


def _seconds(value: str):
    m = TIME_VALUE.match(value.strip())
    if not m:
        return None
    n = float(m.group(1))
    return n / 1000.0 if m.group(2).lower() == "ms" else n


def validate_every_duration_answers_reduce():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    tokens = styles / "tokens"
    if not tokens.is_dir():
        return
    layers = silent = kept = promised = examined = 0
    for name in _packs():
        css = read(tokens / f"{name}.css")
        if css is None:
            continue
        bodies = _reduce_blocks(css)
        if not bodies:
            continue          # the floor above owns the no-branch case
        layers += 1
        inside = "\n".join(bodies)
        # Classify by POSITION, and keep the root declarations in a list. Building a
        # dict over the whole file instead let the branch's own re-declaration
        # overwrite the root one, so every kept token vanished from its own check:
        # the first run of this function printed `0 kept` against a tree where six
        # were measured by hand. A checker that reports zero is indistinguishable
        # from one that passes.
        spans = [(css.index(b), css.index(b) + len(b)) for b in bodies]
        in_span = lambda q: any(a <= q < z for a, z in spans)
        declared = [(m.group(1), m.group(2).strip())
                    for m in REDUCE_DUR_DECL.finditer(css) if not in_span(m.start())]
        in_branch = {m.group(1): (m.group(2).strip(), m.group(3), m.start())
                     for m in REDUCE_DUR_DECL.finditer(inside)}
        for tok, val in sorted(declared):
            # EXACTLY ONE check per duration, whatever its answer. The first version
            # asserted only on the exceptions and fell through on a collapse, so the
            # count this gate contributes was a function of how many exceptions the
            # library holds rather than how many durations it declares. Collapsing
            # atrium's four kept durations -- the remediation the requirement names
            # FIRST -- dropped validate.py by 4 against a ratchet floor and turned
            # `npm test` red on the stricter answer, and the only way through was
            # lowering a floor whose own `_why` says a falling count is how a deleted
            # requirement hides. The second version added a universal check and left
            # the asymmetry: a kept duration still cost two and a collapsed one, one.
            # Measured both times rather than reasoned -- the seam tier of this node's
            # certification instrumented `check()` and collapsed the four in a copy.
            examined += 1
            if tok not in in_branch:
                silent += 1
                check(False,
                      f"styles/tokens/{name}.css: `{tok}: {val}` is declared and the "
                      f"reduced-motion branch says nothing about it. Collapse it, or "
                      f"re-declare it there with the reason — a duration a branch never "
                      f"names reads the same whether the omission was a decision or an "
                      f"oversight, and this repository has shipped both")
                continue
            rval, trailing, rpos = in_branch[tok]
            secs = _seconds(rval)
            if secs is not None and secs <= INSTANT_SECONDS:
                # Collapsed, including the 0.01ms idiom -- and NOT the end of the
                # question. B-045's sharpest case is a duration that collapses and
                # still needs a component-layer stop: `pigeonhole`'s `--dur-marquee`
                # goes to 0.01ms, which strobes an infinite animation at exactly the
                # reader this query protects, so the kit pauses it instead. The first
                # version of this function returned here, and its plant stayed green
                # -- reproducing the defect the board row exists for, one layer up.
                # The promise is checked once per LAYER, below.
                check(True, "")           # the answered case, counted like every other
                continue
            kept += 1
            # The reason may sit on the line or in the comment block above it.
            above = inside[max(0, rpos - 700):rpos]
            check(
                bool(KEPT_MARKER.search(trailing) or KEPT_MARKER.search(above)),
                f"styles/tokens/{name}.css: the reduced-motion branch re-declares "
                f"`{tok}` at `{rval}` — above an instant — and names no reason. A "
                f"value that does not collapse is either a decision or a bug, and "
                f"only the file can say which")

        # The promise is a property of the LAYER, not of one token's verdict: it is
        # made in the branch's prose and it is kept in the kit. Checked once per
        # layer, after the token walk, so a collapsed duration that still needs the
        # stop is covered -- which is the case the row was written about.
        if COMPONENT_STOP.search(inside):
            promised += 1
            kit_css = read(ROOT / "kits" / name / "src" / "styles.css")
            # Comments stripped first. The token layer's own explanation of this
            # promise is copied verbatim into the kit and contains the word
            # `animation-play-state`, so searching the raw text found the sentence
            # describing the rule instead of the rule. The plant stayed green until
            # the strip was added.
            kit_code = CSS_COMMENT.sub(" ", kit_css or "")
            check(
                kit_css is not None and bool(COMPONENT_STOP.search(
                    "\n".join(_reduce_blocks(kit_code)))),
                f"styles/tokens/{name}.css: its reduced-motion branch promises that the "
                f"component layer stops an animation with `animation-play-state`, and "
                f"kits/{name}/src/styles.css has no such rule inside a reduced-motion "
                f"branch. The promise is the whole exception; unkept, the animation runs "
                f"at full speed at exactly the reader the query protects",
            )
    if layers < 2:
        _skips.append("fewer than two layers ship a reduced-motion branch — the strict "
                      "duration check did not run")
        return
    print(f"  reduce coverage: {layers} layers, {examined} duration(s) examined, "
          f"{silent} silent, {kept} kept with a reason, {promised} promise a "
          f"component-layer stop")


# ------------------------------------- a prescribed token that resolves to nothing
#
# A pack's prose tells an implementer which token to spend. Where the layer never
# defines it, `var(--dur-press)` is an undefined custom property: invalid at
# computed-value time, inherited or falling back to nothing, and silent everywhere.
# That is board B-038's class -- `var(--danger)` shipped undefined for four
# releases -- and the commit closing B-042 introduced a fresh one in the same file
# whose own comment describes the trap.
#
# The naive form of this check is unusable and was measured before it was written:
# 19 of 29 packs quote a token their layer does not define, and almost all of it is
# the pack quoting its REFERENCE's vocabulary (`datasheet`'s `--gray-6`, `ora`'s
# `--font-lora`) rather than promising anything. What separates a promise from a
# quotation is the PREFIX FAMILY: a pack that names `--dur-press` while defining
# four other `--dur-*` is speaking its own vocabulary. That cut 60 candidates to 11.
#
# The `--font-` family is excluded on principle rather than convenience: a pack
# layer deliberately does not own font loading (`validate_font_loading_stays_out`),
# so a `--font-*` name in prose is naming somebody else's variable by design. Eight
# of the remaining nine false positives were exactly that.
FAMILY = re.compile(r"^--([a-z]+)-")
QUOTED_TOKEN = re.compile(r"`(--[a-z0-9-]+)`")
DEFINED_TOKEN = re.compile(r"^\s*(--[a-z0-9-]+)\s*:", re.M)
# A pack layer does not own font loading, so a `--font-*` in prose names an
# outside variable by design.
UNOWNED_FAMILIES = {"font"}
# The one case the family test cannot tell apart, declared rather than silently
# widened. `ora` attributes BOTH halves of the pair to the reference in the same
# sentence -- "the reference names the pair `--accent-signature` /
# `--accent-signature-foreground`" -- and adopts only the half it needs, because
# its primary action is `bg-foreground text-background` and there is no second
# colour to define. Read 2026-08-20 at ora.md:126-134.
PRESCRIBED_EXEMPT = {("ora", "--accent-signature")}


def _outside_media(css: str) -> str:
    """The token layer with every `@media` block removed, braces counted.

    A declaration inside `@media (prefers-reduced-motion: reduce)` is not a
    definition for anybody not asking for reduced motion, so counting it as one
    makes this check blind to the defect it exists for. Found by the plant below:
    dropping `--dur-press` from `:root` left the reduce block's copy standing and
    the check reported the token defined. Zero tokens are in that position today
    (measured 2026-08-20 across 29 layers) -- which is why it had to be closed
    now rather than after the first one arrives.
    """
    out, i = [], 0
    while i < len(css):
        if css.startswith("@media", i):
            j = css.find("{", i)
            if j < 0:
                break
            depth, j = 1, j + 1
            while depth and j < len(css):
                depth += (css[j] == "{") - (css[j] == "}")
                j += 1
            i = j
            continue
        out.append(css[i])
        i += 1
    return "".join(out)


def validate_prescribed_tokens_resolve():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    if not styles.is_dir():
        return
    packs, dangling = 0, []
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        css = styles / "tokens" / f"{md.stem}.css"
        prose, layer = read(md), read(css)
        if prose is None or layer is None:
            continue
        packs += 1
        defined = set(DEFINED_TOKEN.findall(_outside_media(layer)))
        families: dict[str, set[str]] = {}
        for d in defined:
            m = FAMILY.match(d)
            if m:
                families.setdefault(m.group(1), set()).add(d)
        for tok in sorted(set(QUOTED_TOKEN.findall(prose)) - defined):
            m = FAMILY.match(tok)
            if not m or m.group(1) in UNOWNED_FAMILIES:
                continue
            if (md.stem, tok) in PRESCRIBED_EXEMPT:
                continue
            # Two siblings, not one: a family of one is as likely to be the
            # reference's word as the pack's.
            if len(families.get(m.group(1), ())) >= 2:
                dangling.append(f"{md.stem}.md names `{tok}` "
                                f"({len(families[m.group(1)])} `--{m.group(1)}-*` defined)")
    if packs < 2:
        _skips.append("fewer than two packs have both a prose file and a token layer "
                      "— prescribed tokens were not checked")
        return
    check(
        not dangling,
        "a pack prescribes a token its own layer never defines, in a family the layer "
        "does own — so `var()` on it resolves to nothing, silently: "
        + "; ".join(dangling)
        + ". Define it, or write the prose so it does not read as a token an "
          "implementer can spend",
    )
    print(f"  prescribed tokens: {packs} packs, {len(dangling)} dangling "
          f"({len(PRESCRIBED_EXEMPT)} declared exemption)")


# ------------------------------------- one curve and a scrub cannot both be total
#
# A pack that says "the one site-wide curve" and then mandates scrubbed motion has
# written two rules that contradict each other, and `MOTION_DOCTRINE.md` §6 settles
# it: under `scrub`, easing must be `none` — the scrollbar is already the clock.
# Easing a scrubbed timeline eases against the scroll position twice, which the
# doctrine names as the family's most common motion bug.
#
# Found on `instrument-console` (board B-042), which named one pack. Measuring the
# shape across the library found FIVE, so this ships as a ratchet: each pack's
# exception has to be carved in its own words, against its own motion section, and
# a pin that only falls is the honest way to say four are still open.
ONE_CURVE = re.compile(r"the one site-wide curve|one curve|single (?:ease|curve)", re.I)
MANDATES_SCRUB = re.compile(r"scrubbed\b", re.I)
# The carve, written any of the three ways the packs write it.
SCRUB_CARVED = re.compile(
    r"ease[^.\n]{0,40}`?none`?|`none`[^.\n]{0,60}scrub|scrub[^.\n]{0,80}`none`", re.I)
# A pack that BANS scrubbing has no contradiction to carve.
BANS_SCRUB = re.compile(
    r"bans? [^.\n]{0,60}scrub|no scrubbing|forbids? [^.\n]{0,40}scrub", re.I)


def validate_scrub_carves_its_exception():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    doctrine = read(ROOT / PLUGIN_DIR / "skills" / PLUGIN / "MOTION_DOCTRINE.md")
    if not styles.is_dir() or doctrine is None:
        return
    # The doctrine must actually carry the rule this check enforces. Without this
    # the check would keep passing after the rule was deleted -- measuring packs
    # against a doctrine that no longer says anything.
    if not check("easing must be `none`" in doctrine,
                 "MOTION_DOCTRINE.md no longer states that easing must be `none` under "
                 "`scrub` — the rule this check enforces has to live somewhere first"):
        return

    subjects, uncarved = 0, []
    for md in sorted(styles.glob("*.md")):
        if md.name == "STYLE_PACK_TEMPLATE.md":
            continue
        txt = read(md) or ""
        if BANS_SCRUB.search(txt):
            continue
        if not (ONE_CURVE.search(txt) and MANDATES_SCRUB.search(txt)):
            continue
        subjects += 1
        if not SCRUB_CARVED.search(txt):
            uncarved.append(md.stem)
    if subjects < 2:
        _skips.append("fewer than two packs both declare one curve and mandate a "
                      "scrub — the scrub exception was not checked")
        return
    try:
        ceiling = json.loads(FLOORS.read_text(encoding="utf-8")).get(
            "scrub_uncarved_at_most")
    except (OSError, ValueError):
        ceiling = None
    if not check(ceiling is not None,
                 "test/floors.json has no `scrub_uncarved_at_most` — a contradiction "
                 "that is not pinned is one that can spread to the next pack quietly"):
        return
    check(
        len(uncarved) <= ceiling,
        f"{len(uncarved)} pack(s) declare one site-wide curve, mandate scrubbed motion "
        f"and carve no `ease: none` exception, above the pinned {ceiling}: "
        f"{', '.join(sorted(uncarved))}. An implementer who reads the curve as total "
        f"eases against the scroll position twice. Lower the pin in the same commit "
        f"as the carve",
    )
    print(f"  scrub exception: {len(uncarved)} of {subjects} pack(s) uncarved "
          f"(pinned at most {ceiling})")

def validate_relative_colour_is_guarded():
    tokens = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles" / "tokens"
    if not tokens.is_dir():
        return
    looked = 0
    for css in sorted(tokens.glob("*.css")):
        text = read(css) or ""
        if "rgb(from" not in text:
            continue
        looked += 1
        lines = text.split("\n")
        depth_supports = 0
        open_braces_at_supports: list[int] = []
        depth = 0
        for i, line in enumerate(lines):
            if re.match(r"\s*@supports\s*\(color:\s*rgb\(\s*from\s", line):
                open_braces_at_supports.append(depth)
            depth += line.count("{") - line.count("}")
            while open_braces_at_supports and depth <= open_braces_at_supports[-1]:
                open_braces_at_supports.pop()
            m = RELATIVE_CUSTOM_PROP.match(line)
            if not m:
                continue
            check(
                bool(open_braces_at_supports),
                f"styles/tokens/{css.name}:{i + 1}: `{m.group(1)}` is declared with "
                f"relative colour outside `@supports (color: rgb(from red r g b))`. "
                f"A custom property parses that value everywhere and fails only at "
                f"substitution, so a literal declared above it is not a fallback — "
                f"every `var({m.group(1)})` resolves to `unset` instead",
            )
    if not looked:
        _skips.append("no token layer uses relative colour — the guard was not checked")



# ------------------------------------- font loading is not this library's layer
#
# The pack skeleton now states it: there is no `@font-face` anywhere in this
# library and no `font-display` declaration, because the packs name families and
# the consumer loads them. That is a decision, and it is the kind that goes stale
# silently — B-030 was filed on the reading that `font-display` appears in 21
# files and metric overrides in none, "a guaranteed reflow". Re-measured
# 2026-08-20: `font-display` appears in exactly **three** places, all of them the
# SAME comment line in `manpage`'s token layer describing the reference, and there
# are **zero** `@font-face` blocks. The defect had no shape here.
#
# Comments are stripped before looking, because that comment is what made the
# original count wrong.
FONT_FACE = re.compile(r"@font-face\b")
FONT_DISPLAY_DECL = re.compile(r"(?<!-)\bfont-display\s*:")
CSS_COMMENT = re.compile(r"/\*.*?\*/", re.S)


def validate_font_loading_stays_out():
    roots = [ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles" / "tokens", ROOT / "kits"]
    looked = 0
    for root in roots:
        if not root.is_dir():
            continue
        for css in sorted(root.rglob("*.css")):
            if "node_modules" in css.parts:
                continue
            looked += 1
            code = CSS_COMMENT.sub(" ", read(css) or "")
            rel = css.relative_to(ROOT)
            check(
                not FONT_FACE.search(code),
                f"{rel}: declares `@font-face`. This library names font families and "
                f"leaves loading to the consumer — the skeleton's Type section says so, "
                f"and a pack that changes that changes the sentence too",
            )
            check(
                not FONT_DISPLAY_DECL.search(code),
                f"{rel}: declares `font-display`, which is a descriptor and only means "
                f"anything inside an `@font-face` this library does not ship. Either the "
                f"pack owns font loading now — and says so — or the declaration is inert",
            )
    if looked < 2:
        _skips.append("fewer than two stylesheets — the font-loading decision was "
                      "not checked")



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
    validate_contents_lists()
    validate_manifest_descriptions()
    validate_contract_terminology()
    validate_contract_split()
    validate_contract_declaration()
    validate_every_surface_class_is_discoverable()
    validate_core_vocabulary()
    validate_reduced_motion()
    validate_pack_container_answer()
    validate_kit_breakpoints()
    validate_release_register()
    validate_board_columns()
    validate_hero_states_its_obligations()
    validate_pack_declares_its_silences()
    validate_a_count_names_its_noun()
    validate_theme_split_is_derived()
    validate_table_marks_match_the_contract()
    validate_motion_ceiling_has_one_home()
    validate_worked_radius_sums_compute()
    validate_component_classes_are_answered()
    validate_excluded_sets_are_declared()
    validate_token_population_counts()
    validate_token_comments_respect_the_bands()
    validate_confined_tokens_measured_where_used()
    validate_t1_carriers_survive()
    validate_reconstructed_stamp_count()
    validate_retirement_window()
    validate_every_plant_names_its_check()
    validate_gate_has_no_shadowed_names()
    validate_every_duration_answers_reduce()
    validate_prescribed_tokens_resolve()
    validate_scrub_carves_its_exception()
    validate_relative_colour_is_guarded()
    validate_font_loading_stays_out()
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
