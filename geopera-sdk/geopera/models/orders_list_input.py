from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrdersListInput")


@_attrs_define
class OrdersListInput:
    """
    Attributes:
        workspace_id (None | str | Unset):
        type_ (None | str | Unset):
        status (None | str | Unset):
        sub_status (None | str | Unset):
        display_name (None | str | Unset):
        data_product_ids (None | str | Unset):
        order_ids (None | str | Unset):
        tags (None | str | Unset):
        size (int | Unset):  Default: 20.
        page (int | Unset):  Default: 0.
        sort (str | Unset):  Default: 'createdAt,desc'.
    """

    workspace_id: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    sub_status: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    data_product_ids: None | str | Unset = UNSET
    order_ids: None | str | Unset = UNSET
    tags: None | str | Unset = UNSET
    size: int | Unset = 20
    page: int | Unset = 0
    sort: str | Unset = "createdAt,desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        sub_status: None | str | Unset
        if isinstance(self.sub_status, Unset):
            sub_status = UNSET
        else:
            sub_status = self.sub_status

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        data_product_ids: None | str | Unset
        if isinstance(self.data_product_ids, Unset):
            data_product_ids = UNSET
        else:
            data_product_ids = self.data_product_ids

        order_ids: None | str | Unset
        if isinstance(self.order_ids, Unset):
            order_ids = UNSET
        else:
            order_ids = self.order_ids

        tags: None | str | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        else:
            tags = self.tags

        size = self.size

        page = self.page

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if sub_status is not UNSET:
            field_dict["subStatus"] = sub_status
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if data_product_ids is not UNSET:
            field_dict["dataProductIds"] = data_product_ids
        if order_ids is not UNSET:
            field_dict["orderIds"] = order_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if size is not UNSET:
            field_dict["size"] = size
        if page is not UNSET:
            field_dict["page"] = page
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_id = _parse_workspace_id(d.pop("workspaceId", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_sub_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_status = _parse_sub_status(d.pop("subStatus", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_data_product_ids(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_product_ids = _parse_data_product_ids(d.pop("dataProductIds", UNSET))

        def _parse_order_ids(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_ids = _parse_order_ids(d.pop("orderIds", UNSET))

        def _parse_tags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        size = d.pop("size", UNSET)

        page = d.pop("page", UNSET)

        sort = d.pop("sort", UNSET)

        orders_list_input = cls(
            workspace_id=workspace_id,
            type_=type_,
            status=status,
            sub_status=sub_status,
            display_name=display_name,
            data_product_ids=data_product_ids,
            order_ids=order_ids,
            tags=tags,
            size=size,
            page=page,
            sort=sort,
        )

        orders_list_input.additional_properties = d
        return orders_list_input

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
