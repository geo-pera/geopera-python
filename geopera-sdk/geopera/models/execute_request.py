from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execute_request_params import ExecuteRequestParams


T = TypeVar("T", bound="ExecuteRequest")


@_attrs_define
class ExecuteRequest:
    """Request to execute a registered analytics operation.

    Attributes:
        operation (str): Name of the registered operation
        params (ExecuteRequestParams): Operation-specific parameters
    """

    operation: str
    params: ExecuteRequestParams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_request_params import ExecuteRequestParams

        d = dict(src_dict)
        operation = d.pop("operation")

        params = ExecuteRequestParams.from_dict(d.pop("params"))

        execute_request = cls(
            operation=operation,
            params=params,
        )

        execute_request.additional_properties = d
        return execute_request

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
