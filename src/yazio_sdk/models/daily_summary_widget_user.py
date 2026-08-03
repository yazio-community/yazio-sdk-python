from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailySummaryWidgetUser")


@_attrs_define
class DailySummaryWidgetUser:
    """
    Attributes:
        start_weight (float | Unset):
        current_weight (float | Unset):
        goal (str | Unset):
        sex (str | Unset):
    """

    start_weight: float | Unset = UNSET
    current_weight: float | Unset = UNSET
    goal: str | Unset = UNSET
    sex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_weight = self.start_weight

        current_weight = self.current_weight

        goal = self.goal

        sex = self.sex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_weight is not UNSET:
            field_dict["start_weight"] = start_weight
        if current_weight is not UNSET:
            field_dict["current_weight"] = current_weight
        if goal is not UNSET:
            field_dict["goal"] = goal
        if sex is not UNSET:
            field_dict["sex"] = sex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_weight = d.pop("start_weight", UNSET)

        current_weight = d.pop("current_weight", UNSET)

        goal = d.pop("goal", UNSET)

        sex = d.pop("sex", UNSET)

        daily_summary_widget_user = cls(
            start_weight=start_weight,
            current_weight=current_weight,
            goal=goal,
            sex=sex,
        )

        daily_summary_widget_user.additional_properties = d
        return daily_summary_widget_user

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
