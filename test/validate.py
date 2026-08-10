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
# The six packs shipped before the widening stay on the nine. Backfilling them
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
    "## 4. Lazyweb sweeps — layout crosses, identity does not",
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


def validate_links():
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in (".git", "node_modules") for part in md.parts):
            continue
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
}
WORD_NUMBERS = {w: n for n, w in NUMBER_WORDS.items()}
COUNTED = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|\d{1,2})"
    r" (?:locked |named |shipped |pluggable |real |React |reference )*"
    r"(?:visual |style )?(pack|kit|scenario|heading)s\b",
    re.I,
)
# "A fork between two packs" counts a relationship, not the library. A hyphen
# means a compound (`four-packs`, a branch name), not a count.
COUNT_NOT_A_TALLY = re.compile(r"(?i)\b(?:between|either|each|any|both|per|same)\s+$")


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
    sources = [
        "README.md", "CONTRIBUTING.md", "bin/cli.js", "docs/DOCMAP.md",
        "cursor/rules/sheleg-design.mdc",
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
            raw, noun = m.group(1).lower(), m.group(2).lower()
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
    for md in sorted(ROOT.rglob("*.md")):
        parts = set(md.parts)
        if parts & {".git", "node_modules", "graphify-out", "test", "audit",
                     "superpowers"} or md.name == "CHANGELOG.md":
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


def has_heading(text: str, heading: str) -> bool:
    """A heading is a line, not a substring.

    `"## Hero" in text` is true of any prose that mentions `## Hero` -- including
    the core-contract note that lists the four sections a pack omits, which made
    six packs look widened the moment they declared they were not. Structure is
    checked structurally.
    """
    return re.search(rf"^{re.escape(heading)}\s*$", text, re.M) is not None


def validate_contract_declaration():
    styles = ROOT / PLUGIN_DIR / "skills" / PLUGIN / "styles"
    skill = read(styles.parent / "SKILL.md") or ""
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
            check(
                f"styles/{name}.md" in skill and "core contract" in skill,
                f"SKILL.md: '{name}' is on the core contract and the pack table does not "
                "say so -- the table is where the pack is chosen",
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
PLANTS = (
    (
        "a count that is true of an older release",
        "README.md",
        lambda t: t.replace("**twelve locked style\npacks**", "**six locked style\npacks**"),
    ),
    (
        "a manifest naming three packs of twelve",
        f"{PLUGIN_DIR}/.claude-plugin/plugin.json",
        lambda t: t.replace("briefing-room (dark 16:9 deck), ", ""),
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
            "## 7. Round-trip discipline\n\nSee `docs/superpowers/backlog.md` for the open rows.",
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
)


def self_test() -> int:
    src = Path(__file__).resolve().parent.parent
    ok = True
    for label, rel, mutate in PLANTS:
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "repo"
            shutil.copytree(
                src, dst,
                ignore=shutil.ignore_patterns(".git", "node_modules", "graphify-out", "dist"),
            )
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
            else:
                print(f"  caught  {label}")
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


# ------------------------------------------------- the bundle stands alone
#
# The installed bundle is `plugins/<p>/skills/<s>/` and nothing above it: 32
# files, every one .md or .css. Three times now a rule inside it has instructed
# the reader to use something only the repository has, and each time the rule
# read as authoritative right up to the moment someone tried to follow it:
#
#   1.10.0  the `Contract: core` note cited `docs/superpowers/backlog.md`
#   1.11.0  §7 said to record the pack version, in a bundle carrying none
#   1.11.0  §1 built an argument on "the same six component names" and named none
#
# The 1.10.0 run fixed the instance and not the class -- it swept the literal
# form (a repo path in backticks, now zero) and left the two forms that are not
# paths. This check covers the three NAMED forms above. It is not a proof that
# the bundle is self-sufficient in general; no check is. It is the three shapes
# that have actually shipped, so a fourth has to be a new shape.
REPO_ONLY_DIRS = ("docs/", "test/", "kits/", ".github/", "scripts/", "cursor/")


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
    validate_contract_declaration()
    validate_core_vocabulary()
    validate_bundle_self_sufficiency()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        sys.exit(1)
    check_floor("validate.py", checks)
    print(f"OK ({checks} checks)")


if __name__ == "__main__":
    main()
