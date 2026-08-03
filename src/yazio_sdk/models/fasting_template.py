from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fasting_template_fasting_periods_item import FastingTemplateFastingPeriodsItem
    from ..models.fasting_template_preset_type_0 import FastingTemplatePresetType0
    from ..models.fasting_tip import FastingTip


T = TypeVar("T", bound="FastingTemplate")


@_attrs_define
class FastingTemplate:
    """
    Attributes:
        key (str | Unset):
        fasting_periods (list[FastingTemplateFastingPeriodsItem] | Unset):
        fasting_days (list[Any] | Unset):
        preset (FastingTemplatePresetType0 | None | Unset):
        fasting_tips (list[FastingTip] | Unset):
    """

    key: str | Unset = UNSET
    fasting_periods: list[FastingTemplateFastingPeriodsItem] | Unset = UNSET
    fasting_days: list[Any] | Unset = UNSET
    preset: FastingTemplatePresetType0 | None | Unset = UNSET
    fasting_tips: list[FastingTip] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fasting_template_preset_type_0 import FastingTemplatePresetType0

        key = self.key

        fasting_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fasting_periods, Unset):
            fasting_periods = []
            for fasting_periods_item_data in self.fasting_periods:
                fasting_periods_item = fasting_periods_item_data.to_dict()
                fasting_periods.append(fasting_periods_item)

        fasting_days: list[Any] | Unset = UNSET
        if not isinstance(self.fasting_days, Unset):
            fasting_days = self.fasting_days

        preset: dict[str, Any] | None | Unset
        if isinstance(self.preset, Unset):
            preset = UNSET
        elif isinstance(self.preset, FastingTemplatePresetType0):
            preset = self.preset.to_dict()
        else:
            preset = self.preset

        fasting_tips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fasting_tips, Unset):
            fasting_tips = []
            for fasting_tips_item_data in self.fasting_tips:
                fasting_tips_item = fasting_tips_item_data.to_dict()
                fasting_tips.append(fasting_tips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if fasting_periods is not UNSET:
            field_dict["fasting_periods"] = fasting_periods
        if fasting_days is not UNSET:
            field_dict["fasting_days"] = fasting_days
        if preset is not UNSET:
            field_dict["preset"] = preset
        if fasting_tips is not UNSET:
            field_dict["fasting_tips"] = fasting_tips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fasting_template_fasting_periods_item import FastingTemplateFastingPeriodsItem
        from ..models.fasting_template_preset_type_0 import FastingTemplatePresetType0
        from ..models.fasting_tip import FastingTip

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _fasting_periods = d.pop("fasting_periods", UNSET)
        fasting_periods: list[FastingTemplateFastingPeriodsItem] | Unset = UNSET
        if _fasting_periods is not UNSET:
            fasting_periods = []
            for fasting_periods_item_data in _fasting_periods:
                fasting_periods_item = FastingTemplateFastingPeriodsItem.from_dict(
                    fasting_periods_item_data
                )

                fasting_periods.append(fasting_periods_item)

        fasting_days = cast(list[Any], d.pop("fasting_days", UNSET))

        def _parse_preset(data: object) -> FastingTemplatePresetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preset_type_0 = FastingTemplatePresetType0.from_dict(data)

                return preset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FastingTemplatePresetType0 | None | Unset, data)

        preset = _parse_preset(d.pop("preset", UNSET))

        _fasting_tips = d.pop("fasting_tips", UNSET)
        fasting_tips: list[FastingTip] | Unset = UNSET
        if _fasting_tips is not UNSET:
            fasting_tips = []
            for fasting_tips_item_data in _fasting_tips:
                fasting_tips_item = FastingTip.from_dict(fasting_tips_item_data)

                fasting_tips.append(fasting_tips_item)

        fasting_template = cls(
            key=key,
            fasting_periods=fasting_periods,
            fasting_days=fasting_days,
            preset=preset,
            fasting_tips=fasting_tips,
        )

        fasting_template.additional_properties = d
        return fasting_template

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
