# Sphinx configuration for the TrafficInsight360 documentation site
# (Read the Docs; see .readthedocs.yaml at the repository root).

import os
import sys

sys.path.insert(0, os.path.abspath("../py/trafficinsight360"))

project = "TrafficInsight360"
author = "Jyotirmaya Ijaradar"
copyright = "2026, Jyotirmaya Ijaradar"  # noqa: A001
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

myst_enable_extensions = ["colon_fence", "deflist", "fieldlist"]
myst_heading_anchors = 3

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    # compiled into the site via include shims (architecture/, changelog)
    # rather than as standalone pages
    "README.md",
    "architecture.md",
    "data_contract.md",
    "FEATURES.md",
    "ui_architecture.md",
    "REDESIGN_AND_ADVISOR_PLAN.md",
]

html_theme = "furo"
html_title = "TrafficInsight360"
html_static_path = []

# The compiled core is optional at docs-build time: the package falls back
# gracefully, and heavy optional deps are mocked.
autodoc_mock_imports = [
    "matplotlib",
    "scipy",
    "plotly",
    "sklearn",
    "polars",
    "httpx",
]
autodoc_member_order = "bysource"
napoleon_numpy_docstring = True
napoleon_google_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# linkcheck: skip hosts that rate-limit CI and local anchors
linkcheck_ignore = [
    r"https://opendata\.dresden\.de/.*",
    r"https://www\.eco-visio\.net/.*",
    r"https://download\.gtfs\.de/.*",
    r"https://download\.geofabrik\.de/.*",
    r"http://localhost.*",
    r"https://github\.com/j-ijaradar/trafficinsight360-dev.*",
]
linkcheck_timeout = 15
