from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.problem import Problem
from ...models.test_subscription_input import TestSubscriptionInput
from ...models.test_subscription_output import TestSubscriptionOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TestSubscriptionInput,
    x_api_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/op/event_subscriptions.test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Problem | TestSubscriptionOutput | None:
    if response.status_code == 200:
        response_200 = TestSubscriptionOutput.from_dict(response.json())

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
) -> Response[HTTPValidationError | Problem | TestSubscriptionOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TestSubscriptionInput,
    x_api_key: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Problem | TestSubscriptionOutput]:
    """Send a test event to a webhook subscription and return the delivery result.

    Args:
        x_api_key (None | str | Unset):
        body (TestSubscriptionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Problem | TestSubscriptionOutput]
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
    body: TestSubscriptionInput,
    x_api_key: None | str | Unset = UNSET,
) -> HTTPValidationError | Problem | TestSubscriptionOutput | None:
    """Send a test event to a webhook subscription and return the delivery result.

    Args:
        x_api_key (None | str | Unset):
        body (TestSubscriptionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Problem | TestSubscriptionOutput
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TestSubscriptionInput,
    x_api_key: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Problem | TestSubscriptionOutput]:
    """Send a test event to a webhook subscription and return the delivery result.

    Args:
        x_api_key (None | str | Unset):
        body (TestSubscriptionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Problem | TestSubscriptionOutput]
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
    body: TestSubscriptionInput,
    x_api_key: None | str | Unset = UNSET,
) -> HTTPValidationError | Problem | TestSubscriptionOutput | None:
    """Send a test event to a webhook subscription and return the delivery result.

    Args:
        x_api_key (None | str | Unset):
        body (TestSubscriptionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Problem | TestSubscriptionOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
        )
    ).parsed
