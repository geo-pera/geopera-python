from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadFailInput")


@_attrs_define
class UploadFailInput:
    """
    Attributes:
        upload_id (str):
        error_message (str):
        error_step (None | str | Unset):
    """

    upload_id: str
    error_message: str
    error_step: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        error_message = self.error_message

        error_step: None | str | Unset
        if isinstance(self.error_step, Unset):
            error_step = UNSET
        else:
            error_step = self.error_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "error_message": error_message,
            }
        )
        if error_step is not UNSET:
            field_dict["error_step"] = error_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        error_message = d.pop("error_message")

        def _parse_error_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_step = _parse_error_step(d.pop("error_step", UNSET))

        upload_fail_input = cls(
            upload_id=upload_id,
            error_message=error_message,
            error_step=error_step,
        )

        upload_fail_input.additional_properties = d
        return upload_fail_input

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
