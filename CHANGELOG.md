# Changelog — geopera

All notable changes to the Geopera Python SDK. This project follows
[Semantic Versioning](https://semver.org); the version tracks the Geopera API contract.

## 2.1.0

- Added a fluent, namespaced client: `Geopera(token=...).<resource>.<action>(body)` over the
  generated operation modules (body may be a dict or the typed input model). The
  `AuthenticatedClient` + `geopera.api.operations.<id>` modules remain the low-level surface.

## 2.0.0

- First public release of the typed Python client for the Geopera platform.
- Sync + async access to every `/v1/op/*` operation, generated from the live OpenAPI.
- Typed inputs, outputs, and errors (`Problem` / `HTTPValidationError`); `py.typed` shipped.
- API-key or OAuth bearer-token auth via `AuthenticatedClient`.
