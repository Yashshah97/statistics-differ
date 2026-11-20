import unittest
from statistics_differ import merge_tool

class TestMergeTool(unittest.TestCase):

    def test_merge(self):
        base = [1, 2, 3]
        left = [4, 5, 6]
        right = [7, 8, 9]
        merged = merge_tool.merge_distributions(base, left, right)
        self.assertEqual(merged, [9, 9, 9])

    def test_merge_no_base(self):
        base = None
        left = [4, 5, 6]
        right = [7, 8, 9]
        merged = merge_tool.merge_distributions(base, left, right)
        self.assertEqual(merged, [11, 13, 15])

    def test_merge_empty_lists(self):
        base = []
        left = []
        right = []
        merged = merge_tool.merge_distributions(base, left, right)
        self.assertEqual(merged, [])

if __name__ == "__main__":
    unittest.main()
