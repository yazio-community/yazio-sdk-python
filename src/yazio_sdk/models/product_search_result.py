from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nutrient_summary import NutrientSummary


T = TypeVar("T", bound="ProductSearchResult")


@_attrs_define
class ProductSearchResult:
    """
    Attributes:
        score (float | Unset):
        name (str | Unset):
        product_id (str | Unset):
        serving (str | Unset):
        serving_quantity (float | Unset):
        amount (float | Unset):
        base_unit (str | Unset):
        producer (str | Unset):
        is_verified (bool | Unset):
        nutrients (NutrientSummary | Unset):
        countries (list[str] | Unset):
        language (str | Unset):
    """

    score: float | Unset = UNSET
    name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    serving: str | Unset = UNSET
    serving_quantity: float | Unset = UNSET
    amount: float | Unset = UNSET
    base_unit: str | Unset = UNSET
    producer: str | Unset = UNSET
    is_verified: bool | Unset = UNSET
    nutrients: NutrientSummary | Unset = UNSET
    countries: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        name = self.name

        product_id = self.product_id

        serving = self.serving

        serving_quantity = self.serving_quantity

        amount = self.amount

        base_unit = self.base_unit

        producer = self.producer

        is_verified = self.is_verified

        nutrients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrients, Unset):
            nutrients = self.nutrients.to_dict()

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if name is not UNSET:
            field_dict["name"] = name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if serving is not UNSET:
            field_dict["serving"] = serving
        if serving_quantity is not UNSET:
            field_dict["serving_quantity"] = serving_quantity
        if amount is not UNSET:
            field_dict["amount"] = amount
        if base_unit is not UNSET:
            field_dict["base_unit"] = base_unit
        if producer is not UNSET:
            field_dict["producer"] = producer
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if nutrients is not UNSET:
            field_dict["nutrients"] = nutrients
        if countries is not UNSET:
            field_dict["countries"] = countries
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nutrient_summary import NutrientSummary

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        name = d.pop("name", UNSET)

        product_id = d.pop("product_id", UNSET)

        serving = d.pop("serving", UNSET)

        serving_quantity = d.pop("serving_quantity", UNSET)

        amount = d.pop("amount", UNSET)

        base_unit = d.pop("base_unit", UNSET)

        producer = d.pop("producer", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        _nutrients = d.pop("nutrients", UNSET)
        nutrients: NutrientSummary | Unset
        if isinstance(_nutrients, Unset):
            nutrients = UNSET
        else:
            nutrients = NutrientSummary.from_dict(_nutrients)

        countries = cast(list[str], d.pop("countries", UNSET))

        language = d.pop("language", UNSET)

        product_search_result = cls(
            score=score,
            name=name,
            product_id=product_id,
            serving=serving,
            serving_quantity=serving_quantity,
            amount=amount,
            base_unit=base_unit,
            producer=producer,
            is_verified=is_verified,
            nutrients=nutrients,
            countries=countries,
            language=language,
        )

        product_search_result.additional_properties = d
        return product_search_result

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
