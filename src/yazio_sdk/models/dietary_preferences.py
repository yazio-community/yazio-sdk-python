from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dietary_preferences_restriction_type_0 import DietaryPreferencesRestrictionType0


T = TypeVar("T", bound="DietaryPreferences")


@_attrs_define
class DietaryPreferences:
    """
    Attributes:
        restriction (DietaryPreferencesRestrictionType0 | None | Unset):
    """

    restriction: DietaryPreferencesRestrictionType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dietary_preferences_restriction_type_0 import (
            DietaryPreferencesRestrictionType0,
        )

        restriction: dict[str, Any] | None | Unset
        if isinstance(self.restriction, Unset):
            restriction = UNSET
        elif isinstance(self.restriction, DietaryPreferencesRestrictionType0):
            restriction = self.restriction.to_dict()
        else:
            restriction = self.restriction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restriction is not UNSET:
            field_dict["restriction"] = restriction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dietary_preferences_restriction_type_0 import (
            DietaryPreferencesRestrictionType0,
        )

        d = dict(src_dict)

        def _parse_restriction(data: object) -> DietaryPreferencesRestrictionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restriction_type_0 = DietaryPreferencesRestrictionType0.from_dict(data)

                return restriction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DietaryPreferencesRestrictionType0 | None | Unset, data)

        restriction = _parse_restriction(d.pop("restriction", UNSET))

        dietary_preferences = cls(
            restriction=restriction,
        )

        dietary_preferences.additional_properties = d
        return dietary_preferences

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
