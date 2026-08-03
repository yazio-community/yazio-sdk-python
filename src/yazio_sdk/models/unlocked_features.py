from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unlocked_features_unlocked_features_item import (
        UnlockedFeaturesUnlockedFeaturesItem,
    )


T = TypeVar("T", bound="UnlockedFeatures")


@_attrs_define
class UnlockedFeatures:
    """
    Attributes:
        unlocked_features (list[UnlockedFeaturesUnlockedFeaturesItem] | Unset):
    """

    unlocked_features: list[UnlockedFeaturesUnlockedFeaturesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unlocked_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unlocked_features, Unset):
            unlocked_features = []
            for unlocked_features_item_data in self.unlocked_features:
                unlocked_features_item = unlocked_features_item_data.to_dict()
                unlocked_features.append(unlocked_features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unlocked_features is not UNSET:
            field_dict["unlocked_features"] = unlocked_features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unlocked_features_unlocked_features_item import (
            UnlockedFeaturesUnlockedFeaturesItem,
        )

        d = dict(src_dict)
        _unlocked_features = d.pop("unlocked_features", UNSET)
        unlocked_features: list[UnlockedFeaturesUnlockedFeaturesItem] | Unset = UNSET
        if _unlocked_features is not UNSET:
            unlocked_features = []
            for unlocked_features_item_data in _unlocked_features:
                unlocked_features_item = UnlockedFeaturesUnlockedFeaturesItem.from_dict(
                    unlocked_features_item_data
                )

                unlocked_features.append(unlocked_features_item)

        unlocked_features = cls(
            unlocked_features=unlocked_features,
        )

        unlocked_features.additional_properties = d
        return unlocked_features

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
