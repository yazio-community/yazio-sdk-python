from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuggestedProduct")


@_attrs_define
class SuggestedProduct:
    """
    Attributes:
        product_id (str | Unset):
        amount (float | Unset):
        serving (str | Unset):
        serving_quantity (float | Unset):
    """

    product_id: str | Unset = UNSET
    amount: float | Unset = UNSET
    serving: str | Unset = UNSET
    serving_quantity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        amount = self.amount

        serving = self.serving

        serving_quantity = self.serving_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if serving is not UNSET:
            field_dict["serving"] = serving
        if serving_quantity is not UNSET:
            field_dict["serving_quantity"] = serving_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        amount = d.pop("amount", UNSET)

        serving = d.pop("serving", UNSET)

        serving_quantity = d.pop("serving_quantity", UNSET)

        suggested_product = cls(
            product_id=product_id,
            amount=amount,
            serving=serving,
            serving_quantity=serving_quantity,
        )

        suggested_product.additional_properties = d
        return suggested_product

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
