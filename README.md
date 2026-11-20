# Statistics Diff Engine

This project provides a diff engine designed to compare and analyze statistical distributions, enabling users to identify differences between data sets and assess the significance of these discrepancies through built-in hypothesis testing capabilities. The engine features a robust three-way merge function for efficient resolution of conflicts, all implemented in pure Python with comprehensive documentation and testing frameworks.

## What makes it unique

Combines distribution fitting and hypothesis tests with a structural diff/merge tool with three-way merge — a niche where few ready-made tools exist.

## Features

- **`statistics_differ/core.py`** — Core diff engine logic
- **`statistics_differ/distribution.py`** — Distribution fitting and hypothesis testing functions
- **`statistics_differ/stats_util.py`** — Utility functions for statistical calculations
- **`statistics_differ/diff_engine.py`** — Main entry point for the statistics diff engine
- **`statistics_differ/merge_tool.py`** — Three-way merge logic for merged results
- **`statistics_differ/tests.py`** — Unit tests and test fixtures for the entire module

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/statistics-differ.git
cd statistics-differ

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
statistics-differ/
├── statistics_differ/
│   ├── core.py
│   ├── distribution.py
│   ├── stats_util.py
│   ├── diff_engine.py
│   ├── merge_tool.py
│   ├── tests.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **statistics** · Archetype: **differ** ·
Built autonomously by JARVIS on 2026-11-19. MIT licensed.
