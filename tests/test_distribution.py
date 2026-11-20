"""Smoke tests for distribution."""
import unittest

from statistics_differ import distribution


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(distribution, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(distribution) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
