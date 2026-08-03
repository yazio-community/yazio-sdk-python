from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShopItemsItemsItem")


@_attrs_define
class ShopItemsItemsItem:
    """
    Attributes:
        shop_item_type (str | Unset):
        currency_type (str | Unset):
        currency_quantity (float | Unset):
    """

    shop_item_type: str | Unset = UNSET
    currency_type: str | Unset = UNSET
    currency_quantity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_item_type = self.shop_item_type

        currency_type = self.currency_type

        currency_quantity = self.currency_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_item_type is not UNSET:
            field_dict["shop_item_type"] = shop_item_type
        if currency_type is not UNSET:
            field_dict["currency_type"] = currency_type
        if currency_quantity is not UNSET:
            field_dict["currency_quantity"] = currency_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shop_item_type = d.pop("shop_item_type", UNSET)

        currency_type = d.pop("currency_type", UNSET)

        currency_quantity = d.pop("currency_quantity", UNSET)

        shop_items_items_item = cls(
            shop_item_type=shop_item_type,
            currency_type=currency_type,
            currency_quantity=currency_quantity,
        )

        shop_items_items_item.additional_properties = d
        return shop_items_items_item

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
