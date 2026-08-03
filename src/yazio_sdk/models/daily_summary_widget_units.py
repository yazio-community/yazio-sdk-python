from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailySummaryWidgetUnits")


@_attrs_define
class DailySummaryWidgetUnits:
    """
    Attributes:
        unit_mass (str | Unset):
        unit_energy (str | Unset):
        unit_serving (str | Unset):
        unit_length (str | Unset):
    """

    unit_mass: str | Unset = UNSET
    unit_energy: str | Unset = UNSET
    unit_serving: str | Unset = UNSET
    unit_length: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_mass = self.unit_mass

        unit_energy = self.unit_energy

        unit_serving = self.unit_serving

        unit_length = self.unit_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_mass is not UNSET:
            field_dict["unit_mass"] = unit_mass
        if unit_energy is not UNSET:
            field_dict["unit_energy"] = unit_energy
        if unit_serving is not UNSET:
            field_dict["unit_serving"] = unit_serving
        if unit_length is not UNSET:
            field_dict["unit_length"] = unit_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_mass = d.pop("unit_mass", UNSET)

        unit_energy = d.pop("unit_energy", UNSET)

        unit_serving = d.pop("unit_serving", UNSET)

        unit_length = d.pop("unit_length", UNSET)

        daily_summary_widget_units = cls(
            unit_mass=unit_mass,
            unit_energy=unit_energy,
            unit_serving=unit_serving,
            unit_length=unit_length,
        )

        daily_summary_widget_units.additional_properties = d
        return daily_summary_widget_units

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
