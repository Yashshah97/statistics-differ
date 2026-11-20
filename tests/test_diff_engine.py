"""Smoke tests for diff_engine."""
import unittest

from statistics_differ import diff_engine


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(diff_engine, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(diff_engine) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
