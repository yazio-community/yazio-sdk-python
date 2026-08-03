from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NutrientSummary")


@_attrs_define
class NutrientSummary:
    """
    Attributes:
        energy_energy (float | Unset):
        nutrient_carb (float | Unset):
        nutrient_fat (float | Unset):
        nutrient_protein (float | Unset):
    """

    energy_energy: float | Unset = UNSET
    nutrient_carb: float | Unset = UNSET
    nutrient_fat: float | Unset = UNSET
    nutrient_protein: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_energy = self.energy_energy

        nutrient_carb = self.nutrient_carb

        nutrient_fat = self.nutrient_fat

        nutrient_protein = self.nutrient_protein

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy_energy is not UNSET:
            field_dict["energy.energy"] = energy_energy
        if nutrient_carb is not UNSET:
            field_dict["nutrient.carb"] = nutrient_carb
        if nutrient_fat is not UNSET:
            field_dict["nutrient.fat"] = nutrient_fat
        if nutrient_protein is not UNSET:
            field_dict["nutrient.protein"] = nutrient_protein

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        energy_energy = d.pop("energy.energy", UNSET)

        nutrient_carb = d.pop("nutrient.carb", UNSET)

        nutrient_fat = d.pop("nutrient.fat", UNSET)

        nutrient_protein = d.pop("nutrient.protein", UNSET)

        nutrient_summary = cls(
            energy_energy=energy_energy,
            nutrient_carb=nutrient_carb,
            nutrient_fat=nutrient_fat,
            nutrient_protein=nutrient_protein,
        )

        nutrient_summary.additional_properties = d
        return nutrient_summary

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
