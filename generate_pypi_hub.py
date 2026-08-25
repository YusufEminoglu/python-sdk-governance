# -*- coding: utf-8 -*-
"""
Builder for Python Spatial & GeoAI SDK Ecosystem Governance Hub Dashboard.
Generates a master portfolio site with interactive topology, telemetry,
live pip install generator, package comparison matrix, and deep documentation links.
"""

import os
import json
import xml.etree.ElementTree as ET

OUTPUT_DIR = r"C:\Users\YE\PyCharmMiscProject\PyPI\pypi_sdk_governance\docs"
ICONS_DIR = os.path.join(OUTPUT_DIR, "icons")
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

os.makedirs(ICONS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Master Hub Logo SVG
SVG_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08141e"/>
      <stop offset="100%" stop-color="#0e263d"/>
    </linearGradient>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="35%" stop-color="#06b6d4"/>
      <stop offset="70%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#06b6d4" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect x="24" y="24" width="464" height="464" rx="96" fill="url(#bg)" stroke="url(#glow)" stroke-width="6" filter="url(#shadow)"/>

  <!-- Python Dual Snakes intertwined with Spatial Voronoi & Neural Nodes -->
  <g transform="translate(106, 106) scale(0.6)">
    <!-- Top Snake (Cyan/Emerald) -->
    <path d="M 250 50 C 140 50 150 100 150 100 L 150 150 L 250 150 L 250 180 L 110 180 C 110 180 50 170 50 280 C 50 390 110 380 110 380 L 170 380 L 170 300 C 170 300 160 220 250 220 C 340 220 330 300 330 300 L 330 380 L 390 380 C 390 380 450 390 450 280 C 450 170 390 180 390 180 L 330 180 L 330 100 C 330 100 340 50 250 50 Z" fill="#06b6d4" opacity="0.9"/>
    <!-- Bottom Snake (Emerald/Teal) -->
    <path d="M 250 450 C 360 450 350 400 350 400 L 350 350 L 250 350 L 250 320 L 390 320 C 390 320 450 330 450 220 C 450 110 390 120 390 120 L 330 120 L 330 200 C 330 200 340 280 250 280 C 160 280 170 200 170 200 L 170 120 L 110 120 C 110 120 50 110 50 220 C 50 330 110 320 110 320 L 170 320 L 170 400 C 170 400 160 450 250 450 Z" fill="#10b981" opacity="0.9"/>
    <circle cx="190" cy="100" r="16" fill="#08141e"/>
    <circle cx="310" cy="400" r="16" fill="#08141e"/>
  </g>

  <!-- Hexagonal Spatial Framework Rings -->
  <polygon points="256,70 376,139 376,278 256,347 136,278 136,139" fill="none" stroke="#06b6d4" stroke-width="2.5" stroke-dasharray="6 4" opacity="0.6"/>
  <circle cx="256" cy="70" r="6" fill="#10b981"/>
  <circle cx="376" cy="139" r="6" fill="#06b6d4"/>
  <circle cx="376" cy="278" r="6" fill="#3b82f6"/>
  <circle cx="256" cy="347" r="6" fill="#a855f7"/>
  <circle cx="136" cy="278" r="6" fill="#f59e0b"/>
  <circle cx="136" cy="139" r="6" fill="#ef4444"/>

  <!-- Badge -->
  <rect x="120" y="420" width="272" height="42" rx="21" fill="#0b1320" stroke="url(#glow)" stroke-width="2.5"/>
  <text x="256" y="446" font-family="'Plus Jakarta Sans', 'Inter', sans-serif" font-size="14.5" font-weight="800" fill="#34d399" text-anchor="middle" letter-spacing="1.5">PYTHON SDK &#183; ECOSYSTEM</text>
</svg>"""

ET.fromstring(SVG_LOGO)

with open(os.path.join(ICONS_DIR, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(SVG_LOGO)
with open(os.path.join(ICONS_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(SVG_LOGO)
with open(os.path.join(OUTPUT_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("# Disable Jekyll\n")


# 2. Complete 8-SDK Metadata Registry
SDKS_DATA = [
    {
        "id": "geoai2analytics",
        "name": "geoai2analytics-sdk",
        "pypi": "geoai2analytics-sdk",
        "version": "0.1.0",
        "category": "Spatial Statistics & GeoAI",
        "tagline": "Pure-Python Spatial Statistics, Econometrics (GWR/MGWR/SAR) & Explainable GeoAI (Spatial SHAP).",
        "color": "#10b981",
        "gradient": "linear-gradient(135deg, #10b981, #06b6d4)",
        "license": "MIT",
        "docs_url": "https://yusufeminoglu.github.io/geoai2analytics-sdk/",
        "pypi_url": "https://pypi.org/project/geoai2analytics-sdk/",
        "github_url": "https://github.com/YusufEminoglu/geoai2analytics-sdk",
        "pip": "pip install geoai2analytics-sdk",
        "highlights": [
            "81 Scientific Algorithm Cards with LaTeX MathJax Proofs",
            "Global Moran's I, LISA, Getis-Ord Gi*, Geary's C, Ripley's K",
            "Spatial Econometrics: OLS, SAR (Lag), SEM (Error), SDM (Durbin)",
            "GWR & Multiscale MGWR Golden-Section Bandwidth Kernels",
            "Explainable GeoAI: Spatial SHAP Attribution Maps & Conformal Uncertainty"
        ],
        "metrics": {"algorithms": "81", "pages_equiv": "400+", "tests": "100%", "pure_python": "Yes"}
    },
    {
        "id": "multilayer",
        "name": "multilayer-sdk",
        "pypi": "multilayer-sdk",
        "version": "0.1.1",
        "category": "Multi-Panel Geovisualization",
        "tagline": "Synchronized Multi-Panel Map Visualization, Real-Time Laser Crosshairs & Curtain Swipe Engine.",
        "color": "#06b6d4",
        "gradient": "linear-gradient(135deg, #06b6d4, #3b82f6)",
        "license": "MIT",
        "docs_url": "https://yusufeminoglu.github.io/multilayer-sdk/",
        "pypi_url": "https://pypi.org/project/multilayer-sdk/",
        "github_url": "https://github.com/YusufEminoglu/multilayer-sdk",
        "pip": "pip install multilayer-sdk",
        "highlights": [
            "2, 3, 4, 6, 8 Synchronized Panel Grids (1x2, 2x1, 1x3, 2x2, 2x3, 2x4)",
            "Bi-directional Real-Time Pan & Zoom Broadcasting",
            "Neon Laser Crosshair Cursor Tracking Across All Viewports",
            "Draggable Split-Screen Curtain Swipe Slider (SwipeMap)",
            "Quantiles, Equal Interval, Natural Breaks Choropleth Engine",
            "Single-File Standalone Interactive HTML Dashboard Exporter"
        ],
        "metrics": {"grids": "6", "basemaps": "8+", "laser_sync": "Active", "pure_python": "Yes"}
    },
    {
        "id": "myface2city",
        "name": "myface2city",
        "pypi": "myface2city",
        "version": "0.1.1",
        "category": "Generative Spatial Art",
        "tagline": "Turn urban street networks, building footprints, and vector maps into live optical portrait art.",
        "color": "#f43f5e",
        "gradient": "linear-gradient(135deg, #f43f5e, #a855f7)",
        "license": "MIT",
        "docs_url": "https://yusufeminoglu.github.io/MyFace2City/",
        "pypi_url": "https://pypi.org/project/myface2city/",
        "github_url": "https://github.com/YusufEminoglu/MyFace2City",
        "pip": "pip install myface2city",
        "highlights": [
            "UrbanPortrait Luminance Sampling with Aspect-Ratio Auto-Fitting",
            "10 Curated Artistic Presets (Cyberpunk 2077, Blueprint, Neon, Vintage)",
            "Algorithmic Halftone Engraving & Variable-Radius Vector Stippling",
            "Built-in OpenStreetMap Overpass API Network Client",
            "Scalable Standalone Vector SVG Poster Exporter"
        ],
        "metrics": {"presets": "10", "stippling": "Active", "svg_render": "60 FPS", "pure_python": "Yes"}
    },
    {
        "id": "ncz2geo",
        "name": "NCZ2Geo",
        "pypi": "NCZ2Geo",
        "version": "0.1.0",
        "category": "CAD / Netcad & Planning",
        "tagline": "Pure-Python Netcad NCZ/NCA reader with PlanGML identity and e-Plan symbology metadata.",
        "color": "#38bdf8",
        "gradient": "linear-gradient(135deg, #38bdf8, #6366f1)",
        "license": "GPL-2.0-or-later",
        "docs_url": "https://yusufeminoglu.github.io/NCZ2Geo/",
        "pypi_url": "https://pypi.org/project/NCZ2Geo/",
        "github_url": "https://github.com/YusufEminoglu/NCZ2Geo",
        "pip": "pip install NCZ2Geo",
        "highlights": [
            "Proprietary Netcad NCZ/NCA Binary CAD Stream Parsing",
            "PlanGML Tabaka Sınıflandırma & MPYY Hiyerarşik Eşleştirme",
            "e-Plan Resmi Renk, Dolgu, Çizgi & Tarama Semboloji Atama",
            "Selective Layer Decoding with Local Indexed Caching",
            "Emits Standards-Compliant Enriched GeoJSON Features"
        ],
        "metrics": {"throughput": "296k ent/s", "plangml": "100%", "eplan": "Official", "pure_python": "Yes"}
    },
    {
        "id": "cad2geo",
        "name": "cad2geo",
        "pypi": "cad2geo",
        "version": "0.1.0",
        "category": "CAD / Netcad & Planning",
        "tagline": "High-Performance Netcad NCZ/NCA binary CAD parser, decompression, and GeoJSON engine.",
        "color": "#3b82f6",
        "gradient": "linear-gradient(135deg, #3b82f6, #06b6d4)",
        "license": "GPL-3.0-or-later",
        "docs_url": "https://yusufeminoglu.github.io/cad2geo/",
        "pypi_url": "https://pypi.org/project/cad2geo/",
        "github_url": "https://github.com/YusufEminoglu/cad2geo",
        "pip": "pip install cad2geo",
        "highlights": [
            "Zero-C Pure-Python Huffman / Inflate Binary CAD Decompressor",
            "Parses Points, Lines, Polylines, Text Labels, Arcs, and Hatches",
            "Coordinate Transformation (ITRF96 / TM30 / ED50 to WGS84)",
            "Headless High-Throughput Batch Processing & CLI"
        ],
        "metrics": {"engine": "NCZ v2", "speed": "3.8 ms parse", "format": "GeoJSON", "pure_python": "Yes"}
    },
    {
        "id": "osm2threejs",
        "name": "osm2threejs",
        "pypi": "osm2threejs",
        "version": "0.1.0",
        "category": "3D & WebGL Geovisualization",
        "tagline": "Headless 3D City Generator from OpenStreetMap into Three.js WebGL, glTF/GLB & Wavefront OBJ.",
        "color": "#a855f7",
        "gradient": "linear-gradient(135deg, #a855f7, #ec4899)",
        "license": "MIT",
        "docs_url": "https://yusufeminoglu.github.io/osm2threejs/",
        "pypi_url": "https://pypi.org/project/osm2threejs/",
        "github_url": "https://github.com/YusufEminoglu/osm2threejs",
        "pip": "pip install osm2threejs",
        "highlights": [
            "Procedural 3D Building Extrusions (Pitched, Mansard, Flat Roofs)",
            "Dynamic Road Ribbons, Traffic Lanes, and Street Trees",
            "Waterbody Bathymetry & Terrain Mesh Integration",
            "Exports Three.js WebGL Scene, glTF / GLB, Wavefront OBJ & 3D GeoJSON",
            "In-Browser First-Person Walk / Fly Mode Camera Navigation"
        ],
        "metrics": {"render": "Three.js", "formats": "glTF/OBJ", "fps": "60 FPS", "pure_python": "Yes"}
    },
    {
        "id": "zero2route3d",
        "name": "zero2route3d_sdk",
        "pypi": "zero2route3d_sdk",
        "version": "0.1.0",
        "category": "Routing & 3D Kinematics",
        "tagline": "Headless 3D spatial mobility, biomechanical kinematics, and metabolic energy routing engine.",
        "color": "#f59e0b",
        "gradient": "linear-gradient(135deg, #f59e0b, #ef4444)",
        "license": "GPL-3.0-or-later",
        "docs_url": "https://yusufeminoglu.github.io/zero2route3d_sdk/",
        "pypi_url": "https://pypi.org/project/zero2route3d_sdk/",
        "github_url": "https://github.com/YusufEminoglu/zero2route3d_sdk",
        "pip": "pip install zero2route3d_sdk",
        "highlights": [
            "Tobler's Hiking Function & Minetti Metabolic Energy Modeling",
            "15 Distinct Multimodal Routing Profiles (Pedestrian, Cycling, Cargo, Wheelchair)",
            "DEM Terrain Slope Penalties & 3D Elevation Profiles",
            "Pareto Multi-Criteria Optimization (Time vs Slope vs Distance vs Caloric Burn)",
            "Hidden Markov Model (HMM) Viterbi Map-Matching for GPS Traces"
        ],
        "metrics": {"profiles": "15", "kinematics": "Minetti", "elevation": "3D DEM", "pure_python": "Yes"}
    },
    {
        "id": "planx",
        "name": "planx_sdk",
        "pypi": "planx_sdk",
        "version": "0.1.0",
        "category": "Spatial Planning & MCDA",
        "tagline": "Core geospatial, spatial statistics, MCDA, and urban resilience engines for the PlanX suite.",
        "color": "#10b981",
        "gradient": "linear-gradient(135deg, #10b981, #3b82f6)",
        "license": "GPL-3.0-or-later",
        "docs_url": "https://yusufeminoglu.github.io/planx_sdk/",
        "pypi_url": "https://pypi.org/project/planx_sdk/",
        "github_url": "https://github.com/YusufEminoglu/planx_sdk",
        "pip": "pip install planx_sdk",
        "highlights": [
            "Multi-Criteria Decision Analysis (AHP, TOPSIS, VIKOR, ELECTRE)",
            "28 Urban Resilience, Hazard Susceptibility & Climate Stress Indices",
            "Spatial Cellular Automata Urban Growth Simulation",
            "Isochronic 15-Minute City Walkability & Spatial Justice Metrics",
            "Unified Spatial Planning Data Schema for Turkey & Global Cities"
        ],
        "metrics": {"tools": "40+", "mcda": "AHP/TOPSIS", "resilience": "28 Tools", "pure_python": "Yes"}
    }
]

# 3. Master Dashboard HTML Template
HTML_DASHBOARD = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GeoAI & Spatial Python SDK Ecosystem Hub · Enterprise Portfolio Studio</title>
<meta name="description" content="Master portfolio and governance studio for 8 pure-Python spatial intelligence, spatial statistics, econometrics, CAD, 3D WebGL, and generative cartography SDKs.">
<meta name="keywords" content="python, pypi, gis, geospatial, geoai, spatial-statistics, gwr, lisa, morans-i, cad, netcad, 3d-city, threejs, routing, kinematics, mcda, urban-planning">
<meta name="author" content="Yusuf Eminoğlu">

<!-- OpenGraph & Twitter Cards -->
<meta property="og:title" content="GeoAI & Spatial Python SDK Ecosystem Hub · Enterprise Portfolio Studio">
<meta property="og:description" content="Centralized governance hub for 8 open-source, pure-Python geospatial & GeoAI SDKs.">
<meta property="og:url" content="https://yusufeminoglu.github.io/python-sdk-governance/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" type="image/svg+xml" href="icons/favicon.svg">

<!-- Typography & Lucide Icons -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>

<style>
:root {{
  --bg: #07121b;
  --bg-card: #0d1e2e;
  --bg-card-hover: #11283d;
  --border: #1e3a53;
  --border-focus: #10b981;
  --fg: #f1f5f9;
  --fg-heading: #ffffff;
  --muted: #94a3b8;
  --accent-emerald: #10b981;
  --accent-cyan: #06b6d4;
  --accent-blue: #3b82f6;
  --accent-purple: #a855f7;
  --accent-rose: #f43f5e;
  --accent-amber: #f59e0b;
  --gradient-brand: linear-gradient(135deg, #10b981 0%, #06b6d4 50%, #3b82f6 100%);
  --shadow-glow: 0 10px 30px -5px rgba(6, 182, 212, 0.2);
}}

[data-theme="light"] {{
  --bg: #f8fafc;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f5f9;
  --border: #cbd5e1;
  --border-focus: #059669;
  --fg: #1e293b;
  --fg-heading: #0f172a;
  --muted: #64748b;
  --shadow-glow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.6;
  transition: background 0.2s ease, color 0.2s ease;
}}

/* Top App Bar */
#top-bar {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: rgba(11, 28, 44, 0.94);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
  z-index: 1000;
}}

[data-theme="light"] #top-bar {{
  background: rgba(255, 255, 255, 0.94);
}}

.brand-wrap {{
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}}

.brand-badge {{
  background: var(--gradient-brand);
  color: #08111a;
  font-weight: 800;
  font-size: 1.2rem;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 14px rgba(16, 185, 129, 0.5);
  font-family: 'Plus Jakarta Sans', sans-serif;
}}

.brand-text {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 800;
  font-size: 1.35rem;
  letter-spacing: -0.02em;
  background: var(--gradient-brand);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.hub-tag {{
  font-family: 'Fira Code', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  background: rgba(16, 185, 129, 0.15);
  color: var(--accent-emerald);
  border: 1px solid rgba(16, 185, 129, 0.3);
}}

.top-actions {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
}}

.top-btn {{
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 0.85rem;
  border-radius: 8px;
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--muted);
  text-decoration: none;
  background: var(--bg-card);
  border: 1px solid var(--border);
  transition: all 0.15s ease;
  cursor: pointer;
}}

.top-btn:hover {{
  color: var(--fg-heading);
  border-color: var(--accent-emerald);
  transform: translateY(-1px);
}}

.top-btn.primary {{
  background: var(--accent-emerald);
  color: #08111a;
  border-color: transparent;
  font-weight: 700;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
}}

/* Main Container */
#main-container {{
  max-width: 1280px;
  margin: 0 auto;
  padding: calc(60px + 2.5rem) 1.5rem 5rem;
}}

/* Hero Section */
.hero {{
  text-align: center;
  padding: 3rem 1.5rem 2.5rem;
  background: radial-gradient(circle at center, rgba(6, 182, 212, 0.1) 0%, transparent 70%);
  border-radius: 20px;
  border: 1px solid var(--border);
  margin-bottom: 2.5rem;
}}

.hero h1 {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 3rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--fg-heading);
  margin-bottom: 0.5rem;
}}

.hero p.tagline {{
  font-size: 1.2rem;
  color: var(--muted);
  max-width: 860px;
  margin: 0 auto 1.8rem;
}}

/* Aggregate Metric Strip */
.metrics-strip {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
}}

.metric-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  text-align: center;
  transition: all 0.2s ease;
}}

.metric-card:hover {{
  border-color: var(--accent-cyan);
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow);
}}

.metric-val {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--accent-emerald);
  line-height: 1.1;
  margin-bottom: 0.25rem;
}}

.metric-label {{
  font-size: 0.85rem;
  color: var(--muted);
  font-weight: 500;
}}

/* Filter & Search Bar */
.controls-bar {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1rem 1.25rem;
  margin-bottom: 2rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}}

.search-input-wrap {{
  position: relative;
  flex: 1;
  min-width: 280px;
}}

.search-input {{
  width: 100%;
  padding: 0.6rem 1rem 0.6rem 2.5rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--fg);
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}}

.search-input:focus {{
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.2);
}}

.search-icon {{
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  width: 16px;
  height: 16px;
}}

.filter-pills {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}}

.pill-btn {{
  padding: 0.4rem 0.85rem;
  border-radius: 999px;
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}}

.pill-btn:hover, .pill-btn.active {{
  background: rgba(16, 185, 129, 0.15);
  color: var(--accent-emerald);
  border-color: var(--accent-emerald);
}}

/* SDK Package Cards Grid */
.sdk-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3.5rem;
}}

.sdk-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}}

.sdk-card:hover {{
  background: var(--bg-card-hover);
  border-color: var(--accent-cyan);
  transform: translateY(-4px);
  box-shadow: 0 12px 36px -8px rgba(0, 0, 0, 0.6);
}}

.sdk-card-header {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 1rem;
}}

.sdk-title-wrap h3 {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--fg-heading);
  letter-spacing: -0.01em;
  margin-bottom: 0.2rem;
}}

.sdk-category-badge {{
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 0.2rem 0.55rem;
  border-radius: 6px;
  background: rgba(6, 182, 212, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(6, 182, 212, 0.3);
}}

.sdk-version-badge {{
  font-family: 'Fira Code', monospace;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--accent-emerald);
  background: rgba(16, 185, 129, 0.15);
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  border: 1px solid rgba(16, 185, 129, 0.3);
}}

.sdk-tagline {{
  font-size: 0.92rem;
  color: var(--fg);
  margin-bottom: 1.25rem;
  line-height: 1.5;
}}

/* Pip Command Box */
.pip-box {{
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.55rem 0.85rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'Fira Code', monospace;
  font-size: 0.82rem;
  color: var(--accent-cyan);
  margin-bottom: 1.25rem;
  cursor: pointer;
  transition: border-color 0.15s;
}}

.pip-box:hover {{
  border-color: var(--accent-emerald);
}}

.pip-copy-btn {{
  background: none;
  border: none;
  color: var(--muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: color 0.15s;
}}

.pip-box:hover .pip-copy-btn {{
  color: var(--accent-emerald);
}}

.highlights-list {{
  list-style: none;
  margin-bottom: 1.5rem;
}}

.highlights-list li {{
  font-size: 0.84rem;
  color: var(--muted);
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}}

.highlights-list li i {{
  color: var(--accent-emerald);
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}}

/* Card Action Links */
.card-actions {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  border-top: 1px solid var(--border);
  padding-top: 1.2rem;
}}

.action-btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.45rem 0.75rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.15s ease;
  text-align: center;
}}

.action-btn.docs {{
  background: rgba(16, 185, 129, 0.18);
  color: var(--accent-emerald);
  border: 1px solid rgba(16, 185, 129, 0.35);
}}

.action-btn.docs:hover {{
  background: var(--accent-emerald);
  color: #08111a;
}}

.action-btn.pypi {{
  background: rgba(6, 182, 212, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(6, 182, 212, 0.35);
}}

.action-btn.pypi:hover {{
  background: var(--accent-cyan);
  color: #08111a;
}}

.action-btn.github {{
  background: var(--bg);
  color: var(--muted);
  border: 1px solid var(--border);
  grid-column: span 2;
}}

.action-btn.github:hover {{
  color: var(--fg-heading);
  border-color: var(--muted);
}}

/* Multi-Install Generator Strip */
.installer-strip {{
  background: var(--bg-card);
  border: 1px solid rgba(16, 185, 129, 0.35);
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 3.5rem;
  box-shadow: var(--shadow-glow);
}}

.installer-strip h2 {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--fg-heading);
  margin-bottom: 0.5rem;
}}

.check-matrix {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.75rem;
  margin: 1.25rem 0;
}}

.check-item {{
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.88rem;
  color: var(--fg);
  cursor: pointer;
}}

.check-item input {{
  accent-color: var(--accent-emerald);
  width: 16px;
  height: 16px;
}}

.combined-pip-out {{
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  font-family: 'Fira Code', monospace;
  font-size: 0.9rem;
  color: var(--accent-emerald);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}}

/* Footer */
footer {{
  border-top: 1px solid var(--border);
  padding: 2.5rem 1.5rem;
  text-align: center;
  font-size: 0.85rem;
  color: var(--muted);
}}

footer a {{
  color: var(--accent-emerald);
  text-decoration: none;
}}

footer a:hover {{
  text-decoration: underline;
}}
</style>
</head>
<body>

<header id="top-bar">
  <a href="#" class="brand-wrap">
    <div class="brand-badge">P</div>
    <span class="brand-text">Python Spatial SDK Hub</span>
    <span class="hub-tag">8 Headless Packages</span>
  </a>
  <div class="top-actions">
    <a href="https://github.com/YusufEminoglu" target="_blank" class="top-btn"><i data-lucide="github" style="width:14px;height:14px;"></i> GitHub Profile</a>
    <a href="https://pypi.org/user/yusuf.eminoglu/" target="_blank" class="top-btn"><i data-lucide="package" style="width:14px;height:14px;"></i> PyPI Profile</a>
    <button id="themeToggle" class="top-btn" title="Toggle Theme"><i data-lucide="sun" id="themeIcon" style="width:14px;height:14px;"></i></button>
    <a href="#installer" class="top-btn primary"><i data-lucide="terminal" style="width:14px;height:14px;"></i> Multi-Installer</a>
  </div>
</header>

<div id="main-container">

  <!-- Hero -->
  <section class="hero">
    <h1>GeoAI &amp; Spatial Python SDK Portfolio</h1>
    <p class="tagline">Enterprise Open-Source Suite: Pure-Python Spatial Statistics, Econometrics (GWR/MGWR), CAD Decompression (NCZ/NCA), PlanGML Symbology, 3D WebGL Cities, Kinematic Routing &amp; Synchronized Geovisualization.</p>
  </section>

  <!-- Metrics Counter Strip -->
  <section class="metrics-strip">
    <div class="metric-card">
      <div class="metric-val">8</div>
      <div class="metric-label">Headless Python SDKs</div>
    </div>
    <div class="metric-card">
      <div class="metric-val">100%</div>
      <div class="metric-label">Pure-Python Portability</div>
    </div>
    <div class="metric-card">
      <div class="metric-val">100+</div>
      <div class="metric-label">Spatial &amp; ML Algorithms</div>
    </div>
    <div class="metric-card">
      <div class="metric-val">3.9 &ndash; 3.13</div>
      <div class="metric-label">Multi-OS Matrix CI Passing</div>
    </div>
  </section>

  <!-- Filter & Search Controls -->
  <section class="controls-bar">
    <div class="search-input-wrap">
      <i data-lucide="search" class="search-icon"></i>
      <input type="text" id="pkgSearch" class="search-input" placeholder="Search algorithms, packages (e.g. Moran, GWR, Netcad, Three.js, Swipe)..." autocomplete="off">
    </div>

    <div class="filter-pills">
      <button class="pill-btn active" data-filter="all">All Packages (8)</button>
      <button class="pill-btn" data-filter="Spatial Statistics & GeoAI">GeoAI &amp; Stats</button>
      <button class="pill-btn" data-filter="Multi-Panel Geovisualization">Multi-Panel Maps</button>
      <button class="pill-btn" data-filter="CAD / Netcad & Planning">CAD / Netcad</button>
      <button class="pill-btn" data-filter="3D & WebGL Geovisualization">3D WebGL</button>
      <button class="pill-btn" data-filter="Routing & 3D Kinematics">Routing &amp; Mobility</button>
      <button class="pill-btn" data-filter="Generative Spatial Art">Generative Art</button>
    </div>
  </section>

  <!-- SDK Cards Grid -->
  <section class="sdk-grid" id="sdkGrid">
"""

# Inject Cards HTML
for sdk in SDKS_DATA:
    highlights_html = "".join([f'<li><i data-lucide="check-circle-2"></i> {h}</li>' for h in sdk["highlights"]])
    HTML_DASHBOARD += f"""
    <div class="sdk-card" data-category="{sdk['category']}" data-search="{sdk['name']} {sdk['category']} {sdk['tagline']} {' '.join(sdk['highlights'])}">
      <div>
        <div class="sdk-card-header">
          <div class="sdk-title-wrap">
            <span class="sdk-category-badge">{sdk['category']}</span>
            <h3>{sdk['name']}</h3>
          </div>
          <span class="sdk-version-badge">v{sdk['version']}</span>
        </div>

        <p class="sdk-tagline">{sdk['tagline']}</p>

        <div class="pip-box" onclick="copyText('{sdk['pip']}', this)" title="Click to copy pip command">
          <span><code>{sdk['pip']}</code></span>
          <button class="pip-copy-btn"><i data-lucide="copy" style="width:15px;height:15px;"></i></button>
        </div>

        <ul class="highlights-list">
          {highlights_html}
        </ul>
      </div>

      <div class="card-actions">
        <a href="{sdk['docs_url']}" target="_blank" class="action-btn docs"><i data-lucide="book-open" style="width:14px;height:14px;"></i> Interactive Docs</a>
        <a href="{sdk['pypi_url']}" target="_blank" class="action-btn pypi"><i data-lucide="package" style="width:14px;height:14px;"></i> PyPI Package</a>
        <a href="{sdk['github_url']}" target="_blank" class="action-btn github"><i data-lucide="github" style="width:14px;height:14px;"></i> GitHub Repository</a>
      </div>
    </div>
"""

HTML_DASHBOARD += r"""
  </section>

  <!-- Multi-Package Installer Generator -->
  <section class="installer-strip" id="installer">
    <h2>⚡ Multi-Package Combined Installer</h2>
    <p style="color:var(--muted);font-size:0.92rem;">Select the Python SDKs you need to generate and copy a unified <code>pip install</code> command for your virtual environment or Jupyter notebook:</p>

    <div class="check-matrix" id="checkMatrix">
      <label class="check-item"><input type="checkbox" value="geoai2analytics-sdk" checked> geoai2analytics-sdk</label>
      <label class="check-item"><input type="checkbox" value="multilayer-sdk" checked> multilayer-sdk</label>
      <label class="check-item"><input type="checkbox" value="NCZ2Geo" checked> NCZ2Geo</label>
      <label class="check-item"><input type="checkbox" value="cad2geo" checked> cad2geo</label>
      <label class="check-item"><input type="checkbox" value="osm2threejs" checked> osm2threejs</label>
      <label class="check-item"><input type="checkbox" value="zero2route3d_sdk" checked> zero2route3d_sdk</label>
      <label class="check-item"><input type="checkbox" value="planx_sdk" checked> planx_sdk</label>
      <label class="check-item"><input type="checkbox" value="myface2city" checked> myface2city</label>
    </div>

    <div class="combined-pip-out">
      <code id="combinedPipCmd">pip install geoai2analytics-sdk multilayer-sdk NCZ2Geo cad2geo osm2threejs zero2route3d_sdk planx_sdk myface2city</code>
      <button class="top-btn primary" onclick="copyCombinedPip()"><i data-lucide="copy" style="width:14px;height:14px;"></i> Copy Command</button>
    </div>
  </section>

</div>

<footer>
  <p><strong>GeoAI &amp; Spatial Python SDK Portfolio</strong> &middot; Developed by <a href="https://github.com/YusufEminoglu">Yusuf Eminoğlu</a> &middot; Dokuz Eylül University</p>
  <p style="margin-top:0.4rem;font-size:0.8rem;color:var(--muted);">All 8 SDK packages are independently versioned, open-source under MIT &amp; GPL licenses, and published on PyPI.</p>
</footer>

<script>
lucide.createIcons();

// Theme Toggle
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("pypi_hub_theme", theme);
  if (theme === "light") {
    themeIcon.setAttribute("data-lucide", "moon");
  } else {
    themeIcon.setAttribute("data-lucide", "sun");
  }
  lucide.createIcons();
}

const savedTheme = localStorage.getItem("pypi_hub_theme") || "dark";
setTheme(savedTheme);

themeToggle.addEventListener("click", () => {
  const cur = document.documentElement.getAttribute("data-theme");
  setTheme(cur === "light" ? "dark" : "light");
});

// Copy pip helper
function copyText(text, el) {
  navigator.clipboard.writeText(text).then(() => {
    const original = el.innerHTML;
    el.innerHTML = '<span style="color:#10b981;font-weight:bold;">✓ Copied to clipboard!</span>';
    setTimeout(() => { el.innerHTML = original; lucide.createIcons(); }, 1600);
  });
}

// Search & Filter
const pkgSearch = document.getElementById("pkgSearch");
const cards = document.querySelectorAll(".sdk-card");
const pillBtns = document.querySelectorAll(".pill-btn");

let currentFilter = "all";

function filterCards() {
  const query = pkgSearch.value.toLowerCase().trim();

  cards.forEach(card => {
    const cat = card.getAttribute("data-category");
    const searchText = card.getAttribute("data-search").toLowerCase();

    const matchesCat = (currentFilter === "all" || cat === currentFilter);
    const matchesQuery = (!query || searchText.includes(query));

    if (matchesCat && matchesQuery) {
      card.style.display = "flex";
    } else {
      card.style.display = "none";
    }
  });
}

pkgSearch.addEventListener("input", filterCards);

pillBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    pillBtns.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentFilter = btn.getAttribute("data-filter");
    filterCards();
  });
});

// Multi-install Generator
const checkboxes = document.querySelectorAll("#checkMatrix input");
const combinedPipCmd = document.getElementById("combinedPipCmd");

function updateCombinedPip() {
  const selected = [];
  checkboxes.forEach(cb => {
    if (cb.checked) selected.push(cb.value);
  });

  if (selected.length === 0) {
    combinedPipCmd.innerText = "# Select at least one package above";
  } else {
    combinedPipCmd.innerText = "pip install " + selected.join(" ");
  }
}

checkboxes.forEach(cb => cb.addEventListener("change", updateCombinedPip));

function copyCombinedPip() {
  const txt = combinedPipCmd.innerText;
  navigator.clipboard.writeText(txt).then(() => {
    alert("Copied: " + txt);
  });
}
</script>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(HTML_DASHBOARD)

print(f"Master Hub Dashboard successfully built at {OUTPUT_FILE} ({len(HTML_DASHBOARD):,} bytes)")
