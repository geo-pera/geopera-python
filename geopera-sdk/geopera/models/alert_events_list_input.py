from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEventsListInput")


@_attrs_define
class AlertEventsListInput:
    """
    Attributes:
        rule_id (None | str | Unset):
        acknowledged (bool | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
    """

    rule_id: None | str | Unset = UNSET
    acknowledged: bool | None | Unset = UNSET
    limit: int | Unset = 50
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_id: None | str | Unset
        if isinstance(self.rule_id, Unset):
            rule_id = UNSET
        else:
            rule_id = self.rule_id

        acknowledged: bool | None | Unset
        if isinstance(self.acknowledged, Unset):
            acknowledged = UNSET
        else:
            acknowledged = self.acknowledged

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if acknowledged is not UNSET:
            field_dict["acknowledged"] = acknowledged
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rule_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule_id = _parse_rule_id(d.pop("rule_id", UNSET))

        def _parse_acknowledged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        acknowledged = _parse_acknowledged(d.pop("acknowledged", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        alert_events_list_input = cls(
            rule_id=rule_id,
            acknowledged=acknowledged,
            limit=limit,
            offset=offset,
        )

        alert_events_list_input.additional_properties = d
        return alert_events_list_input

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
