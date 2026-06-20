from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_rule_input_band_mapping_type_0 import UpdateAlertRuleInputBandMappingType0


T = TypeVar("T", bound="UpdateAlertRuleInput")


@_attrs_define
class UpdateAlertRuleInput:
    """
    Attributes:
        rule_id (str):
        name (None | str | Unset):
        description (None | str | Unset):
        collection_id (None | str | Unset):
        event_types (list[str] | None | Unset):
        expression (None | str | Unset):
        comparison (None | str | Unset):
        threshold (float | None | Unset):
        threshold_upper (float | None | Unset):
        asset_key (None | str | Unset):
        band_mapping (None | Unset | UpdateAlertRuleInputBandMappingType0):
        notification_channels (list[str] | None | Unset):
        active (bool | None | Unset):
        cooldown_minutes (int | None | Unset):
    """

    rule_id: str
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    event_types: list[str] | None | Unset = UNSET
    expression: None | str | Unset = UNSET
    comparison: None | str | Unset = UNSET
    threshold: float | None | Unset = UNSET
    threshold_upper: float | None | Unset = UNSET
    asset_key: None | str | Unset = UNSET
    band_mapping: None | Unset | UpdateAlertRuleInputBandMappingType0 = UNSET
    notification_channels: list[str] | None | Unset = UNSET
    active: bool | None | Unset = UNSET
    cooldown_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_alert_rule_input_band_mapping_type_0 import UpdateAlertRuleInputBandMappingType0

        rule_id = self.rule_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        comparison: None | str | Unset
        if isinstance(self.comparison, Unset):
            comparison = UNSET
        else:
            comparison = self.comparison

        threshold: float | None | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

        threshold_upper: float | None | Unset
        if isinstance(self.threshold_upper, Unset):
            threshold_upper = UNSET
        else:
            threshold_upper = self.threshold_upper

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        band_mapping: dict[str, Any] | None | Unset
        if isinstance(self.band_mapping, Unset):
            band_mapping = UNSET
        elif isinstance(self.band_mapping, UpdateAlertRuleInputBandMappingType0):
            band_mapping = self.band_mapping.to_dict()
        else:
            band_mapping = self.band_mapping

        notification_channels: list[str] | None | Unset
        if isinstance(self.notification_channels, Unset):
            notification_channels = UNSET
        elif isinstance(self.notification_channels, list):
            notification_channels = self.notification_channels

        else:
            notification_channels = self.notification_channels

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        cooldown_minutes: int | None | Unset
        if isinstance(self.cooldown_minutes, Unset):
            cooldown_minutes = UNSET
        else:
            cooldown_minutes = self.cooldown_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_id": rule_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if expression is not UNSET:
            field_dict["expression"] = expression
        if comparison is not UNSET:
            field_dict["comparison"] = comparison
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_upper is not UNSET:
            field_dict["threshold_upper"] = threshold_upper
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key
        if band_mapping is not UNSET:
            field_dict["band_mapping"] = band_mapping
        if notification_channels is not UNSET:
            field_dict["notification_channels"] = notification_channels
        if active is not UNSET:
            field_dict["active"] = active
        if cooldown_minutes is not UNSET:
            field_dict["cooldown_minutes"] = cooldown_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_rule_input_band_mapping_type_0 import UpdateAlertRuleInputBandMappingType0

        d = dict(src_dict)
        rule_id = d.pop("rule_id")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("event_types", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_comparison(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comparison = _parse_comparison(d.pop("comparison", UNSET))

        def _parse_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        def _parse_threshold_upper(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold_upper = _parse_threshold_upper(d.pop("threshold_upper", UNSET))

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        def _parse_band_mapping(data: object) -> None | Unset | UpdateAlertRuleInputBandMappingType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                band_mapping_type_0 = UpdateAlertRuleInputBandMappingType0.from_dict(data)

                return band_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAlertRuleInputBandMappingType0, data)

        band_mapping = _parse_band_mapping(d.pop("band_mapping", UNSET))

        def _parse_notification_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_channels_type_0 = cast(list[str], data)

                return notification_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notification_channels = _parse_notification_channels(d.pop("notification_channels", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_cooldown_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cooldown_minutes = _parse_cooldown_minutes(d.pop("cooldown_minutes", UNSET))

        update_alert_rule_input = cls(
            rule_id=rule_id,
            name=name,
            description=description,
            collection_id=collection_id,
            event_types=event_types,
            expression=expression,
            comparison=comparison,
            threshold=threshold,
            threshold_upper=threshold_upper,
            asset_key=asset_key,
            band_mapping=band_mapping,
            notification_channels=notification_channels,
            active=active,
            cooldown_minutes=cooldown_minutes,
        )

        update_alert_rule_input.additional_properties = d
        return update_alert_rule_input

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
