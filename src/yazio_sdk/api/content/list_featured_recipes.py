from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.recipe_index_entry import RecipeIndexEntry
from ...types import Response


def _get_kwargs(
    country_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/content/v2/recipes/{country_code}".format(
            country_code=quote(str(country_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[RecipeIndexEntry] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecipeIndexEntry.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[RecipeIndexEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[RecipeIndexEntry]]:
    """Editorial recipe collections for a country

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RecipeIndexEntry]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[RecipeIndexEntry] | None:
    """Editorial recipe collections for a country

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RecipeIndexEntry]
    """

    return sync_detailed(
        country_code=country_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    country_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[RecipeIndexEntry]]:
    """Editorial recipe collections for a country

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RecipeIndexEntry]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[RecipeIndexEntry] | None:
    """Editorial recipe collections for a country

    Args:
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RecipeIndexEntry]
    """

    return (
        await asyncio_detailed(
            country_code=country_code,
            client=client,
        )
    ).parsed
