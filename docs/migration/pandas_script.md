# Migrating from a pandas script to a declarative pipeline

The typical starting point: a `analysis.py` that reads a CSV, fixes
timestamps, fills gaps with something, resamples, computes peak stats and
saves a couple of PNGs. It works — until the next dataset, the next
colleague, or the next "how was this number produced?" question.

## The same work as a pipeline

```yaml
# pipeline.yaml
format: ti360.pipeline/v1
name: monthly-loops
input: loops_2024_06.csv
steps:
  - step: validate
  - step: health
  - step: resample
    params: { freq_seconds: 900 }
  - step: advise
  - step: report
    params: { title: June loop report, out: report.html }
  - step: write
    params: { out: cleaned.parquet }
```

```bash
ti360 run pipeline.yaml --out out/
```

Same from Python (`ti.run_yaml_pipeline("pipeline.yaml", out_dir="out")`)
or R (`ti_run_pipeline("pipeline.yaml", out_dir = "out")`) — the
provenance manifests are byte-identical.

## What each script chore becomes

| pandas script | pipeline |
|---|---|
| `pd.read_csv` + dtype fixing | typed load + modality classification (declarative profiles, no regexes) |
| ad-hoc sanity checks | `validate` + `health` steps: structural checks and a Data Health Score, recorded |
| `fillna(df.mean())` because it was easy | the `advise` step tells you why not (mean imputation destroys seasonal structure — with references), and `impute` can run a vetted model instead |
| `resample("15min").mean()` | `resample` step in the core engine (identical in-memory and streaming out-of-core) |
| matplotlib PNGs pasted into a doc | `report` step: one report IR rendered to HTML/MD (PDF/DOCX via the Python builder) |
| "which input produced this?" | `run_manifest.json`: input sha256, pipeline sha256, engine version, every step's parameters and results |

## Why switch

- **Fewer LOC, more checks**: the six-step YAML above replaces ~100
  lines of script and adds validation, health scoring and advice the
  script never had.
- **Reproducibility is structural**: the manifest makes every output
  traceable; re-running the pipeline on the same input reproduces it
  byte for byte.
- **Scales without rewriting**: the streaming kernels take 10× the data
  without 10× the memory (`benchmarks/perf/baseline.md`).

## What you lose (honest)

- **Arbitrary code**: a pipeline step set is finite by design. Anything
  bespoke stays in Python — load the pipeline's `cleaned.parquet` output
  and continue in pandas (`.to_pandas()` is guaranteed forever).
- The pipeline runner is engine-side: custom Python model families run
  via `ti.run_pipeline` (the Python orchestrator), not `ti360 run`.
