from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cog_stats_input_geometry import CogStatsInputGeometry


T = TypeVar("T", bound="CogStatsInput")


@_attrs_define
class CogStatsInput:
    """
    Attributes:
        url (str):
        geometry (CogStatsInputGeometry):
        expression (None | str | Unset):
        bands (None | str | Unset):
        percentiles (list[float] | Unset):
    """

    url: str
    geometry: CogStatsInputGeometry
    expression: None | str | Unset = UNSET
    bands: None | str | Unset = UNSET
    percentiles: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        geometry = self.geometry.to_dict()

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

        percentiles: list[float] | Unset = UNSET
        if not isinstance(self.percentiles, Unset):
            percentiles = []
            for percentiles_item_data in self.percentiles:
                percentiles_item: float
                percentiles_item = percentiles_item_data
                percentiles.append(percentiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "geometry": geometry,
            }
        )
        if expression is not UNSET:
            field_dict["expression"] = expression
        if bands is not UNSET:
            field_dict["bands"] = bands
        if percentiles is not UNSET:
            field_dict["percentiles"] = percentiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cog_stats_input_geometry import CogStatsInputGeometry

        d = dict(src_dict)
        url = d.pop("url")

        geometry = CogStatsInputGeometry.from_dict(d.pop("geometry"))

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

        _percentiles = d.pop("percentiles", UNSET)
        percentiles: list[float] | Unset = UNSET
        if _percentiles is not UNSET:
            percentiles = []
            for percentiles_item_data in _percentiles:

                def _parse_percentiles_item(data: object) -> float:
                    return cast(float, data)

                percentiles_item = _parse_percentiles_item(percentiles_item_data)

                percentiles.append(percentiles_item)

        cog_stats_input = cls(
            url=url,
            geometry=geometry,
            expression=expression,
            bands=bands,
            percentiles=percentiles,
        )

        cog_stats_input.additional_properties = d
        return cog_stats_input

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
