# Quickstart — R

```r
# r-universe first; CRAN later
install.packages("trafficinsight360r",
                 repos = "https://j-ijaradar.r-universe.dev")
```

The package builds the same Rust core Python and the CLI use — results
are byte-identical across all three (CI-compared).

```r
library(trafficinsight360r)

ds <- ti_load("loop_sensors.csv")      # typed dataset, profile-classified
ti_health(ds)$score                    # Data Health Score

recs <- ti_advise(ds)                  # deterministic, offline
print(recs)                            # pitfalls rank first

ti_report(ds, "report.html")           # IR rendered by the core renderer

manifest <- ti_run_pipeline("pipeline.yaml", out_dir = "out")
```

Short alias for interactive use: `ti360$advise(...)`, `ti360$health(...)`,
`ti360$zoo$load_pretrained(...)`.

## Bridges

`ti_as_tibble()`, `ti_as_sf()` and `ti_as_tsibble()` hand your data to
the tidyverse/sf/tsibble ecosystems at any point — adoption is
reversible. The full walkthrough is the package vignette
(`vignette("quickstart", package = "trafficinsight360r")`), which
reproduces the Python quickstart on the same CSV.
