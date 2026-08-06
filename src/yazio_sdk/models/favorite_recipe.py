from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FavoriteRecipe")


@_attrs_define
class FavoriteRecipe:
    """A favorited recipe with the portion count the user favorited it at. Used both as the request body of PUT
    /v22/user/favorites/recipes and as the item shape of GET /v22/user/favorites/recipe.

        Attributes:
            id (str | Unset):
            recipe_id (str | Unset):
            portion_count (float | Unset):
            yazio_id (None | str | Unset): Present on GET /v22/user/favorites/recipe for YAZIO recipes; not sent when
                favoriting. Null for user-created recipes.
    """

    id: str | Unset = UNSET
    recipe_id: str | Unset = UNSET
    portion_count: float | Unset = UNSET
    yazio_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipe_id = self.recipe_id

        portion_count = self.portion_count

        yazio_id: None | str | Unset
        if isinstance(self.yazio_id, Unset):
            yazio_id = UNSET
        else:
            yazio_id = self.yazio_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if portion_count is not UNSET:
            field_dict["portion_count"] = portion_count
        if yazio_id is not UNSET:
            field_dict["yazio_id"] = yazio_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        recipe_id = d.pop("recipe_id", UNSET)

        portion_count = d.pop("portion_count", UNSET)

        def _parse_yazio_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yazio_id = _parse_yazio_id(d.pop("yazio_id", UNSET))

        favorite_recipe = cls(
            id=id,
            recipe_id=recipe_id,
            portion_count=portion_count,
            yazio_id=yazio_id,
        )

        favorite_recipe.additional_properties = d
        return favorite_recipe

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
