from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EulasListInput")


@_attrs_define
class EulasListInput:
    """
    Attributes:
        term (None | str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        sort (str | Unset):  Default: 'createdAt,desc'.
    """

    term: None | str | Unset = UNSET
    page: int | Unset = 0
    size: int | Unset = 20
    sort: str | Unset = "createdAt,desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term: None | str | Unset
        if isinstance(self.term, Unset):
            term = UNSET
        else:
            term = self.term

        page = self.page

        size = self.size

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
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

        def _parse_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        term = _parse_term(d.pop("term", UNSET))

        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        sort = d.pop("sort", UNSET)

        eulas_list_input = cls(
            term=term,
            page=page,
            size=size,
            sort=sort,
        )

        eulas_list_input.additional_properties = d
        return eulas_list_input

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
