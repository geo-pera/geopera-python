from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkInvoicedInput")


@_attrs_define
class MarkInvoicedInput:
    """
    Attributes:
        organization_id (str):
        reference (str):
        period (None | str | Unset):
        order_ids (list[str] | None | Unset):
        note (None | str | Unset):
    """

    organization_id: str
    reference: str
    period: None | str | Unset = UNSET
    order_ids: list[str] | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        reference = self.reference

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        order_ids: list[str] | None | Unset
        if isinstance(self.order_ids, Unset):
            order_ids = UNSET
        elif isinstance(self.order_ids, list):
            order_ids = self.order_ids

        else:
            order_ids = self.order_ids

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "reference": reference,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period
        if order_ids is not UNSET:
            field_dict["order_ids"] = order_ids
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organization_id")

        reference = d.pop("reference")

        def _parse_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        def _parse_order_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                order_ids_type_0 = cast(list[str], data)

                return order_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        order_ids = _parse_order_ids(d.pop("order_ids", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        mark_invoiced_input = cls(
            organization_id=organization_id,
            reference=reference,
            period=period,
            order_ids=order_ids,
            note=note,
        )

        mark_invoiced_input.additional_properties = d
        return mark_invoiced_input

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
