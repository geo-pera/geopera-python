from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitmentsListInput")


@_attrs_define
class CommitmentsListInput:
    """
    Attributes:
        commitment_id (None | str | Unset):
        include_line_items (bool | Unset):  Default: False.
    """

    commitment_id: None | str | Unset = UNSET
    include_line_items: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commitment_id: None | str | Unset
        if isinstance(self.commitment_id, Unset):
            commitment_id = UNSET
        else:
            commitment_id = self.commitment_id

        include_line_items = self.include_line_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commitment_id is not UNSET:
            field_dict["commitment_id"] = commitment_id
        if include_line_items is not UNSET:
            field_dict["include_line_items"] = include_line_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_commitment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commitment_id = _parse_commitment_id(d.pop("commitment_id", UNSET))

        include_line_items = d.pop("include_line_items", UNSET)

        commitments_list_input = cls(
            commitment_id=commitment_id,
            include_line_items=include_line_items,
        )

        commitments_list_input.additional_properties = d
        return commitments_list_input

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
