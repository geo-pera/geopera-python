from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectDeleteOutput")


@_attrs_define
class ProjectDeleteOutput:
    """
    Attributes:
        project_id (str):
        deleted (bool | Unset):  Default: True.
        storage_freed_bytes (int | Unset):  Default: 0.
    """

    project_id: str
    deleted: bool | Unset = True
    storage_freed_bytes: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        deleted = self.deleted

        storage_freed_bytes = self.storage_freed_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if storage_freed_bytes is not UNSET:
            field_dict["storage_freed_bytes"] = storage_freed_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        deleted = d.pop("deleted", UNSET)

        storage_freed_bytes = d.pop("storage_freed_bytes", UNSET)

        project_delete_output = cls(
            project_id=project_id,
            deleted=deleted,
            storage_freed_bytes=storage_freed_bytes,
        )

        project_delete_output.additional_properties = d
        return project_delete_output

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
