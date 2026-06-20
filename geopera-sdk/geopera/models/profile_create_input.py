from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_layer import ProfileLayer
from ..models.profile_type import ProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_create_input_config import ProfileCreateInputConfig


T = TypeVar("T", bound="ProfileCreateInput")


@_attrs_define
class ProfileCreateInput:
    """
    Attributes:
        name (str):
        type_ (ProfileType):
        config (ProfileCreateInputConfig): Render configuration.
        item_id (str):
        layer (ProfileLayer | Unset):
        is_default (bool | Unset):  Default: False.
        sort_order (int | Unset):  Default: 0.
        asset_key (None | str | Unset):
    """

    name: str
    type_: ProfileType
    config: ProfileCreateInputConfig
    item_id: str
    layer: ProfileLayer | Unset = UNSET
    is_default: bool | Unset = False
    sort_order: int | Unset = 0
    asset_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        config = self.config.to_dict()

        item_id = self.item_id

        layer: str | Unset = UNSET
        if not isinstance(self.layer, Unset):
            layer = self.layer.value

        is_default = self.is_default

        sort_order = self.sort_order

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "config": config,
                "item_id": item_id,
            }
        )
        if layer is not UNSET:
            field_dict["layer"] = layer
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_create_input_config import ProfileCreateInputConfig

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ProfileType(d.pop("type"))

        config = ProfileCreateInputConfig.from_dict(d.pop("config"))

        item_id = d.pop("item_id")

        _layer = d.pop("layer", UNSET)
        layer: ProfileLayer | Unset
        if isinstance(_layer, Unset):
            layer = UNSET
        else:
            layer = ProfileLayer(_layer)

        is_default = d.pop("is_default", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        profile_create_input = cls(
            name=name,
            type_=type_,
            config=config,
            item_id=item_id,
            layer=layer,
            is_default=is_default,
            sort_order=sort_order,
            asset_key=asset_key,
        )

        profile_create_input.additional_properties = d
        return profile_create_input

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
