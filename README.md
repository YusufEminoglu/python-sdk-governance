<div align="center">

<img src="docs/icons/logo.svg" width="128" height="128" alt="Python Spatial SDK Hub Logo" style="filter: drop-shadow(0 12px 24px rgba(16,185,129,0.3));"/>

# GeoAI & Spatial Python SDK Ecosystem Hub

**Unified Governance, Telemetry & Interactive Portfolio Studio for 8 Pure-Python Spatial Intelligence Packages.**

[![Live Dashboard](https://img.shields.io/badge/Live_Dashboard-GitHub_Pages-06b6d4?logo=github)](https://geophilo.com/sdk-governance/)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-10b981?logo=python)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Packages](https://img.shields.io/badge/PyPI%20Packages-8%20Active-f59e0b)](https://pypi.org/user/yusuf.eminoglu/)

<br/>

👉 **[Explore the Live Interactive Master Dashboard](https://geophilo.com/sdk-governance/)**

</div>

---

## 📖 Overview

This repository is the single source of truth for a portfolio of eight pure-Python
geospatial and GeoAI SDKs. A single generator script turns a hand-maintained registry
plus live PyPI / GitHub telemetry into a static, self-contained governance dashboard.

The generated page is a zero-backend HTML application that ships with:

| Dashboard tab | What it shows |
| :--- | :--- |
| **Executive Cockpit** | KPI cards (LOC, downloads, algorithms, wheel size, releases) and four Chart.js visualizations. |
| **Portfolio Telemetry** | Sortable, searchable package table with per-package drill-down, license, version and action links. |
| **Econometric Forecasting** | Bass diffusion and Gompertz S-curve projections of ecosystem adoption through 2027. |
| **Quality & Benchmarks** | Coverage, memory, throughput, CI status and security audit matrix. |
| **Neural Architecture** | Interactive HTML5 Canvas topology of the ecosystem data flow. |
| **Developer REPL Studio** | Copy-ready, syntax-checked code samples for every SDK. |

Everything is emitted to `docs/`, which is deployed directly by GitHub Pages. No
database, server, or client-side build step is involved.

---

## 🌟 The 8 Pure-Python Geospatial SDKs

| SDK Package | PyPI Project | License | Primary Capabilities |
| :--- | :--- | :--- | :--- |
| **`geoai2analytics-sdk`** | [![PyPI](https://img.shields.io/pypi/v/geoai2analytics-sdk)](https://pypi.org/project/geoai2analytics-sdk/) | MIT | 81 spatial statistics & econometrics algorithms, Moran's I, LISA, GWR/MGWR, Spatial SHAP. |
| **`multilayer-sdk`** | [![PyPI](https://img.shields.io/pypi/v/multilayer-sdk)](https://pypi.org/project/multilayer-sdk/) | MIT | Synchronized 2–8 panel map grids, real-time laser crosshairs, curtain swipe changer. |
| **`myface2city`** | [![PyPI](https://img.shields.io/pypi/v/myface2city)](https://pypi.org/project/myface2city/) | MIT | Optical urban portrait engine, variable-radius vector stippling, OSM client, SVG exporter. |
| **`NCZ2Geo`** | [![PyPI](https://img.shields.io/pypi/v/NCZ2Geo)](https://pypi.org/project/NCZ2Geo/) | GPL-2.0-or-later | Proprietary Netcad NCZ/NCA parser, PlanGML zoning identity, official e-Plan symbology. |
| **`cad2geo`** | [![PyPI](https://img.shields.io/pypi/v/cad2geo)](https://pypi.org/project/cad2geo/) | GPL-2.0-or-later | High-speed binary CAD block decompressor, coordinate reprojector, and GeoJSON engine. |
| **`osm2threejs`** | [![PyPI](https://img.shields.io/pypi/v/osm2threejs)](https://pypi.org/project/osm2threejs/) | MIT | Headless 3D procedural city generation into Three.js WebGL scenes, glTF/GLB & OBJ. |
| **`zero2route3d-sdk`** | [![PyPI](https://img.shields.io/pypi/v/zero2route3d-sdk)](https://pypi.org/project/zero2route3d-sdk/) | MIT | 3D DEM slope kinematics, Minetti metabolic energy routing, HMM Viterbi map-matching. |
| **`planx-sdk`** | [![PyPI](https://img.shields.io/pypi/v/planx-sdk)](https://pypi.org/project/planx-sdk/) | MIT | Spatial planning MCDA (AHP/TOPSIS/ARAS/COPRAS), 28 urban resilience indices, cellular automata. |

---

## ⚡ Quick Multi-Install

```bash
pip install geoai2analytics-sdk multilayer-sdk myface2city NCZ2Geo cad2geo osm2threejs zero2route3d-sdk planx-sdk
```

Each package can also be installed on its own, for example:

```bash
pip install cad2geo
```

---

## 🚀 Running the Hub Locally

### Requirements

- **Python 3.12+** (the generator uses nested f-strings with escapes).
- Network access is *optional* but recommended; it enables live PyPI and download
  statistics.
- The [GitHub CLI](https://cli.github.com/) (`gh`) is *optional*; when authenticated it
  adds star, fork and issue counts.

### Generate the dashboard

```bash
git clone https://github.com/YusufEminoglu/pypi_sdk_governance.git
cd pypi_sdk_governance

# Regenerate docs/index.html and append today's telemetry snapshot
python generate_pypi_hub.py
```

The command is idempotent per day: an existing snapshot for the current UTC date is
replaced rather than duplicated. The script always exits successfully — a failed
network call falls back to safe defaults and is reported in the console.

### Preview the result

```bash
python -m http.server 8000 --directory docs
# then open http://localhost:8000/
```

You can also open `docs/index.html` directly in a browser; assets are either inline
or referenced from CDNs.

---

## 🗂 Repository Layout

```text
pypi_sdk_governance/
├── generate_pypi_hub.py     # Registry + telemetry collector + HTML generator
├── sdk_history.json         # Rolling 90-day telemetry snapshots
├── docs/
│   ├── index.html           # Generated dashboard (do not edit by hand)
│   ├── .nojekyll            # Disable Jekyll processing on Pages
│   └── icons/               # Favicon and logo
├── tests/
│   └── test_registry.py     # Static registry & telemetry integrity tests
├── .github/workflows/
│   └── daily_sync.yml       # Nightly regenerate + GitHub Pages deploy
├── pyproject.toml           # Ruff and pytest configuration
├── README.md
└── LICENSE
```

> **Note:** `docs/index.html` is generated output. Edit `generate_pypi_hub.py` and
> re-run it instead of patching the HTML directly.

---

## 🧩 How the Registry Works

`SDK_REGISTRY` in `generate_pypi_hub.py` is the only hand-maintained source of package
metadata. Each entry must provide:

| Field | Purpose |
| :--- | :--- |
| `id` | Stable slug used by the dashboard and modal lookups. |
| `name`, `pypi`, `gh_repo` | Display name, canonical PyPI project, GitHub repository. |
| `category`, `tagline` | Grouping and one-line description. |
| `color`, `color_glow`, `gradient` | Per-package visual identity. |
| `license` | SPDX-style license identifier (must match the SDK's `pyproject.toml`). |
| `docs_url`, `pypi_url`, `github_url`, `gitlab_url` | Outbound links. |
| `pip` | Copy-ready install command (`pip install <pypi>`). |
| `algorithms_count` | Number of documented algorithms/engines. |
| `pure_python`, `ci_status`, `coverage`, `benchmark_speed`, `memory_overhead` | Quality and benchmark claims. |
| `bass_m`, `bass_p`, `bass_q` | Bass diffusion parameters used by the forecast tab. |
| `highlights` | Bullet list shown in the detail modal. |
| `repl_example` | Valid Python snippet rendered in the REPL tab. |

To add a new SDK:

1. Append a complete entry to `SDK_REGISTRY`.
2. Add the repository to `local_dir_mapping` so source LOC can be scanned.
3. Add any new category filter to the `filter-pills` markup.
4. Run `python -m pytest -q` — the registry tests will flag missing keys or
   duplicate identifiers.

### Telemetry history schema

`sdk_history.json` is a list of daily snapshots:

```json
[
  {
    "date": "2026-09-06",
    "timestamp": "2026-09-06T17:10:43.924042+00:00",
    "packages": {
      "cad2geo": {
        "version": "0.12.1",
        "downloads_month": 0,
        "stars": 0,
        "releases": 4,
        "pypi_size_kb": 76.1,
        "real_loc": 5507
      }
    }
  }
]
```

Snapshots are ordered chronologically and capped at 90 entries.

---

## 🤖 Automation

`.github/workflows/daily_sync.yml` runs every day at 00:00 UTC (and on pushes to
`main`):

1. Checks out the repository and installs Python 3.13.
2. Installs the pinned `ruff` and `pytest` versions and runs the lint/format/test gate.
3. Runs `python generate_pypi_hub.py`.
4. Commits `docs/index.html` when telemetry changed.
5. Uploads `docs/` as a GitHub Pages artifact and deploys it.

No secrets are required. GitHub statistics rely on the workflow token; local runs can
use the `gh` CLI for richer data.

---

## 🧪 Development & Quality Checks

```bash
python -m pip install pytest ruff

# Static integrity tests for the registry and telemetry log
python -m pytest -q

# Lint and formatting
python -m ruff check .
python -m ruff format --check .
```

The test suite deliberately **does not execute** `generate_pypi_hub.py`; it parses the
module with `ast` so tests remain fast and work offline. It verifies:

- exactly eight packages and unique identifiers;
- required registry fields, install commands and URL conventions;
- registry licenses against the expected upstream values;
- that every REPL snippet is syntactically valid Python;
- `sdk_history.json` structure, ordering and retention limit.

---

## 📜 License

The governance hub, documentation, and generator are released under the **MIT
License** (see [`LICENSE`](LICENSE)). Individual SDK packages retain their own
licenses, as listed in the table above.
