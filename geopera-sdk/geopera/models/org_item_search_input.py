from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_type import ItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_item_search_input_query_type_0 import OrgItemSearchInputQueryType0
    from ..models.org_item_search_input_sortby_type_0_item import OrgItemSearchInputSortbyType0Item


T = TypeVar("T", bound="OrgItemSearchInput")


@_attrs_define
class OrgItemSearchInput:
    """
    Attributes:
        bbox (list[float] | None | Unset):
        datetime_ (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        collections (list[str] | None | Unset):
        type_ (ItemType | None | Unset):
        query (None | OrgItemSearchInputQueryType0 | Unset):
        sortby (list[OrgItemSearchInputSortbyType0Item] | None | Unset):
        format_ (None | str | Unset):
        base_url (None | str | Unset):
    """

    bbox: list[float] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    limit: int | Unset = 100
    offset: int | Unset = 0
    collections: list[str] | None | Unset = UNSET
    type_: ItemType | None | Unset = UNSET
    query: None | OrgItemSearchInputQueryType0 | Unset = UNSET
    sortby: list[OrgItemSearchInputSortbyType0Item] | None | Unset = UNSET
    format_: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.org_item_search_input_query_type_0 import OrgItemSearchInputQueryType0

        bbox: list[float] | None | Unset
        if isinstance(self.bbox, Unset):
            bbox = UNSET
        elif isinstance(self.bbox, list):
            bbox = self.bbox

        else:
            bbox = self.bbox

        datetime_: None | str | Unset
        if isinstance(self.datetime_, Unset):
            datetime_ = UNSET
        else:
            datetime_ = self.datetime_

        limit = self.limit

        offset = self.offset

        collections: list[str] | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = self.collections

        else:
            collections = self.collections

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ItemType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        query: dict[str, Any] | None | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, OrgItemSearchInputQueryType0):
            query = self.query.to_dict()
        else:
            query = self.query

        sortby: list[dict[str, Any]] | None | Unset
        if isinstance(self.sortby, Unset):
            sortby = UNSET
        elif isinstance(self.sortby, list):
            sortby = []
            for sortby_type_0_item_data in self.sortby:
                sortby_type_0_item = sortby_type_0_item_data.to_dict()
                sortby.append(sortby_type_0_item)

        else:
            sortby = self.sortby

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if collections is not UNSET:
            field_dict["collections"] = collections
        if type_ is not UNSET:
            field_dict["type"] = type_
        if query is not UNSET:
            field_dict["query"] = query
        if sortby is not UNSET:
            field_dict["sortby"] = sortby
        if format_ is not UNSET:
            field_dict["format"] = format_
        if base_url is not UNSET:
            field_dict["base_url"] = base_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_item_search_input_query_type_0 import OrgItemSearchInputQueryType0
        from ..models.org_item_search_input_sortby_type_0_item import OrgItemSearchInputSortbyType0Item

        d = dict(src_dict)

        def _parse_bbox(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bbox_type_0 = cast(list[float], data)

                return bbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        bbox = _parse_bbox(d.pop("bbox", UNSET))

        def _parse_datetime_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datetime_ = _parse_datetime_(d.pop("datetime", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        def _parse_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collections_type_0 = cast(list[str], data)

                return collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collections = _parse_collections(d.pop("collections", UNSET))

        def _parse_type_(data: object) -> ItemType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ItemType(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_query(data: object) -> None | OrgItemSearchInputQueryType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_type_0 = OrgItemSearchInputQueryType0.from_dict(data)

                return query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrgItemSearchInputQueryType0 | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_sortby(data: object) -> list[OrgItemSearchInputSortbyType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sortby_type_0 = []
                _sortby_type_0 = data
                for sortby_type_0_item_data in _sortby_type_0:
                    sortby_type_0_item = OrgItemSearchInputSortbyType0Item.from_dict(sortby_type_0_item_data)

                    sortby_type_0.append(sortby_type_0_item)

                return sortby_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrgItemSearchInputSortbyType0Item] | None | Unset, data)

        sortby = _parse_sortby(d.pop("sortby", UNSET))

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        org_item_search_input = cls(
            bbox=bbox,
            datetime_=datetime_,
            limit=limit,
            offset=offset,
            collections=collections,
            type_=type_,
            query=query,
            sortby=sortby,
            format_=format_,
            base_url=base_url,
        )

        org_item_search_input.additional_properties = d
        return org_item_search_input

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
