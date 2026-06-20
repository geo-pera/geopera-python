from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionUpdateInput")


@_attrs_define
class CollectionUpdateInput:
    """
    Attributes:
        project_id (str):
        collection_id (str):
        name (None | str | Unset):
        description (None | str | Unset):
        color (None | str | Unset):
        show_on_map (bool | None | Unset):
        layer_order (int | None | Unset):
    """

    project_id: str
    collection_id: str
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    show_on_map: bool | None | Unset = UNSET
    layer_order: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        collection_id = self.collection_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        show_on_map: bool | None | Unset
        if isinstance(self.show_on_map, Unset):
            show_on_map = UNSET
        else:
            show_on_map = self.show_on_map

        layer_order: int | None | Unset
        if isinstance(self.layer_order, Unset):
            layer_order = UNSET
        else:
            layer_order = self.layer_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "collection_id": collection_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if show_on_map is not UNSET:
            field_dict["show_on_map"] = show_on_map
        if layer_order is not UNSET:
            field_dict["layer_order"] = layer_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        collection_id = d.pop("collection_id")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_show_on_map(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_on_map = _parse_show_on_map(d.pop("show_on_map", UNSET))

        def _parse_layer_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        layer_order = _parse_layer_order(d.pop("layer_order", UNSET))

        collection_update_input = cls(
            project_id=project_id,
            collection_id=collection_id,
            name=name,
            description=description,
            color=color,
            show_on_map=show_on_map,
            layer_order=layer_order,
        )

        collection_update_input.additional_properties = d
        return collection_update_input

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
