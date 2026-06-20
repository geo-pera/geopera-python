from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataProductsListInput")


@_attrs_define
class DataProductsListInput:
    """
    Attributes:
        data_product_id (None | str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 10.
        sort (None | str | Unset):  Default: 'createdAt,desc'.
    """

    data_product_id: None | str | Unset = UNSET
    page: int | Unset = 0
    size: int | Unset = 10
    sort: None | str | Unset = "createdAt,desc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_product_id: None | str | Unset
        if isinstance(self.data_product_id, Unset):
            data_product_id = UNSET
        else:
            data_product_id = self.data_product_id

        page = self.page

        size = self.size

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        else:
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_product_id is not UNSET:
            field_dict["dataProductId"] = data_product_id
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_data_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_product_id = _parse_data_product_id(d.pop("dataProductId", UNSET))

        page = d.pop("page", UNSET)

        size = d.pop("size", UNSET)

        def _parse_sort(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        data_products_list_input = cls(
            data_product_id=data_product_id,
            page=page,
            size=size,
            sort=sort,
        )

        data_products_list_input.additional_properties = d
        return data_products_list_input

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
