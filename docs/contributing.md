# Contributing

## Ground rules (from the platform plan)

1. **One engine**: anything that computes results goes in
   `trafficinsight360-core`; Python/R/CLI are bindings. Cross-language
   byte parity of canonical JSON is enforced in CI — a change that breaks
   parity is a bug even if each language "works".
2. **Determinism first**: no wall-clock in canonical outputs, floats via
   the canonical formatter, BTree ordering for maps. When in doubt,
   choose the option preserving determinism, offline operation and
   honest claims.
3. **Honest claims**: performance statements need committed benchmarks;
   model cards state provenance and limits; the privacy toolkit never
   says "anonymization".

## Setup

```bash
# engine + CLI
cargo test && cargo clippy --workspace --all-targets -- -D warnings

# Python package (builds the PyO3 crate)
pip install ./py/trafficinsight360[dev,full,polars]
pytest -m "not slow and not pdf"          # from py/trafficinsight360
ruff check trafficinsight360/ tests/ && mypy trafficinsight360/

# R package (needs R + Rust)
R CMD INSTALL r/trafficinsight360r
Rscript -e 'testthat::test_dir("r/trafficinsight360r/tests/testthat")'

# docs
pip install sphinx myst-parser furo sphinx-copybutton
sphinx-build -W -b html docs docs/_build/html
```

## Working agreements

- Conventional commits; one PR per phase-sized change.
- Update the plan's status table and `CHANGELOG.md` as work lands.
- Knowledge-base edits regenerate the advisor report card in CI — a rule
  change that regresses the card fails the build, by design.
- New Python code must type-check clean; the mypy legacy baseline in
  `pyproject.toml` only ever shrinks.
- Zoo models: never commit weights; cards are stamped by the committed
  export/eval pipeline, not by hand.
