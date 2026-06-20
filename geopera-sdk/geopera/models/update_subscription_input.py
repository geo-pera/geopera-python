from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscription_input_filter_config_type_0 import UpdateSubscriptionInputFilterConfigType0
    from ..models.update_subscription_input_headers_type_0 import UpdateSubscriptionInputHeadersType0


T = TypeVar("T", bound="UpdateSubscriptionInput")


@_attrs_define
class UpdateSubscriptionInput:
    """
    Attributes:
        subscription_id (str):
        endpoint_url (None | str | Unset):
        filter_config (None | Unset | UpdateSubscriptionInputFilterConfigType0):
        headers (None | Unset | UpdateSubscriptionInputHeadersType0):
        active (bool | None | Unset):
        description (None | str | Unset):
    """

    subscription_id: str
    endpoint_url: None | str | Unset = UNSET
    filter_config: None | Unset | UpdateSubscriptionInputFilterConfigType0 = UNSET
    headers: None | Unset | UpdateSubscriptionInputHeadersType0 = UNSET
    active: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_subscription_input_filter_config_type_0 import UpdateSubscriptionInputFilterConfigType0
        from ..models.update_subscription_input_headers_type_0 import UpdateSubscriptionInputHeadersType0

        subscription_id = self.subscription_id

        endpoint_url: None | str | Unset
        if isinstance(self.endpoint_url, Unset):
            endpoint_url = UNSET
        else:
            endpoint_url = self.endpoint_url

        filter_config: dict[str, Any] | None | Unset
        if isinstance(self.filter_config, Unset):
            filter_config = UNSET
        elif isinstance(self.filter_config, UpdateSubscriptionInputFilterConfigType0):
            filter_config = self.filter_config.to_dict()
        else:
            filter_config = self.filter_config

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, UpdateSubscriptionInputHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription_id": subscription_id,
            }
        )
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if filter_config is not UNSET:
            field_dict["filter_config"] = filter_config
        if headers is not UNSET:
            field_dict["headers"] = headers
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscription_input_filter_config_type_0 import UpdateSubscriptionInputFilterConfigType0
        from ..models.update_subscription_input_headers_type_0 import UpdateSubscriptionInputHeadersType0

        d = dict(src_dict)
        subscription_id = d.pop("subscription_id")

        def _parse_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_url = _parse_endpoint_url(d.pop("endpoint_url", UNSET))

        def _parse_filter_config(data: object) -> None | Unset | UpdateSubscriptionInputFilterConfigType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_config_type_0 = UpdateSubscriptionInputFilterConfigType0.from_dict(data)

                return filter_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateSubscriptionInputFilterConfigType0, data)

        filter_config = _parse_filter_config(d.pop("filter_config", UNSET))

        def _parse_headers(data: object) -> None | Unset | UpdateSubscriptionInputHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = UpdateSubscriptionInputHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateSubscriptionInputHeadersType0, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        update_subscription_input = cls(
            subscription_id=subscription_id,
            endpoint_url=endpoint_url,
            filter_config=filter_config,
            headers=headers,
            active=active,
            description=description,
        )

        update_subscription_input.additional_properties = d
        return update_subscription_input

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
