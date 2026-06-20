from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemWmtsCapabilitiesInput")


@_attrs_define
class ItemWmtsCapabilitiesInput:
    """
    Attributes:
        item_id (str):
        base_url (str):
        key (str | Unset):  Default: ''.
        profile (None | str | Unset):
    """

    item_id: str
    base_url: str
    key: str | Unset = ""
    profile: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        base_url = self.base_url

        key = self.key

        profile: None | str | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "base_url": base_url,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        base_url = d.pop("base_url")

        key = d.pop("key", UNSET)

        def _parse_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        item_wmts_capabilities_input = cls(
            item_id=item_id,
            base_url=base_url,
            key=key,
            profile=profile,
        )

        item_wmts_capabilities_input.additional_properties = d
        return item_wmts_capabilities_input

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
