# Migrating from movingpandas

movingpandas is a mature trajectory library on the GeoPandas stack. This
guide maps its concepts to TrafficInsight360, says concretely why you
would switch — and what you lose. Adoption is reversible: `.to_pandas()`
always works, and an sf/GeoPandas frame is one call away.

## Concept mapping

| movingpandas | TrafficInsight360 |
|---|---|
| `mpd.Trajectory` / `TrajectoryCollection` | `TrajectoryDataset` (`ti.load(df, modality="trajectory")`) — per-entity temporal ordering is a construction-time invariant, not a convention |
| `traj.add_speed()`, `add_direction()` | `TrajectoryDataset.with_speed_heading()` (per-point speed m/s + heading deg, computed in the Rust core) |
| `mpd.DouglasPeuckerGeneralizer` | `TrajectoryDataset.simplify()` (Douglas-Peucker in core) |
| `mpd.TrajectoryStopDetector` | `TrajectoryDataset.stay_points()` (distance + min-duration) |
| OD analysis via start/end points | `TrajectoryDataset.extract_od()` → OD table |
| map matching (external services) | **embeddable HMM map-matching in core** (`map_match_osm`) — no Valhalla/OSRM service to run |
| `traj.df` (escape to pandas) | `.to_pandas()` / `.to_polars()` (guaranteed) |

## Worked example

```python
# movingpandas
import movingpandas as mpd
traj = mpd.Trajectory(gdf, traj_id_col="vehicle_id", t="timestamp")
traj.add_speed()

# trafficinsight360
import trafficinsight360 as ti
ds = ti.load(df, modality="trajectory")   # validates ordering at construction
enriched = ds.with_speed_heading()        # per-point speed + heading (core)
matched = ds.map_match("dresden.osm")     # embeddable, no service
```

## Why switch

- **Validity by construction**: a `TrajectoryDataset` cannot exist with
  out-of-order points per entity; with movingpandas that's your
  discipline.
- **One engine, three languages**: the same kernels give identical
  numbers from Python, R and the `ti360` CLI (byte-compared in our CI).
- **Map-matching without a service**: HMM matching runs in-process.
- **The rest of the platform**: Data Health Score, the Advisor, `.ti360`
  bundles for sharing, reports for free.

## What you lose (honest)

- movingpandas' **rich trajectory generalizers/splitters** (time-gap,
  Douglas-Peucker is here, others are not yet).
- Deep **GeoPandas integration** (any CRS operation, spatial joins) —
  our geometry support is points + network anchoring; for polygon work,
  escape to GeoPandas and come back.
- A large **existing gallery** of examples; ours is younger.

If your work is mostly geometric trajectory manipulation, movingpandas
remains a fine home; bring the data over when you need health scoring,
advice, cross-language parity or the network-anchored analyses.
