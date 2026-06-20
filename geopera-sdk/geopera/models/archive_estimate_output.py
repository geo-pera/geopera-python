from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_estimate_output_errors_item import ArchiveEstimateOutputErrorsItem
    from ..models.archive_estimate_output_groups_item import ArchiveEstimateOutputGroupsItem


T = TypeVar("T", bound="ArchiveEstimateOutput")


@_attrs_define
class ArchiveEstimateOutput:
    """
    Attributes:
        groups (list[ArchiveEstimateOutputGroupsItem] | Unset):
        errors (list[ArchiveEstimateOutputErrorsItem] | Unset):
        total_aud (float | Unset):  Default: 0.0.
        total_credits (int | Unset):  Default: 0.
    """

    groups: list[ArchiveEstimateOutputGroupsItem] | Unset = UNSET
    errors: list[ArchiveEstimateOutputErrorsItem] | Unset = UNSET
    total_aud: float | Unset = 0.0
    total_credits: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        total_aud = self.total_aud

        total_credits = self.total_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if errors is not UNSET:
            field_dict["errors"] = errors
        if total_aud is not UNSET:
            field_dict["total_aud"] = total_aud
        if total_credits is not UNSET:
            field_dict["total_credits"] = total_credits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_estimate_output_errors_item import ArchiveEstimateOutputErrorsItem
        from ..models.archive_estimate_output_groups_item import ArchiveEstimateOutputGroupsItem

        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[ArchiveEstimateOutputGroupsItem] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = ArchiveEstimateOutputGroupsItem.from_dict(groups_item_data)

                groups.append(groups_item)

        _errors = d.pop("errors", UNSET)
        errors: list[ArchiveEstimateOutputErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ArchiveEstimateOutputErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        total_aud = d.pop("total_aud", UNSET)

        total_credits = d.pop("total_credits", UNSET)

        archive_estimate_output = cls(
            groups=groups,
            errors=errors,
            total_aud=total_aud,
            total_credits=total_credits,
        )

        archive_estimate_output.additional_properties = d
        return archive_estimate_output

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
