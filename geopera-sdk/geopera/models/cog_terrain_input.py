from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CogTerrainInput")


@_attrs_define
class CogTerrainInput:
    """
    Attributes:
        url (str):
        z (int):
        x (int):
        y (int):
        invert (bool | Unset):  Default: False.
        aoi (None | str | Unset):
    """

    url: str
    z: int
    x: int
    y: int
    invert: bool | Unset = False
    aoi: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        z = self.z

        x = self.x

        y = self.y

        invert = self.invert

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
            }
        )
        if invert is not UNSET:
            field_dict["invert"] = invert
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

        invert = d.pop("invert", UNSET)

        def _parse_aoi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aoi = _parse_aoi(d.pop("aoi", UNSET))

        cog_terrain_input = cls(
            url=url,
            z=z,
            x=x,
            y=y,
            invert=invert,
            aoi=aoi,
        )

        cog_terrain_input.additional_properties = d
        return cog_terrain_input

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
