from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_subscription_input_filter_config import CreateSubscriptionInputFilterConfig
    from ..models.create_subscription_input_headers import CreateSubscriptionInputHeaders


T = TypeVar("T", bound="CreateSubscriptionInput")


@_attrs_define
class CreateSubscriptionInput:
    """
    Attributes:
        event_type (str):
        endpoint_url (str):
        filter_config (CreateSubscriptionInputFilterConfig | Unset):
        headers (CreateSubscriptionInputHeaders | Unset):
        description (None | str | Unset):
    """

    event_type: str
    endpoint_url: str
    filter_config: CreateSubscriptionInputFilterConfig | Unset = UNSET
    headers: CreateSubscriptionInputHeaders | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        endpoint_url = self.endpoint_url

        filter_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_config, Unset):
            filter_config = self.filter_config.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "endpoint_url": endpoint_url,
            }
        )
        if filter_config is not UNSET:
            field_dict["filter_config"] = filter_config
        if headers is not UNSET:
            field_dict["headers"] = headers
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscription_input_filter_config import CreateSubscriptionInputFilterConfig
        from ..models.create_subscription_input_headers import CreateSubscriptionInputHeaders

        d = dict(src_dict)
        event_type = d.pop("event_type")

        endpoint_url = d.pop("endpoint_url")

        _filter_config = d.pop("filter_config", UNSET)
        filter_config: CreateSubscriptionInputFilterConfig | Unset
        if isinstance(_filter_config, Unset):
            filter_config = UNSET
        else:
            filter_config = CreateSubscriptionInputFilterConfig.from_dict(_filter_config)

        _headers = d.pop("headers", UNSET)
        headers: CreateSubscriptionInputHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateSubscriptionInputHeaders.from_dict(_headers)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        create_subscription_input = cls(
            event_type=event_type,
            endpoint_url=endpoint_url,
            filter_config=filter_config,
            headers=headers,
            description=description,
        )

        create_subscription_input.additional_properties = d
        return create_subscription_input

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
