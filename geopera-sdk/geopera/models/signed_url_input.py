from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignedUrlInput")


@_attrs_define
class SignedUrlInput:
    """
    Attributes:
        upload_id (str):
        file_name (str):
        content_type (str | Unset):  Default: 'application/octet-stream'.
    """

    upload_id: str
    file_name: str
    content_type: str | Unset = "application/octet-stream"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        file_name = self.file_name

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "file_name": file_name,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        file_name = d.pop("file_name")

        content_type = d.pop("content_type", UNSET)

        signed_url_input = cls(
            upload_id=upload_id,
            file_name=file_name,
            content_type=content_type,
        )

        signed_url_input.additional_properties = d
        return signed_url_input

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
