"""Smoke tests for merge_tool."""
import unittest

from statistics_differ import merge_tool


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(merge_tool, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(merge_tool) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
