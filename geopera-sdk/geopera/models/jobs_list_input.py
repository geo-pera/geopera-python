from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsListInput")


@_attrs_define
class JobsListInput:
    """
    Attributes:
        workspace_id (None | str | Unset):
        process_id (None | str | Unset):
        status (None | str | Unset):
        ids (None | str | Unset):
        page (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sort (str | Unset):  Default: 'created,desc'.
    """

    workspace_id: None | str | Unset = UNSET
    process_id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    ids: None | str | Unset = UNSET
    page: int | Unset = 0
    limit: int | Unset = 20
    sort: str | Unset = "created,desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        process_id: None | str | Unset
        if isinstance(self.process_id, Unset):
            process_id = UNSET
        else:
            process_id = self.process_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        ids: None | str | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        else:
            ids = self.ids

        page = self.page

        limit = self.limit

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if process_id is not UNSET:
            field_dict["processId"] = process_id
        if status is not UNSET:
            field_dict["status"] = status
        if ids is not UNSET:
            field_dict["ids"] = ids
        if page is not UNSET:
            field_dict["page"] = page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if sort is not UNSET:
            field_dict["sort"] = sort

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

        def _parse_process_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        process_id = _parse_process_id(d.pop("processId", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_ids(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))

        page = d.pop("page", UNSET)

        limit = d.pop("limit", UNSET)

        sort = d.pop("sort", UNSET)

        jobs_list_input = cls(
            workspace_id=workspace_id,
            process_id=process_id,
            status=status,
            ids=ids,
            page=page,
            limit=limit,
            sort=sort,
        )

        jobs_list_input.additional_properties = d
        return jobs_list_input

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
