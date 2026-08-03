from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FastingParticipants")


@_attrs_define
class FastingParticipants:
    """
    Attributes:
        initial_number_of_participants (float | Unset):
        growth_per_year (float | Unset):
        growth_start (str | Unset):
    """

    initial_number_of_participants: float | Unset = UNSET
    growth_per_year: float | Unset = UNSET
    growth_start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initial_number_of_participants = self.initial_number_of_participants

        growth_per_year = self.growth_per_year

        growth_start = self.growth_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_number_of_participants is not UNSET:
            field_dict["initial_number_of_participants"] = initial_number_of_participants
        if growth_per_year is not UNSET:
            field_dict["growth_per_year"] = growth_per_year
        if growth_start is not UNSET:
            field_dict["growth_start"] = growth_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial_number_of_participants = d.pop("initial_number_of_participants", UNSET)

        growth_per_year = d.pop("growth_per_year", UNSET)

        growth_start = d.pop("growth_start", UNSET)

        fasting_participants = cls(
            initial_number_of_participants=initial_number_of_participants,
            growth_per_year=growth_per_year,
            growth_start=growth_start,
        )

        fasting_participants.additional_properties = d
        return fasting_participants

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
