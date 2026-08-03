from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feeling_note_type_0 import FeelingNoteType0


T = TypeVar("T", bound="Feeling")


@_attrs_define
class Feeling:
    """
    Attributes:
        note (FeelingNoteType0 | None | Unset):
        tags (list[Any] | Unset):
    """

    note: FeelingNoteType0 | None | Unset = UNSET
    tags: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feeling_note_type_0 import FeelingNoteType0

        note: dict[str, Any] | None | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        elif isinstance(self.note, FeelingNoteType0):
            note = self.note.to_dict()
        else:
            note = self.note

        tags: list[Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feeling_note_type_0 import FeelingNoteType0

        d = dict(src_dict)

        def _parse_note(data: object) -> FeelingNoteType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                note_type_0 = FeelingNoteType0.from_dict(data)

                return note_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeelingNoteType0 | None | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        tags = cast(list[Any], d.pop("tags", UNSET))

        feeling = cls(
            note=note,
            tags=tags,
        )

        feeling.additional_properties = d
        return feeling

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
