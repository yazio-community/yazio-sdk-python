from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipe_draft_nutrients import RecipeDraftNutrients
    from ..models.recipe_draft_servings_item import RecipeDraftServingsItem


T = TypeVar("T", bound="RecipeDraft")


@_attrs_define
class RecipeDraft:
    """
    Attributes:
        nutrients (RecipeDraftNutrients | Unset):
        portion_count (int | Unset):
        servings (list[RecipeDraftServingsItem] | Unset):
        instructions (list[str] | Unset):
        name (str | Unset):
        id (str | Unset):
    """

    nutrients: RecipeDraftNutrients | Unset = UNSET
    portion_count: int | Unset = UNSET
    servings: list[RecipeDraftServingsItem] | Unset = UNSET
    instructions: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nutrients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrients, Unset):
            nutrients = self.nutrients.to_dict()

        portion_count = self.portion_count

        servings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servings, Unset):
            servings = []
            for servings_item_data in self.servings:
                servings_item = servings_item_data.to_dict()
                servings.append(servings_item)

        instructions: list[str] | Unset = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = self.instructions

        name = self.name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nutrients is not UNSET:
            field_dict["nutrients"] = nutrients
        if portion_count is not UNSET:
            field_dict["portion_count"] = portion_count
        if servings is not UNSET:
            field_dict["servings"] = servings
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_draft_nutrients import RecipeDraftNutrients
        from ..models.recipe_draft_servings_item import RecipeDraftServingsItem

        d = dict(src_dict)
        _nutrients = d.pop("nutrients", UNSET)
        nutrients: RecipeDraftNutrients | Unset
        if isinstance(_nutrients, Unset):
            nutrients = UNSET
        else:
            nutrients = RecipeDraftNutrients.from_dict(_nutrients)

        portion_count = d.pop("portion_count", UNSET)

        _servings = d.pop("servings", UNSET)
        servings: list[RecipeDraftServingsItem] | Unset = UNSET
        if _servings is not UNSET:
            servings = []
            for servings_item_data in _servings:
                servings_item = RecipeDraftServingsItem.from_dict(servings_item_data)

                servings.append(servings_item)

        instructions = cast(list[str], d.pop("instructions", UNSET))

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        recipe_draft = cls(
            nutrients=nutrients,
            portion_count=portion_count,
            servings=servings,
            instructions=instructions,
            name=name,
            id=id,
        )

        recipe_draft.additional_properties = d
        return recipe_draft

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
