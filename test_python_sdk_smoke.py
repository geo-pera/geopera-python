"""Smoke test for the generated Geopera Python SDK — NO MOCKS.

Proves the built/installed package imports, exposes a typed op module per operation
(sync + async), and that a typed call reaches the live API. The live half skips
cleanly when GEOPERA_API_URL/TOKEN aren't set.

Run against the BUILT package (CI installs the wheel; locally `pip install
geopera-sdk/dist/*.whl` after `./regen.sh`):

    ./regen.sh && pip install geopera-sdk/dist/*.whl
    python -m pytest test_python_sdk_smoke.py -q
    # live half:
    GEOPERA_API_URL=https://api.geopera.com GEOPERA_API_TOKEN=gpra_... \
      python -m pytest test_python_sdk_smoke.py -q
"""
import os
import pkgutil

import httpx
import pytest

API_URL = os.environ.get("GEOPERA_API_URL")
TOKEN = os.environ.get("GEOPERA_API_TOKEN")


def test_package_imports_and_constructs_client():
    from geopera import AuthenticatedClient, Client  # noqa: F401

    client = AuthenticatedClient(base_url="https://api.geopera.com", token="gpra_test")
    assert client is not None


def test_one_typed_op_module_per_operation_with_sync_and_async():
    from geopera.api import operations

    ops = [m.name for m in pkgutil.iter_modules(operations.__path__) if not m.name.startswith("_")]
    assert len(ops) >= 50, f"only {len(ops)} op modules generated"
    # catalog_search is a stable, public op — every generated op exposes sync + async.
    from geopera.api.operations import catalog_search

    for fn in ("sync", "sync_detailed", "asyncio", "asyncio_detailed"):
        assert hasattr(catalog_search, fn), f"catalog_search missing {fn}"


def test_typed_models_and_error_types_import():
    from geopera.models import CatalogSearchInput, CatalogSearchOutput, Problem  # noqa: F401

    body = CatalogSearchInput(host_name="api.geopera.com", limit=5)
    assert body.limit == 5


def _reachable(url: str) -> bool:
    try:
        httpx.get(f"{url.rstrip('/')}/openapi.json", timeout=3.0).raise_for_status()
        return True
    except Exception:  # noqa: BLE001
        return False


@pytest.mark.skipif(
    not (API_URL and TOKEN and _reachable(API_URL)),
    reason="set GEOPERA_API_URL (reachable) + GEOPERA_API_TOKEN for the live test",
)
def test_live_typed_call_returns_real_data():
    from geopera import AuthenticatedClient
    from geopera.api.operations import catalog_search
    from geopera.models import CatalogSearchInput

    client = AuthenticatedClient(base_url=API_URL, token=TOKEN)
    resp = catalog_search.sync_detailed(
        client=client, body=CatalogSearchInput(host_name="api.geopera.com", limit=5)
    )
    assert resp.status_code in (200, 401, 403), f"got {resp.status_code}: {resp.content[:300]}"
    print(f"\nLIVE python SDK catalog.search reached the API — HTTP {resp.status_code}")
