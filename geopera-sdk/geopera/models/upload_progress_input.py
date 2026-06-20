from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadProgressInput")


@_attrs_define
class UploadProgressInput:
    """
    Attributes:
        upload_id (str):
        status (None | str | Unset):
        bytes_uploaded (int | None | Unset):
    """

    upload_id: str
    status: None | str | Unset = UNSET
    bytes_uploaded: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        bytes_uploaded: int | None | Unset
        if isinstance(self.bytes_uploaded, Unset):
            bytes_uploaded = UNSET
        else:
            bytes_uploaded = self.bytes_uploaded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if bytes_uploaded is not UNSET:
            field_dict["bytes_uploaded"] = bytes_uploaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_bytes_uploaded(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_uploaded = _parse_bytes_uploaded(d.pop("bytes_uploaded", UNSET))

        upload_progress_input = cls(
            upload_id=upload_id,
            status=status,
            bytes_uploaded=bytes_uploaded,
        )

        upload_progress_input.additional_properties = d
        return upload_progress_input

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
