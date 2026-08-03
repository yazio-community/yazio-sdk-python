from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_tips_request_experiments_item import DailyTipsRequestExperimentsItem


T = TypeVar("T", bound="DailyTipsRequest")


@_attrs_define
class DailyTipsRequest:
    """
    Attributes:
        request_uuid (str | Unset):
        device_uuid (str | Unset):
        app_version (str | Unset):
        platform (str | Unset):
        session_id (str | Unset):
        delivery_mode (str | Unset):
        experiments (list[DailyTipsRequestExperimentsItem] | Unset):
        requested_at (float | Unset):
        language (str | Unset):
    """

    request_uuid: str | Unset = UNSET
    device_uuid: str | Unset = UNSET
    app_version: str | Unset = UNSET
    platform: str | Unset = UNSET
    session_id: str | Unset = UNSET
    delivery_mode: str | Unset = UNSET
    experiments: list[DailyTipsRequestExperimentsItem] | Unset = UNSET
    requested_at: float | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_uuid = self.request_uuid

        device_uuid = self.device_uuid

        app_version = self.app_version

        platform = self.platform

        session_id = self.session_id

        delivery_mode = self.delivery_mode

        experiments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.experiments, Unset):
            experiments = []
            for experiments_item_data in self.experiments:
                experiments_item = experiments_item_data.to_dict()
                experiments.append(experiments_item)

        requested_at = self.requested_at

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_uuid is not UNSET:
            field_dict["request_uuid"] = request_uuid
        if device_uuid is not UNSET:
            field_dict["device_uuid"] = device_uuid
        if app_version is not UNSET:
            field_dict["app_version"] = app_version
        if platform is not UNSET:
            field_dict["platform"] = platform
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if delivery_mode is not UNSET:
            field_dict["delivery_mode"] = delivery_mode
        if experiments is not UNSET:
            field_dict["experiments"] = experiments
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_tips_request_experiments_item import DailyTipsRequestExperimentsItem

        d = dict(src_dict)
        request_uuid = d.pop("request_uuid", UNSET)

        device_uuid = d.pop("device_uuid", UNSET)

        app_version = d.pop("app_version", UNSET)

        platform = d.pop("platform", UNSET)

        session_id = d.pop("session_id", UNSET)

        delivery_mode = d.pop("delivery_mode", UNSET)

        _experiments = d.pop("experiments", UNSET)
        experiments: list[DailyTipsRequestExperimentsItem] | Unset = UNSET
        if _experiments is not UNSET:
            experiments = []
            for experiments_item_data in _experiments:
                experiments_item = DailyTipsRequestExperimentsItem.from_dict(experiments_item_data)

                experiments.append(experiments_item)

        requested_at = d.pop("requested_at", UNSET)

        language = d.pop("language", UNSET)

        daily_tips_request = cls(
            request_uuid=request_uuid,
            device_uuid=device_uuid,
            app_version=app_version,
            platform=platform,
            session_id=session_id,
            delivery_mode=delivery_mode,
            experiments=experiments,
            requested_at=requested_at,
            language=language,
        )

        daily_tips_request.additional_properties = d
        return daily_tips_request

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
