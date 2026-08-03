from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumedRecipePortion")


@_attrs_define
class ConsumedRecipePortion:
    """
    Attributes:
        id (str | Unset):
        date (str | Unset):
        daytime (str | Unset):
        type_ (str | Unset):
        recipe_id (str | Unset):
        portion_count (float | Unset):
    """

    id: str | Unset = UNSET
    date: str | Unset = UNSET
    daytime: str | Unset = UNSET
    type_: str | Unset = UNSET
    recipe_id: str | Unset = UNSET
    portion_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        daytime = self.daytime

        type_ = self.type_

        recipe_id = self.recipe_id

        portion_count = self.portion_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if daytime is not UNSET:
            field_dict["daytime"] = daytime
        if type_ is not UNSET:
            field_dict["type"] = type_
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if portion_count is not UNSET:
            field_dict["portion_count"] = portion_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        date = d.pop("date", UNSET)

        daytime = d.pop("daytime", UNSET)

        type_ = d.pop("type", UNSET)

        recipe_id = d.pop("recipe_id", UNSET)

        portion_count = d.pop("portion_count", UNSET)

        consumed_recipe_portion = cls(
            id=id,
            date=date,
            daytime=daytime,
            type_=type_,
            recipe_id=recipe_id,
            portion_count=portion_count,
        )

        consumed_recipe_portion.additional_properties = d
        return consumed_recipe_portion

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
