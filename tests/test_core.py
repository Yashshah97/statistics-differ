import unittest
from statistics_differ import core

class TestStatisticsDiffer(unittest.TestCase):

    def test_diff(self):
        stats1 = [1, 2, 3]
        stats2 = [4, 5, 6]
        differ = core.StatisticsDiffer(stats1, stats2)
        self.assertEqual(differ.diff(), [(0, 1, 4, 3.0), (1, 2, 5, 3.0), (2, 3, 6, 3.0)])

    def test_merge(self):
        stats1 = [1, 2]
        stats2 = [4, 5]
        merged_stats = [None, None]
        self.assertEqual(core.merge(stats1, stats2, merged_stats), [1, 5])

    def test_merge_conflict(self):
        stats1 = [1, 2]
        stats2 = [3, 2]
        merged_stats = [None, None]
        with self.assertRaises(ValueError):
            core.merge(stats1, stats2, merged_stats)

if __name__ == '__main__':
    unittest.main()
