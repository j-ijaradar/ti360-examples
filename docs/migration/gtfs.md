# Migrating from gtfs-kit / tidytransit

gtfs-kit (Python) and tidytransit (R) read GTFS feeds into frames/tibbles
per table. TrafficInsight360's `TransitDataset` loads the same zips with
**referential integrity validated at construction** and plugs transit
into the multimodal platform (network anchoring, health score, advisor,
reports). Interop escapes are guaranteed both ways.

## Concept mapping

| gtfs-kit / tidytransit | TrafficInsight360 |
|---|---|
| `gk.read_feed(path)` / `read_gtfs(path)` | `ti.load("feed.zip")` (Python) / `ti_load("feed.zip")` (R) → `TransitDataset` |
| feed validation (`gk.validators`, `validate_gtfs`) | foreign-key validation at construction — a feed with dangling `trip_id`/`stop_id` references **fails to load**, with the violations listed |
| per-table frames (`feed.stops`, `feed.trips`) | `.table("stops")`, `.table("trips")` → pandas/tibble views |
| headway / frequency computations | headway kernels over `stop_times` (identical from Python, R and CLI) |
| stop geometry via shapely/sf | stops→network-node anchoring against an OSM extract (`snap_points_to_nodes`) |

## Worked example

```python
# gtfs-kit
import gtfs_kit as gk
feed = gk.read_feed("vvo.zip", dist_units="km")
problems = gk.validate(feed)

# trafficinsight360 — validation is not optional
import trafficinsight360 as ti
transit = ti.load("vvo.zip")        # raises with FK violations listed
stops = transit.table("stops")      # pandas whenever you want it
```

```r
# tidytransit
gtfs <- read_gtfs("vvo.zip")

# trafficinsight360r
transit <- ti_load("vvo.zip")
```

## Why switch

- **Integrity is enforced, not advisory** — downstream analyses can rely
  on referential validity instead of re-checking it.
- **Cross-modal analysis**: anchored stops share the network with loop
  detectors and trajectories, so corridor comparisons across modes are a
  join, not a project.
- **Same numbers in Python and R** — for a bilingual transit team, the
  byte-parity guarantee removes a whole class of "the R script says
  something else" discussions.

## What you lose (honest)

- gtfs-kit's **feed editing/writing** (we read and validate; we do not
  yet write modified feeds).
- tidytransit's **service-pattern helpers** and gtfs-kit's **map plots**
  — reproduce via the table escapes for now.
- Community recipes specific to those packages.
