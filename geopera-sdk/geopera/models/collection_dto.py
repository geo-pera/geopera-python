from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_dto_render_params import CollectionDTORenderParams


T = TypeVar("T", bound="CollectionDTO")


@_attrs_define
class CollectionDTO:
    """
    Attributes:
        id (str):
        title (str):
        data_type (str):
        render_strategy (str):
        access_model (str):
        gsd (float | None | Unset):
        render_params (CollectionDTORenderParams | Unset):
    """

    id: str
    title: str
    data_type: str
    render_strategy: str
    access_model: str
    gsd: float | None | Unset = UNSET
    render_params: CollectionDTORenderParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        data_type = self.data_type

        render_strategy = self.render_strategy

        access_model = self.access_model

        gsd: float | None | Unset
        if isinstance(self.gsd, Unset):
            gsd = UNSET
        else:
            gsd = self.gsd

        render_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.render_params, Unset):
            render_params = self.render_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "data_type": data_type,
                "render_strategy": render_strategy,
                "access_model": access_model,
            }
        )
        if gsd is not UNSET:
            field_dict["gsd"] = gsd
        if render_params is not UNSET:
            field_dict["render_params"] = render_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_dto_render_params import CollectionDTORenderParams

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        data_type = d.pop("data_type")

        render_strategy = d.pop("render_strategy")

        access_model = d.pop("access_model")

        def _parse_gsd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gsd = _parse_gsd(d.pop("gsd", UNSET))

        _render_params = d.pop("render_params", UNSET)
        render_params: CollectionDTORenderParams | Unset
        if isinstance(_render_params, Unset):
            render_params = UNSET
        else:
            render_params = CollectionDTORenderParams.from_dict(_render_params)

        collection_dto = cls(
            id=id,
            title=title,
            data_type=data_type,
            render_strategy=render_strategy,
            access_model=access_model,
            gsd=gsd,
            render_params=render_params,
        )

        collection_dto.additional_properties = d
        return collection_dto

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
