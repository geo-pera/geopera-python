from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alert_rule_input_band_mapping import CreateAlertRuleInputBandMapping


T = TypeVar("T", bound="CreateAlertRuleInput")


@_attrs_define
class CreateAlertRuleInput:
    """
    Attributes:
        name (str):
        expression (str):
        comparison (str):
        threshold (float):
        description (None | str | Unset):
        collection_id (None | str | Unset):
        event_types (list[str] | Unset):
        threshold_upper (float | None | Unset):
        asset_key (str | Unset):  Default: 'data'.
        band_mapping (CreateAlertRuleInputBandMapping | Unset):
        notification_channels (list[str] | Unset):
        cooldown_minutes (int | Unset):  Default: 60.
    """

    name: str
    expression: str
    comparison: str
    threshold: float
    description: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    threshold_upper: float | None | Unset = UNSET
    asset_key: str | Unset = "data"
    band_mapping: CreateAlertRuleInputBandMapping | Unset = UNSET
    notification_channels: list[str] | Unset = UNSET
    cooldown_minutes: int | Unset = 60
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        expression = self.expression

        comparison = self.comparison

        threshold = self.threshold

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        threshold_upper: float | None | Unset
        if isinstance(self.threshold_upper, Unset):
            threshold_upper = UNSET
        else:
            threshold_upper = self.threshold_upper

        asset_key = self.asset_key

        band_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_mapping, Unset):
            band_mapping = self.band_mapping.to_dict()

        notification_channels: list[str] | Unset = UNSET
        if not isinstance(self.notification_channels, Unset):
            notification_channels = self.notification_channels

        cooldown_minutes = self.cooldown_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "expression": expression,
                "comparison": comparison,
                "threshold": threshold,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if threshold_upper is not UNSET:
            field_dict["threshold_upper"] = threshold_upper
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key
        if band_mapping is not UNSET:
            field_dict["band_mapping"] = band_mapping
        if notification_channels is not UNSET:
            field_dict["notification_channels"] = notification_channels
        if cooldown_minutes is not UNSET:
            field_dict["cooldown_minutes"] = cooldown_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_alert_rule_input_band_mapping import CreateAlertRuleInputBandMapping

        d = dict(src_dict)
        name = d.pop("name")

        expression = d.pop("expression")

        comparison = d.pop("comparison")

        threshold = d.pop("threshold")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        event_types = cast(list[str], d.pop("event_types", UNSET))

        def _parse_threshold_upper(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold_upper = _parse_threshold_upper(d.pop("threshold_upper", UNSET))

        asset_key = d.pop("asset_key", UNSET)

        _band_mapping = d.pop("band_mapping", UNSET)
        band_mapping: CreateAlertRuleInputBandMapping | Unset
        if isinstance(_band_mapping, Unset):
            band_mapping = UNSET
        else:
            band_mapping = CreateAlertRuleInputBandMapping.from_dict(_band_mapping)

        notification_channels = cast(list[str], d.pop("notification_channels", UNSET))

        cooldown_minutes = d.pop("cooldown_minutes", UNSET)

        create_alert_rule_input = cls(
            name=name,
            expression=expression,
            comparison=comparison,
            threshold=threshold,
            description=description,
            collection_id=collection_id,
            event_types=event_types,
            threshold_upper=threshold_upper,
            asset_key=asset_key,
            band_mapping=band_mapping,
            notification_channels=notification_channels,
            cooldown_minutes=cooldown_minutes,
        )

        create_alert_rule_input.additional_properties = d
        return create_alert_rule_input

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
