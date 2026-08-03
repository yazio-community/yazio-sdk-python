from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyNutrients")


@_attrs_define
class DailyNutrients:
    """
    Attributes:
        date (str | Unset):
        energy (float | Unset):
        carb (float | Unset):
        protein (float | Unset):
        fat (float | Unset):
        energy_goal (float | Unset):
    """

    date: str | Unset = UNSET
    energy: float | Unset = UNSET
    carb: float | Unset = UNSET
    protein: float | Unset = UNSET
    fat: float | Unset = UNSET
    energy_goal: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        energy = self.energy

        carb = self.carb

        protein = self.protein

        fat = self.fat

        energy_goal = self.energy_goal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if energy is not UNSET:
            field_dict["energy"] = energy
        if carb is not UNSET:
            field_dict["carb"] = carb
        if protein is not UNSET:
            field_dict["protein"] = protein
        if fat is not UNSET:
            field_dict["fat"] = fat
        if energy_goal is not UNSET:
            field_dict["energy_goal"] = energy_goal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        energy = d.pop("energy", UNSET)

        carb = d.pop("carb", UNSET)

        protein = d.pop("protein", UNSET)

        fat = d.pop("fat", UNSET)

        energy_goal = d.pop("energy_goal", UNSET)

        daily_nutrients = cls(
            date=date,
            energy=energy,
            carb=carb,
            protein=protein,
            fat=fat,
            energy_goal=energy_goal,
        )

        daily_nutrients.additional_properties = d
        return daily_nutrients

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
