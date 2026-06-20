from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecisionsPendingInput")


@_attrs_define
class DecisionsPendingInput:
    """
    Attributes:
        workspace_id (None | str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 20.
        kinds (None | str | Unset):
    """

    workspace_id: None | str | Unset = UNSET
    page: int | Unset = 0
    size: int | Unset = 20
    kinds: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        page = self.page

        size = self.size

        kinds: None | str | Unset
        if isinstance(self.kinds, Unset):
            kinds = UNSET
        else:
            kinds = self.kinds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if kinds is not UNSET:
            field_dict["kinds"] = kinds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_id = _parse_workspace_id(d.pop("workspaceId", UNSET))

        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        def _parse_kinds(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kinds = _parse_kinds(d.pop("kinds", UNSET))

        decisions_pending_input = cls(
            workspace_id=workspace_id,
            page=page,
            size=size,
            kinds=kinds,
        )

        decisions_pending_input.additional_properties = d
        return decisions_pending_input

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
