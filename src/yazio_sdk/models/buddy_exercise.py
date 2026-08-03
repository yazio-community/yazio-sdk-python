from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuddyExercise")


@_attrs_define
class BuddyExercise:
    """
    Attributes:
        steps (float | Unset):
        calories (float | Unset):
    """

    steps: float | Unset = UNSET
    calories: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = self.steps

        calories = self.calories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if steps is not UNSET:
            field_dict["steps"] = steps
        if calories is not UNSET:
            field_dict["calories"] = calories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        steps = d.pop("steps", UNSET)

        calories = d.pop("calories", UNSET)

        buddy_exercise = cls(
            steps=steps,
            calories=calories,
        )

        buddy_exercise.additional_properties = d
        return buddy_exercise

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
