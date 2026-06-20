from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetBandNamesInput")


@_attrs_define
class SetBandNamesInput:
    """
    Attributes:
        item_id (str):
        asset_id (str):
        band_names (list[str]):
    """

    item_id: str
    asset_id: str
    band_names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        asset_id = self.asset_id

        band_names = self.band_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "asset_id": asset_id,
                "band_names": band_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        asset_id = d.pop("asset_id")

        band_names = cast(list[str], d.pop("band_names"))

        set_band_names_input = cls(
            item_id=item_id,
            asset_id=asset_id,
            band_names=band_names,
        )

        set_band_names_input.additional_properties = d
        return set_band_names_input

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
