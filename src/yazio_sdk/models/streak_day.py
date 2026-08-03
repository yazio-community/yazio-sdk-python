from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreakDay")


@_attrs_define
class StreakDay:
    """
    Attributes:
        daytimes (list[str] | Unset):
        streak_count (float | Unset):
        freeze_count (float | Unset):
        origin_of_recovery (str | Unset):
    """

    daytimes: list[str] | Unset = UNSET
    streak_count: float | Unset = UNSET
    freeze_count: float | Unset = UNSET
    origin_of_recovery: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daytimes: list[str] | Unset = UNSET
        if not isinstance(self.daytimes, Unset):
            daytimes = self.daytimes

        streak_count = self.streak_count

        freeze_count = self.freeze_count

        origin_of_recovery = self.origin_of_recovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daytimes is not UNSET:
            field_dict["daytimes"] = daytimes
        if streak_count is not UNSET:
            field_dict["streak_count"] = streak_count
        if freeze_count is not UNSET:
            field_dict["freeze_count"] = freeze_count
        if origin_of_recovery is not UNSET:
            field_dict["origin_of_recovery"] = origin_of_recovery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daytimes = cast(list[str], d.pop("daytimes", UNSET))

        streak_count = d.pop("streak_count", UNSET)

        freeze_count = d.pop("freeze_count", UNSET)

        origin_of_recovery = d.pop("origin_of_recovery", UNSET)

        streak_day = cls(
            daytimes=daytimes,
            streak_count=streak_count,
            freeze_count=freeze_count,
            origin_of_recovery=origin_of_recovery,
        )

        streak_day.additional_properties = d
        return streak_day

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
