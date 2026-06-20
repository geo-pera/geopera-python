from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_type import ProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_update_input_config_type_0 import ProfileUpdateInputConfigType0


T = TypeVar("T", bound="ProfileUpdateInput")


@_attrs_define
class ProfileUpdateInput:
    """
    Attributes:
        item_id (str):
        profile_id (str):
        name (None | str | Unset):
        type_ (None | ProfileType | Unset):
        is_default (bool | None | Unset):
        sort_order (int | None | Unset):
        config (None | ProfileUpdateInputConfigType0 | Unset):
        asset_key (None | str | Unset):
    """

    item_id: str
    profile_id: str
    name: None | str | Unset = UNSET
    type_: None | ProfileType | Unset = UNSET
    is_default: bool | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    config: None | ProfileUpdateInputConfigType0 | Unset = UNSET
    asset_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_update_input_config_type_0 import ProfileUpdateInputConfigType0

        item_id = self.item_id

        profile_id = self.profile_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ProfileType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ProfileUpdateInputConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "profile_id": profile_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if config is not UNSET:
            field_dict["config"] = config
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_update_input_config_type_0 import ProfileUpdateInputConfigType0

        d = dict(src_dict)
        item_id = d.pop("item_id")

        profile_id = d.pop("profile_id")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> None | ProfileType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ProfileType(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileType | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        def _parse_config(data: object) -> None | ProfileUpdateInputConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ProfileUpdateInputConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileUpdateInputConfigType0 | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        profile_update_input = cls(
            item_id=item_id,
            profile_id=profile_id,
            name=name,
            type_=type_,
            is_default=is_default,
            sort_order=sort_order,
            config=config,
            asset_key=asset_key,
        )

        profile_update_input.additional_properties = d
        return profile_update_input

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
