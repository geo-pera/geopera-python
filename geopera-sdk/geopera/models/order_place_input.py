from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_place_input_featurecollection import OrderPlaceInputFeaturecollection
    from ..models.order_place_input_params import OrderPlaceInputParams


T = TypeVar("T", bound="OrderPlaceInput")


@_attrs_define
class OrderPlaceInput:
    """
    Attributes:
        workspace_id (str):
        data_product (str):
        display_name (str | Unset):  Default: ''.
        params (OrderPlaceInputParams | Unset):
        feature_collection (OrderPlaceInputFeaturecollection | Unset):
        tags (list[str] | None | Unset):
    """

    workspace_id: str
    data_product: str
    display_name: str | Unset = ""
    params: OrderPlaceInputParams | Unset = UNSET
    feature_collection: OrderPlaceInputFeaturecollection | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        data_product = self.data_product

        display_name = self.display_name

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        feature_collection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_collection, Unset):
            feature_collection = self.feature_collection.to_dict()

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "dataProduct": data_product,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if params is not UNSET:
            field_dict["params"] = params
        if feature_collection is not UNSET:
            field_dict["featureCollection"] = feature_collection
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_place_input_featurecollection import OrderPlaceInputFeaturecollection
        from ..models.order_place_input_params import OrderPlaceInputParams

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        data_product = d.pop("dataProduct")

        display_name = d.pop("displayName", UNSET)

        _params = d.pop("params", UNSET)
        params: OrderPlaceInputParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = OrderPlaceInputParams.from_dict(_params)

        _feature_collection = d.pop("featureCollection", UNSET)
        feature_collection: OrderPlaceInputFeaturecollection | Unset
        if isinstance(_feature_collection, Unset):
            feature_collection = UNSET
        else:
            feature_collection = OrderPlaceInputFeaturecollection.from_dict(_feature_collection)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        order_place_input = cls(
            workspace_id=workspace_id,
            data_product=data_product,
            display_name=display_name,
            params=params,
            feature_collection=feature_collection,
            tags=tags,
        )

        order_place_input.additional_properties = d
        return order_place_input

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
