from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feasibility_check_input_featurecollection import FeasibilityCheckInputFeaturecollection
    from ..models.feasibility_check_input_params_type_0 import FeasibilityCheckInputParamsType0


T = TypeVar("T", bound="FeasibilityCheckInput")


@_attrs_define
class FeasibilityCheckInput:
    """
    Attributes:
        data_product (str):
        display_name (None | str | Unset):
        feature_collection (FeasibilityCheckInputFeaturecollection | Unset):
        params (FeasibilityCheckInputParamsType0 | None | Unset):
    """

    data_product: str
    display_name: None | str | Unset = UNSET
    feature_collection: FeasibilityCheckInputFeaturecollection | Unset = UNSET
    params: FeasibilityCheckInputParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feasibility_check_input_params_type_0 import FeasibilityCheckInputParamsType0

        data_product = self.data_product

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        feature_collection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_collection, Unset):
            feature_collection = self.feature_collection.to_dict()

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, FeasibilityCheckInputParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataProduct": data_product,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if feature_collection is not UNSET:
            field_dict["featureCollection"] = feature_collection
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feasibility_check_input_featurecollection import FeasibilityCheckInputFeaturecollection
        from ..models.feasibility_check_input_params_type_0 import FeasibilityCheckInputParamsType0

        d = dict(src_dict)
        data_product = d.pop("dataProduct")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        _feature_collection = d.pop("featureCollection", UNSET)
        feature_collection: FeasibilityCheckInputFeaturecollection | Unset
        if isinstance(_feature_collection, Unset):
            feature_collection = UNSET
        else:
            feature_collection = FeasibilityCheckInputFeaturecollection.from_dict(_feature_collection)

        def _parse_params(data: object) -> FeasibilityCheckInputParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = FeasibilityCheckInputParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeasibilityCheckInputParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        feasibility_check_input = cls(
            data_product=data_product,
            display_name=display_name,
            feature_collection=feature_collection,
            params=params,
        )

        feasibility_check_input.additional_properties = d
        return feasibility_check_input

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
