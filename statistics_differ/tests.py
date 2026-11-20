import unittest
from io import StringIO
import sys
import contextlib

class TestStatisticsDiffer(unittest.TestCase):
    def test_mean_diff(self):
        with StringIO() as f:
            sys.stdout = f
            print("1 2")
            print("3 4")
            self.assertEqual(f.getvalue(), "0.5\n")

    @contextlib.contextmanager
    def capture_output(self, *args, **kwargs):
        new_out = StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield sys.stdout
        finally:
            sys.stdout = old_out

    def test_median_diff(self):
        with self.capture_output() as f:
            print("1 2")
            print("3 4")
            self.assertEqual(f.getvalue(), "2\n")

if __name__ == "__main__":
    unittest.main()
