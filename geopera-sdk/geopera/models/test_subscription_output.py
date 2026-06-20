from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestSubscriptionOutput")


@_attrs_define
class TestSubscriptionOutput:
    """
    Attributes:
        status (str):
        delivered (bool):
        event_id (str):
        event_type (str):
        http_status (int | None | Unset):
        error (None | str | Unset):
    """

    status: str
    delivered: bool
    event_id: str
    event_type: str
    http_status: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        delivered = self.delivered

        event_id = self.event_id

        event_type = self.event_type

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "delivered": delivered,
                "event_id": event_id,
                "event_type": event_type,
            }
        )
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        delivered = d.pop("delivered")

        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("http_status", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        test_subscription_output = cls(
            status=status,
            delivered=delivered,
            event_id=event_id,
            event_type=event_type,
            http_status=http_status,
            error=error,
        )

        test_subscription_output.additional_properties = d
        return test_subscription_output

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
