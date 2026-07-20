#!/usr/bin/env python3
"""Consistency validator for the sheleg-design-skill repo (stdlib only).

Checks:
  1. Manifests parse, required fields present, versions in sync with CHANGELOG.
  2. Every skill has front-matter: name (matching its directory), description.
  3. The reference doc SHELEG_DESIGN.md ships next to SKILL.md.
  4. Every command has front-matter: description.
  5. Every cursor rule (.mdc) has front-matter: alwaysApply, and description
     unless alwaysApply is true.
  6. Relative markdown links inside the repo resolve.

Exit code 0 with "OK (<n> checks)" when clean; 1 with FAIL: lines otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "sheleg-design"
PLUGIN_DIR = f"plugins/{PLUGIN}"

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
            if plugin and package and changelog:
                versions = {
                    entry.get("version"),
                    plugin.get("version"),
                    package.get("version"),
                    changelog,
                }
                check(
                    len(versions) == 1,
                    "version mismatch: marketplace=%s plugin=%s package=%s changelog=%s"
                    % (
                        entry.get("version"),
                        plugin.get("version"),
                        package.get("version"),
                        changelog,
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
        check(
            desc.startswith("Use when"),
            f"{rel}/SKILL.md: description must start with 'Use when'",
        )
    check(
        (skills_dir / PLUGIN / "SHELEG_DESIGN.md").is_file(),
        f"{PLUGIN_DIR}/skills/{PLUGIN}/SHELEG_DESIGN.md: missing",
    )
    styles_dir = skills_dir / PLUGIN / "styles"
    packs = sorted(styles_dir.glob("*.md")) if styles_dir.is_dir() else []
    check(len(packs) >= 2, f"{PLUGIN_DIR}/skills/{PLUGIN}/styles: expected >=2 style packs")
    for pack in packs:
        rel = pack.relative_to(ROOT)
        text = read(pack) or ""
        for section in ("## Register", "## Palette", "## Type", "## Motion tokens", "## Bans"):
            check(section in text, f"{rel}: missing required section '{section}'")
        check(
            (styles_dir / "tokens" / f"{pack.stem}.css").is_file(),
            f"{rel}: missing ready-made token layer styles/tokens/{pack.stem}.css",
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


def main():
    validate_manifests()
    validate_skills()
    validate_commands()
    validate_cursor_rules()
    validate_installer_sync()
    validate_links()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        sys.exit(1)
    print(f"OK ({checks} checks)")


if __name__ == "__main__":
    main()
