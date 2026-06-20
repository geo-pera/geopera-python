from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gcs_region import GcsRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectResponse")


@_attrs_define
class ProjectResponse:
    """Project as returned from the API.

    Attributes:
        id (str):
        organization_id (str):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        gcs_region (GcsRegion | None | Unset):
        gcs_bucket_name (None | str | Unset):
        is_archived (bool | Unset):  Default: False.
    """

    id: str
    organization_id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    gcs_region: GcsRegion | None | Unset = UNSET
    gcs_bucket_name: None | str | Unset = UNSET
    is_archived: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        gcs_region: None | str | Unset
        if isinstance(self.gcs_region, Unset):
            gcs_region = UNSET
        elif isinstance(self.gcs_region, GcsRegion):
            gcs_region = self.gcs_region.value
        else:
            gcs_region = self.gcs_region

        gcs_bucket_name: None | str | Unset
        if isinstance(self.gcs_bucket_name, Unset):
            gcs_bucket_name = UNSET
        else:
            gcs_bucket_name = self.gcs_bucket_name

        is_archived = self.is_archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_id": organization_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if gcs_region is not UNSET:
            field_dict["gcs_region"] = gcs_region
        if gcs_bucket_name is not UNSET:
            field_dict["gcs_bucket_name"] = gcs_bucket_name
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organization_id")

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_gcs_region(data: object) -> GcsRegion | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gcs_region_type_0 = GcsRegion(data)

                return gcs_region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GcsRegion | None | Unset, data)

        gcs_region = _parse_gcs_region(d.pop("gcs_region", UNSET))

        def _parse_gcs_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gcs_bucket_name = _parse_gcs_bucket_name(d.pop("gcs_bucket_name", UNSET))

        is_archived = d.pop("is_archived", UNSET)

        project_response = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            gcs_region=gcs_region,
            gcs_bucket_name=gcs_bucket_name,
            is_archived=is_archived,
        )

        project_response.additional_properties = d
        return project_response

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
