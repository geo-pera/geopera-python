from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lifecycle_state import LifecycleState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_update_input_geometry_type_0 import ItemUpdateInputGeometryType0
    from ..models.item_update_input_properties_type_0 import ItemUpdateInputPropertiesType0


T = TypeVar("T", bound="ItemUpdateInput")


@_attrs_define
class ItemUpdateInput:
    """
    Attributes:
        item_id (str):
        collection_id (None | str | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        geometry (ItemUpdateInputGeometryType0 | None | Unset):
        bbox (list[float] | None | Unset):
        datetime_ (None | str | Unset):
        cloud_cover (float | None | Unset):
        gsd (float | None | Unset):
        properties (ItemUpdateInputPropertiesType0 | None | Unset):
        lifecycle_state (LifecycleState | None | Unset):
    """

    item_id: str
    collection_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    geometry: ItemUpdateInputGeometryType0 | None | Unset = UNSET
    bbox: list[float] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    cloud_cover: float | None | Unset = UNSET
    gsd: float | None | Unset = UNSET
    properties: ItemUpdateInputPropertiesType0 | None | Unset = UNSET
    lifecycle_state: LifecycleState | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_update_input_geometry_type_0 import ItemUpdateInputGeometryType0
        from ..models.item_update_input_properties_type_0 import ItemUpdateInputPropertiesType0

        item_id = self.item_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        geometry: dict[str, Any] | None | Unset
        if isinstance(self.geometry, Unset):
            geometry = UNSET
        elif isinstance(self.geometry, ItemUpdateInputGeometryType0):
            geometry = self.geometry.to_dict()
        else:
            geometry = self.geometry

        bbox: list[float] | None | Unset
        if isinstance(self.bbox, Unset):
            bbox = UNSET
        elif isinstance(self.bbox, list):
            bbox = self.bbox

        else:
            bbox = self.bbox

        datetime_: None | str | Unset
        if isinstance(self.datetime_, Unset):
            datetime_ = UNSET
        else:
            datetime_ = self.datetime_

        cloud_cover: float | None | Unset
        if isinstance(self.cloud_cover, Unset):
            cloud_cover = UNSET
        else:
            cloud_cover = self.cloud_cover

        gsd: float | None | Unset
        if isinstance(self.gsd, Unset):
            gsd = UNSET
        else:
            gsd = self.gsd

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, ItemUpdateInputPropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        lifecycle_state: None | str | Unset
        if isinstance(self.lifecycle_state, Unset):
            lifecycle_state = UNSET
        elif isinstance(self.lifecycle_state, LifecycleState):
            lifecycle_state = self.lifecycle_state.value
        else:
            lifecycle_state = self.lifecycle_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if cloud_cover is not UNSET:
            field_dict["cloud_cover"] = cloud_cover
        if gsd is not UNSET:
            field_dict["gsd"] = gsd
        if properties is not UNSET:
            field_dict["properties"] = properties
        if lifecycle_state is not UNSET:
            field_dict["lifecycle_state"] = lifecycle_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_update_input_geometry_type_0 import ItemUpdateInputGeometryType0
        from ..models.item_update_input_properties_type_0 import ItemUpdateInputPropertiesType0

        d = dict(src_dict)
        item_id = d.pop("item_id")

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_geometry(data: object) -> ItemUpdateInputGeometryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_0 = ItemUpdateInputGeometryType0.from_dict(data)

                return geometry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemUpdateInputGeometryType0 | None | Unset, data)

        geometry = _parse_geometry(d.pop("geometry", UNSET))

        def _parse_bbox(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bbox_type_0 = cast(list[float], data)

                return bbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        bbox = _parse_bbox(d.pop("bbox", UNSET))

        def _parse_datetime_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datetime_ = _parse_datetime_(d.pop("datetime", UNSET))

        def _parse_cloud_cover(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cloud_cover = _parse_cloud_cover(d.pop("cloud_cover", UNSET))

        def _parse_gsd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gsd = _parse_gsd(d.pop("gsd", UNSET))

        def _parse_properties(data: object) -> ItemUpdateInputPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = ItemUpdateInputPropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemUpdateInputPropertiesType0 | None | Unset, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_lifecycle_state(data: object) -> LifecycleState | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_state_type_0 = LifecycleState(data)

                return lifecycle_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LifecycleState | None | Unset, data)

        lifecycle_state = _parse_lifecycle_state(d.pop("lifecycle_state", UNSET))

        item_update_input = cls(
            item_id=item_id,
            collection_id=collection_id,
            name=name,
            description=description,
            geometry=geometry,
            bbox=bbox,
            datetime_=datetime_,
            cloud_cover=cloud_cover,
            gsd=gsd,
            properties=properties,
            lifecycle_state=lifecycle_state,
        )

        item_update_input.additional_properties = d
        return item_update_input

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
