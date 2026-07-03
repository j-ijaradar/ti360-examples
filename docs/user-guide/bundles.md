# The `.ti360` bundle format

The AnnData lesson: a domain container plus a **self-describing on-disk
format** is what turns a library into an ecosystem. A `.ti360` bundle is
a directory (or zip) of:

```
mydata.ti360/
├── data.parquet      # the table(s)
├── schema.json       # modality, column roles, units, CRS, anchoring
└── manifest.json     # per-file sha256 hashes + provenance
```

Fully self-describing and hash-verified: `ti360 profile data.ti360`,
`ti.load(...)` and `ti_load(...)` reconstruct the identical typed dataset
(byte-compared in CI). It is the platform's interchange format — share
analysis-ready traffic datasets with schema, units and provenance
attached, instead of a CSV plus a README.

```python
ds = ti.load("loops.csv", modality="auto")
ds.save("loops.ti360", provenance={"source": "opendata.dresden.de"})

again = ti.load("loops.ti360")     # identical typed dataset, verified
```

Tampering is detected: a bundle whose file hashes do not match its
manifest refuses to load.

## Provenance

`manifest.json` carries free-form provenance you supply at save time plus
the writing library's version. Pipeline runs (`ti360 run`) reference
bundles by their manifest hash, so every report traces to exact inputs.
