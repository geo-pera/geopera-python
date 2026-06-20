from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_execute_output import AnalyticsExecuteOutput
from ...models.execute_request import ExecuteRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExecuteRequest,
    x_api_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/op/analytics.execute",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsExecuteOutput | HTTPValidationError | Problem | None:
    if response.status_code == 200:
        response_200 = AnalyticsExecuteOutput.from_dict(response.json())

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
) -> Response[AnalyticsExecuteOutput | HTTPValidationError | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
    x_api_key: None | str | Unset = UNSET,
) -> Response[AnalyticsExecuteOutput | HTTPValidationError | Problem]:
    """Run a registered analytics operation (zonal_stats / time_series / change_detection).

    Args:
        x_api_key (None | str | Unset):
        body (ExecuteRequest): Request to execute a registered analytics operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsExecuteOutput | HTTPValidationError | Problem]
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
    body: ExecuteRequest,
    x_api_key: None | str | Unset = UNSET,
) -> AnalyticsExecuteOutput | HTTPValidationError | Problem | None:
    """Run a registered analytics operation (zonal_stats / time_series / change_detection).

    Args:
        x_api_key (None | str | Unset):
        body (ExecuteRequest): Request to execute a registered analytics operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsExecuteOutput | HTTPValidationError | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
    x_api_key: None | str | Unset = UNSET,
) -> Response[AnalyticsExecuteOutput | HTTPValidationError | Problem]:
    """Run a registered analytics operation (zonal_stats / time_series / change_detection).

    Args:
        x_api_key (None | str | Unset):
        body (ExecuteRequest): Request to execute a registered analytics operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsExecuteOutput | HTTPValidationError | Problem]
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
    body: ExecuteRequest,
    x_api_key: None | str | Unset = UNSET,
) -> AnalyticsExecuteOutput | HTTPValidationError | Problem | None:
    """Run a registered analytics operation (zonal_stats / time_series / change_detection).

    Args:
        x_api_key (None | str | Unset):
        body (ExecuteRequest): Request to execute a registered analytics operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsExecuteOutput | HTTPValidationError | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
        )
    ).parsed
