from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection_dto import CollectionDTO


T = TypeVar("T", bound="SourceDTO")


@_attrs_define
class SourceDTO:
    """
    Attributes:
        id (str):
        title (str):
        description (str):
        access_model (str):
        scope (str):
        countries (list[str]):
        attribution (str):
        license_ (str):
        collections (list[CollectionDTO]):
    """

    id: str
    title: str
    description: str
    access_model: str
    scope: str
    countries: list[str]
    attribution: str
    license_: str
    collections: list[CollectionDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        access_model = self.access_model

        scope = self.scope

        countries = self.countries

        attribution = self.attribution

        license_ = self.license_

        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "access_model": access_model,
                "scope": scope,
                "countries": countries,
                "attribution": attribution,
                "license": license_,
                "collections": collections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_dto import CollectionDTO

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        access_model = d.pop("access_model")

        scope = d.pop("scope")

        countries = cast(list[str], d.pop("countries"))

        attribution = d.pop("attribution")

        license_ = d.pop("license")

        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = CollectionDTO.from_dict(collections_item_data)

            collections.append(collections_item)

        source_dto = cls(
            id=id,
            title=title,
            description=description,
            access_model=access_model,
            scope=scope,
            countries=countries,
            attribution=attribution,
            license_=license_,
            collections=collections,
        )

        source_dto.additional_properties = d
        return source_dto

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
