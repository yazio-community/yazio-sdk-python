from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fasting_participants import FastingParticipants
    from ..models.fasting_template import FastingTemplate
    from ..models.fasting_template_group_fasting_calorie_goal_type_0 import (
        FastingTemplateGroupFastingCalorieGoalType0,
    )
    from ..models.fasting_template_group_teaser_position_type_0 import (
        FastingTemplateGroupTeaserPositionType0,
    )


T = TypeVar("T", bound="FastingTemplateGroup")


@_attrs_define
class FastingTemplateGroup:
    """
    Attributes:
        group_name (str | Unset):
        participants (FastingParticipants | Unset):
        cycle_duration_in_days (float | Unset):
        emoji (str | Unset):
        title (str | Unset):
        subtitle (str | Unset):
        teaser (str | Unset):
        goals (list[str] | Unset):
        flexibility (str | Unset):
        difficulty (str | Unset):
        fasting_calorie_goal (FastingTemplateGroupFastingCalorieGoalType0 | None | Unset):
        free (bool | Unset):
        type_ (str | Unset):
        teaser_position (FastingTemplateGroupTeaserPositionType0 | None | Unset):
        templates (list[FastingTemplate] | Unset):
    """

    group_name: str | Unset = UNSET
    participants: FastingParticipants | Unset = UNSET
    cycle_duration_in_days: float | Unset = UNSET
    emoji: str | Unset = UNSET
    title: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    teaser: str | Unset = UNSET
    goals: list[str] | Unset = UNSET
    flexibility: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    fasting_calorie_goal: FastingTemplateGroupFastingCalorieGoalType0 | None | Unset = UNSET
    free: bool | Unset = UNSET
    type_: str | Unset = UNSET
    teaser_position: FastingTemplateGroupTeaserPositionType0 | None | Unset = UNSET
    templates: list[FastingTemplate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fasting_template_group_fasting_calorie_goal_type_0 import (
            FastingTemplateGroupFastingCalorieGoalType0,
        )
        from ..models.fasting_template_group_teaser_position_type_0 import (
            FastingTemplateGroupTeaserPositionType0,
        )

        group_name = self.group_name

        participants: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants.to_dict()

        cycle_duration_in_days = self.cycle_duration_in_days

        emoji = self.emoji

        title = self.title

        subtitle = self.subtitle

        teaser = self.teaser

        goals: list[str] | Unset = UNSET
        if not isinstance(self.goals, Unset):
            goals = self.goals

        flexibility = self.flexibility

        difficulty = self.difficulty

        fasting_calorie_goal: dict[str, Any] | None | Unset
        if isinstance(self.fasting_calorie_goal, Unset):
            fasting_calorie_goal = UNSET
        elif isinstance(self.fasting_calorie_goal, FastingTemplateGroupFastingCalorieGoalType0):
            fasting_calorie_goal = self.fasting_calorie_goal.to_dict()
        else:
            fasting_calorie_goal = self.fasting_calorie_goal

        free = self.free

        type_ = self.type_

        teaser_position: dict[str, Any] | None | Unset
        if isinstance(self.teaser_position, Unset):
            teaser_position = UNSET
        elif isinstance(self.teaser_position, FastingTemplateGroupTeaserPositionType0):
            teaser_position = self.teaser_position.to_dict()
        else:
            teaser_position = self.teaser_position

        templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if participants is not UNSET:
            field_dict["participants"] = participants
        if cycle_duration_in_days is not UNSET:
            field_dict["cycle_duration_in_days"] = cycle_duration_in_days
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if teaser is not UNSET:
            field_dict["teaser"] = teaser
        if goals is not UNSET:
            field_dict["goals"] = goals
        if flexibility is not UNSET:
            field_dict["flexibility"] = flexibility
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if fasting_calorie_goal is not UNSET:
            field_dict["fasting_calorie_goal"] = fasting_calorie_goal
        if free is not UNSET:
            field_dict["free"] = free
        if type_ is not UNSET:
            field_dict["type"] = type_
        if teaser_position is not UNSET:
            field_dict["teaser_position"] = teaser_position
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fasting_participants import FastingParticipants
        from ..models.fasting_template import FastingTemplate
        from ..models.fasting_template_group_fasting_calorie_goal_type_0 import (
            FastingTemplateGroupFastingCalorieGoalType0,
        )
        from ..models.fasting_template_group_teaser_position_type_0 import (
            FastingTemplateGroupTeaserPositionType0,
        )

        d = dict(src_dict)
        group_name = d.pop("group_name", UNSET)

        _participants = d.pop("participants", UNSET)
        participants: FastingParticipants | Unset
        if isinstance(_participants, Unset):
            participants = UNSET
        else:
            participants = FastingParticipants.from_dict(_participants)

        cycle_duration_in_days = d.pop("cycle_duration_in_days", UNSET)

        emoji = d.pop("emoji", UNSET)

        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        teaser = d.pop("teaser", UNSET)

        goals = cast(list[str], d.pop("goals", UNSET))

        flexibility = d.pop("flexibility", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        def _parse_fasting_calorie_goal(
            data: object,
        ) -> FastingTemplateGroupFastingCalorieGoalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fasting_calorie_goal_type_0 = FastingTemplateGroupFastingCalorieGoalType0.from_dict(
                    data
                )

                return fasting_calorie_goal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FastingTemplateGroupFastingCalorieGoalType0 | None | Unset, data)

        fasting_calorie_goal = _parse_fasting_calorie_goal(d.pop("fasting_calorie_goal", UNSET))

        free = d.pop("free", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_teaser_position(
            data: object,
        ) -> FastingTemplateGroupTeaserPositionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                teaser_position_type_0 = FastingTemplateGroupTeaserPositionType0.from_dict(data)

                return teaser_position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FastingTemplateGroupTeaserPositionType0 | None | Unset, data)

        teaser_position = _parse_teaser_position(d.pop("teaser_position", UNSET))

        _templates = d.pop("templates", UNSET)
        templates: list[FastingTemplate] | Unset = UNSET
        if _templates is not UNSET:
            templates = []
            for templates_item_data in _templates:
                templates_item = FastingTemplate.from_dict(templates_item_data)

                templates.append(templates_item)

        fasting_template_group = cls(
            group_name=group_name,
            participants=participants,
            cycle_duration_in_days=cycle_duration_in_days,
            emoji=emoji,
            title=title,
            subtitle=subtitle,
            teaser=teaser,
            goals=goals,
            flexibility=flexibility,
            difficulty=difficulty,
            fasting_calorie_goal=fasting_calorie_goal,
            free=free,
            type_=type_,
            teaser_position=teaser_position,
            templates=templates,
        )

        fasting_template_group.additional_properties = d
        return fasting_template_group

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
