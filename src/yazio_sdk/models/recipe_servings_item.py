from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recipe_servings_item_note_type_0 import RecipeServingsItemNoteType0
    from ..models.recipe_servings_item_serving_quantity_type_0 import (
        RecipeServingsItemServingQuantityType0,
    )
    from ..models.recipe_servings_item_serving_type_0 import RecipeServingsItemServingType0


T = TypeVar("T", bound="RecipeServingsItem")


@_attrs_define
class RecipeServingsItem:
    """
    Attributes:
        producer (str | Unset):
        name (str | Unset):
        amount (float | Unset):
        serving (None | RecipeServingsItemServingType0 | Unset):
        serving_quantity (None | RecipeServingsItemServingQuantityType0 | Unset):
        base_unit (str | Unset):
        note (None | RecipeServingsItemNoteType0 | Unset):
        product_id (str | Unset):
    """

    producer: str | Unset = UNSET
    name: str | Unset = UNSET
    amount: float | Unset = UNSET
    serving: None | RecipeServingsItemServingType0 | Unset = UNSET
    serving_quantity: None | RecipeServingsItemServingQuantityType0 | Unset = UNSET
    base_unit: str | Unset = UNSET
    note: None | RecipeServingsItemNoteType0 | Unset = UNSET
    product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_servings_item_note_type_0 import RecipeServingsItemNoteType0
        from ..models.recipe_servings_item_serving_quantity_type_0 import (
            RecipeServingsItemServingQuantityType0,
        )
        from ..models.recipe_servings_item_serving_type_0 import RecipeServingsItemServingType0

        producer = self.producer

        name = self.name

        amount = self.amount

        serving: dict[str, Any] | None | Unset
        if isinstance(self.serving, Unset):
            serving = UNSET
        elif isinstance(self.serving, RecipeServingsItemServingType0):
            serving = self.serving.to_dict()
        else:
            serving = self.serving

        serving_quantity: dict[str, Any] | None | Unset
        if isinstance(self.serving_quantity, Unset):
            serving_quantity = UNSET
        elif isinstance(self.serving_quantity, RecipeServingsItemServingQuantityType0):
            serving_quantity = self.serving_quantity.to_dict()
        else:
            serving_quantity = self.serving_quantity

        base_unit = self.base_unit

        note: dict[str, Any] | None | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        elif isinstance(self.note, RecipeServingsItemNoteType0):
            note = self.note.to_dict()
        else:
            note = self.note

        product_id = self.product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if producer is not UNSET:
            field_dict["producer"] = producer
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if serving is not UNSET:
            field_dict["serving"] = serving
        if serving_quantity is not UNSET:
            field_dict["serving_quantity"] = serving_quantity
        if base_unit is not UNSET:
            field_dict["base_unit"] = base_unit
        if note is not UNSET:
            field_dict["note"] = note
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_servings_item_note_type_0 import RecipeServingsItemNoteType0
        from ..models.recipe_servings_item_serving_quantity_type_0 import (
            RecipeServingsItemServingQuantityType0,
        )
        from ..models.recipe_servings_item_serving_type_0 import RecipeServingsItemServingType0

        d = dict(src_dict)
        producer = d.pop("producer", UNSET)

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        def _parse_serving(data: object) -> None | RecipeServingsItemServingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                serving_type_0 = RecipeServingsItemServingType0.from_dict(data)

                return serving_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeServingsItemServingType0 | Unset, data)

        serving = _parse_serving(d.pop("serving", UNSET))

        def _parse_serving_quantity(
            data: object,
        ) -> None | RecipeServingsItemServingQuantityType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                serving_quantity_type_0 = RecipeServingsItemServingQuantityType0.from_dict(data)

                return serving_quantity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeServingsItemServingQuantityType0 | Unset, data)

        serving_quantity = _parse_serving_quantity(d.pop("serving_quantity", UNSET))

        base_unit = d.pop("base_unit", UNSET)

        def _parse_note(data: object) -> None | RecipeServingsItemNoteType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                note_type_0 = RecipeServingsItemNoteType0.from_dict(data)

                return note_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeServingsItemNoteType0 | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        product_id = d.pop("product_id", UNSET)

        recipe_servings_item = cls(
            producer=producer,
            name=name,
            amount=amount,
            serving=serving,
            serving_quantity=serving_quantity,
            base_unit=base_unit,
            note=note,
            product_id=product_id,
        )

        recipe_servings_item.additional_properties = d
        return recipe_servings_item

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
