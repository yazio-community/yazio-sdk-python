from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.water_intake_gateway_type_0 import WaterIntakeGatewayType0
    from ..models.water_intake_source_type_0 import WaterIntakeSourceType0


T = TypeVar("T", bound="WaterIntake")


@_attrs_define
class WaterIntake:
    """
    Attributes:
        water_intake (float | Unset):
        gateway (None | Unset | WaterIntakeGatewayType0):
        source (None | Unset | WaterIntakeSourceType0):
    """

    water_intake: float | Unset = UNSET
    gateway: None | Unset | WaterIntakeGatewayType0 = UNSET
    source: None | Unset | WaterIntakeSourceType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.water_intake_gateway_type_0 import WaterIntakeGatewayType0
        from ..models.water_intake_source_type_0 import WaterIntakeSourceType0

        water_intake = self.water_intake

        gateway: dict[str, Any] | None | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        elif isinstance(self.gateway, WaterIntakeGatewayType0):
            gateway = self.gateway.to_dict()
        else:
            gateway = self.gateway

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, WaterIntakeSourceType0):
            source = self.source.to_dict()
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if water_intake is not UNSET:
            field_dict["water_intake"] = water_intake
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.water_intake_gateway_type_0 import WaterIntakeGatewayType0
        from ..models.water_intake_source_type_0 import WaterIntakeSourceType0

        d = dict(src_dict)
        water_intake = d.pop("water_intake", UNSET)

        def _parse_gateway(data: object) -> None | Unset | WaterIntakeGatewayType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gateway_type_0 = WaterIntakeGatewayType0.from_dict(data)

                return gateway_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WaterIntakeGatewayType0, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        def _parse_source(data: object) -> None | Unset | WaterIntakeSourceType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = WaterIntakeSourceType0.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WaterIntakeSourceType0, data)

        source = _parse_source(d.pop("source", UNSET))

        water_intake = cls(
            water_intake=water_intake,
            gateway=gateway,
            source=source,
        )

        water_intake.additional_properties = d
        return water_intake

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
