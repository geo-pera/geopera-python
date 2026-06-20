from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_tile_input_aoi_clip_body_type_0 import CatalogTileInputAoiClipBodyType0


T = TypeVar("T", bound="CatalogTileInput")


@_attrs_define
class CatalogTileInput:
    """
    Attributes:
        collection (str):
        scene_id (str):
        visualization (str):
        z (int):
        x (int):
        y (int):
        format_ (str):
        provider (None | str | Unset):
        quality (int | None | Unset):  Default: 95.
        aoi_clip (None | str | Unset):
        aoi_clip_body (CatalogTileInputAoiClipBodyType0 | None | Unset):
        expression (None | str | Unset):
        colormap (None | str | Unset):
        rescale (None | str | Unset):
    """

    collection: str
    scene_id: str
    visualization: str
    z: int
    x: int
    y: int
    format_: str
    provider: None | str | Unset = UNSET
    quality: int | None | Unset = 95
    aoi_clip: None | str | Unset = UNSET
    aoi_clip_body: CatalogTileInputAoiClipBodyType0 | None | Unset = UNSET
    expression: None | str | Unset = UNSET
    colormap: None | str | Unset = UNSET
    rescale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_tile_input_aoi_clip_body_type_0 import CatalogTileInputAoiClipBodyType0

        collection = self.collection

        scene_id = self.scene_id

        visualization = self.visualization

        z = self.z

        x = self.x

        y = self.y

        format_ = self.format_

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        quality: int | None | Unset
        if isinstance(self.quality, Unset):
            quality = UNSET
        else:
            quality = self.quality

        aoi_clip: None | str | Unset
        if isinstance(self.aoi_clip, Unset):
            aoi_clip = UNSET
        else:
            aoi_clip = self.aoi_clip

        aoi_clip_body: dict[str, Any] | None | Unset
        if isinstance(self.aoi_clip_body, Unset):
            aoi_clip_body = UNSET
        elif isinstance(self.aoi_clip_body, CatalogTileInputAoiClipBodyType0):
            aoi_clip_body = self.aoi_clip_body.to_dict()
        else:
            aoi_clip_body = self.aoi_clip_body

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        colormap: None | str | Unset
        if isinstance(self.colormap, Unset):
            colormap = UNSET
        else:
            colormap = self.colormap

        rescale: None | str | Unset
        if isinstance(self.rescale, Unset):
            rescale = UNSET
        else:
            rescale = self.rescale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "scene_id": scene_id,
                "visualization": visualization,
                "z": z,
                "x": x,
                "y": y,
                "format": format_,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if quality is not UNSET:
            field_dict["quality"] = quality
        if aoi_clip is not UNSET:
            field_dict["aoi_clip"] = aoi_clip
        if aoi_clip_body is not UNSET:
            field_dict["aoi_clip_body"] = aoi_clip_body
        if expression is not UNSET:
            field_dict["expression"] = expression
        if colormap is not UNSET:
            field_dict["colormap"] = colormap
        if rescale is not UNSET:
            field_dict["rescale"] = rescale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_tile_input_aoi_clip_body_type_0 import CatalogTileInputAoiClipBodyType0

        d = dict(src_dict)
        collection = d.pop("collection")

        scene_id = d.pop("scene_id")

        visualization = d.pop("visualization")

        z = d.pop("z")

        x = d.pop("x")

        y = d.pop("y")

        format_ = d.pop("format")

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_quality(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quality = _parse_quality(d.pop("quality", UNSET))

        def _parse_aoi_clip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aoi_clip = _parse_aoi_clip(d.pop("aoi_clip", UNSET))

        def _parse_aoi_clip_body(data: object) -> CatalogTileInputAoiClipBodyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aoi_clip_body_type_0 = CatalogTileInputAoiClipBodyType0.from_dict(data)

                return aoi_clip_body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogTileInputAoiClipBodyType0 | None | Unset, data)

        aoi_clip_body = _parse_aoi_clip_body(d.pop("aoi_clip_body", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_colormap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        colormap = _parse_colormap(d.pop("colormap", UNSET))

        def _parse_rescale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rescale = _parse_rescale(d.pop("rescale", UNSET))

        catalog_tile_input = cls(
            collection=collection,
            scene_id=scene_id,
            visualization=visualization,
            z=z,
            x=x,
            y=y,
            format_=format_,
            provider=provider,
            quality=quality,
            aoi_clip=aoi_clip,
            aoi_clip_body=aoi_clip_body,
            expression=expression,
            colormap=colormap,
            rescale=rescale,
        )

        catalog_tile_input.additional_properties = d
        return catalog_tile_input

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
