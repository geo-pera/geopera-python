from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareLinkCreateOutput")


@_attrs_define
class ShareLinkCreateOutput:
    """
    Attributes:
        id (str):
        token (str):
        target_type (str):
        target_id (str):
        permission (str):
        organization_id (str):
        project_id (str):
        expires_at (datetime.datetime):
        created_at (datetime.datetime):
        revoked_at (datetime.datetime | None | Unset):
        access_count (int | Unset):  Default: 0.
        last_accessed_at (datetime.datetime | None | Unset):
        created_by (None | str | Unset):
    """

    id: str
    token: str
    target_type: str
    target_id: str
    permission: str
    organization_id: str
    project_id: str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    revoked_at: datetime.datetime | None | Unset = UNSET
    access_count: int | Unset = 0
    last_accessed_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        target_type = self.target_type

        target_id = self.target_id

        permission = self.permission

        organization_id = self.organization_id

        project_id = self.project_id

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        access_count = self.access_count

        last_accessed_at: None | str | Unset
        if isinstance(self.last_accessed_at, Unset):
            last_accessed_at = UNSET
        elif isinstance(self.last_accessed_at, datetime.datetime):
            last_accessed_at = self.last_accessed_at.isoformat()
        else:
            last_accessed_at = self.last_accessed_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "token": token,
                "target_type": target_type,
                "target_id": target_id,
                "permission": permission,
                "organization_id": organization_id,
                "project_id": project_id,
                "expires_at": expires_at,
                "created_at": created_at,
            }
        )
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if access_count is not UNSET:
            field_dict["access_count"] = access_count
        if last_accessed_at is not UNSET:
            field_dict["last_accessed_at"] = last_accessed_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        token = d.pop("token")

        target_type = d.pop("target_type")

        target_id = d.pop("target_id")

        permission = d.pop("permission")

        organization_id = d.pop("organization_id")

        project_id = d.pop("project_id")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        access_count = d.pop("access_count", UNSET)

        def _parse_last_accessed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_accessed_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_accessed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_accessed_at = _parse_last_accessed_at(d.pop("last_accessed_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        share_link_create_output = cls(
            id=id,
            token=token,
            target_type=target_type,
            target_id=target_id,
            permission=permission,
            organization_id=organization_id,
            project_id=project_id,
            expires_at=expires_at,
            created_at=created_at,
            revoked_at=revoked_at,
            access_count=access_count,
            last_accessed_at=last_accessed_at,
            created_by=created_by,
        )

        share_link_create_output.additional_properties = d
        return share_link_create_output

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
