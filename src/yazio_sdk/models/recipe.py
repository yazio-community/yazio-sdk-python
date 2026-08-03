from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipe_available_since_type_0 import RecipeAvailableSinceType0
    from ..models.recipe_image_type_0 import RecipeImageType0
    from ..models.recipe_nutrients import RecipeNutrients
    from ..models.recipe_servings_item import RecipeServingsItem
    from ..models.recipe_yazio_id_type_0 import RecipeYazioIdType0


T = TypeVar("T", bound="Recipe")


@_attrs_define
class Recipe:
    """
    Attributes:
        id (str | Unset):
        yazio_id (None | RecipeYazioIdType0 | Unset):
        locale (str | Unset):
        name (str | Unset):
        portion_count (float | Unset):
        nutrients (RecipeNutrients | Unset):
        image (None | RecipeImageType0 | Unset):
        servings (list[RecipeServingsItem] | Unset):
        instructions (list[Any] | Unset):
        is_yazio_recipe (bool | Unset):
        available_since (None | RecipeAvailableSinceType0 | Unset):
        is_pro_recipe (bool | Unset):
    """

    id: str | Unset = UNSET
    yazio_id: None | RecipeYazioIdType0 | Unset = UNSET
    locale: str | Unset = UNSET
    name: str | Unset = UNSET
    portion_count: float | Unset = UNSET
    nutrients: RecipeNutrients | Unset = UNSET
    image: None | RecipeImageType0 | Unset = UNSET
    servings: list[RecipeServingsItem] | Unset = UNSET
    instructions: list[Any] | Unset = UNSET
    is_yazio_recipe: bool | Unset = UNSET
    available_since: None | RecipeAvailableSinceType0 | Unset = UNSET
    is_pro_recipe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_available_since_type_0 import RecipeAvailableSinceType0
        from ..models.recipe_image_type_0 import RecipeImageType0
        from ..models.recipe_yazio_id_type_0 import RecipeYazioIdType0

        id = self.id

        yazio_id: dict[str, Any] | None | Unset
        if isinstance(self.yazio_id, Unset):
            yazio_id = UNSET
        elif isinstance(self.yazio_id, RecipeYazioIdType0):
            yazio_id = self.yazio_id.to_dict()
        else:
            yazio_id = self.yazio_id

        locale = self.locale

        name = self.name

        portion_count = self.portion_count

        nutrients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrients, Unset):
            nutrients = self.nutrients.to_dict()

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, RecipeImageType0):
            image = self.image.to_dict()
        else:
            image = self.image

        servings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servings, Unset):
            servings = []
            for servings_item_data in self.servings:
                servings_item = servings_item_data.to_dict()
                servings.append(servings_item)

        instructions: list[Any] | Unset = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = self.instructions

        is_yazio_recipe = self.is_yazio_recipe

        available_since: dict[str, Any] | None | Unset
        if isinstance(self.available_since, Unset):
            available_since = UNSET
        elif isinstance(self.available_since, RecipeAvailableSinceType0):
            available_since = self.available_since.to_dict()
        else:
            available_since = self.available_since

        is_pro_recipe = self.is_pro_recipe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if yazio_id is not UNSET:
            field_dict["yazio_id"] = yazio_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name
        if portion_count is not UNSET:
            field_dict["portion_count"] = portion_count
        if nutrients is not UNSET:
            field_dict["nutrients"] = nutrients
        if image is not UNSET:
            field_dict["image"] = image
        if servings is not UNSET:
            field_dict["servings"] = servings
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_yazio_recipe is not UNSET:
            field_dict["is_yazio_recipe"] = is_yazio_recipe
        if available_since is not UNSET:
            field_dict["available_since"] = available_since
        if is_pro_recipe is not UNSET:
            field_dict["is_pro_recipe"] = is_pro_recipe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_available_since_type_0 import RecipeAvailableSinceType0
        from ..models.recipe_image_type_0 import RecipeImageType0
        from ..models.recipe_nutrients import RecipeNutrients
        from ..models.recipe_servings_item import RecipeServingsItem
        from ..models.recipe_yazio_id_type_0 import RecipeYazioIdType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_yazio_id(data: object) -> None | RecipeYazioIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                yazio_id_type_0 = RecipeYazioIdType0.from_dict(data)

                return yazio_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeYazioIdType0 | Unset, data)

        yazio_id = _parse_yazio_id(d.pop("yazio_id", UNSET))

        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        portion_count = d.pop("portion_count", UNSET)

        _nutrients = d.pop("nutrients", UNSET)
        nutrients: RecipeNutrients | Unset
        if isinstance(_nutrients, Unset):
            nutrients = UNSET
        else:
            nutrients = RecipeNutrients.from_dict(_nutrients)

        def _parse_image(data: object) -> None | RecipeImageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = RecipeImageType0.from_dict(data)

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeImageType0 | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        _servings = d.pop("servings", UNSET)
        servings: list[RecipeServingsItem] | Unset = UNSET
        if _servings is not UNSET:
            servings = []
            for servings_item_data in _servings:
                servings_item = RecipeServingsItem.from_dict(servings_item_data)

                servings.append(servings_item)

        instructions = cast(list[Any], d.pop("instructions", UNSET))

        is_yazio_recipe = d.pop("is_yazio_recipe", UNSET)

        def _parse_available_since(data: object) -> None | RecipeAvailableSinceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                available_since_type_0 = RecipeAvailableSinceType0.from_dict(data)

                return available_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeAvailableSinceType0 | Unset, data)

        available_since = _parse_available_since(d.pop("available_since", UNSET))

        is_pro_recipe = d.pop("is_pro_recipe", UNSET)

        recipe = cls(
            id=id,
            yazio_id=yazio_id,
            locale=locale,
            name=name,
            portion_count=portion_count,
            nutrients=nutrients,
            image=image,
            servings=servings,
            instructions=instructions,
            is_yazio_recipe=is_yazio_recipe,
            available_since=available_since,
            is_pro_recipe=is_pro_recipe,
        )

        recipe.additional_properties = d
        return recipe

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
