from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.visualization_spec_kind import VisualizationSpecKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="VisualizationSpec")


@_attrs_define
class VisualizationSpec:
    """
    Attributes:
        id (str):
        label (str):
        kind (VisualizationSpecKind):
        asset (None | str | Unset):
        bands (list[int] | None | Unset):
        expression (None | str | Unset):
        colormap (None | str | Unset):
        rescale (None | str | Unset):
        is_default (bool | Unset):  Default: False.
        category (None | str | Unset):
        description (str | Unset):  Default: ''.
    """

    id: str
    label: str
    kind: VisualizationSpecKind
    asset: None | str | Unset = UNSET
    bands: list[int] | None | Unset = UNSET
    expression: None | str | Unset = UNSET
    colormap: None | str | Unset = UNSET
    rescale: None | str | Unset = UNSET
    is_default: bool | Unset = False
    category: None | str | Unset = UNSET
    description: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        kind = self.kind.value

        asset: None | str | Unset
        if isinstance(self.asset, Unset):
            asset = UNSET
        else:
            asset = self.asset

        bands: list[int] | None | Unset
        if isinstance(self.bands, Unset):
            bands = UNSET
        elif isinstance(self.bands, list):
            bands = self.bands

        else:
            bands = self.bands

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        colormap: None | str | Unset
        if isinstance(self.colormap, Unset):
            colormap = UNSET
        else:
            colormap = self.colormap

        rescale: None | str | Unset
        if isinstance(self.rescale, Unset):
            rescale = UNSET
        else:
            rescale = self.rescale

        is_default = self.is_default

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "kind": kind,
            }
        )
        if asset is not UNSET:
            field_dict["asset"] = asset
        if bands is not UNSET:
            field_dict["bands"] = bands
        if expression is not UNSET:
            field_dict["expression"] = expression
        if colormap is not UNSET:
            field_dict["colormap"] = colormap
        if rescale is not UNSET:
            field_dict["rescale"] = rescale
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        kind = VisualizationSpecKind(d.pop("kind"))

        def _parse_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset = _parse_asset(d.pop("asset", UNSET))

        def _parse_bands(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bands_type_0 = cast(list[int], data)

                return bands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        bands = _parse_bands(d.pop("bands", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_colormap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        colormap = _parse_colormap(d.pop("colormap", UNSET))

        def _parse_rescale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rescale = _parse_rescale(d.pop("rescale", UNSET))

        is_default = d.pop("is_default", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        description = d.pop("description", UNSET)

        visualization_spec = cls(
            id=id,
            label=label,
            kind=kind,
            asset=asset,
            bands=bands,
            expression=expression,
            colormap=colormap,
            rescale=rescale,
            is_default=is_default,
            category=category,
            description=description,
        )

        visualization_spec.additional_properties = d
        return visualization_spec

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
