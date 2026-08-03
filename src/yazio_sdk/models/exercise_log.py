from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_log_activity import ExerciseLogActivity


T = TypeVar("T", bound="ExerciseLog")


@_attrs_define
class ExerciseLog:
    """
    Attributes:
        training (list[Any] | Unset):
        custom_training (list[Any] | Unset):
        activity (ExerciseLogActivity | Unset):
    """

    training: list[Any] | Unset = UNSET
    custom_training: list[Any] | Unset = UNSET
    activity: ExerciseLogActivity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        training: list[Any] | Unset = UNSET
        if not isinstance(self.training, Unset):
            training = self.training

        custom_training: list[Any] | Unset = UNSET
        if not isinstance(self.custom_training, Unset):
            custom_training = self.custom_training

        activity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if training is not UNSET:
            field_dict["training"] = training
        if custom_training is not UNSET:
            field_dict["custom_training"] = custom_training
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_log_activity import ExerciseLogActivity

        d = dict(src_dict)
        training = cast(list[Any], d.pop("training", UNSET))

        custom_training = cast(list[Any], d.pop("custom_training", UNSET))

        _activity = d.pop("activity", UNSET)
        activity: ExerciseLogActivity | Unset
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ExerciseLogActivity.from_dict(_activity)

        exercise_log = cls(
            training=training,
            custom_training=custom_training,
            activity=activity,
        )

        exercise_log.additional_properties = d
        return exercise_log

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
