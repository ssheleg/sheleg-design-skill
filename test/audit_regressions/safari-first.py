#!/usr/bin/env python3
"""Engine order: a rendered surface is checked in WebKit (Safari) first.

Family release 2026-10-16 (R12). The visual-review contract stays tool-agnostic
about the CAPABILITY that takes a frame, but it names the ENGINE order: WebKit
first, Chromium as a stated fallback, and a Chromium-only check reported as
exactly that. The same assertions run against mutations that drop each point,
so the test is watched saying no. Text integrity only: no fixture claims that
an agent followed the order.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / 'plugins/sheleg-design/skills/sheleg-design'
HEADING = '## Engine order — WebKit (Safari) first'


def engine_contract(text):
    section = text.split(HEADING, 1)[1].split('\n## ', 1)[0]
    requirements = {
        'webkit routes': ('safaridriver', 'Playwright', '`webkit`',
                          '--browser webkit', 'npx playwright install webkit',
                          'Safari Web Inspector'),
        'macOS open': ('open -a Safari',),
        'libraries': ('WebKit/Safari backend',),
        'fallback': ('stated fallback', 'Chrome Dev', 'say which and why',
                     'Lighthouse', 'CDP trace', 'chrome-devtools MCP'),
        'own chrome': ('temporary profile', 'close every process'),
        'honest label': ('checked only in Chromium',),
    }
    for name, needles in requirements.items():
        for needle in needles:
            if needle not in section:
                raise AssertionError(f'{name}: missing {needle}')
    # The capability stays tool-agnostic; the engine order sits beside it.
    flat = ' '.join(text.split())
    if 'any working browser capability qualifies' not in flat:
        raise AssertionError('capture is no longer tool-agnostic')
    if 'Playwright is not required' not in flat:
        raise AssertionError('Playwright became required')


class EngineOrder(unittest.TestCase):
    def setUp(self):
        self.text = (BUNDLE / 'VISUAL_REVIEW.md').read_text()

    def test_visual_review_carries_engine_order(self):
        engine_contract(self.text)

    def test_capture_record_names_the_engine(self):
        record = self.text.split('## The capture record', 1)[1].split('\n## ', 1)[0]
        self.assertIn('`engine`', record)

    def test_contents_lists_the_section(self):
        contents = self.text.split('## Contents', 1)[1].split('\n## ', 1)[0]
        self.assertIn('Engine order', contents)

    def test_motion_review_puts_webkit_first(self):
        motion = (BUNDLE / 'MOTION_DOCTRINE.md').read_text()
        step = motion.split('1. **Capture a frame strip and a run video.**', 1)[1]
        step = step.split('2. **Timings against the bands.**', 1)[0]
        self.assertIn('WebKit', step)
        self.assertLess(step.index('WebKit'), step.index('DevTools'))
        self.assertIn('VISUAL_REVIEW.md#engine-order', step)

    def test_director_verify_lane_puts_webkit_first(self):
        director = (BUNDLE / 'CREATIVE_DIRECTOR.md').read_text()
        para = director.split('**Run them where the thing runs.**', 1)[1]
        para = para.split('\n\n', 1)[0]
        self.assertIn('WebKit', para)
        self.assertLess(para.index('WebKit'), para.index('Chrome'))
        self.assertIn('VISUAL_REVIEW.md#engine-order', para)

    def test_dropped_points_are_refused(self):
        engine_contract(self.text)
        for token in ('safaridriver', 'open -a Safari', 'stated fallback',
                      'temporary profile', 'close every process',
                      'checked only in Chromium', 'Chrome Dev',
                      'Playwright is not required'):
            with self.subTest(token=token):
                with self.assertRaises((AssertionError, IndexError)):
                    engine_contract(self.text.replace(token, 'REMOVED'))
        with self.assertRaises(IndexError):
            engine_contract(self.text.replace(HEADING, '## Something else'))


if __name__ == '__main__':
    unittest.main()
