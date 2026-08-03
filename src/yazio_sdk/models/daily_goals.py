from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyGoals")


@_attrs_define
class DailyGoals:
    """
    Attributes:
        energy_energy (float | Unset):
        water (float | Unset):
        activity_step (float | Unset):
        nutrient_protein (float | Unset):
        nutrient_fat (float | Unset):
        nutrient_carb (float | Unset):
        bodyvalue_weight (float | Unset):
    """

    energy_energy: float | Unset = UNSET
    water: float | Unset = UNSET
    activity_step: float | Unset = UNSET
    nutrient_protein: float | Unset = UNSET
    nutrient_fat: float | Unset = UNSET
    nutrient_carb: float | Unset = UNSET
    bodyvalue_weight: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_energy = self.energy_energy

        water = self.water

        activity_step = self.activity_step

        nutrient_protein = self.nutrient_protein

        nutrient_fat = self.nutrient_fat

        nutrient_carb = self.nutrient_carb

        bodyvalue_weight = self.bodyvalue_weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy_energy is not UNSET:
            field_dict["energy.energy"] = energy_energy
        if water is not UNSET:
            field_dict["water"] = water
        if activity_step is not UNSET:
            field_dict["activity.step"] = activity_step
        if nutrient_protein is not UNSET:
            field_dict["nutrient.protein"] = nutrient_protein
        if nutrient_fat is not UNSET:
            field_dict["nutrient.fat"] = nutrient_fat
        if nutrient_carb is not UNSET:
            field_dict["nutrient.carb"] = nutrient_carb
        if bodyvalue_weight is not UNSET:
            field_dict["bodyvalue.weight"] = bodyvalue_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        energy_energy = d.pop("energy.energy", UNSET)

        water = d.pop("water", UNSET)

        activity_step = d.pop("activity.step", UNSET)

        nutrient_protein = d.pop("nutrient.protein", UNSET)

        nutrient_fat = d.pop("nutrient.fat", UNSET)

        nutrient_carb = d.pop("nutrient.carb", UNSET)

        bodyvalue_weight = d.pop("bodyvalue.weight", UNSET)

        daily_goals = cls(
            energy_energy=energy_energy,
            water=water,
            activity_step=activity_step,
            nutrient_protein=nutrient_protein,
            nutrient_fat=nutrient_fat,
            nutrient_carb=nutrient_carb,
            bodyvalue_weight=bodyvalue_weight,
        )

        daily_goals.additional_properties = d
        return daily_goals

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
