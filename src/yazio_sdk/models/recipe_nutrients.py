from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipeNutrients")


@_attrs_define
class RecipeNutrients:
    """
    Attributes:
        energy_energy (float | Unset):
        mineral_arsenic (float | Unset):
        mineral_boron (float | Unset):
        mineral_calcium (float | Unset):
        mineral_chlorine (float | Unset):
        mineral_chrome (float | Unset):
        mineral_copper (float | Unset):
        mineral_fluoride (float | Unset):
        mineral_fluorine (float | Unset):
        mineral_iodine (float | Unset):
        mineral_iron (float | Unset):
        mineral_magnesium (float | Unset):
        mineral_manganese (float | Unset):
        mineral_phosphorus (float | Unset):
        mineral_potassium (float | Unset):
        mineral_selenium (float | Unset):
        mineral_sulfur (float | Unset):
        mineral_zinc (float | Unset):
        nutrient_alcohol (float | Unset):
        nutrient_carb (float | Unset):
        nutrient_cholesterol (float | Unset):
        nutrient_dietaryfiber (float | Unset):
        nutrient_fat (float | Unset):
        nutrient_monounsaturated (float | Unset):
        nutrient_polyunsaturated (float | Unset):
        nutrient_protein (float | Unset):
        nutrient_salt (float | Unset):
        nutrient_saturated (float | Unset):
        nutrient_sodium (float | Unset):
        nutrient_sugar (float | Unset):
        nutrient_water (float | Unset):
        vitamin_a (float | Unset):
        vitamin_b1 (float | Unset):
        vitamin_b11 (float | Unset):
        vitamin_b12 (float | Unset):
        vitamin_b2 (float | Unset):
        vitamin_b3 (float | Unset):
        vitamin_b5 (float | Unset):
        vitamin_b6 (float | Unset):
        vitamin_b7 (float | Unset):
        vitamin_c (float | Unset):
        vitamin_d (float | Unset):
        vitamin_e (float | Unset):
        vitamin_k (float | Unset):
    """

    energy_energy: float | Unset = UNSET
    mineral_arsenic: float | Unset = UNSET
    mineral_boron: float | Unset = UNSET
    mineral_calcium: float | Unset = UNSET
    mineral_chlorine: float | Unset = UNSET
    mineral_chrome: float | Unset = UNSET
    mineral_copper: float | Unset = UNSET
    mineral_fluoride: float | Unset = UNSET
    mineral_fluorine: float | Unset = UNSET
    mineral_iodine: float | Unset = UNSET
    mineral_iron: float | Unset = UNSET
    mineral_magnesium: float | Unset = UNSET
    mineral_manganese: float | Unset = UNSET
    mineral_phosphorus: float | Unset = UNSET
    mineral_potassium: float | Unset = UNSET
    mineral_selenium: float | Unset = UNSET
    mineral_sulfur: float | Unset = UNSET
    mineral_zinc: float | Unset = UNSET
    nutrient_alcohol: float | Unset = UNSET
    nutrient_carb: float | Unset = UNSET
    nutrient_cholesterol: float | Unset = UNSET
    nutrient_dietaryfiber: float | Unset = UNSET
    nutrient_fat: float | Unset = UNSET
    nutrient_monounsaturated: float | Unset = UNSET
    nutrient_polyunsaturated: float | Unset = UNSET
    nutrient_protein: float | Unset = UNSET
    nutrient_salt: float | Unset = UNSET
    nutrient_saturated: float | Unset = UNSET
    nutrient_sodium: float | Unset = UNSET
    nutrient_sugar: float | Unset = UNSET
    nutrient_water: float | Unset = UNSET
    vitamin_a: float | Unset = UNSET
    vitamin_b1: float | Unset = UNSET
    vitamin_b11: float | Unset = UNSET
    vitamin_b12: float | Unset = UNSET
    vitamin_b2: float | Unset = UNSET
    vitamin_b3: float | Unset = UNSET
    vitamin_b5: float | Unset = UNSET
    vitamin_b6: float | Unset = UNSET
    vitamin_b7: float | Unset = UNSET
    vitamin_c: float | Unset = UNSET
    vitamin_d: float | Unset = UNSET
    vitamin_e: float | Unset = UNSET
    vitamin_k: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_energy = self.energy_energy

        mineral_arsenic = self.mineral_arsenic

        mineral_boron = self.mineral_boron

        mineral_calcium = self.mineral_calcium

        mineral_chlorine = self.mineral_chlorine

        mineral_chrome = self.mineral_chrome

        mineral_copper = self.mineral_copper

        mineral_fluoride = self.mineral_fluoride

        mineral_fluorine = self.mineral_fluorine

        mineral_iodine = self.mineral_iodine

        mineral_iron = self.mineral_iron

        mineral_magnesium = self.mineral_magnesium

        mineral_manganese = self.mineral_manganese

        mineral_phosphorus = self.mineral_phosphorus

        mineral_potassium = self.mineral_potassium

        mineral_selenium = self.mineral_selenium

        mineral_sulfur = self.mineral_sulfur

        mineral_zinc = self.mineral_zinc

        nutrient_alcohol = self.nutrient_alcohol

        nutrient_carb = self.nutrient_carb

        nutrient_cholesterol = self.nutrient_cholesterol

        nutrient_dietaryfiber = self.nutrient_dietaryfiber

        nutrient_fat = self.nutrient_fat

        nutrient_monounsaturated = self.nutrient_monounsaturated

        nutrient_polyunsaturated = self.nutrient_polyunsaturated

        nutrient_protein = self.nutrient_protein

        nutrient_salt = self.nutrient_salt

        nutrient_saturated = self.nutrient_saturated

        nutrient_sodium = self.nutrient_sodium

        nutrient_sugar = self.nutrient_sugar

        nutrient_water = self.nutrient_water

        vitamin_a = self.vitamin_a

        vitamin_b1 = self.vitamin_b1

        vitamin_b11 = self.vitamin_b11

        vitamin_b12 = self.vitamin_b12

        vitamin_b2 = self.vitamin_b2

        vitamin_b3 = self.vitamin_b3

        vitamin_b5 = self.vitamin_b5

        vitamin_b6 = self.vitamin_b6

        vitamin_b7 = self.vitamin_b7

        vitamin_c = self.vitamin_c

        vitamin_d = self.vitamin_d

        vitamin_e = self.vitamin_e

        vitamin_k = self.vitamin_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy_energy is not UNSET:
            field_dict["energy.energy"] = energy_energy
        if mineral_arsenic is not UNSET:
            field_dict["mineral.arsenic"] = mineral_arsenic
        if mineral_boron is not UNSET:
            field_dict["mineral.boron"] = mineral_boron
        if mineral_calcium is not UNSET:
            field_dict["mineral.calcium"] = mineral_calcium
        if mineral_chlorine is not UNSET:
            field_dict["mineral.chlorine"] = mineral_chlorine
        if mineral_chrome is not UNSET:
            field_dict["mineral.chrome"] = mineral_chrome
        if mineral_copper is not UNSET:
            field_dict["mineral.copper"] = mineral_copper
        if mineral_fluoride is not UNSET:
            field_dict["mineral.fluoride"] = mineral_fluoride
        if mineral_fluorine is not UNSET:
            field_dict["mineral.fluorine"] = mineral_fluorine
        if mineral_iodine is not UNSET:
            field_dict["mineral.iodine"] = mineral_iodine
        if mineral_iron is not UNSET:
            field_dict["mineral.iron"] = mineral_iron
        if mineral_magnesium is not UNSET:
            field_dict["mineral.magnesium"] = mineral_magnesium
        if mineral_manganese is not UNSET:
            field_dict["mineral.manganese"] = mineral_manganese
        if mineral_phosphorus is not UNSET:
            field_dict["mineral.phosphorus"] = mineral_phosphorus
        if mineral_potassium is not UNSET:
            field_dict["mineral.potassium"] = mineral_potassium
        if mineral_selenium is not UNSET:
            field_dict["mineral.selenium"] = mineral_selenium
        if mineral_sulfur is not UNSET:
            field_dict["mineral.sulfur"] = mineral_sulfur
        if mineral_zinc is not UNSET:
            field_dict["mineral.zinc"] = mineral_zinc
        if nutrient_alcohol is not UNSET:
            field_dict["nutrient.alcohol"] = nutrient_alcohol
        if nutrient_carb is not UNSET:
            field_dict["nutrient.carb"] = nutrient_carb
        if nutrient_cholesterol is not UNSET:
            field_dict["nutrient.cholesterol"] = nutrient_cholesterol
        if nutrient_dietaryfiber is not UNSET:
            field_dict["nutrient.dietaryfiber"] = nutrient_dietaryfiber
        if nutrient_fat is not UNSET:
            field_dict["nutrient.fat"] = nutrient_fat
        if nutrient_monounsaturated is not UNSET:
            field_dict["nutrient.monounsaturated"] = nutrient_monounsaturated
        if nutrient_polyunsaturated is not UNSET:
            field_dict["nutrient.polyunsaturated"] = nutrient_polyunsaturated
        if nutrient_protein is not UNSET:
            field_dict["nutrient.protein"] = nutrient_protein
        if nutrient_salt is not UNSET:
            field_dict["nutrient.salt"] = nutrient_salt
        if nutrient_saturated is not UNSET:
            field_dict["nutrient.saturated"] = nutrient_saturated
        if nutrient_sodium is not UNSET:
            field_dict["nutrient.sodium"] = nutrient_sodium
        if nutrient_sugar is not UNSET:
            field_dict["nutrient.sugar"] = nutrient_sugar
        if nutrient_water is not UNSET:
            field_dict["nutrient.water"] = nutrient_water
        if vitamin_a is not UNSET:
            field_dict["vitamin.a"] = vitamin_a
        if vitamin_b1 is not UNSET:
            field_dict["vitamin.b1"] = vitamin_b1
        if vitamin_b11 is not UNSET:
            field_dict["vitamin.b11"] = vitamin_b11
        if vitamin_b12 is not UNSET:
            field_dict["vitamin.b12"] = vitamin_b12
        if vitamin_b2 is not UNSET:
            field_dict["vitamin.b2"] = vitamin_b2
        if vitamin_b3 is not UNSET:
            field_dict["vitamin.b3"] = vitamin_b3
        if vitamin_b5 is not UNSET:
            field_dict["vitamin.b5"] = vitamin_b5
        if vitamin_b6 is not UNSET:
            field_dict["vitamin.b6"] = vitamin_b6
        if vitamin_b7 is not UNSET:
            field_dict["vitamin.b7"] = vitamin_b7
        if vitamin_c is not UNSET:
            field_dict["vitamin.c"] = vitamin_c
        if vitamin_d is not UNSET:
            field_dict["vitamin.d"] = vitamin_d
        if vitamin_e is not UNSET:
            field_dict["vitamin.e"] = vitamin_e
        if vitamin_k is not UNSET:
            field_dict["vitamin.k"] = vitamin_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        energy_energy = d.pop("energy.energy", UNSET)

        mineral_arsenic = d.pop("mineral.arsenic", UNSET)

        mineral_boron = d.pop("mineral.boron", UNSET)

        mineral_calcium = d.pop("mineral.calcium", UNSET)

        mineral_chlorine = d.pop("mineral.chlorine", UNSET)

        mineral_chrome = d.pop("mineral.chrome", UNSET)

        mineral_copper = d.pop("mineral.copper", UNSET)

        mineral_fluoride = d.pop("mineral.fluoride", UNSET)

        mineral_fluorine = d.pop("mineral.fluorine", UNSET)

        mineral_iodine = d.pop("mineral.iodine", UNSET)

        mineral_iron = d.pop("mineral.iron", UNSET)

        mineral_magnesium = d.pop("mineral.magnesium", UNSET)

        mineral_manganese = d.pop("mineral.manganese", UNSET)

        mineral_phosphorus = d.pop("mineral.phosphorus", UNSET)

        mineral_potassium = d.pop("mineral.potassium", UNSET)

        mineral_selenium = d.pop("mineral.selenium", UNSET)

        mineral_sulfur = d.pop("mineral.sulfur", UNSET)

        mineral_zinc = d.pop("mineral.zinc", UNSET)

        nutrient_alcohol = d.pop("nutrient.alcohol", UNSET)

        nutrient_carb = d.pop("nutrient.carb", UNSET)

        nutrient_cholesterol = d.pop("nutrient.cholesterol", UNSET)

        nutrient_dietaryfiber = d.pop("nutrient.dietaryfiber", UNSET)

        nutrient_fat = d.pop("nutrient.fat", UNSET)

        nutrient_monounsaturated = d.pop("nutrient.monounsaturated", UNSET)

        nutrient_polyunsaturated = d.pop("nutrient.polyunsaturated", UNSET)

        nutrient_protein = d.pop("nutrient.protein", UNSET)

        nutrient_salt = d.pop("nutrient.salt", UNSET)

        nutrient_saturated = d.pop("nutrient.saturated", UNSET)

        nutrient_sodium = d.pop("nutrient.sodium", UNSET)

        nutrient_sugar = d.pop("nutrient.sugar", UNSET)

        nutrient_water = d.pop("nutrient.water", UNSET)

        vitamin_a = d.pop("vitamin.a", UNSET)

        vitamin_b1 = d.pop("vitamin.b1", UNSET)

        vitamin_b11 = d.pop("vitamin.b11", UNSET)

        vitamin_b12 = d.pop("vitamin.b12", UNSET)

        vitamin_b2 = d.pop("vitamin.b2", UNSET)

        vitamin_b3 = d.pop("vitamin.b3", UNSET)

        vitamin_b5 = d.pop("vitamin.b5", UNSET)

        vitamin_b6 = d.pop("vitamin.b6", UNSET)

        vitamin_b7 = d.pop("vitamin.b7", UNSET)

        vitamin_c = d.pop("vitamin.c", UNSET)

        vitamin_d = d.pop("vitamin.d", UNSET)

        vitamin_e = d.pop("vitamin.e", UNSET)

        vitamin_k = d.pop("vitamin.k", UNSET)

        recipe_nutrients = cls(
            energy_energy=energy_energy,
            mineral_arsenic=mineral_arsenic,
            mineral_boron=mineral_boron,
            mineral_calcium=mineral_calcium,
            mineral_chlorine=mineral_chlorine,
            mineral_chrome=mineral_chrome,
            mineral_copper=mineral_copper,
            mineral_fluoride=mineral_fluoride,
            mineral_fluorine=mineral_fluorine,
            mineral_iodine=mineral_iodine,
            mineral_iron=mineral_iron,
            mineral_magnesium=mineral_magnesium,
            mineral_manganese=mineral_manganese,
            mineral_phosphorus=mineral_phosphorus,
            mineral_potassium=mineral_potassium,
            mineral_selenium=mineral_selenium,
            mineral_sulfur=mineral_sulfur,
            mineral_zinc=mineral_zinc,
            nutrient_alcohol=nutrient_alcohol,
            nutrient_carb=nutrient_carb,
            nutrient_cholesterol=nutrient_cholesterol,
            nutrient_dietaryfiber=nutrient_dietaryfiber,
            nutrient_fat=nutrient_fat,
            nutrient_monounsaturated=nutrient_monounsaturated,
            nutrient_polyunsaturated=nutrient_polyunsaturated,
            nutrient_protein=nutrient_protein,
            nutrient_salt=nutrient_salt,
            nutrient_saturated=nutrient_saturated,
            nutrient_sodium=nutrient_sodium,
            nutrient_sugar=nutrient_sugar,
            nutrient_water=nutrient_water,
            vitamin_a=vitamin_a,
            vitamin_b1=vitamin_b1,
            vitamin_b11=vitamin_b11,
            vitamin_b12=vitamin_b12,
            vitamin_b2=vitamin_b2,
            vitamin_b3=vitamin_b3,
            vitamin_b5=vitamin_b5,
            vitamin_b6=vitamin_b6,
            vitamin_b7=vitamin_b7,
            vitamin_c=vitamin_c,
            vitamin_d=vitamin_d,
            vitamin_e=vitamin_e,
            vitamin_k=vitamin_k,
        )

        recipe_nutrients.additional_properties = d
        return recipe_nutrients

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
