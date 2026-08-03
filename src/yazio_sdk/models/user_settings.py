from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettings")


@_attrs_define
class UserSettings:
    """
    Attributes:
        has_water_tracker (bool | Unset):
        has_diary_tipps (bool | Unset):
        has_meal_reminders (bool | Unset):
        has_usage_reminders (bool | Unset):
        has_weight_reminders (bool | Unset):
        has_water_reminders (bool | Unset):
        consume_activity_calories (bool | Unset):
        has_feelings (bool | Unset):
        has_fasting_tracker_reminders (bool | Unset):
        has_fasting_stage_reminders (bool | Unset):
    """

    has_water_tracker: bool | Unset = UNSET
    has_diary_tipps: bool | Unset = UNSET
    has_meal_reminders: bool | Unset = UNSET
    has_usage_reminders: bool | Unset = UNSET
    has_weight_reminders: bool | Unset = UNSET
    has_water_reminders: bool | Unset = UNSET
    consume_activity_calories: bool | Unset = UNSET
    has_feelings: bool | Unset = UNSET
    has_fasting_tracker_reminders: bool | Unset = UNSET
    has_fasting_stage_reminders: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_water_tracker = self.has_water_tracker

        has_diary_tipps = self.has_diary_tipps

        has_meal_reminders = self.has_meal_reminders

        has_usage_reminders = self.has_usage_reminders

        has_weight_reminders = self.has_weight_reminders

        has_water_reminders = self.has_water_reminders

        consume_activity_calories = self.consume_activity_calories

        has_feelings = self.has_feelings

        has_fasting_tracker_reminders = self.has_fasting_tracker_reminders

        has_fasting_stage_reminders = self.has_fasting_stage_reminders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_water_tracker is not UNSET:
            field_dict["has_water_tracker"] = has_water_tracker
        if has_diary_tipps is not UNSET:
            field_dict["has_diary_tipps"] = has_diary_tipps
        if has_meal_reminders is not UNSET:
            field_dict["has_meal_reminders"] = has_meal_reminders
        if has_usage_reminders is not UNSET:
            field_dict["has_usage_reminders"] = has_usage_reminders
        if has_weight_reminders is not UNSET:
            field_dict["has_weight_reminders"] = has_weight_reminders
        if has_water_reminders is not UNSET:
            field_dict["has_water_reminders"] = has_water_reminders
        if consume_activity_calories is not UNSET:
            field_dict["consume_activity_calories"] = consume_activity_calories
        if has_feelings is not UNSET:
            field_dict["has_feelings"] = has_feelings
        if has_fasting_tracker_reminders is not UNSET:
            field_dict["has_fasting_tracker_reminders"] = has_fasting_tracker_reminders
        if has_fasting_stage_reminders is not UNSET:
            field_dict["has_fasting_stage_reminders"] = has_fasting_stage_reminders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_water_tracker = d.pop("has_water_tracker", UNSET)

        has_diary_tipps = d.pop("has_diary_tipps", UNSET)

        has_meal_reminders = d.pop("has_meal_reminders", UNSET)

        has_usage_reminders = d.pop("has_usage_reminders", UNSET)

        has_weight_reminders = d.pop("has_weight_reminders", UNSET)

        has_water_reminders = d.pop("has_water_reminders", UNSET)

        consume_activity_calories = d.pop("consume_activity_calories", UNSET)

        has_feelings = d.pop("has_feelings", UNSET)

        has_fasting_tracker_reminders = d.pop("has_fasting_tracker_reminders", UNSET)

        has_fasting_stage_reminders = d.pop("has_fasting_stage_reminders", UNSET)

        user_settings = cls(
            has_water_tracker=has_water_tracker,
            has_diary_tipps=has_diary_tipps,
            has_meal_reminders=has_meal_reminders,
            has_usage_reminders=has_usage_reminders,
            has_weight_reminders=has_weight_reminders,
            has_water_reminders=has_water_reminders,
            consume_activity_calories=consume_activity_calories,
            has_feelings=has_feelings,
            has_fasting_tracker_reminders=has_fasting_tracker_reminders,
            has_fasting_stage_reminders=has_fasting_stage_reminders,
        )

        user_settings.additional_properties = d
        return user_settings

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
