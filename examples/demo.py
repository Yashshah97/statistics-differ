"""Demo for Statistics Diff Engine."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import statistics_differ

print("Statistics Diff Engine", "v" + statistics_differ.__version__)
print("modules:", [m for m in dir(statistics_differ) if not m.startswith('_')])
