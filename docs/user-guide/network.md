# Network anchoring and map matching

The transport network is a first-class object: any dataset can be
**anchored** to a `NetworkDataset` (loaded from an OSM extract), which is
what makes corridor aggregation, propagation analysis and cross-modal
comparison joins instead of projects.

| Anchoring | Kernel |
|---|---|
| sensor → segment | `snap_points_to_edges` |
| stop → node | `snap_points_to_nodes` |
| trajectory → matched path | HMM map matching (`map_match_osm`) |

## The map-matching claim, stated honestly

Fast map matchers exist — Valhalla/Meili, OSRM `match`, FMM. What did
not exist is an **embeddable, dependency-free library usable identically
from Python, R and a CLI** without running a service. That is what the
core's HMM matcher is: emission probabilities from GPS noise, transition
probabilities from routing distance, Viterbi decoding, all in-process.

```python
ds = ti.load(points_df, modality="trajectory")
matched = ds.map_match("dresden.osm")     # per-point edge assignment
```

Bundled samples include a small OSM extract; the Phase 3 acceptance test
matches the sample trajectories against it with < 30 m residuals.
