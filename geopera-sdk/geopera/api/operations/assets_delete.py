from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_delete_input import AssetDeleteInput
from ...models.asset_delete_output import AssetDeleteOutput
from ...models.http_validation_error import HTTPValidationError
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AssetDeleteInput,
    x_api_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/op/assets.delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetDeleteOutput | HTTPValidationError | Problem | None:
    if response.status_code == 200:
        response_200 = AssetDeleteOutput.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = Problem.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetDeleteOutput | HTTPValidationError | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetDeleteInput,
    x_api_key: None | str | Unset = UNSET,
) -> Response[AssetDeleteOutput | HTTPValidationError | Problem]:
    """Delete an asset (file) from an item (item access required).

    Args:
        x_api_key (None | str | Unset):
        body (AssetDeleteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDeleteOutput | HTTPValidationError | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AssetDeleteInput,
    x_api_key: None | str | Unset = UNSET,
) -> AssetDeleteOutput | HTTPValidationError | Problem | None:
    """Delete an asset (file) from an item (item access required).

    Args:
        x_api_key (None | str | Unset):
        body (AssetDeleteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetDeleteOutput | HTTPValidationError | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetDeleteInput,
    x_api_key: None | str | Unset = UNSET,
) -> Response[AssetDeleteOutput | HTTPValidationError | Problem]:
    """Delete an asset (file) from an item (item access required).

    Args:
        x_api_key (None | str | Unset):
        body (AssetDeleteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDeleteOutput | HTTPValidationError | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AssetDeleteInput,
    x_api_key: None | str | Unset = UNSET,
) -> AssetDeleteOutput | HTTPValidationError | Problem | None:
    """Delete an asset (file) from an item (item access required).

    Args:
        x_api_key (None | str | Unset):
        body (AssetDeleteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetDeleteOutput | HTTPValidationError | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
        )
    ).parsed
