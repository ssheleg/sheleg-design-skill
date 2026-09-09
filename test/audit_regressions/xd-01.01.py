#!/usr/bin/env python3
"""XD-01.01 — knowledge provenance: every adopted method carries its receipt
(sherlock audit, XD-01, external-adoption).

Adopting method from open repositories (pbakaus/impeccable,
julianoczkowski/designer-skills) is only legitimate if each adopted fragment
records WHERE it came from and WHAT was done with it. This leaf creates
KNOWLEDGE_PROVENANCE.md; the test holds it to the acceptance:

* every adopted row has a commit-pinned source, a source-relative path, a
  SHA256 of the reviewed file, and a permalink;
* derived vs adapted is distinguished, with the transfer rules for adapted;
* no promise that a clone licence auto-clears third-party assets; images/fonts
  are not vendored; and the launcher, foreign routers/hooks and API/font
  services are excluded from the knowledge package.

Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                   "KNOWLEDGE_PROVENANCE.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def text():
    with open(DOC, encoding="utf-8") as fh:
        return fh.read()


def rows():
    out = []
    for line in text().splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|(.+)\|\s*$", line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            out.append(cells)
    return out


def t_doc_exists_and_has_rows():
    assert os.path.isfile(DOC), "KNOWLEDGE_PROVENANCE.md was not created"
    assert len(rows()) >= 6, f"only {len(rows())} adopted rows"


def t_every_row_has_source_sha_permalink():
    for r in rows():
        # cells: source(commit), path, sha256, kind, verified, permalink
        source, path, sha, kind, verified, permalink = r[:6]
        assert re.search(r"@\s*`[0-9a-f]{40}`", source), f"row has no commit-pinned source: {source}"
        assert path.startswith("`") and path.endswith("`") and "/" in path, \
            f"row has no source-relative path: {path}"
        assert re.fullmatch(r"`[0-9a-f]{64}`", sha), f"row has no SHA256 of the reviewed file: {sha}"
        assert kind in ("derived", "adapted"), f"row kind is not derived/adapted: {kind}"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", verified), f"row has no verified date: {verified}"
        assert permalink.startswith("https://github.com/") and "/blob/" in permalink, \
            f"row has no permalink: {permalink}"


def t_derived_adapted_distinction_and_transfer_rules():
    flat = " ".join(text().split())
    assert "derived" in flat and "adapted" in flat, "the derived/adapted distinction is missing"
    assert "Carry the licence with the text" in flat, "the Apache notice/modification rule is missing"
    assert "MIT notice is checked and attached" in flat, "the platform MIT-notice rule is missing"


def t_no_auto_clear_and_no_vendored_assets():
    flat = " ".join(text().split())
    assert "does NOT\n   automatically clear the third-party assets".replace("\n   ", " ") in flat \
        or "does NOT automatically clear the third-party assets" in flat, \
        "the clone-does-not-clear-assets rule is missing"
    assert "no binary asset is vendored" in flat.lower() or "no binary asset is vendored" in flat, \
        "images/fonts vendoring is not refused"


def t_package_boundary():
    flat = " ".join(text().split())
    assert "the launcher" in flat and "not knowledge" in flat, "the launcher exclusion is missing"
    assert "foreign router or hook" in flat, "the foreign router/hook exclusion is missing"
    assert "API or font SERVICE" in flat or "API or font service" in flat.replace("SERVICE", "service"), \
        "the API/font service exclusion is missing"


def main():
    case("KNOWLEDGE_PROVENANCE.md exists with adopted rows", t_doc_exists_and_has_rows)
    case("every adopted row has source(commit)+path+SHA256+permalink",
         t_every_row_has_source_sha_permalink)
    case("derived/adapted distinguished, with transfer rules",
         t_derived_adapted_distinction_and_transfer_rules)
    case("no auto-clear of third-party assets; images/fonts not vendored",
         t_no_auto_clear_and_no_vendored_assets)
    case("launcher, foreign router/hook and API/font service are excluded",
         t_package_boundary)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
