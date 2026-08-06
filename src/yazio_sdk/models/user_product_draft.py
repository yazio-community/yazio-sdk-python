from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_product_draft_nutrients import UserProductDraftNutrients
    from ..models.user_product_draft_servings_item import UserProductDraftServingsItem


T = TypeVar("T", bound="UserProductDraft")


@_attrs_define
class UserProductDraft:
    """Request body of POST /v22/user/products.

    Attributes:
        id (str | Unset):
        name (str | Unset):
        category (str | Unset):
        base_unit (str | Unset):
        is_private (bool | Unset):
        producer (str | Unset):
        nutrients (UserProductDraftNutrients | Unset):
        servings (list[UserProductDraftServingsItem] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    category: str | Unset = UNSET
    base_unit: str | Unset = UNSET
    is_private: bool | Unset = UNSET
    producer: str | Unset = UNSET
    nutrients: UserProductDraftNutrients | Unset = UNSET
    servings: list[UserProductDraftServingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        category = self.category

        base_unit = self.base_unit

        is_private = self.is_private

        producer = self.producer

        nutrients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrients, Unset):
            nutrients = self.nutrients.to_dict()

        servings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servings, Unset):
            servings = []
            for servings_item_data in self.servings:
                servings_item = servings_item_data.to_dict()
                servings.append(servings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if base_unit is not UNSET:
            field_dict["base_unit"] = base_unit
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if producer is not UNSET:
            field_dict["producer"] = producer
        if nutrients is not UNSET:
            field_dict["nutrients"] = nutrients
        if servings is not UNSET:
            field_dict["servings"] = servings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_product_draft_nutrients import UserProductDraftNutrients
        from ..models.user_product_draft_servings_item import UserProductDraftServingsItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        category = d.pop("category", UNSET)

        base_unit = d.pop("base_unit", UNSET)

        is_private = d.pop("is_private", UNSET)

        producer = d.pop("producer", UNSET)

        _nutrients = d.pop("nutrients", UNSET)
        nutrients: UserProductDraftNutrients | Unset
        if isinstance(_nutrients, Unset):
            nutrients = UNSET
        else:
            nutrients = UserProductDraftNutrients.from_dict(_nutrients)

        _servings = d.pop("servings", UNSET)
        servings: list[UserProductDraftServingsItem] | Unset = UNSET
        if _servings is not UNSET:
            servings = []
            for servings_item_data in _servings:
                servings_item = UserProductDraftServingsItem.from_dict(servings_item_data)

                servings.append(servings_item)

        user_product_draft = cls(
            id=id,
            name=name,
            category=category,
            base_unit=base_unit,
            is_private=is_private,
            producer=producer,
            nutrients=nutrients,
            servings=servings,
        )

        user_product_draft.additional_properties = d
        return user_product_draft

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
