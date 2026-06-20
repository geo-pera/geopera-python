from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineageGetInput")


@_attrs_define
class LineageGetInput:
    """
    Attributes:
        entity_type (str): Root node type: item | order | processing_job | collection | project
        entity_id (str): Root entity id
        direction (str | Unset): up=ancestors, down=descendants, both Default: 'up'.
        max_depth (int | Unset):  Default: 20.
    """

    entity_type: str
    entity_id: str
    direction: str | Unset = "up"
    max_depth: int | Unset = 20
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        entity_id = self.entity_id

        direction = self.direction

        max_depth = self.max_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_type": entity_type,
                "entity_id": entity_id,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = d.pop("entity_type")

        entity_id = d.pop("entity_id")

        direction = d.pop("direction", UNSET)

        max_depth = d.pop("max_depth", UNSET)

        lineage_get_input = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            direction=direction,
            max_depth=max_depth,
        )

        lineage_get_input.additional_properties = d
        return lineage_get_input

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
