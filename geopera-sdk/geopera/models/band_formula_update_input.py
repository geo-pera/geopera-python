from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandFormulaUpdateInput")


@_attrs_define
class BandFormulaUpdateInput:
    """
    Attributes:
        formula_id (str):
        name (None | str | Unset):
        formula (None | str | Unset):
        display_name (None | str | Unset):
        description (None | str | Unset):
        colormap (None | str | Unset):
        value_range (list[float] | None | Unset):
        category (None | str | Unset):
    """

    formula_id: str
    name: None | str | Unset = UNSET
    formula: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    colormap: None | str | Unset = UNSET
    value_range: list[float] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formula_id = self.formula_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        formula: None | str | Unset
        if isinstance(self.formula, Unset):
            formula = UNSET
        else:
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

        colormap: None | str | Unset
        if isinstance(self.colormap, Unset):
            colormap = UNSET
        else:
            colormap = self.colormap

        value_range: list[float] | None | Unset
        if isinstance(self.value_range, Unset):
            value_range = UNSET
        elif isinstance(self.value_range, list):
            value_range = self.value_range

        else:
            value_range = self.value_range

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formula_id": formula_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if formula is not UNSET:
            field_dict["formula"] = formula
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
        formula_id = d.pop("formula_id")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formula = _parse_formula(d.pop("formula", UNSET))

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

        def _parse_colormap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        colormap = _parse_colormap(d.pop("colormap", UNSET))

        def _parse_value_range(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_range_type_0 = cast(list[float], data)

                return value_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        value_range = _parse_value_range(d.pop("value_range", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        band_formula_update_input = cls(
            formula_id=formula_id,
            name=name,
            formula=formula,
            display_name=display_name,
            description=description,
            colormap=colormap,
            value_range=value_range,
            category=category,
        )

        band_formula_update_input.additional_properties = d
        return band_formula_update_input

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
