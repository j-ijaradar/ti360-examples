# Tutorials

Runnable notebooks live in the repository; the sample-data ones execute
against the committed deterministic samples under `data/samples/` (no
downloads), and `.github/workflows/docs.yml` executes the quickstart
notebook in CI so the tutorials cannot rot.

## Sample-data notebooks (`notebooks/`)

| Notebook | Covers |
|---|---|
| `01_quickstart.ipynb` | load → validate → clean → analyze → report |
| `02_processing_and_analysis.ipynb` | cleaning, transformation, temporal/statistical analysis |
| `03_reporting_html_pdf.ipynb` | report IR, HTML/PDF/DOCX/MD export |
| `04_visualization_dashboard_basics.ipynb` | charts and dashboards |
| `05_zoo_finetune_tutorial.ipynb` | fine-tuning a pretrained zoo model on local data and distributing it through a private registry |

## Real-data recipes

Each recipe states its public source and license, downloads with a pinned
URL, and runs the same typed-dataset pipeline:

- **PeMS / UTD19-class loop archives** — retrain the zoo models with the
  committed pipeline (`zoo/README.md`).
- **NYC Citi Bike** — `TripDataset` with O/D geo-resolution and station
  balance analyses.
- **Public GTFS** (e.g. VVO/DVB) — `TransitDataset` with FK validation,
  headways and stop anchoring.
- **Geolife** — `TrajectoryDataset`, stay points, map matching against an
  OSM extract.

The flagship end-to-end study is the [Carola Bridge case
study](../case-study/index.md).
