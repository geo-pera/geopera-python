from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestApprovalInput")


@_attrs_define
class RequestApprovalInput:
    """
    Attributes:
        credits_ (int):
        expiry_hours (int | None | Unset):
    """

    credits_: int
    expiry_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        expiry_hours: int | None | Unset
        if isinstance(self.expiry_hours, Unset):
            expiry_hours = UNSET
        else:
            expiry_hours = self.expiry_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
            }
        )
        if expiry_hours is not UNSET:
            field_dict["expiry_hours"] = expiry_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        def _parse_expiry_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expiry_hours = _parse_expiry_hours(d.pop("expiry_hours", UNSET))

        request_approval_input = cls(
            credits_=credits_,
            expiry_hours=expiry_hours,
        )

        request_approval_input.additional_properties = d
        return request_approval_input

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
