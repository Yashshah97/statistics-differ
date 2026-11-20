import unittest
from statistics_differ import diff_engine

class TestDiffEngine(unittest.TestCase):

    def test_diff_result_init(self):
        stats_diff = {'mean': 0.5, 'stddev': 0.3}
        result = diff_engine.DiffResult(stats_diff)
        self.assertEqual(result.stats_diff, stats_diff)

    def test_main_args_parsing(self):
        import sys
        import argparse
        parser = argparse.ArgumentParser()
        namespace = parser.parse_args(['--file1', 'file1.txt', '--stats1', 'stats1.json',
                                       '--file2', 'file2.txt', '--stats2', 'stats2.json'])
        self.assertEqual(namespace.file1, 'file1.txt')
        self.assertEqual(namespace.stats1, 'stats1.json')
        self.assertEqual(namespace.file2, 'file2.txt')
        self.assertEqual(namespace.stats2, 'stats2.json')

    def test_main_exit_code(self):
        sys.exitcode = 0
        diff_engine.main()
        self.assertEqual(sys.exitcode, 0)

if __name__ == '__main__':
    unittest.main()
