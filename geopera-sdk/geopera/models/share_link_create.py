from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.share_permission import SharePermission
from ..models.share_target_type import ShareTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareLinkCreate")


@_attrs_define
class ShareLinkCreate:
    """Input for creating a share link.

    Attributes:
        target_type (ShareTargetType):
        target_id (str):
        password (str): Plaintext password (will be bcrypt-hashed)
        expires_at (datetime.datetime):
        permission (SharePermission | Unset):
    """

    target_type: ShareTargetType
    target_id: str
    password: str
    expires_at: datetime.datetime
    permission: SharePermission | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_id = self.target_id

        password = self.password

        expires_at = self.expires_at.isoformat()

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_type": target_type,
                "target_id": target_id,
                "password": password,
                "expires_at": expires_at,
            }
        )
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = ShareTargetType(d.pop("target_type"))

        target_id = d.pop("target_id")

        password = d.pop("password")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        _permission = d.pop("permission", UNSET)
        permission: SharePermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = SharePermission(_permission)

        share_link_create = cls(
            target_type=target_type,
            target_id=target_id,
            password=password,
            expires_at=expires_at,
            permission=permission,
        )

        share_link_create.additional_properties = d
        return share_link_create

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
