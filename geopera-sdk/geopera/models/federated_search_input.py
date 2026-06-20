from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.federated_search_input_intersects_type_0 import FederatedSearchInputIntersectsType0
    from ..models.federated_search_input_query_type_0 import FederatedSearchInputQueryType0


T = TypeVar("T", bound="FederatedSearchInput")


@_attrs_define
class FederatedSearchInput:
    """
    Attributes:
        collections (list[str] | None | Unset):
        ids (list[str] | None | Unset):
        datetime_ (None | str | Unset):
        limit (int | Unset):  Default: 100.
        query (FederatedSearchInputQueryType0 | None | Unset):
        bbox (list[float] | None | Unset):
        intersects (FederatedSearchInputIntersectsType0 | None | Unset):
        full_catalog (bool | None | Unset):
        source_ids (list[str] | None | Unset):
        data_types (list[str] | None | Unset):
    """

    collections: list[str] | None | Unset = UNSET
    ids: list[str] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    limit: int | Unset = 100
    query: FederatedSearchInputQueryType0 | None | Unset = UNSET
    bbox: list[float] | None | Unset = UNSET
    intersects: FederatedSearchInputIntersectsType0 | None | Unset = UNSET
    full_catalog: bool | None | Unset = UNSET
    source_ids: list[str] | None | Unset = UNSET
    data_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.federated_search_input_intersects_type_0 import FederatedSearchInputIntersectsType0
        from ..models.federated_search_input_query_type_0 import FederatedSearchInputQueryType0

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
        elif isinstance(self.query, FederatedSearchInputQueryType0):
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
        elif isinstance(self.intersects, FederatedSearchInputIntersectsType0):
            intersects = self.intersects.to_dict()
        else:
            intersects = self.intersects

        full_catalog: bool | None | Unset
        if isinstance(self.full_catalog, Unset):
            full_catalog = UNSET
        else:
            full_catalog = self.full_catalog

        source_ids: list[str] | None | Unset
        if isinstance(self.source_ids, Unset):
            source_ids = UNSET
        elif isinstance(self.source_ids, list):
            source_ids = self.source_ids

        else:
            source_ids = self.source_ids

        data_types: list[str] | None | Unset
        if isinstance(self.data_types, Unset):
            data_types = UNSET
        elif isinstance(self.data_types, list):
            data_types = self.data_types

        else:
            data_types = self.data_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids
        if data_types is not UNSET:
            field_dict["data_types"] = data_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.federated_search_input_intersects_type_0 import FederatedSearchInputIntersectsType0
        from ..models.federated_search_input_query_type_0 import FederatedSearchInputQueryType0

        d = dict(src_dict)

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

        def _parse_query(data: object) -> FederatedSearchInputQueryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_type_0 = FederatedSearchInputQueryType0.from_dict(data)

                return query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FederatedSearchInputQueryType0 | None | Unset, data)

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

        def _parse_intersects(data: object) -> FederatedSearchInputIntersectsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intersects_type_0 = FederatedSearchInputIntersectsType0.from_dict(data)

                return intersects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FederatedSearchInputIntersectsType0 | None | Unset, data)

        intersects = _parse_intersects(d.pop("intersects", UNSET))

        def _parse_full_catalog(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        full_catalog = _parse_full_catalog(d.pop("full_catalog", UNSET))

        def _parse_source_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_ids_type_0 = cast(list[str], data)

                return source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_ids = _parse_source_ids(d.pop("source_ids", UNSET))

        def _parse_data_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_types_type_0 = cast(list[str], data)

                return data_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        data_types = _parse_data_types(d.pop("data_types", UNSET))

        federated_search_input = cls(
            collections=collections,
            ids=ids,
            datetime_=datetime_,
            limit=limit,
            query=query,
            bbox=bbox,
            intersects=intersects,
            full_catalog=full_catalog,
            source_ids=source_ids,
            data_types=data_types,
        )

        federated_search_input.additional_properties = d
        return federated_search_input

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
