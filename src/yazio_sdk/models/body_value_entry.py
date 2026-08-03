from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_value_entry_weight_item import BodyValueEntryWeightItem


T = TypeVar("T", bound="BodyValueEntry")


@_attrs_define
class BodyValueEntry:
    """
    Attributes:
        weight (list[BodyValueEntryWeightItem] | Unset):
    """

    weight: list[BodyValueEntryWeightItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = []
            for weight_item_data in self.weight:
                weight_item = weight_item_data.to_dict()
                weight.append(weight_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_value_entry_weight_item import BodyValueEntryWeightItem

        d = dict(src_dict)
        _weight = d.pop("weight", UNSET)
        weight: list[BodyValueEntryWeightItem] | Unset = UNSET
        if _weight is not UNSET:
            weight = []
            for weight_item_data in _weight:
                weight_item = BodyValueEntryWeightItem.from_dict(weight_item_data)

                weight.append(weight_item)

        body_value_entry = cls(
            weight=weight,
        )

        body_value_entry.additional_properties = d
        return body_value_entry

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
