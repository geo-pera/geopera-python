# Geopera SDK (Python)

[![PyPI](https://img.shields.io/pypi/v/geopera.svg)](https://pypi.org/project/geopera/)
[![Python](https://img.shields.io/pypi/pyversions/geopera.svg)](https://pypi.org/project/geopera/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The official Python client for the **Geopera** geospatial data platform — satellite tasking &
archive ordering, catalog search, the data platform, billing, and more. Every capability is a typed
*operation*; this SDK gives you a fully typed, sync **and** async client for all of them.

- **Typed end-to-end** — every operation has typed inputs, outputs, and errors (`py.typed` shipped).
- **Sync & async** — call any operation with `.sync()` or `await .asyncio()`.
- **Auth your way** — a Geopera API key, or an OAuth bearer token from sign-in.
- Generated from the live OpenAPI, so it never drifts from the API.

## Install

```bash
pip install geopera
```

Requires Python 3.11+.

## Quickstart

```python
from geopera import AuthenticatedClient
from geopera.api.operations import catalog_search
from geopera.models import CatalogSearchInput

client = AuthenticatedClient(
    base_url="https://api.geopera.com",
    token="gpra_...",            # your Geopera API key
)

result = catalog_search.sync(
    client=client,
    body=CatalogSearchInput(
        host_name="api.geopera.com",
        collections=["sentinel-2-l2a"],
        limit=10,
    ),
)
print(result)   # -> CatalogSearchOutput (typed)
```

Every operation lives under `geopera.api.operations.<operation_id>` (dots become underscores —
e.g. `orders.tasking.estimate` → `orders_tasking_estimate`). Request/response models are in
`geopera.models`. Browse the full operation reference at **https://docs.geopera.com/api-reference**.

## Authentication

Pass either credential as `token`; Geopera accepts both and runs every call as that principal
(with its scopes, audit, and provenance):

```python
# 1) A Geopera API key (headless / server-to-server) — create one in the portal.
client = AuthenticatedClient(base_url="https://api.geopera.com", token="gpra_...")

# 2) An OAuth bearer token (e.g. from a signed-in user session).
client = AuthenticatedClient(base_url="https://api.geopera.com", token=user_access_token)
```

## Async

```python
import asyncio
from geopera import AuthenticatedClient
from geopera.api.operations import orders_tasking_estimate
from geopera.models import TaskingEstimateInput

async def main():
    async with AuthenticatedClient(base_url="https://api.geopera.com", token="gpra_...") as client:
        est = await orders_tasking_estimate.asyncio(
            client=client,
            body=TaskingEstimateInput(...),
        )
        print(est)

asyncio.run(main())
```

## Error handling

Operations return either the typed success model or a typed error — `Problem` (RFC 9457
`problem+json`, what Geopera returns for business/permission errors) or `HTTPValidationError`
(422 input validation). Use the `*_detailed` variant when you need the HTTP status code:

```python
from geopera.api.operations import catalog_search
from geopera.models import CatalogSearchInput, Problem

resp = catalog_search.sync_detailed(client=client, body=CatalogSearchInput(...))
if resp.status_code == 200:
    data = resp.parsed              # CatalogSearchOutput
elif isinstance(resp.parsed, Problem):
    print("geopera error:", resp.parsed.title, resp.parsed.detail)
```

## Configuration

`AuthenticatedClient` accepts the usual knobs (timeouts, retries via httpx, custom headers,
TLS verification):

```python
client = AuthenticatedClient(
    base_url="https://api.geopera.com",
    token="gpra_...",
    timeout=httpx.Timeout(30.0),
    raise_on_unexpected_status=True,
    headers={"X-Request-Source": "my-app"},
)
```

## Versioning

The SDK version tracks the Geopera API contract. Breaking API changes bump the major version.
See the [changelog](https://github.com/geo-pera/geopera-python/blob/main/CHANGELOG.md).

## Links

- 📚 API reference: https://docs.geopera.com/api-reference
- 🌐 Geopera: https://geopera.com
- 🐍 PyPI: https://pypi.org/project/geopera/

## License

MIT © Geopera
