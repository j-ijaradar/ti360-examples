# The Advisor

A hybrid recommendation engine whose deterministic parts live in the
core: a dataset **fingerprint** (modality, sizes, frequency, missingness
rate and pattern, seasonality, trend, outliers, spatial extent, health
score, roles — aggregates only, never rows) is matched against a YAML
**knowledge base** with declarative conditions (`== != < <= > >= in
contains`, no eval). Recommendations carry rationale, confidence and
**citable references**; pitfalls always rank first.

```python
recs = ti.advise("loops.csv")
recs.pitfalls                      # never dropped, always first
recs.to_json()                     # byte-identical to `ti360 advise`
```

## Measured quality, not vibes

The evaluation harness (`benchmarks/advisor/`) compares library defaults,
advisor-recommended pipelines and an exhaustive oracle on three benchmark
datasets with constructed ground truth. The committed report card shows
**+32.8 % mean improvement over defaults with zero advised-below-default
rows**; CI regenerates it on every KB change and fails on regression.

## Authoring KB packs

Packs are YAML files validated against `schemas/kb_entry.json`, layered
`builtin < site < project < user` (later packs override by id):

```yaml
entries:
  - id: site.impute.prefer_seasonal
    kind: preprocessing
    title: Use the seasonal imputer on our loop data
    rationale: Local finding — seasonal imputation wins on our sensors.
    confidence: 0.9
    conditions:
      - { field: modality, op: "==", value: time_series }
      - { field: missingness_rate, op: ">", value: 0 }
    action: { pipeline_step: clean.impute, task: imputation, method: seasonal_imputer }
    references: ["Internal evaluation 2026-05, benchmarks/site_card.md"]
```

```bash
ti360 advise loops.csv --pack site_pack.yaml
```

A CI check ties KB hyperparameter rules to model-registry metadata so
they cannot drift.

## The AI layer (optional, off by default)

The LLM **contract** lives in core — prompt construction (fingerprint +
top KB hits + result summaries, never raw rows; asserted in tests) and
strict response validation — while HTTP lives per language (httpx /
httr2). The KB is the floor: AI may re-rank, annotate (`source: hybrid`)
and add (`source: ai`), but can never remove a pitfall. Offline or
disabled, output is byte-identical to the KB-only run. Every AI sentence
is rendered under an "AI-generated" label.

```python
recs = ti.advise("loops.csv", ai=True,
                 ai_config=ti.AdvisorConfig(enabled=True))
```
