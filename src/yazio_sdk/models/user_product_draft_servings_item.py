from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.serving_unit import ServingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProductDraftServingsItem")


@_attrs_define
class UserProductDraftServingsItem:
    """
    Attributes:
        serving (ServingUnit | Unset): The fixed set of serving units offered when defining custom servings for a user-
            created product via POST /v22/user/products. Distinct from the free-form `serving` strings seen elsewhere (e.g.
            Product.yaml, SuggestedProduct.yaml), which come from the product database and are not limited to this list.
        amount (float | Unset):
    """

    serving: ServingUnit | Unset = UNSET
    amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serving: str | Unset = UNSET
        if not isinstance(self.serving, Unset):
            serving = self.serving.value

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serving is not UNSET:
            field_dict["serving"] = serving
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _serving = d.pop("serving", UNSET)
        serving: ServingUnit | Unset
        if isinstance(_serving, Unset):
            serving = UNSET
        else:
            serving = ServingUnit(_serving)

        amount = d.pop("amount", UNSET)

        user_product_draft_servings_item = cls(
            serving=serving,
            amount=amount,
        )

        user_product_draft_servings_item.additional_properties = d
        return user_product_draft_servings_item

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
