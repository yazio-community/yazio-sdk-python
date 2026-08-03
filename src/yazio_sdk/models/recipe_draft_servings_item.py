from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipeDraftServingsItem")


@_attrs_define
class RecipeDraftServingsItem:
    """
    Attributes:
        amount (float | Unset):
        serving (str | Unset):
        producer (str | Unset):
        name (str | Unset):
        serving_quantity (float | Unset):
        base_unit (str | Unset):
        product_id (str | Unset):
    """

    amount: float | Unset = UNSET
    serving: str | Unset = UNSET
    producer: str | Unset = UNSET
    name: str | Unset = UNSET
    serving_quantity: float | Unset = UNSET
    base_unit: str | Unset = UNSET
    product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        serving = self.serving

        producer = self.producer

        name = self.name

        serving_quantity = self.serving_quantity

        base_unit = self.base_unit

        product_id = self.product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if serving is not UNSET:
            field_dict["serving"] = serving
        if producer is not UNSET:
            field_dict["producer"] = producer
        if name is not UNSET:
            field_dict["name"] = name
        if serving_quantity is not UNSET:
            field_dict["serving_quantity"] = serving_quantity
        if base_unit is not UNSET:
            field_dict["base_unit"] = base_unit
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        serving = d.pop("serving", UNSET)

        producer = d.pop("producer", UNSET)

        name = d.pop("name", UNSET)

        serving_quantity = d.pop("serving_quantity", UNSET)

        base_unit = d.pop("base_unit", UNSET)

        product_id = d.pop("product_id", UNSET)

        recipe_draft_servings_item = cls(
            amount=amount,
            serving=serving,
            producer=producer,
            name=name,
            serving_quantity=serving_quantity,
            base_unit=base_unit,
            product_id=product_id,
        )

        recipe_draft_servings_item.additional_properties = d
        return recipe_draft_servings_item

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
