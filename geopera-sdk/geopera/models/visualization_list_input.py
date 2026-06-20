from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.visualization_list_input_band_roles import VisualizationListInputBandRoles
    from ..models.visualization_list_input_render_params import VisualizationListInputRenderParams


T = TypeVar("T", bound="VisualizationListInput")


@_attrs_define
class VisualizationListInput:
    """
    Attributes:
        band_roles (VisualizationListInputBandRoles | Unset):
        data_type (str | Unset):  Default: 'raster'.
        render_params (VisualizationListInputRenderParams | Unset):
        asset (None | str | Unset):
    """

    band_roles: VisualizationListInputBandRoles | Unset = UNSET
    data_type: str | Unset = "raster"
    render_params: VisualizationListInputRenderParams | Unset = UNSET
    asset: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_roles, Unset):
            band_roles = self.band_roles.to_dict()

        data_type = self.data_type

        render_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.render_params, Unset):
            render_params = self.render_params.to_dict()

        asset: None | str | Unset
        if isinstance(self.asset, Unset):
            asset = UNSET
        else:
            asset = self.asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band_roles is not UNSET:
            field_dict["band_roles"] = band_roles
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if render_params is not UNSET:
            field_dict["render_params"] = render_params
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.visualization_list_input_band_roles import VisualizationListInputBandRoles
        from ..models.visualization_list_input_render_params import VisualizationListInputRenderParams

        d = dict(src_dict)
        _band_roles = d.pop("band_roles", UNSET)
        band_roles: VisualizationListInputBandRoles | Unset
        if isinstance(_band_roles, Unset):
            band_roles = UNSET
        else:
            band_roles = VisualizationListInputBandRoles.from_dict(_band_roles)

        data_type = d.pop("data_type", UNSET)

        _render_params = d.pop("render_params", UNSET)
        render_params: VisualizationListInputRenderParams | Unset
        if isinstance(_render_params, Unset):
            render_params = UNSET
        else:
            render_params = VisualizationListInputRenderParams.from_dict(_render_params)

        def _parse_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset = _parse_asset(d.pop("asset", UNSET))

        visualization_list_input = cls(
            band_roles=band_roles,
            data_type=data_type,
            render_params=render_params,
            asset=asset,
        )

        visualization_list_input.additional_properties = d
        return visualization_list_input

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
