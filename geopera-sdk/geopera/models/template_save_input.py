from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateSaveInput")


@_attrs_define
class TemplateSaveInput:
    """
    Attributes:
        name (str):
        resolution (str):
        sensor (str):
        capture_frequency (str):
        datum (str):
        file_format (str):
        description (None | str | Unset):
        capture_asap (bool | Unset):  Default: True.
        has_control (bool | Unset):  Default: False.
        max_cloud_coverage (int | Unset):  Default: 0.
        max_nadir_angle (int | Unset):  Default: 0.
    """

    name: str
    resolution: str
    sensor: str
    capture_frequency: str
    datum: str
    file_format: str
    description: None | str | Unset = UNSET
    capture_asap: bool | Unset = True
    has_control: bool | Unset = False
    max_cloud_coverage: int | Unset = 0
    max_nadir_angle: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resolution = self.resolution

        sensor = self.sensor

        capture_frequency = self.capture_frequency

        datum = self.datum

        file_format = self.file_format

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        capture_asap = self.capture_asap

        has_control = self.has_control

        max_cloud_coverage = self.max_cloud_coverage

        max_nadir_angle = self.max_nadir_angle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resolution": resolution,
                "sensor": sensor,
                "capture_frequency": capture_frequency,
                "datum": datum,
                "file_format": file_format,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if capture_asap is not UNSET:
            field_dict["capture_asap"] = capture_asap
        if has_control is not UNSET:
            field_dict["has_control"] = has_control
        if max_cloud_coverage is not UNSET:
            field_dict["max_cloud_coverage"] = max_cloud_coverage
        if max_nadir_angle is not UNSET:
            field_dict["max_nadir_angle"] = max_nadir_angle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        resolution = d.pop("resolution")

        sensor = d.pop("sensor")

        capture_frequency = d.pop("capture_frequency")

        datum = d.pop("datum")

        file_format = d.pop("file_format")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        capture_asap = d.pop("capture_asap", UNSET)

        has_control = d.pop("has_control", UNSET)

        max_cloud_coverage = d.pop("max_cloud_coverage", UNSET)

        max_nadir_angle = d.pop("max_nadir_angle", UNSET)

        template_save_input = cls(
            name=name,
            resolution=resolution,
            sensor=sensor,
            capture_frequency=capture_frequency,
            datum=datum,
            file_format=file_format,
            description=description,
            capture_asap=capture_asap,
            has_control=has_control,
            max_cloud_coverage=max_cloud_coverage,
            max_nadir_angle=max_nadir_angle,
        )

        template_save_input.additional_properties = d
        return template_save_input

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
