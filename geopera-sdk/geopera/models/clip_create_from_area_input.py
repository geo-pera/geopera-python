from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_create_from_area_input_aoi_geometry import ClipCreateFromAreaInputAoiGeometry


T = TypeVar("T", bound="ClipCreateFromAreaInput")


@_attrs_define
class ClipCreateFromAreaInput:
    """
    Attributes:
        area (str):
        mosaic_types (list[str]):
        aoi_geometry (ClipCreateFromAreaInputAoiGeometry):
        organization_id (str):
        aoi_name (None | str | Unset):
        project_id (None | str | Unset):
    """

    area: str
    mosaic_types: list[str]
    aoi_geometry: ClipCreateFromAreaInputAoiGeometry
    organization_id: str
    aoi_name: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area = self.area

        mosaic_types = self.mosaic_types

        aoi_geometry = self.aoi_geometry.to_dict()

        organization_id = self.organization_id

        aoi_name: None | str | Unset
        if isinstance(self.aoi_name, Unset):
            aoi_name = UNSET
        else:
            aoi_name = self.aoi_name

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "area": area,
                "mosaic_types": mosaic_types,
                "aoi_geometry": aoi_geometry,
                "organization_id": organization_id,
            }
        )
        if aoi_name is not UNSET:
            field_dict["aoi_name"] = aoi_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clip_create_from_area_input_aoi_geometry import ClipCreateFromAreaInputAoiGeometry

        d = dict(src_dict)
        area = d.pop("area")

        mosaic_types = cast(list[str], d.pop("mosaic_types"))

        aoi_geometry = ClipCreateFromAreaInputAoiGeometry.from_dict(d.pop("aoi_geometry"))

        organization_id = d.pop("organization_id")

        def _parse_aoi_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aoi_name = _parse_aoi_name(d.pop("aoi_name", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        clip_create_from_area_input = cls(
            area=area,
            mosaic_types=mosaic_types,
            aoi_geometry=aoi_geometry,
            organization_id=organization_id,
            aoi_name=aoi_name,
            project_id=project_id,
        )

        clip_create_from_area_input.additional_properties = d
        return clip_create_from_area_input

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
