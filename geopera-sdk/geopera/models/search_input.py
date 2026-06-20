from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_input_filter_type_0 import SearchInputFilterType0
    from ..models.search_input_intersects_type_0 import SearchInputIntersectsType0
    from ..models.sort_clause import SortClause


T = TypeVar("T", bound="SearchInput")


@_attrs_define
class SearchInput:
    """Subset of provider's `POST /assets/stac/search` body schema, plus base_url.

    Attributes:
        base_url (str | Unset):  Default: ''.
        collections (list[str] | None | Unset):
        ids (list[str] | None | Unset):
        datetime_ (None | str | Unset):
        sortby (list[SortClause] | None | Unset):
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        filter_ (None | SearchInputFilterType0 | Unset):
        filter_lang (None | str | Unset):  Default: 'cql2-json'.
        bbox (list[float] | None | Unset):
        intersects (None | SearchInputIntersectsType0 | Unset):
    """

    base_url: str | Unset = ""
    collections: list[str] | None | Unset = UNSET
    ids: list[str] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    sortby: list[SortClause] | None | Unset = UNSET
    limit: int | Unset = 10
    page: int | Unset = 0
    filter_: None | SearchInputFilterType0 | Unset = UNSET
    filter_lang: None | str | Unset = "cql2-json"
    bbox: list[float] | None | Unset = UNSET
    intersects: None | SearchInputIntersectsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_input_filter_type_0 import SearchInputFilterType0
        from ..models.search_input_intersects_type_0 import SearchInputIntersectsType0

        base_url = self.base_url

        collections: list[str] | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = self.collections

        else:
            collections = self.collections

        ids: list[str] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = self.ids

        else:
            ids = self.ids

        datetime_: None | str | Unset
        if isinstance(self.datetime_, Unset):
            datetime_ = UNSET
        else:
            datetime_ = self.datetime_

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

        limit = self.limit

        page = self.page

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, SearchInputFilterType0):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        filter_lang: None | str | Unset
        if isinstance(self.filter_lang, Unset):
            filter_lang = UNSET
        else:
            filter_lang = self.filter_lang

        bbox: list[float] | None | Unset
        if isinstance(self.bbox, Unset):
            bbox = UNSET
        elif isinstance(self.bbox, list):
            bbox = self.bbox

        else:
            bbox = self.bbox

        intersects: dict[str, Any] | None | Unset
        if isinstance(self.intersects, Unset):
            intersects = UNSET
        elif isinstance(self.intersects, SearchInputIntersectsType0):
            intersects = self.intersects.to_dict()
        else:
            intersects = self.intersects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if collections is not UNSET:
            field_dict["collections"] = collections
        if ids is not UNSET:
            field_dict["ids"] = ids
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if sortby is not UNSET:
            field_dict["sortby"] = sortby
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_lang is not UNSET:
            field_dict["filter-lang"] = filter_lang
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if intersects is not UNSET:
            field_dict["intersects"] = intersects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_input_filter_type_0 import SearchInputFilterType0
        from ..models.search_input_intersects_type_0 import SearchInputIntersectsType0
        from ..models.sort_clause import SortClause

        d = dict(src_dict)
        base_url = d.pop("base_url", UNSET)

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

        def _parse_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(list[str], data)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))

        def _parse_datetime_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datetime_ = _parse_datetime_(d.pop("datetime", UNSET))

        def _parse_sortby(data: object) -> list[SortClause] | None | Unset:
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
                    sortby_type_0_item = SortClause.from_dict(sortby_type_0_item_data)

                    sortby_type_0.append(sortby_type_0_item)

                return sortby_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SortClause] | None | Unset, data)

        sortby = _parse_sortby(d.pop("sortby", UNSET))

        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        def _parse_filter_(data: object) -> None | SearchInputFilterType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_0 = SearchInputFilterType0.from_dict(data)

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchInputFilterType0 | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_filter_lang(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_lang = _parse_filter_lang(d.pop("filter-lang", UNSET))

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

        def _parse_intersects(data: object) -> None | SearchInputIntersectsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intersects_type_0 = SearchInputIntersectsType0.from_dict(data)

                return intersects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchInputIntersectsType0 | Unset, data)

        intersects = _parse_intersects(d.pop("intersects", UNSET))

        search_input = cls(
            base_url=base_url,
            collections=collections,
            ids=ids,
            datetime_=datetime_,
            sortby=sortby,
            limit=limit,
            page=page,
            filter_=filter_,
            filter_lang=filter_lang,
            bbox=bbox,
            intersects=intersects,
        )

        search_input.additional_properties = d
        return search_input

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
