from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_log_activity_source_type_0 import ExerciseLogActivitySourceType0


T = TypeVar("T", bound="ExerciseLogActivity")


@_attrs_define
class ExerciseLogActivity:
    """
    Attributes:
        energy (float | Unset):
        distance (float | Unset):
        duration (float | Unset):
        source (ExerciseLogActivitySourceType0 | None | Unset):
        gateway (str | Unset):
        steps (float | Unset):
    """

    energy: float | Unset = UNSET
    distance: float | Unset = UNSET
    duration: float | Unset = UNSET
    source: ExerciseLogActivitySourceType0 | None | Unset = UNSET
    gateway: str | Unset = UNSET
    steps: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exercise_log_activity_source_type_0 import ExerciseLogActivitySourceType0

        energy = self.energy

        distance = self.distance

        duration = self.duration

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, ExerciseLogActivitySourceType0):
            source = self.source.to_dict()
        else:
            source = self.source

        gateway = self.gateway

        steps = self.steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy is not UNSET:
            field_dict["energy"] = energy
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration
        if source is not UNSET:
            field_dict["source"] = source
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_log_activity_source_type_0 import ExerciseLogActivitySourceType0

        d = dict(src_dict)
        energy = d.pop("energy", UNSET)

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        def _parse_source(data: object) -> ExerciseLogActivitySourceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = ExerciseLogActivitySourceType0.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExerciseLogActivitySourceType0 | None | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        gateway = d.pop("gateway", UNSET)

        steps = d.pop("steps", UNSET)

        exercise_log_activity = cls(
            energy=energy,
            distance=distance,
            duration=duration,
            source=source,
            gateway=gateway,
            steps=steps,
        )

        exercise_log_activity.additional_properties = d
        return exercise_log_activity

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
