from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthTokenRequest")


@_attrs_define
class OAuthTokenRequest:
    """
    Attributes:
        username (str | Unset): The account's email address.
        password (str | Unset):
        grant_type (str | Unset): `password` to exchange credentials for a token, `refresh_token` to renew one. Example:
            password.
        client_id (str | Unset): The client id the mobile app ships with. Identifies the app rather than the user; every
            install sends the same value. Example: 3_5rbw4kehpugw8ogsc8ck8oo4ogswgckcskc04gcg8kk8k48ssw.
        client_secret (str | Unset): The client secret the mobile app ships with. Not a per-user secret; see
            `client_id`. Example: 25gdtt1hvdi8gwowoww4oo88sgsw0oo04o0og0kkgwwks8k0k.
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    grant_type: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        grant_type = self.grant_type

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        grant_type = d.pop("grant_type", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        o_auth_token_request = cls(
            username=username,
            password=password,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
        )

        o_auth_token_request.additional_properties = d
        return o_auth_token_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
