from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectJobsInput")


@_attrs_define
class ProjectJobsInput:
    """
    Attributes:
        project_id (str):
        status (None | str | Unset):
        job_type_name (None | str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
    """

    project_id: str
    status: None | str | Unset = UNSET
    job_type_name: None | str | Unset = UNSET
    limit: int | Unset = 50
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        job_type_name: None | str | Unset
        if isinstance(self.job_type_name, Unset):
            job_type_name = UNSET
        else:
            job_type_name = self.job_type_name

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if job_type_name is not UNSET:
            field_dict["job_type_name"] = job_type_name
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_job_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_type_name = _parse_job_type_name(d.pop("job_type_name", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        project_jobs_input = cls(
            project_id=project_id,
            status=status,
            job_type_name=job_type_name,
            limit=limit,
            offset=offset,
        )

        project_jobs_input.additional_properties = d
        return project_jobs_input

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
