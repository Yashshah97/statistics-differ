import unittest
from statistics_differ import distribution

class TestDistributionFunctions(unittest.TestCase):
    def test_normal_cdf(self):
        self.assertAlmostEqual(distribution.normal_cdf(0), 0.5)
        self.assertAlmostEqual(distribution.normal_cdf(-1), 0.15865525)
        self.assertAlmostEqual(distribution.normal_cdf(1), 0.84134475)

    def test_chi_squared(self):
        cdf = distribution.chi_squared(3, p=0.5)
        self.assertAlmostEqual(cdf(4), 0.01014492)
        self.assertAlmostEqual(cdf(10), 0.99996445)

    def test_t_distribution(self):
        cdf = distribution.chi_squared(3)
        t_cdf, _ = distribution.t_distribution(cdf)(1, 3)
        self.assertAlmostEqual(t_cdf, 0.99867292)

if __name__ == '__main__':
    unittest.main()
