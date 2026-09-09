#!/usr/bin/env python3
"""FIX-UP-05.03 — the writer contract applied to the design installer (sherlock
audit, UP-05 leaf 3).

The finding: the design CLI copied each managed file straight into the target
(a crash mid-install leaves a partial write), with no obsolete-managed removal
and no recoverable generation.

The fix under test, against bin/cli.js through node: installFilesTransactionally
stages the managed set on the same filesystem, verifies, snapshots the previous
generation, switches with atomic renames, and removes OBSOLETE managed files
(tracked by a manifest) while never touching unknown user files. A stage crash
leaves the active install intact. The install.sh staging discipline is asserted
textually.

Standard library only.
"""
import json
import os
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CLI = os.path.join(ROOT, "bin", "cli.js")
INSTALL_SH = os.path.join(ROOT, "install.sh")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def make_src(files):
    src = tempfile.mkdtemp()
    for f, body in files.items():
        d = os.path.join(src, f)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        with open(d, "w") as fh:
            fh.write(body)
    return src


def node(body):
    return subprocess.run(["node", "-e", "const m=require(process.argv[1]);" + body, CLI],
                          capture_output=True, text=True, timeout=60)


def t_clean_install_stages_and_verifies():
    src = make_src({"SKILL.md": "# new\n", "styles/workbench.css": "a{}\n"})
    tgt = tempfile.mkdtemp()
    files = ["SKILL.md", "styles/workbench.css"]
    r = node(f"m.installFilesTransactionally({json.dumps(src)}, {json.dumps(tgt)}, {json.dumps(files)});")
    assert r.returncode == 0, r.stderr[:200]
    assert open(os.path.join(tgt, "SKILL.md")).read() == "# new\n"
    assert os.path.isfile(os.path.join(tgt, ".sheleg-manifest.json"))
    assert not [x for x in os.listdir(tgt) if x.startswith(".sheleg-staging-")], "staging leaked"


def t_stage_crash_leaves_active_intact():
    src = make_src({"SKILL.md": "# new\n", "b.md": "# new b\n"})
    tgt = tempfile.mkdtemp()
    with open(os.path.join(tgt, "SKILL.md"), "w") as fh:
        fh.write("# OLD\n")
    files = ["SKILL.md", "b.md"]
    script = (
        "const fs=require('fs');let n=0;const real=fs.copyFileSync;"
        "fs.copyFileSync=(a,b)=>{if(++n===2){throw new Error('ENOSPC');}return real(a,b);};"
        "const m=require(process.argv[1]);"
        f"try{{m.installFilesTransactionally({json.dumps(src)},{json.dumps(tgt)},{json.dumps(files)});"
        "console.log('NO_THROW');}catch(e){console.log('ABORTED');}")
    r = subprocess.run(["node", "-e", script, CLI], capture_output=True, text=True, timeout=60)
    assert "ABORTED" in r.stdout, f"a stage crash did not abort: {r.stdout} {r.stderr[:200]}"
    assert open(os.path.join(tgt, "SKILL.md")).read() == "# OLD\n", \
        "the old install was damaged by a stage crash"
    assert not [x for x in os.listdir(tgt) if ".sheleg-staging-" in x], "staging leaked"


def t_obsolete_managed_removed_user_files_kept():
    src1 = make_src({"SKILL.md": "# v1\n", "styles/old.css": "old\n"})
    tgt = tempfile.mkdtemp()
    node(f"m.installFilesTransactionally({json.dumps(src1)}, {json.dumps(tgt)}, "
         f"{json.dumps(['SKILL.md', 'styles/old.css'])});")
    # a user file the installer never wrote
    with open(os.path.join(tgt, "my-notes.md"), "w") as fh:
        fh.write("mine\n")
    # v2 drops old.css from the managed set
    src2 = make_src({"SKILL.md": "# v2\n"})
    r = node(f"console.log(JSON.stringify(m.installFilesTransactionally({json.dumps(src2)}, "
             f"{json.dumps(tgt)}, {json.dumps(['SKILL.md'])})));")
    res = json.loads(r.stdout)
    assert "styles/old.css" in res["removed"], "an obsolete managed file was not removed"
    assert not os.path.exists(os.path.join(tgt, "styles", "old.css")), \
        "the obsolete managed file survived"
    assert open(os.path.join(tgt, "my-notes.md")).read() == "mine\n", \
        "an unknown user file was removed — obsolete removal touched more than the managed set"


def t_install_sh_stages_before_swapping():
    sh = open(INSTALL_SH, encoding="utf-8").read()
    assert 'STAGING="$TARGET/.sheleg-staging.$$"' in sh, \
        "install.sh does not stage on the target filesystem"
    assert 'mv "$STAGING/$f" "$TARGET/$f"' in sh, \
        "install.sh does not swap staged files into place"
    assert 'cp "$SRC_DIR/$f" "$TARGET/$f"' not in sh, \
        "install.sh still copies straight into the target"


def main():
    case("a clean install stages, verifies and writes a manifest",
         t_clean_install_stages_and_verifies)
    case("a stage crash leaves the active install intact",
         t_stage_crash_leaves_active_intact)
    case("obsolete managed files are removed, user files are kept",
         t_obsolete_managed_removed_user_files_kept)
    case("install.sh stages before swapping", t_install_sh_stages_before_swapping)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
