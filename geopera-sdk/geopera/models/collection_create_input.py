from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionCreateInput")


@_attrs_define
class CollectionCreateInput:
    """CollectionCreate + the project it lives in.

    Attributes:
        name (str):
        project_id (str):
        description (None | str | Unset):
        color (None | str | Unset):
        show_on_map (bool | Unset):  Default: True.
        layer_order (int | Unset):  Default: 0.
    """

    name: str
    project_id: str
    description: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    show_on_map: bool | Unset = True
    layer_order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

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

        show_on_map = self.show_on_map

        layer_order = self.layer_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_id": project_id,
            }
        )
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
        name = d.pop("name")

        project_id = d.pop("project_id")

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

        show_on_map = d.pop("show_on_map", UNSET)

        layer_order = d.pop("layer_order", UNSET)

        collection_create_input = cls(
            name=name,
            project_id=project_id,
            description=description,
            color=color,
            show_on_map=show_on_map,
            layer_order=layer_order,
        )

        collection_create_input.additional_properties = d
        return collection_create_input

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
