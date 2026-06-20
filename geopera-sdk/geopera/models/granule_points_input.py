from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.granule_points_input_clip_polygon_type_0 import GranulePointsInputClipPolygonType0


T = TypeVar("T", bound="GranulePointsInput")


@_attrs_define
class GranulePointsInput:
    """
    Attributes:
        collection (str): Registry collection id, e.g.
        href (str): HTTPS .h5 granule URL from the STAC item (Earthdata-hosted)
        bbox (list[float]): AOI [west, south, east, north]
        max_points (int | Unset): Uniform-subsample ceiling Default: 60000.
        clip_polygon (GranulePointsInputClipPolygonType0 | None | Unset): AOI GeoJSON Polygon/MultiPolygon — points are
            clipped to this exact shape, not just the bbox
    """

    collection: str
    href: str
    bbox: list[float]
    max_points: int | Unset = 60000
    clip_polygon: GranulePointsInputClipPolygonType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.granule_points_input_clip_polygon_type_0 import GranulePointsInputClipPolygonType0

        collection = self.collection

        href = self.href

        bbox = self.bbox

        max_points = self.max_points

        clip_polygon: dict[str, Any] | None | Unset
        if isinstance(self.clip_polygon, Unset):
            clip_polygon = UNSET
        elif isinstance(self.clip_polygon, GranulePointsInputClipPolygonType0):
            clip_polygon = self.clip_polygon.to_dict()
        else:
            clip_polygon = self.clip_polygon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "href": href,
                "bbox": bbox,
            }
        )
        if max_points is not UNSET:
            field_dict["max_points"] = max_points
        if clip_polygon is not UNSET:
            field_dict["clip_polygon"] = clip_polygon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.granule_points_input_clip_polygon_type_0 import GranulePointsInputClipPolygonType0

        d = dict(src_dict)
        collection = d.pop("collection")

        href = d.pop("href")

        bbox = cast(list[float], d.pop("bbox"))

        max_points = d.pop("max_points", UNSET)

        def _parse_clip_polygon(data: object) -> GranulePointsInputClipPolygonType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clip_polygon_type_0 = GranulePointsInputClipPolygonType0.from_dict(data)

                return clip_polygon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GranulePointsInputClipPolygonType0 | None | Unset, data)

        clip_polygon = _parse_clip_polygon(d.pop("clip_polygon", UNSET))

        granule_points_input = cls(
            collection=collection,
            href=href,
            bbox=bbox,
            max_points=max_points,
            clip_polygon=clip_polygon,
        )

        granule_points_input.additional_properties = d
        return granule_points_input

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
