from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseEntryActivityItem")


@_attrs_define
class ExerciseEntryActivityItem:
    """
    Attributes:
        date (str | Unset):
        energy (float | Unset):
        steps (float | Unset):
        distance (float | Unset):
        gateway (str | Unset):
    """

    date: str | Unset = UNSET
    energy: float | Unset = UNSET
    steps: float | Unset = UNSET
    distance: float | Unset = UNSET
    gateway: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        energy = self.energy

        steps = self.steps

        distance = self.distance

        gateway = self.gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if energy is not UNSET:
            field_dict["energy"] = energy
        if steps is not UNSET:
            field_dict["steps"] = steps
        if distance is not UNSET:
            field_dict["distance"] = distance
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        energy = d.pop("energy", UNSET)

        steps = d.pop("steps", UNSET)

        distance = d.pop("distance", UNSET)

        gateway = d.pop("gateway", UNSET)

        exercise_entry_activity_item = cls(
            date=date,
            energy=energy,
            steps=steps,
            distance=distance,
            gateway=gateway,
        )

        exercise_entry_activity_item.additional_properties = d
        return exercise_entry_activity_item

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
