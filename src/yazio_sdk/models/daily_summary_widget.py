from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_goals import DailyGoals
    from ..models.daily_summary_widget_active_fasting_countdown_template_key_type_0 import (
        DailySummaryWidgetActiveFastingCountdownTemplateKeyType0,
    )
    from ..models.daily_summary_widget_meals import DailySummaryWidgetMeals
    from ..models.daily_summary_widget_units import DailySummaryWidgetUnits
    from ..models.daily_summary_widget_user import DailySummaryWidgetUser


T = TypeVar("T", bound="DailySummaryWidget")


@_attrs_define
class DailySummaryWidget:
    """
    Attributes:
        activity_energy (float | Unset):
        consume_activity_energy (bool | Unset):
        steps (float | Unset):
        water_intake (float | Unset):
        goals (DailyGoals | Unset):
        units (DailySummaryWidgetUnits | Unset):
        meals (DailySummaryWidgetMeals | Unset):
        user (DailySummaryWidgetUser | Unset):
        active_fasting_countdown_template_key (DailySummaryWidgetActiveFastingCountdownTemplateKeyType0 | None | Unset):
    """

    activity_energy: float | Unset = UNSET
    consume_activity_energy: bool | Unset = UNSET
    steps: float | Unset = UNSET
    water_intake: float | Unset = UNSET
    goals: DailyGoals | Unset = UNSET
    units: DailySummaryWidgetUnits | Unset = UNSET
    meals: DailySummaryWidgetMeals | Unset = UNSET
    user: DailySummaryWidgetUser | Unset = UNSET
    active_fasting_countdown_template_key: (
        DailySummaryWidgetActiveFastingCountdownTemplateKeyType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.daily_summary_widget_active_fasting_countdown_template_key_type_0 import (
            DailySummaryWidgetActiveFastingCountdownTemplateKeyType0,
        )

        activity_energy = self.activity_energy

        consume_activity_energy = self.consume_activity_energy

        steps = self.steps

        water_intake = self.water_intake

        goals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goals, Unset):
            goals = self.goals.to_dict()

        units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = self.units.to_dict()

        meals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meals, Unset):
            meals = self.meals.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        active_fasting_countdown_template_key: dict[str, Any] | None | Unset
        if isinstance(self.active_fasting_countdown_template_key, Unset):
            active_fasting_countdown_template_key = UNSET
        elif isinstance(
            self.active_fasting_countdown_template_key,
            DailySummaryWidgetActiveFastingCountdownTemplateKeyType0,
        ):
            active_fasting_countdown_template_key = (
                self.active_fasting_countdown_template_key.to_dict()
            )
        else:
            active_fasting_countdown_template_key = self.active_fasting_countdown_template_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_energy is not UNSET:
            field_dict["activity_energy"] = activity_energy
        if consume_activity_energy is not UNSET:
            field_dict["consume_activity_energy"] = consume_activity_energy
        if steps is not UNSET:
            field_dict["steps"] = steps
        if water_intake is not UNSET:
            field_dict["water_intake"] = water_intake
        if goals is not UNSET:
            field_dict["goals"] = goals
        if units is not UNSET:
            field_dict["units"] = units
        if meals is not UNSET:
            field_dict["meals"] = meals
        if user is not UNSET:
            field_dict["user"] = user
        if active_fasting_countdown_template_key is not UNSET:
            field_dict["active_fasting_countdown_template_key"] = (
                active_fasting_countdown_template_key
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_goals import DailyGoals
        from ..models.daily_summary_widget_active_fasting_countdown_template_key_type_0 import (
            DailySummaryWidgetActiveFastingCountdownTemplateKeyType0,
        )
        from ..models.daily_summary_widget_meals import DailySummaryWidgetMeals
        from ..models.daily_summary_widget_units import DailySummaryWidgetUnits
        from ..models.daily_summary_widget_user import DailySummaryWidgetUser

        d = dict(src_dict)
        activity_energy = d.pop("activity_energy", UNSET)

        consume_activity_energy = d.pop("consume_activity_energy", UNSET)

        steps = d.pop("steps", UNSET)

        water_intake = d.pop("water_intake", UNSET)

        _goals = d.pop("goals", UNSET)
        goals: DailyGoals | Unset
        if isinstance(_goals, Unset):
            goals = UNSET
        else:
            goals = DailyGoals.from_dict(_goals)

        _units = d.pop("units", UNSET)
        units: DailySummaryWidgetUnits | Unset
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = DailySummaryWidgetUnits.from_dict(_units)

        _meals = d.pop("meals", UNSET)
        meals: DailySummaryWidgetMeals | Unset
        if isinstance(_meals, Unset):
            meals = UNSET
        else:
            meals = DailySummaryWidgetMeals.from_dict(_meals)

        _user = d.pop("user", UNSET)
        user: DailySummaryWidgetUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DailySummaryWidgetUser.from_dict(_user)

        def _parse_active_fasting_countdown_template_key(
            data: object,
        ) -> DailySummaryWidgetActiveFastingCountdownTemplateKeyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_fasting_countdown_template_key_type_0 = (
                    DailySummaryWidgetActiveFastingCountdownTemplateKeyType0.from_dict(data)
                )

                return active_fasting_countdown_template_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DailySummaryWidgetActiveFastingCountdownTemplateKeyType0 | None | Unset, data
            )

        active_fasting_countdown_template_key = _parse_active_fasting_countdown_template_key(
            d.pop("active_fasting_countdown_template_key", UNSET)
        )

        daily_summary_widget = cls(
            activity_energy=activity_energy,
            consume_activity_energy=consume_activity_energy,
            steps=steps,
            water_intake=water_intake,
            goals=goals,
            units=units,
            meals=meals,
            user=user,
            active_fasting_countdown_template_key=active_fasting_countdown_template_key,
        )

        daily_summary_widget.additional_properties = d
        return daily_summary_widget

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
