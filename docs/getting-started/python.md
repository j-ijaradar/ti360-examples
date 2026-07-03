# Quickstart — Python

```bash
pip install trafficinsight360
```

Binary wheels ship for Linux/macOS/Windows (x86_64 + aarch64) with the
compiled core included; a bounded pure-Python fallback covers only the
Phase 1 kernel surface and is removed at v1.0.

## Load, validate, get advice

```python
import trafficinsight360 as ti

ds = ti.load("loop_sensors.csv", modality="auto")   # typed dataset

recs = ti.advise("loop_sensors.csv")                 # deterministic, offline
print(recs.summary())                                # pitfalls rank first
```

The Advisor is a fingerprint + YAML knowledge base evaluated in the core;
every recommendation carries rationale, confidence and citable
references. Pretrained zoo models appear only when your data falls inside
a model card's declared domain.

## Health, reports, pipelines

```python
from trafficinsight360.native import get_native
import json

health = json.loads(get_native().health(path="loop_sensors.csv"))
print(health["score"])                               # Data Health Score

manifest = ti.run_yaml_pipeline("pipeline.yaml", out_dir="out")
```

Reports are language-neutral JSON IR rendered by the core (`ReportBuilder`
keeps its fluent API and exports html/pdf/docx/md/ir); pipeline runs write
`run_manifest.json` with input hashes and per-step results.

## Pretrained models (opt-in)

```python
model = ti.models.load_pretrained("ti360/impute-saits-mini")
print(model.limits)                # read the card before trusting output
filled, summary = model.impute("loop_sensors.csv")
```

## Leave whenever you want

`.to_pandas()` / `.to_polars()` always work — adoption is reversible.
