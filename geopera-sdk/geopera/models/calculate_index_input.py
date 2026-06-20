from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calculate_index_input_bbox import CalculateIndexInputBbox


T = TypeVar("T", bound="CalculateIndexInput")


@_attrs_define
class CalculateIndexInput:
    """
    Attributes:
        cog_url (str):
        index_name (str):
        bbox (CalculateIndexInputBbox):
        sensor (str):
        max_size (int | Unset):  Default: 2048.
        output_format (str | Unset):  Default: 'json'.
        colormap (None | str | Unset):
    """

    cog_url: str
    index_name: str
    bbox: CalculateIndexInputBbox
    sensor: str
    max_size: int | Unset = 2048
    output_format: str | Unset = "json"
    colormap: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cog_url = self.cog_url

        index_name = self.index_name

        bbox = self.bbox.to_dict()

        sensor = self.sensor

        max_size = self.max_size

        output_format = self.output_format

        colormap: None | str | Unset
        if isinstance(self.colormap, Unset):
            colormap = UNSET
        else:
            colormap = self.colormap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cog_url": cog_url,
                "index_name": index_name,
                "bbox": bbox,
                "sensor": sensor,
            }
        )
        if max_size is not UNSET:
            field_dict["max_size"] = max_size
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if colormap is not UNSET:
            field_dict["colormap"] = colormap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calculate_index_input_bbox import CalculateIndexInputBbox

        d = dict(src_dict)
        cog_url = d.pop("cog_url")

        index_name = d.pop("index_name")

        bbox = CalculateIndexInputBbox.from_dict(d.pop("bbox"))

        sensor = d.pop("sensor")

        max_size = d.pop("max_size", UNSET)

        output_format = d.pop("output_format", UNSET)

        def _parse_colormap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        colormap = _parse_colormap(d.pop("colormap", UNSET))

        calculate_index_input = cls(
            cog_url=cog_url,
            index_name=index_name,
            bbox=bbox,
            sensor=sensor,
            max_size=max_size,
            output_format=output_format,
            colormap=colormap,
        )

        calculate_index_input.additional_properties = d
        return calculate_index_input

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
