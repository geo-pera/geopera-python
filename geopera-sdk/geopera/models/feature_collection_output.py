from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureCollectionOutput")


@_attrs_define
class FeatureCollectionOutput:
    """
    Attributes:
        type_ (str | Unset):  Default: 'FeatureCollection'.
        features (list[Any] | Unset):
        number_matched (int | Unset):  Default: 0.
    """

    type_: str | Unset = "FeatureCollection"
    features: list[Any] | Unset = UNSET
    number_matched: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        features: list[Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        number_matched = self.number_matched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if features is not UNSET:
            field_dict["features"] = features
        if number_matched is not UNSET:
            field_dict["numberMatched"] = number_matched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        features = cast(list[Any], d.pop("features", UNSET))

        number_matched = d.pop("numberMatched", UNSET)

        feature_collection_output = cls(
            type_=type_,
            features=features,
            number_matched=number_matched,
        )

        feature_collection_output.additional_properties = d
        return feature_collection_output

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
