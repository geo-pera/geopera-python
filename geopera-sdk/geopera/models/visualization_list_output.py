from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.visualization_spec import VisualizationSpec


T = TypeVar("T", bound="VisualizationListOutput")


@_attrs_define
class VisualizationListOutput:
    """
    Attributes:
        visualizations (list[VisualizationSpec] | Unset):
        default_id (str | Unset):  Default: ''.
    """

    visualizations: list[VisualizationSpec] | Unset = UNSET
    default_id: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visualizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.visualizations, Unset):
            visualizations = []
            for visualizations_item_data in self.visualizations:
                visualizations_item = visualizations_item_data.to_dict()
                visualizations.append(visualizations_item)

        default_id = self.default_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if visualizations is not UNSET:
            field_dict["visualizations"] = visualizations
        if default_id is not UNSET:
            field_dict["default_id"] = default_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.visualization_spec import VisualizationSpec

        d = dict(src_dict)
        _visualizations = d.pop("visualizations", UNSET)
        visualizations: list[VisualizationSpec] | Unset = UNSET
        if _visualizations is not UNSET:
            visualizations = []
            for visualizations_item_data in _visualizations:
                visualizations_item = VisualizationSpec.from_dict(visualizations_item_data)

                visualizations.append(visualizations_item)

        default_id = d.pop("default_id", UNSET)

        visualization_list_output = cls(
            visualizations=visualizations,
            default_id=default_id,
        )

        visualization_list_output.additional_properties = d
        return visualization_list_output

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
