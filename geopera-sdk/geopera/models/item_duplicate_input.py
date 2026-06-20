from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemDuplicateInput")


@_attrs_define
class ItemDuplicateInput:
    """
    Attributes:
        item_id (str):
        new_name (None | str | Unset): Name for the copy
        target_collection_id (None | str | Unset):
        target_project_id (None | str | Unset):
    """

    item_id: str
    new_name: None | str | Unset = UNSET
    target_collection_id: None | str | Unset = UNSET
    target_project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        new_name: None | str | Unset
        if isinstance(self.new_name, Unset):
            new_name = UNSET
        else:
            new_name = self.new_name

        target_collection_id: None | str | Unset
        if isinstance(self.target_collection_id, Unset):
            target_collection_id = UNSET
        else:
            target_collection_id = self.target_collection_id

        target_project_id: None | str | Unset
        if isinstance(self.target_project_id, Unset):
            target_project_id = UNSET
        else:
            target_project_id = self.target_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
            }
        )
        if new_name is not UNSET:
            field_dict["new_name"] = new_name
        if target_collection_id is not UNSET:
            field_dict["target_collection_id"] = target_collection_id
        if target_project_id is not UNSET:
            field_dict["target_project_id"] = target_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        def _parse_new_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_name = _parse_new_name(d.pop("new_name", UNSET))

        def _parse_target_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_collection_id = _parse_target_collection_id(d.pop("target_collection_id", UNSET))

        def _parse_target_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_project_id = _parse_target_project_id(d.pop("target_project_id", UNSET))

        item_duplicate_input = cls(
            item_id=item_id,
            new_name=new_name,
            target_collection_id=target_collection_id,
            target_project_id=target_project_id,
        )

        item_duplicate_input.additional_properties = d
        return item_duplicate_input

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
