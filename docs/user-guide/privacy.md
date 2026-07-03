# Privacy: risk assessment and mitigation

This toolkit is deliberately **not** an "anonymization" toolkit, and that
word does not appear in its API: a handful of spatio-temporal points
re-identifies most individuals (de Montjoye et al. 2013, *Unique in the
Crowd*), so presenting trajectory data as "made safe" would be false
assurance — under GDPR a legal distinction, not just an ethical one.
Spatio-temporal traces of individuals should be treated as personal data
regardless of any treatment applied here.

## Measure the risk

```python
from trafficinsight360 import privacy

report = privacy.assess_reidentification_risk(
    df, entity="vehicle_id", timestamp="timestamp",
    lon="lon", lat="lat", spatial_bin_m=500, temporal_bin="1h",
)
report.uniqueness_curve          # fraction of entities pinned by n points
report.home_work_k_histogram     # k-anonymity of inferred home/work pairs
report.limits                    # mandatory honest-wording statement
```

The uniqueness curve follows the de Montjoye protocol with nested point
draws (monotone by construction); home/work are the most frequent
night-time and daytime cells per entity.

## Apply named mitigations

```python
treated, record = privacy.apply_mitigations(df, [
    ("spatial_cloaking", {"cell_m": 500}),
    ("endpoint_fuzzing", {"n_points": 2}),
    ("aggregation_threshold", {"k": 5, "temporal_bin": "1h"}),
])
record.to_dict()   # what was applied — including what each mitigation
                   # does NOT protect against — for reports & provenance
```

Every mitigation documents its non-protections (cloaking does not hide
movement patterns; endpoint fuzzing does not hide home/work clusters;
k-anonymity does not compose across releases). The record is meant to be
attached to reports and provenance manifests, so downstream users know
the data's treatment history — and its remaining risk.

## GDPR context

Risk assessment supports a DPIA; it does not replace one. Counting-based
releases should combine `aggregation_threshold` with organizational
controls; trajectory-level releases to third parties generally require a
legal basis independent of any mitigation here. When in doubt, the answer
is access control, not data treatment.
