# Declarative pipelines and provenance

A pipeline is a YAML document (`schemas/pipeline.json`) executed by the
core engine — the same run from the CLI, Python or R produces a
**byte-identical provenance manifest** (CI-compared):

```yaml
format: ti360.pipeline/v1
name: monthly-loops
input: loops.csv
steps:
  - step: validate
  - step: health
  - step: resample
    params: { freq_seconds: 900 }
  - step: impute
    params: { model: ti360/impute-saits-mini }
  - step: advise
  - step: report
    params: { title: June report, out: report.html }
  - step: write
    params: { out: cleaned.parquet }
```

```bash
ti360 run pipeline.yaml --out out/
```

```python
manifest = ti.run_yaml_pipeline("pipeline.yaml", out_dir="out")
```

```r
manifest <- ti_run_pipeline("pipeline.yaml", out_dir = "out")
```

## The provenance manifest

Every run writes `run_manifest.json`: the input's sha256 (for bundles,
of their manifest), the pipeline document's own sha256, the engine
version, and each step's parameters and canonical result summary. No
wall-clock fields — the manifest is deterministic, so identical inputs
reproduce identical manifests byte for byte.

## Scaling

The engine's streaming kernels take 10× the data without 10× the memory
(committed measurement: 1.29× peak memory at 10× rows —
[performance](../performance.md)); zoo imputation parallelizes across
measure columns with a deterministic merge.
