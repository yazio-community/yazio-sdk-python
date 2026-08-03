from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meal_summary import MealSummary


T = TypeVar("T", bound="DailySummaryWidgetMeals")


@_attrs_define
class DailySummaryWidgetMeals:
    """
    Attributes:
        breakfast (MealSummary | Unset):
        lunch (MealSummary | Unset):
        dinner (MealSummary | Unset):
        snack (MealSummary | Unset):
    """

    breakfast: MealSummary | Unset = UNSET
    lunch: MealSummary | Unset = UNSET
    dinner: MealSummary | Unset = UNSET
    snack: MealSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakfast: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakfast, Unset):
            breakfast = self.breakfast.to_dict()

        lunch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lunch, Unset):
            lunch = self.lunch.to_dict()

        dinner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dinner, Unset):
            dinner = self.dinner.to_dict()

        snack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snack, Unset):
            snack = self.snack.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakfast is not UNSET:
            field_dict["breakfast"] = breakfast
        if lunch is not UNSET:
            field_dict["lunch"] = lunch
        if dinner is not UNSET:
            field_dict["dinner"] = dinner
        if snack is not UNSET:
            field_dict["snack"] = snack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meal_summary import MealSummary

        d = dict(src_dict)
        _breakfast = d.pop("breakfast", UNSET)
        breakfast: MealSummary | Unset
        if isinstance(_breakfast, Unset):
            breakfast = UNSET
        else:
            breakfast = MealSummary.from_dict(_breakfast)

        _lunch = d.pop("lunch", UNSET)
        lunch: MealSummary | Unset
        if isinstance(_lunch, Unset):
            lunch = UNSET
        else:
            lunch = MealSummary.from_dict(_lunch)

        _dinner = d.pop("dinner", UNSET)
        dinner: MealSummary | Unset
        if isinstance(_dinner, Unset):
            dinner = UNSET
        else:
            dinner = MealSummary.from_dict(_dinner)

        _snack = d.pop("snack", UNSET)
        snack: MealSummary | Unset
        if isinstance(_snack, Unset):
            snack = UNSET
        else:
            snack = MealSummary.from_dict(_snack)

        daily_summary_widget_meals = cls(
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            snack=snack,
        )

        daily_summary_widget_meals.additional_properties = d
        return daily_summary_widget_meals

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
