from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gcs_region import GcsRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCreate")


@_attrs_define
class ProjectCreate:
    """Input for creating a project.

    Attributes:
        name (str):
        description (None | str | Unset):
        gcs_region (GcsRegion | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    gcs_region: GcsRegion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        gcs_region: str | Unset = UNSET
        if not isinstance(self.gcs_region, Unset):
            gcs_region = self.gcs_region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if gcs_region is not UNSET:
            field_dict["gcs_region"] = gcs_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _gcs_region = d.pop("gcs_region", UNSET)
        gcs_region: GcsRegion | Unset
        if isinstance(_gcs_region, Unset):
            gcs_region = UNSET
        else:
            gcs_region = GcsRegion(_gcs_region)

        project_create = cls(
            name=name,
            description=description,
            gcs_region=gcs_region,
        )

        project_create.additional_properties = d
        return project_create

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
