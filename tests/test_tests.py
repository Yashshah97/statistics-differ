import unittest
from statistics_differ import tests

class TestTests(unittest.TestCase):
    def test_capture_output_context_manager(self):
        with tests.capture_output() as f:
            print("Hello")
        self.assertEqual(f.getvalue(), "Hello\n")

if __name__ == "__main__":
    unittest.main()
