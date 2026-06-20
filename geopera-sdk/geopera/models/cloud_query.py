from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudQuery")


@_attrs_define
class CloudQuery:
    """provider-shape: `query.cloudCoverage: {GT|GTE|LT|LTE: number}`.

    Attributes:
        gt (float | None | Unset):
        gte (float | None | Unset):
        lt (float | None | Unset):
        lte (float | None | Unset):
    """

    gt: float | None | Unset = UNSET
    gte: float | None | Unset = UNSET
    lt: float | None | Unset = UNSET
    lte: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gt: float | None | Unset
        if isinstance(self.gt, Unset):
            gt = UNSET
        else:
            gt = self.gt

        gte: float | None | Unset
        if isinstance(self.gte, Unset):
            gte = UNSET
        else:
            gte = self.gte

        lt: float | None | Unset
        if isinstance(self.lt, Unset):
            lt = UNSET
        else:
            lt = self.lt

        lte: float | None | Unset
        if isinstance(self.lte, Unset):
            lte = UNSET
        else:
            lte = self.lte

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gt is not UNSET:
            field_dict["GT"] = gt
        if gte is not UNSET:
            field_dict["GTE"] = gte
        if lt is not UNSET:
            field_dict["LT"] = lt
        if lte is not UNSET:
            field_dict["LTE"] = lte

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_gt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gt = _parse_gt(d.pop("GT", UNSET))

        def _parse_gte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gte = _parse_gte(d.pop("GTE", UNSET))

        def _parse_lt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lt = _parse_lt(d.pop("LT", UNSET))

        def _parse_lte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lte = _parse_lte(d.pop("LTE", UNSET))

        cloud_query = cls(
            gt=gt,
            gte=gte,
            lt=lt,
            lte=lte,
        )

        cloud_query.additional_properties = d
        return cloud_query

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
