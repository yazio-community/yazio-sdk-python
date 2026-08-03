from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fasting_period_boundary import FastingPeriodBoundary


T = TypeVar("T", bound="FastingTemplateFastingPeriodsItem")


@_attrs_define
class FastingTemplateFastingPeriodsItem:
    """
    Attributes:
        start (FastingPeriodBoundary | Unset):
        end (FastingPeriodBoundary | Unset):
    """

    start: FastingPeriodBoundary | Unset = UNSET
    end: FastingPeriodBoundary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fasting_period_boundary import FastingPeriodBoundary

        d = dict(src_dict)
        _start = d.pop("start", UNSET)
        start: FastingPeriodBoundary | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FastingPeriodBoundary.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: FastingPeriodBoundary | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = FastingPeriodBoundary.from_dict(_end)

        fasting_template_fasting_periods_item = cls(
            start=start,
            end=end,
        )

        fasting_template_fasting_periods_item.additional_properties = d
        return fasting_template_fasting_periods_item

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
