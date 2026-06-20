from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.share_link_validate_output_target import ShareLinkValidateOutputTarget


T = TypeVar("T", bound="ShareLinkValidateOutput")


@_attrs_define
class ShareLinkValidateOutput:
    """
    Attributes:
        permission (str):
        target_type (str):
        target (ShareLinkValidateOutputTarget):
    """

    permission: str
    target_type: str
    target: ShareLinkValidateOutputTarget
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission = self.permission

        target_type = self.target_type

        target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permission": permission,
                "target_type": target_type,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_link_validate_output_target import ShareLinkValidateOutputTarget

        d = dict(src_dict)
        permission = d.pop("permission")

        target_type = d.pop("target_type")

        target = ShareLinkValidateOutputTarget.from_dict(d.pop("target"))

        share_link_validate_output = cls(
            permission=permission,
            target_type=target_type,
            target=target,
        )

        share_link_validate_output.additional_properties = d
        return share_link_validate_output

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
