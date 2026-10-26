"""Static integrity tests for the SDK governance hub.

The generator performs live network requests, so these tests never execute it.
Instead they parse ``generate_pypi_hub.py`` with :mod:`ast` and validate the
hand-maintained registry and the persisted telemetry history.
"""

from __future__ import annotations

import ast
import json
import re
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "generate_pypi_hub.py"
HISTORY = ROOT / "sdk_history.json"

REQUIRED_KEYS = {
    "id",
    "name",
    "pypi",
    "gh_repo",
    "category",
    "tagline",
    "color",
    "gradient",
    "license",
    "docs_url",
    "pypi_url",
    "github_url",
    "doi",
    "pip",
    "algorithms_count",
    "highlights",
    "repl_example",
}

# Licenses that are actually used across the eight SDKs.
ALLOWED_LICENSES = {"MIT", "GPL-2.0-or-later", "GPL-3.0-or-later"}

# Expected license per PyPI project, guarding against registry drift.
EXPECTED_LICENSES = {
    "geoai2analytics-sdk": "MIT",
    "multilayer-sdk": "MIT",
    "myface2city": "MIT",
    "NCZ2Geo": "GPL-2.0-or-later",
    "cad2geo": "GPL-2.0-or-later",
    "osm2threejs": "MIT",
    "zero2route3d-sdk": "MIT",
    "planx-sdk": "MIT",
}


def _parse_module() -> ast.Module:
    """Parse the generator source without importing or executing it."""
    return ast.parse(SCRIPT.read_text(encoding="utf-8"))


def _load_literal(name: str) -> object:
    """Return the literal value assigned to a module-level ``name``."""
    for node in _parse_module().body:
        if not isinstance(node, ast.Assign):
            continue
        targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
        if name in targets:
            return ast.literal_eval(node.value)
    raise AssertionError(f"Module-level assignment {name!r} not found")


@pytest.fixture(scope="module")
def registry() -> list[dict[str, object]]:
    """The parsed ``SDK_REGISTRY`` list."""
    value = _load_literal("SDK_REGISTRY")
    assert isinstance(value, list)
    return value


def test_script_is_valid_python() -> None:
    """The generator must compile cleanly."""
    compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec")


def test_registry_contains_all_eight_packages(registry: list[dict[str, object]]) -> None:
    """The ecosystem hub is defined around exactly eight SDKs."""
    assert len(registry) == 8
    assert {entry["pypi"] for entry in registry} == set(EXPECTED_LICENSES)


def test_registry_entries_have_required_fields(registry: list[dict[str, object]]) -> None:
    """Every registry record must be complete enough to render the dashboard."""
    for entry in registry:
        missing = REQUIRED_KEYS - entry.keys()
        assert not missing, f"{entry.get('id')!r} is missing keys: {sorted(missing)}"

        assert isinstance(entry["algorithms_count"], int)
        assert entry["algorithms_count"] > 0
        assert isinstance(entry["highlights"], list) and entry["highlights"]
        assert isinstance(entry["repl_example"], str) and entry["repl_example"].strip()
        assert entry["license"] in ALLOWED_LICENSES


def test_registry_identifiers_are_unique(registry: list[dict[str, object]]) -> None:
    """Identifiers, PyPI names and repositories must not collide."""
    for key in ("id", "pypi", "gh_repo"):
        values = [entry[key] for entry in registry]
        assert len(values) == len(set(values)), f"duplicate values in {key!r}: {values}"


def test_install_and_url_fields_are_consistent(registry: list[dict[str, object]]) -> None:
    """Derived install commands and URLs must match each PyPI project name."""
    for entry in registry:
        pypi_name = entry["pypi"]
        assert entry["pip"] == f"pip install {pypi_name}"
        assert entry["pypi_url"] == f"https://pypi.org/project/{pypi_name}/"
        assert entry["docs_url"].startswith("https://")
        assert entry["github_url"].startswith("https://github.com/")


def test_licenses_match_upstream_packages(registry: list[dict[str, object]]) -> None:
    """Registry licenses must match the metadata shipped by each SDK."""
    declared = {entry["pypi"]: entry["license"] for entry in registry}
    assert declared == EXPECTED_LICENSES


def test_repl_examples_are_runnable_python(registry: list[dict[str, object]]) -> None:
    """Every dashboard code sample must at least be syntactically valid."""
    for entry in registry:
        try:
            ast.parse(entry["repl_example"])
        except SyntaxError as exc:  # pragma: no cover - assertion message helper
            raise AssertionError(f"{entry['pypi']} has an invalid example: {exc}") from exc


def test_history_file_is_a_valid_telemetry_log() -> None:
    """``sdk_history.json`` must stay a chronologically ordered snapshot list."""
    records = json.loads(HISTORY.read_text(encoding="utf-8"))
    assert isinstance(records, list) and records

    seen_dates: list[str] = []
    for record in records:
        assert {"date", "timestamp", "packages"} <= record.keys()
        # Raises ValueError when the date is malformed.
        date.fromisoformat(record["date"])
        seen_dates.append(record["date"])

        packages = record["packages"]
        assert isinstance(packages, dict) and packages
        for name, metrics in packages.items():
            assert isinstance(name, str) and name
            assert isinstance(metrics, dict) and "version" in metrics

    assert seen_dates == sorted(seen_dates)


def test_history_does_not_exceed_retention_window() -> None:
    """The generator keeps at most 90 daily snapshots."""
    records = json.loads(HISTORY.read_text(encoding="utf-8"))
    assert len(records) <= 90


def test_dois_are_unique_zenodo_dois(registry: list[dict[str, object]]) -> None:
    """Each SDK cites its own Zenodo concept DOI."""
    dois = [str(entry["doi"]) for entry in registry]
    assert len(set(dois)) == len(dois)
    assert all(re.fullmatch(r"10\.5281/zenodo\.\d+", doi) for doi in dois)
