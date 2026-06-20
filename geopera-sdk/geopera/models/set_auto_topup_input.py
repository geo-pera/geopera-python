from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAutoTopupInput")


@_attrs_define
class SetAutoTopupInput:
    """
    Attributes:
        enabled (bool):
        threshold_credits (int):
        topup_amount_credits (int):
        daily_charge_cap_aud (float | None | Unset):
    """

    enabled: bool
    threshold_credits: int
    topup_amount_credits: int
    daily_charge_cap_aud: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        threshold_credits = self.threshold_credits

        topup_amount_credits = self.topup_amount_credits

        daily_charge_cap_aud: float | None | Unset
        if isinstance(self.daily_charge_cap_aud, Unset):
            daily_charge_cap_aud = UNSET
        else:
            daily_charge_cap_aud = self.daily_charge_cap_aud

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "threshold_credits": threshold_credits,
                "topup_amount_credits": topup_amount_credits,
            }
        )
        if daily_charge_cap_aud is not UNSET:
            field_dict["daily_charge_cap_aud"] = daily_charge_cap_aud

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        threshold_credits = d.pop("threshold_credits")

        topup_amount_credits = d.pop("topup_amount_credits")

        def _parse_daily_charge_cap_aud(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_charge_cap_aud = _parse_daily_charge_cap_aud(d.pop("daily_charge_cap_aud", UNSET))

        set_auto_topup_input = cls(
            enabled=enabled,
            threshold_credits=threshold_credits,
            topup_amount_credits=topup_amount_credits,
            daily_charge_cap_aud=daily_charge_cap_aud,
        )

        set_auto_topup_input.additional_properties = d
        return set_auto_topup_input

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
