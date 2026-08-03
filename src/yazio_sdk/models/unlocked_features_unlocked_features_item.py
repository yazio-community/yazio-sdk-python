from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnlockedFeaturesUnlockedFeaturesItem")


@_attrs_define
class UnlockedFeaturesUnlockedFeaturesItem:
    """
    Attributes:
        feature (str | Unset):
        origin (str | Unset):
        expire_date_time_utc (str | Unset):
    """

    feature: str | Unset = UNSET
    origin: str | Unset = UNSET
    expire_date_time_utc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        origin = self.origin

        expire_date_time_utc = self.expire_date_time_utc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature is not UNSET:
            field_dict["feature"] = feature
        if origin is not UNSET:
            field_dict["origin"] = origin
        if expire_date_time_utc is not UNSET:
            field_dict["expire_date_time_utc"] = expire_date_time_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature = d.pop("feature", UNSET)

        origin = d.pop("origin", UNSET)

        expire_date_time_utc = d.pop("expire_date_time_utc", UNSET)

        unlocked_features_unlocked_features_item = cls(
            feature=feature,
            origin=origin,
            expire_date_time_utc=expire_date_time_utc,
        )

        unlocked_features_unlocked_features_item.additional_properties = d
        return unlocked_features_unlocked_features_item

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
