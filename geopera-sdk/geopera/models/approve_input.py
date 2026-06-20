from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApproveInput")


@_attrs_define
class ApproveInput:
    """
    Attributes:
        organization_id (str):
        admin_user_id (None | str | Unset):
    """

    organization_id: str
    admin_user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        admin_user_id: None | str | Unset
        if isinstance(self.admin_user_id, Unset):
            admin_user_id = UNSET
        else:
            admin_user_id = self.admin_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
            }
        )
        if admin_user_id is not UNSET:
            field_dict["admin_user_id"] = admin_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organization_id")

        def _parse_admin_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_user_id = _parse_admin_user_id(d.pop("admin_user_id", UNSET))

        approve_input = cls(
            organization_id=organization_id,
            admin_user_id=admin_user_id,
        )

        approve_input.additional_properties = d
        return approve_input

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
