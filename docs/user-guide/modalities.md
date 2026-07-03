# Modalities and typed datasets

A time series is *defined* by its index and key; validity is a container
property, not a convention (the tsibble lesson). Every typed dataset
validates its modality contract **at construction** — a dataset that
violates its invariants cannot exist:

| Dataset | Invariant enforced at construction |
|---|---|
| `TimeSeriesDataset` | (entity, timestamp) unique and sorted |
| `TrajectoryDataset` | per-entity temporal ordering |
| `TripDataset` | `t_start <= t_end`; O/D geo-resolvable |
| `TransitDataset` | GTFS referential integrity (dangling FK ⇒ load fails) |
| `EventDataset` | point/interval well-formedness |
| `NetworkDataset` | graph consistency (nodes/edges/segments) |

## Classification without regexes

Structural roles (timestamp / entity / measure / geometry) come from the
data; **domain semantics** — which measure is a speed, its unit, its
plausible range — come from declarative modality profiles in
`knowledge/profiles/*.yaml` (`road_sensor`, `bike_share`, `trajectory`,
`gtfs`, `incident`). Alias matching is exact and case-insensitive; no
patterns are evaluated. The same profiles drive Python, R and the CLI.

```python
import trafficinsight360 as ti
ds = ti.load("loops.csv", modality="auto")     # detect + validate
ds = ti.load("loops.csv", modality="road_sensor")  # explicit override
```

```bash
ti360 classify loops.csv
```

## Units and physical validation

Profiles declare units and plausible ranges per measure (speed bounds,
non-negative flows, occupancy 0–100); the validator checks them and the
Data Health Score aggregates completeness, validity, regularity,
uniqueness and cross-measure consistency into one number every report
surfaces and the Advisor consumes.

## ML boundary

`TensorBundle` (dense, named dims `time`/`entity`/`feature`, mask
True=valid) and `RaggedBundle` (values + offsets, mirroring Arrow
ListArray) are the minimal, stable protocol between datasets and model
code — the PyTorch-Dataset lesson.
