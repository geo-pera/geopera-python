from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClipDownloadInput")


@_attrs_define
class ClipDownloadInput:
    """
    Attributes:
        job_id (str):
        mosaic_type (str):
        user_agent (None | str | Unset):
        requester_ip (None | str | Unset):
    """

    job_id: str
    mosaic_type: str
    user_agent: None | str | Unset = UNSET
    requester_ip: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        mosaic_type = self.mosaic_type

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        requester_ip: None | str | Unset
        if isinstance(self.requester_ip, Unset):
            requester_ip = UNSET
        else:
            requester_ip = self.requester_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "mosaic_type": mosaic_type,
            }
        )
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if requester_ip is not UNSET:
            field_dict["requester_ip"] = requester_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        mosaic_type = d.pop("mosaic_type")

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        def _parse_requester_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_ip = _parse_requester_ip(d.pop("requester_ip", UNSET))

        clip_download_input = cls(
            job_id=job_id,
            mosaic_type=mosaic_type,
            user_agent=user_agent,
            requester_ip=requester_ip,
        )

        clip_download_input.additional_properties = d
        return clip_download_input

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
