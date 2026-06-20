from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EulaDocumentsListInput")


@_attrs_define
class EulaDocumentsListInput:
    """
    Attributes:
        eula_id (str):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        sort (str | Unset):  Default: 'validFrom,desc'.
    """

    eula_id: str
    page: int | Unset = 0
    size: int | Unset = 20
    sort: str | Unset = "validFrom,desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eula_id = self.eula_id

        page = self.page

        size = self.size

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eula_id": eula_id,
            }
        )
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eula_id = d.pop("eula_id")

        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        sort = d.pop("sort", UNSET)

        eula_documents_list_input = cls(
            eula_id=eula_id,
            page=page,
            size=size,
            sort=sort,
        )

        eula_documents_list_input.additional_properties = d
        return eula_documents_list_input

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
