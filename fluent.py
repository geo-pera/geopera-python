"""Fluent, namespaced client for the Geopera platform.

``Geopera(token=...).catalog.search({...})`` mirrors the kernel namespace and
calls the generated operation module under the hood. Attribute access descends a
resource path; calling the node invokes the operation at that path::

    from geopera import Geopera

    client = Geopera(token="gpra_...")
    result = client.catalog.search({"host_name": "earthsearch-aws", "limit": 10})
    order = client.orders.archive.place({...})

The body may be a plain ``dict`` (converted to the operation's typed input model)
or the model instance itself. The generated ``AuthenticatedClient`` and the
``geopera.api.operations.<id>`` modules remain as the low-level escape hatch.

This module is hand-written and re-applied after each SDK regeneration by
patch_metadata.py (openapi-python-client overwrites the package on every run).
"""

from __future__ import annotations

import inspect
from importlib import import_module
from typing import Any

from .client import AuthenticatedClient, Client

DEFAULT_BASE_URL = "https://api.geopera.com"
_OPS_PKG = "geopera.api.operations"


def _module_for(operation_id: str):
    """Import the generated operation module for a dotted operation id."""
    name = operation_id.replace(".", "_").replace("-", "_")
    return import_module(f"{_OPS_PKG}.{name}")


class _Node:
    """A node in the resource tree: descend by attribute, invoke by call."""

    __slots__ = ("_client", "_prefix")

    def __init__(self, client: Client, prefix: str) -> None:
        object.__setattr__(self, "_client", client)
        object.__setattr__(self, "_prefix", prefix)

    def __getattr__(self, name: str) -> _Node:
        if name.startswith("_"):
            raise AttributeError(name)
        return _Node(self._client, f"{self._prefix}.{name}")

    def __call__(self, body: Any = None, *, detailed: bool = False, **extra: Any) -> Any:
        """Invoke the operation at this path. Returns the parsed model (or error
        model); pass ``detailed=True`` for the full typed ``Response``."""
        module = _module_for(self._prefix)
        sig = inspect.signature(module.sync)
        kwargs: dict[str, Any] = {"client": self._client}
        if "body" in sig.parameters:
            ann = sig.parameters["body"].annotation
            if isinstance(body, dict) and hasattr(ann, "from_dict"):
                body = ann.from_dict(body)
            elif body is None and hasattr(ann, "from_dict"):
                body = ann.from_dict({})
            kwargs["body"] = body
        for key, value in extra.items():
            if key in sig.parameters:
                kwargs[key] = value
        fn = module.sync_detailed if detailed else module.sync
        return fn(**kwargs)

    def __repr__(self) -> str:
        return f"<geopera operation namespace {self._prefix!r}>"


class Geopera:
    """Fluent entry point: ``Geopera(token=...).<resource>.<action>(body)``.

    Pass a ``dict`` or the operation's typed input model as the body. For the
    sync/async variants and the typed ``Response`` object, use the generated
    ``AuthenticatedClient`` + ``geopera.api.operations.<id>`` modules directly
    (``self.client`` exposes the underlying client).
    """

    def __init__(
        self,
        token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        **client_kwargs: Any,
    ) -> None:
        if token is None:
            self._client: Client = Client(base_url=base_url, **client_kwargs)
        else:
            self._client = AuthenticatedClient(base_url=base_url, token=token, **client_kwargs)

    @property
    def client(self) -> Client:
        """The underlying generated client (low-level escape hatch)."""
        return self._client

    def __getattr__(self, name: str) -> _Node:
        if name.startswith("_"):
            raise AttributeError(name)
        return _Node(self._client, name)
