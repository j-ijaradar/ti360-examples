# Quickstart — CLI

The `ti360` binary is the core engine with a command-line face — static
binaries ship on GitHub releases, or build with
`cargo install --path core`.

```bash
ti360 profile data.csv                # canonical JSON profile
ti360 validate data.csv               # structural checks (exit code 1 on fail)
ti360 health data.csv                 # Data Health Score
ti360 classify data.csv               # modality profile match
ti360 advise data.csv                 # the deterministic Advisor
ti360 fingerprint data.csv            # what the Advisor consumed
```

All outputs are canonical JSON — byte-identical to the Python and R
bindings, which is enforced in CI. Add `--pretty` for humans.

## Bundles, reports, pipelines

```bash
ti360 profile data.ti360              # bundles are self-describing
ti360 render report_ir.json --to html --out report.html
ti360 run pipeline.yaml --out out/    # provenance manifest included
```

## Pretrained models (opt-in)

```bash
ti360 zoo list
ti360 zoo card ti360/impute-saits-mini    # read the limits first
ti360 zoo fetch ti360/impute-saits-mini   # checksum-verified cache
ti360 impute data.csv --model ti360/impute-saits-mini --out filled.parquet
ti360 predict data.csv --model ti360/predict-rnn-mini
```

Result summaries record the exact model id, version and sha256.
