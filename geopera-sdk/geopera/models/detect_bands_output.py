from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetectBandsOutput")


@_attrs_define
class DetectBandsOutput:
    """
    Attributes:
        suggested_band_names (list[Any] | Unset):
        current_band_names (list[Any] | Unset):
        method (str | Unset):  Default: 'reflectance_ranking'.
    """

    suggested_band_names: list[Any] | Unset = UNSET
    current_band_names: list[Any] | Unset = UNSET
    method: str | Unset = "reflectance_ranking"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggested_band_names: list[Any] | Unset = UNSET
        if not isinstance(self.suggested_band_names, Unset):
            suggested_band_names = self.suggested_band_names

        current_band_names: list[Any] | Unset = UNSET
        if not isinstance(self.current_band_names, Unset):
            current_band_names = self.current_band_names

        method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggested_band_names is not UNSET:
            field_dict["suggested_band_names"] = suggested_band_names
        if current_band_names is not UNSET:
            field_dict["current_band_names"] = current_band_names
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggested_band_names = cast(list[Any], d.pop("suggested_band_names", UNSET))

        current_band_names = cast(list[Any], d.pop("current_band_names", UNSET))

        method = d.pop("method", UNSET)

        detect_bands_output = cls(
            suggested_band_names=suggested_band_names,
            current_band_names=current_band_names,
            method=method,
        )

        detect_bands_output.additional_properties = d
        return detect_bands_output

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
