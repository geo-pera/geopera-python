from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetAutoTopupOutput")


@_attrs_define
class SetAutoTopupOutput:
    """
    Attributes:
        enabled (bool):
        threshold_credits (int):
        topup_amount_credits (int):
    """

    enabled: bool
    threshold_credits: int
    topup_amount_credits: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        threshold_credits = self.threshold_credits

        topup_amount_credits = self.topup_amount_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "threshold_credits": threshold_credits,
                "topup_amount_credits": topup_amount_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        threshold_credits = d.pop("threshold_credits")

        topup_amount_credits = d.pop("topup_amount_credits")

        set_auto_topup_output = cls(
            enabled=enabled,
            threshold_credits=threshold_credits,
            topup_amount_credits=topup_amount_credits,
        )

        set_auto_topup_output.additional_properties = d
        return set_auto_topup_output

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
