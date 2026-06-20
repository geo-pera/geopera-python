from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemTileRenderInput")


@_attrs_define
class ItemTileRenderInput:
    """
    Attributes:
        item_id (str):
        z (int):
        x (int):
        y (int):
        format_ (str | Unset):  Default: 'webp'.
        profile (None | str | Unset):
        asset_key (None | str | Unset):
        expression (None | str | Unset):
        bands (None | str | Unset):
        rescale (None | str | Unset):
        colormap (None | str | Unset):
        quality (int | Unset):  Default: 82.
    """

    item_id: str
    z: int
    x: int
    y: int
    format_: str | Unset = "webp"
    profile: None | str | Unset = UNSET
    asset_key: None | str | Unset = UNSET
    expression: None | str | Unset = UNSET
    bands: None | str | Unset = UNSET
    rescale: None | str | Unset = UNSET
    colormap: None | str | Unset = UNSET
    quality: int | Unset = 82
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        z = self.z

        x = self.x

        y = self.y

        format_ = self.format_

        profile: None | str | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        bands: None | str | Unset
        if isinstance(self.bands, Unset):
            bands = UNSET
        else:
            bands = self.bands

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "z": z,
                "x": x,
                "y": y,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if profile is not UNSET:
            field_dict["profile"] = profile
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key
        if expression is not UNSET:
            field_dict["expression"] = expression
        if bands is not UNSET:
            field_dict["bands"] = bands
        if rescale is not UNSET:
            field_dict["rescale"] = rescale
        if colormap is not UNSET:
            field_dict["colormap"] = colormap
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        z = d.pop("z")

        x = d.pop("x")

        y = d.pop("y")

        format_ = d.pop("format", UNSET)

        def _parse_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_bands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bands = _parse_bands(d.pop("bands", UNSET))

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

        item_tile_render_input = cls(
            item_id=item_id,
            z=z,
            x=x,
            y=y,
            format_=format_,
            profile=profile,
            asset_key=asset_key,
            expression=expression,
            bands=bands,
            rescale=rescale,
            colormap=colormap,
            quality=quality,
        )

        item_tile_render_input.additional_properties = d
        return item_tile_render_input

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
