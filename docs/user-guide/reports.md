# Reports as data

Reports are a versioned, language-neutral JSON IR
(`schemas/report_ir.json`): sections of typed blocks — `heading`,
`paragraph`, `key_value_grid`, `table`, `figure`, `callout`,
`code_block`, `insight` and a `raw_html` compatibility block. HTML and
Markdown render **in the core** (minijinja templates, external CSS), so
Python, R and the CLI produce the same document; PDF renders via
Playwright/WeasyPrint over the HTML, DOCX via pandoc from Markdown.

## Python: the fluent builder

```python
from trafficinsight360 import ReportBuilder

report = (
    ReportBuilder(ds, title="June loops")
    .add_overview()
    .add_missing_analysis()
    .add_advisor()                 # recommendations as insight blocks
    .build()
)
report.save("report.html")
report.save_ir("report_ir.json")   # lossless round-trip
```

## CLI and R

```bash
ti360 render report_ir.json --to html --out report.html
```

```r
ti_report(ds, "report.html")       # quickstart IR + core renderer
ti_render(ir_list, to = "md")
```

## AI text is always labeled

`insight` blocks carry `default_text` (deterministic, always present),
optional `ai_text`, and a `source_label` (`computed | kb | ai | hybrid`).
Renderers **must** label AI text "AI-generated" — this is enforced by the
core renderer, not left to callers.
