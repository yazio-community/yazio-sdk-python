from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_base_plan_id_type_0 import SubscriptionBasePlanIdType0


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        start (str | Unset):
        end (str | Unset):
        gateway (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        payment_provider_transaction_id (str | Unset):
        last_status_change_at (str | Unset):
        base_plan_id (None | SubscriptionBasePlanIdType0 | Unset):
    """

    start: str | Unset = UNSET
    end: str | Unset = UNSET
    gateway: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    payment_provider_transaction_id: str | Unset = UNSET
    last_status_change_at: str | Unset = UNSET
    base_plan_id: None | SubscriptionBasePlanIdType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_base_plan_id_type_0 import SubscriptionBasePlanIdType0

        start = self.start

        end = self.end

        gateway = self.gateway

        type_ = self.type_

        status = self.status

        payment_provider_transaction_id = self.payment_provider_transaction_id

        last_status_change_at = self.last_status_change_at

        base_plan_id: dict[str, Any] | None | Unset
        if isinstance(self.base_plan_id, Unset):
            base_plan_id = UNSET
        elif isinstance(self.base_plan_id, SubscriptionBasePlanIdType0):
            base_plan_id = self.base_plan_id.to_dict()
        else:
            base_plan_id = self.base_plan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if payment_provider_transaction_id is not UNSET:
            field_dict["payment_provider_transaction_id"] = payment_provider_transaction_id
        if last_status_change_at is not UNSET:
            field_dict["last_status_change_at"] = last_status_change_at
        if base_plan_id is not UNSET:
            field_dict["base_plan_id"] = base_plan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_base_plan_id_type_0 import SubscriptionBasePlanIdType0

        d = dict(src_dict)
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        gateway = d.pop("gateway", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        payment_provider_transaction_id = d.pop("payment_provider_transaction_id", UNSET)

        last_status_change_at = d.pop("last_status_change_at", UNSET)

        def _parse_base_plan_id(data: object) -> None | SubscriptionBasePlanIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_plan_id_type_0 = SubscriptionBasePlanIdType0.from_dict(data)

                return base_plan_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubscriptionBasePlanIdType0 | Unset, data)

        base_plan_id = _parse_base_plan_id(d.pop("base_plan_id", UNSET))

        subscription = cls(
            start=start,
            end=end,
            gateway=gateway,
            type_=type_,
            status=status,
            payment_provider_transaction_id=payment_provider_transaction_id,
            last_status_change_at=last_status_change_at,
            base_plan_id=base_plan_id,
        )

        subscription.additional_properties = d
        return subscription

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
