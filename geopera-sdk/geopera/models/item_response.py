from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_type import ItemType
from ..models.lifecycle_state import LifecycleState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_response_geometry_type_0 import ItemResponseGeometryType0
    from ..models.item_response_properties import ItemResponseProperties


T = TypeVar("T", bound="ItemResponse")


@_attrs_define
class ItemResponse:
    """Item as returned from the API.

    Attributes:
        id (str):
        project_id (str):
        stac_id (str):
        type_ (ItemType):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        collection_id (None | str | Unset):
        geometry (ItemResponseGeometryType0 | None | Unset):
        bbox (list[float] | None | Unset):
        datetime_ (datetime.datetime | None | Unset):
        start_datetime (datetime.datetime | None | Unset):
        end_datetime (datetime.datetime | None | Unset):
        cloud_cover (float | None | Unset):
        gsd (float | None | Unset):
        description (None | str | Unset):
        properties (ItemResponseProperties | Unset):
        stac_extensions (list[str] | Unset):
        lifecycle_state (LifecycleState | Unset):
        expires_at (datetime.datetime | None | Unset):
        archived_at (datetime.datetime | None | Unset):
        previous_version_id (None | str | Unset):
        duplicated_from_id (None | str | Unset):
        order_id (None | str | Unset):
        upload_id (None | str | Unset):
        job_id (None | str | Unset):
        deleted_at (datetime.datetime | None | Unset):
        created_by (None | str | Unset):
    """

    id: str
    project_id: str
    stac_id: str
    type_: ItemType
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    collection_id: None | str | Unset = UNSET
    geometry: ItemResponseGeometryType0 | None | Unset = UNSET
    bbox: list[float] | None | Unset = UNSET
    datetime_: datetime.datetime | None | Unset = UNSET
    start_datetime: datetime.datetime | None | Unset = UNSET
    end_datetime: datetime.datetime | None | Unset = UNSET
    cloud_cover: float | None | Unset = UNSET
    gsd: float | None | Unset = UNSET
    description: None | str | Unset = UNSET
    properties: ItemResponseProperties | Unset = UNSET
    stac_extensions: list[str] | Unset = UNSET
    lifecycle_state: LifecycleState | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    previous_version_id: None | str | Unset = UNSET
    duplicated_from_id: None | str | Unset = UNSET
    order_id: None | str | Unset = UNSET
    upload_id: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_response_geometry_type_0 import ItemResponseGeometryType0

        id = self.id

        project_id = self.project_id

        stac_id = self.stac_id

        type_ = self.type_.value

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        geometry: dict[str, Any] | None | Unset
        if isinstance(self.geometry, Unset):
            geometry = UNSET
        elif isinstance(self.geometry, ItemResponseGeometryType0):
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
        elif isinstance(self.datetime_, datetime.datetime):
            datetime_ = self.datetime_.isoformat()
        else:
            datetime_ = self.datetime_

        start_datetime: None | str | Unset
        if isinstance(self.start_datetime, Unset):
            start_datetime = UNSET
        elif isinstance(self.start_datetime, datetime.datetime):
            start_datetime = self.start_datetime.isoformat()
        else:
            start_datetime = self.start_datetime

        end_datetime: None | str | Unset
        if isinstance(self.end_datetime, Unset):
            end_datetime = UNSET
        elif isinstance(self.end_datetime, datetime.datetime):
            end_datetime = self.end_datetime.isoformat()
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

        lifecycle_state: str | Unset = UNSET
        if not isinstance(self.lifecycle_state, Unset):
            lifecycle_state = self.lifecycle_state.value

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        previous_version_id: None | str | Unset
        if isinstance(self.previous_version_id, Unset):
            previous_version_id = UNSET
        else:
            previous_version_id = self.previous_version_id

        duplicated_from_id: None | str | Unset
        if isinstance(self.duplicated_from_id, Unset):
            duplicated_from_id = UNSET
        else:
            duplicated_from_id = self.duplicated_from_id

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

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_id": project_id,
                "stac_id": stac_id,
                "type": type_,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
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
        if lifecycle_state is not UNSET:
            field_dict["lifecycle_state"] = lifecycle_state
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if previous_version_id is not UNSET:
            field_dict["previous_version_id"] = previous_version_id
        if duplicated_from_id is not UNSET:
            field_dict["duplicated_from_id"] = duplicated_from_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_response_geometry_type_0 import ItemResponseGeometryType0
        from ..models.item_response_properties import ItemResponseProperties

        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("project_id")

        stac_id = d.pop("stac_id")

        type_ = ItemType(d.pop("type"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_geometry(data: object) -> ItemResponseGeometryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_0 = ItemResponseGeometryType0.from_dict(data)

                return geometry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemResponseGeometryType0 | None | Unset, data)

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

        def _parse_datetime_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datetime_type_0 = datetime.datetime.fromisoformat(data)

                return datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        datetime_ = _parse_datetime_(d.pop("datetime", UNSET))

        def _parse_start_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_datetime_type_0 = datetime.datetime.fromisoformat(data)

                return start_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_datetime = _parse_start_datetime(d.pop("start_datetime", UNSET))

        def _parse_end_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_datetime_type_0 = datetime.datetime.fromisoformat(data)

                return end_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

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
        properties: ItemResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ItemResponseProperties.from_dict(_properties)

        stac_extensions = cast(list[str], d.pop("stac_extensions", UNSET))

        _lifecycle_state = d.pop("lifecycle_state", UNSET)
        lifecycle_state: LifecycleState | Unset
        if isinstance(_lifecycle_state, Unset):
            lifecycle_state = UNSET
        else:
            lifecycle_state = LifecycleState(_lifecycle_state)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_previous_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_version_id = _parse_previous_version_id(d.pop("previous_version_id", UNSET))

        def _parse_duplicated_from_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicated_from_id = _parse_duplicated_from_id(d.pop("duplicated_from_id", UNSET))

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

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        item_response = cls(
            id=id,
            project_id=project_id,
            stac_id=stac_id,
            type_=type_,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            collection_id=collection_id,
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
            lifecycle_state=lifecycle_state,
            expires_at=expires_at,
            archived_at=archived_at,
            previous_version_id=previous_version_id,
            duplicated_from_id=duplicated_from_id,
            order_id=order_id,
            upload_id=upload_id,
            job_id=job_id,
            deleted_at=deleted_at,
            created_by=created_by,
        )

        item_response.additional_properties = d
        return item_response

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
