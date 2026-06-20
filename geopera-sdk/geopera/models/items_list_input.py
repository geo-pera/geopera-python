from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemsListInput")


@_attrs_define
class ItemsListInput:
    """
    Attributes:
        project_id (str):
        collection_id (None | str | Unset):
        uncollected (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
    """

    project_id: str
    collection_id: None | str | Unset = UNSET
    uncollected: bool | Unset = False
    limit: int | Unset = 100
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        uncollected = self.uncollected

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if uncollected is not UNSET:
            field_dict["uncollected"] = uncollected
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        uncollected = d.pop("uncollected", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        items_list_input = cls(
            project_id=project_id,
            collection_id=collection_id,
            uncollected=uncollected,
            limit=limit,
            offset=offset,
        )

        items_list_input.additional_properties = d
        return items_list_input

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
