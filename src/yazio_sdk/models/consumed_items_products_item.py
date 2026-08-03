from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumedItemsProductsItem")


@_attrs_define
class ConsumedItemsProductsItem:
    """
    Attributes:
        id (str | Unset):
        serving (None | str | Unset):
        amount (float | Unset):
        daytime (str | Unset):
        date (str | Unset):
        type_ (str | Unset):
        product_id (str | Unset):
        serving_quantity (float | None | Unset):
    """

    id: str | Unset = UNSET
    serving: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    daytime: str | Unset = UNSET
    date: str | Unset = UNSET
    type_: str | Unset = UNSET
    product_id: str | Unset = UNSET
    serving_quantity: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        serving: None | str | Unset
        if isinstance(self.serving, Unset):
            serving = UNSET
        else:
            serving = self.serving

        amount = self.amount

        daytime = self.daytime

        date = self.date

        type_ = self.type_

        product_id = self.product_id

        serving_quantity: float | None | Unset
        if isinstance(self.serving_quantity, Unset):
            serving_quantity = UNSET
        else:
            serving_quantity = self.serving_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if serving is not UNSET:
            field_dict["serving"] = serving
        if amount is not UNSET:
            field_dict["amount"] = amount
        if daytime is not UNSET:
            field_dict["daytime"] = daytime
        if date is not UNSET:
            field_dict["date"] = date
        if type_ is not UNSET:
            field_dict["type"] = type_
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if serving_quantity is not UNSET:
            field_dict["serving_quantity"] = serving_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_serving(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serving = _parse_serving(d.pop("serving", UNSET))

        amount = d.pop("amount", UNSET)

        daytime = d.pop("daytime", UNSET)

        date = d.pop("date", UNSET)

        type_ = d.pop("type", UNSET)

        product_id = d.pop("product_id", UNSET)

        def _parse_serving_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        serving_quantity = _parse_serving_quantity(d.pop("serving_quantity", UNSET))

        consumed_items_products_item = cls(
            id=id,
            serving=serving,
            amount=amount,
            daytime=daytime,
            date=date,
            type_=type_,
            product_id=product_id,
            serving_quantity=serving_quantity,
        )

        consumed_items_products_item.additional_properties = d
        return consumed_items_products_item

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
