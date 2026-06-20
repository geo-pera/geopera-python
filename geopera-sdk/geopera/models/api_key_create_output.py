from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyCreateOutput")


@_attrs_define
class ApiKeyCreateOutput:
    """
    Attributes:
        id (str):
        prefix (str):
        name (str):
        permissions (list[str]):
        created_at (str):
        key (None | str | Unset):
        expires_at (None | str | Unset):
    """

    id: str
    prefix: str
    name: str
    permissions: list[str]
    created_at: str
    key: None | str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        prefix = self.prefix

        name = self.name

        permissions = self.permissions

        created_at = self.created_at

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "prefix": prefix,
                "name": name,
                "permissions": permissions,
                "created_at": created_at,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        prefix = d.pop("prefix")

        name = d.pop("name")

        permissions = cast(list[str], d.pop("permissions"))

        created_at = d.pop("created_at")

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        api_key_create_output = cls(
            id=id,
            prefix=prefix,
            name=name,
            permissions=permissions,
            created_at=created_at,
            key=key,
            expires_at=expires_at,
        )

        api_key_create_output.additional_properties = d
        return api_key_create_output

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
