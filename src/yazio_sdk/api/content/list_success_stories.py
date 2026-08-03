from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: str | Unset = UNSET,
    sex: str | Unset = UNSET,
    goal: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["locale"] = locale

    params["sex"] = sex

    params["goal"] = goal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/content/v2/success-stories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Any] | None:
    if response.status_code == 200:
        response_200 = cast(list[Any], response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    sex: str | Unset = UNSET,
    goal: str | Unset = UNSET,
) -> Response[list[Any]]:
    """Editorial success stories

    Args:
        locale (str | Unset):
        sex (str | Unset):
        goal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Any]]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sex=sex,
        goal=goal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    sex: str | Unset = UNSET,
    goal: str | Unset = UNSET,
) -> list[Any] | None:
    """Editorial success stories

    Args:
        locale (str | Unset):
        sex (str | Unset):
        goal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Any]
    """

    return sync_detailed(
        client=client,
        locale=locale,
        sex=sex,
        goal=goal,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    sex: str | Unset = UNSET,
    goal: str | Unset = UNSET,
) -> Response[list[Any]]:
    """Editorial success stories

    Args:
        locale (str | Unset):
        sex (str | Unset):
        goal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Any]]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sex=sex,
        goal=goal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    sex: str | Unset = UNSET,
    goal: str | Unset = UNSET,
) -> list[Any] | None:
    """Editorial success stories

    Args:
        locale (str | Unset):
        sex (str | Unset):
        goal (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            sex=sex,
            goal=goal,
        )
    ).parsed
