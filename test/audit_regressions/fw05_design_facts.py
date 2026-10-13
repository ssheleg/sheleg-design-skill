#!/usr/bin/env python3
"""FW05 source-derived palette and disclosure controls; no browser/provider claims."""
import importlib.util
from pathlib import Path
import sys
import subprocess

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('palette', ROOT / 'test/validate_palette.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
count = 0

def expect(ok, label):
    global count
    assert ok, label
    count += 1

for css in sorted(v.TOKENS.glob('*.css')):
    md = v.PACKS / (css.stem + '.md')
    if not md.exists():
        continue
    expect(not v.dark_palette_problems(css.read_text(), md.read_text(), css.stem in v.LEGACY_DARK_TABLES),
           css.stem + ' current table')

expect(bool(v.dark_palette_problems('', 'Themes: full theme twin.\n## Palette\n| Token | Dark value |\n|---|---|\n', legacy=True)), 'legacy empty table refuses')

css = (v.TOKENS / 'daylight.css').read_text()
md = (v.PACKS / 'daylight.md').read_text()
expect(bool(v.dark_palette_problems(css, md.replace('`#0b0f14`', '`#010101`'))), 'stale value refuses')
expect(bool(v.dark_palette_problems(css, md.replace(v.DARK_PALETTE_START, '').replace(v.DARK_PALETTE_END, ''))),
       'marker removal cannot turn new table into legacy')
expect(bool(v.dark_palette_problems(css.replace('--bg: #0b0f14;', '--bg: #010101;'), md)),
       'source change makes old copied value fail')
expect(not v.dark_palette_problems(css, 'Themes: single — not a theme twin.\n## Palette\n'),
       'single-theme counterexample')

generator_spec = importlib.util.spec_from_file_location('sync_dark', ROOT / 'scripts/sync-dark-palettes.py')
g = importlib.util.module_from_spec(generator_spec)
generator_spec.loader.exec_module(g)
expect(g.refresh(css, md) == md, 'generator leaves current table unchanged')
expect(g.refresh(css, md.replace('`#0b0f14`', '`#010101`')) == md, 'generator repairs stale source literal')
reverse = md.replace(v.DARK_PALETTE_START, '__FW05__').replace(v.DARK_PALETTE_END, v.DARK_PALETTE_START).replace('__FW05__', v.DARK_PALETTE_END)
for label, text in [('missing', md.replace(v.DARK_PALETTE_END, '')), ('reversed', reverse)]:
    expect(text != md, label + ' marker plant landed')
    try:
        g.refresh(css, text)
    except ValueError:
        expect(True, label + ' markers refuse generation')
    else:
        raise AssertionError(label + ' markers accepted')
result = subprocess.run([sys.executable, str(ROOT / 'scripts/sync-dark-palettes.py'), '--wrong'], capture_output=True)
expect(result.returncode == 2, 'generator rejects unknown arguments')

md = (v.PACKS / 'pigeonhole.md').read_text()
css = (v.TOKENS / 'pigeonhole.css').read_text()
maps = v._theme_maps(css)
v._reset()
v._check_stated_delta('pigeonhole', '--good', '--warn', maps, md, css)
expect(v.checks > 0 and not v.failures, 'rewritten real disclosure is computed')
v._reset()
v._check_stated_delta('pigeonhole', '--good', '--warn', maps,
                      md.replace('5.0 under', '99.0 under'), css)
expect(any('the disclosure for' in f for f in v.failures), 'wrong pair value refuses by intended check')
v._reset()
v._tally['delta_unbound'] = 0
v._check_stated_delta('pigeonhole', '--good', '--warn', maps,
                      '`--danger`, `--good` and `--warn` are never by colour alone, 5.0 under deuteranopia.', css)
v.validate_disclosure_coverage()
expect(any('unbound token pairs' in f for f in v.failures), 'old multi-pair shape refuses')
expect(v._figures('Cost changed by 14.8; three unrelated items') == [], 'unqualified numbers stay outside parser')
expect(v._figures('`--warning` and `--danger` by 14.8 at full colour') == [(14.8, 'full colour')],
       'explicit qualifier makes number checkable')
print(f'FW05 design facts: {count} controls passed')
