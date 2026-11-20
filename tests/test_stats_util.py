import unittest
from statistics_differ import stats_util


class TestStatsUtil(unittest.TestCase):

    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(stats_util.calculate_mean(data), 3)

    def test_calculate_std_dev(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_util.calculate_std_dev(data), math.sqrt(2.5))

    def test_calculate_variance(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_util.calculate_variance(data), 2.5)

    def test_calculate_skewness(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(stats_util.calculate_skewness(data), 0)

    def test_calculate_kurtosis(self):
        data = [1, 1, 1, 1, 1]
        self.assertAlmostEqual(stats_util.calculate_kurtosis(data), -2)

if __name__ == '__main__':
    unittest.main()
