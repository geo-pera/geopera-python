from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_type import ItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_create_input_geometry_type_0 import ItemCreateInputGeometryType0
    from ..models.item_create_input_properties import ItemCreateInputProperties


T = TypeVar("T", bound="ItemCreateInput")


@_attrs_define
class ItemCreateInput:
    """
    Attributes:
        type_ (ItemType):
        name (str):
        project_id (str):
        collection_id (None | str | Unset):
        stac_id (None | str | Unset):
        geometry (ItemCreateInputGeometryType0 | None | Unset):
        bbox (list[float] | None | Unset):
        datetime_ (None | str | Unset): ISO 8601 datetime
        start_datetime (None | str | Unset):
        end_datetime (None | str | Unset):
        cloud_cover (float | None | Unset):
        gsd (float | None | Unset):
        description (None | str | Unset):
        properties (ItemCreateInputProperties | Unset):
        stac_extensions (list[str] | Unset):
        order_id (None | str | Unset):
        upload_id (None | str | Unset):
        job_id (None | str | Unset):
    """

    type_: ItemType
    name: str
    project_id: str
    collection_id: None | str | Unset = UNSET
    stac_id: None | str | Unset = UNSET
    geometry: ItemCreateInputGeometryType0 | None | Unset = UNSET
    bbox: list[float] | None | Unset = UNSET
    datetime_: None | str | Unset = UNSET
    start_datetime: None | str | Unset = UNSET
    end_datetime: None | str | Unset = UNSET
    cloud_cover: float | None | Unset = UNSET
    gsd: float | None | Unset = UNSET
    description: None | str | Unset = UNSET
    properties: ItemCreateInputProperties | Unset = UNSET
    stac_extensions: list[str] | Unset = UNSET
    order_id: None | str | Unset = UNSET
    upload_id: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_create_input_geometry_type_0 import ItemCreateInputGeometryType0

        type_ = self.type_.value

        name = self.name

        project_id = self.project_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        stac_id: None | str | Unset
        if isinstance(self.stac_id, Unset):
            stac_id = UNSET
        else:
            stac_id = self.stac_id

        geometry: dict[str, Any] | None | Unset
        if isinstance(self.geometry, Unset):
            geometry = UNSET
        elif isinstance(self.geometry, ItemCreateInputGeometryType0):
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

        start_datetime: None | str | Unset
        if isinstance(self.start_datetime, Unset):
            start_datetime = UNSET
        else:
            start_datetime = self.start_datetime

        end_datetime: None | str | Unset
        if isinstance(self.end_datetime, Unset):
            end_datetime = UNSET
        else:
            end_datetime = self.end_datetime

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        stac_extensions: list[str] | Unset = UNSET
        if not isinstance(self.stac_extensions, Unset):
            stac_extensions = self.stac_extensions

        order_id: None | str | Unset
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        upload_id: None | str | Unset
        if isinstance(self.upload_id, Unset):
            upload_id = UNSET
        else:
            upload_id = self.upload_id

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "project_id": project_id,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if stac_id is not UNSET:
            field_dict["stac_id"] = stac_id
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if start_datetime is not UNSET:
            field_dict["start_datetime"] = start_datetime
        if end_datetime is not UNSET:
            field_dict["end_datetime"] = end_datetime
        if cloud_cover is not UNSET:
            field_dict["cloud_cover"] = cloud_cover
        if gsd is not UNSET:
            field_dict["gsd"] = gsd
        if description is not UNSET:
            field_dict["description"] = description
        if properties is not UNSET:
            field_dict["properties"] = properties
        if stac_extensions is not UNSET:
            field_dict["stac_extensions"] = stac_extensions
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_create_input_geometry_type_0 import ItemCreateInputGeometryType0
        from ..models.item_create_input_properties import ItemCreateInputProperties

        d = dict(src_dict)
        type_ = ItemType(d.pop("type"))

        name = d.pop("name")

        project_id = d.pop("project_id")

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_stac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stac_id = _parse_stac_id(d.pop("stac_id", UNSET))

        def _parse_geometry(data: object) -> ItemCreateInputGeometryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_0 = ItemCreateInputGeometryType0.from_dict(data)

                return geometry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemCreateInputGeometryType0 | None | Unset, data)

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

        def _parse_start_datetime(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_datetime = _parse_start_datetime(d.pop("start_datetime", UNSET))

        def _parse_end_datetime(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_datetime = _parse_end_datetime(d.pop("end_datetime", UNSET))

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: ItemCreateInputProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ItemCreateInputProperties.from_dict(_properties)

        stac_extensions = cast(list[str], d.pop("stac_extensions", UNSET))

        def _parse_order_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_id = _parse_order_id(d.pop("order_id", UNSET))

        def _parse_upload_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_id = _parse_upload_id(d.pop("upload_id", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        item_create_input = cls(
            type_=type_,
            name=name,
            project_id=project_id,
            collection_id=collection_id,
            stac_id=stac_id,
            geometry=geometry,
            bbox=bbox,
            datetime_=datetime_,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            cloud_cover=cloud_cover,
            gsd=gsd,
            description=description,
            properties=properties,
            stac_extensions=stac_extensions,
            order_id=order_id,
            upload_id=upload_id,
            job_id=job_id,
        )

        item_create_input.additional_properties = d
        return item_create_input

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
