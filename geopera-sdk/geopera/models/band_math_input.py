from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.band_math_input_bbox import BandMathInputBbox


T = TypeVar("T", bound="BandMathInput")


@_attrs_define
class BandMathInput:
    """
    Attributes:
        cog_url (str):
        formula (str):
        bbox (BandMathInputBbox):
        sensor (str):
        max_size (int | Unset):  Default: 2048.
        output_format (str | Unset):  Default: 'json'.
        colormap (str | Unset):  Default: 'viridis'.
        vmin (float | None | Unset):
        vmax (float | None | Unset):
    """

    cog_url: str
    formula: str
    bbox: BandMathInputBbox
    sensor: str
    max_size: int | Unset = 2048
    output_format: str | Unset = "json"
    colormap: str | Unset = "viridis"
    vmin: float | None | Unset = UNSET
    vmax: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cog_url = self.cog_url

        formula = self.formula

        bbox = self.bbox.to_dict()

        sensor = self.sensor

        max_size = self.max_size

        output_format = self.output_format

        colormap = self.colormap

        vmin: float | None | Unset
        if isinstance(self.vmin, Unset):
            vmin = UNSET
        else:
            vmin = self.vmin

        vmax: float | None | Unset
        if isinstance(self.vmax, Unset):
            vmax = UNSET
        else:
            vmax = self.vmax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cog_url": cog_url,
                "formula": formula,
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
        if vmin is not UNSET:
            field_dict["vmin"] = vmin
        if vmax is not UNSET:
            field_dict["vmax"] = vmax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.band_math_input_bbox import BandMathInputBbox

        d = dict(src_dict)
        cog_url = d.pop("cog_url")

        formula = d.pop("formula")

        bbox = BandMathInputBbox.from_dict(d.pop("bbox"))

        sensor = d.pop("sensor")

        max_size = d.pop("max_size", UNSET)

        output_format = d.pop("output_format", UNSET)

        colormap = d.pop("colormap", UNSET)

        def _parse_vmin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vmin = _parse_vmin(d.pop("vmin", UNSET))

        def _parse_vmax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vmax = _parse_vmax(d.pop("vmax", UNSET))

        band_math_input = cls(
            cog_url=cog_url,
            formula=formula,
            bbox=bbox,
            sensor=sensor,
            max_size=max_size,
            output_format=output_format,
            colormap=colormap,
            vmin=vmin,
            vmax=vmax,
        )

        band_math_input.additional_properties = d
        return band_math_input

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
