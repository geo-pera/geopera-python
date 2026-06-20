from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateFormulaOutput")


@_attrs_define
class ValidateFormulaOutput:
    """
    Attributes:
        formula (str):
        sensor (str):
        valid (bool):
        error (None | str | Unset):
        required_bands (list[str] | Unset):
        available_bands (list[str] | Unset):
    """

    formula: str
    sensor: str
    valid: bool
    error: None | str | Unset = UNSET
    required_bands: list[str] | Unset = UNSET
    available_bands: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formula = self.formula

        sensor = self.sensor

        valid = self.valid

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        required_bands: list[str] | Unset = UNSET
        if not isinstance(self.required_bands, Unset):
            required_bands = self.required_bands

        available_bands: list[str] | Unset = UNSET
        if not isinstance(self.available_bands, Unset):
            available_bands = self.available_bands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formula": formula,
                "sensor": sensor,
                "valid": valid,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if required_bands is not UNSET:
            field_dict["required_bands"] = required_bands
        if available_bands is not UNSET:
            field_dict["available_bands"] = available_bands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        formula = d.pop("formula")

        sensor = d.pop("sensor")

        valid = d.pop("valid")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        required_bands = cast(list[str], d.pop("required_bands", UNSET))

        available_bands = cast(list[str], d.pop("available_bands", UNSET))

        validate_formula_output = cls(
            formula=formula,
            sensor=sensor,
            valid=valid,
            error=error,
            required_bands=required_bands,
            available_bands=available_bands,
        )

        validate_formula_output.additional_properties = d
        return validate_formula_output

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
