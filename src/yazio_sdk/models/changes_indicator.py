from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangesIndicator")


@_attrs_define
class ChangesIndicator:
    """
    Attributes:
        exercises (float | Unset):
        body_values (float | Unset):
        consumed_items (float | Unset):
    """

    exercises: float | Unset = UNSET
    body_values: float | Unset = UNSET
    consumed_items: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercises = self.exercises

        body_values = self.body_values

        consumed_items = self.consumed_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exercises is not UNSET:
            field_dict["exercises"] = exercises
        if body_values is not UNSET:
            field_dict["body_values"] = body_values
        if consumed_items is not UNSET:
            field_dict["consumed_items"] = consumed_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exercises = d.pop("exercises", UNSET)

        body_values = d.pop("body_values", UNSET)

        consumed_items = d.pop("consumed_items", UNSET)

        changes_indicator = cls(
            exercises=exercises,
            body_values=body_values,
            consumed_items=consumed_items,
        )

        changes_indicator.additional_properties = d
        return changes_indicator

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
