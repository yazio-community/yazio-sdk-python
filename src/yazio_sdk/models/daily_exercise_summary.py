from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyExerciseSummary")


@_attrs_define
class DailyExerciseSummary:
    """
    Attributes:
        date (str | Unset):
        duration (float | Unset):
        steps (float | Unset):
        energy (float | Unset):
    """

    date: str | Unset = UNSET
    duration: float | Unset = UNSET
    steps: float | Unset = UNSET
    energy: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        duration = self.duration

        steps = self.steps

        energy = self.energy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if steps is not UNSET:
            field_dict["steps"] = steps
        if energy is not UNSET:
            field_dict["energy"] = energy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        duration = d.pop("duration", UNSET)

        steps = d.pop("steps", UNSET)

        energy = d.pop("energy", UNSET)

        daily_exercise_summary = cls(
            date=date,
            duration=duration,
            steps=steps,
            energy=energy,
        )

        daily_exercise_summary.additional_properties = d
        return daily_exercise_summary

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
