# TrafficInsight360

One multimodal traffic-analysis platform, three languages, **one engine**:
everything that computes — kernels, validation, the Advisor, report
rendering, pretrained-model inference — lives in a shared Rust core, so
Python, R and the `ti360` CLI produce byte-identical results (enforced in
CI). Datasets are typed with construction-time invariants, travel as
self-describing `.ti360` bundles, carry a Data Health Score, and every
pipeline run writes a provenance manifest.

```{toctree}
:maxdepth: 2
:caption: Getting started

getting-started/python
getting-started/r
getting-started/cli
```

```{toctree}
:maxdepth: 2
:caption: Tutorials

tutorials/index
case-study/index
```

```{toctree}
:maxdepth: 2
:caption: User guide

user-guide/modalities
user-guide/bundles
user-guide/network
user-guide/advisor
user-guide/model-zoo
user-guide/privacy
user-guide/reports
user-guide/pipelines
```

```{toctree}
:maxdepth: 1
:caption: Adoption

migration/movingpandas
migration/gtfs
migration/pandas_script
performance
```

```{toctree}
:maxdepth: 1
:caption: Reference

api/python
architecture/index
contributing
changelog
```
