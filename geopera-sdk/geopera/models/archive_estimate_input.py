from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_estimate_input_captures_item import ArchiveEstimateInputCapturesItem


T = TypeVar("T", bound="ArchiveEstimateInput")


@_attrs_define
class ArchiveEstimateInput:
    """
    Attributes:
        captures (list[ArchiveEstimateInputCapturesItem] | Unset):
        split_by_date (bool | None | Unset):  Default: False.
    """

    captures: list[ArchiveEstimateInputCapturesItem] | Unset = UNSET
    split_by_date: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.captures, Unset):
            captures = []
            for captures_item_data in self.captures:
                captures_item = captures_item_data.to_dict()
                captures.append(captures_item)

        split_by_date: bool | None | Unset
        if isinstance(self.split_by_date, Unset):
            split_by_date = UNSET
        else:
            split_by_date = self.split_by_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captures is not UNSET:
            field_dict["captures"] = captures
        if split_by_date is not UNSET:
            field_dict["splitByDate"] = split_by_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_estimate_input_captures_item import ArchiveEstimateInputCapturesItem

        d = dict(src_dict)
        _captures = d.pop("captures", UNSET)
        captures: list[ArchiveEstimateInputCapturesItem] | Unset = UNSET
        if _captures is not UNSET:
            captures = []
            for captures_item_data in _captures:
                captures_item = ArchiveEstimateInputCapturesItem.from_dict(captures_item_data)

                captures.append(captures_item)

        def _parse_split_by_date(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        split_by_date = _parse_split_by_date(d.pop("splitByDate", UNSET))

        archive_estimate_input = cls(
            captures=captures,
            split_by_date=split_by_date,
        )

        archive_estimate_input.additional_properties = d
        return archive_estimate_input

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
