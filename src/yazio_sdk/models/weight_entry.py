from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weight_entry_external_id_type_0 import WeightEntryExternalIdType0
    from ..models.weight_entry_source_type_0 import WeightEntrySourceType0


T = TypeVar("T", bound="WeightEntry")


@_attrs_define
class WeightEntry:
    """
    Attributes:
        date (str | Unset):
        id (str | Unset):
        value (float | Unset):
        external_id (None | Unset | WeightEntryExternalIdType0):
        gateway (str | Unset):
        source (None | Unset | WeightEntrySourceType0):
    """

    date: str | Unset = UNSET
    id: str | Unset = UNSET
    value: float | Unset = UNSET
    external_id: None | Unset | WeightEntryExternalIdType0 = UNSET
    gateway: str | Unset = UNSET
    source: None | Unset | WeightEntrySourceType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.weight_entry_external_id_type_0 import WeightEntryExternalIdType0
        from ..models.weight_entry_source_type_0 import WeightEntrySourceType0

        date = self.date

        id = self.id

        value = self.value

        external_id: dict[str, Any] | None | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        elif isinstance(self.external_id, WeightEntryExternalIdType0):
            external_id = self.external_id.to_dict()
        else:
            external_id = self.external_id

        gateway = self.gateway

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, WeightEntrySourceType0):
            source = self.source.to_dict()
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.weight_entry_external_id_type_0 import WeightEntryExternalIdType0
        from ..models.weight_entry_source_type_0 import WeightEntrySourceType0

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        def _parse_external_id(data: object) -> None | Unset | WeightEntryExternalIdType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_id_type_0 = WeightEntryExternalIdType0.from_dict(data)

                return external_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WeightEntryExternalIdType0, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        gateway = d.pop("gateway", UNSET)

        def _parse_source(data: object) -> None | Unset | WeightEntrySourceType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = WeightEntrySourceType0.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WeightEntrySourceType0, data)

        source = _parse_source(d.pop("source", UNSET))

        weight_entry = cls(
            date=date,
            id=id,
            value=value,
            external_id=external_id,
            gateway=gateway,
            source=source,
        )

        weight_entry.additional_properties = d
        return weight_entry

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
