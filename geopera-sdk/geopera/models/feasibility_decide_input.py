from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeasibilityDecideInput")


@_attrs_define
class FeasibilityDecideInput:
    """
    Attributes:
        study_id (str):
        accepted_option_id (str):
    """

    study_id: str
    accepted_option_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        study_id = self.study_id

        accepted_option_id = self.accepted_option_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "study_id": study_id,
                "acceptedOptionId": accepted_option_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        study_id = d.pop("study_id")

        accepted_option_id = d.pop("acceptedOptionId")

        feasibility_decide_input = cls(
            study_id=study_id,
            accepted_option_id=accepted_option_id,
        )

        feasibility_decide_input.additional_properties = d
        return feasibility_decide_input

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
