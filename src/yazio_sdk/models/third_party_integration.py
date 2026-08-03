from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThirdPartyIntegration")


@_attrs_define
class ThirdPartyIntegration:
    """
    Attributes:
        required_actions (list[Any] | Unset):
        active_gateway (str | Unset):
    """

    required_actions: list[Any] | Unset = UNSET
    active_gateway: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_actions: list[Any] | Unset = UNSET
        if not isinstance(self.required_actions, Unset):
            required_actions = self.required_actions

        active_gateway = self.active_gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_actions is not UNSET:
            field_dict["required_actions"] = required_actions
        if active_gateway is not UNSET:
            field_dict["active_gateway"] = active_gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        required_actions = cast(list[Any], d.pop("required_actions", UNSET))

        active_gateway = d.pop("active_gateway", UNSET)

        third_party_integration = cls(
            required_actions=required_actions,
            active_gateway=active_gateway,
        )

        third_party_integration.additional_properties = d
        return third_party_integration

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
