from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EulaAcceptInput")


@_attrs_define
class EulaAcceptInput:
    """
    Attributes:
        eula_id (str):
        document_id (str):
        is_accepted (bool | Unset):  Default: True.
    """

    eula_id: str
    document_id: str
    is_accepted: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eula_id = self.eula_id

        document_id = self.document_id

        is_accepted = self.is_accepted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eula_id": eula_id,
                "document_id": document_id,
            }
        )
        if is_accepted is not UNSET:
            field_dict["is_accepted"] = is_accepted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eula_id = d.pop("eula_id")

        document_id = d.pop("document_id")

        is_accepted = d.pop("is_accepted", UNSET)

        eula_accept_input = cls(
            eula_id=eula_id,
            document_id=document_id,
            is_accepted=is_accepted,
        )

        eula_accept_input.additional_properties = d
        return eula_accept_input

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
