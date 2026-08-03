from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consumed_items_products_item import ConsumedItemsProductsItem
    from ..models.consumed_recipe_portion import ConsumedRecipePortion


T = TypeVar("T", bound="ConsumedItems")


@_attrs_define
class ConsumedItems:
    """
    Attributes:
        products (list[ConsumedItemsProductsItem] | Unset):
        recipe_portions (list[ConsumedRecipePortion] | Unset):
        simple_products (list[Any] | Unset):
    """

    products: list[ConsumedItemsProductsItem] | Unset = UNSET
    recipe_portions: list[ConsumedRecipePortion] | Unset = UNSET
    simple_products: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        recipe_portions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recipe_portions, Unset):
            recipe_portions = []
            for recipe_portions_item_data in self.recipe_portions:
                recipe_portions_item = recipe_portions_item_data.to_dict()
                recipe_portions.append(recipe_portions_item)

        simple_products: list[Any] | Unset = UNSET
        if not isinstance(self.simple_products, Unset):
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
        from ..models.consumed_items_products_item import ConsumedItemsProductsItem
        from ..models.consumed_recipe_portion import ConsumedRecipePortion

        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[ConsumedItemsProductsItem] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = ConsumedItemsProductsItem.from_dict(products_item_data)

                products.append(products_item)

        _recipe_portions = d.pop("recipe_portions", UNSET)
        recipe_portions: list[ConsumedRecipePortion] | Unset = UNSET
        if _recipe_portions is not UNSET:
            recipe_portions = []
            for recipe_portions_item_data in _recipe_portions:
                recipe_portions_item = ConsumedRecipePortion.from_dict(recipe_portions_item_data)

                recipe_portions.append(recipe_portions_item)

        simple_products = cast(list[Any], d.pop("simple_products", UNSET))

        consumed_items = cls(
            products=products,
            recipe_portions=recipe_portions,
            simple_products=simple_products,
        )

        consumed_items.additional_properties = d
        return consumed_items

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
