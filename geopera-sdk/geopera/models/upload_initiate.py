from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadInitiate")


@_attrs_define
class UploadInitiate:
    """Input for starting an upload session.

    Attributes:
        project_id (str):
        transfer_method (str | Unset):  Default: 'browser'.
        file_count (int | Unset):  Default: 1.
        total_bytes (int | Unset):  Default: 0.
        target_collection_id (None | str | Unset):
        target_item_id (None | str | Unset):
        asset_key (None | str | Unset):
        is_categorical (bool | Unset):  Default: False.
    """

    project_id: str
    transfer_method: str | Unset = "browser"
    file_count: int | Unset = 1
    total_bytes: int | Unset = 0
    target_collection_id: None | str | Unset = UNSET
    target_item_id: None | str | Unset = UNSET
    asset_key: None | str | Unset = UNSET
    is_categorical: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        transfer_method = self.transfer_method

        file_count = self.file_count

        total_bytes = self.total_bytes

        target_collection_id: None | str | Unset
        if isinstance(self.target_collection_id, Unset):
            target_collection_id = UNSET
        else:
            target_collection_id = self.target_collection_id

        target_item_id: None | str | Unset
        if isinstance(self.target_item_id, Unset):
            target_item_id = UNSET
        else:
            target_item_id = self.target_item_id

        asset_key: None | str | Unset
        if isinstance(self.asset_key, Unset):
            asset_key = UNSET
        else:
            asset_key = self.asset_key

        is_categorical = self.is_categorical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if transfer_method is not UNSET:
            field_dict["transfer_method"] = transfer_method
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if total_bytes is not UNSET:
            field_dict["total_bytes"] = total_bytes
        if target_collection_id is not UNSET:
            field_dict["target_collection_id"] = target_collection_id
        if target_item_id is not UNSET:
            field_dict["target_item_id"] = target_item_id
        if asset_key is not UNSET:
            field_dict["asset_key"] = asset_key
        if is_categorical is not UNSET:
            field_dict["is_categorical"] = is_categorical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        transfer_method = d.pop("transfer_method", UNSET)

        file_count = d.pop("file_count", UNSET)

        total_bytes = d.pop("total_bytes", UNSET)

        def _parse_target_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_collection_id = _parse_target_collection_id(d.pop("target_collection_id", UNSET))

        def _parse_target_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_item_id = _parse_target_item_id(d.pop("target_item_id", UNSET))

        def _parse_asset_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_key = _parse_asset_key(d.pop("asset_key", UNSET))

        is_categorical = d.pop("is_categorical", UNSET)

        upload_initiate = cls(
            project_id=project_id,
            transfer_method=transfer_method,
            file_count=file_count,
            total_bytes=total_bytes,
            target_collection_id=target_collection_id,
            target_item_id=target_item_id,
            asset_key=asset_key,
            is_categorical=is_categorical,
        )

        upload_initiate.additional_properties = d
        return upload_initiate

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
