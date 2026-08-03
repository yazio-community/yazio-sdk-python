from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wallet_currencies_item import WalletCurrenciesItem


T = TypeVar("T", bound="Wallet")


@_attrs_define
class Wallet:
    """
    Attributes:
        currencies (list[WalletCurrenciesItem] | Unset):
    """

    currencies: list[WalletCurrenciesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currencies is not UNSET:
            field_dict["currencies"] = currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wallet_currencies_item import WalletCurrenciesItem

        d = dict(src_dict)
        _currencies = d.pop("currencies", UNSET)
        currencies: list[WalletCurrenciesItem] | Unset = UNSET
        if _currencies is not UNSET:
            currencies = []
            for currencies_item_data in _currencies:
                currencies_item = WalletCurrenciesItem.from_dict(currencies_item_data)

                currencies.append(currencies_item)

        wallet = cls(
            currencies=currencies,
        )

        wallet.additional_properties = d
        return wallet

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
