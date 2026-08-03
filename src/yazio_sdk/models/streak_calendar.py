from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.streak_day import StreakDay


T = TypeVar("T", bound="StreakCalendar")


@_attrs_define
class StreakCalendar:
    """
    Attributes:
        field_1970_01_01 (StreakDay | Unset):
    """

    field_1970_01_01: StreakDay | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_1970_01_01: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_1970_01_01, Unset):
            field_1970_01_01 = self.field_1970_01_01.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_1970_01_01 is not UNSET:
            field_dict["1970-01-01"] = field_1970_01_01

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.streak_day import StreakDay

        d = dict(src_dict)
        _field_1970_01_01 = d.pop("1970-01-01", UNSET)
        field_1970_01_01: StreakDay | Unset
        if isinstance(_field_1970_01_01, Unset):
            field_1970_01_01 = UNSET
        else:
            field_1970_01_01 = StreakDay.from_dict(_field_1970_01_01)

        streak_calendar = cls(
            field_1970_01_01=field_1970_01_01,
        )

        streak_calendar.additional_properties = d
        return streak_calendar

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
