from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandFormulaCreateInput")


@_attrs_define
class BandFormulaCreateInput:
    """
    Attributes:
        name (str):
        formula (str):
        display_name (None | str | Unset):
        description (None | str | Unset):
        colormap (str | Unset):  Default: 'RdYlGn'.
        value_range (list[float] | Unset):
        category (str | Unset):  Default: 'custom'.
    """

    name: str
    formula: str
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    colormap: str | Unset = "RdYlGn"
    value_range: list[float] | Unset = UNSET
    category: str | Unset = "custom"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        formula = self.formula

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        colormap = self.colormap

        value_range: list[float] | Unset = UNSET
        if not isinstance(self.value_range, Unset):
            value_range = self.value_range

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "formula": formula,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if colormap is not UNSET:
            field_dict["colormap"] = colormap
        if value_range is not UNSET:
            field_dict["value_range"] = value_range
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        formula = d.pop("formula")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        colormap = d.pop("colormap", UNSET)

        value_range = cast(list[float], d.pop("value_range", UNSET))

        category = d.pop("category", UNSET)

        band_formula_create_input = cls(
            name=name,
            formula=formula,
            display_name=display_name,
            description=description,
            colormap=colormap,
            value_range=value_range,
            category=category,
        )

        band_formula_create_input.additional_properties = d
        return band_formula_create_input

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
