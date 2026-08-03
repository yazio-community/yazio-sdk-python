from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_user_recipe_image_body import AddUserRecipeImageBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    filename: str,
    *,
    body: AddUserRecipeImageBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v22/user/recipes/{id}/image/{filename}".format(
            id=quote(str(id), safe=""),
            filename=quote(str(filename), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddUserRecipeImageBody | Unset = UNSET,
) -> Response[Any]:
    """Add a photo to a recipe

     The app generates `filename` itself as a random id plus the original extension, e.g.
    `a14296b1-5c4b-4201-a6f8-15746c5c9d54.jpg` — it is not returned or read back from anywhere, so any
    value works.

    Args:
        id (str):
        filename (str):
        body (AddUserRecipeImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        filename=filename,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddUserRecipeImageBody | Unset = UNSET,
) -> Response[Any]:
    """Add a photo to a recipe

     The app generates `filename` itself as a random id plus the original extension, e.g.
    `a14296b1-5c4b-4201-a6f8-15746c5c9d54.jpg` — it is not returned or read back from anywhere, so any
    value works.

    Args:
        id (str):
        filename (str):
        body (AddUserRecipeImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        filename=filename,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
