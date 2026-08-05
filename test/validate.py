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
  9. Every style pack has a reference kit and vice versa; the six-component
     spine is present in each with props identical to the workbench exemplar;
     every component carries a doc whose category is in the locked taxonomy;
     styles.css opens with the pack's token layer byte for byte and holds no
     colour literal below the component marker; each kit's sync config has its
     required keys, points readmeHeader at a real conventions.md and carries no
     projectId; and nothing kit-shaped reached the installed bundle (ADR-0002).

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
# The pack contract: nine headings every pack must carry, plus "## Motion
# flavor", which only cinematic packs have (workbench is standalone and has no
# motion layer to flavor). Docs that say "ten-heading contract" mean these nine
# plus that conditional one.
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
    raw = raw_front_matter(path)
    check(
        len(raw) <= 1024,
        f"{rel}/SKILL.md: front-matter is {len(raw)} chars, must be under 1024 (canon)",
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
        for section in PACK_SECTIONS:
            check(section in ttext, f"{trel}: missing required section '{section}'")
        check(
            read(ROOT / "templates/style-pack-template.md") == ttext,
            f"{trel}: drifted from templates/style-pack-template.md",
        )
    skill_text = read(skills_dir / PLUGIN / "SKILL.md") or ""
    cli_text = read(ROOT / "bin/cli.js") or ""
    for pack in packs:
        rel = pack.relative_to(ROOT)
        text = read(pack) or ""
        for section in PACK_SECTIONS:
            check(section in text, f"{rel}: missing required section '{section}'")
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


def main():
    validate_manifests()
    validate_skills()
    validate_commands()
    validate_cursor_rules()
    validate_installer_sync()
    validate_kits()
    validate_links()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        sys.exit(1)
    print(f"OK ({checks} checks)")


if __name__ == "__main__":
    main()
