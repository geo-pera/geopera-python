from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_event_output_alert_event import AlertEventOutputAlertEvent


T = TypeVar("T", bound="AlertEventOutput")


@_attrs_define
class AlertEventOutput:
    """
    Attributes:
        alert_event (AlertEventOutputAlertEvent):
    """

    alert_event: AlertEventOutputAlertEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_event = self.alert_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_event": alert_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_event_output_alert_event import AlertEventOutputAlertEvent

        d = dict(src_dict)
        alert_event = AlertEventOutputAlertEvent.from_dict(d.pop("alert_event"))

        alert_event_output = cls(
            alert_event=alert_event,
        )

        alert_event_output.additional_properties = d
        return alert_event_output

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
