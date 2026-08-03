from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.suggested_product import SuggestedProduct
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    daytime: str | Unset = UNSET,
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["daytime"] = daytime

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v22/user/products/suggested",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[SuggestedProduct] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SuggestedProduct.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[SuggestedProduct]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    daytime: str | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[list[SuggestedProduct]]:
    """Products suggested for a meal slot

    Args:
        daytime (str | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SuggestedProduct]]
    """

    kwargs = _get_kwargs(
        daytime=daytime,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    daytime: str | Unset = UNSET,
    date: str | Unset = UNSET,
) -> list[SuggestedProduct] | None:
    """Products suggested for a meal slot

    Args:
        daytime (str | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SuggestedProduct]
    """

    return sync_detailed(
        client=client,
        daytime=daytime,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    daytime: str | Unset = UNSET,
    date: str | Unset = UNSET,
) -> Response[list[SuggestedProduct]]:
    """Products suggested for a meal slot

    Args:
        daytime (str | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SuggestedProduct]]
    """

    kwargs = _get_kwargs(
        daytime=daytime,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    daytime: str | Unset = UNSET,
    date: str | Unset = UNSET,
) -> list[SuggestedProduct] | None:
    """Products suggested for a meal slot

    Args:
        daytime (str | Unset):
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SuggestedProduct]
    """

    return (
        await asyncio_detailed(
            client=client,
            daytime=daytime,
            date=date,
        )
    ).parsed
