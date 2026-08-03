from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumedItemsDeletion")


@_attrs_define
class ConsumedItemsDeletion:
    """Body of DELETE /v22/user/consumed-items. Each property names one entry by id, as a single string rather than a list
    — passing an array is rejected with "This value should be of type string". Note that the endpoint also accepts an
    `?id=` query parameter, answers 204, and does nothing at all.

        Attributes:
            products (str | Unset):
            recipe_portions (str | Unset):
            simple_products (str | Unset):
    """

    products: str | Unset = UNSET
    recipe_portions: str | Unset = UNSET
    simple_products: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = self.products

        recipe_portions = self.recipe_portions

        simple_products = self.simple_products

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products
        if recipe_portions is not UNSET:
            field_dict["recipe_portions"] = recipe_portions
        if simple_products is not UNSET:
            field_dict["simple_products"] = simple_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        products = d.pop("products", UNSET)

        recipe_portions = d.pop("recipe_portions", UNSET)

        simple_products = d.pop("simple_products", UNSET)

        consumed_items_deletion = cls(
            products=products,
            recipe_portions=recipe_portions,
            simple_products=simple_products,
        )

        consumed_items_deletion.additional_properties = d
        return consumed_items_deletion

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
