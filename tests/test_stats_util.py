"""Smoke tests for stats_util."""
import unittest

from statistics_differ import stats_util


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(stats_util, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(stats_util) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
