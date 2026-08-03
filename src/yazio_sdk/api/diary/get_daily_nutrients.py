from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.daily_nutrients import DailyNutrients
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    end: str | Unset = UNSET,
    start: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["end"] = end

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v22/user/consumed-items/nutrients-daily",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[DailyNutrients] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DailyNutrients.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DailyNutrients]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    end: str | Unset = UNSET,
    start: str | Unset = UNSET,
) -> Response[list[DailyNutrients]]:
    """Nutrient totals per day

    Args:
        end (str | Unset):
        start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DailyNutrients]]
    """

    kwargs = _get_kwargs(
        end=end,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    end: str | Unset = UNSET,
    start: str | Unset = UNSET,
) -> list[DailyNutrients] | None:
    """Nutrient totals per day

    Args:
        end (str | Unset):
        start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DailyNutrients]
    """

    return sync_detailed(
        client=client,
        end=end,
        start=start,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    end: str | Unset = UNSET,
    start: str | Unset = UNSET,
) -> Response[list[DailyNutrients]]:
    """Nutrient totals per day

    Args:
        end (str | Unset):
        start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DailyNutrients]]
    """

    kwargs = _get_kwargs(
        end=end,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    end: str | Unset = UNSET,
    start: str | Unset = UNSET,
) -> list[DailyNutrients] | None:
    """Nutrient totals per day

    Args:
        end (str | Unset):
        start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DailyNutrients]
    """

    return (
        await asyncio_detailed(
            client=client,
            end=end,
            start=start,
        )
    ).parsed
