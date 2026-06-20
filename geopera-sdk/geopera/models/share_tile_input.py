from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareTileInput")


@_attrs_define
class ShareTileInput:
    """
    Attributes:
        token (str):
        z (int):
        x (int):
        y (int):
        password (str | Unset):  Default: ''.
        format_ (str | Unset):  Default: 'png'.
        profile (None | str | Unset):
    """

    token: str
    z: int
    x: int
    y: int
    password: str | Unset = ""
    format_: str | Unset = "png"
    profile: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        z = self.z

        x = self.x

        y = self.y

        password = self.password

        format_ = self.format_

        profile: None | str | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "z": z,
                "x": x,
                "y": y,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if format_ is not UNSET:
            field_dict["format"] = format_
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        z = d.pop("z")

        x = d.pop("x")

        y = d.pop("y")

        password = d.pop("password", UNSET)

        format_ = d.pop("format", UNSET)

        def _parse_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        share_tile_input = cls(
            token=token,
            z=z,
            x=x,
            y=y,
            password=password,
            format_=format_,
            profile=profile,
        )

        share_tile_input.additional_properties = d
        return share_tile_input

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
