from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileDiet")


@_attrs_define
class UserProfileDiet:
    """
    Attributes:
        name (str | Unset):
        carb_percentage (float | Unset):
        fat_percentage (float | Unset):
        protein_percentage (float | Unset):
    """

    name: str | Unset = UNSET
    carb_percentage: float | Unset = UNSET
    fat_percentage: float | Unset = UNSET
    protein_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        carb_percentage = self.carb_percentage

        fat_percentage = self.fat_percentage

        protein_percentage = self.protein_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if carb_percentage is not UNSET:
            field_dict["carb_percentage"] = carb_percentage
        if fat_percentage is not UNSET:
            field_dict["fat_percentage"] = fat_percentage
        if protein_percentage is not UNSET:
            field_dict["protein_percentage"] = protein_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        carb_percentage = d.pop("carb_percentage", UNSET)

        fat_percentage = d.pop("fat_percentage", UNSET)

        protein_percentage = d.pop("protein_percentage", UNSET)

        user_profile_diet = cls(
            name=name,
            carb_percentage=carb_percentage,
            fat_percentage=fat_percentage,
            protein_percentage=protein_percentage,
        )

        user_profile_diet.additional_properties = d
        return user_profile_diet

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
