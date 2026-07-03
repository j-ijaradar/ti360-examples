# Python API reference

The public entry points of the `trafficinsight360` package. Rust API docs
live on docs.rs (`trafficinsight360-core`); the R reference ships with the
package (`?ti_advise` etc.).

## Top level

```{eval-rst}
.. automodule:: trafficinsight360
   :members: load, advise, report, run_pipeline, run_yaml_pipeline, engine_info, is_native_available
```

## Advisor

```{eval-rst}
.. automodule:: trafficinsight360.advisor
   :members: Recommendation, RecommendationSet, advise, advise_json, kb_entries
```

## Model zoo

```{eval-rst}
.. automodule:: trafficinsight360.zoo
   :members:
```

## Privacy risk toolkit

```{eval-rst}
.. automodule:: trafficinsight360.privacy
   :members:
```

## Bundles

```{eval-rst}
.. automodule:: trafficinsight360.bundle
   :members:
```
