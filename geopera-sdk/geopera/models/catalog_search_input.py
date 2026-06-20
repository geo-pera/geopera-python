from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_search_input_intersects_type_0 import CatalogSearchInputIntersectsType0
    from ..models.catalog_search_input_query_type_0 import CatalogSearchInputQueryType0


T = TypeVar("T", bound="CatalogSearchInput")


@_attrs_define
class CatalogSearchInput:
    """
    Attributes:
        host_name (str):
        collections (list[str] | None | Unset):
        ids (list[str] | None | Unset):
        datetime_ (None | str | Unset):
        limit (int | Unset):  Default: 100.
        query (CatalogSearchInputQueryType0 | None | Unset):
        bbox (list[float] | None | Unset):
        intersects (CatalogSearchInputIntersectsType0 | None | Unset):
        full_catalog (bool | None | Unset):
        next_ (None | str | Unset):
    """

    host_name: str
    collections: list[str] | None | Unset = UNSET
    ids: list[str] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    limit: int | Unset = 100
    query: CatalogSearchInputQueryType0 | None | Unset = UNSET
    bbox: list[float] | None | Unset = UNSET
    intersects: CatalogSearchInputIntersectsType0 | None | Unset = UNSET
    full_catalog: bool | None | Unset = UNSET
    next_: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_search_input_intersects_type_0 import CatalogSearchInputIntersectsType0
        from ..models.catalog_search_input_query_type_0 import CatalogSearchInputQueryType0

        host_name = self.host_name

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

        limit = self.limit

        query: dict[str, Any] | None | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, CatalogSearchInputQueryType0):
            query = self.query.to_dict()
        else:
            query = self.query

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
        elif isinstance(self.intersects, CatalogSearchInputIntersectsType0):
            intersects = self.intersects.to_dict()
        else:
            intersects = self.intersects

        full_catalog: bool | None | Unset
        if isinstance(self.full_catalog, Unset):
            full_catalog = UNSET
        else:
            full_catalog = self.full_catalog

        next_: None | str | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_name": host_name,
            }
        )
        if collections is not UNSET:
            field_dict["collections"] = collections
        if ids is not UNSET:
            field_dict["ids"] = ids
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if intersects is not UNSET:
            field_dict["intersects"] = intersects
        if full_catalog is not UNSET:
            field_dict["full_catalog"] = full_catalog
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_search_input_intersects_type_0 import CatalogSearchInputIntersectsType0
        from ..models.catalog_search_input_query_type_0 import CatalogSearchInputQueryType0

        d = dict(src_dict)
        host_name = d.pop("host_name")

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

        limit = d.pop("limit", UNSET)

        def _parse_query(data: object) -> CatalogSearchInputQueryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_type_0 = CatalogSearchInputQueryType0.from_dict(data)

                return query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogSearchInputQueryType0 | None | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

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

        def _parse_intersects(data: object) -> CatalogSearchInputIntersectsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intersects_type_0 = CatalogSearchInputIntersectsType0.from_dict(data)

                return intersects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogSearchInputIntersectsType0 | None | Unset, data)

        intersects = _parse_intersects(d.pop("intersects", UNSET))

        def _parse_full_catalog(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        full_catalog = _parse_full_catalog(d.pop("full_catalog", UNSET))

        def _parse_next_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        catalog_search_input = cls(
            host_name=host_name,
            collections=collections,
            ids=ids,
            datetime_=datetime_,
            limit=limit,
            query=query,
            bbox=bbox,
            intersects=intersects,
            full_catalog=full_catalog,
            next_=next_,
        )

        catalog_search_input.additional_properties = d
        return catalog_search_input

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
