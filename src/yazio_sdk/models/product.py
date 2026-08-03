from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_nutrients import ProductNutrients
    from ..models.product_servings_item import ProductServingsItem


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """Response of GET /v22/products/{id}. Absent from the capture, which only recorded an OPTIONS preflight; filled in
    from a live response. Note that the body carries no id of its own.

        Attributes:
            name (str | Unset):
            producer (None | str | Unset):
            category (str | Unset):
            base_unit (str | Unset):
            is_verified (bool | Unset):
            is_private (bool | Unset):
            is_deleted (bool | Unset):
            has_ean (bool | Unset):
            nutrients (ProductNutrients | Unset):
            servings (list[ProductServingsItem] | Unset):
            eans (list[str] | Unset):
            language (str | Unset):
            countries (list[str] | Unset):
            updated_at (str | Unset):
    """

    name: str | Unset = UNSET
    producer: None | str | Unset = UNSET
    category: str | Unset = UNSET
    base_unit: str | Unset = UNSET
    is_verified: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    has_ean: bool | Unset = UNSET
    nutrients: ProductNutrients | Unset = UNSET
    servings: list[ProductServingsItem] | Unset = UNSET
    eans: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    countries: list[str] | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        producer: None | str | Unset
        if isinstance(self.producer, Unset):
            producer = UNSET
        else:
            producer = self.producer

        category = self.category

        base_unit = self.base_unit

        is_verified = self.is_verified

        is_private = self.is_private

        is_deleted = self.is_deleted

        has_ean = self.has_ean

        nutrients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrients, Unset):
            nutrients = self.nutrients.to_dict()

        servings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servings, Unset):
            servings = []
            for servings_item_data in self.servings:
                servings_item = servings_item_data.to_dict()
                servings.append(servings_item)

        eans: list[str] | Unset = UNSET
        if not isinstance(self.eans, Unset):
            eans = self.eans

        language = self.language

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if producer is not UNSET:
            field_dict["producer"] = producer
        if category is not UNSET:
            field_dict["category"] = category
        if base_unit is not UNSET:
            field_dict["base_unit"] = base_unit
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if has_ean is not UNSET:
            field_dict["has_ean"] = has_ean
        if nutrients is not UNSET:
            field_dict["nutrients"] = nutrients
        if servings is not UNSET:
            field_dict["servings"] = servings
        if eans is not UNSET:
            field_dict["eans"] = eans
        if language is not UNSET:
            field_dict["language"] = language
        if countries is not UNSET:
            field_dict["countries"] = countries
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_nutrients import ProductNutrients
        from ..models.product_servings_item import ProductServingsItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_producer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        producer = _parse_producer(d.pop("producer", UNSET))

        category = d.pop("category", UNSET)

        base_unit = d.pop("base_unit", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        is_private = d.pop("is_private", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        has_ean = d.pop("has_ean", UNSET)

        _nutrients = d.pop("nutrients", UNSET)
        nutrients: ProductNutrients | Unset
        if isinstance(_nutrients, Unset):
            nutrients = UNSET
        else:
            nutrients = ProductNutrients.from_dict(_nutrients)

        _servings = d.pop("servings", UNSET)
        servings: list[ProductServingsItem] | Unset = UNSET
        if _servings is not UNSET:
            servings = []
            for servings_item_data in _servings:
                servings_item = ProductServingsItem.from_dict(servings_item_data)

                servings.append(servings_item)

        eans = cast(list[str], d.pop("eans", UNSET))

        language = d.pop("language", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        product = cls(
            name=name,
            producer=producer,
            category=category,
            base_unit=base_unit,
            is_verified=is_verified,
            is_private=is_private,
            is_deleted=is_deleted,
            has_ean=has_ean,
            nutrients=nutrients,
            servings=servings,
            eans=eans,
            language=language,
            countries=countries,
            updated_at=updated_at,
        )

        product.additional_properties = d
        return product

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
