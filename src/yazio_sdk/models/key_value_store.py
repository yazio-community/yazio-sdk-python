from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyValueStore")


@_attrs_define
class KeyValueStore:
    """
    Attributes:
        streak_repair_remote_key (str | Unset):
    """

    streak_repair_remote_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        streak_repair_remote_key = self.streak_repair_remote_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if streak_repair_remote_key is not UNSET:
            field_dict["StreakRepairRemoteKey"] = streak_repair_remote_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        streak_repair_remote_key = d.pop("StreakRepairRemoteKey", UNSET)

        key_value_store = cls(
            streak_repair_remote_key=streak_repair_remote_key,
        )

        key_value_store.additional_properties = d
        return key_value_store

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
