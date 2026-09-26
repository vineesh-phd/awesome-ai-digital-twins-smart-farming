"""Focused tests for the local checker; no network requests."""
import unittest
from check_repository import anchors, links
from build_catalog import bib_escape


class CheckerTests(unittest.TestCase):
    def test_links_and_code(self):
        self.assertEqual(links('[A](a.md#heading)\n```sh\n[X](missing.md)\n```\n[B](b.md)'), ['a.md#heading', 'b.md'])

    def test_heading_anchors(self):
        self.assertEqual(anchors('# Title\n## A & B\n## A & B\n## AI-Assisted Research Paper'),
                         {'title', 'a--b', 'a--b-1', 'ai-assisted-research-paper'})

    def test_bibtex_escape(self):
        self.assertEqual(bib_escape('A & 10%_B'), r'A \& 10\%\_B')


if __name__ == '__main__':
    unittest.main()
