from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_result_summary import SourceResultSummary


T = TypeVar("T", bound="FederatedSearchOutput")


@_attrs_define
class FederatedSearchOutput:
    """
    Attributes:
        type_ (str | Unset):  Default: 'FeatureCollection'.
        features (list[Any] | Unset):
        number_returned (int | Unset):  Default: 0.
        sources (list[SourceResultSummary] | Unset):
    """

    type_: str | Unset = "FeatureCollection"
    features: list[Any] | Unset = UNSET
    number_returned: int | Unset = 0
    sources: list[SourceResultSummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        features: list[Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        number_returned = self.number_returned

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if features is not UNSET:
            field_dict["features"] = features
        if number_returned is not UNSET:
            field_dict["numberReturned"] = number_returned
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_result_summary import SourceResultSummary

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        features = cast(list[Any], d.pop("features", UNSET))

        number_returned = d.pop("numberReturned", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[SourceResultSummary] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = SourceResultSummary.from_dict(sources_item_data)

                sources.append(sources_item)

        federated_search_output = cls(
            type_=type_,
            features=features,
            number_returned=number_returned,
            sources=sources,
        )

        federated_search_output.additional_properties = d
        return federated_search_output

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
