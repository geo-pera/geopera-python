from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsListInput")


@_attrs_define
class NotificationsListInput:
    """
    Attributes:
        unread_only (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
    """

    unread_only: bool | Unset = False
    limit: int | Unset = 50
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unread_only = self.unread_only

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unread_only is not UNSET:
            field_dict["unread_only"] = unread_only
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unread_only = d.pop("unread_only", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        notifications_list_input = cls(
            unread_only=unread_only,
            limit=limit,
            offset=offset,
        )

        notifications_list_input.additional_properties = d
        return notifications_list_input

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
