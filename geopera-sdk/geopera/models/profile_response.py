from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_layer import ProfileLayer
from ..models.profile_type import ProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_response_config import ProfileResponseConfig


T = TypeVar("T", bound="ProfileResponse")


@_attrs_define
class ProfileResponse:
    """Visualization profile as returned from the API.

    Attributes:
        id (str):
        item_id (str):
        name (str):
        layer (ProfileLayer):
        type_ (ProfileType):
        config (ProfileResponseConfig):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_default (bool | Unset):  Default: False.
        sort_order (int | Unset):  Default: 0.
        asset_key (None | str | Unset):
        version (int | Unset):  Default: 1.
        created_by (None | str | Unset):
    """

    id: str
    item_id: str
    name: str
    layer: ProfileLayer
    type_: ProfileType
    config: ProfileResponseConfig
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_default: bool | Unset = False
    sort_order: int | Unset = 0
    asset_key: None | str | Unset = UNSET
    version: int | Unset = 1
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_id = self.item_id

        name = self.name

        layer = self.layer.value

        type_ = self.type_.value

        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_default = self.is_default

        sort_order = self.sort_order

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        version = self.version

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "item_id": item_id,
                "name": name,
                "layer": layer,
                "type": type_,
                "config": config,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key
        if version is not UNSET:
            field_dict["version"] = version
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_response_config import ProfileResponseConfig

        d = dict(src_dict)
        id = d.pop("id")

        item_id = d.pop("item_id")

        name = d.pop("name")

        layer = ProfileLayer(d.pop("layer"))

        type_ = ProfileType(d.pop("type"))

        config = ProfileResponseConfig.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        is_default = d.pop("is_default", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        version = d.pop("version", UNSET)

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        profile_response = cls(
            id=id,
            item_id=item_id,
            name=name,
            layer=layer,
            type_=type_,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
            is_default=is_default,
            sort_order=sort_order,
            asset_key=asset_key,
            version=version,
            created_by=created_by,
        )

        profile_response.additional_properties = d
        return profile_response

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
