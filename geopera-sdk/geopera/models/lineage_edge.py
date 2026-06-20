from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineageEdge")


@_attrs_define
class LineageEdge:
    """
    Attributes:
        depth (int):
        src_type (None | str | Unset):
        src_id (None | str | Unset):
        dst_type (None | str | Unset):
        dst_id (None | str | Unset):
        relation (None | str | Unset):
        invocation_id (None | str | Unset):
    """

    depth: int
    src_type: None | str | Unset = UNSET
    src_id: None | str | Unset = UNSET
    dst_type: None | str | Unset = UNSET
    dst_id: None | str | Unset = UNSET
    relation: None | str | Unset = UNSET
    invocation_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depth = self.depth

        src_type: None | str | Unset
        if isinstance(self.src_type, Unset):
            src_type = UNSET
        else:
            src_type = self.src_type

        src_id: None | str | Unset
        if isinstance(self.src_id, Unset):
            src_id = UNSET
        else:
            src_id = self.src_id

        dst_type: None | str | Unset
        if isinstance(self.dst_type, Unset):
            dst_type = UNSET
        else:
            dst_type = self.dst_type

        dst_id: None | str | Unset
        if isinstance(self.dst_id, Unset):
            dst_id = UNSET
        else:
            dst_id = self.dst_id

        relation: None | str | Unset
        if isinstance(self.relation, Unset):
            relation = UNSET
        else:
            relation = self.relation

        invocation_id: None | str | Unset
        if isinstance(self.invocation_id, Unset):
            invocation_id = UNSET
        else:
            invocation_id = self.invocation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "depth": depth,
            }
        )
        if src_type is not UNSET:
            field_dict["src_type"] = src_type
        if src_id is not UNSET:
            field_dict["src_id"] = src_id
        if dst_type is not UNSET:
            field_dict["dst_type"] = dst_type
        if dst_id is not UNSET:
            field_dict["dst_id"] = dst_id
        if relation is not UNSET:
            field_dict["relation"] = relation
        if invocation_id is not UNSET:
            field_dict["invocation_id"] = invocation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        depth = d.pop("depth")

        def _parse_src_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        src_type = _parse_src_type(d.pop("src_type", UNSET))

        def _parse_src_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        src_id = _parse_src_id(d.pop("src_id", UNSET))

        def _parse_dst_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dst_type = _parse_dst_type(d.pop("dst_type", UNSET))

        def _parse_dst_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dst_id = _parse_dst_id(d.pop("dst_id", UNSET))

        def _parse_relation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation = _parse_relation(d.pop("relation", UNSET))

        def _parse_invocation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invocation_id = _parse_invocation_id(d.pop("invocation_id", UNSET))

        lineage_edge = cls(
            depth=depth,
            src_type=src_type,
            src_id=src_id,
            dst_type=dst_type,
            dst_id=dst_id,
            relation=relation,
            invocation_id=invocation_id,
        )

        lineage_edge.additional_properties = d
        return lineage_edge

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
