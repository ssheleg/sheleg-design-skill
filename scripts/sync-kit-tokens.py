#!/usr/bin/env python3
"""Re-copy each pack's token layer into its kit, byte for byte.

A kit's `src/styles.css` is the pack's token layer verbatim, followed by the
kit's own component half. `validate.py` refuses any drift between them --
"copy it, never transcribe it" -- which means every edit to a token layer, down
to a comment, makes the kit red until the block is copied again.

That copy was done by hand three times on 2026-08-20 and the third time touched
twelve kits at once, which is where a hand-run step stops being a step and
becomes a defect waiting for a tired afternoon. This is the same operation,
written down.

WHERE THE BOUNDARY COMES FROM, and why this cannot guess. The kit file is
`<old token layer><component half>` and only `git` knows what the old layer was.
So the previous committed version of the token file is read from `HEAD` and used
as the prefix to strip. A kit that does not start with it is REPORTED and left
alone: a mismatch means either the kit was hand-edited inside the token block or
the token file was already committed, and in both cases a script that guessed
the boundary would eat part of the component half.

Usage:  python3 scripts/sync-kit-tokens.py           # re-copy where it drifted
        python3 scripts/sync-kit-tokens.py --check   # report, change nothing
Exit:   0 = every kit carries its pack's token layer
        1 = at least one kit drifted (--check), or could not be synced
        2 = git is not available, so the boundary cannot be established
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles/tokens"
KITS = ROOT / "kits"


def committed(rel: str) -> str | None:
    """The version of a tracked file at HEAD, or None if git cannot say."""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{rel}"],
                             capture_output=True, text=True)
    except FileNotFoundError:
        return None
    return out.stdout if out.returncode == 0 else None


def main() -> int:
    check = "--check" in sys.argv[1:]
    if committed("package.json") is None:
        print("no git history here — the token-block boundary cannot be established, "
              "and a check that cannot look is not a pass", file=sys.stderr)
        return 2

    drifted, synced, stuck = [], [], []
    for css in sorted(TOKENS.glob("*.css")):
        kit = KITS / css.stem / "src" / "styles.css"
        if not kit.is_file():
            continue
        now = css.read_text(encoding="utf-8")
        cur = kit.read_text(encoding="utf-8")
        if cur.startswith(now):
            continue
        drifted.append(css.stem)
        rel = str(css.relative_to(ROOT))
        was = committed(rel)
        if was is None or not cur.startswith(was):
            stuck.append(css.stem)
            continue
        if not check:
            kit.write_text(now + cur[len(was):], encoding="utf-8")
        synced.append((css.stem, len(was), len(now), len(cur) - len(was)))

    for stem, old_n, new_n, tail in synced:
        verb = "would re-copy" if check else "re-copied"
        print(f"  {verb:14} {stem}: token block {old_n} -> {new_n} chars, "
              f"component half {tail} chars untouched")
    for stem in stuck:
        print(f"  STUCK          {stem}: the kit does not start with the committed token "
              f"layer, so the boundary is unknown — copy it by hand and say why",
              file=sys.stderr)

    if not drifted:
        print("every kit carries its pack's token layer")
        return 0
    print(f"\n{len(drifted)} kit(s) drifted, {len(synced)} "
          f"{'syncable' if check else 'synced'}, {len(stuck)} stuck")
    return 1 if (check or stuck) else 0


if __name__ == "__main__":
    raise SystemExit(main())
