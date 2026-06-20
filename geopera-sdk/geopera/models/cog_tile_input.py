from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CogTileInput")


@_attrs_define
class CogTileInput:
    """
    Attributes:
        url (str):
        z (int):
        x (int):
        y (int):
        format_ (str):
        bands (None | str | Unset):
        expression (None | str | Unset):
        rescale (None | str | Unset):
        colormap (None | str | Unset):
        quality (int | Unset):  Default: 85.
        aoi (None | str | Unset):
    """

    url: str
    z: int
    x: int
    y: int
    format_: str
    bands: None | str | Unset = UNSET
    expression: None | str | Unset = UNSET
    rescale: None | str | Unset = UNSET
    colormap: None | str | Unset = UNSET
    quality: int | Unset = 85
    aoi: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        z = self.z

        x = self.x

        y = self.y

        format_ = self.format_

        bands: None | str | Unset
        if isinstance(self.bands, Unset):
            bands = UNSET
        else:
            bands = self.bands

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        rescale: None | str | Unset
        if isinstance(self.rescale, Unset):
            rescale = UNSET
        else:
            rescale = self.rescale

        colormap: None | str | Unset
        if isinstance(self.colormap, Unset):
            colormap = UNSET
        else:
            colormap = self.colormap

        quality = self.quality

        aoi: None | str | Unset
        if isinstance(self.aoi, Unset):
            aoi = UNSET
        else:
            aoi = self.aoi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "z": z,
                "x": x,
                "y": y,
                "format": format_,
            }
        )
        if bands is not UNSET:
            field_dict["bands"] = bands
        if expression is not UNSET:
            field_dict["expression"] = expression
        if rescale is not UNSET:
            field_dict["rescale"] = rescale
        if colormap is not UNSET:
            field_dict["colormap"] = colormap
        if quality is not UNSET:
            field_dict["quality"] = quality
        if aoi is not UNSET:
            field_dict["aoi"] = aoi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        z = d.pop("z")

        x = d.pop("x")

        y = d.pop("y")

        format_ = d.pop("format")

        def _parse_bands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bands = _parse_bands(d.pop("bands", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_rescale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rescale = _parse_rescale(d.pop("rescale", UNSET))

        def _parse_colormap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        colormap = _parse_colormap(d.pop("colormap", UNSET))

        quality = d.pop("quality", UNSET)

        def _parse_aoi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aoi = _parse_aoi(d.pop("aoi", UNSET))

        cog_tile_input = cls(
            url=url,
            z=z,
            x=x,
            y=y,
            format_=format_,
            bands=bands,
            expression=expression,
            rescale=rescale,
            colormap=colormap,
            quality=quality,
            aoi=aoi,
        )

        cog_tile_input.additional_properties = d
        return cog_tile_input

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
