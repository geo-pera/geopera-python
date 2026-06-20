from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GranulePointsOutput")


@_attrs_define
class GranulePointsOutput:
    """
    Attributes:
        points (list[list[float]] | Unset): [lon, lat, elevation_m, value] rows
        value_label (str | Unset):  Default: ''.
        value_range (list[float] | Unset):
        count (int | Unset):  Default: 0.
        returned (int | Unset):  Default: 0.
        subsampled (bool | Unset):  Default: False.
    """

    points: list[list[float]] | Unset = UNSET
    value_label: str | Unset = ""
    value_range: list[float] | Unset = UNSET
    count: int | Unset = 0
    returned: int | Unset = 0
    subsampled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points: list[list[float]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data

                points.append(points_item)

        value_label = self.value_label

        value_range: list[float] | Unset = UNSET
        if not isinstance(self.value_range, Unset):
            value_range = self.value_range

        count = self.count

        returned = self.returned

        subsampled = self.subsampled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points is not UNSET:
            field_dict["points"] = points
        if value_label is not UNSET:
            field_dict["value_label"] = value_label
        if value_range is not UNSET:
            field_dict["value_range"] = value_range
        if count is not UNSET:
            field_dict["count"] = count
        if returned is not UNSET:
            field_dict["returned"] = returned
        if subsampled is not UNSET:
            field_dict["subsampled"] = subsampled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _points = d.pop("points", UNSET)
        points: list[list[float]] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = cast(list[float], points_item_data)

                points.append(points_item)

        value_label = d.pop("value_label", UNSET)

        value_range = cast(list[float], d.pop("value_range", UNSET))

        count = d.pop("count", UNSET)

        returned = d.pop("returned", UNSET)

        subsampled = d.pop("subsampled", UNSET)

        granule_points_output = cls(
            points=points,
            value_label=value_label,
            value_range=value_range,
            count=count,
            returned=returned,
            subsampled=subsampled,
        )

        granule_points_output.additional_properties = d
        return granule_points_output

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
