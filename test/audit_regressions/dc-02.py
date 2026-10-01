#!/usr/bin/env python3
"""DC-02: review-contract integrity, not a punctuation linter or model eval.

The same assertions run against the bundle and mutations that remove each
safety boundary. No fixture result claims that an agent obeyed the instruction.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / 'plugins/sheleg-design/skills/sheleg-design'


def review_contract(text):
    section = text.split('## Rendered copy — the design/copywriting seam', 1)[1]
    requirements = {
        'roles': ('eyebrows', 'headings', 'line-break fragments', 'captions', 'labels'),
        'ownership': ('copywriting', 'AT-07', 'project policy', 'ordinary prose'),
        'evidence': ('selector', 'visible text', 'viewport', 'revision', 'coverage'),
        'exceptions': ('questions', 'abbreviations', 'URLs', 'version numbers'),
        'fallback': ('unverified', 'exit 0', 'source/generated-copy'),
    }
    for name, needles in requirements.items():
        for needle in needles:
            if needle not in section:
                raise AssertionError(f'{name}: missing {needle}')
    for probe in ('Your agents.<br>Your tools.', 'Ready?', 'v1.2.3',
                  'https://example.org', 'No runtime capture'):
        if probe not in section:
            raise AssertionError(f'missing review counterexample: {probe}')


class ReviewContract(unittest.TestCase):
    def setUp(self):
        self.text = (BUNDLE / 'VISUAL_REVIEW.md').read_text()

    def test_visible_copy_contract(self):
        review_contract(self.text)

    def test_load_trigger_reaches_copy_review(self):
        skill = (BUNDLE / 'SKILL.md').read_text()
        trigger = skill.split('**Visual review**', 1)[1].split('\n- ', 1)[0]
        self.assertIn('VISUAL_REVIEW.md', trigger)
        self.assertIn('rendered copy', trigger)

    def test_director_uses_same_review_home(self):
        director = (BUNDLE / 'CREATIVE_DIRECTOR.md').read_text()
        self.assertIn('VISUAL_REVIEW.md#rendered-copy', director)

    def test_empty_state_example_preserves_role_boundary(self):
        example = (ROOT / 'kits/deskmate/src/Empty.md').read_text()
        self.assertIn('title="No integrations match “zzq”"', example)
        self.assertIn('detail="Check the spelling, or clear the filter to see all of them."', example)

    def test_missing_boundary_mutations_are_refused(self):
        review_contract(self.text)
        for token in ('line-break fragments', 'ordinary prose', 'version numbers',
                      'coverage', 'unverified', 'Your agents.<br>Your tools.'):
            with self.subTest(token=token):
                with self.assertRaises((AssertionError, IndexError)):
                    review_contract(self.text.replace(token, 'REMOVED'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
