from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipeDraftNutrients")


@_attrs_define
class RecipeDraftNutrients:
    """
    Attributes:
        nutrient_salt (float | Unset):
        nutrient_monounsaturated (float | Unset):
        nutrient_sugar (float | Unset):
        mineral_calcium (float | Unset):
        nutrient_saturated (float | Unset):
        vitamin_b6 (float | Unset):
        nutrient_protein (float | Unset):
        nutrient_dietaryfiber (float | Unset):
        energy_energy (float | Unset):
        nutrient_polyunsaturated (float | Unset):
        nutrient_fat (float | Unset):
        nutrient_carb (float | Unset):
    """

    nutrient_salt: float | Unset = UNSET
    nutrient_monounsaturated: float | Unset = UNSET
    nutrient_sugar: float | Unset = UNSET
    mineral_calcium: float | Unset = UNSET
    nutrient_saturated: float | Unset = UNSET
    vitamin_b6: float | Unset = UNSET
    nutrient_protein: float | Unset = UNSET
    nutrient_dietaryfiber: float | Unset = UNSET
    energy_energy: float | Unset = UNSET
    nutrient_polyunsaturated: float | Unset = UNSET
    nutrient_fat: float | Unset = UNSET
    nutrient_carb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nutrient_salt = self.nutrient_salt

        nutrient_monounsaturated = self.nutrient_monounsaturated

        nutrient_sugar = self.nutrient_sugar

        mineral_calcium = self.mineral_calcium

        nutrient_saturated = self.nutrient_saturated

        vitamin_b6 = self.vitamin_b6

        nutrient_protein = self.nutrient_protein

        nutrient_dietaryfiber = self.nutrient_dietaryfiber

        energy_energy = self.energy_energy

        nutrient_polyunsaturated = self.nutrient_polyunsaturated

        nutrient_fat = self.nutrient_fat

        nutrient_carb = self.nutrient_carb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nutrient_salt is not UNSET:
            field_dict["nutrient.salt"] = nutrient_salt
        if nutrient_monounsaturated is not UNSET:
            field_dict["nutrient.monounsaturated"] = nutrient_monounsaturated
        if nutrient_sugar is not UNSET:
            field_dict["nutrient.sugar"] = nutrient_sugar
        if mineral_calcium is not UNSET:
            field_dict["mineral.calcium"] = mineral_calcium
        if nutrient_saturated is not UNSET:
            field_dict["nutrient.saturated"] = nutrient_saturated
        if vitamin_b6 is not UNSET:
            field_dict["vitamin.b6"] = vitamin_b6
        if nutrient_protein is not UNSET:
            field_dict["nutrient.protein"] = nutrient_protein
        if nutrient_dietaryfiber is not UNSET:
            field_dict["nutrient.dietaryfiber"] = nutrient_dietaryfiber
        if energy_energy is not UNSET:
            field_dict["energy.energy"] = energy_energy
        if nutrient_polyunsaturated is not UNSET:
            field_dict["nutrient.polyunsaturated"] = nutrient_polyunsaturated
        if nutrient_fat is not UNSET:
            field_dict["nutrient.fat"] = nutrient_fat
        if nutrient_carb is not UNSET:
            field_dict["nutrient.carb"] = nutrient_carb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nutrient_salt = d.pop("nutrient.salt", UNSET)

        nutrient_monounsaturated = d.pop("nutrient.monounsaturated", UNSET)

        nutrient_sugar = d.pop("nutrient.sugar", UNSET)

        mineral_calcium = d.pop("mineral.calcium", UNSET)

        nutrient_saturated = d.pop("nutrient.saturated", UNSET)

        vitamin_b6 = d.pop("vitamin.b6", UNSET)

        nutrient_protein = d.pop("nutrient.protein", UNSET)

        nutrient_dietaryfiber = d.pop("nutrient.dietaryfiber", UNSET)

        energy_energy = d.pop("energy.energy", UNSET)

        nutrient_polyunsaturated = d.pop("nutrient.polyunsaturated", UNSET)

        nutrient_fat = d.pop("nutrient.fat", UNSET)

        nutrient_carb = d.pop("nutrient.carb", UNSET)

        recipe_draft_nutrients = cls(
            nutrient_salt=nutrient_salt,
            nutrient_monounsaturated=nutrient_monounsaturated,
            nutrient_sugar=nutrient_sugar,
            mineral_calcium=mineral_calcium,
            nutrient_saturated=nutrient_saturated,
            vitamin_b6=vitamin_b6,
            nutrient_protein=nutrient_protein,
            nutrient_dietaryfiber=nutrient_dietaryfiber,
            energy_energy=energy_energy,
            nutrient_polyunsaturated=nutrient_polyunsaturated,
            nutrient_fat=nutrient_fat,
            nutrient_carb=nutrient_carb,
        )

        recipe_draft_nutrients.additional_properties = d
        return recipe_draft_nutrients

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
