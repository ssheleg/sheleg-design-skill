#!/usr/bin/env python3
"""Check or refresh marked dark tables from the shipped token graph.

Default/--check reads only; --write refreshes canonical tables and their mirror.
Sections without markers are not created or guessed. The palette validator owns
missing-table checks and the exact historical presence-only exception set.
"""
import argparse
import importlib.util
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('palette', ROOT / 'test/validate_palette.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def refresh(css, text):
    start, end = v.DARK_PALETTE_START, v.DARK_PALETTE_END
    if start not in text and end not in text:
        return text
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('malformed derived-table markers')
    pattern = re.escape(start) + r'.*?' + re.escape(end)
    replacement = start + '\n' + v.dark_palette_table(css) + '\n' + end
    result, count = re.subn(pattern, lambda _: replacement, text, flags=re.S)
    if count != 1:
        raise ValueError('reversed derived-table markers')
    problems = v.dark_palette_problems(css, result)
    if problems:
        raise ValueError('; '.join(problems))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()
    changes, errors, marked = [], [], 0
    for md in sorted(v.PACKS.glob('*.md')):
        text = md.read_text()
        if v.DARK_PALETTE_START not in text and v.DARK_PALETTE_END not in text:
            continue
        marked += 1
        try:
            result = refresh((v.TOKENS / (md.stem + '.css')).read_text(), text)
            mirror = ROOT / '.cursor/skills/sheleg-design/styles' / md.name
            if result != text or mirror.read_text() != result:
                changes.append((md, mirror, result))
        except (OSError, ValueError) as exc:
            errors.append(f'{md.name}: {exc}')
    if not marked:
        errors.append('no derived dark palettes found')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1  # refuse all writes when any source is ambiguous
    for md, mirror, result in changes:
        print(('refresh ' if args.write else 'drift ') + md.name)
        if args.write:
            md.write_text(result)
            mirror.write_text(result)
    print(f'{marked} marked tables checked; {len(changes)} changed' if args.write else
          f'{marked} marked tables checked; {len(changes)} drifted')
    return 0 if args.write or not changes else 1


if __name__ == '__main__':
    raise SystemExit(main())
