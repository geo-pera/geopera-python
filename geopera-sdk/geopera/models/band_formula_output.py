from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandFormulaOutput")


@_attrs_define
class BandFormulaOutput:
    """
    Attributes:
        id (str):
        organization_id (str):
        name (str):
        formula (str):
        colormap (str):
        value_range (list[float]):
        category (str):
        is_template (bool):
        created_at (str):
        updated_at (str):
        display_name (None | str | Unset):
        description (None | str | Unset):
        required_bands (list[str] | Unset):
    """

    id: str
    organization_id: str
    name: str
    formula: str
    colormap: str
    value_range: list[float]
    category: str
    is_template: bool
    created_at: str
    updated_at: str
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    required_bands: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        name = self.name

        formula = self.formula

        colormap = self.colormap

        value_range = self.value_range

        category = self.category

        is_template = self.is_template

        created_at = self.created_at

        updated_at = self.updated_at

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

        required_bands: list[str] | Unset = UNSET
        if not isinstance(self.required_bands, Unset):
            required_bands = self.required_bands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_id": organization_id,
                "name": name,
                "formula": formula,
                "colormap": colormap,
                "value_range": value_range,
                "category": category,
                "is_template": is_template,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if required_bands is not UNSET:
            field_dict["required_bands"] = required_bands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organization_id")

        name = d.pop("name")

        formula = d.pop("formula")

        colormap = d.pop("colormap")

        value_range = cast(list[float], d.pop("value_range"))

        category = d.pop("category")

        is_template = d.pop("is_template")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

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

        required_bands = cast(list[str], d.pop("required_bands", UNSET))

        band_formula_output = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            formula=formula,
            colormap=colormap,
            value_range=value_range,
            category=category,
            is_template=is_template,
            created_at=created_at,
            updated_at=updated_at,
            display_name=display_name,
            description=description,
            required_bands=required_bands,
        )

        band_formula_output.additional_properties = d
        return band_formula_output

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
